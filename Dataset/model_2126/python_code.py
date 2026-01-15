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
class SubTestClass:

    pass
class TestPackage_TestClass:

    def __init__(self, testAttr: bool, TestPackage_TestClass: "SubTestClass" = None):
        self.testAttr = testAttr
        self.TestPackage_TestClass = TestPackage_TestClass
        
    @property
    def testAttr(self) -> bool:
        return self.__testAttr

    @testAttr.setter
    def testAttr(self, testAttr: bool):
        self.__testAttr = testAttr

    @property
    def TestPackage_TestClass(self):
        return self.__TestPackage_TestClass

    @TestPackage_TestClass.setter
    def TestPackage_TestClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestClass__TestPackage_TestClass", None)
        self.__TestPackage_TestClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubTestClass"):
                opp_val = getattr(old_value, "SubTestClass", None)
                if opp_val == self:
                    setattr(old_value, "SubTestClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubTestClass"):
                opp_val = getattr(value, "SubTestClass", None)
                setattr(value, "SubTestClass", self)

    def testOp(self):
        # TODO: Implement testOp method
        pass
