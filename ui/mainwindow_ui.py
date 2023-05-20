# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.store_idLineEdit = QLineEdit(self.tab)
        self.store_idLineEdit.setObjectName(u"store_idLineEdit")

        self.verticalLayout_2.addWidget(self.store_idLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.store_dirLabel = QLabel(self.tab)
        self.store_dirLabel.setObjectName(u"store_dirLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.store_dirLabel.sizePolicy().hasHeightForWidth())
        self.store_dirLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.store_dirLabel)

        self.store_dirChangeButton = QPushButton(self.tab)
        self.store_dirChangeButton.setObjectName(u"store_dirChangeButton")

        self.horizontalLayout.addWidget(self.store_dirChangeButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.store_confirmButton = QPushButton(self.tab)
        self.store_confirmButton.setObjectName(u"store_confirmButton")

        self.verticalLayout_2.addWidget(self.store_confirmButton)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalWidget_2 = QWidget(self.tab_2)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.update_dirLabel = QLabel(self.horizontalWidget_2)
        self.update_dirLabel.setObjectName(u"update_dirLabel")
        sizePolicy2.setHeightForWidth(self.update_dirLabel.sizePolicy().hasHeightForWidth())
        self.update_dirLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.update_dirLabel)

        self.update_dirChangeButton = QPushButton(self.horizontalWidget_2)
        self.update_dirChangeButton.setObjectName(u"update_dirChangeButton")

        self.horizontalLayout_2.addWidget(self.update_dirChangeButton)


        self.verticalLayout_3.addWidget(self.horizontalWidget_2)

        self.update_confirmButton = QPushButton(self.tab_2)
        self.update_confirmButton.setObjectName(u"update_confirmButton")

        self.verticalLayout_3.addWidget(self.update_confirmButton)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5728\u4e0b\u65b9\u8f93\u5165\u8d34\u5b50 ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uff08\u5047\u5982\u94fe\u63a5\u4e3a https://tieba.baidu.com/p/12345678\uff0c\u90a3\u4e48 ID \u5c31\u662f 12345678\u3002\u624b\u673a\u7aef\u53ef\u4ee5\u901a\u8fc7\u5206\u4eab \u2192 \u590d\u5236\u94fe\u63a5\u83b7\u53d6\u8d34\u5b50\u94fe\u63a5\uff09", None))
        self.store_dirLabel.setText(QCoreApplication.translate("MainWindow", u"\u7136\u540e\u6309\u53f3\u4fa7\u6309\u94ae\u9009\u62e9\u4e00\u4e2a\u7a7a\u76ee\u5f55", None))
        self.store_dirChangeButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.store_confirmButton.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6b64\u5b58\u6863", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5b58\u6863", None))
        self.update_dirLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6309\u53f3\u8fb9\u6309\u94ae\u9009\u62e9\u4e00\u4e2a\u6709\u6548\u7684\u5b58\u6863\u76ee\u5f55</p><p>\uff08\u53ef\u4ee5\u770b\u5230 info.yaml\u3001thread.yaml \u7684\u6587\u4ef6\u5939\uff09</p></body></html>", None))
        self.update_dirChangeButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.update_confirmButton.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u65b9\u4fbf\u6d4f\u89c8\u7684 HTML\uff08\u5f00\u53d1\u4e2d\uff0c\u6682\u4e0d\u53ef\u7528 > <\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u66f4\u65b0/\u7ba1\u7406", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5173\u6ce8 <a href=\"https://github.com/283375/tieba-thread-archive-simple-pyside-ui\"><span style=\" text-decoration: underline; color:#0000ff;\">\u8fd9\u4e2a github \u4ed3\u5e93 </span></a>\u83b7\u53d6\u66f4\u65b0\uff01</p></body></html>", None))
    # retranslateUi

