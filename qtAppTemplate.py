# MALLIPOHJA QT-SOVELLUSTEN RAKENTAMISEEN PySide6-KIRJASTON AVULLA
# ================================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Järjestelmäkomentojen kirjasto
import sys

# Pyside-kirjastot
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# LUOKKAMÄÄRITYKSET 
# -----------------

# Pääikkunan luokka, joka perii QMainWindow-luokan
class MainWindow(QMainWindow):

    # Konstruktori
    def __init__(self):
        QMainWindow.__init__(self)

        # Luodaan käyttöliittymän lataaja
        windowLoader = QUiLoader()

        # Annetaan sille käyttöliittymätiedosto
        uiFile = QFile('mainWindow.ui')
        window = windowLoader.load(uiFile)
        window.show()

        self.setWindowTitle('Main Window')
        self.lineE = window.findChild

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())
