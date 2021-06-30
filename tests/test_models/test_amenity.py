#!/usr/bin/python3
"""Amenity"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testamenity(unittest.TestCase):

    def test_pep8_amenity(self):
        """Test that we conform to PEP8."""
        pe = pep8.StyleGuide(quiet=True)
        res = pe.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        amen = Amenity()
        self.assertEqual(amen.__class__.__name__, "Amenity")

    def test_base(self):
        amen = Amenity()
        self.assertTrue(issubclass(amen.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of Class Amenity"""
        amenity = Amenity()
        amenity.name = "kal"
        self.assertEqual(amenity.name, 'kal')

    def test_dict_value(self):
        """
            test dict values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst = Amenity()
        dict_con = inst.to_dict()
        self.assertEqual(dict_con["__class__"], "Amenity")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            inst.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            inst.updated_at.strftime(time_format))
