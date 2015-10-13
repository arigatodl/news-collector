#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import feedparser
from Database.DBManager import DBManager

class Collector(object):
    """
        Python Class for connecting  with MySQL server and accelerate development project using MySQL
        Extremely easy to learn and use, friendly construction.
    """

    __instance   = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
             cls.__instance = super(Collector, cls).__new__(cls,*args,**kwargs)
        return cls.__instance

    def collect(self, db_manager):
        source_urls = db_manager.select('Sources', None, 'url')

        for url in source_urls:
            feeds = feedparser.parse(url)

            values = []
            keys = ['title', 'summary', 'url']

            for feed in feeds['entries']:
                sql_query = 'SELECT idContent FROM Contents C WHERE C.title = %s AND C.summary = %s AND C.url = %s'

                result = db_manager.select_advanced(sql_query, ('title', feed.title),('summary', feed.summary),('url', feed.link))

                if not result:
                    print 'Adding ' + feed.link
                    values.append((feed.title, feed.summary, feed.link))
                else:
                    print 'Skipping ' + feed.link

            print len(values)
            print len(keys)
            result = db_manager.fast_insert('Contents', keys, values)

            if result >= 0:
                print 'Successfully inserted'
            else:
                print 'No insertion'
