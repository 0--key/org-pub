"""Lets meet equality and non equality operators"""

import unittest

"""The program below is identical by its meaning to previous one, but
it written in a distinct manner with intention to introduce the
statement and operator concepts."""


class TestFundamentalStatements(unittest.TestCase):

    def test_equality_operator(self):
        # equality operator is double =
        self.assertTrue(True == True)  # <-- equality statements
        self.assertTrue(False == False)  # are inside the brackets
        # and they evaluated when the program do launch
        self.assertTrue(None == None)

    def test_non_equality_operator(self):
        # non equality operator is !=
        self.assertFalse(True != True)
        self.assertFalse(False != False)
        self.assertFalse(None != None)


"""You might notice that in this case we assert the ~result~ of
statement evaluation. """
