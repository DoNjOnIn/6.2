import unittest
from main import max

class MyTestCase(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max(2,[2,-3,6],0),6)
