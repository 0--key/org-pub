import unittests  # <-- import header


class TestLanguagePrimals(unittest.TestCase):  # <-- class definition

    def test_does_true_ever_exist(self):  # <-- an atomic test case itself
        # and the sample of in-line comment
        # self-explanatory name of the test case to focus attention
        self.assertTrue(True)  # <-- straight assertion
        # If this test passed successfully than True is really exists

    def test_does_false_ever_exist(self):  # No comments
        self.assertFalse(False)  # False also exists

    def test_does_none_ever_exist(self):  # no comments
        self.assertIsNone(None)  # None also predefined by the language
