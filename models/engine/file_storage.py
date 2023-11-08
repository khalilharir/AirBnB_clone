#!/usr/bin/env python3
""" This is the file_storage module
It contains:
    -FileStorage:  a class that serializes instances to a JSON file and
    deserializes JSON file to instances.
"""


import json
import os


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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                obj_dict = json.loads(f.read())
