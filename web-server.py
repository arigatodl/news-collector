import os
if os.name == 'nt':
    import win_unicode_console
    win_unicode_console.enable()

import configparser
import json
from datetime import datetime
from datetime import date
from flask import Flask

from Database.DBManager import DBManager


app = Flask(__name__)
app.debug = True

CONFIG_FILE_NAME = "settings.env"

# starting point

config = configparser.ConfigParser()
config.read(CONFIG_FILE_NAME)

config_raw = configparser.RawConfigParser()
config_raw.read(CONFIG_FILE_NAME)

# configuration
HOST_URL = config.get("Web Server", "HOST_URL")

LIMIT_NUMBER = config.get("Web Server", "LIMIT_NUMBER")
TIME_FORMAT = config_raw.get("Common", "TIME_FORMAT")

DB_HOST = config.get("Database", "DB_HOST")
DB_DATABASE = config.get("Database", "DB_DATABASE")
DB_USERNAME = config.get("Database", "DB_USERNAME")
DB_PASSWORD = config.get("Database", "DB_PASSWORD")

db_manager = DBManager(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(TIME_FORMAT)
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/news/<int:news_id>")
def get_news(news_id):
    sql_query = 'SELECT title, summary, url, content_time ' \
                'FROM Contents C ' \
                'WHERE idContent > %s ' \
                'ORDER BY content_time DESC ' \
                'LIMIT ' + LIMIT_NUMBER

    result = db_manager.select_json(sql_query,
                                    ('idContent', news_id))

    print(result)

    return json.dumps(result, cls=DatetimeEncoder)
# end get_news

if __name__ == "__main__":
    app.run()
