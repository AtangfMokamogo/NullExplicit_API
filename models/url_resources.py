#!/usr/bin/python3
""" Module that implements the url resources for our flask app """
import os
from flask import request
from flasgger.utils import swag_from
from flask_restful import Resource
from models.auth_module import authenticate

from models.api_users import APIUsers
from models.text_query import TextQuery
from models.image_query import ImageQuery
from analysis_engines.text_engine import TextEngine
from analysis_engines.image_engine import ImageEngine
from models.base_query import BaseClass

user_key = BaseClass()


class TextAnalysisResource(Resource):
    """ This Class implements the TextAnalysis URL resource """
    
    @authenticate
    @swag_from(os.path.join(os.path.dirname(__file__), 'swagger.yml'))
    def post(self):
        """Function that implements the post endpoint for sentiment analysis
        """
        
        # Extract the API KEY from the headers use it to find username
        api_key = request.headers.get('Api-Key')
        user = user_key.get_key(api_key)

        
        if not user:
          return {'message': 'Invalid Api-Key provided (there is no user associated with the key)'}, 401
        
        # Extract Text submitted for analysis from request body
        payload = request.get_json()
        text_input = payload.get('text-input')
        
        # Analysing the text and Extract sentiment for saving to database
        query_analysis_object = TextEngine()
        analysis = query_analysis_object.analyze_text(text_input=text_input)
        sentiment_value = analysis['messages'][0]['sentiment']
        
        # create a new instance of TextQuery class to save the request to database
        query_object = TextQuery(api_key, text_input, sentiment_value)
        query_object.save_query()
        return analysis
    

class ImageAnalysisResource(Resource):
    """ This Class implements the ImageAnalysis URL resource """
    
    @authenticate
    def post(self):
        """ Implements the post endpoint for image analysis """
        
        # Check if the 'image' file was uploaded in the request
        if 'image' not in request.files:
            return {'message': 'No image file uploaded.', 'required':'image file'}, 400

        image_file = request.files['image']
        
        api_key = request.headers.get('Api-Key')
        user = user_key.get_key(api_key)

        if not user:
            username = 'default'
        else:
            username = api_key
        
        # Save the image to the specific user folder
        folder_path = os.path.join(os.getcwd(), 'images', username)
        file_path = os.path.join(folder_path, image_file.filename)
        os.makedirs(folder_path, exist_ok=True)
        image_file.save(file_path)
        
        
        # Analysing the image file
        analysis = ImageEngine().analyze_file(file_path)
        
        # Create an ImageQuery object for storage
        query_object = ImageQuery(file_path, username, analysis)
        query_object.save_to_pickle(api_key)
        
        return analysis