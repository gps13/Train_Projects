class WordplayStr(str):
    """docstring for WordplayStr"""

    def same_start_and_end(self):
        """ (WordplayStr) -> bool
        Precondition: len(self) != 0
        Return wheter self start and ends with the same letter

        >>> s=WordplayStr('abracadabra')
        >>> s.same_start_and_end()
        True
        >>> s=WordplayStr('canoe')
        >>> s.same_start_and_end()
        False
        """
        Return self[0]==self[-1]
if __name__ == '__main__':
    import doctest
    doctest.testmod()