#!/usr/bin/env python3
""" This is the user module
It contains the class:
    -User: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ This is the User class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
