# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

		rat initializetion

        >>> Rat('P', 1, 4)
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprous_eaten = 0
    

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        rat location

        >>> rat1 = Rat('P', 1, 4)
        >>> rat1.set_location(2,3)
        """
        self.row = row
        self.col = col
    def eat_sprout(self):
        """ (Rat) -> NoneType

        rat ate a sprout

        >>> rat1 = Rat('P', 1, 4)
        >>> rat1.set_location(2,3)
        >>> rat1.eat_sprout()
        """
        self.num_sprous_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat, in this format:
		symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat1 = Rat('J', 1, 4)
        >>> rat1.set_location(4,3)
        >>> rat1.eat_sprout()
        >>> rat1.eat_sprout()
        'J at (4, 3) ate 2 sprouts.'

        """

        result = self.symbol + ' at ('+str(self.row)+', '+str(self.col)+') ate '+str(self.num_sprous_eaten)+' sprouts.'
        return result

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.