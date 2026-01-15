from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TraceState(Enum):
    USED = "USED"
    UNUSED = "UNUSED"


############################################
# Definition of Classes
############################################

class viewmodeltrace_Constraint:

    pass
class viewmodeltrace_Variable:

    pass
class viewmodeltrace_StringVariablePair:

    def __init__(self, key: str, viewmodeltrace_StringVariablePair: "viewmodeltrace_VariableInstantiationTrace" = None, viewmodeltrace_StringVariablePair10: "viewmodeltrace_Variable" = None):
        self.key = key
        self.viewmodeltrace_StringVariablePair = viewmodeltrace_StringVariablePair
        self.viewmodeltrace_StringVariablePair10 = viewmodeltrace_StringVariablePair10
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def viewmodeltrace_StringVariablePair10(self):
        return self.__viewmodeltrace_StringVariablePair10

    @viewmodeltrace_StringVariablePair10.setter
    def viewmodeltrace_StringVariablePair10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_StringVariablePair__viewmodeltrace_StringVariablePair10", None)
        self.__viewmodeltrace_StringVariablePair10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_Variable"):
                opp_val = getattr(old_value, "viewmodeltrace_Variable", None)
                if opp_val == self:
                    setattr(old_value, "viewmodeltrace_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_Variable"):
                opp_val = getattr(value, "viewmodeltrace_Variable", None)
                setattr(value, "viewmodeltrace_Variable", self)

    @property
    def viewmodeltrace_StringVariablePair(self):
        return self.__viewmodeltrace_StringVariablePair

    @viewmodeltrace_StringVariablePair.setter
    def viewmodeltrace_StringVariablePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_StringVariablePair__viewmodeltrace_StringVariablePair", None)
        self.__viewmodeltrace_StringVariablePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_VariableInstantiationTrace"):
                opp_val = getattr(old_value, "viewmodeltrace_VariableInstantiationTrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_VariableInstantiationTrace"):
                opp_val = getattr(value, "viewmodeltrace_VariableInstantiationTrace", None)
                if opp_val is None:
                    setattr(value, "viewmodeltrace_VariableInstantiationTrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Trace:

    pass
class viewmodeltrace_ConstraintTrace(Trace):

    pass
class viewmodeltrace_VariableInstantiationTrace(Trace):

    pass
class viewmodeltrace_EObject:

    pass
class MatchArgument:

    pass
class viewmodeltrace_EObjectMatchArgument(MatchArgument):

    pass
class viewmodeltrace_MatchArgument(ABC):

    def __init__(self, parameterName: str, viewmodeltrace_MatchArgument: "viewmodeltrace_MatchArgumentTuple" = None):
        self.parameterName = parameterName
        self.viewmodeltrace_MatchArgument = viewmodeltrace_MatchArgument
        
    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def viewmodeltrace_MatchArgument(self):
        return self.__viewmodeltrace_MatchArgument

    @viewmodeltrace_MatchArgument.setter
    def viewmodeltrace_MatchArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_MatchArgument__viewmodeltrace_MatchArgument", None)
        self.__viewmodeltrace_MatchArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_MatchArgumentTuple"):
                opp_val = getattr(old_value, "viewmodeltrace_MatchArgumentTuple", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_MatchArgumentTuple"):
                opp_val = getattr(value, "viewmodeltrace_MatchArgumentTuple", None)
                if opp_val is None:
                    setattr(value, "viewmodeltrace_MatchArgumentTuple", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewmodeltrace_MatchArgumentTuple:

    pass
class viewmodeltrace_Trace(ABC):

    def __init__(self, traceName: str, state: str, viewmodeltrace_Trace: "viewmodeltrace_ViewModelTrace" = None, viewmodeltrace_Trace6: "viewmodeltrace_MatchArgumentTuple" = None):
        self.traceName = traceName
        self.state = state
        self.viewmodeltrace_Trace = viewmodeltrace_Trace
        self.viewmodeltrace_Trace6 = viewmodeltrace_Trace6
        
    @property
    def traceName(self) -> str:
        return self.__traceName

    @traceName.setter
    def traceName(self, traceName: str):
        self.__traceName = traceName

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def viewmodeltrace_Trace(self):
        return self.__viewmodeltrace_Trace

    @viewmodeltrace_Trace.setter
    def viewmodeltrace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_Trace__viewmodeltrace_Trace", None)
        self.__viewmodeltrace_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_ViewModelTrace2"):
                opp_val = getattr(old_value, "viewmodeltrace_ViewModelTrace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_ViewModelTrace2"):
                opp_val = getattr(value, "viewmodeltrace_ViewModelTrace2", None)
                if opp_val is None:
                    setattr(value, "viewmodeltrace_ViewModelTrace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewmodeltrace_Trace6(self):
        return self.__viewmodeltrace_Trace6

    @viewmodeltrace_Trace6.setter
    def viewmodeltrace_Trace6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_Trace__viewmodeltrace_Trace6", None)
        self.__viewmodeltrace_Trace6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_MatchArgumentTuple7"):
                opp_val = getattr(old_value, "viewmodeltrace_MatchArgumentTuple7", None)
                if opp_val == self:
                    setattr(old_value, "viewmodeltrace_MatchArgumentTuple7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_MatchArgumentTuple7"):
                opp_val = getattr(value, "viewmodeltrace_MatchArgumentTuple7", None)
                setattr(value, "viewmodeltrace_MatchArgumentTuple7", self)

class viewmodeltrace_LogicModel:

    pass
class viewmodeltrace_ViewModelTrace:

    def __init__(self, traceModelId: str, viewmodeltrace_ViewModelTrace: "viewmodeltrace_LogicModel" = None, viewmodeltrace_ViewModelTrace2: set["viewmodeltrace_Trace"] = None):
        self.traceModelId = traceModelId
        self.viewmodeltrace_ViewModelTrace = viewmodeltrace_ViewModelTrace
        self.viewmodeltrace_ViewModelTrace2 = viewmodeltrace_ViewModelTrace2 if viewmodeltrace_ViewModelTrace2 is not None else set()
        
    @property
    def traceModelId(self) -> str:
        return self.__traceModelId

    @traceModelId.setter
    def traceModelId(self, traceModelId: str):
        self.__traceModelId = traceModelId

    @property
    def viewmodeltrace_ViewModelTrace(self):
        return self.__viewmodeltrace_ViewModelTrace

    @viewmodeltrace_ViewModelTrace.setter
    def viewmodeltrace_ViewModelTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_ViewModelTrace__viewmodeltrace_ViewModelTrace", None)
        self.__viewmodeltrace_ViewModelTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewmodeltrace_LogicModel"):
                opp_val = getattr(old_value, "viewmodeltrace_LogicModel", None)
                if opp_val == self:
                    setattr(old_value, "viewmodeltrace_LogicModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewmodeltrace_LogicModel"):
                opp_val = getattr(value, "viewmodeltrace_LogicModel", None)
                setattr(value, "viewmodeltrace_LogicModel", self)

    @property
    def viewmodeltrace_ViewModelTrace2(self):
        return self.__viewmodeltrace_ViewModelTrace2

    @viewmodeltrace_ViewModelTrace2.setter
    def viewmodeltrace_ViewModelTrace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewmodeltrace_ViewModelTrace__viewmodeltrace_ViewModelTrace2", None)
        self.__viewmodeltrace_ViewModelTrace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewmodeltrace_Trace"):
                    opp_val = getattr(item, "viewmodeltrace_Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "viewmodeltrace_Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewmodeltrace_Trace"):
                    opp_val = getattr(item, "viewmodeltrace_Trace", None)
                    
                    setattr(item, "viewmodeltrace_Trace", self)
                    

class viewmodeltrace_JavaObjectMatchArgument(MatchArgument):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value
