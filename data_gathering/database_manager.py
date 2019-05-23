#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This module is for managing the database connection
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
import logging

log_to_file = False
if  log_to_file:
   logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
   print("The logs are logged in app.log")
else:
    logging.basicConfig(level=1, format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to terminal')

#Globals
MEMORY_DB = 'sqlite:///:memory:'
USER = 'root'
PASSWORD = 'root'
PORT = '5432'
HOST = 'localhost'
P_CONNECTOR = 'postgresql'
MYSQL_CONNECTOR = 'mysql+mysqlconnector'
DB = 'sqlalchemy'
SQL_DB = P_CONNECTOR+'://'+USER+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+ DB

Base = declarative_base()

# ORM this is the class for jobs
class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    created_at = Column(Date)
    location = Column(String)
    description = Column(String)

    def __init__ (self, id, title, url, created_at, location, description):
        self.id = id
        self.title = title
        self.url = url
        self.created_at = created_at
        self.location = location
        self.description = description

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)


class Database():

    engine = create_engine(MEMORY_DB, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    def get_session(self):
        return self.session

    def get_tables(self):
        return self.engine.table_names()

    def get_job(self, id: int):
        """
        This method is to get any
        unique job based on id
        """
        job = self.session.query(Job).get(id)
        return job

    def add_job(self, id: int,  title: str, url: str,\
         created_at: Date, location: str, description: str):
        """
        This is the method to add jobs 
        to the database
        """
        job = Job(id, title, url,\
        created_at, location, \
        description)
        self.session.add(job)