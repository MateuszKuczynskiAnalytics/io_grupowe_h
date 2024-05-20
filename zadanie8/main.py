#Zadanie 8

import csv
import random
import time
from datetime import datetime


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
