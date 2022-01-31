#!/usr/bin/python3
"""test for city"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Class: TestCity"""
    def setUp(self):
        """instance setup"""
        self.city = City()

    def testattr(self):
        """Testing the attributes of City"""
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.__class__.__name__, "City")
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "New Haven"
        self.state_id = "454r127"
        self.assertEqual(self.city.name, "New Haven")

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(self.city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(self.city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

if __name__ == '__main__':
    unittest.main()
