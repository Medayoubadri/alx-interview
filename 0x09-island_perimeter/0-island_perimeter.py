#!/usr/bin/python3
"""
Module for calculating island perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list): A list of list of integers where:
                    - 0 represents water
                    - 1 represents land

    Returns:
        int: The perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                cell_perimeter = 4

                if i > 0 and grid[i - 1][j] == 1:
                    cell_perimeter -= 1

                if i < rows - 1 and grid[i + 1][j] == 1:
                    cell_perimeter -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    cell_perimeter -= 1

                if j < cols - 1 and grid[i][j + 1] == 1:
                    cell_perimeter -= 1

                perimeter += cell_perimeter

    return perimeter
