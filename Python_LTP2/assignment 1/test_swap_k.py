import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_empty(self):
        """Test swap_k for an empty list."""
        L = []
        a1.swap_k(L,0)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_single(self):
        """Test swap_k for a 1-element list."""
        L = [1]
        a1.swap_k(L,0)
        expected = [1]
        self.assertEqual(L, expected)

    def test_swap_k_two(self):
        """Test swap_k for a 2-element list.(the minimum size of an even-length list)."""
        L = [1,7]
        a1.swap_k(L,1)
        expected = [7,1]
        self.assertEqual(L, expected)

    def test_swap_k_three(self):
        """Test swap_k for a 3-element list (the minimum size of an odd-length list)."""
        L = [1,7,3]
        a1.swap_k(L,1)
        expected = [3,7,1]
        self.assertEqual(L, expected)

    def test_swap_k_five_no_swaps(self):
        """Test swap_k for a 5-element list with no swaps."""
        L = [1,7,4,3,5]
        a1.swap_k(L,0)
        expected = [1,7,4,3,5]
        self.assertEqual(L, expected)

    def test_swap_k_five_single_swap(self):
        """Test swap_k for a 5-element list with a single swap."""
        L = [1,7,4,3,5]
        a1.swap_k(L,1)
        expected = [5,7,4,3,1]
        self.assertEqual(L, expected)   

    def test_swap_k_five_max_swaps(self):
        """Test swap_k for a 5-element list with the maximum number of swaps."""
        L = [1,7,4,3,5]
        a1.swap_k(L,2)
        expected = [3,5,4,1,7]
        self.assertEqual(L, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
