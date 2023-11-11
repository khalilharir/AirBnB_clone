#!/usr/bin/python3
""" This is the test_base_model module
for testing the BaseModel class
"""


import unittest
from ...models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """ This is the TestBaseModelClass class """

    def test_construction(self):
        """ Testing the __init__ function """
        a = BaseModel()
        creation_date = a.created_at
        a.save()
        self.assertAlmostEqual(a.created_at, creation_date)
