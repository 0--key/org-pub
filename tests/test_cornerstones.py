# [[file:../2024-06-05-python-fundamentals.org::*Basics][Basics:1]]
import unittest

"""

First and foremost let be sure about True, False and None
existence:

"""


class TestTheBasement(unittest.TestCase):

    def test_does_true_ever_exist(self):
        self.assertTrue(True)

    def test_does_false_ever_exist(self):
        self.assertFalse(False)

    def test_does_none_ever_exist(self):
        self.assertIsNone(None)
        self.assertFalse(None)  # None is showed up!
        # None has a boolean value

    def test_true_and_false_are_not_none_at_all(self):
        self.assertIsNotNone(True)  # NotNone (inverted None) has no
        self.assertIsNotNone(False)  # any Boolean value, it is unique
        self.assertFalse(None)  # But the vanilla None is False!


"""

Now it is very moment to dismantle the content of ~unittest~
toolbox. A dozen of acute utensils are there and you need to know which do
what. Bear in mind that you're already familiar with ~assertFalse~,
~assertTrue~, ~assertIsNotNone~ and ~assertIsNone as well.

"""


class TestAddtionalAssertionMethods(unittest.TestCase):

    def test_are_they_the_same(self):
        self.assertIs(True, True)
        self.assertIs(False, False)
        self.assertIs(None, None)

    def test_are_they_not_the_same(self):
        self.assertIsNot(True, False)
        self.assertIsNot(True, None)
        self.assertIsNot(None, False)

    def test_are_they_equal(self):
        self.assertEqual(True, True)
        self.assertEqual(False, False)
        self.assertEqual(None, None)

    def test_are_they_not_equal(self):
        self.assertNotEqual(True, False)
        self.assertNotEqual(True, None)
        self.assertNotEqual(None, False)
# Basics:1 ends here

# [[file:../2024-06-05-python-fundamentals.org::*Comparisons][Comparisons:1]]


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
# Comparisons:1 ends here
