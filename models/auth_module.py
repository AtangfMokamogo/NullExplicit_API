#!/usr/bin/python3
""" Module that implements authentication for our flask api """

from flask_restful import reqparse
from models.text_query import APIUsers
from models.engines.database_storage import DBStorage


def authenticate(func):
    """This function authenticates requests with API-KEYS against
        issued API-KEYS

    Args:
        func (func): A flask URL resource to provide authentication for
    """ 
    
    def wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('API-Key', location='headers', required=True)
        args = parser.parse_args()
        
        # Check if the API Key provided is present for a user in database
        storage = DBStorage()
        storage.reload_database()

        api_key = api_key=args['API-Key']
        user = storage.get_user_by_api_key(api_key)
        if user:
            return func(*args, **kwargs)
        else:
            return {'message': 'Authentication failed. Please request login access from Developer'}, 401
    return wrapper