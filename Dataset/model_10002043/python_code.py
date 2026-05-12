from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass9:

    pass


class mypackage2_MyClass2:

    pass


class mypackage2_MyInterface_Interface:

    pass


class mypackage2_MyClass:

    pass


class MyInterface_Interface:

    pass


class MyClass8:

    pass


class MyClass7:

    pass


class MyClass6:

    pass


class MyClass5:

    pass


class MyClass4:

    pass


class MyClass3:

    pass


class MyClass2:

    pass


class MyClass:

    pass


class Location2:

    pass


class Location:

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location



class BaseBO:

    def __init__(self, testString: str, newInt: int, newBool: bool):
        self.testString = testString
        self.newInt = newInt
        self.newBool = newBool
        
        pass
    @property
    def newBool(self):
        return self.__newBool
    @newBool.setter
    def newBool(self, newBool: bool):
        self.__newBool = newBool

    @property
    def testString(self):
        return self.__testString
    @testString.setter
    def testString(self, testString: str):
        self.__testString = testString

    @property
    def newInt(self):
        return self.__newInt
    @newInt.setter
    def newInt(self, newInt: int):
        self.__newInt = newInt



class Class:

    pass


class PolicyImage:

    def __init__(self, serialVersionID: str):
        self.serialVersionID = serialVersionID
        
        pass
    @property
    def serialVersionID(self):
        return self.__serialVersionID
    @serialVersionID.setter
    def serialVersionID(self, serialVersionID: str):
        self.__serialVersionID = serialVersionID

