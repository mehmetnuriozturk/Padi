# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Padi.ui'
#
# Created: Mon Jul  8 10:49:10 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_padi(object):
    def setupUi(self, padi):
        padi.setObjectName(_fromUtf8("padi"))
        padi.resize(939, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/padi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        padi.setWindowIcon(icon)
        padi.setStyleSheet(_fromUtf8("#padiCentral{\n"
"    background-image: url(:/icons/b32.png);\n"
"    /*background-repeat: no-repeat;\n"
"    background-position: left top;*/\n"
"    /*background-color: #642437;*/\n"
"    /*alternate-background-color: gray;\n"
"    selection-background-color: gray;*/\n"
"    /*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.572, y2:0.688, stop:0 rgba(75, 114, 137, 255), stop:1 rgba(29, 42, 51, 255));*/\n"
"\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"background-color:qlineargradient(spread:pad, x1:0.595628, y1:0.721591, x2:1, y2:0, stop:0 rgba(255, 96, 0, 255), stop:0.415301 rgba(255, 142, 0, 255), stop:1 rgba(255, 127, 0, 255))\n"
"}\n"
"\n"
"#description {\n"
"    color:rgb(240, 240, 240);\n"
"}\n"
""))
        self.padiCentral = QtGui.QWidget(padi)
        self.padiCentral.setStyleSheet(_fromUtf8(""))
        self.padiCentral.setObjectName(_fromUtf8("padiCentral"))
        self.gridLayout_10 = QtGui.QGridLayout(self.padiCentral)
        self.gridLayout_10.setMargin(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.padiContainer = QtGui.QWidget(self.padiCentral)
        self.padiContainer.setMinimumSize(QtCore.QSize(650, 475))
        self.padiContainer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.padiContainer.setObjectName(_fromUtf8("padiContainer"))
        self.verticalLayout = QtGui.QVBoxLayout(self.padiContainer)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.statusProgLabel = QtGui.QLabel(self.padiContainer)
        self.statusProgLabel.setMinimumSize(QtCore.QSize(50, 30))
        self.statusProgLabel.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.statusProgLabel.setFont(font)
        self.statusProgLabel.setAutoFillBackground(False)
        self.statusProgLabel.setStyleSheet(_fromUtf8("padding: 8px 4px 4px 8px; \n"
"color: white;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-bottom-left-radius:2px;\n"
"\n"
""))
        self.statusProgLabel.setLineWidth(0)
        self.statusProgLabel.setText(_fromUtf8(""))
        self.statusProgLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/padi.png")))
        self.statusProgLabel.setScaledContents(True)
        self.statusProgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusProgLabel.setWordWrap(True)
        self.statusProgLabel.setMargin(4)
        self.statusProgLabel.setIndent(0)
        self.statusProgLabel.setObjectName(_fromUtf8("statusProgLabel"))
        self.horizontalLayout.addWidget(self.statusProgLabel)
        self.screenLabel = QtGui.QLabel(self.padiContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenLabel.sizePolicy().hasHeightForWidth())
        self.screenLabel.setSizePolicy(sizePolicy)
        self.screenLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.screenLabel.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.screenLabel.setFont(font)
        self.screenLabel.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-bottom: 1px solid rgba(0,0,0,10)\n"
"\n"
""))
        self.screenLabel.setLineWidth(0)
        self.screenLabel.setMidLineWidth(0)
        self.screenLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.screenLabel.setMargin(5)
        self.screenLabel.setIndent(-1)
        self.screenLabel.setObjectName(_fromUtf8("screenLabel"))
        self.horizontalLayout.addWidget(self.screenLabel)
        self.label = QtGui.QLabel(self.padiContainer)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-bottom: 1px solid rgba(0,0,0,10)\n"
