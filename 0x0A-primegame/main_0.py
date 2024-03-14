#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(3, [4, 5, 1])))

print(isWinner(3, [5, 10, 15]))  # Output should be "Ben"
print(isWinner(5, [2, 3, 4, 5, 6]))  # Output should be "Maria"
print(isWinner(4, [11, 13, 17, 19]))  # Output should be "Ben"
print(isWinner(2, [7, 8]))  # Output should be "Maria"
print(isWinner(1, [20]))  # Output should be None
print("Winner: {}".format(isWinner(0, [0])))
print("Winner: {}".format(isWinner(-1, [10])))
