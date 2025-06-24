#!/usr/bin/python3
"""
Prime Game module
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate all prime numbers up to max_n using Sieve of Eratosthenes
    Returns a list where index i is True if i is prime, False otherwise
    """
    if max_n < 2:
        return [False] * (max_n + 1)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    return is_prime


def count_primes_up_to_n(n, is_prime):
    """
    Count the number of prime numbers from 2 to n
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
    return count


def isWinner(x, nums):
    """
    Determine the winner of the prime game

    Args:
        x: number of rounds
        nums: array of n values for each round

    Returns:
        Name of the player that won the most rounds, or None if tie
    """
    if not nums or x <= 0:
        return None

    # Find the maximum n to optimize prime generation
    max_n = max(nums)

    # Generate all primes up to max_n
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:  # Only consider first x rounds
        # Count primes available for this round
        prime_count = count_primes_up_to_n(n, is_prime)

        # If odd number of primes, Maria wins (she goes first)
        # If even number of primes, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