""))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/nexttitle.png")))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.statusLabel = QtGui.QLabel(self.padiContainer)
        self.statusLabel.setMinimumSize(QtCore.QSize(200, 40))
        self.statusLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setAutoFillBackground(False)
        self.statusLabel.setStyleSheet(_fromUtf8("border-bottom-right-radius:2px;\n"
"color: white;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-bottom: 1px solid rgba(0,0,0,10)\n"
""))
        self.statusLabel.setLineWidth(2)
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusLabel.setWordWrap(False)
        self.statusLabel.setMargin(5)
        self.statusLabel.setIndent(0)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout.addWidget(self.statusLabel)
        self.frame = QtGui.QFrame(self.padiContainer)
        self.frame.setMinimumSize(QtCore.QSize(50, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet(_fromUtf8("border-bottom-right-radius:2px;\n"
"color: white;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-bottom: 1px solid rgba(0,0,0,10)\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_11 = QtGui.QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, -1, 5, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonTamEkran = QtGui.QPushButton(self.frame)
        self.buttonTamEkran.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonTamEkran.setMaximumSize(QtCore.QSize(25, 16777215))
        self.buttonTamEkran.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-left:1px solid rgba(255, 255, 255, 30);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border-top:1px solid  rgba(255, 255, 255, 40);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 40);\n"
"    border-left:1px solid rgba(255, 255, 255, 40);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-left:1px solid rgba(255, 255, 255, 30);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border-top:1px solid  rgba(255, 255, 255, 15);\n"
"    border-left:1px solid rgba(255, 255, 255, 15);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 15);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}"))
        self.buttonTamEkran.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tam-ekran.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonTamEkran.setIcon(icon1)
        self.buttonTamEkran.setFlat(True)
        self.buttonTamEkran.setObjectName(_fromUtf8("buttonTamEkran"))
        self.horizontalLayout_2.addWidget(self.buttonTamEkran)
        self.buttonTamEkrandanCik = QtGui.QPushButton(self.frame)
        self.buttonTamEkrandanCik.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonTamEkrandanCik.setMaximumSize(QtCore.QSize(25, 16777215))
        self.buttonTamEkrandanCik.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 30);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border-top:1px solid  rgba(255, 255, 255, 40);\n"
"    border-bottom:1px solid rgba(255, 255, 255, 40);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 40);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border-top:1px solid rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 30);\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 30);\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        self.buttonTamEkrandanCik.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tam-ekrandan-cik.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonTamEkrandanCik.setIcon(icon2)
        self.buttonTamEkrandanCik.setFlat(True)
        self.buttonTamEkrandanCik.setObjectName(_fromUtf8("buttonTamEkrandanCik"))
        self.horizontalLayout_2.addWidget(self.buttonTamEkrandanCik)
        self.gridLayout_11.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem, 0, 0, 1, 1)
        self.padiyazilabel = QtGui.QLabel(self.frame)
        self.padiyazilabel.setMinimumSize(QtCore.QSize(50, 30))
        self.padiyazilabel.setMaximumSize(QtCore.QSize(50, 50))
        self.padiyazilabel.setStyleSheet(_fromUtf8(""))
        self.padiyazilabel.setText(_fromUtf8(""))
        self.padiyazilabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/padi-yazi.png")))
        self.padiyazilabel.setScaledContents(True)
        self.padiyazilabel.setObjectName(_fromUtf8("padiyazilabel"))
        self.gridLayout_11.addWidget(self.padiyazilabel, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.mainStack = QtGui.QWidget(self.padiContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainStack.sizePolicy().hasHeightForWidth())
        self.mainStack.setSizePolicy(sizePolicy)
        self.mainStack.setMinimumSize(QtCore.QSize(200, 0))
        self.mainStack.setStyleSheet(_fromUtf8("QStackedWidget#mainStack{\n"
"/*background-color:rgba(255, 255, 255,0);*/\n"
"margin: 0px;\n"
"border-radius: 0px;\n"
"color: white;\n"
"}\n"
""))
        self.mainStack.setObjectName(_fromUtf8("mainStack"))
        self.gridLayout_3 = QtGui.QGridLayout(self.mainStack)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.stackedWidget = QtGui.QStackedWidget(self.mainStack)
        self.stackedWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 360))
        self.stackedWidget.setStyleSheet(_fromUtf8("#stackedWidget{\n"
"/*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 191));*/\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 80), stop:1 rgba(0, 0, 0, 40));\n"
"border-top: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"border-bottom: 1px solid rgba(255, 255, 255, 75);/*white*/\n"
"\n"
"}\n"
"QLabel{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 0));\n"
"border-radius:5px;\n"
"color:white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 0));\n"
"border-radius:3px;\n"
"color:white;\n"
"padding: 5px 5px 5px 5px;\n"
"border-bottom:0px;\n"
"border-top:0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border: 1px solid rgb(87, 87, 87);\n"
"border-radius:4px;\n"
"color:rgb(57, 57, 57)\n"
"}\n"
"\n"
"QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"     image: url(:/icons/unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"     image:url(:/icons/unchecked_hover.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked {\n"
"     image: url(:/icons/unchecked_checked.png)\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"     image: url(:/icons/unchecked_checked_hover.png)\n"
" }\n"
"\n"
"QScrollArea::corner {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 10));\n"
"    border: 0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        width: 13px;\n"
"        margin: 3px 3px 3px 3px;\n"
"        background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        min-height: 16px;\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"        border: 1px solid rgb(150, 150, 150);\n"
"        border-radius: 3px;\n"
"    padding:3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"        min-height: 16px;\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 80));\n"
"        border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"        border: 0px;\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 191));\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"        border: 0px;\n"
"        height: 0px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"        background: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"        height: 13px;\n"
"        margin: 3px 3px 3px 3px;\n"
"        background: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"        min-width: 16px;\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"        border: 1px solid rgb(150, 150, 150);\n"
"        border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"        min-width: 16px;\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 80));\n"
"        border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"        border: none;\n"
"        background: transparent;\n"
"        width: 0px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"        border: none;\n"
"        width: 0px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"}\n"
""))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.anaEkran = QtGui.QWidget()
        self.anaEkran.setStyleSheet(_fromUtf8(""))
        self.anaEkran.setObjectName(_fromUtf8("anaEkran"))
        self.gridLayout_6 = QtGui.QGridLayout(self.anaEkran)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(-1, 4, -1, 12)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.welcomeLabel = QtGui.QLabel(self.anaEkran)
        self.welcomeLabel.setMaximumSize(QtCore.QSize(16777215, 276))
        self.welcomeLabel.setStyleSheet(_fromUtf8("border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:2px;\n"
"border-bottom-left-radius:2px;\n"
"color:white;"))
        self.welcomeLabel.setScaledContents(True)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setWordWrap(True)
        self.welcomeLabel.setMargin(15)
        self.welcomeLabel.setIndent(-1)
        self.welcomeLabel.setObjectName(_fromUtf8("welcomeLabel"))
        self.verticalLayout_9.addWidget(self.welcomeLabel)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.urlDevelop = QtGui.QPushButton(self.anaEkran)
        self.urlDevelop.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border-top:1px solid rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-left:1px solid rgba(255, 255, 255, 30);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border-top:1px solid  rgba(255, 255, 255, 40);\n"
