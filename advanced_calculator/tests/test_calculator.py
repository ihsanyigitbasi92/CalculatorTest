import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(np.pi / 2), 1.0)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(np.pi), -1.0)

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(np.pi / 4), 1.0)

    def test_log(self):
        self.assertAlmostEqual(self.calc.log(np.e), 1.0)

    def test_exp(self):
        self.assertAlmostEqual(self.calc.exp(1), np.e)

    def test_mean(self):
        self.assertEqual(self.calc.mean([1, 2, 3]), 2)

    def test_median(self):
        self.assertEqual(self.calc.median([1, 2, 3]), 2)

    def test_mode(self):
        self.assertEqual(self.calc.mode([1, 1, 2, 3]), 1)

    def test_std_dev(self):
        self.assertAlmostEqual(self.calc.std_dev([1, 2, 3]), np.std([1, 2, 3]))
