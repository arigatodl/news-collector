__author__ = 'Dulguun'

import ConfigParser

from Database.DBManager import DBManager

CONFIG_FILE_NAME = ".env"

config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE_NAME)

_db_host = config.get("Database", "DB_HOST")
_db_database = config.get("Database", "DB_DATABASE")
_db_username = config.get("Database", "DB_USERNAME")
_db_password = config.get("Database", "DB_PASSWORD")

db_manager = DBManager(_db_host, _db_username, _db_password, _db_database)

print db_manager.select()
