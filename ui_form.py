# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(538, 346)
        Widget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.dhtH = QLabel(Widget)
        self.dhtH.setObjectName(u"dhtH")
        sizePolicy.setHeightForWidth(self.dhtH.sizePolicy().hasHeightForWidth())
        self.dhtH.setSizePolicy(sizePolicy)
        self.dhtH.setStyleSheet(u"font: 28pt \"JetBrainsMono Nerd Font Mono\";")
        self.dhtH.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.dhtH)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.dhtC = QLabel(Widget)
        self.dhtC.setObjectName(u"dhtC")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dhtC.sizePolicy().hasHeightForWidth())
        self.dhtC.setSizePolicy(sizePolicy1)
        self.dhtC.setStyleSheet(u"font: 48pt \"JetBrainsMono Nerd Font Mono\";")
        self.dhtC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.dhtC)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.dhtF = QLabel(Widget)
        self.dhtF.setObjectName(u"dhtF")
        sizePolicy.setHeightForWidth(self.dhtF.sizePolicy().hasHeightForWidth())
        self.dhtF.setSizePolicy(sizePolicy)
        self.dhtF.setStyleSheet(u"font: 28pt \"JetBrainsMono Nerd Font Mono\";")

        self.verticalLayout_4.addWidget(self.dhtF)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.graphs = QHBoxLayout()
        self.graphs.setObjectName(u"graphs")

        self.verticalLayout_5.addLayout(self.graphs)


        self.verticalLayout_6.addWidget(self.frame)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"DHT11", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Humedad (%)", None))
        self.dhtH.setText(QCoreApplication.translate("Widget", u"0.00 ", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Temperatura (\u00b0C)", None))
        self.dhtC.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Temperatura (\u00b0F)", None))
        self.dhtF.setText(QCoreApplication.translate("Widget", u"0.00", None))
    # retranslateUi

