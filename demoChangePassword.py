# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoChangePassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 265)
        Dialog.setMinimumSize(QtCore.QSize(400, 265))
        Dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(50, -1, 70, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 11pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.gridLayout.addWidget(self.labelResponse, 3, 0, 1, 1)
        self.lineEditOldPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditOldPassword.setObjectName("lineEditOldPassword")
        self.gridLayout.addWidget(self.lineEditOldPassword, 0, 1, 1, 3)
        self.lineEditRePassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditRePassword.setObjectName("lineEditRePassword")
        self.gridLayout.addWidget(self.lineEditRePassword, 2, 1, 1, 3)
        self.lineEditNewPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")
        self.gridLayout.addWidget(self.lineEditNewPassword, 1, 1, 1, 3)
        self.pushButtonChangePassword = QtWidgets.QPushButton(Dialog)
        self.pushButtonChangePassword.setStyleSheet("font: 10pt \"Arial\";")
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")
        self.gridLayout.addWidget(self.pushButtonChangePassword, 3, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButtonChangePassword.clicked.connect(Dialog.SearchRows) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "????????????"))
        self.label_2.setText(_translate("Dialog", "????????????"))
        self.label_3.setText(_translate("Dialog", "??????????????????"))
        self.pushButtonChangePassword.setText(_translate("Dialog", "??????"))
