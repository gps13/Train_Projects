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

        >>> rat1 = Rat('P', 1, 4)
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
        >>> print rat1
        J at (4, 3) ate 2 sprouts.

        """

        result = self.symbol + ' at ('+str(self.row)+', '+str(self.col)+') ate '+str(self.num_sprous_eaten)+' sprouts.'
        return result

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        maze initializetion

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Rat('J', 1, 1),
      Rat('P', 1, 4))
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprous_left = 3

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        if there is a wall at the given row and column of the maze.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Rat('J', 1, 1),
      Rat('P', 1, 4))
        >>> mymaze.is_wall(1,0)
        True
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be returned rather than HALL.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Rat('J', 1, 1),
      Rat('P', 1, 4))
        >>> mymaze.get_character(0,0)
        '#'
        >>> mymaze.get_character(2,1)
        '.'
        >>> mymaze.get_character(4,1)
        '@'
        >>> mymaze.get_character(1,1)
        'J'
        >>> mymaze.get_character(1,4)
        'P'
        """
        if [self.rat_1.row,self.rat_1.col] == [row,col]:
            return self.rat_1.symbol
        elif [self.rat_2.row,self.rat_2.col] == [row,col]:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, Rat, vertical, horizonatl):
        """ Maze, Rat, int, int) -> bool

       Move the rat in the given direction, unless there is a wall in the way. 
       Also, check for a Brussels sprout at that location
       Return True if and only if there wasn't a wall in the way.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Rat('J', 1, 1),
      Rat('P', 1, 4))
        >>> mymaze.get_character(0,0)
        '#'
        >>> mymaze.get_character(2,1)
        '.'
        >>> mymaze.get_character(4,1)
        '@'
        >>> mymaze.get_character(1,1)
        'J'
        >>> mymaze.get_character(1,4)
        'P'
        """
        if [self.rat_1.row,self.rat_1.col] == [row,col]:
            return self.rat_1.symbol
        elif [self.rat_2.row,self.rat_2.col] == [row,col]:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]