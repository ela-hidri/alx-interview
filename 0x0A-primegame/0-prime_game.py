#!/usr/bin/python3
"""Solving Prime game"""


def isWinner(x, nums):
    """Determines the winner of the game."""
    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimes(n):
        """Get a list of prime numbers less than or equal to n."""
        return [num for num in range(2, n + 1) if is_prime(num)]

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
