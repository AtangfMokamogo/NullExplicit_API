#!/usr/bin/python3
""" This Module implements a Base Image Query object """
import uuid
#from models.api_users import Users


class ImageQuery():
    """ A reresentation of an image query object """
    
    def __init__(self, image_file, username, classification_results):
        self.image_file = image_file 
        self.classification = classification_results
        self.username = username
    
   
    
    def save_to_pickle(self):
        """ Method that saves object to pickle file """ 
        from models.engines.pickle_storage import PickleStorage
        storage = PickleStorage()
        # create new object
        storage.pickler(self.username)
        
        
    def load_from_pickle(self, pickle_file):
        # pass the piclke file to the de pickler:
        pass
        
    def delete_pickle_file(self):
        # call the pickle_file delete method
        # also handle any database in any
        pass