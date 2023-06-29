#!/usr/bin/python3
""" This module implements the Sentiment Analysis Engine """

import requests
import json
import time


class TextEngine():
    """ This Class implements methods that communicate with rev.ai Sentiment
        Analysis Engine
    """
    
    def __init__(self):
        self.__ACCESS_TOKEN = "02eSslKwFRZ7M3hO3B-mtupMCN2KpBTpbPi6QKZgmIYLhg1nZZ7pBA6Dc1j83L0IgMtRpWr_YNy4vycW1RKDWTgOfRGF4"
        
        
    def _request_state(self, query_id):
        """ retrieve the final sentiment analysis score 
            
            Args:
                query_id (str): This is the query id genreted by the initial
                                `post` request to REV.ai API
            Returns:
                string: A JSON format string with the analysis score
        """
        
        try:
            url = "https://api.rev.ai/sentiment_analysis/v1/jobs/" + query_id + "/result"
            headers = {
                "Authorization":"Bearer {}".format(self.__ACCESS_TOKEN)
            }
            
            response = requests.get(url, headers=headers)
            
            return response.json()
        
        except requests.exceptions.RequestException as ERROR_IN_PROCESSING_REQUEST:
            print("A request exception occurred:", str(ERROR_IN_PROCESSING_REQUEST))
        
        except json.JSONDecodeError as e:
            print("JSON decoding error:", str(e))

                
    def analyze_text(self, text_input):
        """This Function Analyses the text_input and returns
            a sentiment analysis score

        Args:
            text_input (str): This is the text object passed in as input from the user
            
        Returns:
            string: The sentiment analysis score.
        """
        
        print(text_input)
        try:
            
            url = "https://api.rev.ai/sentiment_analysis/v1/jobs"
            
            payload = {
                "language":"en",
                "metadata":"sample test queries not on production yet",
                "delete_after_seconds":1000000,
                "text":"{}".format(text_input)
            }
            
            headers = {
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(self.__ACCESS_TOKEN)
            }
            
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
        
        except requests.exceptions.RequestException as ERROR_IN_HANDLING_REQUEST:
            print("A request exception occurred:", str(ERROR_IN_HANDLING_REQUEST))
        
        except json.JSONDecodeError as ERROR_IN_DECODING_TEXT_ANALYSIS_JSON_RESPONSE:
            print("JSON decoding error in the TextEngine Module:",
                  str(ERROR_IN_DECODING_TEXT_ANALYSIS_JSON_RESPONSE))
        
        except Exception as e:
            print("An unexpected error occurred:", str(e))
            
        # Extract query id from the response
        id = data["id"]
        
        # Wait for the API to process the results
        print("The Model is analyzing your text. Please wait for at least 35 seconds", end='')
    
        start_time = time.time()
        elapsed_time = 0
        dot_count = 0
        while elapsed_time < 30:
            if elapsed_time > dot_count * 7:
                print('.', end='', flush=True)
                dot_count += 1
            time.sleep(1)
            elapsed_time = time.time() - start_time
        
        print(" Done! Here are your results")
        text_analysis_score = self._request_state(query_id=id)
        return text_analysis_score