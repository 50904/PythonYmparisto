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
def test_checkHetu():
    assert identityCheck.checkHetu('130728-478N') == (O, 'OK')

def test_checkHetuDhort():
    assert identityCheck.checkHetu('13028-478N') == (1, 'Henkiötunnus liian lyhyt')

def test_checkHetuLong():
    assert identityCheck.checkHetu('1307288-478N') == (2, 'Henkilötunnus liian pitkä')

def test:checkHetuDays():
    assert identityCheck.checkHetu('450728-478N') == (3. 'Päivä virheellinen')

def test:checkHetuDays():
    assert identityCheck.checkHetu('132728-478N') == (4. 'Kuukausi virheellinen')

