#!/usr/bin/python3
from flask import Flask, request, render_template
from flasgger import Swagger
from flask_restful import Api
from flask_cors import CORS

from models.url_resources import TextAnalysisResource, ImageAnalysisResource
from models.api_users import APIUsers

app = Flask(__name__)
CORS(app)
api = Api(app)
swagger = Swagger(app, template_file='swagger.yaml')

# Add the resource classes to the API
api.add_resource(TextAnalysisResource, '/api/v1/text_analysis')
api.add_resource(ImageAnalysisResource, '/api/v1/image_analysis')

# Requesting api keys
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    """Create a new user with a unique API key"""
    username = request.json.get('username')
    
    if not username:
        return {'message': 'Please provide a username'}, 400
    
    # Generate a unique API key for the user
    user = APIUsers(username)
    api_key= user.save_query()
    
    # Save the user and their API key to the database or any other storage mechanism
    
    return {'username': username, 'api_key': api_key}, 201
if __name__ == '__main__':
    app.run(host='0.0.0.0')