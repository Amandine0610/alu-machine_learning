"""
This module contains a function that calculates the definiteness of a matrix.
The definiteness is determined based on the eigenvalues of the matrix and is classified as:

- Positive definite
- Positive semi-definite
- Negative definite
- Negative semi-definite
- Indefinite

The matrix must be a square, symmetric numpy ndarray.
"""

#!/usr/bin/env python3
import numpy as np


def definiteness(matrix):
    # Check if matrix is a numpy.ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return None
    # Check if matrix is symmetric
    if not np.array_equal(matrix, matrix.T):
        return None
    # Calculate definiteness based on eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)
    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
