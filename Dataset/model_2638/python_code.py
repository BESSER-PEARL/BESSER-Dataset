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
class SubTestClass:

    pass
class UberClass:

    pass
class SuperClass:

    pass
class TestPackage_TestInterface(SuperClass):

    def __init__(self, testAttr: str, TestPackage_TestInterface23: "TestPackage_TestClass" = None, TestPackage_TestInterface: "TestPackage_TestClass" = None, TestPackage_TestInterface5: "TestPackage_TestClass" = None, TestPackage_TestInterface8: "TestPackage_TestClass" = None, TestPackage_TestInterface11: "TestPackage_TestClass" = None, TestPackage_TestInterface14: "TestPackage_TestClass" = None, TestPackage_TestInterface17: "TestPackage_TestClass" = None, TestPackage_TestInterface20: "TestPackage_TestClass" = None, TestPackage_TestInterface26: "TestPackage_TestClass" = None, TestPackage_TestInterface29: "TestPackage_TestClass" = None):
        self.testAttr = testAttr
        self.TestPackage_TestInterface23 = TestPackage_TestInterface23
        self.TestPackage_TestInterface = TestPackage_TestInterface
        self.TestPackage_TestInterface5 = TestPackage_TestInterface5
        self.TestPackage_TestInterface8 = TestPackage_TestInterface8
        self.TestPackage_TestInterface11 = TestPackage_TestInterface11
        self.TestPackage_TestInterface14 = TestPackage_TestInterface14
        self.TestPackage_TestInterface17 = TestPackage_TestInterface17
        self.TestPackage_TestInterface20 = TestPackage_TestInterface20
        self.TestPackage_TestInterface26 = TestPackage_TestInterface26
        self.TestPackage_TestInterface29 = TestPackage_TestInterface29
        
    @property
    def testAttr(self) -> str:
        return self.__testAttr

    @testAttr.setter
    def testAttr(self, testAttr: str):
        self.__testAttr = testAttr

    @property
    def TestPackage_TestInterface14(self):
        return self.__TestPackage_TestInterface14

    @TestPackage_TestInterface14.setter
    def TestPackage_TestInterface14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface14", None)
        self.__TestPackage_TestInterface14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass13"):
                opp_val = getattr(old_value, "TestPackage_TestClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass13"):
                opp_val = getattr(value, "TestPackage_TestClass13", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestPackage_TestInterface20(self):
        return self.__TestPackage_TestInterface20

    @TestPackage_TestInterface20.setter
    def TestPackage_TestInterface20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface20", None)
        self.__TestPackage_TestInterface20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass19"):
                opp_val = getattr(old_value, "TestPackage_TestClass19", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_TestClass19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass19"):
                opp_val = getattr(value, "TestPackage_TestClass19", None)
                setattr(value, "TestPackage_TestClass19", self)

    @property
    def TestPackage_TestInterface(self):
        return self.__TestPackage_TestInterface

    @TestPackage_TestInterface.setter
    def TestPackage_TestInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface", None)
        self.__TestPackage_TestInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass2"):
                opp_val = getattr(old_value, "TestPackage_TestClass2", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_TestClass2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass2"):
                opp_val = getattr(value, "TestPackage_TestClass2", None)
                setattr(value, "TestPackage_TestClass2", self)

    @property
    def TestPackage_TestInterface17(self):
        return self.__TestPackage_TestInterface17

    @TestPackage_TestInterface17.setter
    def TestPackage_TestInterface17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface17", None)
        self.__TestPackage_TestInterface17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass16"):
                opp_val = getattr(old_value, "TestPackage_TestClass16", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_TestClass16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass16"):
                opp_val = getattr(value, "TestPackage_TestClass16", None)
                setattr(value, "TestPackage_TestClass16", self)

    @property
    def TestPackage_TestInterface8(self):
        return self.__TestPackage_TestInterface8

    @TestPackage_TestInterface8.setter
    def TestPackage_TestInterface8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface8", None)
        self.__TestPackage_TestInterface8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass7"):
                opp_val = getattr(old_value, "TestPackage_TestClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass7"):
                opp_val = getattr(value, "TestPackage_TestClass7", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestPackage_TestInterface5(self):
        return self.__TestPackage_TestInterface5

    @TestPackage_TestInterface5.setter
    def TestPackage_TestInterface5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface5", None)
        self.__TestPackage_TestInterface5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass4"):
                opp_val = getattr(old_value, "TestPackage_TestClass4", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_TestClass4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass4"):
                opp_val = getattr(value, "TestPackage_TestClass4", None)
                setattr(value, "TestPackage_TestClass4", self)

    @property
    def TestPackage_TestInterface23(self):
        return self.__TestPackage_TestInterface23

    @TestPackage_TestInterface23.setter
    def TestPackage_TestInterface23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface23", None)
        self.__TestPackage_TestInterface23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass22"):
                opp_val = getattr(old_value, "TestPackage_TestClass22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass22"):
                opp_val = getattr(value, "TestPackage_TestClass22", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestPackage_TestInterface26(self):
        return self.__TestPackage_TestInterface26

    @TestPackage_TestInterface26.setter
    def TestPackage_TestInterface26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface26", None)
        self.__TestPackage_TestInterface26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass25"):
                opp_val = getattr(old_value, "TestPackage_TestClass25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass25"):
                opp_val = getattr(value, "TestPackage_TestClass25", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestPackage_TestInterface11(self):
        return self.__TestPackage_TestInterface11

    @TestPackage_TestInterface11.setter
    def TestPackage_TestInterface11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface11", None)
        self.__TestPackage_TestInterface11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass10"):
                opp_val = getattr(old_value, "TestPackage_TestClass10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass10"):
                opp_val = getattr(value, "TestPackage_TestClass10", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestPackage_TestInterface29(self):
        return self.__TestPackage_TestInterface29

    @TestPackage_TestInterface29.setter
    def TestPackage_TestInterface29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TestPackage_TestInterface__TestPackage_TestInterface29", None)
        self.__TestPackage_TestInterface29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_TestClass28"):
                opp_val = getattr(old_value, "TestPackage_TestClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_TestClass28"):
                opp_val = getattr(value, "TestPackage_TestClass28", None)
                if opp_val is None:
                    setattr(value, "TestPackage_TestClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TestPackage_TestClass(SuperClass, UberClass):

    pass