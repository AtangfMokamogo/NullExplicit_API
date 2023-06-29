#!/usr/bin/python3
""" module that implements the image classification engine """
import requests
import os
import json


class ImageEngine():
    """ This Module Is Responsible For Communicationg With The 
        Imagga Image Analysis API
    """
    
    
    def __init__(self):
        self.__IMAGGA_API_KEY = os.environ.get('IMAGGA_API_KEY')
        self.__IMAGGA_API_SECRET = os.environ.get('IMAGGA_API_SECRET')
    
    def _parse_response(self, json_str):
        """This private class function parses the json response
            from imagga into a much more comprehesible form for our api

        Args:
            json_str (str): json response object typecast to a string variable
            
        Returns:
            string: a json type string containing the parsed response
        """
        data = json.loads(json_str)
        categories = data['result']['categories']
        categories_detected = [{'name': category['name']['en'], 'confidence': category['confidence']} for category in categories]
        result = {'categories-detected': categories_detected}
        json_str = json.dumps(result, indent=4)
        return json.loads(json_str)
        
    
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
            return self._parse_response(response.text)
        
        except IOError as FILE_OPERATIONS_ERROR:
            print(self.__IMAGGA_API_KEY)
            print(self.__IMAGGA_API_SECRET)
            print('An Error Occured while reading the file: {}'.format(FILE_OPERATIONS_ERROR))
        
        except requests.exceptions.RequestException as HTTP_REQUEST_EXCEPTION:
            print('An error occured while sending the request to Imagga: {}'.format(HTTP_REQUEST_EXCEPTION))