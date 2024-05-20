# Zadanie 2

import time
import random

def wyslij_sowe(adresat, tresc_listu):
    print(f'Wyślij sowę do: {adresat}')
    print(f'Treść listu: {tresc_listu}')

    time.sleep(1) #odczekanie 1 sekundy

    if random.random() < 0.9:
        print("Sowa wysłana pomyślnie")
        return True
    else:
        print("Niestety sowa nie została wysłana")
        return False

adresat = "Kandydat na ucznia Szkoły Magii i Czarodziejstwa w Hogwarcie"
tresc_listu = "Miło nam poinformować, że otworzyła się przed Tobą możliwość dołączenia do elitarnej Szkoły w Hogwarcie. Zapraszamy i życzymy samych sukcesów. "
wynik = wyslij_sowe(adresat, tresc_listu)
print("Wynik operacji:", wynik)


# Zadanie 3

#Funkcja konwertująca input_dict (słownik, gdzie kluczami są knuts, sykls i galeons a wartościami listy zawierające liczbę
#danych nominałów) do najwyższych możliwych nominałów, zwrqacanych w słowniku output_dict.
def licz_sume(input_dict):
    total_knuts = sum(input_dict.get("knut", []))
    total_sykls = sum(input_dict.get("sykl", []))
    total_galeons = sum(input_dict.get("galeon", []))
    
    total_sykls += total_knuts // 21
    remaining_knuts = total_knuts % 21
    
    total_galeons += total_sykls // 17
    remaining_sykls = total_sykls % 17
    
    output_dict = {
        "galeon": total_galeons,
        "sykl": remaining_sykls,
        "knut": remaining_knuts
    }
    
    return output_dict


#Zadanie 4
"""
Funkcja ta oblicza koszt wysłania przesyłki za pomocą sowy
na podstawie różnych czynników, takich jak odległość, rodzaj przesyłki
i dodatkowe usługi.
"""
def wybierz_sowe_zwroc_koszt(potwierdzenie, odleglosc, typ, specjalna):
    cennik = {
        'lokalna': {'list': (0, 0, 2), 'paczka': (0, 0, 7)},
        'krajowa': {'list': (0, 0, 12), 'paczka': (0, 1, 2)},
        'dalekobiezna': {'list': (0, 0, 20), 'paczka': (0, 2, 1)}
    }

    """
    Funkcja konwertuje te wartości na równoważną liczbę knutów, aby ułatwić
    obliczenia kosztu przesyłki.
    """
    def konwersja_na_knuty(galeony, sykle, knuty):
        return galeony * 493 + sykle * 29 + knuty

    """
    Konwertuje liczbę knutów na równoważne wartości
    w galionach, syklach i knutach.
    """
    def podsumowanie_kosztow(knuty):
        galeony = knuty // 493
        knuty %= 493
        sykle = knuty // 29
        knuty %= 29
        return {"galeon": galeony, "sykl": sykle, "knut": knuty}

    if potwierdzenie:
        koszt_k += 7

    if specjalna == 'wyjec':
        koszt_k += 4
    elif specjalna == 'list gonczy':
        koszt_s += 1

    total_knuts = konwersja_na_knuty(koszt_g, koszt_s, koszt_k)

    return podsumowanie_kosztow(total_knuts)

# Test funkcji
print(wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec'))


# Zadanie 5
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

