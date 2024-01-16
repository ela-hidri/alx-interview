#!/usr/bin/python3
"""
Solve Minimum Operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly n
    H characters in the file

    Keyword arguments:
    n -- n H characters in the file
    Return: fewest number of operations or 0 if n is impossible
    """
    if not isinstance(n, int) or n <= 0:
        return 0
    divs = []
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            divs.append(i)
        else:
            i += 1
    return sum(divs)
