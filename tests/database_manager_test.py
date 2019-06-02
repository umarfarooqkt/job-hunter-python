# /usr/bin/python
# -*- coding: utf-8 -*-

"""
This is the test suit for the database
"""

import os, sys, inspect
import pprint
import datetime
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# print(currentdir)
# print(parentdir)
sys.path.append(parentdir+"/data_gathering")
from sqlalchemy import create_engine
import database_manager
import unittest
import random

def get_unique():
    id = str(datetime.datetime.now())
    random_int = random.randint(1, 100000)
    id = id + str(random_int)
    return id

UNIQUE_ID = get_unique()

test_job = {
    "title" : "test_title",
    "url" : "test_url",
    "created_at" : datetime.datetime.now(),
    "location" : "test_location",
    "description" : "test_description",
    "id" : UNIQUE_ID + "1",
    "company" : "test_company",
    "hours" : "test_hours"
}

test_job_2 = {
    "title" : "test_title_2",
    "url" : "test_url_2",
    "created_at" : datetime.datetime.now(),
    "location" : "test_location_2",
    "description" : "test_description_2",
    "id" : UNIQUE_ID + "2",
    "company" : "test_company_2",
    "hours" : "test_hours_2"
}

test_job_3 = {
    "title" : "test_title_3",
    "url" : "test_url_3",
    "created_at" : datetime.datetime.now(),
    "location" : "test_location_3",
    "description" : "test_description_3",
    "id" : UNIQUE_ID + "3",
    "company" : "test_company_3",
    "hours" : "test_hours_3"
}

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup test suite")
        # cls.database_connection = db.engine
        # ## monkey patching an in memory database
        # db.engine = create_engine('sqlite:///:memory:', echo=True)
        #second attempt
        # cls.database = database_manager.SQL_DB
        # database_manager.SQL_DB = 'sqlite:///:memory:'

    def setUp(self):
        self.db_connection = database_manager.Database()
        self.count_jobs = 2
        self.db_connection.add_job(id=test_job_2["id"] ,title=test_job_2["title"], \
            url=test_job_2["url"], created_at=test_job_2["created_at"], \
            location=test_job_2["location"], description=test_job_2["description"], \
            company=test_job_2["company"], hours=test_job_2["hours"])
        self.db_connection.add_job(id=test_job_3["id"], title=test_job_3["title"], \
             url=test_job_2["url"], created_at=test_job_2["created_at"], \
             location=test_job_3["location"], description=test_job_3["description"], \
             company=test_job_3["company"], hours=test_job_3["hours"])
        print("setup method")

    def test_add_job(self):
        """
        This method tests adding new
        jobs to the database
        :return: void
        """
        self.db_connection.\
        add_job(id=test_job["id"] ,title=test_job["title"], \
            url=test_job["url"], created_at=test_job["created_at"], \
            location=test_job["location"], description=test_job["description"], \
            company=test_job["company"], hours=test_job["hours"])
        job  = self.db_connection.get_job_id(test_job["id"])
        self.assertEqual(job.title,test_job["title"])

    def test_all_jobs_with_complete_match(self):
        """
        Test for the filters and
        see if the exact match is found for all
        the filters together
        :return: void
        """
        jobs = self.db_connection.get_all_jobs_with(title=test_job_2["title"],\
            description=test_job_2["description"], company=test_job_2["company"],\
            location=test_job_2["location"], hours=test_job_2["hours"])
        self.assertEqual(jobs[0].title,test_job_2["title"])
        self.assertEqual(jobs[0].company, test_job_2["company"])
        self.assertEqual(jobs[0].location, test_job_2["location"])
        # there shouldn't be a second job
        self.assertLess(len(jobs), self.count_jobs)
        self.assertEqual(len(jobs), 1)

    def test_all_jobs_with_nothing(self):
        """
        This test is for checking if the
        function will return all the jobs
        Unfiltered
        :return: void
        """
        jobs = self.db_connection.get_all_jobs_with()
        self.assertNotEqual(jobs[0].title, test_job["title"])
        self.assertNotEqual(jobs[0].company, test_job["company"])
        self.assertNotEqual(jobs[0].title, test_job_2["title"])
        self.assertNotEqual(jobs[0].company, test_job_2["company"])
        self.assertNotEqual(jobs[0].title, test_job_3["title"])
        self.assertNotEqual(jobs[0].company, test_job_3["company"])

    def test__all_jobs_with_kind_of_match(self):
        """
        This method tests if partial matches
        to the jobs works
        :return: void
        """
        jobs = self.db_connection.get_all_jobs_with(company="test_c")
        # This depends on the num of jobs added for testing
        self.assertEqual(len(jobs), self.count_jobs)

    def tearDown(self):
        self.db_connection.get_session().rollback()
        print("teardown method")

    @classmethod
    def tearDownClass(cls):
        print("teardown test suite")
        #db.engine = cls.database_connection
        #second attempt
        #database_manager.SQL_DB = cls.database

if __name__ == "__main__":
    unittest.main()