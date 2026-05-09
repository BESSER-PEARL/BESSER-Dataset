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
class statemachines_CallEventOccurrence(EventOccurrence):

    pass
class statemachines_CompletionEventOccurrence:

    pass
class statemachines_EventOccurrence(ABC):

    pass
class AttributeValue:

    pass
class statemachines_StringAttributeValue(AttributeValue):

    def __init__(self, value: str, statemachines_StringAttributeValue: "statemachines_StringAttribute" = None):
        self.value = value
        self.statemachines_StringAttributeValue = statemachines_StringAttributeValue
        
        pass
    @property
    def value(self):
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

class statemachines_IntegerAttributeValue(AttributeValue):

    def __init__(self, value: str, statemachines_IntegerAttributeValue: "statemachines_IntegerAttribute" = None):
        self.value = value
        self.statemachines_IntegerAttributeValue = statemachines_IntegerAttributeValue
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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
class statemachines_Constraint(ABC):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Attribute:

    pass
class statemachines_IntegerAttribute(Attribute):

    pass
class statemachines_StringAttribute(Attribute):

    pass
class statemachines_BooleanAttribute(Attribute):

    pass
class Vertex:

    pass
class statemachines_Pseudostate(Vertex):

    def __init__(self, kind: str, Pseudostate: "statemachines_State" = None, connectionPoint: "statemachines_State" = None):
        self.kind = kind
        self.Pseudostate = Pseudostate
        self.connectionPoint = connectionPoint
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def connectionPoint(self):
        return self.__connectionPoint

    @connectionPoint.setter
    def connectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__connectionPoint", None)
        self.__connectionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State34"):
                opp_val = getattr(old_value, "State34", None)
                if opp_val == self:
                    setattr(old_value, "State34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State34"):
                opp_val = getattr(value, "State34", None)
                setattr(value, "State34", self)

    @property
    def Pseudostate(self):
        return self.__Pseudostate

    @Pseudostate.setter
    def Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Pseudostate__Pseudostate", None)
        self.__Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state47"):
                opp_val = getattr(old_value, "state47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state47"):
                opp_val = getattr(value, "state47", None)
                if opp_val is None:
                    setattr(value, "state47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachines_State(Vertex):

    pass
class statemachines_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
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
class statemachines_Transition(NamedElement):

    def __init__(self, kind: str, Transition: "statemachines_Region" = None, Transition30: "statemachines_Vertex" = None, Transition32: "statemachines_Vertex" = None, outgoingTransitions: "statemachines_Vertex" = None, incomingTransitions: "statemachines_Vertex" = None, statemachines_Transition: set["statemachines_Trigger"] = None, transitions: "statemachines_Region" = None, statemachines_Transition57: "statemachines_Behavior" = None):
        self.kind = kind
        self.Transition = Transition
        self.Transition30 = Transition30
        self.Transition32 = Transition32
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.statemachines_Transition = statemachines_Transition if statemachines_Transition is not None else set()
        self.transitions = transitions
        self.statemachines_Transition57 = statemachines_Transition57
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region55"):
                opp_val = getattr(old_value, "Region55", None)
                if opp_val == self:
                    setattr(old_value, "Region55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region55"):
                opp_val = getattr(value, "Region55", None)
                setattr(value, "Region55", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container23"):
                opp_val = getattr(old_value, "container23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container23"):
                opp_val = getattr(value, "container23", None)
                if opp_val is None:
                    setattr(value, "container23", set([self]))
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
                if hasattr(item, "statemachines_Trigger53"):
                    opp_val = getattr(item, "statemachines_Trigger53", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Trigger53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Trigger53"):
                    opp_val = getattr(item, "statemachines_Trigger53", None)
                    
                    setattr(item, "statemachines_Trigger53", self)
                    

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex51"):
                opp_val = getattr(old_value, "Vertex51", None)
                if opp_val == self:
                    setattr(old_value, "Vertex51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex51"):
                opp_val = getattr(value, "Vertex51", None)
                setattr(value, "Vertex51", self)

    @property
    def Transition32(self):
        return self.__Transition32

    @Transition32.setter
    def Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition32", None)
        self.__Transition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Transition57(self):
        return self.__statemachines_Transition57

    @statemachines_Transition57.setter
    def statemachines_Transition57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition57", None)
        self.__statemachines_Transition57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior58"):
                opp_val = getattr(old_value, "statemachines_Behavior58", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior58"):
                opp_val = getattr(value, "statemachines_Behavior58", None)
                setattr(value, "statemachines_Behavior58", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex49"):
                opp_val = getattr(old_value, "Vertex49", None)
                if opp_val == self:
                    setattr(old_value, "Vertex49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex49"):
                opp_val = getattr(value, "Vertex49", None)
                setattr(value, "Vertex49", self)

    @property
    def Transition30(self):
        return self.__Transition30

    @Transition30.setter
    def Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition30", None)
        self.__Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachines_Trigger(NamedElement):

    pass
class statemachines_Behavior(NamedElement):

    pass
class statemachines_Region(NamedElement):

    pass
class statemachines_Attribute(NamedElement):

    pass
class statemachines_Vertex(NamedElement):

    pass
class statemachines_Operation(NamedElement):

    pass
class statemachines_Signal(NamedElement):

    pass
class statemachines_StateMachine(NamedElement):

    pass
class statemachines_CustomSystem:

    pass