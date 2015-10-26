"""
    Web server
    Processes rest api requests and sends the response back
"""

import configparser
import os
from flask import Flask

from Database.DBManager import DBManager


app = Flask(__name__)
app.debug = True

SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE_NAME = SOURCE_PATH + "/settings.env"

"""
    STARTING POINT
"""

config = configparser.ConfigParser()
config.read(CONFIG_FILE_NAME)

config_raw = configparser.RawConfigParser()
config_raw.read(CONFIG_FILE_NAME)

"""
    CONFIGURATION
"""
HOST_URL = config.get("Web Server", "HOST_URL")

LIMIT_NUMBER = config.get("Web Server", "LIMIT_NUMBER")
#TIME_FORMAT = config_raw.get("Common", "TIME_FORMAT")

DB_HOST = config.get("Database", "DB_HOST")
DB_DATABASE = config.get("Database", "DB_DATABASE")
DB_USERNAME = config.get("Database", "DB_USERNAME")
DB_PASSWORD = config.get("Database", "DB_PASSWORD")

db_manager = DBManager(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

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

    result = db_manager.select_raw_json(sql_query,
                                        ('idContent', news_id))

    return result
# end get_news

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)  # Listen on all public IPs.
