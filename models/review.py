#!/usr/bin/env python3
""" This is the review module
It contains the class:
    -Review: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ This is the Amenity class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
