# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apps_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_apps_form(object):
    def setupUi(self, apps_form):
        apps_form.setObjectName("apps_form")
        apps_form.resize(387, 254)
        self.formLayoutWidget = QtWidgets.QWidget(apps_form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 123, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.documentationButton = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.documentationButton.sizePolicy().hasHeightForWidth())
        self.documentationButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.documentationButton.setFont(font)
        self.documentationButton.setObjectName("documentationButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.documentationButton)
        self.installButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.installButton.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.installButton.setFont(font)
        self.installButton.setObjectName("installButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.installButton)
        self.testButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.testButton.setFont(font)
        self.testButton.setObjectName("testButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.testButton)
        self.runButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.runButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(apps_form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 0, 241, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.retranslateUi(apps_form)
        QtCore.QMetaObject.connectSlotsByName(apps_form)

    def retranslateUi(self, apps_form):
        _translate = QtCore.QCoreApplication.translate
        apps_form.setWindowTitle(_translate("apps_form", "Form"))
        self.documentationButton.setText(_translate("apps_form", "Documentation"))
        self.installButton.setText(_translate("apps_form", "Install"))
        self.testButton.setText(_translate("apps_form", "Test"))
        self.runButton.setText(_translate("apps_form", "Run"))

