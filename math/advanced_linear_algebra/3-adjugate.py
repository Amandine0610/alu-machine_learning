#!/usr/bin/env python3
def adjugate(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    
    cofactor_matrix = cofactor(matrix)
    return [list(row) for row in zip(*cofactor_matrix)]  # Transpose the cofactor matrix
