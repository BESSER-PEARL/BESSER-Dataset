from datetime import datetime, date, time
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

class UML2_MultiplicityElement:

    def __init__(self, lower: int):
        self.lower = lower
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class Pin:

    pass
class UML2_InputPin(Pin):

    pass
class UML2_OutputPin(Pin):

    pass
class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class MultiplicityElement:

    pass
class UML2_Pin(MultiplicityElement):

    pass
class UML2_Parameter(MultiplicityElement):

    def __init__(self, direction: str, UML2_Parameter: "UML2_Operation" = None):
        self.direction = direction
        self.UML2_Parameter = UML2_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def UML2_Parameter(self):
        return self.__UML2_Parameter

    @UML2_Parameter.setter
    def UML2_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter", None)
        self.__UML2_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Operation"):
                opp_val = getattr(old_value, "UML2_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Operation"):
                opp_val = getattr(value, "UML2_Operation", None)
                if opp_val is None:
                    setattr(value, "UML2_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_Variable(MultiplicityElement):

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class UML2_Operation(MultiplicityElement):

    pass
class UML2_StructuralFeature(MultiplicityElement):

    pass