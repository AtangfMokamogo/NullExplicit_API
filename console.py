#!/usr/bin/python3
""" Implements a basic command interpreter in python """

import cmd
from analysis_engines.image_engine import ImageEngine
from analysis_engines.text_engine import TextEngine
from models.engines.pickle_storage import PickleStorage
from models.image_query import ImageQuery
from models.text_query import TextQuery, APIUsers
import os
import json
#from models.engines.database_storage import DBStorage
import sys

classes = ['ImageQuery', 'APIUsers', 'TextQuery']


class NullExplicitConsole(cmd.Cmd):
    """ The NULLX console """
    
    prompt = 'x>>'
    
    def precmd(self, line):
        # Perform command validation
        if line.split()[0] not in ['greet', 'quit', 'q', 'create', 'AnalyzeImage', 'AnalyzeText', 'unpickle', 'AddUser']:
            print("Invalid command.")
            return ''
        return line
    
    def do_greet(self, user):
        return print('Hello {}!'.format(user))
    
    """ def do_send_image_for_analysis(self, image_query_object, image_file):
        // send image for analysis here
        // call a function in the image classification engine
        // the function should return a JSON with the classification results 
        
        
        def do_analize_text(self, text_query_object):
            get text
    """
    
    
    def do_create(self, command):
        """ This method creates a query object and adds it to storage """
        
        # Parse the command
        cmd_parts = command.strip().split('(')
        command_name = cmd_parts[0]
        
        if len(cmd_parts) != 2 and command_name == "TextQuery":
            print("Invalid command format")
            return
        
        # This extracts the class name from the command
        
        
        # Extract the parameters
        args = cmd_parts[1].rstrip(')')
        
        # Initialize parameter extraction variables
        param_parts = []
        param_start = 0
        param_end = 0
        in_quotes = False
        
        # Iterate over the characters of args to extract parameters correctly
        for i, char in enumerate(args):
            if char == '(':
                in_quotes = True
            elif char == ')':
                in_quotes = False
            elif char == ',' and not in_quotes:
                param_parts.append(args[param_start:param_end].strip())
                param_start = param_end + 1
            
            param_end += 1
        
        # Append the last parameter
        param_parts.append(args[param_start:param_end].strip())
        
        params = {}
        
        for arg in param_parts:
            param_parts = arg.split('=')
            if len(param_parts) != 2:
                print("Invalid command format")
                return
            
            # Save the parameters as key-value pairs
            name = param_parts[0].strip()
            value = param_parts[1].strip()
            params[name] = value
            
        # Do something based on the command
        if command_name == "TextQuery" and len(params) >= 3:
            obj = TextQuery(
                user_id=params.get('user_id'),
                query_id=int(params.get('query_id')),
                text_input=params.get('text_input'),
                analysis_score=params.get('analysis_score')
            )
            TextQuery.save(obj)
        else:
            if command_name == 'ImageQuery':
            
                image_query = ImageQuery('/docs/images/user/image1.jpeg','Test-User', 'positive')
                print('query created: {}'.format(image_query.__dict__))
                PickleStorage.pickler(image_query, 'admin')

    def do_AnalyzeImage(self, line):
        """ This Console Method Sends an image to the Image Engine for analysis """
        image_filename = line
        current_dir = os.getcwd()

        # Construct the full image path.
        # NOTE that all images tested via the console should be saved
        # In the images/users/admin directory
        image_path = os.path.join(current_dir, "images", "users", "admin", image_filename)
        image_filename = os.path.basename(image_path)

        image_analyzer = ImageEngine()
        image_classification = image_analyzer.analyze_file(image_path)
        pickle = ImageQuery(image_path, 'admin', image_classification)
        pickle.save_to_pickle()
        print (image_classification)
        
    def do_AnalyzeText(self, line):
        """ This Console Method sends a Test Text Input for Sentiment Analysis """
        
        text_input = line
        
        analyse_this = TextEngine()
        analysis = analyse_this.analyze_text(text_input)
        
        sentiments = [message['sentiment'] for message in analysis['messages']]
        query_object = TextQuery("3445d25a-25cd-4de4-8472-1d9e3909a0a8 ", text_input, sentiments)
        query_object.save()
        print("Detected sentiment/s: {}".format(sentiments))
        print(analysis)
    
    def do_unpickle(self, path):
        """ This console method implements the console command
            unpickle. The command deserialses a pickle file object

        Args:
            pickle_file (file): the serialised pickle file
        
        Returns:
            class: The object instance that was pickled
        """
        file_name = path
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, "pickle_file_storage", "admin", file_name)
        file_name = os.path.basename(file_path)
        
        instance = PickleStorage.de_pickler(file_path)
        print("this is the object")
        print(instance)
    
    def do_AddUser(self, line):
        """This console method creates a new user 
            The user will have a unique API key
            
        Args:
            username (str): A user provided name
            
        Returns:
            string: A Unique API-Key associated with username
        """
        user =  APIUsers(line)
        user_token = user.add_user()
        print("User: {} - was granted access to our api with API SECRET KEY: {}".format(line, user_token))
        
    def do_quit(self, user='Default'):
        sys.exit()
    
    
if __name__ == '__main__':
    NullExplicitConsole().cmdloop()