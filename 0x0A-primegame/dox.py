oldMaria = Maria
        oldBen = ben
        for j in range(1, nums[i] + 1):
            print(j)
            if isPrime(j):
                print(f'prime {j}')
                if Maria_ben:
                    Maria_ben = False
                    Maria += 1
                else:
                    Maria_ben = True
                    ben += 1
        if oldMaria == Maria:
            return "Ben"
        if oldBen == ben:
            return "Maria"
        print(f"Ben {ben}")
        print(f"maria {Maria}")
    if ben > Maria:
        return "Ben"
    elif Maria > ben:
        return "Maria"
    else:
        return None





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
        print(f"maria {Maria}")
        print(f'ben {ben}')
        print("----------------------------------------------")
    if ben > Maria:
        return "Ben"
    elif Maria > ben:
        return "Maria"
    else:
        return None