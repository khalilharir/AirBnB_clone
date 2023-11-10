#!/usr/bin/env python3
""" This is the file_storage module
It contains:
    -FileStorage:  a class that serializes instances to a JSON file and
    deserializes JSON file to instances.
"""


from models.base_model import BaseModel
import json


class FileStorage:
    """ This is the FileStorage class:
    a class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This public instance method returns the dictionary that contains
        the objects """
        from importlib import import_module
        for key in self.__objects.keys():
            class_name, id = key.split(".")
            if class_name != 'BaseModel':
                mod_name = import_module("models." + class_name.lower(), ".")
                class_n = getattr(mod_name, class_name)
                self.__objects[key] = class_n(**self.__objects[key])
            else:
                self.__objects[key] = BaseModel(**self.__objects[key])
        return self.__objects

    def new(self, obj):
        """ This is the new function:
        It sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        from copy import deepcopy
        with open(self.__file_path, "w", encoding='utf-8') as f:
            obj_dict = deepcopy(self.__objects)
            for key in obj_dict.keys():
                obj_dict[key] = obj_dict[key].to_dict()
            f.write(json.dumps(obj_dict))

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists) """
        import os
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                data = f.read()
            if len(data) > 0:
                self.__objects = json.loads(data)
