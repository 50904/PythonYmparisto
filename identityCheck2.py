# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MODUULIT
# ---------------------

# LUOKAT
# ------

# Henkilötunnuksen käsittely
class NationalSSN:
    def __init__(self, ssn: str) -> None:
        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''