#!/usr/bin/env python3
"""
Module to compute the sum of squares of the first n natural numbers.
"""


def summation_i_squared(n):
    """
    Calculates the summation of i squared for i in range 1 to n.
    """
    if not isinstance(n, int) or n < 1:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
