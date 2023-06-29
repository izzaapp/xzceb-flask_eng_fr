# pylint: disable=invalid-name
"""Module for full test translator.py ."""
import unittest
from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    """Test class for translator.py ."""

    def test_englishToFrench_equal(self):
        """Test (equal) englishToFrench function from translator.py ."""
        self.assertEqual( englishToFrench('hello'), 'bonjour' )

    def test_englishToFrench_notEqual(self):
        """Test (notEqual) englishToFrench function from translator.py ."""
        self.assertNotEqual( englishToFrench('hello'), 'halo' )


    def test_frenchToEnglish_equal(self):
        """Test (equal) frenchToEnglish function from translator.py ."""
        self.assertEqual( frenchToEnglish('bonjour'), 'hello' )

    def test_frenchToEnglish_notEqual(self):
        """Test (notEqual) frenchToEnglish function from translator.py ."""
        self.assertNotEqual( frenchToEnglish('bonjour'), 'halo' )

if __name__=='__main__':
    unittest.main()
