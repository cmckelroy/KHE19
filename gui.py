# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.mainInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainInputLabel.setGeometry(QtCore.QRect(30, 10, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mainInputLabel.setFont(font)
        self.mainInputLabel.setObjectName("mainInputLabel")
        self.mode_group = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_group.setGeometry(QtCore.QRect(30, 260, 341, 261))
        self.mode_group.setObjectName("mode_group")
        self.mode_radio_pass = QtWidgets.QRadioButton(self.mode_group)
        self.mode_radio_pass.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.mode_radio_pass.setObjectName("mode_radio_pass")
        self.mode_radio_acct = QtWidgets.QRadioButton(self.mode_group)
        self.mode_radio_acct.setGeometry(QtCore.QRect(20, 130, 181, 20))
        self.mode_radio_acct.setObjectName("mode_radio_acct")
        self.mode_radio_file = QtWidgets.QRadioButton(self.mode_group)
        self.mode_radio_file.setGeometry(QtCore.QRect(20, 220, 181, 20))
        self.mode_radio_file.setObjectName("mode_radio_file")
        self.mainRun = QtWidgets.QPushButton(self.centralwidget)
        self.mainRun.setGeometry(QtCore.QRect(450, 490, 93, 28))
        self.mainRun.setObjectName("mainRun")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(610, 490, 93, 28))
        self.Quit.setObjectName("Quit")
        self.outputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.outputBox.setEnabled(True)
        self.outputBox.setGeometry(QtCore.QRect(390, 290, 371, 181))
        self.outputBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.outputBox.setAcceptDrops(False)
        self.outputBox.setReadOnly(True)
        self.outputBox.setObjectName("outputBox")
        self.outputboxLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputboxLabel.setGeometry(QtCore.QRect(390, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.outputboxLabel.setFont(font)
        self.outputboxLabel.setObjectName("outputboxLabel")
        self.mainInputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.mainInputBox.setGeometry(QtCore.QRect(30, 40, 721, 211))
        self.mainInputBox.setObjectName("mainInputBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainInputLabel.setText(_translate("MainWindow", "Input:"))
        self.mode_group.setTitle(_translate("MainWindow", "Mode"))
        self.mode_radio_pass.setText(_translate("MainWindow", "Single Password Check"))
        self.mode_radio_acct.setText(_translate("MainWindow", "Single Account Check"))
        self.mode_radio_file.setText(_translate("MainWindow", "File Check"))
        self.mainRun.setText(_translate("MainWindow", "Run"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.outputboxLabel.setText(_translate("MainWindow", "Output:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())