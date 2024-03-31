import unittest
import pytest
@pytest.mark.order(1)
class TestTrivial(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(1, 1)
    
    def test_trivial2(self):
        self.assertEqual(1, 1)