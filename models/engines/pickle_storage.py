#!/usr/bin/python3
""" Implements the pickle file storage """

import pickle
from models.image_query import ImageQuery
import os
import uuid


class PickleStorage():
    """ Serializes an object to pickle file and back to object instance again """
    
    def pickler(self, username):
        """ This Function serializes an ImageQuery Object 
            into a pickle file

        Args:
            self(binary): The pickled file to deserialize
            username(str): A string identifying a user
        Returns:
            binary: The serialized pickle file.
        """
        
        
        # Pickle file name created from the query unique id
        # TODO: implement a way of uploading pickle file names to the database
        if Exception:
            print('An Exception Occured: {}'.format(Exception))
            return str(Exception)
        try:
            """ generate unique directory for username """  
            project_base_directory = os.getcwd()
            storage_directory = os.path.join(project_base_directory, 'pickle_file_storage')
            print(storage_directory)
            os.makedirs(storage_directory, exist_ok=True)
            user_directory = os.path.join(storage_directory, username)
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
        
        
    def de_pickler(pickle_file) :
        """ This Function de-serializes a pickle file
            into the original ImageQuery object

        Args:
            pickle_file(binary): The pickled file to deserialize
            
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
        