#!/usr/bin/python3
"""
Module that creates States
"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel
    public class attribute:
    name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """create new state
        """
        super().__init__(self, *args, **kwargs)
