from sqlalchemy import create_engine
from models.base_query import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DataStorage:
    """ Handles the setup of the database """
    engine = None
    session = None
    
    def __init__(self):
        """ Instantiate The database class """
        
        NULL_X_MYSQL_USER = os.environ.get('NULL_EXPLICIT_MYSQL_USER')
        NULL_X_MYSQL_PWD = os.environ.get('NULL_EXPLICIT_MYSQL_PASSWORD')
        NULL_X_MYSQL_HOST = os.environ.get('NULL_EXPLICIT_MYSQL_HOST')
        NULL_X_MYSQL_DATABASE = os.environ.get('NULL_EXPLICIT_MYSQL_DATABASE')

        print(NULL_X_MYSQL_HOST)
        self.engine = create_engine(f"mysql+pymysql://{NULL_X_MYSQL_USER}:{NULL_X_MYSQL_PWD}@{NULL_X_MYSQL_HOST}/{NULL_X_MYSQL_DATABASE}")
    
    
    def reload(self):
        """ Reloads data from the database """
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.session = Session
        
    