# /usr/bin/python
# -*- coding: utf-8 -*-

"""
This is the test suit for the database
"""

import os, sys, inspect
import pprint
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# print(currentdir)
# print(parentdir)
sys.path.append(parentdir+"/data_gathering")
from sqlalchemy import create_engine
from database_manager import Database as db
import unittest

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup test suite")
        cls.database_connection = db.engine
        ## monkey patching an in memory database
        db.engine = create_engine('sqlite:///:memory:', echo=True)

    def setUp(self):
        print("setup method")

    def test_tester(self):
        self.assertEqual(True,True)

    def test_thre(self):
        self.assertEqual(True,True)

    def test_two(self):
        self.assertEqual(True,True)

    def tearDown(self):
        print("teardown method")

    @classmethod
    def tearDownClass(cls):
        print("teardown test suite")
        db.engine = cls.database_connection

if __name__ == "__main__":
    unittest.main()