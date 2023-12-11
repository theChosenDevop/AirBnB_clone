#!/usr/bin/python3
"""
    Defines unittest for models/base_model.py
    Unittest classes:
        TestFileStorage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests for testing for FileStorage"""

    def setUp(self):
        """Ensure a clean state for each test by removing the file"""
        if os.path.exists(FileStorage._FIleStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.file_storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        all_objects = self.file_storage.all()
        self.assert(type(all_objects), dict)
        self.assertEqual(all_objects, {})

    def test_save_reload(self):
        """Test the save and reload methods"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.save()

        """Create new FileStorage instance to reload"""
        new_file_storage = FileStorage()
        new_file_storage.reload()

        """compare if reloaded objects match original ones"""
        all_objects = new_file_storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"{type(obj1).__name__}.{obj1.id}", all_objects)
        self.assertIn(f"{type(obj2).__name__}.{obj2.id}", all_objects)

    def test_new(self):
        """test new method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn(f"{type(obj).__name__}.{obj.id}", all_objects)

    def tearDown(self):
        """Remove file created during test"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
