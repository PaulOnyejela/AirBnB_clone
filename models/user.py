#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""