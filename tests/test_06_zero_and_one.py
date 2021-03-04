"""Initial numerical values testing.
"""

import unittest

"""Lets check 0 and 1 up against already known innate Python values
with already known testing methods"""


class TestPrimaryNumericFeatures(unittest.TestCase):
    """Zero and one are pertinent innate numeric objects to test it up

    """

    def test_zero_main_properties(self):
        self.assertFalse(0)  # <-- numeric zero also is Boolean False
        self.assertIsNotNone(0)  # and it is not None!
        self.assertEqual(0, 0)  # equality assertion by the method
        self.assertTrue(0 == 0)  # true statement assertion

    def test_one_main_properties(self):
        self.assertTrue(1)  # numeric one is also Boolean True
        self.assertIsNotNone(1)  # and it is not None!
        self.assertEqual(1, 1)  # equality assertion by the method
        self.assertTrue(1 == 1)  # true statement assertion

    def test_compare_one_and_zero(self):
        self.assertNotEqual(0, 1)  # as expected
        self.assertFalse(0 == 1)  # no comments
        self.assertTrue(0 < 1)  # a new comparison operator 'less'
        self.assertTrue(1 > 0)  # a new operator 'greater than'
        self.assertTrue(0 <= 1)  # 'less than or equal' operator
        self.assertTrue(1 >= 0)  # 'greater than or equal' operator


"""Check yourself up:

Try to extend the test suite to answer questions:
 - Does 0 equal False?
 - Does True greater than False?
 - Does True equal 1?
 - etc.
"""
