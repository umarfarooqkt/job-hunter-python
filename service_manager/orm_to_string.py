#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This class if for converting the database objects to jsons
"""
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        This Method converts query
        objects to dictionary/json
        :param obj: query object
        :return: dict
        """
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

    def convert_list(self, list_object):
        """
        This method iterates through a list
        of query objects so they can be converted
        :param list_object:
        :return: list of dictionaries
        """
        json_list = []
        for i in list_object:
            json_list.append(self.default(i))
        return json_list