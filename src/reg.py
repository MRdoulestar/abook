# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created: Sun Feb  5 22:19:05 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(440, 329)
        loginWindow.setStyleSheet("")
        loginWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.regButton = QtWidgets.QPushButton(self.centralwidget)
        self.regButton.setGeometry(QtCore.QRect(90, 220, 101, 31))
        self.regButton.setAutoDefault(False)
        self.regButton.setDefault(False)
        self.regButton.setFlat(False)
        self.regButton.setObjectName("regButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(260, 220, 101, 31))
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
        self.label_3.setGeometry(QtCore.QRect(150, 280, 151, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 71, 16))
        self.label_4.setObjectName("label_4")
        self.passwordCheck = QtWidgets.QTextBrowser(self.centralwidget)
        self.passwordCheck.setGeometry(QtCore.QRect(150, 160, 211, 31))
        self.passwordCheck.setObjectName("passwordCheck")
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        self.quitButton.clicked.connect(loginWindow.quitButton)
        self.regButton.clicked.connect(loginWindow.regButton)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)
        loginWindow.setTabOrder(self.user, self.password)
        loginWindow.setTabOrder(self.password, self.regButton)
        loginWindow.setTabOrder(self.regButton, self.quitButton)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "通讯录登录"))
        self.regButton.setText(_translate("loginWindow", "注册"))
        self.quitButton.setText(_translate("loginWindow", "退出"))
        self.label.setText(_translate("loginWindow", "用户名："))
        self.label_2.setText(_translate("loginWindow", "密码："))
        self.label_3.setText(_translate("loginWindow", "Designed by yunsle"))
        self.label_4.setText(_translate("loginWindow", "确认密码："))

