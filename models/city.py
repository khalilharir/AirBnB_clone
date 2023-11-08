#!/usr/bin/env python3
""" This is the city module
It contains the class:
    -City: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ This is the City class """

    def __init__(self, state_id="", name="", id=None, created_at=None,
                 updated_at=None):
        super().__init__(id, created_at, updated_at)
