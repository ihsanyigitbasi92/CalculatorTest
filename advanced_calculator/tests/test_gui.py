import unittest
from app.gui import CalculatorGUI

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        self.gui = CalculatorGUI()

    def test_gui_initialization(self):
        self.assertIsNotNone(self.gui.root)
