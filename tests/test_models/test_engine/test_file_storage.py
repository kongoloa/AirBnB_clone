import unittest
import pep8
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import *


class Test_FileStorage(unittest.TestCase):
    """
    Test file storage
    """

    def setUp(self):
        self.store = FileStorage()

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        p = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attrs(self):
        """test for presence of attributes"""
        self.assertFalse(hasattr(self.store, "BrandynAndGary.json"))

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

if "__main__" == __name__:
    unittest.main()
