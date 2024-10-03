# MODUULI OPISKELIJANUMERON JA HENKILÖTUNNUKSEN TARKISTUKSEEN
# ===========================================================

"""Moldule makes sanity checks for Raseko student id and the Finnish Social Security Number
    """

# KIRJASTO JA MODUULIT
# --------------------

# FUNKTIOT
# --------

# Opiskelijatunnukset oikea muoto
def opiskelijanumeroOk(opiskelijanumero: str) -> bool: 
    """Checks if student number is 5 or 6 digits and does not contain any characters other than numerics

    Args:
        opiskelijanumero (str): Raseko's student id

    Returns:
        bool: True if correct otherwise False
    """
    result: bool = False
    pituus = len(opiskelijanumero)
    if pituus == 5 or pituus == 6:
        if opiskelijanumero.isdigit():
            result = True 
    return  result

# TODO: Tee testi HeTu:a varten ja vasta sitten kirjoita koodi

# Henkilötunnus esimerkki 130728-478N testataan
# 1. Pituus
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - JA A
# 4. Modulo 31 tarkistus

# Lopullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja

def checkHetu(Hetu):
    pass