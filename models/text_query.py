#!/usr/bin/python3
""" This Module Implemnts a Base Text Query Object """
from models.base_query import BaseQuery
import uuid


class TextQuery(BaseQuery):
    """ This Class represents the base text query sent by user for
        sentiment analysis
    """
    def __init__(self, text_input, user):
        super().__init__()
        
        self.text_input = text_input # Text string received from user
        self.text_queryID = str(uuid.uuid4()) # The unique id for each query
        