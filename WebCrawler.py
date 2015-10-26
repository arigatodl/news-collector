#!/usr/bin/env python
# coding=utf-8


import configparser
import os

from Database.DBManager import DBManager
from Collector import Collector

SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE_NAME = SOURCE_PATH + "/settings.env"

print(CONFIG_FILE_NAME)

# Starting point

config = configparser.ConfigParser()
config.read(CONFIG_FILE_NAME)

config_raw = configparser.RawConfigParser()
config_raw.read(CONFIG_FILE_NAME)

TIME_FORMAT = config_raw.get("Common", "TIME_FORMAT")

DB_HOST = config.get("Database", "DB_HOST")
DB_DATABASE = config.get("Database", "DB_DATABASE")
DB_USERNAME = config.get("Database", "DB_USERNAME")
DB_PASSWORD = config.get("Database", "DB_PASSWORD")

db_manager = DBManager(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

Collector.collect(db_manager, TIME_FORMAT)
