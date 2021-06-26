#!/usr/bin/python3
"""
FileStorage that serializes and deserializes instances to a JSON file
"""
import json
import os.path


class FileStorage:
    """ String representing a simple data structure in JSON format.
        ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ 
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[new_key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dict = {}
        for key in self__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f, indent=4)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self__file_path):
            with open(self.__file_path, "r") as f:
                json_obj = json.load(f)
