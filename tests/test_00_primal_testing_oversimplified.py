import unittest


class TestLanguagePrimals(unittest.TestCase):

    def test_does_true_ever_exist(self):
        self.assertTrue(True)

    def test_does_false_ever_exist(self):
        self.assertFalse(False)

    def test_does_none_ever_exist(self):
        self.assertIsNone(None)
