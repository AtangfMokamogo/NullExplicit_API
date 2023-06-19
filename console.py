#!/usr/bin/python3
""" Implements a basic command interpreter in python """

import cmd
from models.engines.pickle_storage import PickleStorage
from models.base_query import BaseQuery
from models.image_query import ImageQuery
import sys

classes = ['ImageQuery', 'BaseQuery', 'TextQuery']


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
    
    def do_create(self, class_name):
        if class_name in classes:
            if class_name == 'ImageQuery':
                image_query = ImageQuery('/docs/images/user/image1.jpeg','Test-User', 'positive')
                print('query created: {}'.format(image_query.__dict__))
                PickleStorage.pickler(image_query)
            else:
                print('some other class {} was created'.format(class_name))
        
    def do_quit(self, user='Default'):
        sys.exit()
        
if __name__ == '__main__':
    NullExplicitConsole().cmdloop()