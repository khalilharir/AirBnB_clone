#!/usr/bin/env python3
""" This is the amenity module
It contains the class:
    -Amenity: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This is the Amenity class """

    def __init__(self, name="", id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
