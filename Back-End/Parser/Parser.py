__author__ = 'Dulguun'

import feedparser

class myParser:

    def __init__(self):
        self.feeds = []

    def parse(self):
        # GOGO MN
        self.feeds.append(feedparser.parse('http://news.gogo.mn/feed'))

        # IKON MN
        self.feeds.append(feedparser.parse('http://www.ikon.mn/rss'))