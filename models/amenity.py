#!/usr/bin/python3
"""
Module that creates amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """create new amenity
        """
        super().__init__(self, *args, **kwargs)
