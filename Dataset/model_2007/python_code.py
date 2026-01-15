from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParamterKindEnum(Enum):
    IN = "IN"
    INOUT = "INOUT"
    OUT = "OUT"
    RETURN = "RETURN"


############################################
# Definition of Classes
############################################

class Step:

    pass
class trace_SmallStep(Step):

    pass
class Value:

    pass
class trace_LiteralValue(Value):

    pass
class trace_RefValue(Value):

    pass
class trace_BigStep(Step):

    pass
class trace_ParameterValue:

    def __init__(self, DirectionKind: str, trace_ParameterValue: "trace_Step" = None, trace_ParameterValue27: set["trace_Value"] = None):
        self.DirectionKind = DirectionKind
        self.trace_ParameterValue = trace_ParameterValue
        self.trace_ParameterValue27 = trace_ParameterValue27 if trace_ParameterValue27 is not None else set()
        
    @property
    def DirectionKind(self) -> str:
        return self.__DirectionKind

    @DirectionKind.setter
    def DirectionKind(self, DirectionKind: str):
        self.__DirectionKind = DirectionKind

    @property
    def trace_ParameterValue(self):
        return self.__trace_ParameterValue

    @trace_ParameterValue.setter
    def trace_ParameterValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ParameterValue__trace_ParameterValue", None)
        self.__trace_ParameterValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Step13"):
                opp_val = getattr(old_value, "trace_Step13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Step13"):
                opp_val = getattr(value, "trace_Step13", None)
                if opp_val is None:
                    setattr(value, "trace_Step13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_ParameterValue27(self):
        return self.__trace_ParameterValue27

    @trace_ParameterValue27.setter
    def trace_ParameterValue27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ParameterValue__trace_ParameterValue27", None)
        self.__trace_ParameterValue27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Value28"):
                    opp_val = getattr(item, "trace_Value28", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Value28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Value28"):
                    opp_val = getattr(item, "trace_Value28", None)
                    
                    setattr(item, "trace_Value28", self)
                    

class trace_Value(ABC):

    pass
class trace_TracedObject:

    pass
class trace_ObjectState:

    pass
class trace_ModelState:

    pass
class trace_Step(ABC):

    pass
class trace_Trace:

    pass