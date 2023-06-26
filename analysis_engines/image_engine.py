#!/usr/bin/python3
""" module that implements the image classification engine """
import requests
import os


class ImageEngine():
    """ This Module Is Responsible For Communicationg With The 
        Imagga Image Analysis API
    """
    
    
    def __init__(self):
        self.__IMAGGA_API_KEY = "acc_be0866406e09521"
        self.__IMAGGA_API_SECRET = "8ad8461cd9f61144317b9987258ce562"
    
    
    def analyze_file(self, image_path):
        """This Method Requests an Imagge categorisation form the Imagga API 

        Args:
            image_path (str): The path to the image file
        
        Returns:
            The classification score of the image
        """
        try:    
            response = requests.post(
            'https://api.imagga.com/v2/categories/nsfw_beta',
            auth=(self.__IMAGGA_API_KEY, self.__IMAGGA_API_SECRET),
            files={'image': open(image_path, 'rb')}
            )
            response.raise_for_status()
            print(response.json())
        
        except IOError as FILE_OPERATIONS_ERROR:
            print(self.__IMAGGA_API_KEY)
            print(self.__IMAGGA_API_SECRET)
            print('An Error Occured while reading the file: {}'.format(FILE_OPERATIONS_ERROR))
        
        except requests.exceptions.RequestException as HTTP_REQUEST_EXCEPTION:
            print('An error occured while sending the request to Imagga: {}'.format(HTTP_REQUEST_EXCEPTION))