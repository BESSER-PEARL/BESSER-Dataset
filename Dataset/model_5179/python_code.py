from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MM1_A(ABC):

    def __init__(self, name: str, MM1_A: "MM1_ContainerMM1" = None):
        self.name = name
        self.MM1_A = MM1_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MM1_A(self):
        return self.__MM1_A

    @MM1_A.setter
    def MM1_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MM1_A__MM1_A", None)
        self.__MM1_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MM1_ContainerMM1"):
                opp_val = getattr(old_value, "MM1_ContainerMM1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MM1_ContainerMM1"):
                opp_val = getattr(value, "MM1_ContainerMM1", None)
                if opp_val is None:
                    setattr(value, "MM1_ContainerMM1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MM1_ContainerMM1:

    def __init__(self, aname: int, MM1_ContainerMM12: set["MM1_D"] = None, MM1_ContainerMM1: set["MM1_A"] = None):
        self.aname = aname
        self.MM1_ContainerMM12 = MM1_ContainerMM12 if MM1_ContainerMM12 is not None else set()
        self.MM1_ContainerMM1 = MM1_ContainerMM1 if MM1_ContainerMM1 is not None else set()
        
    @property
    def aname(self) -> int:
        return self.__aname

    @aname.setter
    def aname(self, aname: int):
        self.__aname = aname

    @property
    def MM1_ContainerMM12(self):
        return self.__MM1_ContainerMM12

    @MM1_ContainerMM12.setter
    def MM1_ContainerMM12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MM1_ContainerMM1__MM1_ContainerMM12", None)
        self.__MM1_ContainerMM12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MM1_D"):
                    opp_val = getattr(item, "MM1_D", None)
                    
                    if opp_val == self:
                        setattr(item, "MM1_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MM1_D"):
                    opp_val = getattr(item, "MM1_D", None)
                    
                    setattr(item, "MM1_D", self)
                    

    @property
    def MM1_ContainerMM1(self):
        return self.__MM1_ContainerMM1

    @MM1_ContainerMM1.setter
    def MM1_ContainerMM1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MM1_ContainerMM1__MM1_ContainerMM1", None)
        self.__MM1_ContainerMM1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MM1_A"):
                    opp_val = getattr(item, "MM1_A", None)
                    
                    if opp_val == self:
                        setattr(item, "MM1_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MM1_A"):
                    opp_val = getattr(item, "MM1_A", None)
                    
                    setattr(item, "MM1_A", self)
                    

class A:

    pass
class MM1_C(A):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class MM1_B(A):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class MM1_D:

    pass