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
        l = []
        code = 'for i in range(3):\n\tl.append(i)\n'
        exec(code)
        self.assertTrue(l == [0, 1, 2])

    def test_wrong_type_argument(self):
        self.assertRaises(TypeError, lambda: exec(2 + 2))


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


class TestFrozenset(unittest.TestCase):
    """Tuples are immutable lists, frozensets are immutable sets"""

    def test_simple_frozen_set(self):
        self.assertEqual(frozenset('def'), set('def'))

    def test_only_unique_elements(self):
        self.assertEqual(frozenset('defdek'), set('dekdef'))


class TestGetattr(unittest.TestCase):
    """Get a named attribute from an object"""

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj = Pear()

    def test_existing_attr(self):
        self.assertEqual(getattr(self.obj, 'size'), 123)

    def test_non_existing_attr(self):
        self.assertRaises(AttributeError, lambda: getattr(self.obj, 'shape'))

    def test_default_value(self):
        self.assertEqual(getattr(self.obj, 'shape', 'pyramid'), 'pyramid')


class TestGlobals(unittest.TestCase):
    """Return the dictionary containing the current scope's global
    variables
    """

    def test_current_scope_classes(self):
        self.assertTrue('TestGetattr' and 'TestGlobals' in globals())


class TestHasattr(unittest.TestCase):
    """Return whether the object has an attribute with the given name"""

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj = Pear()

    def test_existing_attr(self):
        self.assertTrue(hasattr(self.obj, 'size'))

    def test_non_existing_attr(self):
        self.assertFalse(hasattr(self.obj, 'shape'))


class TestHash(unittest.TestCase):
    """Return a hash value for the object"""

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj1 = Pear()
        self.obj2 = Pear()

    def test_the_same_object(self):
        self.assertEqual(hash(self.obj1), hash(self.obj1))

    def test_different_objects(self):
        """Different objects with equal properties has different
        hashes"""
        self.assertNotEqual(hash(self.obj1), hash(self.obj2))

    def test_equal_attributes(self):
        self.assertEqual(hash(self.obj2.size), hash(self.obj1.size))


class TestHelp(unittest.TestCase):

    def test_help_on_existing_function(self):
        self.assertIsNone(help(zip))

    def test_help_none_existing_function(self):
        self.assertRaises(NameError, lambda: help(mod))


class TestHex(unittest.TestCase):

    def test_integer_argument(self):
        self.assertEqual(hex(3735928559), '0xdeadbeef')

    def test_float_argument(self):
        self.assertRaises(TypeError, lambda: hex(2.2))


class TestId(unittest.TestCase):

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj1 = Pear()
        self.obj2 = self.obj3 = Pear()

    def test_different_objects(self):
        self.assertNotEqual(id(self.obj1), id(self.obj2))

    def test_same_objects(self):
        self.assertEqual(id(self.obj2), id(self.obj3))


class TestId(unittest.TestCase):

    def setUp(self):
        """Create a mockup object for testing purposes"""
        class Pear():

            def __init__(self):
                self.size = 123
                self.color = 'green'

        self.obj1 = Pear()
        self.obj2 = self.obj3 = Pear()

    def test_different_objects(self):
        self.assertNotEqual(id(self.obj1), id(self.obj2))

    def test_same_objects(self):
        self.assertEqual(id(self.obj2), id(self.obj3))


class TestInput(unittest.TestCase):
    """::"""

    def test_tap(self):
        """TODO"""
        self.assertTrue(True)


class TestInt(unittest.TestCase):

    def test_integer_argument(self):
        self.assertEqual(int(3735928559), 3735928559)

    def test_float_argument(self):
        self.assertEqual(int(2.2), 2)

    def test_float_negative_argument(self):
        self.assertEqual(int(-2.2), -2)

    def test_string_argument(self):
        self.assertRaises(ValueError, lambda: int('a'))


class TestIsinstance(unittest.TestCase):

    def test_argument_type(self):
        self.assertTrue(isinstance('Bob and Alice', str))

    def test_argument_class(self):
        class Pear():
            pass

        self.obj = Pear()
        self.assertTrue(isinstance(self.obj, Pear))


