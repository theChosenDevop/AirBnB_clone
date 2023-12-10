#!/usr/bin/python3
"""
    Defines unittest for models/base_model.py

    Unittest classes:
        TestBaseModel
"""
import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test for Base MOdel"""

    def setUp(self):
        """Instance of a class"""
        self.base_model = BaseModel()

    def test_base_model_id(self):
        """ Test if id is a string and not empty """
        self.assertIsInstance(self.base_model.id, str)
        self.assertNotEqual(self.base_model.id, "")

    def test_created_at(self):
        """Test if created_at is  datetime object """
        self.assertIsInstance(self.base_model.create_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object """
    self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_two_models_id_is_unique(self):
        """ Test two instance of a clss id for uniqueness """
        model_one = self.base_model()
        model_two = self.base_model()
        self.assertNotEqual(model_one.id, model_two.id)

    def test_base_model_created_at_different_time(self):
        """ Test instance of base_model at different time apart """
        model_one = self.base_model()
        sleep(0.10)
        model_two = self.base_model()
        self.assertLess(model_one.created_at, model_two.created_at)

    def test_base_model_updated_at_different_time(self):
        """ Test instance of base_model at different time apart """
        model_one = self.base_model()
        sleep(0.10)
        model_two = self.base_model()
        self.assertLess(model_one.updated_at, model.updated_at)

    def test_str_method(self):
        """Test __str__ method return string output"""
        expected_str_format = "[{}] ({}) {{}}".format(
                BaseModel,
                BaseModel.id,
                self.BaseModel.__dict__)
        self.assertEqual(str(self.base_model), expected_str_format)

    def test_save_method(self):
        """Test save method"""
        prev_updated_at = self.base_model.updated_at
        next_updated_at = self.base_model.save()
        self.assertNotEqual(prev_updated_at, next_updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method """
        dict_repr = self.base_model.to_dict()
        """ check if __class__ is added with the correct class name """
        self.assertIn('__class__', dict_repr)
        self.assertEqual(dict_repr['__class__'], 'BaseModel')
        """ Check if created_at and updated_at are converted to string in ISO format """
        self.assertIn('created_at', dict_repr)
        self.assertIn('updated_at', dict_repr)
        self.assertIsInstance(dict_repr['created_at'], str)
        self.assertIsInstance(dict_repr['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
