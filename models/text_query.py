#!/usr/bin/python3
""" This Module Implemnts a Base Text Query Object """
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

#from models.api_users import APIUsers



Base = declarative_base()

class TextQuery(Base):
    """ This Class represents the base text query sent by user for
        sentiment analysis
    """
    __tablename__ = 'TextQueries'
    user_id = Column(String(36))
    query_id = Column(Integer, primary_key=True)
    text_input = Column(Text)
    analysis_score = Column(String(36))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    
    # methods that deal with sending and reloading info from databse
    def save(self):
        from models.engines.database_storage import DBStorage
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