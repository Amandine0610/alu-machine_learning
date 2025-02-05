#!/usr/bin/env python3
"""Function that calculates the determinant of a matrix"""


def determinant(matrix):
    """Function that calculates the determinant of a matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    
    # Ensure each row is a list
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")
    
    # Check for square matrix
    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError("matrix must be a square matrix")
    
    # Handle base case for 1x1 matrix
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    
    # Handle base case for 2x2 matrix
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    # Recursive case for larger matrices
    det = []
    for i in range(len(matrix)):
        mini = [row[:i] + row[i + 1:] for row in matrix[1:]]  # Create minor matrix
        if i % 2 == 0:
            det.append(matrix[0][i] * determinant(mini))
        else:
            det.append(-matrix[0][i] * determinant(mini))
    return sum(det)
