#!/usr/bin/python3
""" Implements database storage module """

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

import models


class DBStorage():
    """ controls MySQL database transactions """
    __engine = None
    __session = None
    
    def __init__(self):
        """ initialise the database storage object """
        
        NULL_X_MYSQL_USER = os.environ.get('NULL_EXPLICIT_MYSQL_USER')
        NULL_X_MYSQL_PWD = os.environ.get('NULL_EXPLICIT_MYSQL_PASSWORD')
        NULL_X_MYSQL_HOST = os.environ.get('NULL_EXPLICIT_MYSQL_HOST')
        NULL_X_MYSQL_DATABASE = os.environ.get('NULL_EXPLICIT_MYSQL_DATABASE')
        NULL_X_ENVIRONMENT = os.environ.get('NULL_EXPLICIT_ENVIRONMENT')
        
        print(NULL_X_MYSQL_DATABASE)
        
        
        connection_string = f"mysql+pymysql://{NULL_X_MYSQL_USER}:{NULL_X_MYSQL_PWD}@{NULL_X_MYSQL_HOST}/{NULL_X_MYSQL_DATABASE}"

        # create the engine to use for communicating with the database
        self.__engine = create_engine(connection_string)
        
        if NULL_X_ENVIRONMENT == "test":
            Base.metadata.drop_all(self.__engine)
            
    def get_user_by_api_key(self, api_key):
        """ Retrieves a user from the database based on the API key

        Args:
            api_key (str): API key of the user

        Returns:
            APIUsers: User object if found, None otherwise
        """
        from models.text_query import APIUsers
        
        user = self.__session.query(APIUsers).filter_by(api_key=api_key).first()
        return user

    def all_queries(self, query_object=None):
        """Get all entries of object in current database session 

        Args:
            query_object (class, optional): this is the object instance to count in storage.
            Defaults to None since only one class is stored.

        Returns:
            string: a list of all available object in storage
        """
        if query_object is None or type(query_object).__name__ == 'TextQuery':
            objs = self.__session.query(query_object).all()
        return objs
    
    def new_query(self, query_object):
        """ Adds the object to the current database session

        Args:
            query_object (class): The ImageQuery object to add to database
        """
        self.__session.add(query_object)
    
    
    def save_to_db(self):
        """ Commits all changes of the databse session  """
        self.__session.commit()
        print("Successfully saved to Database: NullExplicit")
    
    
    def delete_from_db(self, object_query=None):
        """ Deletes an object from the current database section

        Args:
            object_query (class, optional): ImageQuery object. Defaults to None.
        """
        self.__session.delete(object_query) if object_query is not None else None
        
        
    def reload_database(self):
        """ updates the session object used for interacting with the database """
        from models.text_query import Base, APIUsers
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
        
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()