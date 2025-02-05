#!/usr/bin/env python3
def determinant(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is square
    rows = len(matrix)
    if any(len(row) != rows for row in matrix):
        raise ValueError("matrix must be a square matrix")
    
    # Base case for 0x0 matrix
    if rows == 0:
        return 1  # The determinant of a 0x0 matrix is defined as 1

    # Base case for 1x1 matrix
    if rows == 1:
        return matrix[0][0]

    # Recursively calculate determinant for larger matrices
    det = 0
    for col in range(rows):
        # Create minor matrix by excluding the current row and column
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Add or subtract the determinant of the minor, depending on the column
        det += (-1) ** col * matrix[0][col] * determinant(minor)
    
    return det
