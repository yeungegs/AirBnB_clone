#!/usr/bin/python3
from datetime import datetime, date, time
import uuid
import models

"""
This is the BaseModel module
It contains one class: BaseModel
It contains the following functions:
    def to_json(self)
"""

class BaseModel:
    """docstring
    """
    def __init__(self, *args, **kwargs):
        """public instance attributes
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current
        datetime when an instance is created
        updated_at: datetime
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
        self.__dict__ = args[0]
        self.__dict__['created_at'] = datetime.strptime((self.__dict__['created_at']), "%Y-%m-%d %H: %M:%S.%f")
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
        models.storage.save()
        
    def to_json(self):
        """class method to convert __dict__ to json"""
        dictionary = {}
        for x in self.__dict__.keys():
            if (isinstance(self.__dict__[x], datetime)):
                dictionary[x] = str(self.__dict__[x])
            else:
                dictionary[x] = self.__dict__[x]
            dictionary['__class__'] = self.__class__.__name__
            return(dictionary)
    
