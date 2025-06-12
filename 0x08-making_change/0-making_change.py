#!/usr/bin/python3
"""
Module for making change with the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins: List of coin values
        total: Target amount

    Returns:
        Fewest number of coins needed to meet total
        0 if total is 0 or less
        -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
