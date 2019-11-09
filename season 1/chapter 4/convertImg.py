# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_openimage(object):
    def setupUi(self, openimage):
        openimage.setObjectName("openimage")
        openimage.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(openimage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_raw = QtWidgets.QLabel(self.centralwidget)
        self.label_raw.setGeometry(QtCore.QRect(50, 140, 201, 211))
        self.label_raw.setObjectName("label_raw")
        self.readButton = QtWidgets.QPushButton(self.centralwidget)
        self.readButton.setGeometry(QtCore.QRect(90, 410, 99, 27))
        self.readButton.setObjectName("readButton")
        self.label_red = QtWidgets.QLabel(self.centralwidget)
        self.label_red.setGeometry(QtCore.QRect(520, 30, 150, 150))
        self.label_red.setObjectName("label_red")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(310, 250, 99, 27))
        self.convertButton.setObjectName("convertButton")
        self.label_green = QtWidgets.QLabel(self.centralwidget)
        self.label_green.setGeometry(QtCore.QRect(520, 190, 150, 150))
        self.label_green.setObjectName("label_green")
        self.label_blue = QtWidgets.QLabel(self.centralwidget)
        self.label_blue.setGeometry(QtCore.QRect(520, 370, 150, 150))
        self.label_blue.setObjectName("label_blue")
        openimage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(openimage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        openimage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(openimage)
        self.statusbar.setObjectName("statusbar")
        openimage.setStatusBar(self.statusbar)

        self.retranslateUi(openimage)
        self.readButton.clicked.connect(openimage.openNewImage)
        self.convertButton.clicked.connect(openimage.convertImg)
        QtCore.QMetaObject.connectSlotsByName(openimage)

    def retranslateUi(self, openimage):
        _translate = QtCore.QCoreApplication.translate
        openimage.setWindowTitle(_translate("openimage", "MainWindow"))
        self.label_raw.setText(_translate("openimage", "读取图片"))
        self.readButton.setText(_translate("openimage", "打开图片"))
        self.label_red.setText(_translate("openimage", "R通道"))
        self.convertButton.setText(_translate("openimage", "分离"))
        self.label_green.setText(_translate("openimage", "G通道"))
        self.label_blue.setText(_translate("openimage", "B通道"))

