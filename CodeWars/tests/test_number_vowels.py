# [[file:../../2024-03-27-code-wars-with-tdd.org::*Test 001][Test 001:1]]
import unittest
from CodeWars.functions import getCount, input_string

class TestNumberVowelsInString(unittest.TestCase):

    def setUp(self):
        self.variable_inside_test_suite = "Alioth"

    def test_innate_variable(self):
        self.assertEqual(getCount(self.variable_inside_test_suite), 3)
        #pass

    def test_imported_values(self):
        print("Hello, its the first test!")
        self.assertEqual(getCount(input_string), 9)
# Test 001:1 ends here
