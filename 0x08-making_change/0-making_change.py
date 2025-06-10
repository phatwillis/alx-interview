#!/usr/bin/python3
"""Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    n = 0
    fewest_num = 1
    sorted_coins = sorted(coins, reverse=True)
    placeholder_total = sorted_coins[n]
    if total == 0 or total < 0:
        return 0
    try:
        while True:
            placeholder_total += sorted_coins[n]
            if placeholder_total > total:
                # remove the just added coin value
                placeholder_total -= sorted_coins[n]
                n += 1
            else:
                fewest_num += 1
            if placeholder_total == total:
                return fewest_num
    except IndexError:
        # if the movement of n has gone beyond the last coin value
        return -1
