import unittest
from CodeWars.constants import first_constant_value


class TestUpperModule(unittest.TestCase):

    def test_import_from_upper_module(self):
        self.assertTrue(first_constant_value)
