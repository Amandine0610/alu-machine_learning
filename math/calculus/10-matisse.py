#!/usr/bin/env python3
"""
Module to compute the derivative of a polynomial.
"""


def poly_derivative(poly):
    """
    Computes the derivative of a polynomial.
    """
    if (not isinstance(poly, list) or
            not all(isinstance(c, (int, float)) for c in poly)):
        return None
    if len(poly) == 0:
        return None
    if poly == [0]:
        return [0]

    derivative = [i * coef for i, coef in enumerate(poly)][1:]

    return derivative if derivative else [0]
