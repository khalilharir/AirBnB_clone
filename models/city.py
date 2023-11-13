#!/usr/bin/env python3
""" This is the city module
It contains the class:
    -City: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ This is the City class """

    state_id = ""
    name = ""
