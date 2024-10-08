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
    return result


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
    centuryCodes = {
        '+': 1800,
        '-': 1900,
        'A': 2000
    }

    validCenturyCodes = centuryCodes.keys()

    # Sanakirja jossa on jakojäännösten kirjaintunnukset
    modulusSymbols = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
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

        # Tarkistetaan päiväosan oikeellisuus, pitää olla pelkkiä numeroita
        partsCombined = dayPart + monthPart + yearPart + numberPart 
   
        if partsCombined.isdigit():
            checkSumCalculated = int(partsCombined)%31
            if checksum != modulusSymbols[checkSumCalculated]:
                result = (7, 'Varmistussumma ei täsmää')

                
        try: 
            position = list(validCenturyCodes).index(centuryPart)
        except:
            result = (6, 'Vuosisatakoodi virheellinen')
        # YKSIKKÖTESTIT MODUULEILLE identityCheck.py
            

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

        # Tarkistetaan vuosisatakoodi
    if lenght < 11:
        result = (1, 'Henkilötunnus liian lyhyt')

    if lenght > 11:
        result = (2, 'Henkilötunnus liian pitkä')
    
    return result 
        
import identityCheck

def test_opiskelijanumeroOk_5():
    assert identityCheck.opiskelijanumeroOk('12345') == True

def test_opiskelijanumeroOk_6():
    assert identityCheck.opiskelijanumeroOk('123456') == True

def test_opiskelijanumeroOk_4():
    assert identityCheck.opiskelijanumeroOk('1234') == False

def test_opiskelijanumeroOk_7():
    assert identityCheck.opiskelijanumeroOk('1234567') == False   

def test_opiskelijanumeroOk_kirjain():
    assert identityCheck.opiskelijanumeroOk('12X45') == False

def test_opiskelijanumeroOk_desimaali():
    assert identityCheck.opiskelijanumeroOk('12.45') == False

# Joukossa desimaalipilkku
def test_opiskelijanumeroOk_desimaali2():
    assert identityCheck.opiskelijanumeroOk('12,45') == False

# TDD-testausta
# -------------

# Henkilötunnus on oikein muodostettu, ei virhettä

def test_checkHetuOK():
    assert identityCheck.checkHetu('130728-478N') == (0, 'OK')

# Henkilötunnuksessa pitää olla 11 merkkiä, merkkejä on liikaa
def test_checkHetuShort():
    assert identityCheck.checkHetu('13028-478N') == (1, 'Henkilötunnus liian lyhyt')

# Henkilötunnuksen päiväosassa saa olla 01 - 31
def test_checkHetuLong():
    assert identityCheck.checkHetu('1307288-478N') == (2, 'Henkilötunnus liian pitkä')

# Henkilötunnuksen kuukausosassa saa olla 01 - 12
def test_checkHetuDays():
    assert identityCheck.checkHetu('450728-478N') == (3, 'Päivä virheellinen')

def test_checkHetuMonths():
    assert identityCheck.checkHetu('132728-478N') == (4, 'Kuukausi virheellinen')

def test_checkHetuYears():
    assert identityCheck.checkHetu('13072x-478N') == (5, "Vuosi virheellinen")

# Käytössä olevat vuosisatakoodit + (1800), - (1900) ja A (2000)
def test_checkHetuCenturyCode():
    assert identityCheck.checkHetu('130728S478n') == (6, 'Vuosisatakoodi virheellinen')


        # TODO: Tähän modulo 31 tarkistetaan laskenta ja vertaus syötettynä


    

    

# TODO: Poista loput rivit, kun valmista!
# KOKEILLAAN ERILAISIA VAIHTOEHTOJA
# ---------------------------------
if __name__ == "__main__":
    hetu = '130728-478N'
    paivat = hetu[2:0]
    kuukaudet = hetu[2:4]
    # print (paivat)
    # print (kuukaudet)

 # Vuosisatakoodien sanakirja
    centuryCodes = {
        '+': 1800,
        '-': 1900,
        'A': 2000
    }

    validCenturyCodes = list(centuryCodes.keys())
    validCC = [*centuryCodes.keys()]
    print('Hassu tapa', validCC)
    print('Listafunktiolla', validCenturyCodes)

    # Haetaan vuosisata avaimen perusteella
    print('Vuosisatakoodi - on ', centuryCodes['-'])

    # Vuosisatakoodien avaimet listana
    print('Sallitut vuosisatakoodit ovat', validCenturyCodes)

    # Haetaan olemattomalla avaimella
    # print('Vuosisatakoodi * on ',centuryCodes['*'])

    # Haetaan indeksinumero listan jäsenelle

    try:
        position = validCenturyCodes.index('*')
    except Exception as e:
        print('Tapahtui virhe:', e)

    print('Ja tämä tulee virheenkäsittelyn jälkeen näkyviin')

    searchLetter = '+'

    for value in validCenturyCodes:
        if value == searchLetter:
            found = True
            break
        else: 
            found = False
    if found == False:
        print('Ei löytynyt')

