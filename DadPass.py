import sys
import os
import psutil

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from dadpass import password, account, data, browserpass, wifi
from collections import Counter
from dadpass.gui import *
from sqlite3 import OperationalError

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

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
        else:
            outputstr += "This account has not been seen in any breaches\n"
    except TypeError:
        outputstr += "This account has not been seen in any breaches\n"
    finally:
        return outputstr

def file_check(fp):
    outputstr = ""
    (acclist, passlist) = data.load_from_plainfile(fp)
    for account in acclist:
        outputstr += f"\n\nAccount Username: {account}\n"
        outputstr += "---------------------------------------------\n\n"
        outputstr += single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        outputstr += f"\n\nPassword: {pwdCheck}\n"
        outputstr += "--------------------------------------------\n\n"
        if pwddupes[pwdCheck] > 1:
            outputstr += f"You appear to be using this password {pwddupes[pwdCheck]} times!\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

def chrome_check(acclist, passlist):
    outputstr = ""
    for account in acclist:
        outputstr += f"Account Username: {account}\n"
        outputstr += "---------------------------------------------\n\n"
        outputstr += single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        outputstr += f"Password: {pwdCheck}\n"
        outputstr += "---------------------------------------------\n\n"
        if pwddupes[pwdCheck] > 1:
            outputstr += "You appear to be using this password {pwddupes[pwdCheck]} times!\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

def wifi_check(passlist):
    outputstr = ""
    for pwdCheck in passlist:
        outputstr += f"Password: {pwdCheck}\n"
        outputstr += "---------------------------------------------\n\n"
        outputstr += single_pass(pwdCheck)
        outputstr += "\n\n"
    return outputstr

