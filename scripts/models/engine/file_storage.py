#!/usr/bin/python3
"""Saving an object to a file
"""
import json
import models
from models.base_model import BaseModel
from datetime import datetime


# time_format = "%Y-%m-%dT%H:%M:%S.%f"

class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects
        """
        print("\nall IS USED\n")
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __obj the obj with
        key <obj class name>.id
        """
        print("\nnew HAS STARTED\n")
        new_obj_id = "{}.{}".format(type(obj).__name__,
                                 obj.id)
        FileStorage.__objects[new_obj_id] = obj
        print("\nnew IS COMPLETED\n")

    def save(self):
        """serializes __objects to the JSON file
        """
        print("\nsave HAS STARTED\n")
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as to_file:
            (json.dump(new_dict, to_file))
        print("\nsave IS COMPLETED\n")

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file exists ; otherwise, do nothing)
        """
        print("\nreload HAS STARTED\n")
        try:
            print("\nreload SUCCESSFUL TRY\n")
            with open(FileStorage.__file_path, mode="r", encoding="UTF-8") as to_file:
                object_loaded = json.load(to_file)
            for key, value in object_loaded.items():
                print("\nreload LOOP ENTERED\n")
                class_function = value["__class__"]
                FileStorage.__objects[key] = class_function(**object_loaded[item])
                
        except:
            print("\nreload TRIED FAILED\n")
            pass
        print("\nreload IS COMPLETED\n")


