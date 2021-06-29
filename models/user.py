#!/usr/bin/python3
"""
 class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ defining User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
