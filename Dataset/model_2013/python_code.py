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

class TransientObject:

    pass
class trace_DynamicTransientObject(TransientObject):

    pass
class trace_StaticTransientObject(TransientObject):

    pass
class ParameterList:

    pass
class trace_LeafParameterList(ParameterList):

    pass
class trace_CompositParameterList(ParameterList):

    def __init__(self, paramtervaluesOrder: int, trace_CompositParameterList: set["trace_ParameterList"] = None):
        self.paramtervaluesOrder = paramtervaluesOrder
        self.trace_CompositParameterList = trace_CompositParameterList if trace_CompositParameterList is not None else set()
        
    @property
    def paramtervaluesOrder(self) -> int:
        return self.__paramtervaluesOrder

    @paramtervaluesOrder.setter
    def paramtervaluesOrder(self, paramtervaluesOrder: int):
        self.__paramtervaluesOrder = paramtervaluesOrder

    @property
    def trace_CompositParameterList(self):
        return self.__trace_CompositParameterList

    @trace_CompositParameterList.setter
    def trace_CompositParameterList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_CompositParameterList__trace_CompositParameterList", None)
        self.__trace_CompositParameterList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ParameterList84"):
                    opp_val = getattr(item, "trace_ParameterList84", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ParameterList84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ParameterList84"):
                    opp_val = getattr(item, "trace_ParameterList84", None)
                    
                    setattr(item, "trace_ParameterList84", self)
                    

class trace_EClass:

    pass
class LiteralValue:

    pass
class trace_LiteralString(LiteralValue):

    def __init__(self, stringvalue: str):
        self.stringvalue = stringvalue
        
    @property
    def stringvalue(self) -> str:
        return self.__stringvalue

    @stringvalue.setter
    def stringvalue(self, stringvalue: str):
        self.__stringvalue = stringvalue

class trace_StepSpec(ABC):

    pass
class ObjectState:

    pass
class trace_CompositeObjectState(ObjectState):

    def __init__(self, objectstatesOrder: int, trace_CompositeObjectState: set["trace_ObjectState"] = None):
        self.objectstatesOrder = objectstatesOrder
        self.trace_CompositeObjectState = trace_CompositeObjectState if trace_CompositeObjectState is not None else set()
        
    @property
    def objectstatesOrder(self) -> int:
        return self.__objectstatesOrder

    @objectstatesOrder.setter
    def objectstatesOrder(self, objectstatesOrder: int):
        self.__objectstatesOrder = objectstatesOrder

    @property
    def trace_CompositeObjectState(self):
        return self.__trace_CompositeObjectState

    @trace_CompositeObjectState.setter
    def trace_CompositeObjectState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_CompositeObjectState__trace_CompositeObjectState", None)
        self.__trace_CompositeObjectState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ObjectState79"):
                    opp_val = getattr(item, "trace_ObjectState79", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ObjectState79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ObjectState79"):
                    opp_val = getattr(item, "trace_ObjectState79", None)
                    
                    setattr(item, "trace_ObjectState79", self)
                    

class trace_LeafObjectState(ObjectState):

    pass
class trace_EStructuralFeature:

    pass
class trace_LiteralFloat(LiteralValue):

    def __init__(self, floatvalue: float):
        self.floatvalue = floatvalue
        
    @property
    def floatvalue(self) -> float:
        return self.__floatvalue

    @floatvalue.setter
    def floatvalue(self, floatvalue: float):
        self.__floatvalue = floatvalue

class trace_LiteralInteger(LiteralValue):

    def __init__(self, intvalue: int):
        self.intvalue = intvalue
        
    @property
    def intvalue(self) -> int:
        return self.__intvalue

    @intvalue.setter
    def intvalue(self, intvalue: int):
        self.__intvalue = intvalue

class trace_LiteralBoolean(LiteralValue):

    def __init__(self, boolvalue: bool):
        self.boolvalue = boolvalue
        
    @property
    def boolvalue(self) -> bool:
        return self.__boolvalue

    @boolvalue.setter
    def boolvalue(self, boolvalue: bool):
        self.__boolvalue = boolvalue

class trace_TransientObjectState:

    pass
class trace_EObject:

    pass
class trace_PatternOccurrenceStepData:

    pass
class StepSpec:

    pass
class Step:

    pass
class trace_PatternOcurrence(Step):

    def __init__(self, repet: int, trace_PatternOcurrence: "trace_StepPattern" = None, trace_PatternOcurrence45: set["trace_PatternOccurrenceStepData"] = None):
        self.repet = repet
        self.trace_PatternOcurrence = trace_PatternOcurrence
        self.trace_PatternOcurrence45 = trace_PatternOcurrence45 if trace_PatternOcurrence45 is not None else set()
        
    @property
    def repet(self) -> int:
        return self.__repet

    @repet.setter
    def repet(self, repet: int):
        self.__repet = repet

    @property
    def trace_PatternOcurrence45(self):
        return self.__trace_PatternOcurrence45

    @trace_PatternOcurrence45.setter
    def trace_PatternOcurrence45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_PatternOcurrence__trace_PatternOcurrence45", None)
        self.__trace_PatternOcurrence45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_PatternOccurrenceStepData"):
                    opp_val = getattr(item, "trace_PatternOccurrenceStepData", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_PatternOccurrenceStepData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_PatternOccurrenceStepData"):
                    opp_val = getattr(item, "trace_PatternOccurrenceStepData", None)
                    
                    setattr(item, "trace_PatternOccurrenceStepData", self)
                    

    @property
    def trace_PatternOcurrence(self):
        return self.__trace_PatternOcurrence

    @trace_PatternOcurrence.setter
    def trace_PatternOcurrence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_PatternOcurrence__trace_PatternOcurrence", None)
        self.__trace_PatternOcurrence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_StepPattern43"):
                opp_val = getattr(old_value, "trace_StepPattern43", None)
                if opp_val == self:
                    setattr(old_value, "trace_StepPattern43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_StepPattern43"):
                opp_val = getattr(value, "trace_StepPattern43", None)
                setattr(value, "trace_StepPattern43", self)

class trace_NormalStep(StepSpec, Step):

    pass
class trace_Trace:

    pass
class trace_TransientObject(ABC):

    pass
class trace_Value(ABC):

    pass
class Value:

    pass
class trace_RefValue(Value):

    pass
class trace_LiteralValue(Value):

    pass
class trace_ParameterList(ABC):

    pass
class trace_ParameterValue:

    def __init__(self, DirectionKind: str, trace_ParameterValue: "trace_Trace" = None, trace_ParameterValue68: set["trace_Value"] = None, trace_ParameterValue87: "trace_ParameterList" = None):
        self.DirectionKind = DirectionKind
        self.trace_ParameterValue = trace_ParameterValue
        self.trace_ParameterValue68 = trace_ParameterValue68 if trace_ParameterValue68 is not None else set()
        self.trace_ParameterValue87 = trace_ParameterValue87
        
    @property
    def DirectionKind(self) -> str:
        return self.__DirectionKind

    @DirectionKind.setter
    def DirectionKind(self, DirectionKind: str):
        self.__DirectionKind = DirectionKind

    @property
    def trace_ParameterValue68(self):
        return self.__trace_ParameterValue68

    @trace_ParameterValue68.setter
    def trace_ParameterValue68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ParameterValue__trace_ParameterValue68", None)
        self.__trace_ParameterValue68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Value69"):
                    opp_val = getattr(item, "trace_Value69", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Value69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Value69"):
                    opp_val = getattr(item, "trace_Value69", None)
                    
                    setattr(item, "trace_Value69", self)
                    

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
            if hasattr(old_value, "trace_Trace16"):
                opp_val = getattr(old_value, "trace_Trace16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace16"):
                opp_val = getattr(value, "trace_Trace16", None)
                if opp_val is None:
                    setattr(value, "trace_Trace16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_ParameterValue87(self):
        return self.__trace_ParameterValue87

    @trace_ParameterValue87.setter
    def trace_ParameterValue87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ParameterValue__trace_ParameterValue87", None)
        self.__trace_ParameterValue87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_ParameterList86"):
                opp_val = getattr(old_value, "trace_ParameterList86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_ParameterList86"):
                opp_val = getattr(value, "trace_ParameterList86", None)
                if opp_val is None:
                    setattr(value, "trace_ParameterList86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_Step(ABC):

    pass
class trace_RepeatingStep(StepSpec):

    pass
class trace_ObjectState(ABC):

    pass
class trace_StepPattern:

    pass
class trace_StepType:

    def __init__(self, stepName: str, trace_StepType: "trace_Trace" = None, trace_StepType59: "trace_StepSpec" = None):
        self.stepName = stepName
        self.trace_StepType = trace_StepType
        self.trace_StepType59 = trace_StepType59
        
    @property
    def stepName(self) -> str:
        return self.__stepName

    @stepName.setter
    def stepName(self, stepName: str):
        self.__stepName = stepName

    @property
    def trace_StepType(self):
        return self.__trace_StepType

    @trace_StepType.setter
    def trace_StepType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_StepType__trace_StepType", None)
        self.__trace_StepType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace4"):
                opp_val = getattr(old_value, "trace_Trace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace4"):
                opp_val = getattr(value, "trace_Trace4", None)
                if opp_val is None:
                    setattr(value, "trace_Trace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_StepType59(self):
        return self.__trace_StepType59

    @trace_StepType59.setter
    def trace_StepType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_StepType__trace_StepType59", None)
        self.__trace_StepType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_StepSpec"):
                opp_val = getattr(old_value, "trace_StepSpec", None)
                if opp_val == self:
                    setattr(old_value, "trace_StepSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_StepSpec"):
                opp_val = getattr(value, "trace_StepSpec", None)
                setattr(value, "trace_StepSpec", self)

class trace_State:

    pass