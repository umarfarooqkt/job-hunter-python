#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
This module is for gather job listings
the listings are gathered using opne source api's
"""

#import urllib.request
import urllib3
import certifi
import logging
import json

log_to_file = False

#https://realpython.com/python-logging/
if  log_to_file:
   logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
   print("The logs are logged in app.log")
else:
    logging.basicConfig(level=1, format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to terminal')

#Global Variables
SUCCESS_STATUS = 200
GITHUB_URI = "https://jobs.github.com/positions.json?"

def get_connection(url: str, method: str, **kargs) -> bytes:
    """
    This method creates an Http client and makes a
    call based on the method specified
    (**kargs) -> lets the user of the method pass a args to the method
    for more on this method go through this documentation
    https://urllib3.readthedocs.io/en/latest/user-guide.html
    """
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    try:
        request = http.request(method ,url, kargs)
        if request.status != SUCCESS_STATUS:
            raise Exception("The request was not success full: \n",request.status)
    except Exception as e:
        logging.exception(str(e))
        raise e
    return request.data

if __name__ == "__main__":
    logging.info("Starting the data miner module")
    resp = json.loads(get_connection(GITHUB_URI, "GET"))
    list1 = []
    for i in resp:
        if "skill" not in i['description']:
            list1.append(i['description'])
    print(len(resp),len(list1))
    print(resp[0]['created_at'])
    #print(resp.keys())
    #print(get_connection("https://jobs.github.com/positions.json?", "GET", fields=None))