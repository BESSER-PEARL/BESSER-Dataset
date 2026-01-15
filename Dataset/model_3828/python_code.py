from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SubTestEnum(Enum):
class TestEnum(Enum):


############################################
# Definition of Classes
############################################

class TestPackage_SubPackage_SubTestInterface(ABC):

    pass
class TestPackage_SubPackage_SubTestClass:

    def __init__(self, testIntAttr: int, testStringAttr: str, testRealAttr: str, testBooleanAttr: bool, testAttr: date):
        self.testIntAttr = testIntAttr
        self.testStringAttr = testStringAttr
        self.testRealAttr = testRealAttr
        self.testBooleanAttr = testBooleanAttr
        self.testAttr = testAttr
        
    @property
    def testRealAttr(self) -> str:
        return self.__testRealAttr

    @testRealAttr.setter
    def testRealAttr(self, testRealAttr: str):
        self.__testRealAttr = testRealAttr

    @property
    def testIntAttr(self) -> int:
        return self.__testIntAttr

    @testIntAttr.setter
    def testIntAttr(self, testIntAttr: int):
        self.__testIntAttr = testIntAttr

    @property
    def testAttr(self) -> date:
        return self.__testAttr

    @testAttr.setter
    def testAttr(self, testAttr: date):
        self.__testAttr = testAttr

    @property
    def testStringAttr(self) -> str:
        return self.__testStringAttr

    @testStringAttr.setter
    def testStringAttr(self, testStringAttr: str):
        self.__testStringAttr = testStringAttr

    @property
    def testBooleanAttr(self) -> bool:
        return self.__testBooleanAttr

    @testBooleanAttr.setter
    def testBooleanAttr(self, testBooleanAttr: bool):
        self.__testBooleanAttr = testBooleanAttr

class TestPackage_UberClass(ABC):

    pass
class TestPackage_SuperClass(ABC):

    pass
class UberClass:

    pass
class SuperClass:

    pass
class TestPackage_TestInterface(SuperClass):

    pass
class TestPackage_TestClass(SuperClass, UberClass):

    def __init__(self, testRealAttr: str, testBooleanAttr: bool, testIntAttr: int, testAttr1: int, testAttr2: int, testAttr3: int, testAttr4: int, testAttr5: int, testUnlimitedNaturalAttr: str, testAttr: date, testStringAttr: str, testAttr6: int, testAttr7: int, testAttr8: int):
        self.testRealAttr = testRealAttr
        self.testBooleanAttr = testBooleanAttr
        self.testIntAttr = testIntAttr
        self.testAttr1 = testAttr1
        self.testAttr2 = testAttr2
        self.testAttr3 = testAttr3
        self.testAttr4 = testAttr4
        self.testAttr5 = testAttr5
        self.testUnlimitedNaturalAttr = testUnlimitedNaturalAttr
        self.testAttr = testAttr
        self.testStringAttr = testStringAttr
        self.testAttr6 = testAttr6
        self.testAttr7 = testAttr7
        self.testAttr8 = testAttr8
        
    @property
    def testUnlimitedNaturalAttr(self) -> str:
        return self.__testUnlimitedNaturalAttr

    @testUnlimitedNaturalAttr.setter
    def testUnlimitedNaturalAttr(self, testUnlimitedNaturalAttr: str):
        self.__testUnlimitedNaturalAttr = testUnlimitedNaturalAttr

    @property
    def testAttr5(self) -> int:
        return self.__testAttr5

    @testAttr5.setter
    def testAttr5(self, testAttr5: int):
        self.__testAttr5 = testAttr5

    @property
    def testAttr1(self) -> int:
        return self.__testAttr1

    @testAttr1.setter
    def testAttr1(self, testAttr1: int):
        self.__testAttr1 = testAttr1

    @property
    def testAttr2(self) -> int:
        return self.__testAttr2

    @testAttr2.setter
    def testAttr2(self, testAttr2: int):
        self.__testAttr2 = testAttr2

    @property
    def testIntAttr(self) -> int:
        return self.__testIntAttr

    @testIntAttr.setter
    def testIntAttr(self, testIntAttr: int):
        self.__testIntAttr = testIntAttr

    @property
    def testStringAttr(self) -> str:
        return self.__testStringAttr

    @testStringAttr.setter
    def testStringAttr(self, testStringAttr: str):
        self.__testStringAttr = testStringAttr

    @property
    def testBooleanAttr(self) -> bool:
        return self.__testBooleanAttr

    @testBooleanAttr.setter
    def testBooleanAttr(self, testBooleanAttr: bool):
        self.__testBooleanAttr = testBooleanAttr

    @property
    def testRealAttr(self) -> str:
        return self.__testRealAttr

    @testRealAttr.setter
    def testRealAttr(self, testRealAttr: str):
        self.__testRealAttr = testRealAttr

    @property
    def testAttr8(self) -> int:
        return self.__testAttr8

    @testAttr8.setter
    def testAttr8(self, testAttr8: int):
        self.__testAttr8 = testAttr8

    @property
    def testAttr3(self) -> int:
        return self.__testAttr3

    @testAttr3.setter
    def testAttr3(self, testAttr3: int):
        self.__testAttr3 = testAttr3

    @property
    def testAttr(self) -> date:
        return self.__testAttr

    @testAttr.setter
    def testAttr(self, testAttr: date):
        self.__testAttr = testAttr

    @property
    def testAttr7(self) -> int:
        return self.__testAttr7

    @testAttr7.setter
    def testAttr7(self, testAttr7: int):
        self.__testAttr7 = testAttr7

    @property
    def testAttr4(self) -> int:
        return self.__testAttr4

    @testAttr4.setter
    def testAttr4(self, testAttr4: int):
        self.__testAttr4 = testAttr4

    @property
    def testAttr6(self) -> int:
        return self.__testAttr6

    @testAttr6.setter
    def testAttr6(self, testAttr6: int):
        self.__testAttr6 = testAttr6
