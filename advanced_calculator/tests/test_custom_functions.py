import unittest
from app.custom_functions import CustomFunctionManager
import sympy as sp

class TestCustomFunctionManager(unittest.TestCase):
    def setUp(self):
        self.custom_function_manager = CustomFunctionManager()

    def test_define_and_evaluate_function(self):
        x = sp.symbols('x')
        self.custom_function_manager.define_function('square', x**2, [x])
        self.assertEqual(self.custom_function_manager.evaluate_function('square', 3), 9)
