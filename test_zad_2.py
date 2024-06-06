import unittest
from unittest.mock import patch
import random
import time

#test dla zadania 2

#zadanie 2
def wyslij_sowe(adresat, tresc_listu):
    print(f'Wyślij sowę do: {adresat}')
    print(f'Treść listu: {tresc_listu}')

    time.sleep(1) # odczekanie 1 sekundy

    if random.random() < 0.9:
        print("Sowa wysłana pomyślnie")
        return True
    else:
        print("Niestety sowa nie została wysłana")
        return False




class TestWyslijSowe(unittest.TestCase):

    @patch('random.random')
    @patch('time.sleep', return_value=None)
    def test_wyslij_sowe_sukces(self, mock_sleep, mock_random):
        mock_random.return_value = 0.5  # Zwróć wartość mniejszą niż 0.9, aby symulować sukces
        adresat = "Kandydat na ucznia Szkoły Magii i Czarodziejstwa w Hogwarcie"
        tresc_listu = "Miło nam poinformować, że otworzyła się przed Tobą możliwość dołączenia do elitarnej Szkoły w Hogwarcie. Zapraszamy i życzymy samych sukcesów."

        wynik = wyslij_sowe(adresat, tresc_listu)
        
        self.assertTrue(wynik)
        mock_sleep.assert_called_once_with(1)
        mock_random.assert_called_once()

    @patch('random.random')
    @patch('time.sleep', return_value=None)
    def test_wyslij_sowe_niepowodzenie(self, mock_sleep, mock_random):
        mock_random.return_value = 0.95  # Zwróć wartość większą niż 0.9, aby symulować niepowodzenie
        adresat = "Kandydat na ucznia Szkoły Magii i Czarodziejstwa w Hogwarcie"
        tresc_listu = "Miło nam poinformować, że otworzyła się przed Tobą możliwość dołączenia do elitarnej Szkoły w Hogwarcie. Zapraszamy i życzymy samych sukcesów."

        wynik = wyslij_sowe(adresat, tresc_listu)
        
        self.assertFalse(wynik)
        mock_sleep.assert_called_once_with(1)
        mock_random.assert_called_once()

if __name__ == '__main__':
    unittest.main()