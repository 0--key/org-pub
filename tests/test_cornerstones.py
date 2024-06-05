# [[file:../2024-06-05-python-fundamentals.org::*Basics][Basics:1]]
import unittest


class TestTheBasement(unittest.TestCase):

    def test_does_true_ever_exist(self):
        self.assertTrue(True)

    def test_does_false_ever_exist(self):
        self.assertFalse(False)


class TestTheLiteralTruths(unittest.TestCase):

    def test_any_non_zero_is_true(self):
        self.assertTrue(1)
        self.assertTrue(-1)
        self.assertTrue("L")
        self.assertFalse(None) # Except the None!

    def test_zero_and_none_are_same_as_false(self):
        self.assertFalse(0)
        self.assertFalse(None) # and None as well!


class TestPrimalsQuirks(unittest.TestCase):

    def test_true_equals_one(self):
        self.assertTrue(True == 1)  # it is equal
        self.assertFalse(True == -1)
        self.assertFalse(True == 2)  # it isn't equal two!
        self.assertFalse(True == 0)  # True is not zero

    def test_any_non_zero_value_is_true(self):
        self.assertTrue("A")
        self.assertTrue(32)
# Basics:1 ends here
