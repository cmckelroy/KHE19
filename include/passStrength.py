"""
passStrength.py
------------

Defines the classes and functions necessary to determine password strength
"""

from zxcvbn import zxcvbn


class PasswordStrength:
    """Represents the strengh of a password
    
    Attributes
    ------------
    score: :class:`int`
        A score from 0-4 (0 is lowest) of the password strength
    warnings :class:`str`
        Warnings about the password
    suggestions: :class:`list`
        A list of suggestions for the password
    """
    def __init__(self, password):
        self.__strengthResult = zxcvbn(password)
        self.score = int(self.__strengthResult['score'])
        self.warnings = self.__strengthResult['feedback']['warning']
        self.suggestions = self.__strengthResult['feedback']['suggestions']
