#!/usr/bin/python3
""" solving roatate 2d matrix"""


def rotate_2d_matrix(matrix):
    """ rotate it 90 degrees clockwise """
    rot = [row[:] for row in matrix]
    length = len(matrix)
    for i in range(length):
        for index, j in enumerate(matrix[i]):
            matrix[index][length - i - 1] = rot[i][index]
