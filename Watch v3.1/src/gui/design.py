# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(551, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addBtn = QtGui.QToolButton(self.centralwidget)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setMouseTracking(False)
        self.addBtn.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.addBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon1)
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.gridLayout.addWidget(self.addBtn, 0, 5, 1, 1)
        self.reloadBtn = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reloadBtn.sizePolicy().hasHeightForWidth())
        self.reloadBtn.setSizePolicy(sizePolicy)
        self.reloadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reloadBtn.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.reloadBtn.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../reload.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadBtn.setIcon(icon2)
        self.reloadBtn.setObjectName(_fromUtf8("reloadBtn"))
        self.gridLayout.addWidget(self.reloadBtn, 0, 8, 1, 1)
        self.userInput = QtGui.QLineEdit(self.centralwidget)
        self.userInput.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.userInput.setObjectName(_fromUtf8("userInput"))
        self.gridLayout.addWidget(self.userInput, 0, 2, 1, 1)
        self.removeBtn = QtGui.QToolButton(self.centralwidget)
        self.removeBtn.setText(_fromUtf8(""))
        self.removeBtn.setObjectName(_fromUtf8("removeBtn"))
        self.gridLayout.addWidget(self.removeBtn, 0, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.serieList = QtGui.QListWidget(self.centralwidget)
        self.serieList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.serieList.setObjectName(_fromUtf8("serieList"))
        self.verticalLayout.addWidget(self.serieList)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.logBrowser = QtGui.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logBrowser.setFont(font)
        self.logBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.logBrowser.setAcceptDrops(False)
        self.logBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logBrowser.setAutoFillBackground(False)
        self.logBrowser.setFrameShadow(QtGui.QFrame.Sunken)
        self.logBrowser.setAutoFormatting(QtGui.QTextEdit.AutoNone)
        self.logBrowser.setOpenExternalLinks(True)
        self.logBrowser.setObjectName(_fromUtf8("logBrowser"))
        self.verticalLayout.addWidget(self.logBrowser)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.watchBtn = QtGui.QPushButton(self.centralwidget)
        self.watchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.watchBtn.setAutoDefault(True)
        self.watchBtn.setDefault(True)
        self.watchBtn.setFlat(False)
        self.watchBtn.setObjectName(_fromUtf8("watchBtn"))
        self.verticalLayout.addWidget(self.watchBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Watch v3 - bs.to Manager", None))
        self.addBtn.setToolTip(_translate("MainWindow", "Add", None))
        self.reloadBtn.setToolTip(_translate("MainWindow", "Reload files", None))
        self.userInput.setPlaceholderText(_translate("MainWindow", "Enter a serie here", None))
        self.serieList.setToolTip(_translate("MainWindow", "Click on any serie and press \'Watch\'", None))
        self.serieList.setWhatsThis(_translate("MainWindow", "Here you can find your saved series", None))
        self.logBrowser.setToolTip(_translate("MainWindow", "log", None))
        self.watchBtn.setText(_translate("MainWindow", "Watch", None))

