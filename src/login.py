# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sun Feb  5 21:55:44 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(441, 251)
        loginWindow.setStyleSheet("")
        loginWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(90, 160, 101, 31))
        self.loginButton.setObjectName("loginButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(260, 160, 101, 31))
        self.quitButton.setObjectName("quitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 51, 16))
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QTextBrowser(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(150, 60, 211, 31))
        self.user.setObjectName("user")
        self.password = QtWidgets.QTextBrowser(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(150, 110, 211, 31))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 151, 20))
        self.label_3.setObjectName("label_3")
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        self.quitButton.clicked.connect(loginWindow.quitButton)
        self.loginButton.clicked.connect(loginWindow.loginButton)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)
        loginWindow.setTabOrder(self.user, self.password)
        loginWindow.setTabOrder(self.password, self.loginButton)
        loginWindow.setTabOrder(self.loginButton, self.quitButton)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "通讯录登录"))
        self.loginButton.setText(_translate("loginWindow", "登录"))
        self.quitButton.setText(_translate("loginWindow", "退出"))
        self.label.setText(_translate("loginWindow", "用户名："))
        self.label_2.setText(_translate("loginWindow", "密码："))
        self.label_3.setText(_translate("loginWindow", "Designed by yunsle"))

