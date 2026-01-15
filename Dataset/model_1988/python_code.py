from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Any:

    pass
class trace_StringAny(Any):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trace_IntAny(Any):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trace_ObjectAny(Any):

    pass
class trace_DecimalAny(Any):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trace_BoolAny(Any):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class trace_EObject:

    pass
class trace_Any(ABC):

    pass
class trace_Trace:

    def __init__(self, name: str, trace_Trace: set["trace_Any"] = None, trace_Trace2: "trace_EObject" = None, trace_Trace4: set["trace_EObject"] = None):
        self.name = name
        self.trace_Trace = trace_Trace if trace_Trace is not None else set()
        self.trace_Trace2 = trace_Trace2
        self.trace_Trace4 = trace_Trace4 if trace_Trace4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trace_Trace(self):
        return self.__trace_Trace

    @trace_Trace.setter
    def trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace", None)
        self.__trace_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Any"):
                    opp_val = getattr(item, "trace_Any", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Any", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Any"):
                    opp_val = getattr(item, "trace_Any", None)
                    
                    setattr(item, "trace_Any", self)
                    

    @property
    def trace_Trace2(self):
        return self.__trace_Trace2

    @trace_Trace2.setter
    def trace_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace2", None)
        self.__trace_Trace2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject"):
                opp_val = getattr(old_value, "trace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject"):
                opp_val = getattr(value, "trace_EObject", None)
                setattr(value, "trace_EObject", self)

    @property
    def trace_Trace4(self):
        return self.__trace_Trace4

    @trace_Trace4.setter
    def trace_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace4", None)
        self.__trace_Trace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject5"):
                    opp_val = getattr(item, "trace_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject5"):
                    opp_val = getattr(item, "trace_EObject5", None)
                    
                    setattr(item, "trace_EObject5", self)
                    
