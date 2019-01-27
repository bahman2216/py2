#!/usr/bin/env python

import ConfigParser
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
    QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
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


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        config = GetConfig()

        self.title = config.title
        self.left = config.left
        self.top = config.top
        self.width = config.width
        self.height = config.height
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        label = QLabel(self)
        pixmap = QPixmap(config.logo)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.home = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.home, "Home")
        self.tabs.addTab(self.tab2, "Apps")
        self.tabs.addTab(self.tab3, "Utilities")
        self.tabs.addTab(self.tab4, "News")

        # Create first tab
        self.createGridLayout()

        self.home.layout = QVBoxLayout(self)

        self.home.layout.addWidget(self.horizontalGroupBox)
        self.home.setLayout(self.home.layout)

        #
        # self.pushButton1 = QPushButton("Click Btn")
        # self.home.layout.addWidget(self.pushButton1)
        # self.home.setLayout(self.home.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")

        layout = QGridLayout()
        layout.setColumnStretch(10, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.horizontalGroupBox.setLayout(layout)
    # @pyqtSlot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
