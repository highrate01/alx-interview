#!/usr/bin/python3
"""
copy/paste interview
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    Args:
        n: number of H characters to achieve
    Returns: int
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1
    if n > 1:
        operations += n

    return operations
