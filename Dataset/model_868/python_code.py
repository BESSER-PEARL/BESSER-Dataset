from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class PseudostateKind(Enum):
    initial = "initial"
    join = "join"
    fork = "fork"
    terminate = "terminate"
    entrypoint = "entrypoint"
    exitpoint = "exitpoint"


############################################
# Definition of Classes
############################################

class EventOccurrence:

    pass
class statemachines_CompletionEventOccurrence:

    pass
class statemachines_EventOccurrence:

    pass
class AttributeValue:

    pass
class statemachines_IntegerAttributeValue(AttributeValue):

    def __init__(self, value: str, statemachines_IntegerAttributeValue: "statemachines_IntegerAttribute" = None):
        self.value = value
        self.statemachines_IntegerAttributeValue = statemachines_IntegerAttributeValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def statemachines_IntegerAttributeValue(self):
        return self.__statemachines_IntegerAttributeValue

    @statemachines_IntegerAttributeValue.setter
    def statemachines_IntegerAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_IntegerAttributeValue__statemachines_IntegerAttributeValue", None)
        self.__statemachines_IntegerAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_IntegerAttribute"):
                opp_val = getattr(old_value, "statemachines_IntegerAttribute", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_IntegerAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_IntegerAttribute"):
                opp_val = getattr(value, "statemachines_IntegerAttribute", None)
                setattr(value, "statemachines_IntegerAttribute", self)

class statemachines_StringAttributeValue(AttributeValue):

    def __init__(self, value: str, statemachines_StringAttributeValue: "statemachines_StringAttribute" = None):
        self.value = value
        self.statemachines_StringAttributeValue = statemachines_StringAttributeValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def statemachines_StringAttributeValue(self):
        return self.__statemachines_StringAttributeValue

    @statemachines_StringAttributeValue.setter
    def statemachines_StringAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StringAttributeValue__statemachines_StringAttributeValue", None)
        self.__statemachines_StringAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_StringAttribute"):
                opp_val = getattr(old_value, "statemachines_StringAttribute", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_StringAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_StringAttribute"):
                opp_val = getattr(value, "statemachines_StringAttribute", None)
                setattr(value, "statemachines_StringAttribute", self)

class statemachines_BooleanAttributeValue(AttributeValue):

    def __init__(self, value: str, statemachines_BooleanAttributeValue: "statemachines_BooleanAttribute" = None):
        self.value = value
        self.statemachines_BooleanAttributeValue = statemachines_BooleanAttributeValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def statemachines_BooleanAttributeValue(self):
        return self.__statemachines_BooleanAttributeValue

    @statemachines_BooleanAttributeValue.setter
    def statemachines_BooleanAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_BooleanAttributeValue__statemachines_BooleanAttributeValue", None)
        self.__statemachines_BooleanAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_BooleanAttribute"):
                opp_val = getattr(old_value, "statemachines_BooleanAttribute", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_BooleanAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_BooleanAttribute"):
                opp_val = getattr(value, "statemachines_BooleanAttribute", None)
                setattr(value, "statemachines_BooleanAttribute", self)

class statemachines_CallEventOccurrence(EventOccurrence):

    pass
class State:

    pass
class statemachines_FinalState(State):

    pass
class statemachines_AttributeValue(ABC):

    pass
class Behavior:

    pass
class statemachines_OperationBehavior(Behavior):

    pass
class statemachines_SignalEventOccurrence(EventOccurrence):

    pass
class Vertex:

    pass
class statemachines_State(Vertex):

    def __init__(self, isEntryCompleted: bool, isDoActivityCompleted: bool, isExitCompleted: bool, 46: "statemachines_Pseudostate" = None, 48: set["statemachines_Region"] = None, statemachines_State: "statemachines_Behavior" = None, statemachines_State52: "statemachines_Behavior" = None, statemachines_State55: "statemachines_Behavior" = None, 33: "statemachines_Region" = None, statemachines_State58: set["statemachines_Trigger"] = None, 60: set["statemachines_Pseudostate"] = None, statemachines_State85: "statemachines_CompletionEventOccurrence" = None):
        self.isEntryCompleted = isEntryCompleted
        self.isDoActivityCompleted = isDoActivityCompleted
        self.isExitCompleted = isExitCompleted
        self.46 = 46
        self.48 = 48 if 48 is not None else set()
        self.statemachines_State = statemachines_State
        self.statemachines_State52 = statemachines_State52
        self.statemachines_State55 = statemachines_State55
        self.33 = 33
        self.statemachines_State58 = statemachines_State58 if statemachines_State58 is not None else set()
        self.60 = 60 if 60 is not None else set()
        self.statemachines_State85 = statemachines_State85
        
    @property
    def isExitCompleted(self) -> bool:
        return self.__isExitCompleted

    @isExitCompleted.setter
    def isExitCompleted(self, isExitCompleted: bool):
        self.__isExitCompleted = isExitCompleted

    @property
    def isDoActivityCompleted(self) -> bool:
        return self.__isDoActivityCompleted

    @isDoActivityCompleted.setter
    def isDoActivityCompleted(self, isDoActivityCompleted: bool):
        self.__isDoActivityCompleted = isDoActivityCompleted

    @property
    def isEntryCompleted(self) -> bool:
        return self.__isEntryCompleted

    @isEntryCompleted.setter
    def isEntryCompleted(self, isEntryCompleted: bool):
        self.__isEntryCompleted = isEntryCompleted

    @property
    def 33(self):
        return self.__33

    @33.setter
    def 33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__33", None)
        self.__33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "32"):
                opp_val = getattr(old_value, "32", None)
                if opp_val == self:
                    setattr(old_value, "32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "32"):
                opp_val = getattr(value, "32", None)
                setattr(value, "32", self)

    @property
    def statemachines_State85(self):
        return self.__statemachines_State85

    @statemachines_State85.setter
    def statemachines_State85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State85", None)
        self.__statemachines_State85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_CompletionEventOccurrence"):
                opp_val = getattr(old_value, "statemachines_CompletionEventOccurrence", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_CompletionEventOccurrence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_CompletionEventOccurrence"):
                opp_val = getattr(value, "statemachines_CompletionEventOccurrence", None)
                setattr(value, "statemachines_CompletionEventOccurrence", self)

    @property
    def statemachines_State55(self):
        return self.__statemachines_State55

    @statemachines_State55.setter
    def statemachines_State55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State55", None)
        self.__statemachines_State55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior56"):
                opp_val = getattr(old_value, "statemachines_Behavior56", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior56"):
                opp_val = getattr(value, "statemachines_Behavior56", None)
                setattr(value, "statemachines_Behavior56", self)

    @property
    def statemachines_State(self):
        return self.__statemachines_State

    @statemachines_State.setter
    def statemachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State", None)
        self.__statemachines_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior"):
                opp_val = getattr(old_value, "statemachines_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior"):
                opp_val = getattr(value, "statemachines_Behavior", None)
                setattr(value, "statemachines_Behavior", self)

    @property
    def 46(self):
        return self.__46

    @46.setter
    def 46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__46", None)
        self.__46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "45"):
                opp_val = getattr(old_value, "45", None)
                if opp_val == self:
                    setattr(old_value, "45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "45"):
                opp_val = getattr(value, "45", None)
                setattr(value, "45", self)

    @property
    def 48(self):
        return self.__48

    @48.setter
    def 48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__48", None)
        self.__48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "49"):
                    opp_val = getattr(item, "49", None)
                    
                    if opp_val == self:
                        setattr(item, "49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "49"):
                    opp_val = getattr(item, "49", None)
                    
                    setattr(item, "49", self)
                    

    @property
    def statemachines_State52(self):
        return self.__statemachines_State52

    @statemachines_State52.setter
    def statemachines_State52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State52", None)
        self.__statemachines_State52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior53"):
                opp_val = getattr(old_value, "statemachines_Behavior53", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior53"):
                opp_val = getattr(value, "statemachines_Behavior53", None)
                setattr(value, "statemachines_Behavior53", self)

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__60", None)
        self.__60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "61"):
                    opp_val = getattr(item, "61", None)
                    
                    if opp_val == self:
                        setattr(item, "61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "61"):
                    opp_val = getattr(item, "61", None)
                    
                    setattr(item, "61", self)
                    

    @property
    def statemachines_State58(self):
        return self.__statemachines_State58

    @statemachines_State58.setter
    def statemachines_State58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State58", None)
        self.__statemachines_State58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_Trigger"):
                    opp_val = getattr(item, "statemachines_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Trigger"):
                    opp_val = getattr(item, "statemachines_Trigger", None)
                    
                    setattr(item, "statemachines_Trigger", self)
                    

class statemachines_Pseudostate(Vertex):

    def __init__(self, kind: str, 45: "statemachines_State" = None, 61: "statemachines_State" = None):
        self.kind = kind
        self.45 = 45
        self.61 = 61
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 45(self):
        return self.__45

    @45.setter
    def 45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__45", None)
        self.__45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "46"):
                opp_val = getattr(old_value, "46", None)
                if opp_val == self:
                    setattr(old_value, "46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "46"):
                opp_val = getattr(value, "46", None)
                setattr(value, "46", self)

    @property
    def 61(self):
        return self.__61

    @61.setter
    def 61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__61", None)
        self.__61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "60"):
                opp_val = getattr(old_value, "60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "60"):
                opp_val = getattr(value, "60", None)
                if opp_val is None:
                    setattr(value, "60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachines_Constraint(ABC):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Attribute:

    pass
class statemachines_StringAttribute(Attribute):

    pass
class statemachines_IntegerAttribute(Attribute):

    pass
class statemachines_BooleanAttribute(Attribute):

    pass
class EventType:

    pass
class statemachines_CallEventType(EventType):

    pass
class statemachines_SignalEventType(EventType):

    pass
class statemachines_EventType(ABC):

    pass
class NamedElement:

    pass
class statemachines_Vertex(NamedElement):

    pass
class statemachines_Behavior(NamedElement):

    pass
class statemachines_Trigger(NamedElement):

    pass
class statemachines_Transition(NamedElement):

    def __init__(self, kind: str, 27: "statemachines_Region" = None, 40: "statemachines_Vertex" = None, 43: "statemachines_Vertex" = None, statemachines_Transition74: "statemachines_Behavior" = None, 63: "statemachines_Vertex" = None, 66: "statemachines_Vertex" = None, statemachines_Transition: set["statemachines_Trigger"] = None, 71: "statemachines_Region" = None):
        self.kind = kind
        self.27 = 27
        self.40 = 40
        self.43 = 43
        self.statemachines_Transition74 = statemachines_Transition74
        self.63 = 63
        self.66 = 66
        self.statemachines_Transition = statemachines_Transition if statemachines_Transition is not None else set()
        self.71 = 71
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 63(self):
        return self.__63

    @63.setter
    def 63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__63", None)
        self.__63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "64"):
                opp_val = getattr(old_value, "64", None)
                if opp_val == self:
                    setattr(old_value, "64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "64"):
                opp_val = getattr(value, "64", None)
                setattr(value, "64", self)

    @property
    def 43(self):
        return self.__43

    @43.setter
    def 43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__43", None)
        self.__43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "42"):
                opp_val = getattr(old_value, "42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "42"):
                opp_val = getattr(value, "42", None)
                if opp_val is None:
                    setattr(value, "42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 66(self):
        return self.__66

    @66.setter
    def 66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__66", None)
        self.__66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "67"):
                opp_val = getattr(old_value, "67", None)
                if opp_val == self:
                    setattr(old_value, "67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "67"):
                opp_val = getattr(value, "67", None)
                setattr(value, "67", self)

    @property
    def 40(self):
        return self.__40

    @40.setter
    def 40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__40", None)
        self.__40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "39"):
                opp_val = getattr(old_value, "39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "39"):
                opp_val = getattr(value, "39", None)
                if opp_val is None:
                    setattr(value, "39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Transition74(self):
        return self.__statemachines_Transition74

    @statemachines_Transition74.setter
    def statemachines_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition74", None)
        self.__statemachines_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior75"):
                opp_val = getattr(old_value, "statemachines_Behavior75", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior75"):
                opp_val = getattr(value, "statemachines_Behavior75", None)
                setattr(value, "statemachines_Behavior75", self)

    @property
    def 71(self):
        return self.__71

    @71.setter
    def 71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__71", None)
        self.__71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "72"):
                opp_val = getattr(old_value, "72", None)
                if opp_val == self:
                    setattr(old_value, "72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "72"):
                opp_val = getattr(value, "72", None)
                setattr(value, "72", self)

    @property
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__27", None)
        self.__27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                if opp_val is None:
                    setattr(value, "26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Transition(self):
        return self.__statemachines_Transition

    @statemachines_Transition.setter
    def statemachines_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition", None)
        self.__statemachines_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_Trigger69"):
                    opp_val = getattr(item, "statemachines_Trigger69", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Trigger69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Trigger69"):
                    opp_val = getattr(item, "statemachines_Trigger69", None)
                    
                    setattr(item, "statemachines_Trigger69", self)
                    

    def fire(self, eventOccurrence: str):
        # TODO: Implement fire method
        pass

class statemachines_Region(NamedElement):

    pass
class statemachines_Attribute(NamedElement):

    pass
class statemachines_Operation(NamedElement):

    pass
class statemachines_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class statemachines_StringConstraint:

    pass
class statemachines_IntegerConstraint:

    pass
class statemachines_BooleanConstraint:

    pass
class statemachines_Signal(NamedElement):

    pass
class statemachines_StateMachine(NamedElement):

    def __init__(self, statemachines_StateMachine: "statemachines_CustomSystem" = None, : set["statemachines_Region"] = None, 30: "statemachines_Region" = None):
        self.statemachines_StateMachine = statemachines_StateMachine
        self. =  if  is not None else set()
        self.30 = 30
        
    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StateMachine__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    if opp_val == self:
                        setattr(item, "21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    setattr(item, "21", self)
                    

    @property
    def statemachines_StateMachine(self):
        return self.__statemachines_StateMachine

    @statemachines_StateMachine.setter
    def statemachines_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StateMachine__statemachines_StateMachine", None)
        self.__statemachines_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_CustomSystem"):
                opp_val = getattr(old_value, "statemachines_CustomSystem", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_CustomSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_CustomSystem"):
                opp_val = getattr(value, "statemachines_CustomSystem", None)
                setattr(value, "statemachines_CustomSystem", self)

    @property
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StateMachine__30", None)
        self.__30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    def eventOccurrenceReceived(self, event: str):
        # TODO: Implement eventOccurrenceReceived method
        pass

    def run(self):
        # TODO: Implement run method
        pass

class statemachines_CustomSystem:

    pass