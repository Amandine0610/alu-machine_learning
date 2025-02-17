#!/usr/bin/env python3

"""
Module to compute the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    Computes the integral of a polynomial.
    """
    if (not isinstance(poly, list) or not isinstance(C, (int, float)) or
            not all(isinstance(c, (int, float)) for c in poly)):
        return None
    if not poly:
        return None
    if poly == [0]:
        return [C]

    integral = [C]
    for i, coef in enumerate(poly):
        integral.append(coef / (i + 1))

    integral = [int(x) if isinstance(x, float) and x.is_integer() else x
                for x in integral]

    return integral    