# [[file:../2024-06-06-python-comparison-explained.org::*Self-explanatory test suite][Self-explanatory test suite:1]]
"""

Now lets figure out how to compare with unittest

"""


class TestTheLiteralTruths(unittest.TestCase):

    def test_any_non_zero_is_true(self):
        self.assertTrue(1)
        self.assertTrue(-1)
        self.assertTrue("L")
        self.assertFalse(None)  # Except the None!

    def test_zero_and_none_are_same_as_false(self):
        self.assertFalse(0)
        self.assertFalse(None)  # and None as well!


class TestPrimalsQuirks(unittest.TestCase):

    def test_true_equals_one(self):
        self.assertTrue(True == 1)  # it is equal
        self.assertFalse(True == -1)
        self.assertFalse(True == 2)  # it isn't equal two!
        self.assertFalse(True == 0)  # True is not zero

    def test_any_non_zero_value_is_true(self):
        self.assertTrue("A")
        self.assertTrue(32)
# Self-explanatory test suite:1 ends here
