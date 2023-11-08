#!/usr/bin/env python3
""" This is the State module
It contains the class:
    -State: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """ This is the State class """

    def __init__(self, name="", id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
