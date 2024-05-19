def wybierz_sowe_zwroc_koszt(potwierdzenie, odleglosc, typ, specjalna):
    cennik = {
        'lokalna': {'list': (0, 0, 2), 'paczka': (0, 0, 7)},
        'krajowa': {'list': (0, 0, 12), 'paczka': (0, 1, 2)},
        'dalekobiezna': {'list': (0, 0, 20), 'paczka': (0, 2, 1)}
    }

    def konwersja_na_knuty(galeony, sykle, knuty):
        return galeony * 493 + sykle * 29 + knuty

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


print(wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec'))
