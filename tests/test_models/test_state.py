#!/usr/bin/python3
"""
Test Review Classes
"""
from datetime import datetime
import inspect
from models.state import State
from models.base_model import BaseModel
import pep8
import unittest


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.model = State()
        self.model.save()

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attributes_State(self):
        """check State attributes"""
        self.assertTrue('id' in self.model.__dict__)
        self.assertTrue('created_at' in self.model.__dict__)
        self.assertTrue('updated_at' in self.model.__dict__)
        self.assertFalse('name' in self.model.__dict__)

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.model.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
