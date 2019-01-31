#!/usr/bin/env python

import configparser
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from design import Ui_mainWindow

from PyQt5.QtGui import QIcon, QPixmap


class GetConfig:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('config.cfg')

        self.logo = config.get('HOME', 'logo')
        self.img = config.get('HOME', 'img')
        self.title = config.get('HOME', 'title')
        self.left = config.getint('HOME', 'left')
        self.top = config.getint('HOME', 'top')
        self.width = config.getint('HOME', 'width')
        self.height = config.getint('HOME', 'height')


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        config = GetConfig()

        self.ui = Ui_mainWindow()
        self.QtWidgets = QtWidgets
        self.QtGui = QtGui

        self.ui.setupUi(self)

        self.ui.tabWidget.setCurrentIndex(0)

        self.show()

        logo = QPixmap(config.logo)
        self.ui.logoView.setPixmap(logo)
        self.ui.logoView.resize(logo.width(), logo.height())

        home_img = QPixmap(config.img)
        self.ui.imageView.setPixmap(home_img)
        self.ui.imageView.resize(350, 220)

        self.setWindowTitle(' ')
        self.left = config.left
        self.top = config.top
        self.resize(QtCore.QSize(config.width, config.height))
        self.height = config.height

        self.ui.HeaderMenu.setText("OpenFOAM")

        self.ui.appsFullscreen.clicked.connect(self.apps_fullscreen)
        self.ui.appsFullscreen_back.clicked.connect(self.apps_fullscreen_back)
        self.ui.appsFullscreen_back.hide()

        self.ui.openfoamButton.clicked.connect(self.apps_btn0_clicked)
        self.ui.patoButton.clicked.connect(self.apps_btn1_clicked)
        self.ui.pumaButton.clicked.connect(self.apps_btn2_clicked)
        self.ui.oplrButton.clicked.connect(self.apps_btn3_clicked)

        # OpenFOAM BUTTONS
        self.ui.of_documentationButton.clicked.connect(self.of_btn1_clicked)
        self.ui.of_installButton.clicked.connect(self.of_btn2_clicked)
        self.ui.of_testButton.clicked.connect(self.of_btn3_clicked)
        self.ui.of_runButton.clicked.connect(self.of_btn4_clicked)

        self.ui.installListView.hide()
        self.ui.installButton.hide()

        self.of_btn1_clicked()

        self.ui.openfoamButton.setStyleSheet("""
                   QPushButton:active{ background-color: #c1c1c1; }
               """
        )
        self.ui.appsGroupBox.setStyleSheet("""
                   QPushButton:focus{ background-color: #c1c1c1; }
                   QPushButton:hover{ background-color: white; }
               """
        )
        self.ui.appsQframe.setStyleSheet("""
                   QPushButton:focus{ background-color: #a1a1a1; }
                   QPushButton:hover{ background-color: white; }
               """
        )

    def apps_fullscreen(self):
        self.ui.textBrowser.setGeometry(QtCore.QRect(5, 10, self.ui.tabWidget.width() - 10, self.ui.tabWidget.height() - 80))
        self.ui.installListView.setGeometry(QtCore.QRect(5, 10, self.ui.tabWidget.width() - 10, self.ui.tabWidget.height() - 80))
        self.ui.installButton.setGeometry(QtCore.QRect(10, 660, 130, 25))
        self.ui.appsGroupBox.hide()
        self.ui.appsQframe.hide()

        self.ui.appsFullscreen.hide()
        self.ui.appsFullscreen_back.show()

    def apps_fullscreen_back(self):
        self.ui.textBrowser.setGeometry(QtCore.QRect(320, 80, 490, 430))
        self.ui.installListView.setGeometry(QtCore.QRect(320, 80, 490, 430))
        self.ui.installButton.setGeometry(QtCore.QRect(325, 480, 130, 25))
        self.ui.appsFullscreen.show()
        self.ui.appsFullscreen_back.hide()

        self.ui.appsGroupBox.show()
        self.ui.appsQframe.show()

    def apps_btn0_clicked(self):
        self.ui.HeaderMenu.setText(self.ui.openfoamButton.text())

    def apps_btn1_clicked(self):
        self.ui.HeaderMenu.setText(self.ui.patoButton.text())
        self.ui.openfoamButton.setStyleSheet(" ")

    def apps_btn2_clicked(self):
        self.ui.HeaderMenu.setText(self.ui.pumaButton.text())
        self.ui.openfoamButton.setStyleSheet(" ")

    def apps_btn3_clicked(self):
        self.ui.HeaderMenu.setText(self.ui.oplrButton.text())
        self.ui.openfoamButton.setStyleSheet(" ")

    # OpenFOAM Section
    def of_btn1_clicked(self):
        self.ui.installListView.hide()
        self.ui.installButton.hide()
        self.ui.textBrowser.show()
        text = open('data/apps_openfoam_documentation.html').read()
        self.ui.textBrowser.setText(text)

    def of_btn2_clicked(self):
        self.ui.textBrowser.hide()
        self.ui.installListView.setWindowTitle(' ')
        self.ui.installListView.setMinimumSize(200, 400)

        self.model = self.QtGui.QStandardItemModel(self.ui.installListView)

        self.packageList = [
            'OPENFOAM (5)',
            'GCC (5 or newer)',
            'openmpi (2.0.1 or newer)',
            'cmake (3.7.1 or newer)',
            'boost (1.61 or newer)'
        ]

        for plist in self.packageList:
            self.item = self.QtGui.QStandardItem(plist)
            self.item.setCheckable(True)
            self.model.appendRow(self.item)

        self.model.itemChanged.connect(self.on_item_changed)
        self.ui.installListView.setModel(self.model)
        self.ui.installListView.show()
        self.ui.installButton.show()

    def on_item_changed(self):
        if not self.item.checkState():
            return
        i = 0
        while self.model.item(i):
            if not self.model.item(i).checkState():
                return
            i += 1

    def of_btn3_clicked(self):
        self.ui.installListView.hide()
        self.ui.installButton.hide()
        self.ui.textBrowser.show()
        self.ui.textBrowser.setText("test")

    def of_btn4_clicked(self):
        self.ui.installListView.hide()
        self.ui.installButton.hide()
        self.ui.textBrowser.show()
        self.ui.textBrowser.setText("run")

    # PATO Section
    def pato_btn1_clicked(self):
        text = open('data/apps_openfoam_documentation.html').read()
        self.ui.textBrowser.setText(text)

    def pato_btn2_clicked(self):
        text = open('data/apps_openfoam_install.html').read()
        self.ui.textBrowser.setText(text)

    def pato_btn3_clicked(self):
        self.ui.textBrowser.setText("test")

    def pato_btn4_clicked(self):
        self.ui.textBrowser.setText("run")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()

    sys.exit(app.exec_())
