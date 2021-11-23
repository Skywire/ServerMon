import unittest
from app.atop import run_atop

class TestAtop(unittest.TestCase):
    def test_run(self):
        result = run_atop()
        self.assertTrue(result)
