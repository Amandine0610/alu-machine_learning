#!/usr/bin/env python3
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
    # Function to calculate determinant of a 2x2 matrix
    def determinant_2x2(m):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    # Function to calculate the determinant of a matrix
    def determinant(m):
        if len(m) == 2:
            return determinant_2x2(m)
        det = 0
        for col in range(len(m)):
            sub_matrix = [row[:col] + row[col+1:] for row in m[1:]]
            det += ((-1) ** col) * m[0][col] * determinant(sub_matrix)
        return det
    # Function to calculate the cofactor matrix
    def cofactor_matrix(m):
        cofactors = []
        for row in range(len(m)):
            cofactor_row = []
            for col in range(len(m)):
                sub_matrix = [r[:col] + r[col+1:] for i, r in enumerate(m) if i != row]
                cofactor_row.append(((-1) ** (row + col)) * determinant(sub_matrix))
            cofactors.append(cofactor_row)
        return cofactors
    # Calculate the determinant of the matrix
    det_matrix = determinant(matrix)
    # If the determinant is zero, return None as the matrix is singular
    if det_matrix == 0:
        return None
    # Calculate the adjugate matrix (transpose of the cofactor matrix)
    cofactors = cofactor_matrix(matrix)
    adjugate = list(zip(*cofactors))
    # Calculate the inverse (adjugate / determinant)
    inverse_matrix = [[adjugate[i][j] / det_matrix for j in range(len(matrix))] for i in range(len(matrix))]
    
    return inverse_matrix
