#test dla zadania 2


import unittest
from unittest.mock import patch
from main import wyslij_sowe

class TestWyslijSowe(unittest.TestCase):

    @patch('random.random', return_value=0.5)
    @patch('time.sleep', return_value=None)
    def test_wyslij_sowe(self, mock_sleep, mock_random):
        self.assertTrue(wyslij_sowe("Kandydat", "List do Kandydata"))

if __name__ == '__main__':
    unittest.main()