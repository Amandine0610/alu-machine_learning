#!/usr/bin/env python3

def poly_integral(poly, C=0):
    """Computes the integral of a polynomial."""
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    if len(poly) == 0:
        return [C]

    integral = [C]  # Start with the integration constant
    for i, coeff in enumerate(poly):
        integral.append(coeff / (i + 1))

    # Convert exact integer values to int
    integral = [int(x) if x.is_integer() else x for x in integral]
    
    return integral

# Example usage
poly = [5, 3, 0, 1]
print(poly_integral(poly))  # Output: [0, 5, 1.5, 0, 0.25]
