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
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                    time_format)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                    time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_json(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        + the class name in the key __class__.
        This method will be the first piece of the
        serialization/deserialization process.
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = type(self).__name__
        for key, value in model_dict.items():
            if isinstance(value, datetime):
                model_dict[key] = value.strftime(time_format)
        return model_dict

    def __str__(self):
        """Print BaseModel info
        """
        return ("[{0}] ({1}) {2}".format(self.__class__.__name__,
                                         self.id, self.__dict__))