class TestIssubclass(unittest.TestCase):

    def test_the_mock_object_direct_relation(self):

        class Fruit():
            pass

        class Pear(Fruit):
            pass

        self.assertTrue(issubclass(Pear, Fruit))

    def test_the_mock_object_reverse_relation(self):

        class Fruit():
            pass

        class Pear(Fruit):
            pass

        self.assertFalse(issubclass(Fruit, Pear))


class TestIter(unittest.TestCase):

    def setUp(self):
        self.mockup_list = [1, 2, 3]
        self.mockup_string = 'This is EOF the test string'

    def test_strict_iteration(self):
        self.assertTrue(iter(self.mockup_list))

    def test_all_elements_in_sequence(self):
        l = iter(self.mockup_list)
        m = []
        for i in l:
            m.append(i)
        self.assertEqual(m, [1, 2, 3])

    def test_separate_elements_iteration(self):
        i = iter(self.mockup_list)
        a = next(i)
        b = next(i)
        c = next(i)
        self.assertTrue(a == 1 and b == 2 and c == 3)


class TestLen(unittest.TestCase):

    def test_lenghth_of_string(self):
        self.assertEqual(len('Ahab'), 4)

    def test_lenghth_of_list(self):
        self.assertEqual(len([1, 2, 3]), 3)


class TestList(unittest.TestCase):

    def test_simple_list_of_letters(self):
        self.assertEqual(list('Pear'), ['P', 'e', 'a', 'r'])

    def test_convert_tuple_into_list(self):
        self.assertEqual(list((1, 2, 3)), [1, 2, 3])

    def test_convert_dictionary_into_list(self):
        # dictionary is an unordered sequence by its definition
        self.assertTrue(list({'a': 1, 'b': 2}) == ['a', 'b'] or ['b', 'a'])

    def test_not_iterable_argument(self):
        self.assertRaises(TypeError, lambda: list(123.11))


d = {'this': 1, 'is': 2, 'a': 3, 'global': 4, 'variable': 5}


class TestLocals_and_Globals(unittest.TestCase):

    def setUp(self):
        """Cooke the mixture of objects"""
        self.d = {'the': 1, 'global': 2, 'dictionary': 3}

    def test_string_as_argument(self):
        l = "Just a local variable"
        self.assertEqual(locals()['l'], "Just a local variable")

    def test_reassign_variable(self):
        d = {'a': 1, 'simple': 2, 'dictionary': 3}
        self.assertEqual(locals()['d']['a'], 1)
        self.assertEqual(locals()['d']['simple'], 2)

    def test_global_dict(self):
        self.assertEqual(globals()['d']['this'], 1)


class TestMap(unittest.TestCase):

    def test_map_under_num_seq(self):
        i = map(lambda x: x * 1.25, [4, 8, 12])
        self.assertTrue(next(i) == 5 and next(i) == 10 and
                        next(i) == 15)


class TestMax(unittest.TestCase):

    def test_simple_list_of_int(self):
        self.assertTrue(max([1, 2, 3]) == 3)

    def test_simple_list_of_letters(self):
        self.assertTrue(max(['a', 'b', 'c']) == 'c')

    def test_list_of_strings(self):
        self.assertTrue(max('Aaron', 'Bobby', 'Scotty') == 'Scotty')

        def test_string_values_comparison(self):
            self.assertTrue(max(['1', '100', '111', '2']) == '2')

    def test_with_key_function(self):
        self.assertTrue(max(['1', '100', '111', '2'],
                            key=lambda x: int(x)) == '111')

    def test_with_key_function_1(self):
        self.assertTrue(max('Aaron', 'Bobby', 'Scotty',
                            key=lambda x: x[2]) == 'Aaron')


class TestMemoryview(unittest.TestCase):

    def setUp(self):
        self.v = memoryview(b'abcefg')

    def test_simple_behaviour(self):
        self.assertTrue(self.v[0] == 97 and
                        self.v[-1] == 103)


class TestMin(unittest.TestCase):

    def test_simple_behaviour_with_string_argument(self):
        self.assertEqual(min('abc'), 'a')

    def test_simple_behaviour_with_list_of_int_argument(self):
        self.assertEqual(min([2, 3, 1]), 1)

    def test_with_key_function(self):
        self.assertTrue(min('Aaron', 'Bobby', 'Scotty',
                            key=lambda x: x[2]) == 'Bobby')


