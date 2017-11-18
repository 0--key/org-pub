"""Discover how it works by testing"""
import unittest


class TestBuiltInConstants(unittest.TestCase):

    def test_true(self):
        self.assertTrue(1 + 3 == 4)

    def test_false(self):
        self.assertFalse(1 + 4 == 4)

    def test_none(self):
        value = None
        self.assertIsNone(value)


class TestEqualityQuirks(unittest.TestCase):
    """Equality is not identity

    """

    def setUp(self):
        self.arbitrary_numeric_variable = 5.4

    def test_unequality_by_value(self):
        # these are not the same objecsts
        self.assertFalse(self.arbitrary_numeric_variable is 5.4)

    def test_equality_by_value(self):
        self.assertTrue(self.arbitrary_numeric_variable == 5.4)

    def test_equality_by_temp_variable(self):
        clone_variable = self.arbitrary_numeric_variable
        self.assertTrue(clone_variable == self.arbitrary_numeric_variable)

    def tearDown(self):
        del(self.arbitrary_numeric_variable)
