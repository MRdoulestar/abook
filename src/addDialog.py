# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialog.ui'
#
# Created: Tue Feb  7 11:10:00 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addDialog(object):
    def setupUi(self, addDialog):
        addDialog.setObjectName("addDialog")
        addDialog.setWindowModality(QtCore.Qt.NonModal)
        addDialog.resize(465, 298)
        self.addButton = QtWidgets.QPushButton(addDialog)
        self.addButton.setGeometry(QtCore.QRect(360, 60, 93, 28))
        self.addButton.setObjectName("addButton")
        self.returnButton = QtWidgets.QPushButton(addDialog)
        self.returnButton.setGeometry(QtCore.QRect(360, 110, 93, 28))
        self.returnButton.setObjectName("returnButton")
        self.frame = QtWidgets.QFrame(addDialog)
        self.frame.setGeometry(QtCore.QRect(30, 20, 321, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 41, 16))
        self.label_5.setObjectName("label_5")
        self.addNameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.addNameLineEdit.setGeometry(QtCore.QRect(100, 30, 171, 21))
        self.addNameLineEdit.setObjectName("addNameLineEdit")
        self.addTel1LineEdit = QtWidgets.QLineEdit(self.frame)
        self.addTel1LineEdit.setGeometry(QtCore.QRect(100, 70, 171, 21))
        self.addTel1LineEdit.setObjectName("addTel1LineEdit")
        self.addTel1LineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.addTel1LineEdit_2.setGeometry(QtCore.QRect(100, 110, 171, 21))
        self.addTel1LineEdit_2.setObjectName("addTel1LineEdit_2")
        self.addAddressLineEdit = QtWidgets.QLineEdit(self.frame)
        self.addAddressLineEdit.setGeometry(QtCore.QRect(100, 150, 171, 21))
        self.addAddressLineEdit.setObjectName("addAddressLineEdit")
        self.addQQLineEdit = QtWidgets.QLineEdit(self.frame)
        self.addQQLineEdit.setGeometry(QtCore.QRect(100, 190, 171, 21))
        self.addQQLineEdit.setObjectName("addQQLineEdit")
        self.line = QtWidgets.QFrame(addDialog)
        self.line.setGeometry(QtCore.QRect(340, 0, 16, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(addDialog)
        self.returnButton.clicked.connect(addDialog.returnMain)
        self.addButton.clicked.connect(addDialog.addTable)
        QtCore.QMetaObject.connectSlotsByName(addDialog)

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "添加联系人"))
        self.addButton.setText(_translate("addDialog", "添加"))
        self.returnButton.setText(_translate("addDialog", "返回"))
        self.label.setText(_translate("addDialog", "姓名："))
        self.label_2.setText(_translate("addDialog", "电话一："))
        self.label_3.setText(_translate("addDialog", "电话二："))
        self.label_4.setText(_translate("addDialog", "地址："))
        self.label_5.setText(_translate("addDialog", "QQ："))

