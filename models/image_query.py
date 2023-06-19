#!/usr/bin/python3
""" This Module implements a Base Image Query object """
import uuid
from models.base_query import BaseQuery

class ImageQuery(BaseQuery):
    """ A reresentation of an image query object """
    def __init__(self, image_file, user_id, classification_results):
        super().__init__(user_id)
        
        # Get the file path from the request headers in the flask app
        self.image_file = image_file # The file path for the image
        self.classification = classification_results
        
    def create_image_path(self, user_id):
        pass