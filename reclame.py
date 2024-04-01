def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

def inkomsten_totaal(inkomsten, btw=0):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
def laag_en_hoog(mijn_lijst):
    laagste_inkomst = min(mijn_lijst)
    hoogste_inkomst = max(mijn_lijst)
    return [laagste_inkomst, hoogste_inkomst]

def gemiddelde(mijn_lijst):
    totaal_inkomsten = sum(mijn_lijst)
    gemiddelde_inkomsten = totaal_inkomsten / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."

inkomsten_deze_week = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(inkomsten_deze_week))
print(gemiddelde(inkomsten_deze_week))
from algemene_functies import mijn_functie_2  

def hoog_en_laag(invoer_lijst):
    laagste_waarde = min(invoer_lijst)
    hoogste_waarde = max(invoer_lijst)
    return [laagste_waarde, hoogste_waarde]

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)
invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]
print(combinatie(invoer_lijst_2))