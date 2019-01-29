#!/usr/bin/env python

import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from design import Ui_mainWindow

from PyQt5.QtGui import QIcon, QPixmap


class GetConfig:
    def __init__(self):
        config = ConfigParser.RawConfigParser()
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

        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

        #self.table_widget = MyTableWidget(self)
        #self.setCentralWidget(self.table_widget)

        # label = QLabel(self)
        self.ui = Ui_mainWindow()

        self.ui.setupUi(self)

        self.ui.tabWidget.setCurrentIndex(0)

        self.show()

        logo = QPixmap(config.logo)
        self.ui.logoView.setPixmap(logo)
        self.ui.logoView.resize(logo.width(), logo.height())

        home_img = QPixmap(config.img)
        self.ui.imageView.setPixmap(home_img)
        self.ui.imageView.resize(200, 120)

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

        # PATO BUTTONS
        self.ui.pato_documentationButton.clicked.connect(self.pato_btn1_clicked)
        self.ui.pato_installButton.clicked.connect(self.pato_btn2_clicked)
        self.ui.pato_testButton.clicked.connect(self.pato_btn3_clicked)
        self.ui.pato_runButton.clicked.connect(self.pato_btn4_clicked)

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

    def apps_fullscreen(self):
        self.ui.textBrowser.resize(350, 400)
        self.ui.appsFullscreen.hide()
        self.ui.appsFullscreen_back.show()

    def apps_fullscreen_back(self):
        self.ui.textBrowser.resize(200, 250)
        self.ui.appsFullscreen.show()
        self.ui.appsFullscreen_back.hide()

    def apps_btn0_clicked(self):
        self.ui.HeaderMenu.setText("OpenFOAM")

    def apps_btn1_clicked(self):
        self.ui.HeaderMenu.setText("PATO")

    def apps_btn2_clicked(self):
        self.ui.HeaderMenu.setText("PUMA")

    def apps_btn3_clicked(self):
        self.ui.HeaderMenu.setText("OPLR")

    # PATO Section
    def of_btn1_clicked(self):
        text = open('data/apps_openfoam_documentation.html').read()
        self.ui.textBrowser.setText(text)

    def of_btn2_clicked(self):
        text = open('data/apps_openfoam_install.html').read()
        self.ui.textBrowser.setText(text)

    def of_btn3_clicked(self):
        self.ui.textBrowser.setText("test")

    def of_btn4_clicked(self):
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
