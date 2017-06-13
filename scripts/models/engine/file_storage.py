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
# time_format = "%Y-%m-%dT%H:%M:%S.%f"


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
        # print("\nFILE all IS USED\n")
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __obj the obj with
        key <obj class name>.id
        """
        # print("\nFILE new HAS STARTED\n")
        new_obj_id = "{}.{}".format(type(obj).__name__,
                                    obj.id)
        # print("This is the new_obj {}".format(new_obj_id))
        FileStorage.__objects[new_obj_id] = obj
        # print("This is __objects dictionary {}".format(self.__objects))
        # print("\nFILE new IS COMPLETED\n")

    def save(self):
        """serializes __objects to the JSON file
        """
        # print("\nFILE save HAS STARTED\n")
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
            # print("This is new_dict --> {}".format(new_dict))
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as to_file:
            # serialize here
            (json.dump(new_dict, to_file))
        # print("\nFILE save IS COMPLETED\n")

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file exists ; otherwise, do nothing)
        """
        try:
            # print("\nATTEMPTING TRY reload\n")
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF-8") as to_file:
                # print("\nRELOAD File opened\n")
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

                """
                for key in json_obj.keys():
                    self.__objects[key] = BaseModel(**json_obj[key])

                for obj_id, dic in object_loaded.items():
                    # print("\nreload LOOP ENTERED\n")
                    obj_class = objects_loaded[obj_id].get("__class__")
                    if obj_class in classes:
                        meth = objects_loaded.get(obj_class)
                        FileStorage.__objects[obj_id] = meth(
                            **objects_loaded[obj])
                """
            # print("\nSUCCESSFUL TRY\n")
        except:
            # print("\nreload EXCEPT USED\n")
            pass

        # print("\nreload IS COMPLETED\n")
