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

def checkHetu(hetu):

    # Oletustulos 0 OK jos kaikki on kunnossa
    result = (0, 'OK')

    # Lasketaan Hetu-parametrin pituus
    lenght = len(hetu)

    # Jos pituus oikea tehdään eri osat 
    if lenght == 11:
        dayPart = hetu[0:2]
        monthPart = hetu[2:4]
        yearPart = hetu[4:6]
        centuryPart = hetu[6:7]
        numberPart = hetu[7:10] 
        checksum = hetu[10]
        # Tarkistetaan päiväosan oikeellisuus
        if dayPart.isdigit():
            day = int(dayPart)
             
            # Päivän pitää olla väliltä 1 - 31
            if day < 1:
                result = (3, "Päivä virheellinen") 
            if day > 31:
                 result = (3, "Päivä virheellinen") 
        else: 
            # Jos muuta kuin pelkkiä numeroita
            result = (3, "Päivä virheellinen")

    if lenght < 11: 
        result = (1, 'Henkiötunnus liian lyhyt')

    if lenght > 11:
        result = (2, 'Henkilötunnus liian pitkä')

   
    return result

