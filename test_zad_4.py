from main import wybierz_sowe_zwroc_koszt

def test_wybierz_sowe_zwroc_koszt():
    expected_output = {"galeon" : 0, "sykl" : 0, "knut" : 13}
    assert wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec') == expected_output

test_wybierz_sowe_zwroc_koszt()