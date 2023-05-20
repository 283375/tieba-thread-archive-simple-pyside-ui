# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threadInfoDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.idLabel = QLabel(self.widget)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idLabel)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.titleLabel)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lzLabel = QLabel(self.widget)
        self.lzLabel.setObjectName(u"lzLabel")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lzLabel)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.barLabel = QLabel(self.widget)
        self.barLabel.setObjectName(u"barLabel")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.barLabel)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.idLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6807\u9898", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u697c\u4e3b", None))
        self.lzLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5427", None))
        self.barLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

