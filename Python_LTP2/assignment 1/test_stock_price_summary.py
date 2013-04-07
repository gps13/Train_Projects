import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_sum(self):
    	"""Test stock_price_summary with a list of stock price changes. Should return
    	a 2-item tuple. First item is the sum of the gains in price_changes and
    	the second is the sum of the losses in price_changes. The list contains all negative
    	prices so the result would be no gains and only losses
    	"""
    	portfolio = [0, 0, -0.02, -0.14, 0, 0, 0, -0.01]
    	wealth_expected = (0, -0.17)
    	
    	self.assertEqual(a1.stock_price_summary(portfolio),wealth_expected)


if __name__ == '__main__':
    unittest.main(exit=False)
