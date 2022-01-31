#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def setUp(self):
        """instance setup"""
        self.amenity = Amenity()

    def testattr(self):
        """Testing the attributes of Amenity"""
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.amenity.name, "")

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def teststr(self):
        """Testing the str format of Amenity"""
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id),
                                  self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

if __name__ == '__main__':
    unittest.main()
