#!/usr/bin/python3
"""
Test Review Classes
"""
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
import pep8
import unittest


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review class
    """

    def setUp(self):
        self.model = Review()
        self.model.save()

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        rev = Review()
        new_d = rev.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], rev.created_at.strftime(time))
        self.assertEqual(new_d["updated_at"], rev.updated_at.strftime(time))

if __name__ == "__main__":
    unittest.main()
