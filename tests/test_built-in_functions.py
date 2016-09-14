"""Discover how they work by a coherent testing"""
import unittest


class TestAbs(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(abs(4) == 4)

    def test_negative(self):
        self.assertFalse(abs(-4) == -4)

    def test_string_as_argument(self):
        self.assertRaises(TypeError, lambda x: abs('A'))


class TestAll(unittest.TestCase):

    def test_one_value_is_zero(self):
        self.assertFalse(all([0, 1]))

    def test_all_values_are_positive_numbers(self):
        self.assertTrue(all([1, 2, 3]))

    def test_single_element_is_false(self):
        self.assertFalse(all([False, 3]))

    def test_single_element_is_None(self):
        self.assertFalse(all([None, 3]))

    def test_all_values_are_negative(self):
        self.assertTrue(all([-1, -2]))

    def test_all_values_are_strings(self):
        self.assertTrue(all(["String", "value"]))

    def test_one_value_is_empty_string(self):
        self.assertFalse(all(["", "Empty"]))

    def test_empty_list(self):
        self.assertTrue(all([]))

    def test_string_as_argument(self):
        self.assertTrue(all('l') and all('low') and all('at the'))

    def test_non_iter_argument(self):
        self.assertRaises(TypeError, lambda x: all(11))

    # assertRaises(exception, callable, *args, **kwds)

    def test_bool_argument(self):
        self.assertRaises(TypeError, lambda x: all(True))


class TestAny(unittest.TestCase):

    def test_boolean_arguments(self):
        self.assertTrue(any([True, True]))

    def test_mixed_arguments(self):
        self.assertTrue(any([True, False]))

    def test_all_false_elements(self):
        self.assertFalse(any([False, False]))

    def test_string_as_argument(self):
        self.assertTrue(any("Blasphemy"))

    def test_empty_list(self):
        self.assertFalse(any([]))

    # def test_(self):
    #     self.assertTrue(any([True, True]))

    # def test_(self):
    #     self.assertTrue(any([True, True]))

    # def test_(self):
    #     self.assertTrue(any([True, True]))
