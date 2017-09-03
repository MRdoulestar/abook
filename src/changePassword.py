# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePassword.ui'
#
# Created: Mon Feb  6 12:31:28 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_changePasswordWindow(object):
    def setupUi(self, changePasswordWindow):
        changePasswordWindow.setObjectName("changePasswordWindow")
        changePasswordWindow.resize(440, 329)
        changePasswordWindow.setStyleSheet("")
        changePasswordWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(changePasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.changePasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePasswordButton.setGeometry(QtCore.QRect(90, 220, 101, 31))
        self.changePasswordButton.setAutoDefault(False)
        self.changePasswordButton.setDefault(False)
        self.changePasswordButton.setFlat(False)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(260, 220, 101, 31))
        self.returnButton.setObjectName("returnButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 51, 16))
        self.label_2.setObjectName("label_2")
        self.oldPassword = QtWidgets.QTextBrowser(self.centralwidget)
        self.oldPassword.setGeometry(QtCore.QRect(150, 60, 211, 31))
        self.oldPassword.setObjectName("oldPassword")
        self.newPassword = QtWidgets.QTextBrowser(self.centralwidget)
        self.newPassword.setGeometry(QtCore.QRect(150, 110, 211, 31))
        self.newPassword.setObjectName("newPassword")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 280, 151, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 91, 16))
        self.label_4.setObjectName("label_4")
        self.newPasswordCheck = QtWidgets.QTextBrowser(self.centralwidget)
        self.newPasswordCheck.setGeometry(QtCore.QRect(150, 160, 211, 31))
        self.newPasswordCheck.setObjectName("newPasswordCheck")
        changePasswordWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(changePasswordWindow)
        self.statusbar.setObjectName("statusbar")
        changePasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(changePasswordWindow)
        self.returnButton.clicked.connect(changePasswordWindow.quitButton)
        self.changePasswordButton.clicked.connect(changePasswordWindow.regButton)
        QtCore.QMetaObject.connectSlotsByName(changePasswordWindow)
        changePasswordWindow.setTabOrder(self.oldPassword, self.newPassword)
        changePasswordWindow.setTabOrder(self.newPassword, self.changePasswordButton)
        changePasswordWindow.setTabOrder(self.changePasswordButton, self.returnButton)

    def retranslateUi(self, changePasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        changePasswordWindow.setWindowTitle(_translate("changePasswordWindow", "修改密码"))
        self.changePasswordButton.setText(_translate("changePasswordWindow", "修改"))
        self.returnButton.setText(_translate("changePasswordWindow", "返回"))
        self.label.setText(_translate("changePasswordWindow", "原密码："))
        self.label_2.setText(_translate("changePasswordWindow", "新密码："))
        self.label_3.setText(_translate("changePasswordWindow", "Designed by yunsle"))
        self.label_4.setText(_translate("changePasswordWindow", "确认新密码："))

