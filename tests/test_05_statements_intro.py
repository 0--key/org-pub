"""Lets meet equality and non equality operators"""

import unittest

"""The program below is identical by its meaning to previous one, but
it written in a distinct manner with intention to introduce a
statement concept."""


class TestEqualityStatements(unittest.TestCase):

    def test_equal_or_not_equal(self):
        # equality operator is double =
        self.assertTrue(True == True)
        self.assertTrue(False == False)
        self.assertTrue(None == None)
        # non equality operator is !=
        self.assertFalse(True != True)
        self.assertFalse(False != False)
        self.assertFalse(None != None)


"""You might notice that in this case we assert the ~result~ of
statement evaluation. """
