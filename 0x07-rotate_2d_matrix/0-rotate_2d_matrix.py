#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): A 2D matrix to rotate

    The function modifies the matrix in-place by:
    1. Transposing the matrix (swapping rows and columns)
    2. Reversing each row

    This approach effectively rotates the matrix 90 degrees clockwise.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
