# testy dla zadania nr 5

import unittest

def waluta_dict_na_str(waluta):
    wynik = ""
    if "galeon" in waluta and waluta["galeon"] != 0:
        wynik += str(waluta["galeon"]) + " galeon "
    if "sykl" in waluta and waluta["sykl"] != 0:
        wynik += str(waluta["sykl"]) + " sykl "
    if "knut" in waluta and waluta["knut"] != 0:
        wynik += str(waluta["knut"]) + " knut"
    return wynik.strip()

class TestWalutaDictNaStr(unittest.TestCase):
    
    def test_all_zeroes(self):
        waluta = {"galeon": 0, "sykl": 0, "knut": 0}
        expected_output = ""
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)
    
    def test_only_knuts(self):
        waluta = {"galeon": 0, "sykl": 0, "knut": 13}
        expected_output = "13 knut"
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)

    def test_all_non_zero(self):
        waluta = {"galeon": 17, "sykl": 2, "knut": 13}
        expected_output = "17 galeon 2 sykl 13 knut"
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)

    def test_no_galeons(self):
        waluta = {"galeon": 0, "sykl": 2, "knut": 13}
        expected_output = "2 sykl 13 knut"
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)

    def test_no_sykls(self):
        waluta = {"galeon": 17, "sykl": 0, "knut": 13}
        expected_output = "17 galeon 13 knut"
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)

    def test_no_knuts(self):
        waluta = {"galeon": 17, "sykl": 2, "knut": 0}
        expected_output = "17 galeon 2 sykl"
        self.assertEqual(waluta_dict_na_str(waluta), expected_output)

if __name__ == "__main__":
    unittest.main()
