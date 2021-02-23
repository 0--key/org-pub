"""A module-level docstring brief single-line description

A module-level docstring multi-line description. Notice the second line
with a straight encoding definition. 

Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.

"""

import unittest  # <-- import header

"""The place below an import section reserved for multi-line comments
which might be utilized as a preamble to your Python program. It is
being red only by humans, not compiled ever, and permits author to
write down all stuff necessary to be at the foremost place.

It might be unnecessary in our case, when we write a simplified
version of programs. But our basic aim is to serve as paragon of
clarity thus it should contain all lucidity's attributes.

By its purpose all programming languages should allow readers to
perceive what exactly this particular text do in a much explicit
manner. The real state of things, when programs are habitually
clogged, requires from a literate reader tons of time and perceverance
for litter decluttering and a core idea grasp. Noticeable that
nowadays most programs demand from its reader such literacy that it
made them actually indecipherable for humans and in most cases
extremely knotty even to its author.

Nevertheless, this fact usually omitted by specialists, who spent a
huge amount of time reading so overcomplicated texts of programs.
Through time, it became a normal if anybody can't make an idea out
from program's text on the fly.

“It is just lack of experience!”: they say usually. You might object
by notation that several professionals can't catch the essence out
from that text because it is poorly written, they answer something
like: “It works well enough to be scrutinized much diligently.”

"""


class TestLanguagePrimals(unittest.TestCase):  # <-- class definition
    """The class-level for a brief single-line docstring

    Class defininition begins this reserved word /class/ following by
    the /name of class/ and its /parent class/ in the brackets. On
    first steps it might be like a magic mantra to enter the /test
    suite/

    """

    def test_does_true_ever_exist(self):  # <-- an atomic test case itself
        """A single-line brief description for particular test case"""
        self.assertTrue(True)  # <-- straight assertion
        # If this test passed successfully than True is really exists

    def test_does_false_ever_exist(self):  # another test case
        """A single-line brief description for particular test case"""
        self.assertFalse(False)  # False also exists

    def test_does_none_ever_exist(self):  # the last primitive test case
        """A single-line brief description for particular test case"""
        self.assertIsNone(None)  # None also predefined by the language


"""This is a conclusion multi-line comment section. It is useful to
put all bottom-line conclusion there."""
