#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Module to compute the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """
    Computes the integral of a polynomial.
    """
    if not isinstance(poly, list) or not isinstance(C, (int, float)) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not poly or poly == [0]:  # Return None for an empty list or [0]
        return None

    integral = [C]  # Add integration constant first
    for i, coef in enumerate(poly):
        integral.append(coef / (i + 1))  # Compute integral coefficients

    # Convert float values that are whole numbers to int
    integral = [int(x) if isinstance(x, float) and x.is_integer() else x for x in integral]

    return integral
