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
        result = True 
    return  result