"    border-bottom:1px solid rgba(255, 255, 255, 40);\n"
"    border-left:1px solid rgba(255, 255, 255, 40);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-left:1px solid rgba(255, 255, 255, 30);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border-top:1px solid  rgba(255, 255, 255, 15);\n"
"    border-left:1px solid rgba(255, 255, 255, 15);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 15);\n"
"    border-top-left-radius:2px;\n"
"    border-bottom-left-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}"))
        self.urlDevelop.setFlat(True)
        self.urlDevelop.setObjectName(_fromUtf8("urlDevelop"))
        self.horizontalLayout_7.addWidget(self.urlDevelop)
        self.urlPage = QtGui.QPushButton(self.anaEkran)
        self.urlPage.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border-top:1px solid rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-radius:0px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border-top:1px solid rgba(255, 255, 255, 40);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 40);\n"
"    border-radius:0px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border-top:1px solid rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid rgba(255, 255, 255, 30);\n"
"    border-radius:0px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border-top:1px solid  rgba(255, 255, 255, 15);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 15);\n"
"    border-radius:0px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        self.urlPage.setFlat(True)
        self.urlPage.setObjectName(_fromUtf8("urlPage"))
        self.horizontalLayout_7.addWidget(self.urlPage)
        self.urlLicense = QtGui.QPushButton(self.anaEkran)
        self.urlLicense.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 30);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border-top:1px solid  rgba(255, 255, 255, 40);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 40);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 40);\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border-top:1px solid  rgba(255, 255, 255, 30);\n"
