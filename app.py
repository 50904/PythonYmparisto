# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
# from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0


while True:
    pass
    userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivenSsn = userGivenSsn.upper() # Varmistetaan, että tarkiste on isolla
    # TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
    
    # TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille  -> reg exp
    

    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth()
            gender = ssnToCheck.getGender()
            age = ssnToCheck.calculateAge() 
            userGivenLastname = input('Syötä asiakkaan sukunimi: ')
            userGivenLastname = userGivenLastname.capitalize()
            userGivenFirstname = input('Syötä asiakkaan etunimi: ')
            userGivenFirstname = userGivenFirstname.capitalize()
            print('Asaikas:', userGivenLastname, userGivenFirstname)
            print('Syntymäaika:', ssnToCheck.dateOfBirth)
            print('Ikä:', age)
            print('Sukupuoli:', ssnToCheck.gender)
        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunnuksessasi oli virhe', e)

    # Kysytään halutaanko poistua ohjelmasta
    wantAbort = input('Haluatko päättää ohjelman k/E: ')
    # Muutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko vastaus K
    if wantAbort.upper() == 'K':
        break # Poistutaan ikuisesta silmukasta


