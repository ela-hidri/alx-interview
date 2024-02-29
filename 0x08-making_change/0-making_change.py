#!/usr/bin/python3
"""Solving making change"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount"""
    if total is 0 or total < 0:
        return 0
    nb = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        if total != 0:
            nb += total // coin
            total = total % coin
    if total != 0:
        return -1
    return nb
