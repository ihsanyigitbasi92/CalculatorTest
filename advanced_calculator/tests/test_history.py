import unittest
from app.history import HistoryManager

class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_add_to_history(self):
        self.history_manager.add_to_history("1 + 1 = 2")
        self.assertIn("1 + 1 = 2", self.history_manager.get_history())

    def test_clear_history(self):
        self.history_manager.add_to_history("1 + 1 = 2")
        self.history_manager.clear_history()
        self.assertEqual(self.history_manager.get_history(), [])
