#!/usr/bin/python3
""" Defines Base Model"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Base model class of all subclasses """
    def __init__(self):
        """Initialization of instance of BaseModel
            Args:
                id:ssign with an uuid when an instance is created
                create_at: assign with the current datetime when an instance is created
                updated_at:  assign with the current datetime when an instance is created and it will be updated every time you change your object
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ returns a string format of BaseModel """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.__dict__.update({'updated_at': datetime.today()})
        #self.updated_at = datetime.today()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__  """
        dict_output = dict(self.__dict__)
        """ Create new key __class__ in dict_output """
        dict_output['__class__'] = self.__class__.__name__
        """ Convert created_at ro ISO format"""
        dict_output['created_at'] = dict_output['created_at'].isoformat()
        """ Convert upated_at to ISO format """
        dict_output['updated_at'] = dict_output['updated_at'].isoformat()
 
        return dict_output
