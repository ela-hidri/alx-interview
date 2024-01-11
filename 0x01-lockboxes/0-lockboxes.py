#!/usr/bin/python3

"""
Solve the lockBoxes Problem
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened

    Keyword arguments:
    boxes -- boxes to check
    Return: True if all boxes can be opened, else return False
    """
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
