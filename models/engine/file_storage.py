#!/usr/bin/python3
import json
import datetime
"""
This is module file_storage
This module contains one class: FileStorage
"""



class FileStorage:
    """
    Serialize and deserialize objects in models to json
    Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    __objects = {}
    """
    def all(self):
        """Public instance method: Returns __objects
        """
        return self.__objects

    def new(self, obj):
        """Public instance method:
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Public instance method:
        serializes __objects to the JSON file (path: __file_path)
        """
        human_read = {}
        for key, value in self.__objects.items():
            human_read[k] = v.to_json()
        with open(self.__file_path, mode="w", encoding="UTF-8") as fhandle:
            json.dump(printable, fhandle)
        

    def reload(self):
        """Public instance method:
        deserializes the JSON file to __objects
        
        * should only do this if the JSON file exists ; otherwise, do nothing)
        """
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as fhandle:
                human_read = json.load(fhandle)
            for i, j in human_read.items():
                self.__objects[i] = BaseModel(*j)
        except FileNotFoundError:
            pass

        def userSerialize(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return obj
