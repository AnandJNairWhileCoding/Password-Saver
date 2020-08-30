# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\mypasswords.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from proj import appnd,decrypter,encrypter



class Ui_mypasswords(object):
    def __init__(self,message):
        self.message=message
    def mainm(self,mypasswords):
        from firstpage import Ui_Form
        self.window = QtWidgets.QWidget() 
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        mypasswords.hide()
        self.window.show()
    def setupUi(self, mypasswords):
        mypasswords.setObjectName("mypasswords")
        mypasswords.resize(898, 593)
        mypasswords.setStyleSheet("#mypasswords{\n"
"background:white;}\n"
"QPushButton{\n"
"border:4px solid rgb(1, 253, 60);\n"
"border-radius:20px;\n"
"color:white;\n"
"background:rgb(1, 253, 60);\n"
"font:16pt;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(1, 253, 60);\n"
"background:white;\n"
"font:14pt;\n"
"}\n"
"QLineEdit{\n"
"border:4px solid rgb(1, 253, 60);\n"
"font:13pt;\n"
"color:rgb(1, 253, 60);\n"
"}\n"
"QLineEdit:hover{\n"
"border-radius:20px;\n"
"}\n"
"QTextEdit{\n"
"border:4px solid rgb(1, 253, 60);\n"
"border-radius:40px;\n"
"background:rgb(1, 253, 60);\n"
"color:white;\n"
"font:14pt;\n"
"}")
        self.save_password = QtWidgets.QPushButton(mypasswords)
        self.save_password.setGeometry(QtCore.QRect(350, 160, 161, 41))
        self.save_password.setObjectName("save_password")
        self.save_password.clicked.connect(self.savepass)
        self.account_name = QtWidgets.QLineEdit(mypasswords)
        self.account_name.setGeometry(QtCore.QRect(20, 100, 311, 41))
        self.account_name.setObjectName("account_name")
        self.password_output = QtWidgets.QTextEdit(mypasswords)
        self.password_output.setGeometry(QtCore.QRect(140, 220, 641, 301))
        self.password_output.setObjectName("password_output")
        
        self.mainmenu = QtWidgets.QPushButton(mypasswords)
        self.mainmenu.setGeometry(QtCore.QRect(20, 540, 171, 41))
        self.mainmenu.setObjectName("mainmenu")
        self.mainmenu.clicked.connect(lambda:self.mainm(mypasswords))
        self.show_password = QtWidgets.QPushButton(mypasswords)
        self.show_password.setGeometry(QtCore.QRect(700, 540, 181, 41))
        self.show_password.setObjectName("show_password")
        self.show_password.clicked.connect(self.showpass)
        self.password = QtWidgets.QLineEdit(mypasswords)
        self.password.setGeometry(QtCore.QRect(560, 100, 311, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(mypasswords)
        self.label.setGeometry(QtCore.QRect(20, 30, 861, 31))
        self.label.setStyleSheet("color: rgb(1, 253, 60);\n"
"font:20pt;")
        self.label.setObjectName("label")
        self.clear = QtWidgets.QPushButton(mypasswords)
        self.clear.setGeometry(QtCore.QRect(370, 540, 171, 41))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.cl)

        self.retranslateUi(mypasswords)
        QtCore.QMetaObject.connectSlotsByName(mypasswords)
        

    def retranslateUi(self, mypasswords):
        _translate = QtCore.QCoreApplication.translate
        mypasswords.setWindowTitle(_translate("mypasswords", self.message+"'s passwords"))
        self.save_password.setText(_translate("mypasswords", "Save Password"))
        self.account_name.setText(_translate("mypasswords", "Account Name"))
        self.mainmenu.setText(_translate("mypasswords", "Main Menu"))
        self.show_password.setText(_translate("mypasswords", "Show Passwords"))
        self.password.setText(_translate("mypasswords", "Password"))
        
        self.label.setText(_translate("mypasswords", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.label.setText("           Welcome "+(self.message).capitalize()+" Your Passwords are safe here !")
        self.clear.setText(_translate("mypasswords", "Clear"))
    def cl(self):
        
        self.account_name.setText("") 
        self.password.setText("")
        self.password_output.setPlainText("")        
    def savepass(self):
        toapnd=self.account_name.text()+" :  "+self.password.text()
        toapnd=encrypter(toapnd,self.message)
        appnd(self.message,toapnd)
    def showpass(self,mypasswords):
        file=open("user/"+self.message+".txt",'r')
        t=1;o=""
        for i in file:
            if t>3:
                #self.password_output.setPlainText(self.password_output.toPlainText + decrypter(u,i) + "\n")
                o=o +" "+ decrypter(self.message,i) +"\n"
            t=t+1 
        self.password_output.setPlainText(o)
        # ui.textEdit->verticalScrollBar()->setValue(ui.textEdit->verticalScrollBar()->maximum()
        # self.cursor=self.password_output.textCursor()
        # self.cursor.movePosition(QtGui.QTextCursor.End)
        # self.password_output.setFocus()
        self.password_output.moveCursor(QtGui.QTextCursor.End)
        #print(o)           
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mypasswords = QtWidgets.QWidget()
    ui = Ui_mypasswords()
    ui.setupUi(mypasswords)
    mypasswords.show()
    
    sys.exit(app.exec_())
