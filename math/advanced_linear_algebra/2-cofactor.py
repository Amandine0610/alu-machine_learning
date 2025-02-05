#!/usr/bin/env python3
"""Function that calculates the cofactor matrix of a matrix"""


def determinant(matrix):
    """Function that calculates the determinant of a matrix"""
    if len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
    det = []
    for i in range(len(matrix)):
        mini = [row[:i] + row[i + 1:] for row in matrix[1:]]
        if i % 2 == 0:
            det.append(matrix[0][i] * determinant(mini))
        else:
            det.append(-1 * matrix[0][i] * determinant(mini))
    return sum(det)


def cofactor(matrix):
    """Function that calculates the cofactor matrix of a matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a list of lists")
    for i in matrix:
        if len(matrix) != len(i):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]
    if len(matrix) == 2:
        cofactor = [i[::-1] for i in matrix]
        cofactor = cofactor[::-1]
        cofactor = [[cofactor[i][j] if (i + j) % 2 == 0 else -cofactor[i][j]
                     for j in range(len(cofactor[i]))]
                    for i in range(len(cofactor))]
        return cofactor
    cofactor = [[0 for _ in range(len(matrix))] for _ in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mini = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:
            ])]
            cofactor[i][j] = ((-1) ** (i + j)) * determinant(mini)
    return cofactor
