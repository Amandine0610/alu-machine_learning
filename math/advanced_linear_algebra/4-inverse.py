#!/usr/bin/env python3
def inverse(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    
    det_matrix = det(matrix)  # You need a function to calculate the determinant
    
    if det_matrix == 0:
        return None  # Matrix is singular, no inverse exists
    
    adjugate_matrix = adjugate(matrix)
    return [[adjugate_matrix[i][j] / det_matrix for j in range(len(matrix))] for i in range(len(matrix))]
