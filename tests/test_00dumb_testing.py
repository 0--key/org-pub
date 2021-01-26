# -*- coding: utf-8 -*-
"""A module-level docstring

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.

It might be unnecessary in our case, when we write a simplified
version of programs. If the aim is a paragon of clarity it should
contain all required attributes of clarity and further support.

You might notice that /coding definition/ on the first string, the
second string begins with tripled double quotes and a sentence there.
They are the obligatory attributes if you have intention to do things
as it should do.

"""


import unittest

"""By its purpose all programming languages should allow the reader to
understand what exactly this particular text do in a much explicit
manner. The real state of things requires a literate reader with a huge
experience exactly in reading programs and comprehension. Noticeable
that nowadays most programs demand from reader such proficiency that
it made them truly readable for the handful of true geeks only.

Nevertheless, this fact usually omitted by specialists, who spent a
huge amount of time reading so overcomplicated texts of programs.
Through time, it became a normal if anybody can't grasp an idea out
from program's source code on the fly.

“It is just lack of experience!”: they say usually. You might object
by notation that several professionals can't catch the essence out
from that text because it poorly written, they answer something like:
“It works well enough to be scrutinized much more precisely.”

Nowadays it is deemed as normal to lack capability to understand
source code even for professionals. Naturally it is abnormal.

"""


class TestLanguageBase(unittest.TestCase):  # <-- class definition
    """begins this reserved word /class/ following by the /name of class/
    and its /parent class/ in the brackets. On first steps it might be
    like a magic mantra to enter the /test suite/.

    The first and foremost taks for testing is to ensure how testing
    tools work. In our case lets begit from the simplest things ever -
    lets discover built-in constants True, False, None with already
    defining testing methods one by one.

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
        # and the sample of in-line comment
        # self-explanatory name of the test case to focus attention
        self.assertTrue(True)  # <-- straight assertion
        # True really exists.
        # if this test do pass with success.

    def test_does_false_ever_exist(self):  # No comments
        self.assertFalse(False)  # False also exists

    def test_does_none_ever_exist(self):  # no comments
        self.assertIsNone(None)  # None also predefined by the language

    """ Now it became obious that three built-in constants are well-defined
    out of the box.  It is very time to compare them against each other.
    """

    def test_none_fasle_true_comparison(self):
        self.assertIsNotNone(True)  # Naturally, neiver False
        self.assertIsNotNone(False)  # nor True are not None
        self.assertFalse(None)  # !! None has a Boolean False
        #
        self.assertIs(True, True)  #
        self.assertIs(False, False)  #
        self.assertIs(None, None)  #
        #
        self.assertNotEqual(False, True)  #
        self.assertNotEqual(True, None)  #
        self.assertNotEqual(False, None)  #
        #
        self.assertIsNotNone(False)  #
        self.assertIsNotNone(True)  #


"""
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

Now we definitely check up several methods of assertion embedded into
Python unittest module, and ensure that three fundamental constants
are also accessible out from the box.

The four methods at the bottom of the table:

 - assertIn(a, b)
 - assertNotIn(a, b)
 - assertIsInstance(a, b)
 - assertNotIsInstance(a, b)

are unnecessary right now because their purpose is testing of
sequencies and instances wich will be introduced a bit later.

In the next chapter new and principal concepts will be introduced.

"""


class TestCompareFundamentals(unittest.TestCase):

    """Now, when we ensure in existence of None, False and Ture constants,
    it is very time to compare them with its own derivatives as zero
    (0), one (1), the letter('A')

    """

    def test_does_zero_really_boolean_false(self):
        self.assertFalse(0)  #
