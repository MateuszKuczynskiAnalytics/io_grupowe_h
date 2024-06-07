import unittest
from main import waluta_str_na_dict

class TestWalutaStrNaDict(unittest.TestCase):
    def test_waluta_str_na_dict_single_currency(self):
        result = waluta_str_na_dict("13 knut")
        self.assertEqual(result, {"galeon": 0, "sykl": 0, "knut": 13})

    def test_waluta_str_na_dict_multiple_currencies(self):
        result = waluta_str_na_dict("17 galeon 2 sykl 13 knut")
        self.assertEqual(result, {"galeon": 17, "sykl": 2, "knut": 13})

    def test_waluta_str_na_dict_missing_currency(self):
        result = waluta_str_na_dict("28 sykl")
        self.assertEqual(result, {"galeon": 0, "sykl": 28, "knut": 0})

    def test_waluta_str_na_dict_empty_input(self):
        result = waluta_str_na_dict("")
        self.assertEqual(result, {"galeon": 0, "sykl": 0, "knut": 0})

    def test_waluta_str_na_dict_invalid_input(self):
        result = waluta_str_na_dict("12 galeon 3,5 knut")
        self.assertEqual(result, {"galeon": 12, "sykl": 0, "knut": 0})

if __name__ == '__main__':
    unittest.main()