"    border-bottom:1px solid  rgba(255, 255, 255, 30);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid rgba(255, 255, 255, 30);\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border-top:1px solid  rgba(255, 255, 255, 15);\n"
"    border-bottom:1px solid rgba(255, 255, 255, 15);\n"
"    border-top-right-radius:2px;\n"
"    border-bottom-right-radius:2px;\n"
"    border-right:1px solid  rgba(255, 255, 255, 15);\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        self.urlLicense.setFlat(True)
        self.urlLicense.setObjectName(_fromUtf8("urlLicense"))
        self.horizontalLayout_7.addWidget(self.urlLicense)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.logoLabel = QtGui.QLabel(self.anaEkran)
        self.logoLabel.setMaximumSize(QtCore.QSize(250, 220))
        self.logoLabel.setStyleSheet(_fromUtf8("border-radius:2px"))
        self.logoLabel.setText(_fromUtf8(""))
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/padi.png")))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        self.horizontalLayout_9.addWidget(self.logoLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.anaEkran)
        self.selectPage = QtGui.QWidget()
        self.selectPage.setObjectName(_fromUtf8("selectPage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.selectPage)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.widget = QtGui.QWidget(self.selectPage)
        self.widget.setStyleSheet(_fromUtf8("#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0));/*22*/\n"
"border-radius:0px;\n"
"}\n"
""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(500, 300))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelScreenshots = QtGui.QLabel(self.widget_2)
        self.labelScreenshots.setMinimumSize(QtCore.QSize(500, 250))
        self.labelScreenshots.setMaximumSize(QtCore.QSize(400, 250))
        self.labelScreenshots.setStyleSheet(_fromUtf8("border:1px solid gray;\n"
"border-radius:4px;"))
        self.labelScreenshots.setText(_fromUtf8(""))
        self.labelScreenshots.setPixmap(QtGui.QPixmap(_fromUtf8(":/screenshots/Screenshots/Gnome.png")))
        self.labelScreenshots.setScaledContents(True)
        self.labelScreenshots.setObjectName(_fromUtf8("labelScreenshots"))
        self.horizontalLayout_3.addWidget(self.labelScreenshots)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.comboBox = QtGui.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(149, 28))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 28))
        self.comboBox.setStyleSheet(_fromUtf8("/* ====================================== */\n"
"\n"
" QComboBox {\n"
"    border:1px solid  rgba(255, 255, 255, 30);\n"
"     border-radius:2px;\n"
"     padding: 1px 18px 1px 3px;\n"
"     min-width: 6em;\n"
"     color: black;\n"
" }\n"
"\n"
" QComboBox:editable {\n"
"     background: gray;\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));*/\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 10));\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"/*    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255));*/\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 10));\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"     border:0px solid  rgba(34, 49, 60, 100);\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"    image: url(:/icons/white-arrow-down.gif);     /*image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);*/\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }"))
        self.comboBox.setIconSize(QtCore.QSize(32, 32))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_18.addWidget(self.comboBox)
        self.xdesktopLabel = QtGui.QLabel(self.widget_2)
        self.xdesktopLabel.setMinimumSize(QtCore.QSize(75, 25))
        self.xdesktopLabel.setMaximumSize(QtCore.QSize(100, 25))
        self.xdesktopLabel.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"border-radius:2px;\n"
"color:rgb(232, 232, 232)"))
        self.xdesktopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xdesktopLabel.setMargin(0)
        self.xdesktopLabel.setObjectName(_fromUtf8("xdesktopLabel"))
        self.horizontalLayout_18.addWidget(self.xdesktopLabel)
        self.getinfoButton = QtGui.QPushButton(self.widget_2)
        self.getinfoButton.setMinimumSize(QtCore.QSize(0, 25))
        self.getinfoButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.getinfoButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    border-radius:2px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(255, 255, 255, 40);\n"
