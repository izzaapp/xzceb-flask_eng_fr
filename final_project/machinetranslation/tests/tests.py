# pylint: disable=invalid-name
"""Module for testing translator.py ."""
import unittest
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    """Test class for translator.py ."""

    def test_englishToFrench(self):
        """Test englishToFrench function from translator.py ."""
        self.assertEqual( englishToFrench('hello'), 'bonjour' )

    def test_frenchToEnglish(self):
        """Test frenchToEnglish function from translator.py ."""
        self.assertEqual( frenchToEnglish('bonjour'), 'hello' )

if __name__=='__main__':
    unittest.main()
