#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of coin denominations available.
    total (int): The target amount to make change for.

    Returns:
    int: The minimum number of coins needed to make the total.
         Returns 0 if total is 0 or less.
         Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Sort the coins in decreasing order
    coins.sort(reverse=True)
    # Initialize the coin count to zero
    coin_count = 0
    # Iterate through each coin in the list of coins
    for coin in coins:
        # If the coin is greater than the remaining total, skip it
        if coin > total:
            continue
        # Calculate the number of times the current coin can be used
        count = total // coin
        # Update the total by subtracting the value of the coins used
        total -= count * coin
        # Update the coin count by adding the number of coins used
        coin_count += count
        # If the total is now zero, we're done
        if total == 0:
            break
    # If we couldn't make change for the total, return -1
    if total > 0:
        return -1
    # Otherwise, return the coin count
    return coin_count
