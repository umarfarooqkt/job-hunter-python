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
import schedule
import time
from database_manager import Database

log_to_file = False

#https://realpython.com/python-logging/
if  log_to_file:
   logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
   print("The logs are logged in app.log")
else:
    logging.basicConfig(level=1, format='%(name)s - %(levelname)s - %(message)s')
    logging.info('This will get logged to terminal')

#Global Variables
SUCCESS_STATUS = 200
GITHUB_URI = "https://jobs.github.com/positions.json?"
PAGES = 6
DB = Database()
SESSION = DB.get_session()

def get_connection(url: str, method: str, **kargs) -> bytes:
    """
    This method creates an Http client and makes a
    call based on the method specified
    (**kargs) -> lets the user of the method pass a args to the method
    for more on this method go through this documentation
    https://urllib3.readthedocs.io/en/latest/user-guide.html
    :param url: uri resource
    :param method: method to call on resource GET | POST etc
    :param kargs: any other configurations for the connection
    :return Response: Response to the call
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

def add_to_database(job_list: list, db: Database, session):
    """
    This method adds each job to the database
    :param job_list: list of dictionaries
    :param db: database manager
    :param session: database session
    :return: void
    """
    for i in job_list:
        db.add_job(i['id'], i['title'], i['url'], \
        i['created_at'], i['location'], i['description'], \
        i['company'], i['type'])
        session.commit()

def runner():
    """
    This is a scheduled runner for getting new jobs
    :return: void
    """
    try:
        for i in range(PAGES):
            respond = json.loads(get_connection(GITHUB_URI + "page=" + str(i), "GET"))
            add_to_database(respond, DB, SESSION)
    except Exception as e:
        logging.debug("Attempting rollback")
        SESSION.rollback()
        raise Exception(e)

if __name__ == "__main__":
    logging.info("Starting the data miner module")
    try:
        job_list = DB.get_all_jobs_with()
        if len(job_list) < 10:
            runner()
        schedule.every().day.at("01:00").do(runner, 'It is 01:00')
        while True:
            schedule.run_pending()
            time.sleep(60)  # wait one minute
    except Exception as e:
        logging.exception(str(e))
    # <class 'list'> dict_keys(['id', 'type', 'url', 'created_at', 'company', 'company_url', 'location', 'title', 'description', 'how_to_apply', 'company_logo'])
