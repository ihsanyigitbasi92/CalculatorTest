import sympy as sp

class CustomFunctionManager:
    def __init__(self):
        self.custom_functions = {}

    def define_function(self, name, expression, variables):
        self.custom_functions[name] = sp.lambdify(variables, expression)

    def evaluate_function(self, name, *args):
        if name not in self.custom_functions:
            raise ValueError(f"Function '{name}' is not defined.")
        return self.custom_functions[name](*args)
