#!/usr/bin/env python3
"""
This module contains a function that calculates the definiteness of a matrix.
The definiteness is determined based on the eigenvalues of the matrix and is
classified as:

- Positive definite
- Positive semi-definite
- Negative definite
- Negative semi-definite
- Indefinite

The matrix must be a square, symmetric numpy ndarray.
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a square, symmetric matrix.

    Args:
    matrix (numpy.ndarray): The matrix whose definiteness needs to be determined.

    Returns:
        str: One of the following strings:
            - "Positive definite"
            - "Positive semi-definite"
            - "Negative definite"
            - "Negative semi-definite"
            - "Indefinite"
    """
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
    # Positive definite: all eigenvalues > 0
    if np.all(eigenvalues > 0):
        return "Positive definite"
    # Positive semi-definite: all eigenvalues >= 0
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    # Negative definite: all eigenvalues < 0
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    # Negative semi-definite: all eigenvalues <= 0
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    # Indefinite: eigenvalues are mixed
    else:
        return "Indefinite"
