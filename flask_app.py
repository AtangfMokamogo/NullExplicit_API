from flask import Flask, request
from flask_restful import Api, Resource
from models.url_resources import TextAnalysisResource, ImageAnalysisResource
from models.text_query import APIUsers
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template_file='swagger.yml')

# Add the resource classes to the API
api.add_resource(TextAnalysisResource, '/nullxapi/v1/text_analysis')
api.add_resource(ImageAnalysisResource, '/nullxapi/v1/image_analysis')

# Requesting api keys
@app.route('/nullxapi/v1/users', methods=['POST'])
def create_user():
    """Create a new user with a unique API key"""
    username = request.json.get('username')
    
    if not username:
        return {'message': 'Please provide a username'}, 400
    
    # Generate a unique API key for the user
    user = APIUsers(username)
    api_key= user.add_user()
    
    # Save the user and their API key to the database or any other storage mechanism
    
    return {'username': username, 'api_key': api_key}, 201
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)