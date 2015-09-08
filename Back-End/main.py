__author__ = 'Dulguun'

import schedule
import time
import logging
from pymongo import MongoClient

from Parser.Parser import myParser
from Database.DBManager import write_to_db
from Database.DBManager import retrieve_documents
from Server.Server import push_to_server
from Server.Server import receive_and_check

#CONSTANTS
NUM_OF_DOCUMENTS = 10
SOURCES = {"GoGo Мэдээ", "iKon.mn - Шинэ мэдээ"}

logging.basicConfig(filename=time.strftime("%Y%m%d")+".log",level=logging.INFO)
db = MongoClient().feedAr

def get_and_push():
    _parser = myParser()
    _parser.parse()

    added_contents = 0
    for feed_entries in _parser.feeds:
        added_contents += write_to_db(feed_entries.entries, feed_entries.feed.title, db)

    logging.info(time.strftime("%H:%M:%S") + " added " + str(added_contents) + " content(s) to database")

    result_by_sources = []

    for source in SOURCES:
        result_by_sources.append(retrieve_documents(NUM_OF_DOCUMENTS, source, db))

    feeds_to_write = receive_and_check(result_by_sources)
    print(feeds_to_write)

    server_response = push_to_server(feeds_to_write)
    logging.info(server_response)

#TODO currently not working
def log_file_changer():
    file_name = time.strftime("%Y%m%d")+".log"
    file_handler = logging.FileHandler(file_name, 'a')

    log = logging.getLogger()  # root logger
    for handler in log.handlers:  # remove all old handlers
        log.removeHandler(handler)
    log.addHandler(file_handler)      # set the new handler

get_and_push()
log_file_changer()
schedule.every(1).minutes.do(get_and_push)
#schedule.every().day.at("00:00").do(log_file_changer)

while True:
    schedule.run_pending()
    time.sleep(1)
