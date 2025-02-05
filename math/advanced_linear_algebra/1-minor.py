#!/usr/bin/env python3
def minor(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square and not empty
    rows = len(matrix)
    if rows == 0 or any(len(row) != rows for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Create minor matrix by calculating minors for each element
    minor_matrix = []
    for i in range(rows):
        row_minor = []
        for j in range(rows):
            # Create submatrix by excluding row i and column j
            submatrix = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
            # Add the determinant of the submatrix
            row_minor.append(determinant(submatrix))
        minor_matrix.append(row_minor)
    
    return minor_matrix
