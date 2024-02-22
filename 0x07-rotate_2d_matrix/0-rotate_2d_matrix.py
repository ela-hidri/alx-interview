#!/usr/bin/python3
""" solving roatate 2d matrix"""


def rotate_2d_matrix(matrix):
    """ rotate it 90 degrees clockwise """
    rot = [row[:] for row in matrix]
    l = len(matrix)
    for i in range(l):
        for index, j in enumerate(matrix[i]):
            matrix[index][l - i - 1] = rot[i][index]
