#!/usr/bin/python3
"""Another application of greedy algorithm"""


def makeChange(coins: list, total):
    """This function uses a greedy algorithm
    to calculate the number of change needed for
    for a larger denomination"""
    result = 0
    if total <= 0 or coins = []:
        return 0
    while True:
        x = max(coins)
        while x <= total:
            total -= x
            result += 1
        coins.remove(x)
        if total == 0:
            return result
        if coins == []:
            return -1
