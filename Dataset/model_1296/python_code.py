from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    external = "external"
    internal = "internal"


############################################
# Definition of Classes
############################################

class StateMachines_ProtocolStateMachines_Operation:

    pass
class Operation:

    pass
class Classifier:

    pass
class StateMachines_ProtocolStateMachines_Interface(Classifier):

    pass
class StateMachines_ProtocolStateMachines_Port:

    pass
class StateMachines_ProtocolStateMachines_DirectedRelationship(ABC):

    pass
class ProtocolStateMachine:

    pass
class DirectedRelationship:

    pass
class StateMachines_ProtocolStateMachines_ProtocolConformance(DirectedRelationship):

    pass
class ProtocolConformance:

    pass
class ConnectionPointReference:

    pass
class BehaviorStateMachines_Vertex:

    pass
class StateMachines_BehaviorStateMachines_Trigger(ABC):

    pass
class StateMachines_BehaviorStateMachines_Constraint(ABC):

    pass
class StateMachines_BehaviorStateMachines_TimeEvent:

    pass
class StateMachines_BehaviorStateMachines_Classifier(ABC):

    pass
class StateMachines_BehaviorStateMachines_RedefinableElement(ABC):

    pass
class NamedElement:

    pass
class StateMachines_BehaviorStateMachines_Vertex(NamedElement):

    pass
class StateMachines_BehaviorStateMachines_NamedElement(ABC):

    pass
class Transition:

    pass
class StateMachines_ProtocolStateMachines_ProtocolTransition(Transition):

    pass
class Vertex:

    pass
class StateMachines_BehaviorStateMachines_ConnectionPointReference(Vertex):

    pass
class StateMachines_BehaviorStateMachines_Pseudostate(Vertex):

    pass
class BehaviorStateMachines_RedefinableElement:

    pass
class BehaviorStateMachines_Namespace:

    pass
