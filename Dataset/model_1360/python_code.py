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
class statemachines_EventOccurrence(ABC):

    pass
class statemachines_CallEventOccurrence(EventOccurrence):

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

class statemachines_AttributeValue(ABC):

    pass
class Behavior:

    pass
class statemachines_OperationBehavior(Behavior):

    pass
class statemachines_SignalEventOccurrence(EventOccurrence):

    pass
class State:

    pass
class statemachines_FinalState(State):

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

class Vertex:

    pass
class statemachines_State(Vertex):

    pass
class statemachines_Pseudostate(Vertex):

    def __init__(self, kind: str, 44: "statemachines_State" = None, 60: "statemachines_State" = None):
        self.kind = kind
        self.44 = 44
        self.60 = 60
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__60", None)
        self.__60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "59"):
                opp_val = getattr(old_value, "59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "59"):
                opp_val = getattr(value, "59", None)
                if opp_val is None:
                    setattr(value, "59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 44(self):
        return self.__44

    @44.setter
    def 44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__44", None)
        self.__44 = value
        
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
class statemachines_StringConstraint:

    pass
class statemachines_IntegerConstraint:

    pass
class statemachines_BooleanConstraint:

    pass
class statemachines_CustomSystem:

    pass
class NamedElement:

    pass
class statemachines_StateMachine(NamedElement):

    pass
class statemachines_Region(NamedElement):

    pass
class statemachines_Attribute(NamedElement):

    pass
class statemachines_Transition(NamedElement):

    def __init__(self, kind: str, 42: "statemachines_Vertex" = None, 27: "statemachines_Region" = None, 39: "statemachines_Vertex" = None, 70: "statemachines_Region" = None, statemachines_Transition73: "statemachines_Behavior" = None, 62: "statemachines_Vertex" = None, 65: "statemachines_Vertex" = None, statemachines_Transition: set["statemachines_Trigger"] = None):
        self.kind = kind
        self.42 = 42
        self.27 = 27
        self.39 = 39
        self.70 = 70
        self.statemachines_Transition73 = statemachines_Transition73
        self.62 = 62
        self.65 = 65
        self.statemachines_Transition = statemachines_Transition if statemachines_Transition is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 70(self):
        return self.__70

    @70.setter
    def 70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__70", None)
        self.__70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "71"):
                opp_val = getattr(old_value, "71", None)
                if opp_val == self:
                    setattr(old_value, "71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "71"):
                opp_val = getattr(value, "71", None)
                setattr(value, "71", self)

    @property
    def 65(self):
        return self.__65

    @65.setter
    def 65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__65", None)
        self.__65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "66"):
                opp_val = getattr(old_value, "66", None)
                if opp_val == self:
                    setattr(old_value, "66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "66"):
                opp_val = getattr(value, "66", None)
                setattr(value, "66", self)

    @property
    def 39(self):
        return self.__39

    @39.setter
    def 39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__39", None)
        self.__39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "38"):
                opp_val = getattr(old_value, "38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "38"):
                opp_val = getattr(value, "38", None)
                if opp_val is None:
                    setattr(value, "38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Transition73(self):
        return self.__statemachines_Transition73

    @statemachines_Transition73.setter
    def statemachines_Transition73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition73", None)
        self.__statemachines_Transition73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior74"):
                opp_val = getattr(old_value, "statemachines_Behavior74", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior74"):
                opp_val = getattr(value, "statemachines_Behavior74", None)
                setattr(value, "statemachines_Behavior74", self)

    @property
    def 42(self):
        return self.__42

    @42.setter
    def 42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__42", None)
        self.__42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "41"):
                opp_val = getattr(old_value, "41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "41"):
                opp_val = getattr(value, "41", None)
                if opp_val is None:
                    setattr(value, "41", set([self]))
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
                if hasattr(item, "statemachines_Trigger68"):
                    opp_val = getattr(item, "statemachines_Trigger68", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Trigger68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Trigger68"):
                    opp_val = getattr(item, "statemachines_Trigger68", None)
                    
                    setattr(item, "statemachines_Trigger68", self)
                    

    @property
    def 62(self):
        return self.__62

    @62.setter
    def 62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__62", None)
        self.__62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "63"):
                opp_val = getattr(old_value, "63", None)
                if opp_val == self:
                    setattr(old_value, "63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "63"):
                opp_val = getattr(value, "63", None)
                setattr(value, "63", self)

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

class statemachines_Vertex(NamedElement):

    pass
class statemachines_Behavior(NamedElement):

    pass
class statemachines_Trigger(NamedElement):

    pass
class statemachines_Operation(NamedElement):

    pass
class statemachines_Signal(NamedElement):

    pass