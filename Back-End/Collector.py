#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import feedparser
import time

from time import strftime

from Database.DBManager import DBManager

TIME_FORMAT = '%Y%m%d%H%M%S'

class Collector(object):
    """
        Python Class for connecting  with MySQL server and accelerate development project using MySQL
        Extremely easy to learn and use, friendly construction.
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
             cls.__instance = super(Collector, cls).__new__(cls,*args,**kwargs)
        return cls.__instance

    def collect(self, db_manager):
        source_urls = db_manager.select('Sources', None, 'url')

        for url in source_urls:
            feeds = feedparser.parse(url)

            values = []
            keys = ['title',
                    'summary',
                    'url',
                    'retrieve_time',
                    'content_time']

            for feed in feeds['entries']:
                sql_query = 'SELECT idContent ' \
                            'FROM Contents C ' \
                            'WHERE C.title = %s AND C.summary = %s AND C.url = %s'

                result = db_manager.select_advanced(sql_query,
                                                    ('title', feed.title),
                                                    ('summary', feed.summary),
                                                    ('url', feed.link))

                if not result:
                    print 'Adding ' + feed.link

                    _content_time = time.strftime(TIME_FORMAT)
                    if hasattr(feed, 'published'):
                        _content_time = feed.published_parsed
                    elif hasattr(feed, 'created'):
                        _content_time = feed.created_parsed
                    elif hasattr(feed, 'updated'):
                        _content_time = feed.updated_parsed

                    try:
                        _content_time = time.strftime(TIME_FORMAT, _content_time)
                    except:
                        print 'Time conversion error'
                        print _content_time

                    values.append((feed.title,
                                   feed.summary,
                                   feed.link,
                                   time.strftime(TIME_FORMAT),
                                   _content_time))
                else:
                    print 'Skipping ' + feed.link

            if len(values) > 0:
                result = db_manager.fast_insert('Contents', keys, values)

                if result >= 0:
                    print 'Successfully inserted %d rows' % len(values)
                else:
                    print 'Insertion failed'
            else:
                print 'Nothing inserted'
