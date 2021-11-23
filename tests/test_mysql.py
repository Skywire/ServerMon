import unittest
from os import chdir

from app.mysql import get_processlist

class TestMySql(unittest.TestCase):
    def test_run(self):
        chdir("/home/neil/development/magento2")

        result = get_processlist("/usr/local/bin/n98").decode("UTF-8")
        self.assertIn("Command", result)
        self.assertIn("Rows_sent", result)
