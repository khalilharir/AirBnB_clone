#!/usr/bin/env python3
""" This is the place module
It contains the class:
    -Place: This class inherits from BaseModel.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ This is the Amenity class """

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0, amenity_ids=[],
                 id=None, created_at=None, updated_at=None):
        super().__init__(id, created_at, updated_at)
