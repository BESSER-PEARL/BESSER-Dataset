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
class Vertex:

    pass
class statemachines_Pseudostate(Vertex):

    def __init__(self, kind: str, connectionPoint: "statemachines_State" = None, Pseudostate: "statemachines_State" = None):
        self.kind = kind
        self.connectionPoint = connectionPoint
        self.Pseudostate = Pseudostate
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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
            if hasattr(old_value, "state48"):
                opp_val = getattr(old_value, "state48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state48"):
                opp_val = getattr(value, "state48", None)
                if opp_val is None:
                    setattr(value, "state48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "State35"):
                opp_val = getattr(old_value, "State35", None)
                if opp_val == self:
                    setattr(old_value, "State35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State35"):
                opp_val = getattr(value, "State35", None)
                setattr(value, "State35", self)

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


class statemachines_State(Vertex):

    def __init__(self, isEntryCompleted: bool, isDoActivityCompleted: bool, isExitCompleted: bool, State: "statemachines_Region" = None, State35: "statemachines_Pseudostate" = None, state: set["statemachines_Region"] = None, statemachines_State: "statemachines_Behavior" = None, statemachines_State40: "statemachines_Behavior" = None, statemachines_State43: "statemachines_Behavior" = None, statemachines_State46: set["statemachines_Trigger"] = None, state48: set["statemachines_Pseudostate"] = None, statemachines_State69: "statemachines_CompletionEventOccurrence" = None):
        self.isEntryCompleted = isEntryCompleted
        self.isDoActivityCompleted = isDoActivityCompleted
        self.isExitCompleted = isExitCompleted
        self.State = State
        self.State35 = State35
        self.state = state if state is not None else set()
        self.statemachines_State = statemachines_State
        self.statemachines_State40 = statemachines_State40
        self.statemachines_State43 = statemachines_State43
        self.statemachines_State46 = statemachines_State46 if statemachines_State46 is not None else set()
        self.state48 = state48 if state48 is not None else set()
        self.statemachines_State69 = statemachines_State69
        
        pass
    @property
    def isExitCompleted(self):
        return self.__isExitCompleted

    @isExitCompleted.setter
    def isExitCompleted(self, isExitCompleted: bool):
        self.__isExitCompleted = isExitCompleted


    @property
    def isEntryCompleted(self):
        return self.__isEntryCompleted

    @isEntryCompleted.setter
    def isEntryCompleted(self, isEntryCompleted: bool):
        self.__isEntryCompleted = isEntryCompleted


    @property
    def isDoActivityCompleted(self):
        return self.__isDoActivityCompleted

    @isDoActivityCompleted.setter
    def isDoActivityCompleted(self, isDoActivityCompleted: bool):
        self.__isDoActivityCompleted = isDoActivityCompleted


    @property
    def state48(self):
        return self.__state48

    @state48.setter
    def state48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__state48", None)
        self.__state48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pseudostate"):
                    opp_val = getattr(item, "Pseudostate", None)
                    
                    if opp_val == self:
                        setattr(item, "Pseudostate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pseudostate"):
                    opp_val = getattr(item, "Pseudostate", None)
                    
                    setattr(item, "Pseudostate", self)
                    

    @property
    def statemachines_State46(self):
        return self.__statemachines_State46

    @statemachines_State46.setter
    def statemachines_State46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State46", None)
        self.__statemachines_State46 = value if value is not None else set()
        
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
                    

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region37"):
                    opp_val = getattr(item, "Region37", None)
                    
                    if opp_val == self:
                        setattr(item, "Region37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region37"):
                    opp_val = getattr(item, "Region37", None)
                    
                    setattr(item, "Region37", self)
                    

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
    def statemachines_State69(self):
        return self.__statemachines_State69

    @statemachines_State69.setter
    def statemachines_State69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State69", None)
        self.__statemachines_State69 = value
        
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
    def statemachines_State40(self):
        return self.__statemachines_State40

    @statemachines_State40.setter
    def statemachines_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State40", None)
        self.__statemachines_State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior41"):
                opp_val = getattr(old_value, "statemachines_Behavior41", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior41"):
                opp_val = getattr(value, "statemachines_Behavior41", None)
                setattr(value, "statemachines_Behavior41", self)

    @property
    def statemachines_State43(self):
        return self.__statemachines_State43

    @statemachines_State43.setter
    def statemachines_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State43", None)
        self.__statemachines_State43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior44"):
                opp_val = getattr(old_value, "statemachines_Behavior44", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior44"):
                opp_val = getattr(value, "statemachines_Behavior44", None)
                setattr(value, "statemachines_Behavior44", self)

    @property
    def State35(self):
        return self.__State35

    @State35.setter
    def State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__State35", None)
        self.__State35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectionPoint"):
                opp_val = getattr(old_value, "connectionPoint", None)
                if opp_val == self:
                    setattr(old_value, "connectionPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectionPoint"):
                opp_val = getattr(value, "connectionPoint", None)
                setattr(value, "connectionPoint", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "regions26"):
                opp_val = getattr(old_value, "regions26", None)
                if opp_val == self:
                    setattr(old_value, "regions26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "regions26"):
                opp_val = getattr(value, "regions26", None)
                setattr(value, "regions26", self)

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
class statemachines_Behavior(NamedElement):

    pass
class statemachines_Attribute(NamedElement):

    pass
class statemachines_Vertex(NamedElement):

    pass
class statemachines_Transition(NamedElement):

    def __init__(self, kind: str, Transition: "statemachines_Region" = None, Transition31: "statemachines_Vertex" = None, Transition33: "statemachines_Vertex" = None, outgoingTransitions: "statemachines_Vertex" = None, incomingTransitions: "statemachines_Vertex" = None, statemachines_Transition: set["statemachines_Trigger"] = None, transitions: "statemachines_Region" = None, statemachines_Transition58: "statemachines_Behavior" = None):
        self.kind = kind
        self.Transition = Transition
        self.Transition31 = Transition31
        self.Transition33 = Transition33
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.statemachines_Transition = statemachines_Transition if statemachines_Transition is not None else set()
        self.transitions = transitions
        self.statemachines_Transition58 = statemachines_Transition58
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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
            if hasattr(old_value, "Vertex50"):
                opp_val = getattr(old_value, "Vertex50", None)
                if opp_val == self:
                    setattr(old_value, "Vertex50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex50"):
                opp_val = getattr(value, "Vertex50", None)
                setattr(value, "Vertex50", self)

    @property
    def Transition33(self):
        return self.__Transition33

    @Transition33.setter
    def Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition33", None)
        self.__Transition33 = value
        
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region56"):
                opp_val = getattr(old_value, "Region56", None)
                if opp_val == self:
                    setattr(old_value, "Region56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region56"):
                opp_val = getattr(value, "Region56", None)
                setattr(value, "Region56", self)

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
            if hasattr(old_value, "Vertex52"):
                opp_val = getattr(old_value, "Vertex52", None)
                if opp_val == self:
                    setattr(old_value, "Vertex52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex52"):
                opp_val = getattr(value, "Vertex52", None)
                setattr(value, "Vertex52", self)

    @property
    def statemachines_Transition58(self):
        return self.__statemachines_Transition58

    @statemachines_Transition58.setter
    def statemachines_Transition58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition58", None)
        self.__statemachines_Transition58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Behavior59"):
                opp_val = getattr(old_value, "statemachines_Behavior59", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Behavior59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Behavior59"):
                opp_val = getattr(value, "statemachines_Behavior59", None)
                setattr(value, "statemachines_Behavior59", self)

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
                if hasattr(item, "statemachines_Trigger54"):
                    opp_val = getattr(item, "statemachines_Trigger54", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Trigger54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Trigger54"):
                    opp_val = getattr(item, "statemachines_Trigger54", None)
                    
                    setattr(item, "statemachines_Trigger54", self)
                    

    @property
    def Transition31(self):
        return self.__Transition31

    @Transition31.setter
    def Transition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition31", None)
        self.__Transition31 = value
        
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

    def fire(self, statemachines_eventOccurrence):
        # TODO: Implement fire method
        pass

class statemachines_Region(NamedElement):

    pass
class statemachines_Trigger(NamedElement):

    pass
class statemachines_Operation(NamedElement):

    pass
class statemachines_Signal(NamedElement):

    pass
class statemachines_StateMachine(NamedElement):

    def __init__(self, statemachines_StateMachine: "statemachines_CustomSystem" = None, stateMachine: set["statemachines_Region"] = None, StateMachine: "statemachines_Region" = None):
        self.statemachines_StateMachine = statemachines_StateMachine
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.StateMachine = StateMachine
        
        pass
    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "regions"):
                opp_val = getattr(old_value, "regions", None)
                if opp_val == self:
                    setattr(old_value, "regions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "regions"):
                opp_val = getattr(value, "regions", None)
                setattr(value, "regions", self)

    @property
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_StateMachine__stateMachine", None)
        self.__stateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    if opp_val == self:
                        setattr(item, "Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    setattr(item, "Region", self)
                    

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

    def run(self):
        # TODO: Implement run method
        pass

    def eventOccurrenceReceived(self, statemachines_event):
        # TODO: Implement eventOccurrenceReceived method
        pass

class statemachines_CustomSystem:

    pass
class EventOccurrence:

    pass
class statemachines_SignalEventOccurrence(EventOccurrence):

    pass
class statemachines_CallEventOccurrence(EventOccurrence):

    pass