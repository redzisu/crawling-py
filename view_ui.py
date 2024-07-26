# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(110, 10, 571, 61))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.btn_folder = QPushButton(self.gridLayoutWidget)
        self.btn_folder.setObjectName(u"btn_folder")

        self.gridLayout_2.addWidget(self.btn_folder, 1, 3, 1, 1)

        self.ibx_scrollNum = QSpinBox(self.gridLayoutWidget)
        self.ibx_scrollNum.setObjectName(u"ibx_scrollNum")
        self.ibx_scrollNum.setValue(1)

        self.gridLayout_2.addWidget(self.ibx_scrollNum, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.btn_search = QPushButton(self.gridLayoutWidget)
        self.btn_search.setObjectName(u"btn_search")

        self.gridLayout_2.addWidget(self.btn_search, 0, 3, 1, 1)

        self.ibx_keyword = QLineEdit(self.gridLayoutWidget)
        self.ibx_keyword.setObjectName(u"ibx_keyword")

        self.gridLayout_2.addWidget(self.ibx_keyword, 0, 1, 1, 1)

        self.ibx_path = QLineEdit(self.gridLayoutWidget)
        self.ibx_path.setObjectName(u"ibx_path")
        self.ibx_path.setEnabled(False)

        self.gridLayout_2.addWidget(self.ibx_path, 1, 1, 1, 2)

        self.grd_list = QTableWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setGeometry(QRect(20, 250, 761, 301))
        self.console = QTextEdit(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(20, 120, 761, 121))
        self.console.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.console.setReadOnly(True)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 90, 761, 23))
        self.progressBar.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Keyword", None))
        self.btn_folder.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Download path", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

