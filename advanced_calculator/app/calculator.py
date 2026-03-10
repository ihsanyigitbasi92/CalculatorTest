import numpy as np
import scipy.stats as stats
import sympy as sp

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def sin(self, x):
        return np.sin(x)

    def cos(self, x):
        return np.cos(x)

    def tan(self, x):
        return np.tan(x)

    def log(self, x, base=np.e):
        return np.log(x) / np.log(base)

    def exp(self, x):
        return np.exp(x)

    def mean(self, data):
        return np.mean(data)

    def median(self, data):
        return np.median(data)

    def mode(self, data):
        mode_result = stats.mode(data)
        return mode_result.mode[0]

    def std_dev(self, data):
        return np.std(data)
