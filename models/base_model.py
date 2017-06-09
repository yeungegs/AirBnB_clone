#!/usr/bin/python3

from datetime import datetime, date, time
import uuid
"""
This is the BaseModel module
It contains one class: BaseModel
It contains the following functions:
    def to_json(self)
"""

class BaseModel:
    """docstring
    """
    def __init__(self):
        """public instance attributes
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current
        datetime when an instance is created
        updated_at: datetime
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        """private method
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
         """
        return("[{}] {{}) {}".format(self.__class__.name__,
                                      self.id,
                                      self.__dict__))
    def __save__(self):
        """public instance method"""
        self.updated_at = datetime.now()

    def to_json(self):
        """public instance method"""
        json = self.__dict__
        json['class'] = self.__class__.__name__
        return(json)
