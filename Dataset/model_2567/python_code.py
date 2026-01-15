from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TestPackage_TestIndexEntry:

    pass
class TestPackage_TestIndex:

    pass
class AbstractTestClass:

    pass
class TestPackage_TestClass2(AbstractTestClass):

    pass
class TestPackage_TestClass1(AbstractTestClass):

    def __init__(self, theAttributeToListen: str):
        self.theAttributeToListen = theAttributeToListen
        
    @property
    def theAttributeToListen(self) -> str:
        return self.__theAttributeToListen

    @theAttributeToListen.setter
    def theAttributeToListen(self, theAttributeToListen: str):
        self.__theAttributeToListen = theAttributeToListen

    def testOperation(self, testParameter: int) -> str:
        # TODO: Implement testOperation method
        pass

class TestPackage_AbstractTestClass(ABC):

    def __init__(self, name: str, TestPackage_AbstractTestClass: "TestPackage_TestIndexEntry" = None):
        self.name = name
        self.TestPackage_AbstractTestClass = TestPackage_AbstractTestClass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TestPackage_AbstractTestClass(self):
        return self.__TestPackage_AbstractTestClass

    @TestPackage_AbstractTestClass.setter
    def TestPackage_AbstractTestClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_AbstractTestClass__TestPackage_AbstractTestClass", None)
        self.__TestPackage_AbstractTestClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestIndexEntry2"):
                opp_val = getattr(old_value, "TestPackage_TestIndexEntry2", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_TestIndexEntry2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestIndexEntry2"):
                opp_val = getattr(value, "TestPackage_TestIndexEntry2", None)
                setattr(value, "TestPackage_TestIndexEntry2", self)
