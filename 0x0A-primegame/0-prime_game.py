#!/usr/bin/python3
""" solving Prime game"""


def isWinner(x, nums):
    """ maria or ben wins """
    ben = 0
    Maria = 0
    Maria_ben = True
    primes = []
    for i in range(x):
        for j in range(1, nums[i]):
            primes = getPrimes(j)
            if primes == [] and Maria_ben:
                ben += 1
                break
            elif  primes == [] and not Maria_ben:
                Maria += 1
                break
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
    primes = []
    for i in range(2, n):
        if (n % i) == 0:
            primes.append(i)
    return primes