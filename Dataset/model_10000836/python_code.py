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
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

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



class StockNotice:

    def __init__(self, ID: float, ProductID: str, ProductName: str, MatchedPrice: str, Source: str):
        self.ID = ID
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.MatchedPrice = MatchedPrice
        self.Source = Source
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: float):
        self.__ID = ID

    @property
    def Source(self):
        return self.__Source
    @Source.setter
    def Source(self, Source: str):
        self.__Source = Source

    @property
    def ProductName(self):
        return self.__ProductName
    @ProductName.setter
    def ProductName(self, ProductName: str):
        self.__ProductName = ProductName

    @property
    def MatchedPrice(self):
        return self.__MatchedPrice
    @MatchedPrice.setter
    def MatchedPrice(self, MatchedPrice: str):
        self.__MatchedPrice = MatchedPrice

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: str):
        self.__ProductID = ProductID

