#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): The matrix for which to calculate the determinant.

    Returns:
        float: The determinant of the matrix.
    """
    if len(matrix) == 2:
        # Base case: 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case: for larger matrices, calculate determinant using minors
    det = 0
    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    
    return det

def minor(matrix):
    """
    Calculates the minor of each element of the matrix.

    Args:
        matrix (list of lists): The matrix for which to calculate minors.

    Returns:
        list of lists: A matrix containing the minors of the elements of the input matrix.
    """
    minors_matrix = []
    
    # Iterate over each element in the matrix to calculate the minor
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix[i])):
            submatrix = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
            minor_row.append(determinant(submatrix))
        minors_matrix.append(minor_row)
    
    return minors_matrix
