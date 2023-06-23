#!/usr/bin/python3
""" Implements a basic command interpreter in python """

import cmd
from models.engines.pickle_storage import PickleStorage
from models.image_query import ImageQuery
from models.text_query import TextQuery
#from models.api_users import APIUsers
from models.engines.database_storage import DBStorage
import sys

classes = ['ImageQuery', 'APIUsers', 'TextQuery']


class NullExplicitConsole(cmd.Cmd):
    """ The NULLX console """
    
    prompt = 'x>>'
    
    def precmd(self, line):
        # Perform command validation
        if line.split()[0] not in ['greet', 'quit', 'q', 'create']:
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
        if len(cmd_parts) != 2:
            print("Invalid command format")
            return
        
        # This extracts the class name from the command
        command_name = cmd_parts[0]
        
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
            print("Invalid command or arguments")
        """if class_name in classes:
            if class_name == 'ImageQuery':
                image_query = ImageQuery('/docs/images/user/image1.jpeg','Test-User', 'positive')
                print('query created: {}'.format(image_query.__dict__))
                PickleStorage.pickler(image_query)
            elif class_name == 'TextQuery':
                obj = TextQuery(user_id="makhado", text_input="another test string", analysis_score="Negative")
                TextQuery.save(obj)"""
        
    def do_quit(self, user='Default'):
        sys.exit()
        
if __name__ == '__main__':
    NullExplicitConsole().cmdloop()