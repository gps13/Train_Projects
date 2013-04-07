import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def tests_num_of_buses(self):
    	"""Test num_buses where you need to find 
    	the minimum number of buses required to transport a number of people.
    	This tests "number of people" > "single bus capacity"
    	Each bus can hold 50 people
    	"""
    	people = 75
    	self.assertEqual(a1.num_buses(people),2)
    	

if __name__ == '__main__':
    unittest.main(exit=False)
