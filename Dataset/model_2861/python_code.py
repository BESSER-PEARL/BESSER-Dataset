from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestEnum(Enum):
    pass
class SubTestEnum(Enum):
    pass

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
        
        pass
    def testOp8(self) :
        # TODO: Implement testOp8 method
        pass

    def testVoidOp(self):
        # TODO: Implement testVoidOp method
        pass

    def testOp2(self) :
        # TODO: Implement testOp2 method
        pass

    def testOp9(self, TestPackage_testParam, TestPackage_testParam2):
        # TODO: Implement testOp9 method
        pass

    def testOp5(self) :
        # TODO: Implement testOp5 method
        pass

    def testOp6(self) :
        # TODO: Implement testOp6 method
        pass

    def testOp7(self) :
        # TODO: Implement testOp7 method
        pass

    def testOp1(self) :
        # TODO: Implement testOp1 method
        pass

    def testOp(self, TestPackage_testParam, TestPackage_testParam2):
        # TODO: Implement testOp method
        pass

    def testOp4(self) :
        # TODO: Implement testOp4 method
        pass

    def testOp3(self) :
        # TODO: Implement testOp3 method
        pass
