import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_case_swap_num(self):
    	"""Test swap_k where in a list we swap the 
    	first k items with the last k items.
    	Precondtion: 0 <= k <= len(L) // 2
		We test a 2 items list
    	"""
    	list1 = [1, 2]
    	numbers_to_swap = 1
    	list1_expected = [2,1]

    	a1.swap_k(list1,numbers_to_swap)

    	self.assertEqual(list1, list1_expected)




if __name__ == '__main__':
    unittest.main(exit=False)
