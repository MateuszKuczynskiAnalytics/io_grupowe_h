import time
import random
import csv
from datetime import datetime


# Zadanie 2


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
    
    koszt_g, koszt_s, koszt_k = cennik[odleglosc][typ]
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

# Zadanie 6

def waluta_str_na_dict(ciag_znakow):
#OPIS
#Funkcja przetwarza ciąg znaków reprezentujący ceny w różnych walutach na słownik.
#Parametry: ciag_znakow (str): Ciąg znaków zawierający ceny w formacie "wartość waluta", gdzie wartość jest liczbą całkowitą, a waluta może być galeonem (g), syklem (s) lub knutem (k).
#Zwraca: dict: Słownik zawierający ceny w formacie {"galeon": wartość, "sykl": wartość, "knut": wartość}. Domyślnie wartości dla każdej waluty są ustawione na 0, chyba że występują w ciągu znaków.

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



#Zadanie 7

def nadaj_sowe(adresat: str, tresc: str, potw_odbioru: bool, odleglosc: str, typ: str, specjalna: str):
    """
    Funkcja dodaje wpis do pliku 'poczta_nadania_lista.csv' z informacjami o nadanej przesyłce.

    Parametry:
    adresat (str): Adresat wiadomości.
    tresc (str): Treść wiadomości.
    potw_odbioru (bool): Czy potwierdzenie odbioru jest wymagane (True/False).
    odleglosc (str): Odległość (lokalna/krajowa/dalekobieżna).
    typ (str): Typ przesyłki (list/paczka).
    specjalna (str): Specjalna kategoria (nie dotyczy/wyjec/list gończy).

    Funkcja nic nie zwraca!
    """
    koszt_przesylki_dict = wybierz_sowe_zwroc_koszt(potw_odbioru, odleglosc, typ, specjalna)
    koszt_przesylki_str = waluta_dict_na_str(koszt_przesylki_dict)

    potwierdzenie_odbioru_str = "TAK" if potw_odbioru else "NIE"
    dane_do_zapisu = [adresat, tresc, koszt_przesylki_str, potwierdzenie_odbioru_str]
    with open("poczta_nadania_lista.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(dane_do_zapisu)

#Zadanie 8

# Kod przetwarza liste z pliku csv, oblicza koszt wysyłki i zapisuje rezultat w nowym csv

def wyslij_sowe(adresat, tresc):
    print(f"Wysyłanie sowy do {adresat} z treścią: {tresc}")
    time.sleep(1)
    result = random.choices([True, False], weights=[90, 10])[0]
    return result


def poczta_wyslij_sowy(plik_csv):
    with open(plik_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sowy_list = list(reader)

    rezultaty = []
    for sowa in sowy_list:
        adresat = sowa['adresat']
        tresc = sowa['treść wiadomości']
        koszt_str = sowa['koszt przesyłki']
        potwierdzenie_odbioru = sowa['potwierdzenie odbioru']

        koszt_dict = waluta_str_na_dict(koszt_str)
        sowa_doszla = wyslij_sowe(adresat, tresc)

        if sowa_doszla:
            rzeczywisty_koszt = koszt_dict
        else:
            if potwierdzenie_odbioru == 'TAK':
                rzeczywisty_koszt = {"galeon": 0, "sykl": 0, "knut": 0}
            else:
                rzeczywisty_koszt = koszt_dict

        rzeczywisty_koszt_str = waluta_dict_na_str(rzeczywisty_koszt)
        rezultaty.append({
            "adresat": adresat,
            "treść wiadomości": tresc,
            "koszt przesyłki": koszt_str,
            "potwierdzenie odbioru": potwierdzenie_odbioru,
            "rzeczywisty koszt": rzeczywisty_koszt_str
        })


    teraz = datetime.now()
    nazwa_pliku_wyjsciowego = teraz.strftime("output_sowy_z_poczty_%d_%m_%Y.csv")

    with open(nazwa_pliku_wyjsciowego, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["adresat", "treść wiadomości", "koszt przesyłki", "potwierdzenie odbioru", "rzeczywisty koszt"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for rezultat in rezultaty:
            writer.writerow(rezultat)

# Test:
poczta_wyslij_sowy('poczta_nadania_lista.csv')
