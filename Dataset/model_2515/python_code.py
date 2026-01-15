from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EEnum0(Enum):
    a = "a"
    b = "b"


############################################
# Definition of Classes
############################################

class test_EClass1:

    def __init__(self, EAttribute0: str, test_EClass1: "test_EClass0" = None, test_EClass14: "test_EClass2" = None):
        self.EAttribute0 = EAttribute0
        self.test_EClass1 = test_EClass1
        self.test_EClass14 = test_EClass14
        
    @property
    def EAttribute0(self) -> str:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: str):
        self.__EAttribute0 = EAttribute0

    @property
    def test_EClass1(self):
        return self.__test_EClass1

    @test_EClass1.setter
    def test_EClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass1__test_EClass1", None)
        self.__test_EClass1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass0"):
                opp_val = getattr(old_value, "test_EClass0", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass0"):
                opp_val = getattr(value, "test_EClass0", None)
                setattr(value, "test_EClass0", self)

    @property
    def test_EClass14(self):
        return self.__test_EClass14

    @test_EClass14.setter
    def test_EClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass1__test_EClass14", None)
        self.__test_EClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass25"):
                opp_val = getattr(old_value, "test_EClass25", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass25"):
                opp_val = getattr(value, "test_EClass25", None)
                setattr(value, "test_EClass25", self)

class test_EClass0:

    def __init__(self, attr0: str, attr1: bool, test_EClass0: "test_EClass1" = None, test_EClass02: set["test_EClass2"] = None):
        self.attr0 = attr0
        self.attr1 = attr1
        self.test_EClass0 = test_EClass0
        self.test_EClass02 = test_EClass02 if test_EClass02 is not None else set()
        
    @property
    def attr0(self) -> str:
        return self.__attr0

    @attr0.setter
    def attr0(self, attr0: str):
        self.__attr0 = attr0

    @property
    def attr1(self) -> bool:
        return self.__attr1

    @attr1.setter
    def attr1(self, attr1: bool):
        self.__attr1 = attr1

    @property
    def test_EClass0(self):
        return self.__test_EClass0

    @test_EClass0.setter
    def test_EClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass0__test_EClass0", None)
        self.__test_EClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass1"):
                opp_val = getattr(old_value, "test_EClass1", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass1"):
                opp_val = getattr(value, "test_EClass1", None)
                setattr(value, "test_EClass1", self)

    @property
    def test_EClass02(self):
        return self.__test_EClass02

    @test_EClass02.setter
    def test_EClass02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass0__test_EClass02", None)
        self.__test_EClass02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_EClass2"):
                    opp_val = getattr(item, "test_EClass2", None)
                    
                    if opp_val == self:
                        setattr(item, "test_EClass2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_EClass2"):
                    opp_val = getattr(item, "test_EClass2", None)
                    
                    setattr(item, "test_EClass2", self)
                    

class test_EClass2:

    def __init__(self, EAttribute0: bool, EAttribute1: int, test_EClass2: "test_EClass0" = None, test_EClass25: "test_EClass1" = None):
        self.EAttribute0 = EAttribute0
        self.EAttribute1 = EAttribute1
        self.test_EClass2 = test_EClass2
        self.test_EClass25 = test_EClass25
        
    @property
    def EAttribute1(self) -> int:
        return self.__EAttribute1

    @EAttribute1.setter
    def EAttribute1(self, EAttribute1: int):
        self.__EAttribute1 = EAttribute1

    @property
    def EAttribute0(self) -> bool:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: bool):
        self.__EAttribute0 = EAttribute0

    @property
    def test_EClass25(self):
        return self.__test_EClass25

    @test_EClass25.setter
    def test_EClass25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass2__test_EClass25", None)
        self.__test_EClass25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass14"):
                opp_val = getattr(old_value, "test_EClass14", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass14"):
                opp_val = getattr(value, "test_EClass14", None)
                setattr(value, "test_EClass14", self)

    @property
    def test_EClass2(self):
        return self.__test_EClass2

    @test_EClass2.setter
    def test_EClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClass2__test_EClass2", None)
        self.__test_EClass2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass02"):
                opp_val = getattr(old_value, "test_EClass02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass02"):
                opp_val = getattr(value, "test_EClass02", None)
                if opp_val is None:
                    setattr(value, "test_EClass02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
