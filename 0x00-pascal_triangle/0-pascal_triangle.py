#!/usr/bin/python3
"""
Pascal's Triangle
Function that returns a list of lists of integers representing the triangle.
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1

        # Fill in the middle v alues
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
