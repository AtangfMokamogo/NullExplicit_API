import datetime
import models
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class BaseClass:
    """ Base class for all classes in the egnine """
    
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self):
        self.created_at = datetime.utcnow()
        
        
    def get_key(self, api_key):
        """ This method checks if the api_key provided is associated with a
            in the database

        Args:
            api_key (str): an Api-Key to check
            
        Returns:
            bool: True if key is available else false
        """
        from models.api_users import APIUsers
        try:
            ApiKey = models.storage.session.query(APIUsers).filter_by(apikey=api_key).first()
            return ApiKey is not None
        
        finally:
            models.storage.session.close()        
        
    def save(self):
        """Adds A new object to storage"""
        
        
        models.storage.new_obj(self)
        models.storage.save_obj()
        
        
    def delete(self):
        """ Remove query from database """
        models.storage.delete_obj(self)