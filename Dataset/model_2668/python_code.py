from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class B:

    pass
class minher_E(B):

    pass
class minher_A:

    pass
class minher_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class minher_G(Named):

    pass
class minher_C(Named):

    pass
class minher_B(Named):

    def __init__(self, value: str, minher_B: "minher_A" = None, minher_B2: set["minher_G"] = None, minher_B4: set["minher_C"] = None):
        self.value = value
        self.minher_B = minher_B
        self.minher_B2 = minher_B2 if minher_B2 is not None else set()
        self.minher_B4 = minher_B4 if minher_B4 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def minher_B(self):
        return self.__minher_B

    @minher_B.setter
    def minher_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minher_B__minher_B", None)
        self.__minher_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minher_A"):
                opp_val = getattr(old_value, "minher_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minher_A"):
                opp_val = getattr(value, "minher_A", None)
                if opp_val is None:
                    setattr(value, "minher_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minher_B2(self):
        return self.__minher_B2

    @minher_B2.setter
    def minher_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minher_B__minher_B2", None)
        self.__minher_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minher_G"):
                    opp_val = getattr(item, "minher_G", None)
                    
                    if opp_val == self:
                        setattr(item, "minher_G", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minher_G"):
                    opp_val = getattr(item, "minher_G", None)
                    
                    setattr(item, "minher_G", self)
                    

    @property
    def minher_B4(self):
        return self.__minher_B4

    @minher_B4.setter
    def minher_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minher_B__minher_B4", None)
        self.__minher_B4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minher_C"):
                    opp_val = getattr(item, "minher_C", None)
                    
                    if opp_val == self:
                        setattr(item, "minher_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minher_C"):
                    opp_val = getattr(item, "minher_C", None)
                    
                    setattr(item, "minher_C", self)
                    
