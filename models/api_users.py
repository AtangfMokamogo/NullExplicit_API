import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from models.base_query import Base, BaseClass



class APIUsers(Base, BaseClass):
    """ Represents a User Object """
    
    __tablename__= 'APIUsers'
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    apikey = Column(String)
    queries = relationship("TextQuery", back_populates="user")
    
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.apikey = str(uuid.uuid4())
        
    
    def save_query(self):
        """ Saves a new user to database
        Args:
            object (str): the user object to save to database
        """

        try:
            models.storage.session.add(self)
            models.storage.session.commit()
            
            return self.apikey
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.close()
    
    
    def confirm_key(self, api_key):
        """ This method checks if the api_key provided is associated with a
            in the database

        Args:
            api_key (str): an Api-Key to check
            
        Returns:
            bool: True if key is available else false
        """
        
        try:
            ApiKey = models.storage.session.query(APIUsers).filter_by(apikey=api_key).first()
            return ApiKey is not None
        
        finally:
            models.storage.session.close()
    
    
    def remove_user(self, username, api_key):
        """ This method removes a username associated with api_key

        Args:
            username (str): The username to remove from string
            api_key (str): The Api-Key associated with username
        
        Returns:
            string: "User Deleted" if username is present or
                    "The <username> Associated with <api_key> is not available"
        """
        
        try:
            user = models.storage.session.query(APIUsers).filter_by(username=username, apikey=api_key).first()
            
            if user:
                models.storage.session.delete(user)
                models.storage.session.commit()
                
                return "User Deleted"
            else:
                return "User Not Found"
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.close()
            
    
    
    def update_key(self, username, O_api_key, N_api_key):
        """ This method updates a users Api-Key in the database

        Args:
            username (str): The username to update the key for
            O_api_key (str): The Old Api-Key
            N_api_key (str): The New Api-Key
            
        Returns:
            string: "Updated" if <username> associated with <O_api_key>
                    is present else "Your username does not match the old
                    api-key: key update failed"
        """
        
        try:
            user = models.storage.session.query(APIUsers).filter_by(username=username, api_key=O_api_key).first()
            
            if user:
                user.apikey = N_api_key
                models.storage.session.commit()
                return "Api-Key Updated Succefully!"
            
            else:
                return "Username: {} provided is not associated With key: {}".format(username, O_api_key)
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.commit()
    
    