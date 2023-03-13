# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watsapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class window2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 579)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chislo = QtWidgets.QLineEdit(self.centralwidget)
        self.chislo.setObjectName("Nomer")
        self.verticalLayout.addWidget(self.chislo)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Name_pol = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_pol.setObjectName("Name_pol")
        self.verticalLayout.addWidget(self.Name_pol)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.prinat_zav = QtWidgets.QPushButton(self.centralwidget)
        self.prinat_zav.setObjectName("prinat_zav")
        self.verticalLayout.addWidget(self.prinat_zav)
        self.chislo.raise_()
        self.prinat_zav.raise_()
        self.Name_pol.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.activ_reg()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">номер</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">имя контакта</span></p><p><br/></p></body></html>"))
        self.prinat_zav.setText(_translate("MainWindow", "Зарегистрировать"))
     
        
    def records(self, Name_abon, nomer_abon):
        self.insert_data( Name_abon, nomer_abon)
    def activ_reg(self):
        self.prinat_zav.clicked.connect(self.activ_reg_2)
    def activ_reg_2(self):
        self.records(self.Name_pol.text(),self.chislo.text())
        
        
    def __init__(self):
        self.conn = sqlite3.connect('name.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Nomera (Name_abon text , nomer_abon text )''')
        self.conn.commit()

    def insert_data(self, Name_abon, nomer_abon):
        self.c.execute(f"SELECT Name_abon FROM Nomera WHERE Name_abon='{self.Name_pol.text()}' ")
        if self.c.fetchone() is None:
            self.c.execute(f"SELECT nomer_abon FROM Nomera WHERE nomer_abon='{self.chislo.text()}' ")
            if self.c.fetchone() is None:
                self.c.execute("INSERT INTO Nomera VALUES(?,?)",(self.Name_pol.text(),self.chislo.text()))
                self.conn.commit()
                self.oktain=QMessageBox()
                self.oktain.setWindowTitle("всё классно")
                self.oktain.setText("номер зарегистрирован")
                self.oktain.setStandardButtons(QMessageBox.Ok)
                self.oktain.exec_()
            else:
                self.eroor=QMessageBox()
                self.eroor.setWindowTitle("ошибка")
                self.eroor.setText("уже есть такой номер")
                self.eroor.setStandardButtons(QMessageBox.Ok)
                self.eroor.exec_()

        else:
            self.eroor=QMessageBox()
            self.eroor.setWindowTitle("ошибка")
            self.eroor.setText("уже есть такой номер")
            self.eroor.setStandardButtons(QMessageBox.Ok)
            self.eroor.exec_()
        self.conn.commit()
class window_contackt():
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())