"    border-radius:2px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(255, 255, 255, 30);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(255, 255, 255, 15);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dialog-information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getinfoButton.setIcon(icon3)
        self.getinfoButton.setIconSize(QtCore.QSize(20, 20))
        self.getinfoButton.setFlat(True)
        self.getinfoButton.setObjectName(_fromUtf8("getinfoButton"))
        self.horizontalLayout_18.addWidget(self.getinfoButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_18, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.selectPage)
        self.downloadPage = QtGui.QWidget()
        self.downloadPage.setObjectName(_fromUtf8("downloadPage"))
        self.gridLayout_8 = QtGui.QGridLayout(self.downloadPage)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.addPackLabel = QtGui.QLabel(self.downloadPage)
        self.addPackLabel.setMinimumSize(QtCore.QSize(300, 60))
        self.addPackLabel.setMaximumSize(QtCore.QSize(800, 40))
        self.addPackLabel.setStyleSheet(_fromUtf8("border-radius:2px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 15))"))
        self.addPackLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addPackLabel.setWordWrap(True)
        self.addPackLabel.setMargin(4)
        self.addPackLabel.setIndent(0)
        self.addPackLabel.setObjectName(_fromUtf8("addPackLabel"))
        self.horizontalLayout_11.addWidget(self.addPackLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.desktopLogoLabel = QtGui.QLabel(self.downloadPage)
        self.desktopLogoLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.desktopLogoLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.desktopLogoLabel.setStyleSheet(_fromUtf8("padding: 5px 5px 5px 5px; \n"
"border-radius:2px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 15));\n"
"border:1px solid rgba(255, 255, 255, 15);\n"
"\n"
""))
        self.desktopLogoLabel.setText(_fromUtf8(""))
        self.desktopLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo/Logo/Gnome.png")))
        self.desktopLogoLabel.setScaledContents(True)
        self.desktopLogoLabel.setObjectName(_fromUtf8("desktopLogoLabel"))
        self.horizontalLayout_8.addWidget(self.desktopLogoLabel)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.downloadButton = QtGui.QPushButton(self.downloadPage)
        self.downloadButton.setMinimumSize(QtCore.QSize(125, 25))
        self.downloadButton.setMaximumSize(QtCore.QSize(125, 25))
        self.downloadButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    border-radius:2px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(255, 255, 255, 40);\n"
"    border-radius:2px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(255, 255, 255, 30);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(255, 255, 255, 15);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon4)
        self.downloadButton.setIconSize(QtCore.QSize(20, 20))
        self.downloadButton.setFlat(True)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout_10.addWidget(self.downloadButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addLayout(self.verticalLayout_11)
        self.gridLayout_8.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.downloadPage)
        self.moreInfo = QtGui.QWidget()
        self.moreInfo.setObjectName(_fromUtf8("moreInfo"))
        self.gridLayout_2 = QtGui.QGridLayout(self.moreInfo)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.infoTextBrowser = QtGui.QTextBrowser(self.moreInfo)
        self.infoTextBrowser.setMinimumSize(QtCore.QSize(600, 0))
        self.infoTextBrowser.setStyleSheet(_fromUtf8(""))
        self.infoTextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.infoTextBrowser.setLineWidth(0)
        self.infoTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infoTextBrowser.setDocumentTitle(_fromUtf8(""))
        self.infoTextBrowser.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.infoTextBrowser.setOverwriteMode(False)
        self.infoTextBrowser.setOpenExternalLinks(True)
        self.infoTextBrowser.setObjectName(_fromUtf8("infoTextBrowser"))
        self.gridLayout_2.addWidget(self.infoTextBrowser, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.moreInfo)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.mainStack)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.labelAlt = QtGui.QLabel(self.padiContainer)
        self.labelAlt.setMinimumSize(QtCore.QSize(0, 35))
        self.labelAlt.setMaximumSize(QtCore.QSize(1000, 35))
        self.labelAlt.setStyleSheet(_fromUtf8("border-radius:1px;\n"
"color:rgb(232, 232, 232);\n"
"background-color: rgba(0, 0, 0, 70);"))
        self.labelAlt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlt.setWordWrap(False)
        self.labelAlt.setMargin(5)
        self.labelAlt.setObjectName(_fromUtf8("labelAlt"))
        self.horizontalLayout_17.addWidget(self.labelAlt)
        self.animasyon = QtGui.QLabel(self.padiContainer)
        self.animasyon.setMinimumSize(QtCore.QSize(0, 35))
        self.animasyon.setMaximumSize(QtCore.QSize(16777215, 35))
        self.animasyon.setStyleSheet(_fromUtf8("border-radius:1px;\n"
"color:rgb(232, 232, 232);\n"
"background-color: rgba(0, 0, 0, 70);"))
        self.animasyon.setText(_fromUtf8(""))
        self.animasyon.setMargin(5)
        self.animasyon.setObjectName(_fromUtf8("animasyon"))
        self.horizontalLayout_17.addWidget(self.animasyon)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.groupBox = QtGui.QGroupBox(self.padiContainer)
        self.groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 33))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox.setBaseSize(QtCore.QSize(40, 40))
        self.groupBox.setAcceptDrops(True)
        self.groupBox.setStyleSheet(_fromUtf8("#groupBox{\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 40), stop:0.510753 rgba(9, 9, 9, 70), stop:1 rgba(0, 0, 0, 40));\n"
"    border-top: 1px solid rgba(255, 255, 255, 100)/*white*/\n"
"}\n"
"\n"
"/*background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 70), stop:0.510753 rgba(9, 9, 9, 125), stop:1 rgba(0, 0, 0, 70));*/\n"
"\n"
"QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(255, 255, 255, 40);\n"
"    border-radius:2px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(127, 127, 127, 10), stop:0.513661 rgba(231, 231, 231, 50), stop:1 rgba(94, 94, 94, 10))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(255, 255, 255, 30);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(27, 27, 27, 0), stop:0.510753 rgba(9, 9, 9, 10), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(255, 255, 255, 15);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 52, 52, 50));\n"
"}\n"
""))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_13.setContentsMargins(10, 0, 5, 0)
        self.gridLayout_13.setHorizontalSpacing(5)
        self.gridLayout_13.setVerticalSpacing(0)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.buttonGeri2 = QtGui.QPushButton(self.groupBox)
        self.buttonGeri2.setMinimumSize(QtCore.QSize(70, 23))
        self.buttonGeri2.setMaximumSize(QtCore.QSize(200, 23))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Arrow_Left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonGeri2.setIcon(icon5)
        self.buttonGeri2.setIconSize(QtCore.QSize(16, 16))
        self.buttonGeri2.setFlat(True)
        self.buttonGeri2.setObjectName(_fromUtf8("buttonGeri2"))
        self.gridLayout_13.addWidget(self.buttonGeri2, 0, 4, 1, 1)
        self.buttonGeri = QtGui.QPushButton(self.groupBox)
        self.buttonGeri.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonGeri.setMaximumSize(QtCore.QSize(16777215, 23))
        self.buttonGeri.setIcon(icon5)
        self.buttonGeri.setIconSize(QtCore.QSize(16, 16))
        self.buttonGeri.setFlat(True)
        self.buttonGeri.setObjectName(_fromUtf8("buttonGeri"))
        self.gridLayout_13.addWidget(self.buttonGeri, 0, 2, 1, 1)
        self.buttonIptal = QtGui.QPushButton(self.groupBox)
        self.buttonIptal.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonIptal.setMaximumSize(QtCore.QSize(16777215, 23))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Error.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIptal.setIcon(icon6)
        self.buttonIptal.setIconSize(QtCore.QSize(16, 16))
        self.buttonIptal.setFlat(True)
        self.buttonIptal.setObjectName(_fromUtf8("buttonIptal"))
        self.gridLayout_13.addWidget(self.buttonIptal, 0, 0, 1, 1)
        self.buttonIleri = QtGui.QPushButton(self.groupBox)
        self.buttonIleri.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonIleri.setMaximumSize(QtCore.QSize(16777215, 23))
        self.buttonIleri.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Arrow_Right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIleri.setIcon(icon7)
        self.buttonIleri.setIconSize(QtCore.QSize(16, 16))
        self.buttonIleri.setCheckable(False)
        self.buttonIleri.setAutoRepeat(False)
        self.buttonIleri.setAutoExclusive(False)
        self.buttonIleri.setAutoDefault(False)
        self.buttonIleri.setDefault(False)
        self.buttonIleri.setFlat(True)
        self.buttonIleri.setObjectName(_fromUtf8("buttonIleri"))
        self.gridLayout_13.addWidget(self.buttonIleri, 0, 3, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem13, 0, 1, 1, 1)
        self.buttonSon = QtGui.QPushButton(self.groupBox)
        self.buttonSon.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonSon.setMaximumSize(QtCore.QSize(16777215, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSon.setIcon(icon8)
        self.buttonSon.setIconSize(QtCore.QSize(16, 16))
        self.buttonSon.setCheckable(False)
        self.buttonSon.setAutoRepeat(False)
        self.buttonSon.setAutoExclusive(False)
        self.buttonSon.setAutoDefault(False)
        self.buttonSon.setDefault(False)
        self.buttonSon.setFlat(True)
        self.buttonSon.setObjectName(_fromUtf8("buttonSon"))
        self.gridLayout_13.addWidget(self.buttonSon, 0, 5, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem14 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_12.addWidget(self.padiContainer)
        self.gridLayout_10.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        padi.setCentralWidget(self.padiCentral)

        self.retranslateUi(padi)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonTamEkran, QtCore.SIGNAL(_fromUtf8("clicked()")), padi.showFullScreen)
        QtCore.QObject.connect(self.buttonTamEkrandanCik, QtCore.SIGNAL(_fromUtf8("clicked()")), padi.showNormal)
        QtCore.QMetaObject.connectSlotsByName(padi)

    def retranslateUi(self, padi):
        padi.setWindowTitle(QtGui.QApplication.translate("padi", "Padi", None, QtGui.QApplication.UnicodeUTF8))
        self.screenLabel.setText(QtGui.QApplication.translate("padi", "Padi\'ye Hoş Geldiniz", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("padi", "Masaüstünüzü değiştirin", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTamEkran.setToolTip(QtGui.QApplication.translate("padi", "Full screen", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTamEkrandanCik.setToolTip(QtGui.QApplication.translate("padi", "Exit full screen", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeLabel.setText(QtGui.QApplication.translate("padi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:16pt;\">Hoş Geldiniz!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">Padi ile yeni masaüstü ortamları ile tanışabilir, Linux deneyimlerinizi farklı masaüstü ortamlarında yaşayabilirsiniz.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.urlDevelop.setText(QtGui.QApplication.translate("padi", "Geliştiriciler", None, QtGui.QApplication.UnicodeUTF8))
        self.urlPage.setText(QtGui.QApplication.translate("padi", "Proje Sayfası", None, QtGui.QApplication.UnicodeUTF8))
        self.urlLicense.setText(QtGui.QApplication.translate("padi", "Lisans", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("padi", "Seç", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("padi", "Kde", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("padi", "Gnome", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("padi", "Xfce", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("padi", "Lxde", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("padi", "Mate", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("padi", "Cinnamon", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("padi", "Fluxbox", None, QtGui.QApplication.UnicodeUTF8))
        self.xdesktopLabel.setText(QtGui.QApplication.translate("padi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.getinfoButton.setToolTip(QtGui.QApplication.translate("padi", "internet", None, QtGui.QApplication.UnicodeUTF8))
        self.getinfoButton.setText(QtGui.QApplication.translate("padi", "Daha Fazla Bilgi", None, QtGui.QApplication.UnicodeUTF8))
        self.addPackLabel.setText(QtGui.QApplication.translate("padi", "<html><head/><body><p><span style=\" font-weight:600;\">Masaüstü ortamının bilgisayarınız kurulmaya başlaması için yükle düğmesine bir kez basınız ve bekleyiniz. Bu işlem bilgisayarınızın ve internetinizin hızına bağlı olarak 5 ile 10 dakika arasındadır</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("padi", "Yükle", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setShortcut(QtGui.QApplication.translate("padi", "Ctrl+R, Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTextBrowser.setHtml(QtGui.QApplication.translate("padi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/desktops/Desktops/razor-qt.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Enlightenment is the flagship and original name bearer for this project. Once it was just a humble window manager for X11 that wanted to do things differently. To do them better, but it has expanded. This can be confusing so when we refer to Enlightenment, we may mean the project as a whole or just the window manager proper. The libraries behind Enlightenment are referred to as EFL collectively, each with a specific name and purpose.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">The window manager is a lean, fast, modular and very extensible window manager for X11 and Linux. It is classed as a &quot;desktop shell&quot; providing the things you need to operate your desktop (or laptop), but is not a whole application suite. This covered launching applications, managing their windows and doing other system tasks like suspending, reboots, managing files etc.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAlt.setText(QtGui.QApplication.translate("padi", "Yeni masaüstü hazır !", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonGeri2.setText(QtGui.QApplication.translate("padi", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonGeri.setText(QtGui.QApplication.translate("padi", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIptal.setToolTip(QtGui.QApplication.translate("padi", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIptal.setText(QtGui.QApplication.translate("padi", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIleri.setText(QtGui.QApplication.translate("padi", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSon.setText(QtGui.QApplication.translate("padi", "Son", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
