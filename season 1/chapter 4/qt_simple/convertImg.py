# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np

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

class PyQtMainEntry(QMainWindow, Ui_openimage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def openNewImage(self):
        # 打开文件选取对话框
        filename,  _ = QFileDialog.getOpenFileName(self, '打开图片', '../img_src/')
        if filename:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)

            self.label_raw.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_raw.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def convertImg(self):
        bayer = np.zeros((256, 256, 3), np.uint8)

        # R, G, G, B

        bayer[0:128, 0:128, 0] = 255

        bayer[0:128:, 128:256, 1] = 255
        bayer[128:256, 0:128, 1] = 255

        bayer[128:256, 128:256, 2] = 255


        if self.captured is not None:
            height, width, channels = self.captured.shape
            bytesPerLine = channels * width

            self.red = np.zeros((height, width, channels), np.uint8)
            self.red[:, :, 0] = self.captured[:, :, 0]

            QImg = QImage(self.red.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label_red.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_red.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            self.green = np.zeros((height, width, channels), np.uint8)
            self.green[:, :, 1] = self.captured[:, :, 1]

            QImg = QImage(self.green.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label_green.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_green.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            self.blue = np.zeros((height, width, channels), np.uint8)
            self.blue[:, :, 2] = self.captured[:, :, 2]

            QImg = QImage(self.blue.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label_blue.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_blue.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyQtMainEntry()
    win.show()
    sys.exit(app.exec())