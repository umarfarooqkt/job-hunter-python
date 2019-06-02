#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This module is for managing the API interface
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import helper_res_module as get_response
from orm_to_string import AlchemyEncoder
import os, json, inspect, sys, logging
if "DOCKER_ENV" in  os.environ:
    from database_manager import Database
else:
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir+"/data_gathering")
    from database_manager import Database

log_to_file = False
if  log_to_file:
   logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
   print("The logs are logged in app.log")
else:
    logging.basicConfig(level=1, format='%(name)s - %(levelname)s - %(message)s')
    logging.info('This will get logged to terminal')

DB = Database()

app = Flask(__name__)
api = Api(app)

class Job(Resource):
    def get(self, id):
        return {'new': 'job'}

class JobList(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title")
        self.parser.add_argument("company")
        self.parser.add_argument("description")
        self.parser.add_argument("location")
        self.parser.add_argument("hours")

    def get(self):
        response = get_response.SERVER_ERROR
        args = self.parser.parse_args()
        try:
            print("arguments passed are = ",args.keys())
            jobs = DB.get_all_jobs_with(title=args["title"],
                                        company=args["company"],
                                        description=args["description"],
                                        location=args["location"],
                                        hours=args["hours"])
            response = AlchemyEncoder().convert_list(jobs)
        except Exception as e:
            logging.exception(str(e))
        return response

    def post(self):
        return get_response.CLIENT_ERROR_METHOD_NOT_ALLOWED

    def put(self):
        return get_response.CLIENT_ERROR_METHOD_NOT_ALLOWED

    def delete(self):
        return get_response.CLIENT_ERROR_METHOD_NOT_ALLOWED


api.add_resource(Job, '/job/<string:id>')
api.add_resource(JobList, '/joblist')

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db.remove()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()