from main import licz_sume

#Test zadania 3
def test_licz_sume():
    input_dict = {
        "galeon": [1, 3, 5],
        "sykl": [18, 20, 10],
        "knut": [30, 40, 7]
    }
    expected_output = {
        "galeon": 12,
        "sykl": 0,
        "knut": 14
    }
    assert licz_sume(input_dict) == expected_output, f"Test failed: {licz_sume(input_dict)} != {expected_output}"

if __name__ == '__main__':
    test_licz_sume()
    print("Testy przeszły pomyślnie")