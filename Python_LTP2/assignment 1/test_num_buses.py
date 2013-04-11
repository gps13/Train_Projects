import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

     def test_num_buses_zero_people(self):
        """Test num_buses for zero people."""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_one_person(self):
        """Test num_buses for one person."""
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_num_buses_single_near_capacity(self):
        """Test num_buses for the number that fills a single bus just under capacity."""
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_single_at_capacity(self):
        """Test num_buses for the number that fills a single bus at capacity."""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_single_over_capacity(self):
        """Test num_buses for the number that is just over capacity for a single bus."""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_multiple_at_capacity(self):
        """Test num_buses for a number that fills multiple buses at capacity (i.e., a number divisible by 50)."""
        actual = a1.num_buses(250)
        expected = 5
        self.assertEqual(actual, expected)

    def test_num_buses_multiple_mixed_occupancy(self):
        """Test num_buses for a number that fills multiple buses but with not all buses at capacity (i.e., a number over 50 but not divisible by 50)."""
        actual = a1.num_buses(251)
        expected = 6
        self.assertEqual(actual, expected) 
     	

if __name__ == '__main__':
    unittest.main(exit=False)
