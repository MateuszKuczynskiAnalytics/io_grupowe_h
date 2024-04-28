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