# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Labra.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 361)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setGeometry(QRect(20, 40, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(20)
        self.ssnLineEdit.setFont(font1)
        self.ssnLineEdit.setMouseTracking(True)
        self.ssnLineEdit.setToolTipDuration(3000)
        self.ssnLineEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.ssnLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.ssnLineEdit.setClearButtonEnabled(True)
        self.ssnLabel_2 = QLabel(self.centralwidget)
        self.ssnLabel_2.setObjectName(u"ssnLabel_2")
        self.ssnLabel_2.setGeometry(QRect(20, 20, 81, 16))
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(20, 140, 231, 41))
        self.firstNameLineEdit.setFont(font1)
        self.firstNameLineEdit.setMouseTracking(True)
        self.firstNameLineEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(270, 140, 231, 41))
        self.lastNameLineEdit.setFont(font1)
        self.lastNameLineEdit.setMouseTracking(True)
        self.lastNameLineEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(20, 120, 41, 16))
        self.lastLabel = QLabel(self.centralwidget)
        self.lastLabel.setObjectName(u"lastLabel")
        self.lastLabel.setGeometry(QRect(270, 120, 71, 20))
        self.barcodeLabel = QLabel(self.centralwidget)
        self.barcodeLabel.setObjectName(u"barcodeLabel")
        self.barcodeLabel.setGeometry(QRect(20, 200, 201, 71))
        font2 = QFont()
        font2.setFamilies([u"Libre Barcode 128 Text"])
        font2.setPointSize(36)
        self.barcodeLabel.setFont(font2)
        self.PrintPushButton = QPushButton(self.centralwidget)
        self.PrintPushButton.setObjectName(u"PrintPushButton")
        self.PrintPushButton.setEnabled(False)
        self.PrintPushButton.setGeometry(QRect(380, 210, 131, 41))
        font3 = QFont()
        font3.setPointSize(18)
        self.PrintPushButton.setFont(font3)
        self.PrintPushButton.setStyleSheet(u"")
        self.amountSpinBox = QSpinBox(self.centralwidget)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(270, 210, 101, 41))
        font4 = QFont()
        font4.setPointSize(24)
        self.amountSpinBox.setFont(font4)
        self.amountSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.amountSpinBox.setMaximum(99)
        self.amountStickerLabel = QLabel(self.centralwidget)
        self.amountStickerLabel.setObjectName(u"amountStickerLabel")
        self.amountStickerLabel.setGeometry(QRect(270, 190, 81, 16))
        self.exampleStickerLabel = QLabel(self.centralwidget)
        self.exampleStickerLabel.setObjectName(u"exampleStickerLabel")
        self.exampleStickerLabel.setGeometry(QRect(20, 190, 61, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 19))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.ssnLineEdit, self.firstNameLineEdit)
        QWidget.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        QWidget.setTabOrder(self.lastNameLineEdit, self.amountSpinBox)
        QWidget.setTabOrder(self.amountSpinBox, self.PrintPushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.ssnLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Suomalainen henkil\u00f6tunnus", None))
#endif // QT_CONFIG(tooltip)
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"311259-123X", None))
        self.ssnLabel_2.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.lastLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.barcodeLabel.setText(QCoreApplication.translate("MainWindow", u"ppkkvv-nnnv", None))
        self.PrintPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.amountStickerLabel.setText(QCoreApplication.translate("MainWindow", u"Etikettien m\u00e4\u00e4r\u00e4", None))
        self.exampleStickerLabel.setText(QCoreApplication.translate("MainWindow", u"Mallietiketti", None))
    # retranslateUi

