import unittest
import divisors

class TestDivisors(unittest.TestCase):
    """example unittest test methods for get_divisors"""
        
        def test_divisors_example_1(self):
            ''' Test get_divisors with 8 and [1, 2, 3]'''

            actual = divisors.get_divisors(8, [1, 2, 3])
            expected = [1,2]
            self.assertEqual(actual,expected)

        def test_divisors_example_2(self):
            ''' Test get_divisors with 4 and [-2, 0, 2]'''

            actual = divisors.get_divisors(8, [1, 2, 3])
            expected = [-2,2]
            self.assertEqual(actual,expected)


        if __name__ == '__main__':
            unittest.main(exit=False)