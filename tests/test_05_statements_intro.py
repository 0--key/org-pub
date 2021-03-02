"""Lets meet equality and non equality operators"""

import unittest

"""Lets immerse into statement and operators in it.

The program below is identical by its meaning to previous one, but it
written in a distinct manner with intention to introduce the statement
and operator concepts, which are the pillars of further studying of
programming."""


class TestEqualityStatements(unittest.TestCase):

    def test_equality_operator(self):
        # equality operator is double =
        self.assertTrue(True == True)  # <-- equality statements
        self.assertTrue(False == False)  # are inside the brackets
        # and they do evaluate when the program do launch
        self.assertTrue(None == None)

    def test_non_equality_operator(self):
        # non equality operator is !=
        self.assertFalse(True != True)  # <-- non-equality statements
        self.assertFalse(False != False)  # are inside the brackets
        # and they do evaluate when you're launch the program
        self.assertFalse(None != None)


"""
You might notice that in these cases we:
 - assert the ~result~ of statement evaluation;
 - disclose the magic above only two operators
"""
