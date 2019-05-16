# /usr/bin/python
# -*- coding: utf-8 -*-

"""
This is the test suit for the database
"""

import os, sys, inspect
import pprint
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
print(currentdir)
print(parentdir)
sys.path.append(parentdir+"/data_gathering")
from database_manager import Database as db
import unittest

class TestDatabase(unittest.TestCase):

    def test_tester(self):
        self.assertEquals(True,True)

if __name__ == "__main__":
    unittest.main()