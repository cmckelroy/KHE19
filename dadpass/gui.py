# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver1.ui'
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
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Top = QtWidgets.QGraphicsView(self.centralwidget)
        self.Top.setGeometry(QtCore.QRect(0, -30, 1921, 151))
        self.Top.setStyleSheet("background-color: rgb(0, 196, 180);")
        self.Top.setObjectName("Top")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(300, 20, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPixelSize(91)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color:rgb(0, 196, 180);\n"
"color: white;")
        self.Title.setObjectName("Title")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(50, 10, 211, 105))
        self.Logo.setStyleSheet("background-color: rgb(0, 196, 180);")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("assets\logo.png"))
        self.Logo.setObjectName("Logo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 120, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(300, 120, 801, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 390, 191, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.usernameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.usernameEdit.setGeometry(QtCore.QRect(20, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.usernameEdit.setFont(font)
        self.usernameEdit.setStyleSheet("background-color: rgb(236, 236, 236)")
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setGeometry(QtCore.QRect(20, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.passwordEdit.setFont(font)
        self.passwordEdit.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.passwordEdit.setObjectName("passwordEdit")
        self.acclabel = QtWidgets.QLabel(self.groupBox)
        self.acclabel.setGeometry(QtCore.QRect(20, 20, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.acclabel.setFont(font)
        self.acclabel.setObjectName("acclabel")
        self.Subtitle = QtWidgets.QLabel(self.centralwidget)
        self.Subtitle.setGeometry(QtCore.QRect(60, 140, 680, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Subtitle.setFont(font)
        self.Subtitle.setObjectName("Subtitle")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 180, 191, 201))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.instructions = QtWidgets.QLabel(self.groupBox_2)
        self.instructions.setGeometry(QtCore.QRect(10, 10, 171, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.instructions.setFont(font)
        self.instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.instructions.setWordWrap(True)
        self.instructions.setObjectName("instructions")
        self.Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(240, 470, 301, 71))
        self.Input.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.Input.setReadOnly(True)
        self.Input.setObjectName("Input")
        self.Output = QtWidgets.QTextEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(563, 200, 211, 311))
        self.Output.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.Output.setObjectName("Output")
        self.inputDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputDisplayLabel.setGeometry(QtCore.QRect(240, 440, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.inputDisplayLabel.setFont(font)
        self.inputDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputDisplayLabel.setObjectName("inputDisplayLabel")
        self.outputDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputDisplayLabel.setGeometry(QtCore.QRect(570, 170, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.outputDisplayLabel.setFont(font)
        self.outputDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputDisplayLabel.setObjectName("outputDisplayLabel")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(563, 520, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.run.setFont(font)
        self.run.setAutoFillBackground(False)
        self.run.setStyleSheet("background-color: rgb(156, 116, 236);\n"
"color: white;\n"
"font-weight: bold;")
        self.run.setAutoDefault(False)
        self.run.setDefault(False)
        self.run.setFlat(False)
        self.run.setObjectName("run")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 170, 301, 221))
        self.groupBox_3.setObjectName("groupBox_3")
        self.passCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.passCheck.setGeometry(QtCore.QRect(20, 40, 131, 16))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.passCheck.setFont(font)
        self.passCheck.setObjectName("passCheck")
        self.usernameCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.usernameCheck.setGeometry(QtCore.QRect(150, 40, 141, 16))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.usernameCheck.setFont(font)
        self.usernameCheck.setObjectName("usernameCheck")
        self.browserCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.browserCheck.setGeometry(QtCore.QRect(20, 80, 121, 16))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.browserCheck.setFont(font)
        self.browserCheck.setObjectName("browserCheck")
        self.wifiCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.wifiCheck.setGeometry(QtCore.QRect(150, 80, 121, 16))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.wifiCheck.setFont(font)
        self.wifiCheck.setObjectName("wifiCheck")
        self.fileChoose = QtWidgets.QToolButton(self.groupBox_3)
        self.fileChoose.setGeometry(QtCore.QRect(230, 120, 21, 20))
        self.fileChoose.setObjectName("fileChoose")
        self.fileLabel = QtWidgets.QLabel(self.groupBox_3)
        self.fileLabel.setGeometry(QtCore.QRect(150, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(10)
        self.fileLabel.setFont(font)
        self.fileLabel.setObjectName("fileLabel")
        self.fp_output = QtWidgets.QLineEdit(self.groupBox_3)
        self.fp_output.setGeometry(QtCore.QRect(40, 170, 211, 21))
        self.fp_output.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.fp_output.setReadOnly(True)
        self.fp_output.setObjectName("fp_output")
        self.fileCheck = QtWidgets.QRadioButton(self.groupBox_3)
        self.fileCheck.setGeometry(QtCore.QRect(20, 120, 69, 16))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.fileCheck.setFont(font)
        self.fileCheck.setObjectName("fileCheck")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.Title.setText(_translate("MainWindow", "Dad Pass"))
        self.usernameEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.acclabel.setText(_translate("MainWindow", "Account"))
        self.Subtitle.setText(_translate("MainWindow", "Password and Username Security Analysis for Your At-Home Needs"))
        self.instructions.setText(_translate("MainWindow", "1. Select a mode\n"
"2. Enter details or pick a file (if needed)\n"
"3. Click run\n"
"4. See the results!"))
        self.inputDisplayLabel.setText(_translate("MainWindow", "Your last input:"))
        self.outputDisplayLabel.setText(_translate("MainWindow", "Output"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mode"))
        self.passCheck.setText(_translate("MainWindow", "Single Password check"))
        self.usernameCheck.setText(_translate("MainWindow", "Single Username check"))
        self.browserCheck.setText(_translate("MainWindow", "Browser Check"))
        self.wifiCheck.setText(_translate("MainWindow", "Wifi Pass Check"))
        self.fileChoose.setText(_translate("MainWindow", "..."))
        self.fileLabel.setText(_translate("MainWindow", "Choose File"))
        self.fp_output.setPlaceholderText(_translate("MainWindow", "File Path"))
        self.fileCheck.setText(_translate("MainWindow", "File Check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())