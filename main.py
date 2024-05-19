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

    koszt_g, koszt_s, koszt_k = cennik[odleglosc][typ]

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

