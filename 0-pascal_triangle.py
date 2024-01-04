#!/usr/bin/python3

"""
Pascal’s triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    list = [[1]]
    m = [1]
    if n <= 0:
        return []
    for i in range(1, n):
        for j in range(1, i):
            m.append(list[i - 1][j] + list[i - 1][j - 1])
        m.append(1)
        list.append(m)
        m = [1]
    return list
