#!/usr/bin/env python
# coding=utf-8


import configparser

from Database.DBManager import DBManager
from Collector import Collector


CONFIG_FILE_NAME = ".env"

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
