"""
account.py
------------

Defines the classes and functions that define an account and breaches
"""
import argparse
from colorama import Fore, Back, Style

from include import password, account, data
from collections import Counter
k

def single_pass(pswd):
    passwd = password.Password(pswd)
    if passwd.is_pwned():
        print(Fore.RED + f"This password is known to be breached. It has been seen {passwd.pwned_count()} times")
        print(Style.RESET_ALL)
    if passwd.score() == 0:
        print(Fore.RED + "This password is very weak")
    elif passwd.score() == 1:
        print(Fore.RED + "This password is weak")
    elif passwd.score() == 2:
        print(Fore.YELLOW + "This password is mild")
    elif passwd.score() == 3:
        print(Fore.GREEN + "This password is strong")
    elif passwd.score() == 4:
        print(Fore.GREEN + "This password is very strong")
    print(Style.RESET_ALL)
    suggestions = passwd.suggestions()
    warnings = passwd.warnings()
    
    if warnings != "":
        print(f"Password Warning: {Fore.RED} {warnings}")
        print(Style.RESET_ALL)
        
    if len(suggestions) > 0:
        print(f"Password suggestions:")
        for suggestion in suggestions:
            print(f"\t{suggestion}")
        print()
    

def single_account(acc):
    acct = account.Account(acc)
    try:
        breachCount = len(acct.breaches)
        if breachCount > 0 and breachCount < 5:
            print(Fore.YELLOW + f"This account has been seen in {breachCount} breaches")
        else:
            print(Fore.RED + f"This account has been seen in {breachCount} breaches")
    except TypeError:
        print(Fore.GREEN + "This account has not been seen in any breaches")
    finally:
        print(Style.RESET_ALL)

def file_check(fp):
    (acclist, passlist) = data.load_from_plainfile(fp)
    for account in acclist:
        print('\033[1m' + f"Account Username: {account}")
        print("-------------------------------------------------------")
        single_account(account)
    pwddupes = Counter(passlist)
    passlistDeDupe = []
    for item in passlist:
        if item not in passlistDeDupe:
            passlistDeDupe.append(item)
    for pwdCheck in passlistDeDupe:
        print('\033[1m' + f"Password: {pwdCheck}")
        print("-------------------------------------------------------")
        if pwddupes[pwdCheck] > 1:
            print(f"\033[1m {Fore.RED} You appear to be using this password {pwddupes[pwdCheck]} times!")
            print(Style.RESET_ALL)
        single_pass(pwdCheck)
        print("\n\n")
            
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password/Account Security Checker')
    parser.add_argument("-a", "--account", help="Checks a single account", action="store", nargs='?', default=None)
    #parser.add_argument("account", help="The single account to check", type=str, default=None)
    
    parser.add_argument("-p", "--password", help="Checks a single password",  action="store", nargs='?', default=None)
    #parser.add_argument("password", help="The single password to check", type=str, default=None)
    
    parser.add_argument("-f", "--file", help="Checks account:password pairs from a file ",  action="store", nargs='?', default=None)
    #parser.add_argument("file", help="The file to parse and process", type=str, default=None)
    
    args = parser.parse_args()
    
    if args.account is not None:
        single_account(args.account)
        
    elif args.password is not None:
        single_pass(args.password)

    elif args.file is not None:
        file_check(args.file)
        
    else:
        print("You must pick at least one option")
    