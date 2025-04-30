import unittest                                       # importing unittest to test my software
import calculator_commandline as calc                  # Importing the python file to test

class AddTests(unittest.TestCase):                    # The class to test the add function
    def test_two_plus_one_is_tree(self):              # A function to test if the add function can add two and one
        self.assertEqual(3, calc.calc_add(2, 1))      # 2 + 1
        self.assertEqual(3, calc.calc_add(1, 2))      # 1 + 2
    
    def test_zero_plus_zero_is_zero(self):            # A function to test if the add function can add zero and zero
        self.assertEqual(0, calc.calc_add(0, 0))      # 0 + 0

class SubtractTests(unittest.TestCase):               # The class to test the subtract function
    def test_one_minus_one_is_zero(self):             # A function to test if the subtract function can subtract one and one
        self.assertEqual(0, calc.calc_subtract(1, 1)) # 1 - 1
    
    def test_two_minus_one_is_one(self):              # A function to test if the subtract function can subtract two and one
        self.assertEqual(1, calc.calc_subtract(2, 1)) # 2 - 1

class TimesTests(unittest.TestCase):                  # The class to test the times function
    def test_one_times_one_is_one(self):              # A function to test if the times function can take one times one
        self.assertEqual(1, calc.calc_times(1, 1))    # 1 * 1
    
    def test_one_times_two_is_two(self):              # A function to test if the times function can take one times two
        self.assertEqual(2, calc.calc_times(1, 2))    # 1 * 2
        self.assertEqual(2, calc.calc_times(2, 1))    # 2 * 1
    
    def test_one_times_tree_is_tree(self):            # A function to test if the times function can take one times tree
        self.assertEqual(3, calc.calc_times(1, 3))    # 1 * 3
        self.assertEqual(3, calc.calc_times(3, 1))    # 3 * 2
    
    def test_two_times_tree_is_six(self):             # A function to test if the times function can take two times six
        self.assertEqual(6, calc.calc_times(2, 3))    # 2 * 6
        self.assertEqual(6, calc.calc_times(3, 2))    # 6 * 2

class DivideTests(unittest.TestCase):                 # The class to test the divide function
    def test_zero_divided_by_zero_is_zero(self):      # A function to test if the divide function can divide zero and zero
        self.assertEqual(0, calc.calc_divide(0, 0))   # 0 / 0
    
    def test_one_divided_by_one_is_one(self):         # A function to test if the divide function can divide one and two
        self.assertEqual(1, calc.calc_divide(1, 1))   # 1 / 1

if __name__ == "__main__":                            # Code that only runs if you run this specific file
    unittest.main()                                   # Runs all the tests