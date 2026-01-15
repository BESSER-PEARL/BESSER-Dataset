from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MyEnum(Enum):
    X = "X"
    Y = "Y"


############################################
# Definition of Classes
############################################

class test_subpackage_SubpackageMetaClass:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SubpackageMetaClass:

    pass
class test_MyMetaClass:

    def __init__(self, name: str, enumAttr: str, test_MyMetaClass: "test_MyMetaClass" = None, test_MyMetaClass0: set["test_MyMetaClass"] = None, test_MyMetaClass3: "SubpackageMetaClass" = None):
        self.name = name
        self.enumAttr = enumAttr
        self.test_MyMetaClass = test_MyMetaClass
        self.test_MyMetaClass0 = test_MyMetaClass0 if test_MyMetaClass0 is not None else set()
        self.test_MyMetaClass3 = test_MyMetaClass3
        
    @property
    def enumAttr(self) -> str:
        return self.__enumAttr

    @enumAttr.setter
    def enumAttr(self, enumAttr: str):
        self.__enumAttr = enumAttr

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test_MyMetaClass(self):
        return self.__test_MyMetaClass

    @test_MyMetaClass.setter
    def test_MyMetaClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_MyMetaClass__test_MyMetaClass", None)
        self.__test_MyMetaClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_MyMetaClass0"):
                opp_val = getattr(old_value, "test_MyMetaClass0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_MyMetaClass0"):
                opp_val = getattr(value, "test_MyMetaClass0", None)
                if opp_val is None:
                    setattr(value, "test_MyMetaClass0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_MyMetaClass3(self):
        return self.__test_MyMetaClass3

    @test_MyMetaClass3.setter
    def test_MyMetaClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_MyMetaClass__test_MyMetaClass3", None)
        self.__test_MyMetaClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubpackageMetaClass"):
                opp_val = getattr(old_value, "SubpackageMetaClass", None)
                if opp_val == self:
                    setattr(old_value, "SubpackageMetaClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubpackageMetaClass"):
                opp_val = getattr(value, "SubpackageMetaClass", None)
                setattr(value, "SubpackageMetaClass", self)

    @property
    def test_MyMetaClass0(self):
        return self.__test_MyMetaClass0

    @test_MyMetaClass0.setter
    def test_MyMetaClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_MyMetaClass__test_MyMetaClass0", None)
        self.__test_MyMetaClass0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_MyMetaClass"):
                    opp_val = getattr(item, "test_MyMetaClass", None)
                    
                    if opp_val == self:
                        setattr(item, "test_MyMetaClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_MyMetaClass"):
                    opp_val = getattr(item, "test_MyMetaClass", None)
                    
                    setattr(item, "test_MyMetaClass", self)
                    
