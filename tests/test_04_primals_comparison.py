"""Only code to compare None, True and False"""

import unittest

"""If in previous tests we were introduced by three test methods only:

 - assertFalse();
 - assertTrue();
 - assertIsNone();

Right now it is a right time to show several additional ones:

 - assertIs() - identity assertion;
 - assertIsNotNone() - not None assertion;
 - assertNotEqual() - non equality assertion; 
"""


class TestCompareFundamentals(unittest.TestCase):

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


"""Seems it is much elegant than before, but less self-explanatory"""
