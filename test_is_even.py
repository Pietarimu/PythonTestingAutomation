import unittest
from is_even import is_even

# comment

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(5))

    def test_zero(self):
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()
