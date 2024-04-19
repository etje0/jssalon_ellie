def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit


def som(dictionary):
    """
    Bereken de som van alle waarden in de opgegeven dictionary.
    
    Args:
    dictionary (dict): De invoer dictionary waarvan de waarden moeten worden opgeteld.
    
    Returns:
    int of float: De som van alle waarden in de dictionary.
    """
    total = sum(dictionary.values())
    return total

totaal_inkomsten = som(inkomsten)
print("De totale inkomsten zijn:", totaal_inkomsten)
