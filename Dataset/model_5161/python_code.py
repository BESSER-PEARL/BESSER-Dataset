from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RootIn:

    pass
class in_B(RootIn):

    pass
class in_A(RootIn):

    def __init__(self, name: str, in_A: set["in_B"] = None, in_A3: "in_B" = None):
        self.name = name
        self.in_A = in_A if in_A is not None else set()
        self.in_A3 = in_A3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def in_A(self):
        return self.__in_A

    @in_A.setter
    def in_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_in_A__in_A", None)
        self.__in_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "in_B"):
                    opp_val = getattr(item, "in_B", None)
                    
                    if opp_val == self:
                        setattr(item, "in_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "in_B"):
                    opp_val = getattr(item, "in_B", None)
                    
                    setattr(item, "in_B", self)
                    

    @property
    def in_A3(self):
        return self.__in_A3

    @in_A3.setter
    def in_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_in_A__in_A3", None)
        self.__in_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in_B2"):
                opp_val = getattr(old_value, "in_B2", None)
                if opp_val == self:
                    setattr(old_value, "in_B2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in_B2"):
                opp_val = getattr(value, "in_B2", None)
                setattr(value, "in_B2", self)

class in_RootIn(ABC):

    pass