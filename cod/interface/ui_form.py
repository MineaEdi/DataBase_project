# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(927, 442)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 891, 391))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 61, 16))
        self.textBrowser = QTextBrowser(self.page_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(60, 10, 141, 21))
        self.layoutWidget = QWidget(self.page_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 840, 211))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendarWidget = QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout.addWidget(self.calendarWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.calendarWidget_2 = QCalendarWidget(self.layoutWidget)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")

        self.verticalLayout_2.addWidget(self.calendarWidget_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.page_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 300, 281, 24))
        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 270, 281, 24))
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 10, 71, 21))
        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(600, 270, 261, 24))
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(700, 40, 81, 16))
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 49, 16))
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 270, 151, 81))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(170, 270, 41, 81))
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.widget1)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_6.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.widget1)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.verticalLayout_6.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.widget1)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.verticalLayout_6.addWidget(self.spinBox_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 50, 91, 16))
        self.widget2 = QWidget(self.page_4)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(310, 70, 258, 226))
        self.verticalLayout_10 = QVBoxLayout(self.widget2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.widget2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_10.addWidget(self.listWidget_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_8 = QPushButton(self.widget2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.widget2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_4)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.layoutWidget_4 = QWidget(self.page_1)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(330, 130, 100, 61))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.widget3 = QWidget(self.page_1)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(430, 130, 110, 61))
        self.verticalLayout_7 = QVBoxLayout(self.widget3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.widget3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_7.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.widget3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_7.addWidget(self.lineEdit_4)

        self.widget4 = QWidget(self.page_1)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(440, 190, 82, 56))
        self.verticalLayout_8 = QVBoxLayout(self.widget4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.widget4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pushButton_10 = QPushButton(self.page_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(390, 270, 80, 24))
        self.widget5 = QWidget(self.page_2)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(280, 90, 331, 171))
        self.horizontalLayout_5 = QHBoxLayout(self.widget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.widget5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)

        self.label_11 = QLabel(self.widget5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_14)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit = QLineEdit(self.widget5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_12.addWidget(self.lineEdit_2)

        self.lineEdit_5 = QLineEdit(self.widget5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_12.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.widget5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_12.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.widget5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_12.addWidget(self.lineEdit_7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.pushButton_9 = QPushButton(self.widget5)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 927, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Utilizator:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Rezerva!", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Verifica!", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Log out!", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Rezervarile mele!", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Disponibilitati!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Check-in", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Camera pentru 2 persoane", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Camera pentru 3 persoane", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Camera pentru 4 persoane", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rezervarile tale!", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Intoarcere", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Anuleaza", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nume de utilizator", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Parola", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Autentificare", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Inregistrare", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Intoarcere", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Prenume", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nume de utilizator", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Parola", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Inregistrare", None))
    # retranslateUi

