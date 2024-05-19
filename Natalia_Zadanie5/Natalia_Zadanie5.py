def waluta_dict_na_str(waluta):
    wynik = ""
    if "galeon" in waluta and waluta["galeon"] != 0:
        wynik += str(waluta["galeon"]) + " galeon "
    if "sykl" in waluta and waluta["sykl"] != 0:
        wynik += str(waluta["sykl"]) + " sykl "
    if "knut" in waluta and waluta["knut"] != 0:
        wynik += str(waluta["knut"]) + " knut"
    return wynik.strip()

# Przykładowe wywołania funkcji dla danych z polecenia
print(waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 13}))
print(waluta_dict_na_str({"galeon": 17, "sykl": 2, "knut": 13}))

