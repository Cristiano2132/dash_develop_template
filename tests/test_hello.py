import unittest
import pytest

@pytest.mark.order(2)
class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(1, 1)
    
    def test_hello2(self):
        self.assertEqual(1, 1)
