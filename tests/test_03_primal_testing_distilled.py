"""The initial test suite to check up existence of True, False and
None

Functionally it is the same as the programs above, but compressed for
density and lucidity. 

"""


import unittest

"""Now it is the moment to distill your knowledge about writing
=unittests= in ~Python~. Our previous program allocates too much space
in the case if you're grasp the core idea. Exactly - what is the right
place and content of:

   - Module docstrings;
   - Import section;
   - Multi-line comments;
   - Test class definition;
   - A single test case function;
   - Conclusion multi-line comments

are necesseties to be clear when you're in writing ~Python~ code. Lets
create a much dense test suite out from existing ones

"""


class TestPrimariesExistence(unittest.TestCase):

    """Allocates all the existence tests in a single function"""

    def test_the_existence(self):
        self.assertTrue(True)  # <-- straight assertion
        self.assertFalse(False)  # False also exists
        self.assertIsNone(None)  # None also predefined by the language


"""Naturally that it is more convenient to tame a dense and terse code
blocks which are well-fitted on a single page. Thus, try to make up all
your tests into /coherent/ blocks for clarity purpose."""
