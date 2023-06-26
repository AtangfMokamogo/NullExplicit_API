#!/usr/bin/python3
""" Implements the pickle file storage """

import pickle
from models.image_query import ImageQuery


class PickleStorage:
    """ Serializes an object to pickle file and back to object instance again """
    
    def pickler(query_object):
        """ This Function serializes an ImageQuery Object 
            into a pickle file

        Args:
            query_object(binary): The pickled file to deserialize
            
        Returns:
            binary: The serialized pickle file.
        """
        
        
        # Pickle file name created from the query unique id
        # TODO: implement a way of uploading pickle file names to the database
        filename = query_object.__dict__['query_id']
        try:
            # Pickle the ImageQuery object
            with open (filename + '.pickle', 'wb') as pickle_file:
                pickle.dump(query_object, pickle_file)
                
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
        
        
    def de_pickler(pickle_file):
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
            print(serial_query_obj.__dict__)
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
        
    """ this function deletes a pickle file from the system
     def remove_pickles(self, pickle_file):
        // handle neccessary imports
        // find pickle file in system
        // purge it from system
        // return successful or error
    """