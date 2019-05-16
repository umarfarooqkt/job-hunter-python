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

#Globals
MEMORY_DB = 'sqlite:///:memory:'
USER = 'root'
PASSWORD = '03224884959'
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

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)


class Database():

    engine = create_engine(MEMORY_DB, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    def create_db(self) -> None:
        """
        This method is intended to 
        create an instance of database
        """
        Base.metadata.create_all(self.engine)

    def get_tables(self):
        return self.engine.table_names()

    def add_job(self, id: int, **kargs):
        """
        This is the method to add jobs 
        to the database
        """
        job = Job(id, kargs["title"], kargs["url"], 
        kargs["created_at"], kargs["location"], 
        kargs["description"])
        self.session.add(job)
    
    #def get_jobs(self,)

# title: str, url: str, created_at: Date, location: str, description: str
db = Database()
print(db.get_tables())