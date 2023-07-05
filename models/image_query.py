#!/usr/bin/python3
""" This Module implements a Base Image Query object """
import uuid
import os
import pickle
#from models.api_users import Users


class ImageQuery():
    """ A reresentation of an image query object """
    
    def __init__(self, image_file, username, classification_results):
        self.image_file = image_file 
        self.classification = classification_results
        self.username = username
    
   
    
    def save_to_pickle(self, user_key):
        """ generate unique directory for user_key
        Args:
            user_key (str): The User provided Api-Key
        """
        
        if Exception:
            print('An Exception Occured: {}'.format(Exception))
            return str(Exception)
        try:
            
            project_base_directory = os.getcwd()
            storage_directory = os.path.join(project_base_directory, 'pickle_file_storage')
            print(storage_directory)
            os.makedirs(storage_directory, exist_ok=True)
            user_directory = os.path.join(storage_directory, user_key)
            os.makedirs(user_directory, exist_ok=True)
                      
            filename = str(uuid.uuid4())
            file_path = os.path.join(user_directory, filename + '.pickle')
            
            # Pickle the ImageQuery object
            with open (file_path, 'wb') as pickle_file:
                pickle.dump(self, pickle_file)
                
            print("Object Successfully Pickled!")
            return pickle_file
               
        except pickle.PicklingError as PE:
            print("Error in Creating Pickle!: {}".format(PE))
            return False
        
        except (IOError, FileNotFoundError) as IOErrors:
            print("Error occured when working on file: {}".format(IOErrors))
            return False
        
        except Exception as E:
            print(" An Error Occured: {}".format(E))
            return False
        
        
        
    def load_from_pickle(self, pickle_file):
        """ This Function de-serializes a pickle file
            into the original ImageQuery object

        Args:
            pickle_file(file): The pickled file to deserialize
            
        Returns:
            class: The instance of the pickled class.
        """
        
        try:
            with open(pickle_file, 'rb') as file:
                serial_query_obj = pickle.load(file)
                
            # Verify the object was succefully created
            print('This object: {} was successfully un-pickled'.format(serial_query_obj.__dict__))
            return serial_query_obj
        
        except pickle.PickleError as PE:
            print("Error occurred during unpickling: {}".format(PE))
            return None

        except (IOError, FileNotFoundError) as IOErrors:
            print("Error occurred while opening or reading the file: {}".format(IOErrors))
            return None

        except AttributeError as Attr_Error:
            print("Error occurred during unpickling. Attribute not found: {}".format(Attr_Error))
            return None

        except Exception as E:
            print("An error occurred:", str(E))
            return None
        
    def delete_pickle_file(self):
        # call the pickle_file delete method
        # also handle any database in any
        pass