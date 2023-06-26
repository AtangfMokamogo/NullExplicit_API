#!/usr/bin/python3
""" This Module implements a Base Image Query object """
import uuid
#from models.api_users import Users


class ImageQuery():
    """ A reresentation of an image query object """
    
    def __init__(self, image_file, user_id, classification_results):
        
        # Get the file path after saving from the request headers in the flask app
        self.image_file = image_file # The file path for the image
        self.classification = classification_results
        self.query_id = str(uuid.uuid4())
        
    
    """ The following methods should be defined
    
    def save_to_pickle(self):
        // save to pickle file by 
        // calling the pickler method method
        // return stauts of pickle or error
    
    def load_from_pickle(self, pickle_file):
        // pass the piclke file to the de pickler:
        
    def delete_pickle_file():
        // call the pickle_file delete method
        // also handle any database in any
    """