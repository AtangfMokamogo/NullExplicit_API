#!/usr/bin/python3
""" The Base Class for all our Query Objects """

import uuid
from datetime import datetime


class BaseQuery:
    def __init__(self, user_id):
        
        # Unique identifier for each query
        self.query_id = str(uuid.uuid4())
        
        # The date and time of each query
        self.created_at = datetime.now()
        
        # Unique id for every user
        # TODO: import the authetication module here
        self.user_id = user_id