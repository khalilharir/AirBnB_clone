#!/usr/bin/env python3
""" This is the city module
It contains the class:
    -City: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ This is the City class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
