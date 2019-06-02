#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This module is for storing all the responses and
help in building modules
"""

CLIENT_ERROR = {
    "Status" : 400,
    "Message" : "Bad request"
}

CLIENT_ERROR_FORBIDDEN = {
    "Status" : 403,
    "Message" : "Request is valid but proper "\
                + "Authorization isn't provided"
}

CLIENT_ERROR_METHOD_NOT_ALLOWED = {
    "Status" : 405,
    "Message" : "Method error: "
}

CLIENT_ERROR_NOT_FOUND = {
    "Status" : 404,
    "Message" : " Resource could not be found "
}

SERVER_ERROR = {
    "Status" : 500,
    "Message" : "Internal Server Error, Sorry more information can't be provided"
}

JOB_LIST_METHODS = ["title", "description", "company", "location", "hours"]