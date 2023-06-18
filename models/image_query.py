#!/usr/bin/python3
""" This Module implements a Base Image Query object """
import uuid
from models.base_query import BaseQuery

class ImageQuery(BaseQuery):
    """ A reresentation of an image query object """
    def __init__(self, image_file, user):
        super().__init__()
        self.image_id = str(uuid.uuid4()) # Unique id for every image
        self.image_file = image_file # The file pathe for the image