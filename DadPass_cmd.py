import argparse

from dadpass import password, account, data, browserpass, wifi
from collections import Counter


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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dad Pass Command Line Tool')
    parser.add_argument("-a", "--account", help="Checks a single account", action="store", nargs='?', default=None)
    parser.add_argument("-p", "--password", help="Checks a single password",  action="store", nargs='?', default=None)
    parser.add_argument("-f", "--file", help="Checks account:password pairs from a file ",  action="store", nargs='?', default=None)
    parser.add_argument("-b", "--browser", help="Check accounts and passwords saved in web browsers", action="store_true")
    parser.add_argument("-w", "--wifi", help="Checks saved WiFi passwords", action="store_true")
    args = parser.parse_args()
    
    if args.account is not None:
        try:
            print(single_account(args.account))
        except KeyError:
            print("Missing API Key. Account checking is not available, as no API key is installed on the system")
        
    elif args.password is not None:
        print(single_pass(args.password))

    elif args.file is not None:
        try:
            print(file_check(args.file))
        except KeyError:
            print("Missing API Key. Account checking is not available, as no API key is installed on the system")
        except data.FileLoadError:
            print("Unknown File. That file either doesn't exist, or it cannot be accessed")
        
    elif args.browser:
        print("Chrome needs to be closed for this to work.")
        input("Please verify Chrome is closed then press enter")
        try:
            (acclist, passlist) = browserpass.retrieve_chrome()
            print(chrome_check(acclist, passlist))
        except KeyError:
                print("Missing API Key. Account checking is not available, as no API key is installed on the system")
        except OperationalError:
            print("Database locked. Cannot read the database. Is Chrome open?")

    
    elif args.wifi:
        passlist = wifi.retrive_all()
        print(wifi_check(passlist))
    
    else:
        print("You must pick at least one option")
    