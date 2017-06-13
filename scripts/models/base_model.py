#!/usr/bin/python3
"""defines all common attributes/methods for other classes
"""
import json
import uuid
from datetime import datetime
import models 
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel class for other classes
    """
    def __init__(self, *args, **kwargs):
        """init BaseModel class
        """
        print("\nINIT NOW\n")
        if (len(args) == 0 and len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            # self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.__dict__ = kwargs
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                                time_format)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                                time_format)
        print("\nINIT HAS COMPLETED\n")

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        # print("\nSTART SAVE NOW\n")
        self.updated_at = datetime.now()
        models.storage.save()
        print("\nSAVE HAS COMPLETED\n")

    def to_json(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        + the class name in the key __class__.
        This method will be the first piece of the
        serialization/deserialization process.
        """
        """NEW CODE POST 5"""
        print("\nto_json START NOW\n")
        model_dict = self.__dict__.copy()
        model_dict.update({"__class__": str(type(self).__name__)})
        for key, value in model_dict.items():
            if isinstance(value, datetime):
                model_dict[key] = value.strftime(time_format)
        print("\nto_json HAS COMPLETED\n")
        return model_dict
        """
        OLD PRIOR 5
        model_dict.created_at = str(self.created_at.isoformat())
        model_dict["__class__"] = type(self).__name__
        if hasattr(self, "updated_at") == True:
            self.updated_at = str(datetime.now().isoformat())
        # print("\nto_json has happened\n")
        return (self.__dict__)
        """
        
    def __str__(self):
        """Print BaseModel info
        """
        print("\n__str__ HAS HAPPENED BELOW\n")
        return ("[{0}] ({1}) {2}".format(self.__class__.__name__,
                                         self.id, self.__dict__))