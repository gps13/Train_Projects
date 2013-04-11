import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty(self):
        """Test stock_price_summary for an empty list."""
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_single_negative(self):
        """Test stock_price_summary for a single negative value."""
        actual = a1.stock_price_summary([-5.01])
        expected = (0,-5.01)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_single_positive(self):
        """Test stock_price_summary for a single positive value."""
        actual = a1.stock_price_summary([5.01])
        expected = (5.01,0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_all_negative(self):
        """Test stock_price_summary for multiple values that are all negative."""
        actual = a1.stock_price_summary([-2.2, -0.1, -5, -7.02])
        expected = (0,-14.32)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_all_positive(self):
        """Test stock_price_summary for multiple values that are all positive."""
        actual = a1.stock_price_summary([2.2, 0.1, 5, 7.02])
        expected = (14.32,0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_all_zeros(self):
        """Test stock_price_summary for multiple values that are all zero."""
        actual = a1.stock_price_summary([0, 0, 0, 0])
        expected = (0,0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_stock_price_summary_mixed(self):
        """Test stock_price_summary for mixed values."""
        actual = a1.stock_price_summary([2.2, 0, -5, 7.02])
        expected = (9.22,-5)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])



if __name__ == '__main__':
    unittest.main(exit=False)
