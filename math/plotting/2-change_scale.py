#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
'''This module provides a function for plotting a line'''

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here
plt.plot(x, y, r)
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of C-14")
plt.yscale("log")
plt.show()
