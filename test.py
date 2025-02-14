from fractions import Fraction
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

# The test results show that one of the tests failed while th other passed. 
# The fail occured in the test_list_fraction test which was testing if the summing of a list of fractions equals 1.
# The actual result is 9/10, this means the sum function is working correctly but the expectation for the test is incorrect.
# To pass the test you could make the expected value self.assertEqual(result, Fraction(9,10))