#!/usr/bin/python3
""" This Module Implemnts a Base Text Query Object """
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.engines.database_storage import DBStorage
#from models.api_users import APIUsers



Base = declarative_base()


class APIUsers(Base):
    """ This class models an API User Object """
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80))
    api_key = Column(String(100))

    
    def __init__(self, username):
        self.username = username
        
        """ The following methods should be defined for the user class """
        
    def add_user(self):
        """add new user to database"""
        self.api_key = str(uuid.uuid4())
        
        storage = DBStorage()
        storage.reload_database()
        
        # create new object
        storage.new_query(self)
        
        # save object to database
        storage.save_to_db()
        
        return self.api_key
        
    
    def delete_user(self, user_id):
        """ delete user associated with user_id """
        # from database
        
    def query_api_key(self, api_key) -> bool:
        """This Method retrieves an api key from database

        Args:
            api_key (str): This is the API key to retrieve from database

        Returns:
            bool: True if key is present else False
        """
        
        
class TextQuery(Base):
    """ This Class represents the base text query sent by user for
        sentiment analysis
    """
    __tablename__ = 'TextQueries'
    user_id = Column(String(100))
    text_input = Column(Text)
    analysis_score = Column(String())
    created_at = Column(DateTime, default=datetime.utcnow)
    query_number = Column(Integer, primary_key=True, autoincrement=True)
    
    def __init__(self, api_key, text_input, classification_result):
        self.user_id = api_key
        self.text_input = text_input
        self.analysis_score = classification_result
        

        
    def save(self):
        """ Saves object instance to database """
        
        storage = DBStorage()
        storage.reload_database()
        
        # create new object
        storage.new_query(self)
        
        # save object to database
        storage.save_to_db()
        
        
    def delete(self):
        """ delete instance of object from database"""
        from models.engines.database_storage import DBStorage
        DBStorage.delete_from_db(self)