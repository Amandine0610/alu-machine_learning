#!/usr/bin/env python3

def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if not poly:
        return None
    
    integral = [C]  # Add integration constant first
    for i, coef in enumerate(poly):
        integral.append(coef / (i + 1))  # Compute integral coefficients
    
    # Convert float values that are whole numbers to int
    integral = [int(x) if isinstance(x, float) and x.is_integer() else x for x in integral]

    return integral
