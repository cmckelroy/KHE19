"""
hibp.py
------------

Defines the classes and queries the haveibeenpwned api.
"""
import requests
import json
import re

from datetime import datetime
from hashlib import sha1
from os import environ

class AccountBreach:
    """Represents a breach returned from HaveIBeenPwned
    
    Attributes
    ------------
    title: :class:`str`
        The Title of the Breach
    domain: :class:`str`
        The domain of the service breached
    breach_date: :class:`datetime`
        The date the breach occured
    pwncount: :class:`int`
        The total number of accounts included in the breach
    description: :class:`str`
        An overview of the breach and included data
    verified: :class:`bool`
        Whether or not a significant amount of the data is legitimate
    
    """
    def __init__(self, data):
        self.__title = data['Title']
        self.__domain = data['Domain']
        self.__breach_date = data ['BreachDate']
        self.__pwncount = data ['PwnCount']
        self.__description = data ['Description']
        self.__verified = bool(data['IsVerified'])
        
        
    def get_title(self):
        return self.__title
    
    def get_domain(self):
        return self.__domain
    
    def get_breach_date(self):
        return self.__breach_date
    
    def get_pwncount(self):
        return self.__pwncount

    def get_description(self):
        return self.__description
    
    def get_verified(self):
        return self.__verified
    
class PwnedPassword:
    """Represents a Pwned Password returned from HaveIBeenPwned
    
    Attributes
    ------------
    hash: :class:`str`
        The Hash of the password
    pwncount: :class:`int`
        Count of the number of times the password has been seen
    """
    
    def __init__(self, data):
        self.__hash = data['hash']
        self.__pwncount = data['pwncount']
        
    def get_hash(self):
        return self.__hash
        
    def get_pwncount(self):
        return self.__pwncount

class APIException(Exception):
    pass
    
def check_account(username):
    apikey = environ["HIBP_API_KEY"] # I Really didn't want to store this in code, so maybe I'd package this with the installer?
    apiurl_base = "https://haveibeenpwned.com/api/v3/breachedaccount/"
    request_headers = {
        'hibp-api-key': apikey,
        'user-agent': "KHE2019PassSecurity"
    }
    apiurl = f"{apiurl_base}{username}?truncateResponse=false"
    breachRequest = requests.get(apiurl,headers=request_headers)
    
    if breachRequest.status_code == 404:
        return None # The account is not known in any breaches
    elif breachRequest.status_code != 200:
        raise APIException(f"API Raised an unexpected response. HTTP status code {breachRequest.status_code}")
    
    returnedJsonData = breachRequest.content
    BreachDataList = json.loads(returnedJsonData)
    breachReturn = []
    for breach in BreachDataList:
        breachobj = AccountBreach(breach)
        breachReturn.append(breachobj)
    
    return breachReturn

def check_password(password):
    passwordHash = str(sha1(password.encode()).hexdigest())
    apiurl_base = "https://api.pwnedpasswords.com/range/"
    apiurl = f"{apiurl_base}{passwordHash[:5]}"
    pwnedPassRequest = requests.get(apiurl)
    
    if pwnedPassRequest.status_code == 404: # This should NEVER happen, buttttt just in case
        return None
    elif pwnedPassRequest.status_code != 200:
        raise APIException(f"API Raised an unexpected response. HTTP status code {pwnedPassRequest.status_code}")
    
    returnedHashes = str(pwnedPassRequest.content.decode())
    hashList = returnedHashes.split()
    for hashobj in hashList:
        if hashobj[:35].lower() == passwordHash[5:].lower():
            foundPwnDict = {
                "hash": passwordHash,
                "pwncount": hashobj[36:]
            }
            foundPwn = PwnedPassword(foundPwnDict)
            return foundPwn
    return None # Password is not pwned