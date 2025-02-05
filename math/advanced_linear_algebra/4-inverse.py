#!/usr/bin/env python3
import numpy as np

def inverse(matrix):
    """
    Calculates the inverse of a matrix.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    # Check if the matrix is non-empty and square
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    # Convert matrix to a numpy array for easier manipulation
    np_matrix = np.array(matrix)
    # Check if the determinant is zero (singular matrix)
    if np.linalg.det(np_matrix) == 0:
        return None
    # Compute the inverse
    return np.linalg.inv(np_matrix).tolist()
