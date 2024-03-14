#!/usr/bin/python3
"""Solving Prime game"""


def isWinner(x, nums):
    """Determines the winner of the game."""
    def sieve_of_eratosthenes(n):
        """ get ll prime"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return [i for i in range(2, n + 1) if sieve[i]]

    ben_wins = 0
    maria_wins = 0

    for i in range(x):
        n = nums[i]
        primes = sieve_of_eratosthenes(n)
        is_maria_turn = True
        while primes:
            if is_maria_turn:
                selected_prime = primes.pop(0)
                primes = [num for num in primes if num % selected_prime != 0]
                is_maria_turn = False
            else:
                selected_prime = primes.pop()
                primes = [num for num in primes if num % selected_prime != 0]
                is_maria_turn = True

        if is_maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
