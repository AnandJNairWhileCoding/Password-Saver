# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\createusr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


  
from PyQt5 import QtCore, QtGui, QtWidgets
import os.path
import random
from proj import encrypter,appnd
from mypasswords import Ui_mypasswords
char="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=+_/,.<>?;':"}[]{ |"""

# print(random.shuffle(char))
class Ui_createUser(object):
    def back(self,createUser):
        from firstpage import Ui_Form    
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        createUser.hide()
        self.window.show() 
#     def mypass(self,message):
#         self.window = QtWidgets.QWidget()
#         self.createUser = QtWidgets.QWidget()
#         self.message=message
#         self.ui = Ui_mypasswords(self.message)
#         self.ui.setupUi(self.window)
        
#         self.window.show()
        


    def setupUi(self, createUser):
        createUser.setObjectName("createUser")
        createUser.resize(592, 383)
        createUser.setStyleSheet("#createUser{\n"
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
        self.inptusrName = QtWidgets.QLineEdit(createUser)
        self.inptusrName.setGeometry(QtCore.QRect(190, 130, 221, 31))
        self.inptusrName.setObjectName("inptusrName")
        self.label = QtWidgets.QLabel(createUser)
        self.label.setGeometry(QtCore.QRect(190, 100, 91, 21))
        self.label.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createUser)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 91, 21))
        self.label_2.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label_2.setObjectName("label_2")
        self.inptpswd = QtWidgets.QLineEdit(createUser)
        self.inptpswd.setGeometry(QtCore.QRect(190, 200, 221, 31))
        self.inptpswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inptpswd.setObjectName("inptpswd")
        self.inptcinfrmpswd = QtWidgets.QLineEdit(createUser)
        self.inptcinfrmpswd.setGeometry(QtCore.QRect(190, 270, 221, 31))
        self.inptcinfrmpswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inptcinfrmpswd.setObjectName("inptcinfrmpswd")
        self.label_3 = QtWidgets.QLabel(createUser)
        self.label_3.setGeometry(QtCore.QRect(190, 240, 141, 21))
        self.label_3.setStyleSheet("color:rgb(1, 253, 60);\n"
"font:12pt;")
        self.label_3.setObjectName("label_3")
        self.create_button = QtWidgets.QPushButton(createUser)
        self.create_button.setGeometry(QtCore.QRect(480, 330, 91, 31))
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(lambda:self.createa(createUser))
        self.label_4 = QtWidgets.QLabel(createUser)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 411, 51))
        self.label_4.setStyleSheet("background:rgb(1, 253, 60);\n"
"border-radius:25px;\n"
"color:white;\n"
"font: 25pt;")
        self.label_4.setObjectName("label_4")
        self.back_btn = QtWidgets.QPushButton(createUser)
        self.back_btn.setGeometry(QtCore.QRect(20, 330, 91, 31))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda:self.back(createUser))
        self.clear_button = QtWidgets.QPushButton(createUser)
        self.clear_button.setGeometry(QtCore.QRect(250, 330, 91, 31))
        self.clear_button.setObjectName("clear_button")
        self.clear_button.clicked.connect(self.clear)

        self.retranslateUi(createUser)
        QtCore.QMetaObject.connectSlotsByName(createUser)

    def retranslateUi(self, createUser):
        _translate = QtCore.QCoreApplication.translate
        createUser.setWindowTitle(_translate("createUser", "Create Account"))
        self.label.setText(_translate("createUser", "User Name :"))
        self.label_2.setText(_translate("createUser", "Password :"))
        self.label_3.setText(_translate("createUser", "Confirm Password :"))
        self.create_button.setText(_translate("createUser", "Create"))
        self.label_4.setText(_translate("createUser", "<html><head/><body><p align=\"center\">Create User</p></body></html>"))
        self.back_btn.setText(_translate("createUser", "Back"))
        self.clear_button.setText(_translate("createUser", "Clear"))
#     def hid(self,createUser):
#         createUser.hide()
    def messagefun(self,text):
        self.mes = QtWidgets.QMessageBox()
        self.mes.setIcon(self.mes.Warning)
        self.mes.setInformativeText(text)
        self.mes.show() 
    def clear (self):
        self.inptcinfrmpswd.setText("")
        self.inptpswd.setText("") 
        self.inptusrName.setText("")                  
    def createa(self,createUser):
        usrName=self.inptusrName.text()
        password=self.inptpswd.text()
        if usrName=="" or password =="":
                self.messagefun("All the fields should be filled")
        else:        
                conf_password=self.inptcinfrmpswd.text()
                if os.path.isfile("user/"+usrName + ".txt"):
                        self.messagefun("The user name already exist !")
                else:
                        if password == conf_password:
                                usrfile=open("user/"+usrName + ".txt" , "a")
                                usrfile.write(char + "\n")
                                tmp=random.sample(range(1111,9999), len(char))
                                #print(tmp)
                                for num in tmp:
                                        usrfile.write(str(num))
                                usrfile.close()
                                appnd(usrName,encrypter(password,usrName)) 
                                self.usrName=usrName 
                            #    lambda:self.hid(createUser)
                                # self.createUser = QtWidgets.QWidget()
                                # self.createUser.hide()
                               # self.mypass(self.usrName)
                                # def mypass(self,message):
                                self.window = QtWidgets.QWidget()
                                self.createUser = QtWidgets.QWidget()
                                self.message=usrName
                                self.ui = Ui_mypasswords(self.message)
                                self.ui.setupUi(self.window)
                                createUser.hide()               
                                self.window.show()        
                        else :
                                self.messagefun("Your passwords doesn't match with confirm password")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createUser = QtWidgets.QWidget()
    ui = Ui_createUser()
    ui.setupUi(createUser)
    createUser.show()
    sys.exit(app.exec_())
