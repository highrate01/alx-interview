#!/usr/bin/python3
"""
Prime Game
"""


def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using the
    Sieve of Eratosthenes algorithm.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game for x
    rounds with given n values.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count prime numbers up to n
        prime_count = sum(primes[:n+1])

        # If the count is odd, Maria wins; if even, Ben wins
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
