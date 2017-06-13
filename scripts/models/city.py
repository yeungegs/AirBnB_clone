#!/usr/bin/python3
"""
Module that creates city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """create new city
        """
        super().__init__(self, *args, **kwargs)
