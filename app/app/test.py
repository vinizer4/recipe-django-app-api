"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)