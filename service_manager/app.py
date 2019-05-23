#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This module is for managing the API interface
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Job(Resource):
    def get(self, id):
        return {'new': 'job'}

api.add_resource(Job, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)