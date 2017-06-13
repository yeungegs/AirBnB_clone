#!/usr/bin/python3
from models.base_mode import BaseModel



class User(BaseModel):
    """
    User class inherited from BaseModel
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init method
        """
        if (args and type(args[0]) == dict:
            super(User, self),__init__(args[0])
        else:
            supe(User, self).__init__()
        
