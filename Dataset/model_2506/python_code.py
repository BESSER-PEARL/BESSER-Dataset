from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnumExample(Enum):
    value1 = "value1"
    value2 = "value2"
    value3 = "value3"


############################################
# Definition of Classes
############################################

class dummy_C:

    def __init__(self, k: float, dummy_C: "dummy_B" = None):
        self.k = k
        self.dummy_C = dummy_C
        
    @property
    def k(self) -> float:
        return self.__k

    @k.setter
    def k(self, k: float):
        self.__k = k

    @property
    def dummy_C(self):
        return self.__dummy_C

    @dummy_C.setter
    def dummy_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_C__dummy_C", None)
        self.__dummy_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_B6"):
                opp_val = getattr(old_value, "dummy_B6", None)
                if opp_val == self:
                    setattr(old_value, "dummy_B6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_B6"):
                opp_val = getattr(value, "dummy_B6", None)
                setattr(value, "dummy_B6", self)

class dummy_E(ABC):

    def __init__(self, eName: str, dummy_E: "dummy_A" = None):
        self.eName = eName
        self.dummy_E = dummy_E
        
    @property
    def eName(self) -> str:
        return self.__eName

    @eName.setter
    def eName(self, eName: str):
        self.__eName = eName

    @property
    def dummy_E(self):
        return self.__dummy_E

    @dummy_E.setter
    def dummy_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_E__dummy_E", None)
        self.__dummy_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_A4"):
                opp_val = getattr(old_value, "dummy_A4", None)
                if opp_val == self:
                    setattr(old_value, "dummy_A4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_A4"):
                opp_val = getattr(value, "dummy_A4", None)
                setattr(value, "dummy_A4", self)

class dummy_D:

    def __init__(self, name: str, l: float, m: float, dummy_D: "dummy_A" = None):
        self.name = name
        self.l = l
        self.m = m
        self.dummy_D = dummy_D
        
    @property
    def m(self) -> float:
        return self.__m

    @m.setter
    def m(self, m: float):
        self.__m = m

    @property
    def l(self) -> float:
        return self.__l

    @l.setter
    def l(self, l: float):
        self.__l = l

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dummy_D(self):
        return self.__dummy_D

    @dummy_D.setter
    def dummy_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_D__dummy_D", None)
        self.__dummy_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_A2"):
                opp_val = getattr(old_value, "dummy_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_A2"):
                opp_val = getattr(value, "dummy_A2", None)
                if opp_val is None:
                    setattr(value, "dummy_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dummy_B:

    def __init__(self, y: float, z: float, dummy_B: "dummy_A" = None, dummy_B6: "dummy_C" = None):
        self.y = y
        self.z = z
        self.dummy_B = dummy_B
        self.dummy_B6 = dummy_B6
        
    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float):
        self.__z = z

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def dummy_B(self):
        return self.__dummy_B

    @dummy_B.setter
    def dummy_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_B__dummy_B", None)
        self.__dummy_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_A"):
                opp_val = getattr(old_value, "dummy_A", None)
                if opp_val == self:
                    setattr(old_value, "dummy_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_A"):
                opp_val = getattr(value, "dummy_A", None)
                setattr(value, "dummy_A", self)

    @property
    def dummy_B6(self):
        return self.__dummy_B6

    @dummy_B6.setter
    def dummy_B6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_B__dummy_B6", None)
        self.__dummy_B6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_C"):
                opp_val = getattr(old_value, "dummy_C", None)
                if opp_val == self:
                    setattr(old_value, "dummy_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_C"):
                opp_val = getattr(value, "dummy_C", None)
                setattr(value, "dummy_C", self)

class dummy_A:

    def __init__(self, x: float, en: str, dummy_A: "dummy_B" = None, dummy_A2: set["dummy_D"] = None, dummy_A4: "dummy_E" = None):
        self.x = x
        self.en = en
        self.dummy_A = dummy_A
        self.dummy_A2 = dummy_A2 if dummy_A2 is not None else set()
        self.dummy_A4 = dummy_A4
        
    @property
    def en(self) -> str:
        return self.__en

    @en.setter
    def en(self, en: str):
        self.__en = en

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def dummy_A(self):
        return self.__dummy_A

    @dummy_A.setter
    def dummy_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_A__dummy_A", None)
        self.__dummy_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_B"):
                opp_val = getattr(old_value, "dummy_B", None)
                if opp_val == self:
                    setattr(old_value, "dummy_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_B"):
                opp_val = getattr(value, "dummy_B", None)
                setattr(value, "dummy_B", self)

    @property
    def dummy_A2(self):
        return self.__dummy_A2

    @dummy_A2.setter
    def dummy_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_A__dummy_A2", None)
        self.__dummy_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dummy_D"):
                    opp_val = getattr(item, "dummy_D", None)
                    
                    if opp_val == self:
                        setattr(item, "dummy_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dummy_D"):
                    opp_val = getattr(item, "dummy_D", None)
                    
                    setattr(item, "dummy_D", self)
                    

    @property
    def dummy_A4(self):
        return self.__dummy_A4

    @dummy_A4.setter
    def dummy_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dummy_A__dummy_A4", None)
        self.__dummy_A4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy_E"):
                opp_val = getattr(old_value, "dummy_E", None)
                if opp_val == self:
                    setattr(old_value, "dummy_E", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy_E"):
                opp_val = getattr(value, "dummy_E", None)
                setattr(value, "dummy_E", self)

class E:

    pass
class dummy_G(E):

    def __init__(self, gString: str):
        self.gString = gString
        
    @property
    def gString(self) -> str:
        return self.__gString

    @gString.setter
    def gString(self, gString: str):
        self.__gString = gString

class dummy_F(E):

    def __init__(self, fString: str, fDouble: float):
        self.fString = fString
        self.fDouble = fDouble
        
    @property
    def fString(self) -> str:
        return self.__fString

    @fString.setter
    def fString(self, fString: str):
        self.__fString = fString

    @property
    def fDouble(self) -> float:
        return self.__fDouble

    @fDouble.setter
    def fDouble(self, fDouble: float):
        self.__fDouble = fDouble
