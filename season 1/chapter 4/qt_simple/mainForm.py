# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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

class Ui_openimage(object):
    def setupUi(self, openimage):
        openimage.setObjectName("openimage")
        openimage.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(openimage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 150, 150))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 80, 150, 150))
        self.label_2.setObjectName("label_2")
        self.div_channel = QtWidgets.QPushButton(self.centralwidget)
        self.div_channel.setGeometry(QtCore.QRect(480, 340, 99, 27))
        self.div_channel.setObjectName("div_channel")
        openimage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(openimage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        openimage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(openimage)
        self.statusbar.setObjectName("statusbar")
        openimage.setStatusBar(self.statusbar)

        self.retranslateUi(openimage)
        self.pushButton.clicked.connect(openimage.openNewImage)
        QtCore.QMetaObject.connectSlotsByName(openimage)

    def retranslateUi(self, openimage):
        _translate = QtCore.QCoreApplication.translate
        openimage.setWindowTitle(_translate("openimage", "MainWindow"))
        self.label.setText(_translate("openimage", "读取图片"))
        self.pushButton.setText(_translate("openimage", "打开图片"))
        self.label_2.setText(_translate("openimage", "分离通道图片"))
        self.div_channel.setText(_translate("openimage", "分离通道"))


class PyQtMainEntry(QMainWindow, Ui_openimage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def openNewImage(self):
        # 打开文件选取对话框
        filename,  _ = QFileDialog.getOpenFileName(self, '打开图片', '../')
        if filename:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)

            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyQtMainEntry()
    win.show()
    sys.exit(app.exec())
