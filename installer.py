# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer.ui'
#
# Created: Wed Apr 19 23:26:12 2017
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_InstallerWidget(object):
    def setupUi(self, InstallerWidget):
        InstallerWidget.setObjectName(_fromUtf8("InstallerWidget"))
        InstallerWidget.resize(400, 300)
        self.stackedWidget = QtGui.QStackedWidget(InstallerWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.pushButton_Cancel1 = QtGui.QPushButton(self.page1)
        self.pushButton_Cancel1.setGeometry(QtCore.QRect(190, 250, 95, 31))
        self.pushButton_Cancel1.setObjectName(_fromUtf8("pushButton_Cancel1"))
        self.pushButton_Next1 = QtGui.QPushButton(self.page1)
        self.pushButton_Next1.setGeometry(QtCore.QRect(300, 250, 95, 31))
        self.pushButton_Next1.setObjectName(_fromUtf8("pushButton_Next1"))
        self.textBrowser_Page1 = QtGui.QTextBrowser(self.page1)
        self.textBrowser_Page1.setGeometry(QtCore.QRect(0, 0, 401, 241))
        self.textBrowser_Page1.setObjectName(_fromUtf8("textBrowser_Page1"))
        self.stackedWidget.addWidget(self.page1)
        self.page2_2 = QtGui.QWidget()
        self.page2_2.setObjectName(_fromUtf8("page2_2"))
        self.progressBar = QtGui.QProgressBar(self.page2_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 220, 371, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_Back1 = QtGui.QPushButton(self.page2_2)
        self.pushButton_Back1.setGeometry(QtCore.QRect(190, 260, 95, 31))
        self.pushButton_Back1.setObjectName(_fromUtf8("pushButton_Back1"))
        self.pushButton_Finish2_2 = QtGui.QPushButton(self.page2_2)
        self.pushButton_Finish2_2.setGeometry(QtCore.QRect(300, 260, 95, 31))
        self.pushButton_Finish2_2.setObjectName(_fromUtf8("pushButton_Finish2_2"))
        self.textBrowser_Page2_Status = QtGui.QTextBrowser(self.page2_2)
        self.textBrowser_Page2_Status.setGeometry(QtCore.QRect(20, 70, 351, 111))
        self.textBrowser_Page2_Status.setObjectName(_fromUtf8("textBrowser_Page2_Status"))
        self.label_Page2_3 = QtGui.QLabel(self.page2_2)
        self.label_Page2_3.setGeometry(QtCore.QRect(20, 200, 64, 21))
        self.label_Page2_3.setObjectName(_fromUtf8("label_Page2_3"))
        self.label_Page2_2 = QtGui.QLabel(self.page2_2)
        self.label_Page2_2.setGeometry(QtCore.QRect(10, 50, 121, 21))
        self.label_Page2_2.setObjectName(_fromUtf8("label_Page2_2"))
        self.label_Page_1 = QtGui.QLabel(self.page2_2)
        self.label_Page_1.setGeometry(QtCore.QRect(50, 20, 211, 21))
        self.label_Page_1.setObjectName(_fromUtf8("label_Page_1"))
        self.stackedWidget.addWidget(self.page2_2)
        self.page3 = QtGui.QWidget()
        self.page3.setObjectName(_fromUtf8("page3"))
        self.pushButton_Finish2 = QtGui.QPushButton(self.page3)
        self.pushButton_Finish2.setGeometry(QtCore.QRect(290, 250, 95, 31))
        self.pushButton_Finish2.setObjectName(_fromUtf8("pushButton_Finish2"))
        self.textBrowser_Finish = QtGui.QTextBrowser(self.page3)
        self.textBrowser_Finish.setGeometry(QtCore.QRect(20, 30, 331, 201))
        self.textBrowser_Finish.setObjectName(_fromUtf8("textBrowser_Finish"))
        self.stackedWidget.addWidget(self.page3)

        self.retranslateUi(InstallerWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InstallerWidget)

    def retranslateUi(self, InstallerWidget):
        InstallerWidget.setWindowTitle(_translate("InstallerWidget", "Form", None))
        self.pushButton_Cancel1.setText(_translate("InstallerWidget", "Cancel", None))
        self.pushButton_Next1.setText(_translate("InstallerWidget", "Next", None))
        self.textBrowser_Page1.setHtml(_translate("InstallerWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to Adobe Flash Setup</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Pro Setup Wizard</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This will install Adobe Flash Version 7.0.1 on your computer.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">It is recommended that you close all other applications before continuing.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click Next to continue, or Cancel to exit Setup.</span></p></body></html>", None))
        self.pushButton_Back1.setText(_translate("InstallerWidget", "Back", None))
        self.pushButton_Finish2_2.setText(_translate("InstallerWidget", "Finish", None))
        self.label_Page2_3.setText(_translate("InstallerWidget", "Installing:", None))
        self.label_Page2_2.setText(_translate("InstallerWidget", "Installation status:", None))
        self.label_Page_1.setText(_translate("InstallerWidget", "The Updates are being installed", None))
        self.pushButton_Finish2.setText(_translate("InstallerWidget", "Finish", None))
        self.textBrowser_Finish.setHtml(_translate("InstallerWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Pro Wizard Setup Complete</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The Pro Wizard has sucessfully installed the update.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click Finish to exit the wizard.</span></p></body></html>", None))

