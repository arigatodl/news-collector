#!/usr/bin/env python

from unittest import TestCase
import WebCrawler

class WebCrawlerUnitTest(TestCase):

    def test_crawler(self):
        try:
            WebCrawler.main()
            pass
        except:
            self.fail("Crawler failed!")


if __name__ == '__main__':
    WebCrawlerUnitTest.main()