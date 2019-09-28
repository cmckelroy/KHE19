import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from include import password, account, data
from collections import Counter
from gui import *

"""Modes
0 - Not defined yet
1 - Password
2 - Account
3 - File
"""

def single_pass(pswd):
    outputstr = ""
    passwd = password.Password(pswd)
    if passwd.is_pwned():
        outputstr += f"This password is known to be breached. It has been seen {passwd.pwned_count()} times\n"
    if passwd.score() == 0:
        outputstr += "This password is very weak\n"
    elif passwd.score() == 1:
        outputstr += "This password is weak\n"
    elif passwd.score() == 2:
        outputstr += "This password is mild\n"
    elif passwd.score() == 3:
        outputstr += "This password is strong\n"
    elif passwd.score() == 4:
        outputstr += "This password is very strong\n"
    suggestions = passwd.suggestions()
    warnings = passwd.warnings()
    
    if warnings != "":
        outputstr += f"\nPassword Warning: {warnings}\n"        
    if len(suggestions) > 0:
        outputstr += f"\nPassword suggestions:\n\n"
        for suggestion in suggestions:
            outputstr += f"{suggestion}\n"
    return outputstr
    

def single_account(acc):
    outputstr = ""
    acct = account.Account(acc)
    try:
        breachCount = len(acct.breaches)
        if breachCount > 0 and breachCount < 5:
            outputstr += f"This account has been seen in {breachCount} breaches\n"
        else:
            outputstr += f"This account has been seen in {breachCount} breaches\n"
    except TypeError:
        output += "This account has not been seen in any breaches\n"
    finally:
        return outputstr

def file_check(fp):
    outputstr = ""
    (acclist, passlist) = data.load_from_plainfile(fp)
    for account in acclist:
        outputstr += f"Account Username: {account}\n"
        outputstr += "-------------------------------------------------------\n\n"
        outputstr += single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        outputstr += f"Password: {pwdCheck}\n"
        outputstr += "-------------------------------------------------------\n\n"
        if pwddupes[pwdCheck] > 1:
            outputstr += "You appear to be using this password {pwddupes[pwdCheck]} times!\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

class MyForm(QMainWindow):
    def __init__(self):
        self.procmode = 0
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Password Checker')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui.mainRun.clicked.connect(self.dispmessage)
        self.ui.mode_radio_pass.toggled.connect(self.displaymode)
        self.ui.mode_radio_acct.toggled.connect(self.displaymode)
        self.ui.mode_radio_file.toggled.connect(self.displaymode)
        self.ui.Quit.clicked.connect(self.close)
        self.show()

    def displaymode(self):
        if self.ui.mode_radio_pass.isChecked():
            self.procmode = 1
            self.ui.mainInputLabel.setText("Enter password:")
        if self.ui.mode_radio_acct.isChecked():
            self.procmode = 2
            self.ui.mainInputLabel.setText("Enter username:")
        if self.ui.mode_radio_file.isChecked():
            self.procmode = 3
            self.ui.mainInputLabel.setText("Enter file path:")
   		
    def dispmessage(self):
        if self.procmode == 1:
            pswd = str(self.ui.mainInputBox.text())
            self.ui.outputBox.setText(single_pass(pswd))
        if self.procmode == 2:
            acct = str(self.ui.mainInputBox.text())
            self.ui.outputBox.setText(single_account(acct))
        if self.procmode == 3:
            file = str(self.ui.mainInputBox.text())
            self.ui.outputBox.setText(file_check(file))
  

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())