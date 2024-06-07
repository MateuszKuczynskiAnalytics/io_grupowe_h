import unittest
from main import waluta_str_na_dict


class TestWalutaStrNaDict(unittest.TestCase):

    def test_only_knuts(self):
        ciag_znakow = "13 knut"
        expected_output = {"galeon": 0, "sykl": 0, "knut": 13}
        self.assertEqual(waluta_str_na_dict(ciag_znakow), expected_output)

    def test_all_non_zero(self):
        ciag_znakow = "17 galeon 2 sykl 13 knut"
        expected_output = {"galeon": 17, "sykl": 2, "knut": 13}
        self.assertEqual(waluta_str_na_dict(ciag_znakow), expected_output)

    def test_no_sykls(self):
        ciag_znakow = "28 sykl"
        expected_output = {"galeon": 0, "sykl": 28, "knut": 0}
        self.assertEqual(waluta_str_na_dict(ciag_znakow), expected_output)

    def test_no_galeons(self):
        ciag_znakow = "12 galeon 3 knut"
        expected_output = {"galeon": 12, "sykl": 0, "knut": 3}
        self.assertEqual(waluta_str_na_dict(ciag_znakow), expected_output)


if __name__ == "__main__":
    unittest.main()