class MyForm(QMainWindow):
    def __init__(self):
        self.procmode = 0
        self.fname = ""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Dad Pass') # Window Title
        self.setWindowIcon(QtGui.QIcon('assets\icon.png')) # Window icon
        
        """ Mode Buttons
        Modes
        0 - Not picked yet
        1 - Password
        2 - Account
        3 - File
        4 - browser
        5 - WiFi
        """
        self.ui.passCheck.toggled.connect(self.pickmode) # single pass
        self.ui.usernameCheck.toggled.connect(self.pickmode) # single username
        self.ui.fileCheck.toggled.connect(self.pickmode) # file 
        self.ui.browserCheck.toggled.connect(self.pickmode) # browser
        self.ui.wifiCheck.toggled.connect(self.pickmode) # wifi
        
        """ Buttons"""
        self.ui.run.clicked.connect(self.process) # Run Button
        self.ui.fileChoose.clicked.connect(self.choose_file) # File picker
        
        self.ui.usernameEdit.setReadOnly(True)
        self.ui.passwordEdit.setReadOnly(True)
        self.ui.run.setEnabled(False)
        self.ui.fileChoose.setEnabled(False)
        self.show()

    def clear_all(self):
        self.ui.usernameEdit.setText("")
        self.ui.passwordEdit.setText("")
        self.ui.fp_output.setText("")
        
    def choose_file(self):
        (self.fname, self.ftype) = QFileDialog.getOpenFileName(self, 'Open file', 
         '.',"Text files (*.txt)")
        self.ui.fp_output.setText(self.fname)
    
    def pickmode(self):
        self.ui.run.setEnabled(True)
        if self.ui.passCheck.isChecked():
            self.procmode = 1
            self.ui.passwordEdit.setReadOnly(False)
            self.ui.usernameEdit.setReadOnly(True)
            self.ui.fileChoose.setEnabled(False)
        
        elif self.ui.usernameCheck.isChecked():
            self.procmode = 2
            self.ui.passwordEdit.setReadOnly(True)
            self.ui.usernameEdit.setReadOnly(False)
            self.ui.fileChoose.setEnabled(False)
            
        elif self.ui.fileCheck.isChecked():
            self.procmode = 3
            self.ui.usernameEdit.setReadOnly(True)
            self.ui.passwordEdit.setReadOnly(True)
            self.ui.fileChoose.setEnabled(True)
        
        elif self.ui.browserCheck.isChecked():
            self.procmode = 4
            self.ui.usernameEdit.setReadOnly(True)
            self.ui.passwordEdit.setReadOnly(True)
            self.ui.fileChoose.setEnabled(False)
        
        elif self.ui.wifiCheck.isChecked():
            self.procmode = 5
            self.ui.usernameEdit.setReadOnly(True)
            self.ui.passwordEdit.setReadOnly(True)
            self.ui.fileChoose.setEnabled(False)
   		
    def process(self):
        self.ui.Output.setText("Loading....")
        lastInputStr = ""
        if self.procmode == 1:
            self.ui.run.setEnabled(False)
            if len(self.ui.passwordEdit.text()) > 0:
                pswd = str(self.ui.passwordEdit.text())
                self.ui.Output.setText(single_pass(pswd))
                lastInputStr = f"Mode: Single Password Check with password: {pswd}"
            else:
                QMessageBox.about(self, "Missing Field", "You forgot to specify password")
            self.ui.run.setEnabled(True)
        
        elif self.procmode == 2:
            self.ui.run.setEnabled(False)
            if len(self.ui.usernameEdit.text()) > 0:
                acct = str(self.ui.usernameEdit.text())
                try:
                    self.ui.Output.setText(single_account(acct))
                except KeyError:
                    QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
                finally:
                    self.ui.run.setEnabled(True)
                    lastInputStr = f"Mode: Single Account Check with Account: {acct}"
            else:
                QMessageBox.about(self, "Missing Field", "You forgot to specify username")
                self.ui.run.setEnabled(True)

        elif self.procmode == 3:
            self.ui.run.setEnabled(False)
            if len(self.fname) > 0:
                file = str(self.fname)
                try:
                    self.ui.Output.setText(file_check(file))
                except KeyError:
                    QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
                except data.FileLoadError:
                    QMessageBox.about(self, "Unknown File", "That file either doesn't exist, or it cannot be accessed")
                finally:
                    self.ui.run.setEnabled(True)
                    lastInputStr = f"Mode: File Check with File: {self.fname}"
            else:
                QMessageBox.about(self, "Missing Field", "You forgot to pick a file")
                self.ui.run.setEnabled(True)
        
        elif self.procmode == 4:
            self.ui.run.setEnabled(False)
            try:
                if checkIfProcessRunning("chrome.exe"):
                    closeChrome = QMessageBox()
                    closeChrome.setWindowIcon(QtGui.QIcon('assets\icon.png'))
                    closeChrome.setIconPixmap(QPixmap("assets\icon_small.png"))
                    closeChrome.setWindowTitle("Close Chrome")
                    closeChrome.setText("Chrome needs to be closed. Would you like me to close it?")
                    closeChrome.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    retval = closeChrome.exec_()
                    if retval == QtWidgets.QMessageBox.Yes:
                        os.system("taskkill /f /im chrome.exe")
                    else:
                        QMessageBox.about(self, "Close Chrome", "Please close Chrome before proceeding")

                (acclist, passlist) = browserpass.retrieve_chrome()
                if acclist is not None or passlist is not None:
                    self.ui.Output.setText(chrome_check(acclist, passlist))
                else:
                    QMessageBox.about(self, "Cannot find Chrome", "Cannot read the database. Is Chrome installed?")
            except KeyError:
                QMessageBox.about(self, "Missing API Key", "Account checking is not available, as no API key is installed on the system")
            except OperationalError:
                QMessageBox.about(self, "Database locked", "Cannot read the database. Is Chrome open?")
            finally:
                self.ui.run.setEnabled(True)
                lastInputStr = f"Mode: Browser Check"
        
        elif self.procmode == 5:
            self.ui.run.setEnabled(False)
            passlist = wifi.retrive_all()
            if passlist is not None:
                self.ui.Output.setText(wifi_check(passlist))
            else:
                self.ui.Output.setText("No WiFi Passwords Found")
            self.ui.run.setEnabled(True)
            lastInputStr = f"Mode: Wifi Check"
        self.ui.Input.setText(lastInputStr)
        self.clear_all()
    
  

if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())