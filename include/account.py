"""
account.py
------------

Defines the classes and functions that define an account and breaches
"""
from .hibp import check_account

class Account:
    def __init__(self, username):
        self.username = username
        self.breaches = check_account(username)
    
    def breachcount(self):
        return len(self.breaches)