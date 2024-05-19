def waluta_dict_na_str(waluta):
    """
    Funkcja `waluta_dict_na_str` przyjmuje jako argument słownik `waluta`, który zawiera klucze odpowiadające trzem rodzajom waluty
    (galeon, sykl, knut) oraz ich ilości. Funkcja zwraca ciąg znaków opisujący ilość każdej waluty, pomijając waluty, które mają wartość 0.

    Parametry:
    waluta (dict): Słownik zawierający klucze "galeon", "sykl" oraz "knut" i ich odpowiadające wartości całkowite.

    Zwracana wartość:
    str: Ciąg znaków opisujący ilość poszczególnych walut w formacie "<ilość> <waluta>".

    Przykłady:
    >>> waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 13})
    '13 knut'
    >>> waluta_dict_na_str({"galeon": 17, "sykl": 2, "knut": 13})
    '17 galeon 2 sykl 13 knut'
    """
    wynik = ""
    if "galeon" in waluta and waluta["galeon"] != 0:
        wynik += str(waluta["galeon"]) + " galeon "
    if "sykl" in waluta and waluta["sykl"] != 0:
        wynik += str(waluta["sykl"]) + " sykl "
    if "knut" in waluta and waluta["knut"] != 0:
        wynik += str(waluta["knut"]) + " knut"
    return wynik.strip()

# Przykładowe wywołania funkcji
print(waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 13}))
print(waluta_dict_na_str({"galeon": 17, "sykl": 2, "knut": 13}))
