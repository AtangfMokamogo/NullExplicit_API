#!/usr/bin/python3
""" Implements the Users Class """

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

class APIUsers:
    """ This class models an API User Object """
    __tablename__ = 'Users'
    user_id = Column(String(36), primary_key=True)
    username = Column(String(36))
    def __init__(self, username, user_id):
        
        """ The following methods should be defined for the user class
        
                def add_user(self, username, user_id):
                    // add new user to database
                
                def delete_user(self, user_id):
                    // delete user associated with user_id 
                    // from database
                    
                def show_all(self, user_id, class):
                    // show all queries made to the api by user_id
                    // pass the class to distinguish between the calssifiers
                    
        """