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