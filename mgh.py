#!/usr/bin/env python

import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
# from mainwindow import Ui_MainWindow

import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
#    QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from mghui import Ui_MainWindow

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


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


class App(Ui_MainWindow):
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
        pixmap = QPixmap(config.logo)
        # Ui_MainWindow.logoView.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())

        # self.show()


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
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
