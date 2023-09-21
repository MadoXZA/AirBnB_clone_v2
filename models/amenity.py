#!/usr/bin/python3
"""Defines the Amenity class."""
from models
from models.base_model import BaseModel, Base
from sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity"""
    if models.storage_t == 'db':
        __tablename__ = 'amentities'
        name = Colum(string(128), nullable=False)
    else:
        name - ""

        def __init__(self, *args, **kwargs);
        """initializes Amenity"""
        super().__init__(*args,**kwargs)
