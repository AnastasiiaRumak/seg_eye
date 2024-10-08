# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anastasiia/eyes/seg/segmenter/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QSlider, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QLabel, QSizePolicy, QHBoxLayout, QPushButton
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 761, 491))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(110, 330, 181, 41))
        self.pushButton.setObjectName("pushButton")

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.imageLable = QtWidgets.QLabel(self.page_2)
        self.imageLable.setGeometry(QtCore.QRect(10, 40, 481, 461))
        self.imageLable.setText("")
        self.imageLable.setObjectName("imageLable")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 50, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout.addWidget(self.horizontalSlider_3)
        self.stackedWidget.addWidget(self.page_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.switch_to_page_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "выборать изображение"))
        self.label.setText(_translate("MainWindow", "1 parametr"))
        self.label_2.setText(_translate("MainWindow", "2 parametr"))
        self.label_3.setText(_translate("MainWindow", "3 paratetr"))

    def switch_to_page_2(self):
        """Метод для переключения на вторую страницу"""
        # Открываем диалоговое окно для выбора изображения
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Изображения (*.png *.xpm *.jpg *.jpeg *.JPG);;Все файлы (*)", options=options)

        if file_name:
            # Загружаем изображение с помощью OpenCV
            image = cv2.imread(file_name)
            if image is None:
                QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение")
                return

            # Преобразуем изображение в формат, совместимый с QPixmap
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channels = image.shape
            bytes_per_line = channels * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Получаем QPixmap из QImage
            pixmap = QPixmap.fromImage(q_image)

            # Получаем доступ к QLabel и масштабируем изображение
            label = self.imageLable  # Используем имя imageLabel
            scaled_pixmap = pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

            # Устанавливаем масштабированное изображение в QLabel
            label.setPixmap(scaled_pixmap)

            # При необходимости, можно изменить размер QLabel, чтобы он соответствовал изображению
            label.setFixedSize(scaled_pixmap.size())  # Устанавливаем размер QLabel под размер изображения

        self.stackedWidget.setCurrentIndex(1)  # Переход на вторую страницу

