"""
password.py
------------

Defines the classes and functions that define a password and its flaws
"""

from .hibp import check_password
from .passStrength import PasswordStrength

class Password:
    """Represents a password object
    
    Attributes
    ------------
    passvalue: :class:`str`
        The actual password value
    __pwned :class:`PwnedPassword`
        Stores the PwnedPassword object (or None)
    __passstrengh: :class:`PasswordStrength`
        Stores the password strength object
    """
    def __init__(self, password):
        self.passvalue = password
        self.__pwned = check_password(password)
        self.__passstrength = PasswordStrength(password)
        
    def is_pwned(self):
        return __pwned is not None
    
    def pwned_count(self):
        if self.__pwned is not None:
            return self.__pwned.get_pwncount()
    
    def score(self):
        return self.__passstrength.score
    
    def suggestions(self):
        return self.__passstrength.suggestions
    
    def warnings(self):
        return self.__passstrength.warnings