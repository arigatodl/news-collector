__author__ = 'Dulguun'

import pymongo

from pymongo import MongoClient

def write_to_db(feeds, source, db):

    addedContents = 0
    for entry in feeds:
        data = {}
        data['title'] = entry.title
        data['description'] = entry.description
        data['link'] = entry.link
        data['date'] = entry.published
        if (db[source].find_one(data) == None):
            db[source].insert(data)
            addedContents += 1

        return addedContents

def retrieve_documents(num_of_docs, source, db):
    return db[source].find().sort("date", -1).limit(num_of_docs)