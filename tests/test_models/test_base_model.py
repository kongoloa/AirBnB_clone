#!/usr/bin/python3
"""
Unit tests for base_model.py
"""
import unittest
from models.base_model import BaseModel
import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel
    """
    def setUp(self):
        """Set up instances"""
        self.basemodel = BaseModel()

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def testattr(self):
        """Test the attributes of BaseModel"""
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.basemodel.name = "Betty"
        self.basemodel.age = 89
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertEqual(self.basemodel.name, "Betty")
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

if __name__ == "__main__":
    unittest.main()
