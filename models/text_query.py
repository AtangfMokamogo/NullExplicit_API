from sqlalchemy import Column, Text, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engines.db import Base, DataStorage
import models



class TextQuery(DataStorage, Base):
    """ Represents the Text query object """
    
    __tablename__ = 'TextQuery'
    id = Column(Integer, primary_key=True)
    userApiKey = Column(String, ForeignKey('APIUsers.apikey'))
    text = Column(Text)
    analysis = Column(Text)
    user = relationship("APIUsers", back_populates="queries")
    
    
    def __init__(self, api_key, text_input, analysis):
        """ Initialises the APIUsers class """
        super().__init__()
        id = Column(Integer, primary_key=True)
        self.userApiKey = api_key
        self.text = text_input
        self.analysis = analysis
        
       
     
    def save_query(self):
        """ adds new text query to database """

        try:
            models.storage.session.add(self)
            models.storage.session.commit()
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.close()
    
    
    def retrieve_query(self, query_id):
        """ Retrieves Record associated with <query_id> from database.

        Args:
            query_id (int): The query id associated with record
            
        Returns:
            string: A string representation of the record
        """
        
        try:
            query= models.storage.session.query(TextQuery).filter_by(id=query_id).first()
            
            if query:
                record = "Query ID: {}  User-Api-Key: {} Input-Text: {} Text-Sentiment: {}".format(TextQuery.id, TextQuery.userApiKey, TextQuery.text, TextQuery.analysis)
                return record
            
            else:
                return "There is no Query associated with the provided Query ID"
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.commit()
        
    
    
    def remove_query(self, query_id):
        """ Deletes a record associated with <query_id>

        Args:
            query_id (int): The query id associated with record
            
        Returns:
            string: "Query removed from record" else "No record assosciated with <query_id>
        """
        
        try:
            query= models.storage.session.query(TextQuery).filter_by(id=query_id).first()
            
            if query:
                models.storage.session.delete(query)
                
                return "Query associated with Query ID: {} Has been successfully deleted!".format(query_id)

            else:
                return "Unsuccessful!: There is no Query associated with the provided Query ID"
            
        except:
            models.storage.session.rollback()
            raise
        
        finally:
            models.storage.session.commit()