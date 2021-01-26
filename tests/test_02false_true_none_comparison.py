# -*- coding: utf-8 -*-
"""Only code to compare None, True and False"""

import unittest


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
