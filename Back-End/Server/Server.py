__author__ = 'Dulguun'

import json
import requests

url = "https://api.myjson.com/bins/17x1m"
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

def push_to_server(data):
    for
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r

# Returns non-duplicated results
def receive_and_check(result_by_sources):
    server_feeds = requests.get(url).json()

    feeds_to_write = []

    for feeds in result_by_sources:
        for feed in feeds:
            if not any(feed == server_feed for server_feed in server_feeds):
                feeds_to_write.append(feed)

    return feeds_to_write