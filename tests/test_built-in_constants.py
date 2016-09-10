"""Discover how it works by testing"""
import unittest


class TestBuiltInConstants(unittest.TestCase):

    def test_true(self):
        self.assertTrue(1 + 3 == 4)

    def test_false(self):
        self.assertFalse(1 + 4 == 4)

    def test_none(self):
        value = None
        self.assertIsNone(value)
