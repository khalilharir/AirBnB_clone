#!/usr/bin/env python3
""" This is the amenity module
It contains the class:
    -Amenity: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This is the Amenity class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
