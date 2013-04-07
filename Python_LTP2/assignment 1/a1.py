def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    """
    # BUGGY IPLEMENTATION!!! DEV WITH FLOAT -> RESULT=FLOAT !!!
    if n%50 != 0:
        return n/50.0 + 1
    else:
        return n/50.0

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    # BUGGY IPLEMENTATION!!! gains = losses SHOULD BE 0 !!!
    gains = losses = 10
    for price in price_changes:
        if price > 0:
            gains += price
        else:
            losses += price

    return gains,losses


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> swap_k([1, 2, 3, 4, 5, 6], 2)
    [5, 6, 3, 4, 1, 2]
    >>> swap_k([1, 2, 3, 4, 5, 6], 3)
    [4, 5, 6, 1, 2, 3]  
    """
    for num in range(k):
        # CORRECT  L[num],L[len(L)-2+num]=L[len(L)-2+num], L[num]
        # BUGGY
        L[num],L[len(L)-2]=L[len(L)-2], L[num]
    return L



if __name__ == '__main__':
    import doctest
    doctest.testmod()
