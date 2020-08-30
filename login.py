# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from proj import encrypter
from mypasswords import Ui_mypasswords
import os.path

class Ui_login(object):
    def back(self,login):
        from firstpage import Ui_Form    
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        login.hide()
        self.window.show()
#     def mypass(self):
#         self.window = QtWidgets.QWidget() 
#         self.mes="p"
#         self.ui = Ui_mypasswords(self.mes)
#         self.ui.setupUi(self.window)
#         login.hide()
#         self.window.show()        
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(592, 383)
        login.setStyleSheet("#login{\n"
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
        self.inptusrName = QtWidgets.QLineEdit(login)
        self.inptusrName.setGeometry(QtCore.QRect(190, 150, 221, 31))
        self.inptusrName.setObjectName("inptusrName")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(190, 120, 91, 21))
        self.label.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 91, 21))
        self.label_2.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label_2.setObjectName("label_2")
        self.inptpswd = QtWidgets.QLineEdit(login)
        self.inptpswd.setGeometry(QtCore.QRect(190, 220, 221, 31))
        self.inptpswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inptpswd.setObjectName("inptpswd")
        self.create_button = QtWidgets.QPushButton(login)
        self.create_button.setGeometry(QtCore.QRect(480, 330, 91, 31))
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(lambda:self.log(login))
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setGeometry(QtCore.QRect(100, 20, 411, 51))
        self.label_4.setStyleSheet("background:rgb(1, 253, 60);\n"
"border-radius:25px;\n"
"color:white;\n"
"font: 25pt;")
        self.label_4.setObjectName("label_4")
        self.back_btn = QtWidgets.QPushButton(login)
        self.back_btn.setGeometry(QtCore.QRect(20, 330, 91, 31))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda:self.back(login))
        self.clear_button = QtWidgets.QPushButton(login)
        self.clear_button.setGeometry(QtCore.QRect(250, 330, 91, 31))
        self.clear_button.setObjectName("clear_button")
        self.clear_button.clicked.connect(self.clear)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.label.setText(_translate("login", "User Name :"))
        self.label_2.setText(_translate("login", "Password :"))
        self.create_button.setText(_translate("login", "Login"))
        self.label_4.setText(_translate("login", "<html><head/><body><p align=\"center\">Login</p></body></html>"))
        self.back_btn.setText(_translate("login", "Back"))
        self.clear_button.setText(_translate("login", "Clear"))
    def messagefun(self,text):
        self.mes = QtWidgets.QMessageBox()
        self.mes.setIcon(self.mes.Warning)
        self.mes.setInformativeText(text)
        self.mes.show()
    def clear (self):
        
        self.inptpswd.setText("") 
        self.inptusrName.setText("")                
    def log(self,login):
        usrname=self.inptusrName.text()
        passw = self.inptpswd.text()
        if usrname=="" or passw =="":
                self.messagefun("All fields should be filled")
        else : 
                if os.path.isfile("user/"+usrname + ".txt"):       
                        file=open("user/"+usrname + ".txt",'r')
                        line=file.readlines() 
                        file.close()
                        if line[2].strip()== encrypter(passw,usrname).strip() :
                                        
                                self.window = QtWidgets.QWidget() 
                                self.messsage=usrname
                                self.ui = Ui_mypasswords(self.messsage)
                                self.ui.setupUi(self.window)
                                login.hide()
                                self.window.show()
                        else :
                                self.messagefun("wrong password")        
                else :
                        self.messagefun("The user doesnot exist")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
