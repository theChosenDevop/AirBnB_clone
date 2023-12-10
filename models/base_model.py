#!/usr/bin/python3
""""Module for the BaseModel class."""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        models.storage.new(self)
    
    def save(self):
        """"updates the public instance attribute updated_at
        to the current time."""
        self.updated_at = datetime.utcnow()
        models.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Returns official string representation"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


