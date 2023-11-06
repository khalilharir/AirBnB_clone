#!/usr/bin/env python3
""" This is the base_model module
it contains :
    -BaseModel class that defines all common attributes/methods for other
    classes.
"""


import json
from datetime import datetime


class BaseModel:
    """ This is the BaseModel class
    -It defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """ This is the instantiation function """
        import uuid
        if len(kwargs) > 0:
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    date = kwargs[key]
                    year = int(date[0:4])
                    month = int(date[5:7])
                    day = int(date[8:10])
                    hour = int(date[11:13])
                    minute = int(date[14:16])
                    second = int(date[17:19])
                    millisec = int(date[20:])
                    kwargs[key] = datetime(year, month, day, hour, minute,
                                           second, millisec)
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ This is the __str__ function it prints
        [<class name>] (<self.id>) <self.__dict__>
        """
        str_base = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return f"{str_base}"

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        self.__dict__["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M\
:%S.%f")
        self.__dict__["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M\
:%S.%f")
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
