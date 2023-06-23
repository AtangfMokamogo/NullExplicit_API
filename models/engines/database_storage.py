#!/usr/bin/python3
""" Implements database storage module """

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

import models
from models.text_query import Base, TextQuery
# from models.api_users import APIUsers


class DBStorage():
    """ controls MySQL database transactions """
    __engine = None
    __session = None
    
    def __init__(self):
        """ initialise the database storage object """
        
        #NULL_X_MYSQL_USER = getenv('NULL_EXPLICIT_MYSQL_USER')
        #NULL_X_MYSQL_PWD = getenv('NULL_EXPLICIT_MYSQL_PASSWORD')
        #NULL_X_MYSQL_HOST = getenv('NULL_EXPLICIT_MYSQL_HOST')
        #NULL_X_MYSQL_DATABASE = getenv('NULL_EXPLICIT_MYSQL_DATABASE')
        NULL_X_ENVIRONMENT = getenv('NULL_EXPLICIT_ENVIRONMENT')
        
        # create the engine to use for communicating with the database
        self.__engine = create_engine('mysql+mysqldb://NULL_X_USER:NULL_X_USER@localhost:3306/NullExplicit')
        
        # check environment srcipt is run on
        if NULL_X_ENVIRONMENT == "test":
            Base.metadata.drop_all(self.__engine)
            
    # define a method that retrieves all instances of a class from the databse
    def all_queries(self, query_object=None):
        """ Get all entries of object in current database session """
        if query_object is None or type(query_object).__name__ == 'TextQuery':
            objs = self.__session.query(query_object).all()
        return objs
    
    def new_query(self, query_object):
        """ adds the object to the current database session """
        self.__session.add(query_object)
    
    def save_to_db(self):
        """ Commits all changes of the databse session """
        self.__session.commit()
    
    def delete_from_db(self, object_query=None):
        """ Deletes object from current database session
            if object_query is not none
        """
        self.__session.delete(object_query) if object_query is not None else None
        
    def reload_database(self):
        """ updates the session object used for interacting with the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
        
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()