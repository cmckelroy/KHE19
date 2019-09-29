# Modified from https://github.com/D4Vinci/WifiPass/blob/master/Dump.py
import os, re

#Get all saved wifi networks names
def get_wlans():
    data = os.popen("netsh wlan show profiles").read()
    wifi = re.compile("All User Profile\s*:.(.*)")
    return wifi.findall(data)

#Get a password for a network
def get_pass(network):
    try:
        wlan = os.popen("netsh wlan show profile "+str(network.replace(" ","*"))+" key=clear").read()
        pass_regex = re.compile("Key Content\s*:.(.*)")
        return pass_regex.search(wlan).group(1)
    except:
        return " "

def retrive_all():
    passlist = []
    for wlan in get_wlans():
        pswd = get_pass(wlan)
        if len(pswd) > 1:
            if pswd not in passlist:
                passlist.append(pswd)
    return passlist