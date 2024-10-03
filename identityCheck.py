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


# Henkilötunnus esimerkki 130728-478N testataan
# 1. Pituus
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - JA A
# 4. Modulo 31 tarkistus

# Lopullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja

def checkHetu(hetu):

    # Oletustulos 0 OK jos kaikki on kunnossa
    result = (0, 'OK')

    # Vuosisatakoodien sanakirja
    centurCodes = {
        '+': 1800,
        '-': 1900,
        'A': 2000
    }

    validCenturyCodes = centurCodes.keys()

    # Sanakirja jossa on jakojäännösten kirjaintunnukset
    modulusSymbols = {
        10: 'A', 
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'H',
        17: 'J',
        18: 'K',
        19: 'L',
        20: 'M',
        21: 'N',
        22: 'P',
        23: 'R',
        24: 'S',
        25: 'T',
        26: 'U',
        27: 'V',
        28: 'W',
        29: 'X',
        30: 'Y',

    }
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
        # Jos muuta kuin pelkkiä numeroita
        else: 
            result = (3, "Päivä virheellinen")
        
        # Tarkistetaan kuukausiosan oikeellisuus, pitää olla pelkkiä
        if monthPart.isdigit():
            month = int(monthPart)

            # Kuukausi pitää olla väliltä 1 - 12
            if month < 1:
                result = (4, 'Kuukausi virheellinen')
            if month > 12:
                result = (4, 'Kuukausi virheellinen')
        # Jos muuta kuin pelkkiä numeroita
        else:
            result = (4, 'Kuukausi virheellinen')

        if yearPart.isdigit():
            year = int(yearPart) 
        else:
            result = (5, "Vuosi virheellinen")

        # TODO: Tähän Try-Except, jolla tarkistetaan vuosisatakoodi
        
        # TODO: Tähän modulo 31 tarkistetaan laskenta ja vertaus syötettynä 

    

    if lenght < 11: 
        result = (1, 'Henkiötunnus liian lyhyt')

    if lenght > 11:
        result = (2, 'Henkilötunnus liian pitkä')

   
    return result


if __name__  == "__main__":
    hetu = '130728-478N'
    paivat = hetu[2:0]



 # Vuosisatakoodien sanakirja
    centuryCodes = {
        '+': 1800,
        '-': 1900,
        'A': 2000
    }

    validCenturyCodes = list(centuryCodes.keys())
    print(validCenturyCodes)

    # Haetaan vuosisata avaimen perusteella
    print('Vuosisatakoodi - on ',centuryCodes['-'])

    # Vuosisatakoodien avaimet listana
    print('Sallitut vuosisatakoodit ovat', validCenturyCodes)

    # Haetaan olemattomalla avaimella
    # print('Vuosisatakoodi * on ',centuryCodes['*'])

    # Haetaan indeksinumero listan jäsenelle
    try: 
        position = validCenturyCodes.index('*') 
        print(position)
    except:
        print('Ei löytynyt')









    
