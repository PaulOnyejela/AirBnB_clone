#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    user_id = ""
    place_id = ""
    text = ""