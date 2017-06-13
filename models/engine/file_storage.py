#!/usr/bin/python3
"""Saving an object to a file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def all(self):
        """Returns objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __obj the obj with
        key <obj class name>.id
        """
        new_obj_id = "{}.{}".format(type(obj).__name__,
                                    obj.id)
        FileStorage.__objects[new_obj_id] = obj

    def save(self):
        """serializes __objects to the JSON file
        """
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as to_file:
            (json.dump(new_dict, to_file))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file exists ; otherwise, do nothing)
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF-8") as to_file:
                objects_loaded = json.load(to_file)
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User

                class_list = ["BaseModel", "Amenity", "City", "Place",
                              "Review", "State", "User"]

                for key, value in objects_loaded.items():
                    if value.get("__class__") in class_list:
                        meth = value.get("__class__")
                        self.__objects[key] = eval(
                            str(meth))(objects_loaded[key])
        except:
            pass
