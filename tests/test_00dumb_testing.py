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


class TestLanguageBasemet(unittest.TestCase):

    """The first and foremost taks for testing is to ensure how testing
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
        self.assertTrue(True)  # <-- straight assertion

    def test_does_false_ever_exist(self):  #
        self.assertFalse(False)  #

    def test_does_none_ever_exist(self):  #
        self.assertIsNone(None)  #

    """ Now it became obious that three built-in values are well-defined
    out of the box.  It is very time to compare them against each other.
    """

    def test_none_fasle_true_comparison(self):
        self.assertIsNotNone(True)  # Naturally, niever False
        self.assertIsNotNone(False)  # nor True are not None
        self.assertFalse(None)  # !! None is a Boolean False


class TestCompareFundamentals(unittest.TestCase):

    """Now, when we ensure in existence of None, False and Ture constants,
    it is very time to compare them with its own derivatives as zero
    (0), one (1), the letter('A')

    """

    def test_does_zero_really_boolean_false(self):
        self.assertFalse(0)  #
