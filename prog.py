import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from include import password, account, data, browserpass, wifi
from collections import Counter
from gui import *
from sqlite3 import OperationalError

"""Modes
0 - Not defined yet
1 - Password
2 - Account
3 - File
4 - browser
5 - WiFi
"""

def single_pass(pswd):
    outputstr = ""
    passwd = password.Password(pswd)
    if passwd.is_pwned():
        if passwd.pwned_count() == 1:
            outputstr += f"This password is known to be breached. It has been seen {passwd.pwned_count()} time\n"
        else:
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
    except TypeError:
        outputstr += "This account has not been seen in any breaches\n"
    finally:
        return outputstr

def file_check(fp):
    outputstr = ""
    (acclist, passlist) = data.load_from_plainfile(fp)
    for account in acclist:
        outputstr += f"\n\nAccount Username: {account}\n"
        outputstr += "------------------------------------------------\n\n"
        outputstr += single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        outputstr += f"\n\nPassword: {pwdCheck}\n"
        outputstr += "-----------------------------------------------\n\n"
        if pwddupes[pwdCheck] > 1:
            outputstr += f"You appear to be using this password {pwddupes[pwdCheck]} times!\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

def chrome_check(acclist, passlist):
    outputstr = ""
    for account in acclist:
        outputstr += f"Account Username: {account}\n"
        outputstr += "------------------------------------------------\n\n"
        outputstr += single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        outputstr += f"Password: {pwdCheck}\n"
        outputstr += "------------------------------------------------\n\n"
        if pwddupes[pwdCheck] > 1:
            outputstr += "You appear to be using this password {pwddupes[pwdCheck]} times!\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

def wifi_check(passlist):
    outputstr = ""
    for pwdCheck in passlist:
        outputstr += f"Password: {pwdCheck}\n"
        outputstr += "------------------------------------------------\n\n"
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
        self.ui.mode_chrome_check.toggled.connect(self.displaymode)
        self.ui.mode_wifi_check.toggled.connect(self.displaymode)
        self.ui.choose_file.clicked.connect(self.onInputFileButtonClicked)
        self.ui.choose_file.setEnabled(False)
        self.ui.Quit.clicked.connect(self.close)
        self.show()
        
    def onInputFileButtonClicked(self):
        (self.fname, self.ftype) = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Text files (*.txt)")
    
    def displaymode(self):
        if self.ui.mode_radio_pass.isChecked():
            self.procmode = 1
            self.ui.mainInputLabel.setText("Enter password:")
            self.ui.mainInputBox.setReadOnly(False)
            self.ui.mainInputBox.setText("")
        elif self.ui.mode_radio_acct.isChecked():
            self.procmode = 2
            self.ui.mainInputLabel.setText("Enter username:")
            self.ui.mainInputBox.setReadOnly(False)
            self.ui.mainInputBox.setText("")
        elif self.ui.mode_radio_file.isChecked():
            self.ui.choose_file.setEnabled(True)
            self.procmode = 3
            self.ui.mainInputLabel.setText("Enter file path:")
            self.ui.mainInputBox.setReadOnly(True)
            self.ui.mainInputBox.setText("Not used for this mode")
        elif self.ui.mode_chrome_check.isChecked():
            self.procmode = 4
            self.ui.mainInputBox.setText("Not used for this mode")
            self.ui.mainInputBox.setReadOnly(True)
        elif self.ui.mode_wifi_check.isChecked():
            self.procmode = 5
            self.ui.mainInputBox.setText("Not used for this mode")
            self.ui.mainInputBox.setReadOnly(False)
   		
    def dispmessage(self):
        if self.procmode == 1:
            self.ui.mainRun.setEnabled(False)
            pswd = str(self.ui.mainInputBox.text())
            self.ui.outputBox.setText(single_pass(pswd))
            self.ui.mainRun.setEnabled(True)
        elif self.procmode == 2:
            self.ui.mainRun.setEnabled(False)
            acct = str(self.ui.mainInputBox.text())
            try:
                self.ui.outputBox.setText(single_account(acct))
            except KeyError:
                QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
            finally:
                self.ui.mainRun.setEnabled(True)
        elif self.procmode == 3:
            self.ui.mainRun.setEnabled(False)
            file = str(self.fname)
            try:
                self.ui.outputBox.setText(file_check(file))
            except KeyError:
                QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
            except data.FileLoadError:
                QMessageBox.about(self, "Unknown File", "That file either doesn't exist, or it cannot be accessed")
            finally:
                self.ui.mainRun.setEnabled(True)
        elif self.procmode == 4:
            self.ui.mainRun.setEnabled(False)
            try:
                QMessageBox.about(self, "Close Chrome", "Please close Chrome before running this.")
                (acclist, passlist) = browserpass.retrieve_chrome()
                if acclist is not None or passlist is not None:
                    self.ui.outputBox.setText(chrome_check(acclist, passlist))
                else:
                    QMessageBox.about(self, "Cannot find Chrome", "Cannot read the database. Is Chrome installed?")
            except KeyError:
                QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
            except OperationalError:
                QMessageBox.about(self, "Database locked", "Cannot read the database. Is Chrome open?")
            finally:
                self.ui.mainRun.setEnabled(True)
        elif self.procmode == 5:
            self.ui.mainRun.setEnabled(False)
            passlist = wifi.retrive_all()
            if passlist is not None:
                self.ui.outputBox.setText(wifi_check(passlist))
            else:
                self.ui.outputBox.setText("No WiFi Passwords Found")
            self.ui.mainRun.setEnabled(True)
    
  

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())