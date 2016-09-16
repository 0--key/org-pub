"""Discover how they work by a coherent testing"""
import unittest


class TestAbs(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(abs(4) == 4)

    def test_negative(self):
        self.assertFalse(abs(-4) == -4)

    def test_string_as_argument(self):
        self.assertRaises(TypeError, lambda: abs('A'))


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
        self.assertRaises(TypeError, lambda: all(11))

    # assertRaises(exception, callable, *args, **kwds)

    def test_bool_argument(self):
        self.assertRaises(TypeError, lambda: all(True))


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


class TestAscii(unittest.TestCase):
    def test_list_convertation(self):
        self.assertEqual(ascii(['Several', 'words']),
                         "['Several', 'words']")

# dictionary is unordered sequence in Python

    def test_dict_convertation_double_quotes(self):
        self.assertNotEqual(ascii({"first": 1, "second": 2}),
                            '{"first": 1, "second": 2}')

    def test_dict_convertation_double_quotes_unordered(self):
        self.assertNotEqual(ascii({"first": 1, "second": 2}),
                            '{"second": 2, "first": 1}')

# tests below have a HIDDEN CAVEAT: it might pass SOMETIMES
# due undefined dictionary sequence

# def test_dict_convertation_single_quotes_ordered(self):
#     self.assertNotEqual(ascii({"first": 1, "second": 2}),
#                         "{'first': 1, 'second': 2}")

# def test_dict_convertation_single_quotes_unordered(self):
#     self.assertEqual(ascii({"first": 1, "second": 2}),
#                      "{'second': 2, 'first': 1}")


class TestBin(unittest.TestCase):

    def test_integer_argument(self):
        self.assertEqual(bin(16), '0b10000')

    def test_integer_negative(self):
        self.assertEqual(bin(-16), '-0b10000')

    def test_string_as_argument(self):
        self.assertRaises(TypeError, lambda: bin("A"))

    def test_float_as_argument(self):
        self.assertRaises(TypeError, lambda: bin(16.3))


class TestBool(unittest.TestCase):

    def test_numeric_argument(self):
        self.assertTrue(bool(1) and bool(-2) and bool(1.3))

    def test_zero_or_false_argument(self):
        self.assertFalse(bool(0) and bool(False))

    def test_string_as_argument(self):
        self.assertTrue(bool("Abc"))

    def test_mixed_arguments_list(self):
        self.assertTrue(bool(["A", False]))


class TestByteArray(unittest.TestCase):
    def setUp(self):
        self.seq = bytearray([0x13, 0x00, 0x00, 0x07, 0x08, 0x00])

    def test_as_iterable_of_bytes(self):
        self.assertEqual(self.seq.pop(), 0)
        self.assertEqual(self.seq.pop(), 8)

    def test_add_and_pop_item(self):
        self.seq.append(0x09)
        self.assertEqual(self.seq.pop(), 9)

    def test_string_as_argument(self):
        self.assertRaises(TypeError, lambda: self.seq.append('Foo'))
        # it's should be an array of integers from zero to 255

    def test_unsupported_value(self):
        self.assertRaises(ValueError, lambda: self.seq.append(0x257))

    def test_arbitrary_array_member(self):
        self.assertEqual(self.seq.pop(1), 0)
        self.assertEqual(self.seq.pop(1), 0)
        self.assertEqual(self.seq.pop(1), 7)

    def tearDown(self):
        self.seq.clear()


class TestBytes(unittest.TestCase):
    """By definition it is an immutable byte sequence"""

    def setUp(self):
        self.seq = bytes([0x13, 0x00, 0x00, 0x07, 0x08, 0x00])

    def test_count(self):
        self.assertEqual(self.seq.count(0, 2), 2)

    def test_find_bytes(self):
        self.assertEqual(self.seq.find(7), 3)

    def test_index(self):
        self.assertRaises(ValueError, lambda: self.seq.index(11))

    def test_is_digit(self):
        self.assertFalse(self.seq.isalnum())


class TestCallable(unittest.TestCase):

    def sample_function():
        return True

    def test_anonimous_function(self):
        self.assertTrue(callable(lambda: 3 + 2))

    def test_built_in_function(self):
        self.assertFalse(callable(abs(2)))

    def test_string_as_argument(self):
        self.assertFalse(callable("Ismael"))

    def test_numeric_argument(self):
        self.assertFalse(callable(2))

    def test_sample_function(self):
        self.assertTrue(self.sample_function)


class TestChr(unittest.TestCase):

    def test_string_as_argument(self):
        self.assertRaises(TypeError, lambda: chr("Ismael"))

    def test_numeric_argument(self):
        self.assertEqual(chr(2), '\x02')
        self.assertEqual(chr(105), 'i')





    


class TestComplex(unittest.TestCase):

    def test_summ_two_arguments(self):
        self.assertEqual(complex(3, 3) + complex(2, 2),
                         complex(5, 5))

    def test_string_as_argument(self):
        self.assertRaises(ValueError, lambda: complex("Alioth"))
