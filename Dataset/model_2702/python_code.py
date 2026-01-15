from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sample_C:

    pass
class A:

    pass
class sample_B(A):

    def __init__(self, label: str, sample_B: set["sample_C"] = None):
        self.label = label
        self.sample_B = sample_B if sample_B is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def sample_B(self):
        return self.__sample_B

    @sample_B.setter
    def sample_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_B__sample_B", None)
        self.__sample_B = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_C"):
                    opp_val = getattr(item, "sample_C", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_C"):
                    opp_val = getattr(item, "sample_C", None)
                    
                    setattr(item, "sample_C", self)
                    

class sample_A(ABC):

    def __init__(self, name: str, valid: bool, quantity: int, sample_A: "sample_C" = None):
        self.name = name
        self.valid = valid
        self.quantity = quantity
        self.sample_A = sample_A
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def valid(self) -> bool:
        return self.__valid

    @valid.setter
    def valid(self, valid: bool):
        self.__valid = valid

    @property
    def sample_A(self):
        return self.__sample_A

    @sample_A.setter
    def sample_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_A__sample_A", None)
        self.__sample_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_C2"):
                opp_val = getattr(old_value, "sample_C2", None)
                if opp_val == self:
                    setattr(old_value, "sample_C2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_C2"):
                opp_val = getattr(value, "sample_C2", None)
                setattr(value, "sample_C2", self)
