# [[file:../../2024-03-27-code-wars-with-tdd.org::*Test 001][Test 001:1]]
import unittest
from CodeWars.functions import getCount, input_string


class TestNumberVowelsInString(unittest.TestCase):

    def test_its_freaking_number(self):
        self.assertEqual(getCount(input_string), 9)
# Test 001:1 ends here
