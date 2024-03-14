#!/usr/bin/python3
""" solving Prime game"""


def isWinner(x, nums):
    """ maria or ben wins """
    ben = 0
    Maria = 0
    Maria_ben = True
    primes = []
    for i in range(x):
        primes = getPrimes(nums[i])
        for _ in range(1, nums[i]):
            if primes == [] and Maria_ben:
                ben += 1
                continue
            elif  primes == [] and not Maria_ben:
                Maria += 1
                continue
            if Maria_ben:
                Maria_ben = False
                Maria += 1
                primes.pop(0)
            else:
                Maria_ben = True
                ben += 1
                primes.pop(0)
    if ben > Maria:
        return "Ben"
    elif Maria > ben:
        return "Maria"
    else:
        return None



def getPrimes(n):
    """check if primeNbr"""
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = [str(num) for num in range(2, n+1) if is_prime(num)]
    return prime_list
