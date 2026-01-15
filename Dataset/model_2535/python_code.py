from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_EClass:

    pass
class test_EClassToAMap:

    pass
class test_EClassToEStringMap:

    def __init__(self, value: str, test_EClassToEStringMap: "test_C" = None, test_EClassToEStringMap16: "test_EClass" = None):
        self.value = value
        self.test_EClassToEStringMap = test_EClassToEStringMap
        self.test_EClassToEStringMap16 = test_EClassToEStringMap16
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test_EClassToEStringMap(self):
        return self.__test_EClassToEStringMap

    @test_EClassToEStringMap.setter
    def test_EClassToEStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClassToEStringMap__test_EClassToEStringMap", None)
        self.__test_EClassToEStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_C9"):
                opp_val = getattr(old_value, "test_C9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_C9"):
                opp_val = getattr(value, "test_C9", None)
                if opp_val is None:
                    setattr(value, "test_C9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_EClassToEStringMap16(self):
        return self.__test_EClassToEStringMap16

    @test_EClassToEStringMap16.setter
    def test_EClassToEStringMap16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_EClassToEStringMap__test_EClassToEStringMap16", None)
        self.__test_EClassToEStringMap16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_EClass"):
                opp_val = getattr(old_value, "test_EClass", None)
                if opp_val == self:
                    setattr(old_value, "test_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_EClass"):
                opp_val = getattr(value, "test_EClass", None)
                setattr(value, "test_EClass", self)

class test_D:

    def __init__(self, x: str, yList: int, test_D: "test_C" = None):
        self.x = x
        self.yList = yList
        self.test_D = test_D
        
    @property
    def yList(self) -> int:
        return self.__yList

    @yList.setter
    def yList(self, yList: int):
        self.__yList = yList

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def test_D(self):
        return self.__test_D

    @test_D.setter
    def test_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_D__test_D", None)
        self.__test_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_C7"):
                opp_val = getattr(old_value, "test_C7", None)
                if opp_val == self:
                    setattr(old_value, "test_C7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_C7"):
                opp_val = getattr(value, "test_C7", None)
                setattr(value, "test_C7", self)

class test_C:

    pass
class test_B:

    pass
class test_A:

    pass