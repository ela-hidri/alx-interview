#!/usr/bin/python3
"""Solving Prime game"""


def isWinner(x, nums):
    """Determines the winner of the game."""
    def getPrimes(n):
        """Check if a number is prime."""
        primes = []
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, n+1):
            if prime[p]:
                primes.append(p)
        return primes

    ben_wins = 0
    maria_wins = 0

    for i in range(x):
        n = nums[i]
        primes = getPrimes(n)
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
