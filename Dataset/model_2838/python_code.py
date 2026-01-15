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

    pass
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
class TestPackage_TestClass(UberClass, SuperClass):

    def __init__(self):
        
    def testOp6(self) -> str:
        # TODO: Implement testOp6 method
        pass

    def testOp7(self) -> str:
        # TODO: Implement testOp7 method
        pass

    def testOp2(self) -> str:
        # TODO: Implement testOp2 method
        pass

    def testOp3(self) -> str:
        # TODO: Implement testOp3 method
        pass

    def testOp8(self) -> str:
        # TODO: Implement testOp8 method
        pass

    def testOp(self, testParam2: str, testParam: bool) -> str:
        # TODO: Implement testOp method
        pass

    def testOp1(self) -> str:
        # TODO: Implement testOp1 method
        pass

    def testOp4(self) -> str:
        # TODO: Implement testOp4 method
        pass

    def testOp5(self) -> str:
        # TODO: Implement testOp5 method
        pass

    def testVoidOp(self):
        # TODO: Implement testVoidOp method
        pass

    def testOp9(self, testParam2: str, testParam: bool) -> str:
        # TODO: Implement testOp9 method
        pass
