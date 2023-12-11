#!/usr/bin/python3
"""
Module for the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class Representation.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
