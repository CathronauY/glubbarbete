import unittest
from calculator_comandline import *

class AddTests(unittest.TestCase):
    def test_two_plus_one_is_tree(self):
        self.assertEqual(3, calc_add(2, 1))
        self.assertEqual(3, calc_add(1, 2))
    
    def test_zero_plus_zero_is_zero(self):
        self.assertEqual(0, calc_add(0, 0))

class SubtractTests(unittest.TestCase):
    def test_one_minus_one_is_zero(self):
        self.assertEqual(0, calc_subtract(1, 1))
    
    def test_two_minus_one_is_one(self):
        self.assertEqual(1, calc_subtract(2, 1))

class TimesTests(unittest.TestCase):
    def test_one_times_one_is_one(self):
        self.assertEqual(1, calc_times(1, 1))
    
    def test_one_times_two_is_two(self):
        self.assertEqual(2, calc_times(1, 2))
        self.assertEqual(2, calc_times(2, 1))
    
    def test_one_times_tree_is_tree(self):
        self.assertEqual(3, calc_times(1, 3))
        self.assertEqual(3, calc_times(3, 1))
    
    def test_two_times_tree_is_six(self):
        self.assertEqual(6, calc_times(2, 3))
        self.assertEqual(6, calc_times(3, 2))

if __name__ == "__main__":
    unittest.main()