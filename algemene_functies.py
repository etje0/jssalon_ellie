def mijn_functie_1(argument):
    return argument ** 2

def mijn_functie_2(argument):
    if argument == 12.3:
        return [argument + 15, argument - 9, argument * 36, 4 / argument]
    elif argument == 12.2:
        return [argument + 14, argument - 10, argument * 24, 6 / argument]
    elif argument == 10.5:
        return [argument + 15, argument - 5, argument * 50, 2 / argument]
    elif argument == 100.20:
        return [argument + 120, argument - 80, argument * 2000, 5 / argument]
    else:
        return "Argument niet gevonden in de tabel"