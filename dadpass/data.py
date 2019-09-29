"""
data.py
--------

This file contains the functions for loading data
"""
class FileLoadError(Exception):
    pass

def load_passwords(datafile):
    freader = datafile.readlines()
    passList = []
    for line in freader:
        delimIndex = line.find(":") + 1
        pwd = line[delimIndex:]
        pwd = pwd.replace("\n","")
        pwd = pwd.replace("\t","")
        pwd = pwd.replace("\r","")
        passList.append(pwd)
    return passList

def load_accounts(datafile):
    freader = datafile.readlines()
    accList = []
    for line in freader:
        delimIndex = line.find(":")
        acc = line[:delimIndex].lower()
        acc = acc.replace("\n","")
        acc = acc.replace("\t","")
        acc = acc.replace("\r","")
        accList.append(acc)
    dedupAccList = []
    for item in accList:
        if item not in dedupAccList:
            dedupAccList.append(item)
    return dedupAccList

def load_from_plainfile(file):
    """
    This requires files to be plaintext and in the following format for correct processing
    username:password
    """
    try:
        datafile = open(file, "r")
        passList = load_passwords(datafile)
        datafile.seek(0)
        accList = load_accounts(datafile)
        if datafile.mode !="r":
            raise FileLoadError("File could not be loaded correctly")
        return (accList,passList)
    except FileNotFoundError:
        raise FileLoadError("File was unable to be loaded. Verify the file exists")
