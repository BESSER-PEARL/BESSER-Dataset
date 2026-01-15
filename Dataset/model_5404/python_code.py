from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"


############################################
# Definition of Classes
############################################

class Element:

    pass
class UML2WithID_Operation(Element):

    pass
class UML2WithID_Element(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class UML2WithID_Parameter(Element):

    def __init__(self, direction: str, UML2WithID_Parameter: "UML2WithID_Operation" = None):
        self.direction = direction
        self.UML2WithID_Parameter = UML2WithID_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def UML2WithID_Parameter(self):
        return self.__UML2WithID_Parameter

    @UML2WithID_Parameter.setter
    def UML2WithID_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter", None)
        self.__UML2WithID_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Operation"):
                opp_val = getattr(old_value, "UML2WithID_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Operation"):
                opp_val = getattr(value, "UML2WithID_Operation", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
