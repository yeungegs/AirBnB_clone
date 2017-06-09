#!/usr/bin/python3

from datetime import datetime, date, time
import uuid

class BaseModel:
    """docstring
    """
    def __init__(self):
        """public instance methods"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        """docstring """
        return("[{}] {{}) {}".format(self.__class__.name__,
                                      self.id,
                                      self.__dict__))
    def __save__(self):
        """docstring"""
        self.updated_at = datetime.now()
        
        
    
