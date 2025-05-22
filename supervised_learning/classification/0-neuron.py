import numpy as np

class Neuron:
    def __init__(self, nx):
        # Validate that nx is an integer
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        # Validate that nx is positive
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        
        # Initialize weights with random normal distribution
        self.W = np.random.randn(1, nx)
        # Initialize bias to 0
        self.b = 0
        # Initialize activated output to 0
        self.A = 0