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


class TestDelattr(unittest.TestCase):

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj = Pear()

    def test_all_obj_attributes(self):
        self.assertTrue(self.obj.size and self.obj.color)

    def test_del_existing_attribute(self):
        self.assertIsNone(delattr(self.obj, 'size'))
        self.assertRaises(AttributeError, lambda: self.obj.size)

    def test_del_non_existing_attribute(self):
        self.assertRaises(AttributeError,
                          lambda: delattr(self.obj, 'shape'))


class TestDict(unittest.TestCase):

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj = Pear()
        self.mock_dict = dict(a=1, b=2)

    def test_all_dict_attributes(self):
        self.assertTrue(self.mock_dict["a"] == 1)
        self.assertTrue(self.mock_dict["b"] == 2)

    # def test_mapping_obj(self):
    #     #
    #     self.assertTrue(dict(self.obj))
    #     # self.assertRaises(AttributeError, lambda: self.obj.size)


class TestDir(unittest.TestCase):

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj = Pear()

    def test_existing_attr(self):
        self.assertTrue(dir(self.obj)[-1] == 'size' and
                        dir(self.obj)[-2] == 'color')


class TestDivmod(unittest.TestCase):

    def test_simple_division(self):
        self.assertTrue(divmod(5, 3) == (1, 2))

    def test_complex_division(self):
        self.assertTrue(divmod(10, 3) == (3, 1))


class TestEnumerate(unittest.TestCase):

    def test_enumerate_zero_list(self):
        """function returns an iterator"""
        alist = [0, 1, 2]
        for i, j in enumerate(alist):
            self.assertEqual(i, j)

    def test_enumerate_arbitrary_list(self):
        alist = [2, 3, 4]
        for i, j in enumerate(alist, 2):
            self.assertEqual(i, j)


class TestEval(unittest.TestCase):

    def test_strict_addition(self):
        self.assertTrue(eval('2 + 2') == 4)

    def test_wrong_type_argument(self):
        """eval() arg 1 must be a string, bytes or code object"""
        self.assertRaises(TypeError, lambda: eval(2 + 2))


class TestExec(unittest.TestCase):

    def test_code_execution(self):
        code = 'l = []\nfor i in range(3):\n\tl.append(i)\n'
        exec(code)
        self.assertTrue(self.l == [0, 1, 2])

    def test_wrong_type_argument(self):
        """eval() arg 1 must be a string, bytes or code object"""
        self.assertRaises(TypeError, lambda: eval(2 + 2))


class TestFilter(unittest.TestCase):

    def setUp(self):
        self.f = filter(None, [True, False, None, 0, 1, 2])
        self.ff = filter(None, [False, None, 0])
        self.fc = filter(lambda x: x > 2 and x < 5, range(10))

    def test_simple_filter(self):
        """Accepts the true elements only"""
        result = []
        for j in self.f:
            result.append(j)
        self.assertEqual(result, [True, 1, 2])

    def test_simple_false_filter(self):
        """False elements are quashed"""
        result = []
        for j in self.ff:
            result.append(j)
        self.assertEqual(result, [])

    def test_complex_filter(self):
        result = []
        for j in self.fc:
            result.append(j)
        self.assertEqual(result, [3, 4])


class TestFloat(unittest.TestCase):

    def test_simple_conversion(self):
        self.assertEqual(float(1), 1.0)

    def test_string_as_argument(self):
        self.assertEqual(float('1.11'), 1.11)

    def test_expression_as_argument(self):
        self.assertEqual(float(1 / 2), 0.5)

    def test_wrong_type_argument(self):
        self.assertRaises(ValueError, lambda: float('Bob and Alice'))


class TestFormat(unittest.TestCase):
    """http://www.python-course.eu/python3_formatted_output.php"""

    def test_simple_string_formatting(self):
        template = "Just {a} template {b}"
        self.assertEqual(template.format(a='a', b='string'),
                         'Just a template string')

    def test_positional_args_formatting(self):
        template = "This {0} sample {1}"
        self.assertEqual(template.format('is a', 'formatting'),
                         'This is a sample formatting')
