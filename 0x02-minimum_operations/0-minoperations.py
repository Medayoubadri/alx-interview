#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): Target number of H characters

    Returns:
        int: Minimum num of operations (Copy All & Paste) to get n H characters
             Returns 0 if n is impossible to achieve (n < 1)
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

        if divisor * divisor > n and n > 1:
            operations += n
            break

    return operations
