# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(920, 710)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setBaseSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(250, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 107, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.home)
        self.groupBox.setGeometry(QtCore.QRect(30, 340, 481, 201))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 441, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.logoView = QtWidgets.QLabel(self.home)
        self.logoView.setGeometry(QtCore.QRect(470, 20, 71, 31))
        self.logoView.setAutoFillBackground(True)
        self.logoView.setObjectName("logoView")
        self.imageView = QtWidgets.QLabel(self.home)
        self.imageView.setGeometry(QtCore.QRect(220, 130, 54, 17))
        self.imageView.setObjectName("imageView")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.home)
        self.textBrowser_3.setGeometry(QtCore.QRect(450, 191, 171, 141))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.home, "")
        self.apps = QtWidgets.QWidget()
        self.apps.setObjectName("apps")
        self.label_6 = QtWidgets.QLabel(self.apps)
        self.label_6.setGeometry(QtCore.QRect(600, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.HeaderMenu = QtWidgets.QLabel(self.apps)
        self.HeaderMenu.setGeometry(QtCore.QRect(330, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.HeaderMenu.setFont(font)
        self.HeaderMenu.setText("")
        self.HeaderMenu.setObjectName("HeaderMenu")
        self.label_3 = QtWidgets.QLabel(self.apps)
        self.label_3.setGeometry(QtCore.QRect(620, 120, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.apps)
        self.label_4.setGeometry(QtCore.QRect(610, 140, 54, 17))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.apps)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 660, 139, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.patoLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.patoLayout.setContentsMargins(10, 0, 0, 0)
        self.patoLayout.setObjectName("patoLayout")
        self.pato_documentationButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pato_documentationButton.sizePolicy().hasHeightForWidth())
        self.pato_documentationButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pato_documentationButton.setFont(font)
        self.pato_documentationButton.setObjectName("pato_documentationButton")
        self.patoLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pato_documentationButton)
        self.pato_installButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pato_installButton.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pato_installButton.setFont(font)
        self.pato_installButton.setObjectName("pato_installButton")
        self.patoLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pato_installButton)
        self.pato_testButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pato_testButton.setFont(font)
        self.pato_testButton.setObjectName("pato_testButton")
        self.patoLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pato_testButton)
        self.pato_runButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pato_runButton.setFont(font)
        self.pato_runButton.setObjectName("pato_runButton")
        self.patoLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pato_runButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.apps)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 136, 188))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pumaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pumaButton.setFont(font)
        self.pumaButton.setObjectName("pumaButton")
        self.gridLayout_3.addWidget(self.pumaButton, 2, 0, 1, 1)
        self.patoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.patoButton.setFont(font)
        self.patoButton.setObjectName("patoButton")
        self.gridLayout_3.addWidget(self.patoButton, 1, 0, 1, 1)
        self.openfoamButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.openfoamButton.setFont(font)
        self.openfoamButton.setObjectName("openfoamButton")
        self.gridLayout_3.addWidget(self.openfoamButton, 0, 0, 1, 1)
        self.oplrButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.oplrButton.setFont(font)
        self.oplrButton.setObjectName("oplrButton")
        self.gridLayout_3.addWidget(self.oplrButton, 3, 0, 1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.apps)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(170, 80, 134, 191))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.openfoamLayout = QtWidgets.QFormLayout()
        self.openfoamLayout.setContentsMargins(10, -1, -1, -1)
        self.openfoamLayout.setObjectName("openfoamLayout")
        self.of_documentationButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.of_documentationButton.sizePolicy().hasHeightForWidth())
        self.of_documentationButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.of_documentationButton.setFont(font)
        self.of_documentationButton.setObjectName("of_documentationButton")
        self.openfoamLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.of_documentationButton)
        self.of_installButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.of_installButton.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.of_installButton.setFont(font)
        self.of_installButton.setObjectName("of_installButton")
        self.openfoamLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.of_installButton)
        self.of_testButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.of_testButton.setFont(font)
        self.of_testButton.setObjectName("of_testButton")
        self.openfoamLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.of_testButton)
        self.of_runButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.of_runButton.setFont(font)
        self.of_runButton.setObjectName("of_runButton")
        self.openfoamLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.of_runButton)
        self.horizontalLayout_4.addLayout(self.openfoamLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.apps)
        self.textBrowser.setGeometry(QtCore.QRect(320, 80, 239, 309))
        self.textBrowser.setObjectName("textBrowser")
        self.appsFullscreen = QtWidgets.QPushButton(self.apps)
        self.appsFullscreen.setGeometry(QtCore.QRect(560, 210, 16, 29))
        self.appsFullscreen.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appsFullscreen.setIcon(icon)
        self.appsFullscreen.setObjectName("appsFullscreen")
        self.appsFullscreen_back = QtWidgets.QPushButton(self.apps)
        self.appsFullscreen_back.setGeometry(QtCore.QRect(250, 360, 61, 29))
        self.appsFullscreen_back.setIcon(icon)
        self.appsFullscreen_back.setObjectName("appsFullscreen_back")
        self.tabWidget.addTab(self.apps, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "DAO TMP"))
        self.label_2.setText(_translate("mainWindow", "Design Analysis..."))
        self.groupBox.setTitle(_translate("mainWindow", "news"))
        self.textBrowser_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Using the Hello World guide, you’ll create a repository, start a branch, write comments, and open a pull request.</p></body></html>"))
        self.logoView.setText(_translate("mainWindow", "logo"))
        self.imageView.setText(_translate("mainWindow", "image"))
        self.textBrowser_3.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Using the Hello World guide, you’ll create a repository, start a branch, write comments, and open a pull request.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("mainWindow", "Home"))
        self.label_6.setText(_translate("mainWindow", "Utilities"))
        self.label_3.setText(_translate("mainWindow", "MESH"))
        self.label_4.setText(_translate("mainWindow", "TECPLOT"))
        self.pato_documentationButton.setText(_translate("mainWindow", "Documentation"))
        self.pato_installButton.setText(_translate("mainWindow", "Install"))
        self.pato_testButton.setText(_translate("mainWindow", "Test"))
        self.pato_runButton.setText(_translate("mainWindow", "Run"))
        self.pumaButton.setText(_translate("mainWindow", "PUMA"))
        self.patoButton.setText(_translate("mainWindow", "PATO"))
        self.openfoamButton.setText(_translate("mainWindow", "OpenFOAM"))
        self.oplrButton.setText(_translate("mainWindow", "OPLR"))
        self.of_documentationButton.setText(_translate("mainWindow", "Documentation"))
        self.of_installButton.setText(_translate("mainWindow", "Install"))
        self.of_testButton.setText(_translate("mainWindow", "Test"))
        self.of_runButton.setText(_translate("mainWindow", "Run"))
        self.appsFullscreen_back.setText(_translate("mainWindow", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.apps), _translate("mainWindow", "Apps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

