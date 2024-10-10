# YKSIKKÖTESTIT MODUULEILLE identityCheck.py

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

# Henkilötunnuksen numeroista tehdään luku, esim 1307288478 ja jaetaan se luvulla 31. Jakojäännös on tarkiste. Jos se on alle 10, käytetään numeroa, jos yli haetaan taulukosta vastaava kirjainmerkki 10 -> A, 11 -> B G ja I eivät ole käytössä
def test_checkHetuModulo():
    assert identityCheck.checkHetu('130728-478M') == (7, 'Varmistussumma ei täsmää')



