#!/usr/bin/env python3
""" This is the user module
It contains the class:
    -User: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ This is the User class """

    def __init__(self, email="", password="", first_name="",
                 last_name="", id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
