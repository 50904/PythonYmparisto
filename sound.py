# MODUULI ÄÄNIMERKKIEN ANTAMISEEN
# ===============================
"""A module to produce various sound patterns and play wav-files
    """
# KIRJASTOT JA MODUULIT
# ---------------------

# Windows-äänet
import winsound

# Ajan käsittely
import time

# ÄÄNIFUNCTIOT
# ------------

def shortBeep():
    """Creates a 1 kHz sound for 1/4 seconds
    """
    winsound.Beep(1000, 250)

def longBeeb():
    """Creates a 1 kHz sound for 2 seconds
    """
    winsound.Beep(1000, 2000)  

def waitMs(ms):  
    """Waits for a timeperiod

    Args:
        ms (int): time in millisecond
    """
    seconds = ms / 1000
    time.sleep(seconds)

# Säädettävät äänet 1. Korkeus ja kesto parametreina
def parametricBeep(frequency, duration=250):
    """Produces a sound at given frequency and duration

    Args:
        frequency (int): Frequency of the tone in Hz
        duration (int): Duration in milliseconds
    """
    winsound.Beep(frequency, duration)

# Säädettävät äänet 2. toistuva äänimerkki korkeus, kesto ja määrä
def repeatingBeep(frequency: int, duration: int, count: int)  -> None:
    """Greates a repeating buzzer sound

    Args:
        frequency (int): Tone frequency in Hz 
        duration (int): Duration of the single tone in milliseconds
        count (int): How many times sound will be repated
    """
    for i in range(count):
        winsound.Beep(frequency, duration)
        waitMs(250)
# Ääni tulee halutusta tiedostosta, parametrina äänen nimi
def playWav(fileName: str) -> None:
    """Play a wav file

    Args:
        fileName (str): Name of the audiofile
    """
    winsound.PlaySound(fileName, winsound.SND_FILENAME)

if __name__ == "__main__":
    # shortBeep()
    # waitMs(500)
    # longBeeb()
    # waitMs(500)
    # parametricBeep(360)
    repeatingBeep(360, 500, 5)
    waitMs(1000)
    playWav('Alkaa.WAV')
    waitMs(1000)
    playWav('Loppuu.WAV')