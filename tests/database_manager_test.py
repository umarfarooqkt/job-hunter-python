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
from database_manager import Database as db
import unittest

test_job = {
    "title" : "test_title",
    "url" : "test_url",
    "created_at" : datetime.datetime.now(),
    "location" : "test_location",
    "description" : "test_description",
    "id" : 2345678933
}

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup test suite")
        cls.database_connection = db.engine
        ## monkey patching an in memory database
        db.engine = create_engine('sqlite:///:memory:', echo=True)

    def setUp(self):
        self.db_connection = db()
        print("setup method")

    def test_tester(self):
        self.assertEqual(True,True)

    def test_add_job(self):
        """
        This method tests adding new
        jobs to the database
        """
        self.db_connection.\
        add_job(id=test_job["id"] ,title=test_job["title"], \
            url=test_job["url"], created_at=test_job["created_at"], \
            location=test_job["location"], description=test_job["description"])
        self.db_connection.get_session().commit()
        job  = self.db_connection.get_job(test_job["id"])
        self.assertEqual(job.title,test_job["title"])

    def tearDown(self):
        print("teardown method")

    @classmethod
    def tearDownClass(cls):
        print("teardown test suite")
        db.engine = cls.database_connection

if __name__ == "__main__":
    unittest.main()