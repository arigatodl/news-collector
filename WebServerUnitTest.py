#!/usr/bin/env python

from unittest import TestCase
import WebServer

class WebServerUnitTest(TestCase):

    def test_db_query(self):
        try:
            WebServer.get_news(10)
            pass
        except:
            self.fail("Database query failed!")

    def test_flask(self):
        try:
            WebServer.hello()
            pass
        except:
            self.fail("Flask failed!")

if __name__ == '__main__':
    WebServerUnitTest.main()