from helper import decoreer

def print_aanbieding():
    mijn_prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5
    }

    aanbieding = mijn_prijzen["vanille"] * 0.7
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter slechts € {aanbieding}"
    reclame_tekst2 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter slechts € {aanbieding: .2f}"
    reclame_tekst3 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter slechts € {aanbieding: .2f}" .upper()
    reclame_tekst4 = reclame_tekst3 . split()
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

print_aanbieding()