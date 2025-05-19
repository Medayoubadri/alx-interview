#!/usr/bin/python3
"""
Solves the N-Queens puzzle.
"""
import sys


def solve_nqueens(n):
    """
    Solves the N-Queens puzzle.
    Args:
        n: The number of queens.
    Returns:
        A list of solutions.
    """
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        """
        Checks if placing a queen at board[row][col] is safe.
        """
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def find_solutions(row):
        """
        Recursively finds all solutions.
        """
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(board)])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                find_solutions(row + 1)
                board[row] = -1

    find_solutions(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n_value = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n_value < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = solve_nqueens(n_value)
    for res in results:
        print(res)
