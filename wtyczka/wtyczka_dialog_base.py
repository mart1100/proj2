# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wtyczkaDialogBase(object):
    def setupUi(self, wtyczkaDialogBase):
        wtyczkaDialogBase.setObjectName("wtyczkaDialogBase")
        wtyczkaDialogBase.resize(430, 597)
        self.combo_box = QgsMapLayerComboBox(wtyczkaDialogBase)
        self.combo_box.setGeometry(QtCore.QRect(170, 20, 151, 27))
        self.combo_box.setObjectName("combo_box")
        self.label_przewyzszenie_wynik = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_przewyzszenie_wynik.setGeometry(QtCore.QRect(60, 400, 131, 21))
        self.label_przewyzszenie_wynik.setObjectName("label_przewyzszenie_wynik")
        self.pushButton_dh = QtWidgets.QPushButton(wtyczkaDialogBase)
        self.pushButton_dh.setGeometry(QtCore.QRect(60, 350, 111, 23))
        self.pushButton_dh.setObjectName("pushButton_dh")
        self.label_wynik_dh = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_wynik_dh.setGeometry(QtCore.QRect(210, 400, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_wynik_dh.setFont(font)
        self.label_wynik_dh.setText("")
        self.label_wynik_dh.setObjectName("label_wynik_dh")
        self.buttonBox = QtWidgets.QDialogButtonBox(wtyczkaDialogBase)
        self.buttonBox.setGeometry(QtCore.QRect(240, 530, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label_wybierz_warstwe = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_wybierz_warstwe.setGeometry(QtCore.QRect(70, 0, 91, 61))
        self.label_wybierz_warstwe.setObjectName("label_wybierz_warstwe")
        self.pushButton_pole = QtWidgets.QPushButton(wtyczkaDialogBase)
        self.pushButton_pole.setGeometry(QtCore.QRect(230, 350, 111, 23))
        self.pushButton_pole.setObjectName("pushButton_pole")
        self.label_wynik_pole = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_wynik_pole.setGeometry(QtCore.QRect(230, 430, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_wynik_pole.setFont(font)
        self.label_wynik_pole.setText("")
        self.label_wynik_pole.setObjectName("label_wynik_pole")
        self.label_pole_wynik = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_pole_wynik.setGeometry(QtCore.QRect(60, 430, 151, 21))
        self.label_pole_wynik.setObjectName("label_pole_wynik")
        self.pushButton_zlicz = QtWidgets.QPushButton(wtyczkaDialogBase)
        self.pushButton_zlicz.setGeometry(QtCore.QRect(170, 60, 91, 23))
        self.pushButton_zlicz.setObjectName("pushButton_zlicz")
        self.label_obiekty = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_obiekty.setGeometry(QtCore.QRect(70, 100, 171, 21))
        self.label_obiekty.setObjectName("label_obiekty")
        self.label_wynik_obiekty = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_wynik_obiekty.setGeometry(QtCore.QRect(250, 100, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_wynik_obiekty.setFont(font)
        self.label_wynik_obiekty.setText("")
        self.label_wynik_obiekty.setObjectName("label_wynik_obiekty")
        self.label_obiekty_wsp = QtWidgets.QLabel(wtyczkaDialogBase)
        self.label_obiekty_wsp.setGeometry(QtCore.QRect(70, 150, 211, 21))
        self.label_obiekty_wsp.setObjectName("label_obiekty_wsp")
        self.line1 = QtWidgets.QFrame(wtyczkaDialogBase)
        self.line1.setGeometry(QtCore.QRect(-10, 130, 461, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.line = QtWidgets.QFrame(wtyczkaDialogBase)
        self.line.setGeometry(QtCore.QRect(-3, 309, 441, 51))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(wtyczkaDialogBase)
        self.line_2.setGeometry(QtCore.QRect(-10, 510, 461, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.list_wsp = QtWidgets.QListView(wtyczkaDialogBase)
        self.list_wsp.setGeometry(QtCore.QRect(70, 170, 256, 121))
        self.list_wsp.setObjectName("list_wsp")
        self.plik = QgsFileWidget(wtyczkaDialogBase)
        self.plik.setGeometry(QtCore.QRect(60, 300, 151, 27))
        self.plik.setObjectName("plik")
        self.comboBox_uklad = QtWidgets.QComboBox(wtyczkaDialogBase)
        self.comboBox_uklad.setGeometry(QtCore.QRect(220, 300, 121, 22))
        self.comboBox_uklad.setObjectName("comboBox_uklad")
        self.comboBox_uklad.addItem("")
        self.comboBox_uklad.addItem("")
        self.comboBox_uklad.addItem("")
        self.comboBox_uklad.addItem("")
        self.comboBox_uklad.addItem("")
        self.comboBox_jedn = QtWidgets.QComboBox(wtyczkaDialogBase)
        self.comboBox_jedn.setGeometry(QtCore.QRect(300, 460, 73, 22))
        self.comboBox_jedn.setObjectName("comboBox_jedn")
        self.comboBox_jedn.addItem("")
        self.comboBox_jedn.addItem("")
        self.comboBox_jedn.addItem("")

        self.retranslateUi(wtyczkaDialogBase)
        QtCore.QMetaObject.connectSlotsByName(wtyczkaDialogBase)

    def retranslateUi(self, wtyczkaDialogBase):
        _translate = QtCore.QCoreApplication.translate
        wtyczkaDialogBase.setWindowTitle(_translate("wtyczkaDialogBase", "wtyczka"))
        self.label_przewyzszenie_wynik.setText(_translate("wtyczkaDialogBase", "Przewyższenie wynosi"))
        self.pushButton_dh.setText(_translate("wtyczkaDialogBase", "Oblicz dh"))
        self.label_wybierz_warstwe.setText(_translate("wtyczkaDialogBase", "Wybierz warstwę"))
        self.pushButton_pole.setText(_translate("wtyczkaDialogBase", "Oblicz pole"))
        self.label_pole_wynik.setText(_translate("wtyczkaDialogBase", "Pole powierzchni  wynosi"))
        self.pushButton_zlicz.setText(_translate("wtyczkaDialogBase", "Zlicz"))
        self.label_obiekty.setText(_translate("wtyczkaDialogBase", "Liczba obiektów na warstwie wynosi:"))
        self.label_obiekty_wsp.setText(_translate("wtyczkaDialogBase", "Współrzędne wczytanych punktów:"))
        self.comboBox_uklad.setItemText(0, _translate("wtyczkaDialogBase", "PL-1992"))
        self.comboBox_uklad.setItemText(1, _translate("wtyczkaDialogBase", "PL-2000(strefa 5)"))
        self.comboBox_uklad.setItemText(2, _translate("wtyczkaDialogBase", "PL-2000(strefa 6)"))
        self.comboBox_uklad.setItemText(3, _translate("wtyczkaDialogBase", "PL-2000(strefa 7)"))
        self.comboBox_uklad.setItemText(4, _translate("wtyczkaDialogBase", "PL-2000(strefa 8)"))
        self.comboBox_jedn.setItemText(0, _translate("wtyczkaDialogBase", "m2"))
        self.comboBox_jedn.setItemText(1, _translate("wtyczkaDialogBase", "a"))
        self.comboBox_jedn.setItemText(2, _translate("wtyczkaDialogBase", "ha"))
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox
