"""
Lets discover built-in constants True, False, None and already
existing testing methods one by one

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
import unittest


class TestTrue(unittest.TestCase):

    def test_does_true_exist(self):  # <-- an atomic test case itself
        self.assertTrue(True)  # <-- straight assertion


class TestFalse(unittest.TestCase):
    """
    If True does exist, what about the opposite?
    """

    def test_does_false_exist(self):
        self.assertFalse(False)  # the same assertion as above
