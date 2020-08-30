# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\deleteaccount.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from proj import encrypter

class Ui_delete_2(object):
    def back(self,delete_2):
        from firstpage import Ui_Form    
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        delete_2.hide()
        self.window.show()        
    def setupUi(self, delete_2):
        delete_2.setObjectName("delete_2")
        delete_2.resize(592, 383)
        delete_2.setStyleSheet("#delete_2{\n"
"background: white;}\n"
"\n"
"QLineEdit{\n"
"border:4px solid rgb(1, 253, 60);\n"
"color:rgb(1, 253, 60);\n"
"font:10pt;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"font: 14pt;\n"
"background:rgb(1, 253, 60);\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"background:white;\n"
"border:4px solid rgb(1, 253, 60);;\n"
"color:rgb(1, 253, 60);\n"
"}")
        self.inptusrName = QtWidgets.QLineEdit(delete_2)
        self.inptusrName.setGeometry(QtCore.QRect(190, 150, 221, 31))
        self.inptusrName.setObjectName("inptusrName")
        self.label = QtWidgets.QLabel(delete_2)
        self.label.setGeometry(QtCore.QRect(190, 120, 91, 21))
        self.label.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(delete_2)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 91, 21))
        self.label_2.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label_2.setObjectName("label_2")
        self.inptpswd = QtWidgets.QLineEdit(delete_2)
        self.inptpswd.setGeometry(QtCore.QRect(190, 220, 221, 31))
        self.inptpswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inptpswd.setObjectName("inptpswd")
        self.delete_btn = QtWidgets.QPushButton(delete_2)
        self.delete_btn.setGeometry(QtCore.QRect(480, 330, 91, 31))
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.delete)
        self.label_4 = QtWidgets.QLabel(delete_2)
        self.label_4.setGeometry(QtCore.QRect(100, 20, 411, 51))
        self.label_4.setStyleSheet("background:rgb(1, 253, 60);\n"
"border-radius:25px;\n"
"color:white;\n"
"font: 25pt;")
        self.label_4.setObjectName("label_4")
        self.clear_button = QtWidgets.QPushButton(delete_2)
        self.clear_button.setGeometry(QtCore.QRect(250, 330, 91, 31))
        self.clear_button.setObjectName("clear_button")
        self.clear_button.clicked.connect(self.clear)
        self.back_btn = QtWidgets.QPushButton(delete_2)
        self.back_btn.setGeometry(QtCore.QRect(20, 330, 91, 31))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda:self.back(delete_2))

        self.retranslateUi(delete_2)
        QtCore.QMetaObject.connectSlotsByName(delete_2)

    def retranslateUi(self, delete_2):
        _translate = QtCore.QCoreApplication.translate
        delete_2.setWindowTitle(_translate("delete_2", "Delete Account"))
        self.label.setText(_translate("delete_2", "User Name :"))
        self.label_2.setText(_translate("delete_2", "Password :"))
        self.delete_btn.setText(_translate("delete_2", "Delete"))
        self.label_4.setText(_translate("delete_2", "<html><head/><body><p align=\"center\">Delete Account</p></body></html>"))
        self.clear_button.setText(_translate("delete_2", "Clear"))
        self.back_btn.setText(_translate("delete_2", "Back"))
    def clear (self):
        
        self.inptpswd.setText("") 
        self.inptusrName.setText("")        
    def messagefun(self,text):
        self.mes = QtWidgets.QMessageBox()
        self.mes.setIcon(self.mes.Warning)
        self.mes.setInformativeText(text)
        self.mes.show()       
    def delete(self):
        usrname=self.inptusrName.text()
        passw = self.inptpswd.text()
        if usrname=="" or passw =="":
                self.messagefun("All the fields should be filled")
        else :        
                if os.path.isfile("user/"+usrname + ".txt"):
                        file=open("user/"+usrname + ".txt",'r')
                        line=file.readlines()
                        file.close() 
                        if line[2].strip()== encrypter(passw,usrname).strip() :
                                os.remove("user/"+usrname + ".txt")
                                self.messagefun("Account deleted !")
                                self.inptusrName.setText("")
                                self.inptpswd.setText("")
                        else :
                                self.messagefun("You have entered an incorrect password !")        
                else :
                        self.messagefun("The user doesn't exist !")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_2 = QtWidgets.QWidget()
    ui = Ui_delete_2()
    ui.setupUi(delete_2)
    delete_2.show()
    sys.exit(app.exec_())
