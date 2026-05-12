from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ClassV:

    pass


class ClassU:

    pass


class ClassT:

    pass


class ClassS:

    pass


class ClassR:

    pass


class ClassQ:

    pass


class InterfaceO_Interface:

    pass


class ClassP:

    pass


class ClassN:

    pass


class ClassM:

    pass


class ClassL:

    pass


class ClassK:

    pass


class ClassH:

    pass


class ClassJ:

    pass


class ClassG:

    pass


class ClassF:

    pass


class ClassE:

    pass


class ClassD:

    pass


class ClassC:

    def __init__(self, publicAttribute: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute

    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute



class ClassB:

    pass


class ClassA:

    def __init__(self, publicAttribute: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute



class UserBean:

    def __init__(self, username: str, pass1: str, email: str, company: str, registration_date: str, valid: bool):
        self.username = username
        self.pass1 = pass1
        self.email = email
        self.company = company
        self.registration_date = registration_date
        self.valid = valid
        
        pass
    @property
    def registration_date(self):
        return self.__registration_date
    @registration_date.setter
    def registration_date(self, registration_date: str):
        self.__registration_date = registration_date

    @property
    def pass1(self):
        return self.__pass
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass = pass1

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, company: str):
        self.__company = company

    @property
    def valid(self):
        return self.__valid
    @valid.setter
    def valid(self, valid: bool):
        self.__valid = valid

