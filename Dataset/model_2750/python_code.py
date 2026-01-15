from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simplea_B(ABC):

    pass
class simplea_A:

    def __init__(self, name: str, simplea_A: set["simplea_B"] = None):
        self.name = name
        self.simplea_A = simplea_A if simplea_A is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplea_A(self):
        return self.__simplea_A

    @simplea_A.setter
    def simplea_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplea_A__simplea_A", None)
        self.__simplea_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplea_B"):
                    opp_val = getattr(item, "simplea_B", None)
                    
                    if opp_val == self:
                        setattr(item, "simplea_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplea_B"):
                    opp_val = getattr(item, "simplea_B", None)
                    
                    setattr(item, "simplea_B", self)
                    
