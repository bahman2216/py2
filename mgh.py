#!/usr/bin/env python

import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from mghui import Ui_MainWindow

from PyQt5.QtGui import QIcon, QPixmap


class GetConfig:
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')

        self.logo = config.get('HOME', 'logo')
        self.title = config.get('HOME', 'title')
        self.left = config.getint('HOME', 'left')
        self.top = config.getint('HOME', 'top')
        self.width = config.getint('HOME', 'width')
        self.height = config.getint('HOME', 'height')


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        config = GetConfig()

        self.title = config.title
        self.left = config.left
        self.top = config.top
        self.width = config.width
        self.height = config.height
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

        #self.table_widget = MyTableWidget(self)
        #self.setCentralWidget(self.table_widget)

        # label = QLabel(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.show()

        # pixmap = QPixmap(config.logo)
        # self.ui.logoView.setPixmap(pixmap)
        # self.ui.logoView.resize(pixmap.width(), pixmap.height())

        self.ui.HeaderMenu.setText("PATO")

        self.ui.patoButton.clicked.connect(self.apps_btn1_clicked)
        self.ui.pumaButton.clicked.connect(self.apps_btn2_clicked)
        self.ui.oplrButton.clicked.connect(self.apps_btn3_clicked)

        # PATO BUTTONS
        self.ui.documentorButton.clicked.connect(self.pato_btn1_clicked)
        self.ui.installButton.clicked.connect(self.pato_btn2_clicked)
        self.ui.testButton.clicked.connect(self.pato_btn3_clicked)
        self.ui.runButton.clicked.connect(self.pato_btn4_clicked)

    # def function(self):
    #     self.show_frame_in_display(self.config.logo)
    #
    # def show_frame_in_display(self, image_path):
    #     frame = QtGui.QWidget()
    #     label_Image = QtGui.QLabel(frame)
    #     image_profile = QtGui.QImage(image_path)  # QImage object
    #     image_profile = image_profile.scaled(250, 250, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
    #                                          transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
    #     label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile))

    def apps_btn1_clicked(self):
        self.ui.HeaderMenu.setText("PATO")

    def apps_btn2_clicked(self):
        self.ui.HeaderMenu.setText("PUMA")

    def apps_btn3_clicked(self):
        self.ui.HeaderMenu.setText("OPLR")

    # PATO Section
    def pato_btn1_clicked(self):
        text = open('documentor.html').read()
        self.ui.textBrowser.setText(text)

    def pato_btn2_clicked(self):
        text = open('install.html').read()
        self.ui.textBrowser.setText(text)

    def pato_btn3_clicked(self):
        self.ui.textBrowser.setText("test")

    def pato_btn4_clicked(self):
        self.ui.textBrowser.setText("run")

# class MyTableWidget(QWidget):
#     def __init__(self, parent):
#         super(QWidget, self).__init__(parent)
#         self.layout = QVBoxLayout(self)
#
#         # Initialize tab screen
#         self.tabs = QTabWidget()
#         self.home = QWidget()
#         self.tab2 = QWidget()
#         self.tab3 = QWidget()
#         self.tab4 = QWidget()
#         self.tabs.resize(300, 200)
#
#         # Add tabs
#         self.tabs.addTab(self.home, "Home")
#         self.tabs.addTab(self.tab2, "Apps")
#         self.tabs.addTab(self.tab3, "Utilities")
#         self.tabs.addTab(self.tab4, "News")
#
#         # Create first tab
#         self.home.layout = QVBoxLayout(self)
#
#         self.home.layout.addWidget(self.horizontalGroupBox)
#         self.home.setLayout(self.home.layout)
#
#         #
#         # self.pushButton1 = QPushButton("Click Btn")
#         # self.home.layout.addWidget(self.pushButton1)
#         # self.home.setLayout(self.home.layout)
#
#         # Add tabs to widget
#         self.layout.addWidget(self.tabs)
#         self.setLayout(self.layout)
#
#         self.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = App()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
