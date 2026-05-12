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
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute



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



class BankAccount:

    def __init__(self, ownerName: str, balance: float):
        self.ownerName = ownerName
        self.balance = balance
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

