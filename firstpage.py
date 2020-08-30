# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_login
from createusr import Ui_createUser
from deleteaccount import Ui_delete_2

class Ui_Form(object):
    def login(self,Form):
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_login()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()
    def createusr(self,Form):
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_createUser()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def deleteusr(self,Form):
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_delete_2()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 385)
        Form.setStyleSheet("#Form{\n"
"background:white}\n"
"QFrame{\n"
"background:rgb(1, 253, 60);\n"
"border-radius:80px;}\n"
"\n"
"QPushButton{\n"
"background:rgb(1, 253, 60);\n"
"border:4px solid white;\n"
"border-radius:18px;\n"
"color:white;\n"
"font:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background:white;\n"
"color:rgb(1, 253, 60);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(120, 90, 331, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(100, 30, 131, 51))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(lambda:self.login(Form))
        self.create_btn = QtWidgets.QPushButton(self.frame)
        self.create_btn.setGeometry(QtCore.QRect(80, 100, 171, 51))
        self.create_btn.setObjectName("create_btn")
        self.create_btn.clicked.connect(lambda:self.createusr(Form))
        self.Delete_btn = QtWidgets.QPushButton(self.frame)
        self.Delete_btn.setGeometry(QtCore.QRect(80, 170, 171, 51))
        self.Delete_btn.setObjectName("Delete_btn")
        self.Delete_btn.clicked.connect(lambda:self.deleteusr(Form))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 321, 61))
        self.label.setStyleSheet("border-radius:20px;\n"
"color:rgb(1, 253, 60);;\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"background:white;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 360, 121, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Password Saver"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.create_btn.setText(_translate("Form", "Create Account"))
        self.Delete_btn.setText(_translate("Form", "Delete Account"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Password Saver</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Built By: Anand J Nair</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