class TestNext(unittest.TestCase):

    def setUp(self):
        self.i = iter('abcdef')

    def test_iteration(self):
        self.assertTrue(next(self.i) == 'a' and
                        next(self.i) == 'b')

    def test_continuous_iteration(self):
        self.assertFalse(next(self.i) == 'c')


class TestObject(unittest.TestCase):
    """The most base type"""

    def setUp(self):
        self.obj = object()

    def test_simple_behaviour(self):
        self.assertTrue(self.obj)


class TestOct(unittest.TestCase):

    def test_integer_argument(self):
        self.assertEqual(oct(11), '0o13')

    def test_negative_argument(self):
        self.assertEqual(oct(-11), '-0o13')

    def test_string_argument(self):
        self.assertRaises(TypeError, lambda: oct('a'))


class TestOpen(unittest.TestCase):

    def test_simple_behaviour(self):
        pass


class TestOrd(unittest.TestCase):

    def test_simple_behaviour(self):
        self.assertTrue(ord('a') == 97)

    def test_wrong_argument(self):
        self.assertRaises(TypeError, lambda: ord('ab'))


class TestPow(unittest.TestCase):

    def test_simple_behaviour(self):
        self.assertEqual(pow(2, 2), 4)

    def test_complex_power(self):
        self.assertAlmostEqual(pow(9, 0.5), 3)

    def test_specific_third_argument(self):
        self.assertTrue(pow(3, 3, 2) == 1)


class TestPrint(unittest.TestCase):

    def test_simple_behaviour(self):
        self.assertIsNone(print('Hellow World'))


class TestProperty(unittest.TestCase):

    def setUp(self):
        """property(fget=None, fset=None, fdel=None, doc=None) ->
        property attribute"""

        class C(object):
            @property
            def x(self):
                "I am the 'x' property."
                return self._x

            @x.setter
            def x(self, value):
                self._x = value

                @x.deleter
            def x(self):
                del self._x

        class D(object):
      
            def getx(self):
                return self._x
      
            def setx(self, value):
                self._x = value
          
            def delx(self):
                del self._x
            x = property(getx, setx, delx, "I'm the 'x' property.")

        self.obj_1 = C()
        self.obj_2 = D()

    def test_simple_behaviour(self):
        self.assertEqual(self.obj_1.x, self.obj_2.x)


class TestRange(unittest.TestCase):

    def setUp(self):
        self.A = range(3)
        self.B = range(3, 10, 2)
        self.C = range(3, 11, 2)
        self.D = range(-3, -10, -2)

    def test_simple_behaviour(self):
        l = []
        for i in self.A:
            l.append(i)
        self.assertEqual(l, [0, 1, 2])

    def test_with_step(self):
        l = []
        for i in self.B:
            l.append(i)
        self.assertEqual(l, [3, 5, 7, 9])

    def test_with_step_and_right_exclude(self):
        l = []
        for i in self.C:
            l.append(i)
        self.assertEqual(l, [3, 5, 7, 9])

    def test_negative_range(self):
        l = []
        for i in self.D:
            l.append(i)
        self.assertEqual(l, [-3, -5, -7, -9])


class TestRepr(unittest.TestCase):

    def setUp(self):
        class Pear():

            def __init__(self):
                self.size = 124
                self.color = 'green'

            def __repr__(self):
                return('This is a particular representation')

        self.obj = Pear()

    def test_simple_behaviour(self):
        self.assertTrue(repr(123) == '123' and
                        repr([1, 2, 3]) == '[1, 2, 3]')

    def test_object_representation(self):
        self.assertTrue(repr(self.obj) ==
                        'This is a particular representation')


class TestReversed(unittest.TestCase):
    """reversed(sequence) -> reverse iterator over values of the sequence"""

    def setUp(self):
        self.s = reversed('abc')
        self.d = reversed([1, 2, 3])

    def test_simple_behaviour(self):
        self.assertTrue(next(self.s) == 'c' and
                        next(self.s) == 'b')

    def test_list_as_argument(self):
        self.assertTrue(next(self.d) == 3 and
                        next(self.d) == 2)
