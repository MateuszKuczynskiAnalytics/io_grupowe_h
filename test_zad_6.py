import unittest
class TestWalutaStrNaDict(unittest.TestCase):
    def test_waluta_str_na_dict(self):
        self.assertEqual(waluta_str_na_dict("5 galeon 10 sykl 15 knut"), {"galeon": 5, "sykl": 10, "knut": 15})
        self.assertEqual(waluta_str_na_dict("10 sykl 15 knut"), {"galeon": 0, "sykl": 10, "knut": 15})
        self.assertEqual(waluta_str_na_dict("5 galeon 15 knut"), {"galeon": 5, "sykl": 0, "knut": 15})
        self.assertEqual(waluta_str_na_dict("20 knut"), {"galeon": 0, "sykl": 0, "knut": 20})
        self.assertEqual(waluta_str_na_dict(""), {"galeon": 0, "sykl": 0, "knut": 0})

if __name__ == '__main__':
    unittest.main()
