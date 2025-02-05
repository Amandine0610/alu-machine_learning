#!/usr/bin/env python3
import numpy as np

def definiteness(matrix):
    # Check if matrix is a numpy ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    # Check if the matrix is square (n x n)
    if matrix.shape[0] != matrix.shape[1]:
        return None
    
    # Calculate eigenvalues of the matrix
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Check for positive definite, positive semi-definite, negative semi-definite, negative definite, or indefinite
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
