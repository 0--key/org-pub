# -*- coding: utf-8 -*-
"""Now it is the moment to distill your knowledge about writing
=unittests= in ~Python~. Our previous work in
=tests/test_00dumb_testing.py= spare too much place in case if you're
grasp the core idea. Exactly:

   - Module comments;
   - Import section;
   - Test class definition;
   - Set of test cases

are necesseties to be clear when you're in writing ~Python~ code. Lets
create a much dense test suite out from existing one and put it in a
new file =tests/test_01false_true_none_existence.py=

"""

import unittest

"""The initial Python test suite

Asserts the existence True, False and None in Python
"""


class TestFundamentalConstantsExistence(unittest.TestCase):

    """Put all the existence tests together"""

    def test_the_existence(self):
        self.assertTrue(True)  # <-- straight assertion
        self.assertFalse(False)  # False also exists
        self.assertIsNone(None)  # None also predefined by the language
