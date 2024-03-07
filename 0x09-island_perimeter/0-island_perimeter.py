#!/usr/bin/python3
""" Solving Island Perimeter """


def island_perimeter(grid):
    """Calculates  the perimeter of the island described in grid"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    def dfs(i, j):
        nonlocal perimeter
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            perimeter += 1
            return
        if grid[i][j] == -1:
            return
        grid[i][j] = -1
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dfs(i, j)
                return perimeter

    return perimeter
