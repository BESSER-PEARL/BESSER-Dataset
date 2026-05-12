from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Player:

    def __init__(self, name: str, token: str, position: int, balance: int):
        self.name = name
        self.token = token
        self.position = position
        self.balance = balance
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def token(self):
        return self.__token
    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

