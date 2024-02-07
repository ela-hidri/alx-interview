#!/usr/bin/python3
"""Solving N queens"""
from sys import argv


def isDegit(n):
    """check if digit"""
    try:
        int(n)
        return True
    except ValueError:
        return False


def canPlace(n, i, x, mx):
    """check if can place qween"""
    for m in range(n):
        if mx[m][x] == 1 or mx[i][m] == 1: return False
    for m in range(n):
            if (i + m < n and x + m < n) : 
                if (mx[i + m][x + m] == 1) : return False
            if (i + m < n and x - m >= 0) :
                if (mx[i + m][x - m] == 1): return False
            if i - m >= 0  and x + m < n: 
                if (mx[i - m][x + m] == 1): return False
            if (i - m >= 0 and x - m >= 0) : 
                if(mx[i - m][x - m] == 1): return False 
    return True


def printSlt(mx, n):
    """print solution"""
    rst = []

    for l in range(0, n):
        for ll in range(0, n):
            if mx[l][ll] == 1:
                rst.append([l, ll])
    print(rst)


def placeQueens(st, n, row):
    """place Queens"""
    if row == n:
        printSlt(st, n)
        return

    for i in range(n):
        if canPlace(n, i, row, mx):
            mx[i][row] = 1
            placeQueens(mx, n, row + 1)
            mx[i][row] = 0


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = argv[1]
    if not isDegit(n):
        print("N must be a number")
        exit(1)
    n = int(n)
    if  n < 4:
        print("N must be at least 4")
        exit(1)
    mx = [[0 for _ in range(n)] for _ in range(n)]
    i = 0
    x = 0
    placeQueens(mx, n, 0)
