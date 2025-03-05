#!/usr/bin/env python3
""" matrix multiplication
"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication between mat1 and mat2"""
    if len(mat1[0]) != len(mat2):# Check if matrices can be multiplied
        return None

    result = [[sum(a * b for a, b in zip(row, col)) 
    for col in zip(*mat2)] for row in mat1]

    return result
