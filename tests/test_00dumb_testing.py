import unittest

"""
By its purpose all programming languages should allow the reader to
understand what exactly this particular text do in a much explicit
manner. The real state of things requires a literate reader with a huge
experience exactly in reading programs and comprehension. Noticeable
that nowadays most programs demand from reader such proficiency that
it made it truly readable for the true geeks only.

"""


class TestLanguageBasemet(unittest.TestCase):

    """
    Lets discover built-in constants True, False, None and already
    existing testing methods one by one

    | Method                    | Checks that          |
    |---------------------------+----------------------+
    | assertEqual(a, b)         | a == b               |
    | assertNotEqual(a, b)      | a != b               |
    | assertTrue(x)             | bool(x) is True      |
    | assertFalse(x)            | bool(x) is False     |
    | assertIs(a, b)            | a is b               |
    | assertIsNot(a, b)         | a is not b           |
    | assertIsNone(x)           | x is None            |
    | assertIsNotNone(x)        | x is not None        |
    | assertIn(a, b)            | a in b               |
    | assertNotIn(a, b)         | a not in b           |
    | assertIsInstance(a, b)    | isinstance(a, b)     |
    | assertNotIsInstance(a, b) | not isinstance(a, b) |

    """

    def test_does_true_ever_exist(self):  # <-- an atomic test case itself
        self.assertTrue(True)  # <-- straight assertion

    def test_does_false_ever_exist(self):  #
        self.assertFalse(False)  #

    def test_does_none_ever_exist(self):  #
        self.assertNone(None)  #

    """ Now it became obious that three built-in values are well-defined
    out of the box.  It is time to compare them against each other
    """


class TestFalse(unittest.TestCase):
    """
    If True does exist, what about the opposite?
    """

    def test_does_false_exist(self):
        self.assertFalse(False)  # the same assertion as above
