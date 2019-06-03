#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
This module is for managing the database connection
"""
import sqlalchemy
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
import logging, os

log_to_file = False
if  log_to_file:
   logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
   print("The logs are logged in app.log")
else:
    logging.basicConfig(level=1, format='%(name)s - %(levelname)s - %(message)s')
    logging.info('This will get logged to terminal')

#Globals
MEMORY_DB = 'sqlite:///:memory:'
USER = 'root'
#USER = 'postgres'
PASSWORD = 'root'
PORT = '5400'
PORT = os.environ["POSTGRES_PORT"]
HOST = 'localhost'
HOST = os.environ["DB_HOST"]
P_CONNECTOR = 'postgresql'
MYSQL_CONNECTOR = 'mysql+mysqlconnector'
DB = 'sqlalchemy'
SQL_DB = P_CONNECTOR+'://'+USER+':'+PASSWORD+'@'+HOST+':'+PORT+'/'
Log = False

Base = declarative_base()

# ORM this is the class for jobs
class Job(Base):
    __tablename__ = 'job'
    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    created_at = Column(Date)
    location = Column(String(255))
    description = Column(String)
    company = Column(String(255))
    hours = Column(String(255)) # type of e.g full time or part time

    def __init__ (self, id, title, url, created_at, location, description, company, hours):
        self.id = id
        self.title = title
        self.url = url
        self.created_at = created_at
        self.location = location
        self.description = description
        self.company = company
        self.hours = hours

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

def create_database(database):
   """
    Create database schema and 
    create relational mapping
   :param database: 
   :return: void
   """
   Base.metadata.create_all(database.engine)

def drop_database(database):
    """
    Drop database
    :param database: database class object
    :return: void
    """
    Job.__table__.drop(database.engine)
    User.__table__.drop(database.engine)

class Database():

    engine = create_engine(SQL_DB, pool_size=10, max_overflow=20, echo=Log)
    Session = sessionmaker(bind=engine)
    session = Session()

    def get_session(self):
        """
        Getter for the session
        :return session: this session
        """
        return self.session

    def get_tables(self):
        """
        This returns list of all tables
        :return list: list of tables
        """
        return self.engine.table_names()

    def get_job_id(self, id: int):
        """
        This method is to get any
        unique job based on id
        :param id: unique identifier
        :return: returns a base object
        """
        job = self.session.query(Job).get(id)
        return job

    def get_job(self, title: str, company: str):
        """
        Getting the jobs for filtering, this is
        to check if similar or the same job for another time
        is added
        :param title:
        :param company:
        :return: return the first job matching
        """
        job = self.session.query(Job).filter(Job.title == title)\
            .filter(Job.company == company).first()
        return job

    def add_job(self, id: String,  title: str, url: str,\
         created_at: Date, location: str, description: str, \
         company: str, hours: str):
        """
        This is the method to add jobs
        to the database
        :param id:
        :param title:
        :param url:
        :param created_at:
        :param location:
        :param description:
        :param company:
        :param hours:
        :return: void
        """
        old_job = self.get_job(title, company)
        if old_job is None:
            job = Job(id, title, url,\
            created_at, location, \
            description, company, hours)
            self.session.add(job)
        else:
            logging.debug("Job already exits, ")

    def get_all_jobs_with(self, **kwargs):
        """
        The main filter for multiple or
        no filters with jobs
        :param kwargs: different filters
        :return: query of the list of jobs
        """
        query = self.session.query(Job)
        if "title" in kwargs and kwargs["title"] != None:
            query = query.filter(Job.title.ilike('%'+kwargs["title"]+'%'))
        if "description" in kwargs and kwargs["description"] != None:
            query = query.filter(Job.description.ilike('%'+kwargs["description"]+'%'))
        if "company" in kwargs and kwargs["company"] != None:
            query = query.filter(Job.company.ilike('%'+kwargs["company"]+'%'))
        if "location" in kwargs and kwargs["location"] != None:
            query = query.filter(Job.location.ilike('%'+kwargs["location"]+'%'))
        if "hours" in kwargs and kwargs["hours"] != None:
            query = query.filter(Job.hours.ilike('%'+kwargs["hours"]+'%'))
        jobs = query.order_by(Job.created_at).all()
        return jobs

    def delete(self, id: int):
        """
        Delete the job with the given id
        :param id: job id\ identifier
        :return: void
        """
        job = self.session.query(Job).get(id)
        self.session.delete(job)