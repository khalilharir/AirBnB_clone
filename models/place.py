#!/usr/bin/env python3
""" This is the place module
It contains the class:
    -Place: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ This is the Amenity class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
