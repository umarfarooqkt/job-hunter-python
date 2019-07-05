# /usr/bin/python
# -*- coding: utf-8 -*-

"""
This module is for testing the data miner
"""

import os, sys, inspect
import pprint
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# print(currentdir)
# print(parentdir)
sys.path.append(parentdir+"/data_gathering")
import data_miner
import unittest
import json

class TestDataMiner(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup test suite")

    def setUp(self):
        print("setup method")

    def test_http_client_connection(self):
        """
        This test ensure that the client is able to connect
        """
        uri = "google.com"
        response = data_miner.get_connection(uri, "GET")
        self.assertTrue("<title>Google</title>" in str(response))

    def tearDown(self):
        print("teardown method")

    @classmethod
    def tearDownClass(cls):
        print("teardown test suite")

if __name__ == "__main__":
    unittest.main()