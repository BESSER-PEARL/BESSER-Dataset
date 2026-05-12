from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










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



class Exception:

    pass


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


class ClassG:

    pass


class ClassF:

    pass


class ClassE:

    pass


class ClassD:

    pass


class ErrorCode:

    def __init__(self, tier: int, domain: int, subdomain: int, reason: int):
        self.tier = tier
        self.domain = domain
        self.subdomain = subdomain
        self.reason = reason
        
        pass
    @property
    def tier(self):
        return self.__tier
    @tier.setter
    def tier(self, tier: int):
        self.__tier = tier

    @property
    def reason(self):
        return self.__reason
    @reason.setter
    def reason(self, reason: int):
        self.__reason = reason

    @property
    def domain(self):
        return self.__domain
    @domain.setter
    def domain(self, domain: int):
        self.__domain = domain

    @property
    def subdomain(self):
        return self.__subdomain
    @subdomain.setter
    def subdomain(self, subdomain: int):
        self.__subdomain = subdomain



class ErrorCodeException:

    def __init__(self, errorCode: ErrorCode, errorCodeMessage: str, throwable: str):
        self.errorCode = errorCode
        self.errorCodeMessage = errorCodeMessage
        self.throwable = throwable
        
        pass
    @property
    def errorCode(self):
        return self.__errorCode
    @errorCode.setter
    def errorCode(self, errorCode: ErrorCode):
        self.__errorCode = errorCode

    @property
    def errorCodeMessage(self):
        return self.__errorCodeMessage
    @errorCodeMessage.setter
    def errorCodeMessage(self, errorCodeMessage: str):
        self.__errorCodeMessage = errorCodeMessage

    @property
    def throwable(self):
        return self.__throwable
    @throwable.setter
    def throwable(self, throwable: str):
        self.__throwable = throwable

