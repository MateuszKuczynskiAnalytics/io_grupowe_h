def waluta_str_na_dict(ciag_znakow):
    # Inicjalizacja słownika
    waluta_dict = {"galeon": 0, "sykl": 0, "knut": 0}

    # Podział ciągu po spacji
    elements = ciag_znakow.split()

    # Iteracja po elementach co drugim
    for i in range(0, len(elements), 2):
        # Ustalenie klucza i wartości
        klucz = elements[i + 1]
        wartosc = int(elements[i]) if elements[i].isdigit() else 0

        # Zmiana wartości na kluczach odpowiednich bilonów
        if klucz.startswith("g"):
            waluta_dict["galeon"] = wartosc
        elif klucz.startswith("s"):
            waluta_dict["sykl"] = wartosc
        elif klucz.startswith("k"):
            waluta_dict["knut"] = wartosc

    return waluta_dict


# Testowanie funkcji
print(waluta_str_na_dict("13 knut"))
print(waluta_str_na_dict("17 galeon 2 sykl 13 knut"))
print(waluta_str_na_dict("28 sykl"))
print(waluta_str_na_dict("12 galeon 3 knut"))