class StateMachines_BehaviorStateMachines_State(BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement, BehaviorStateMachines_Vertex):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, StateMachines_BehaviorStateMachines_State: set["Trigger"] = None, StateMachines_BehaviorStateMachines_State56: "Behavior" = None, StateMachines_BehaviorStateMachines_State59: "Behavior" = None, StateMachines_BehaviorStateMachines_State62: "Behavior" = None, StateMachines_BehaviorStateMachines_State65: "Constraint" = None, StateMachines_BehaviorStateMachines_State68: "State" = None, state: set["ConnectionPointReference"] = None, state46: set["Pseudostate"] = None, submachineState: "StateMachine" = None, state51: set["Region"] = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.StateMachines_BehaviorStateMachines_State = StateMachines_BehaviorStateMachines_State if StateMachines_BehaviorStateMachines_State is not None else set()
        self.StateMachines_BehaviorStateMachines_State56 = StateMachines_BehaviorStateMachines_State56
        self.StateMachines_BehaviorStateMachines_State59 = StateMachines_BehaviorStateMachines_State59
        self.StateMachines_BehaviorStateMachines_State62 = StateMachines_BehaviorStateMachines_State62
        self.StateMachines_BehaviorStateMachines_State65 = StateMachines_BehaviorStateMachines_State65
        self.StateMachines_BehaviorStateMachines_State68 = StateMachines_BehaviorStateMachines_State68
        self.state = state if state is not None else set()
        self.state46 = state46 if state46 is not None else set()
        self.submachineState = submachineState
        self.state51 = state51 if state51 is not None else set()
        
        pass
    @property
    def isSimple(self):
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple


    @property
    def isOrthogonal(self):
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def isSubmachineState(self):
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState


    @property
    def StateMachines_BehaviorStateMachines_State(self):
        return self.__StateMachines_BehaviorStateMachines_State

    @StateMachines_BehaviorStateMachines_State.setter
    def StateMachines_BehaviorStateMachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State", None)
        self.__StateMachines_BehaviorStateMachines_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger54"):
                    opp_val = getattr(item, "Trigger54", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger54"):
                    opp_val = getattr(item, "Trigger54", None)
                    
                    setattr(item, "Trigger54", self)
                    

    @property
    def StateMachines_BehaviorStateMachines_State59(self):
        return self.__StateMachines_BehaviorStateMachines_State59

    @StateMachines_BehaviorStateMachines_State59.setter
    def StateMachines_BehaviorStateMachines_State59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State59", None)
        self.__StateMachines_BehaviorStateMachines_State59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior60"):
                opp_val = getattr(old_value, "Behavior60", None)
                if opp_val == self:
                    setattr(old_value, "Behavior60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior60"):
                opp_val = getattr(value, "Behavior60", None)
                setattr(value, "Behavior60", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    setattr(item, "ConnectionPointReference", self)
                    

    @property
    def StateMachines_BehaviorStateMachines_State68(self):
        return self.__StateMachines_BehaviorStateMachines_State68

    @StateMachines_BehaviorStateMachines_State68.setter
    def StateMachines_BehaviorStateMachines_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State68", None)
        self.__StateMachines_BehaviorStateMachines_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State69"):
                opp_val = getattr(old_value, "State69", None)
                if opp_val == self:
                    setattr(old_value, "State69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State69"):
                opp_val = getattr(value, "State69", None)
                setattr(value, "State69", self)

    @property
    def state51(self):
        return self.__state51

    @state51.setter
    def state51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__state51", None)
        self.__state51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region52"):
                    opp_val = getattr(item, "Region52", None)
                    
                    if opp_val == self:
                        setattr(item, "Region52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region52"):
                    opp_val = getattr(item, "Region52", None)
                    
                    setattr(item, "Region52", self)
                    

    @property
    def StateMachines_BehaviorStateMachines_State62(self):
        return self.__StateMachines_BehaviorStateMachines_State62

    @StateMachines_BehaviorStateMachines_State62.setter
    def StateMachines_BehaviorStateMachines_State62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State62", None)
        self.__StateMachines_BehaviorStateMachines_State62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior63"):
                opp_val = getattr(old_value, "Behavior63", None)
                if opp_val == self:
                    setattr(old_value, "Behavior63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior63"):
                opp_val = getattr(value, "Behavior63", None)
                setattr(value, "Behavior63", self)

    @property
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__submachineState", None)
        self.__submachineState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine49"):
                opp_val = getattr(old_value, "StateMachine49", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine49"):
                opp_val = getattr(value, "StateMachine49", None)
                setattr(value, "StateMachine49", self)

    @property
    def state46(self):
        return self.__state46

    @state46.setter
    def state46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__state46", None)
        self.__state46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pseudostate47"):
                    opp_val = getattr(item, "Pseudostate47", None)
                    
                    if opp_val == self:
                        setattr(item, "Pseudostate47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pseudostate47"):
                    opp_val = getattr(item, "Pseudostate47", None)
                    
                    setattr(item, "Pseudostate47", self)
                    

    @property
    def StateMachines_BehaviorStateMachines_State65(self):
        return self.__StateMachines_BehaviorStateMachines_State65

    @StateMachines_BehaviorStateMachines_State65.setter
    def StateMachines_BehaviorStateMachines_State65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State65", None)
        self.__StateMachines_BehaviorStateMachines_State65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint66"):
                opp_val = getattr(old_value, "Constraint66", None)
                if opp_val == self:
                    setattr(old_value, "Constraint66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint66"):
                opp_val = getattr(value, "Constraint66", None)
                setattr(value, "Constraint66", self)

    @property
    def StateMachines_BehaviorStateMachines_State56(self):
        return self.__StateMachines_BehaviorStateMachines_State56

    @StateMachines_BehaviorStateMachines_State56.setter
    def StateMachines_BehaviorStateMachines_State56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State56", None)
        self.__StateMachines_BehaviorStateMachines_State56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior57"):
                opp_val = getattr(old_value, "Behavior57", None)
                if opp_val == self:
                    setattr(old_value, "Behavior57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior57"):
                opp_val = getattr(value, "Behavior57", None)
                setattr(value, "Behavior57", self)

class StateMachines_BehaviorStateMachines_Region(BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement):

    pass
class StateMachines_BehaviorStateMachines_Namespace(ABC):

    pass
class StateMachine:

    pass
class StateMachines_ProtocolStateMachines_ProtocolStateMachine(StateMachine):

    pass
class State:

    pass
class StateMachines_BehaviorStateMachines_FinalState(State):

    pass
class Constraint:

    pass
class Trigger:

    pass
class StateMachines_BehaviorStateMachines_Transition(BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement):

    def __init__(self, kind: str, outgoing: "Vertex" = None, incoming: "Vertex" = None, StateMachines_BehaviorStateMachines_Transition: "Behavior" = None, StateMachines_BehaviorStateMachines_Transition27: "Trigger" = None, StateMachines_BehaviorStateMachines_Transition29: "Constraint" = None, transition: "Region" = None, StateMachines_BehaviorStateMachines_Transition33: "Transition" = None):
        self.kind = kind
        self.outgoing = outgoing
        self.incoming = incoming
        self.StateMachines_BehaviorStateMachines_Transition = StateMachines_BehaviorStateMachines_Transition
        self.StateMachines_BehaviorStateMachines_Transition27 = StateMachines_BehaviorStateMachines_Transition27
        self.StateMachines_BehaviorStateMachines_Transition29 = StateMachines_BehaviorStateMachines_Transition29
        self.transition = transition
        self.StateMachines_BehaviorStateMachines_Transition33 = StateMachines_BehaviorStateMachines_Transition33
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex24"):
                opp_val = getattr(old_value, "Vertex24", None)
                if opp_val == self:
                    setattr(old_value, "Vertex24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex24"):
                opp_val = getattr(value, "Vertex24", None)
                setattr(value, "Vertex24", self)

    @property
    def StateMachines_BehaviorStateMachines_Transition33(self):
        return self.__StateMachines_BehaviorStateMachines_Transition33

    @StateMachines_BehaviorStateMachines_Transition33.setter
    def StateMachines_BehaviorStateMachines_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition33", None)
        self.__StateMachines_BehaviorStateMachines_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition34"):
                opp_val = getattr(old_value, "Transition34", None)
                if opp_val == self:
                    setattr(old_value, "Transition34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition34"):
                opp_val = getattr(value, "Transition34", None)
                setattr(value, "Transition34", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region31"):
                opp_val = getattr(old_value, "Region31", None)
                if opp_val == self:
                    setattr(old_value, "Region31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region31"):
                opp_val = getattr(value, "Region31", None)
                setattr(value, "Region31", self)

    @property
    def StateMachines_BehaviorStateMachines_Transition(self):
        return self.__StateMachines_BehaviorStateMachines_Transition

    @StateMachines_BehaviorStateMachines_Transition.setter
    def StateMachines_BehaviorStateMachines_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition", None)
        self.__StateMachines_BehaviorStateMachines_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior"):
                opp_val = getattr(old_value, "Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior"):
                opp_val = getattr(value, "Behavior", None)
                setattr(value, "Behavior", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex22"):
                opp_val = getattr(old_value, "Vertex22", None)
                if opp_val == self:
                    setattr(old_value, "Vertex22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex22"):
                opp_val = getattr(value, "Vertex22", None)
                setattr(value, "Vertex22", self)

    @property
    def StateMachines_BehaviorStateMachines_Transition29(self):
        return self.__StateMachines_BehaviorStateMachines_Transition29

    @StateMachines_BehaviorStateMachines_Transition29.setter
    def StateMachines_BehaviorStateMachines_Transition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition29", None)
        self.__StateMachines_BehaviorStateMachines_Transition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint"):
                opp_val = getattr(old_value, "Constraint", None)
                if opp_val == self:
                    setattr(old_value, "Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint"):
                opp_val = getattr(value, "Constraint", None)
                setattr(value, "Constraint", self)

    @property
    def StateMachines_BehaviorStateMachines_Transition27(self):
        return self.__StateMachines_BehaviorStateMachines_Transition27

    @StateMachines_BehaviorStateMachines_Transition27.setter
    def StateMachines_BehaviorStateMachines_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition27", None)
        self.__StateMachines_BehaviorStateMachines_Transition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trigger"):
                opp_val = getattr(old_value, "Trigger", None)
                if opp_val == self:
                    setattr(old_value, "Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trigger"):
                opp_val = getattr(value, "Trigger", None)
                setattr(value, "Trigger", self)

class Pseudostate:

    pass
class Region:

    pass
class Behavior:

    pass
class StateMachines_BehaviorStateMachines_StateMachine(Behavior):

    pass
class StateMachines_BehaviorStateMachines_Behavior(ABC):

    pass