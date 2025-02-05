#!/usr/bin/env python3
def cofactor(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square and not empty
    rows = len(matrix)
    if rows == 0 or any(len(row) != rows for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Get minor matrix
    minor_matrix_result = minor(matrix)
    
    # Create cofactor matrix by applying sign factor to the minor matrix
    cofactor_matrix = []
    for i in range(rows):
        cofactor_row = []
        for j in range(rows):
            # Apply the sign factor (-1)^(i+j) to each minor element
            cofactor_row.append((-1) ** (i + j) * minor_matrix_result[i][j])
        cofactor_matrix.append(cofactor_row)
    
    return cofactor_matrix
