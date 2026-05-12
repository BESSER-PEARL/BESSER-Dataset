from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, address: str, phone: str, email: str):
        self.address = address
        self.phone = phone
        self.email = email
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

