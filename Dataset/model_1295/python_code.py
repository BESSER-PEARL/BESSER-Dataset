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
class ProtocolConformance:

    pass
class StateMachines_BehaviorStateMachines_TimeEvent:

    pass
class StateMachines_BehaviorStateMachines_Classifier(ABC):

    pass
class StateMachines_BehaviorStateMachines_RedefinableElement(ABC):

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
class ConnectionPointReference:

    pass
class StateMachines_BehaviorStateMachines_Trigger(ABC):

    pass
class StateMachines_BehaviorStateMachines_Constraint(ABC):

    pass
class BehaviorStateMachines_Vertex:

    pass
class Constraint:

    pass
class Trigger:

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
class Region:

    pass
class Behavior:

    pass
class StateMachines_BehaviorStateMachines_StateMachine(Behavior):

    pass
class StateMachines_BehaviorStateMachines_Behavior(ABC):

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
class StateMachines_BehaviorStateMachines_Transition(BehaviorStateMachines_RedefinableElement, BehaviorStateMachines_Namespace):

    def __init__(self, kind: str, StateMachines_BehaviorStateMachines_Transition: "Behavior" = None, StateMachines_BehaviorStateMachines_Transition38: "Trigger" = None, StateMachines_BehaviorStateMachines_Transition40: "Constraint" = None, 42: "Region" = None, 31: "Vertex" = None, 34: "Vertex" = None, StateMachines_BehaviorStateMachines_Transition45: "Transition" = None):
        self.kind = kind
        self.StateMachines_BehaviorStateMachines_Transition = StateMachines_BehaviorStateMachines_Transition
        self.StateMachines_BehaviorStateMachines_Transition38 = StateMachines_BehaviorStateMachines_Transition38
        self.StateMachines_BehaviorStateMachines_Transition40 = StateMachines_BehaviorStateMachines_Transition40
        self.42 = 42
        self.31 = 31
        self.34 = 34
        self.StateMachines_BehaviorStateMachines_Transition45 = StateMachines_BehaviorStateMachines_Transition45
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 42(self):
        return self.__42

    @42.setter
    def 42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__42", None)
        self.__42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "43"):
                opp_val = getattr(old_value, "43", None)
                if opp_val == self:
                    setattr(old_value, "43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "43"):
                opp_val = getattr(value, "43", None)
                setattr(value, "43", self)

    @property
    def StateMachines_BehaviorStateMachines_Transition38(self):
        return self.__StateMachines_BehaviorStateMachines_Transition38

    @StateMachines_BehaviorStateMachines_Transition38.setter
    def StateMachines_BehaviorStateMachines_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition38", None)
        self.__StateMachines_BehaviorStateMachines_Transition38 = value
        
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

    @property
    def StateMachines_BehaviorStateMachines_Transition45(self):
        return self.__StateMachines_BehaviorStateMachines_Transition45

    @StateMachines_BehaviorStateMachines_Transition45.setter
    def StateMachines_BehaviorStateMachines_Transition45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition45", None)
        self.__StateMachines_BehaviorStateMachines_Transition45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def 34(self):
        return self.__34

    @34.setter
    def 34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__34", None)
        self.__34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "35"):
                opp_val = getattr(old_value, "35", None)
                if opp_val == self:
                    setattr(old_value, "35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "35"):
                opp_val = getattr(value, "35", None)
                setattr(value, "35", self)

    @property
    def 31(self):
        return self.__31

    @31.setter
    def 31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__31", None)
        self.__31 = value
        
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
    def StateMachines_BehaviorStateMachines_Transition40(self):
        return self.__StateMachines_BehaviorStateMachines_Transition40

    @StateMachines_BehaviorStateMachines_Transition40.setter
    def StateMachines_BehaviorStateMachines_Transition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_Transition__StateMachines_BehaviorStateMachines_Transition40", None)
        self.__StateMachines_BehaviorStateMachines_Transition40 = value
        
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

class StateMachines_BehaviorStateMachines_State(BehaviorStateMachines_RedefinableElement, BehaviorStateMachines_Namespace, BehaviorStateMachines_Vertex):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, StateMachines_BehaviorStateMachines_State75: "Behavior" = None, StateMachines_BehaviorStateMachines_State78: "Behavior" = None, StateMachines_BehaviorStateMachines_State81: "Constraint" = None, StateMachines_BehaviorStateMachines_State84: "State" = None, 58: set["ConnectionPointReference"] = None, 61: set["Pseudostate"] = None, 64: "StateMachine" = None, 67: set["Region"] = None, StateMachines_BehaviorStateMachines_State: set["Trigger"] = None, StateMachines_BehaviorStateMachines_State72: "Behavior" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.StateMachines_BehaviorStateMachines_State75 = StateMachines_BehaviorStateMachines_State75
        self.StateMachines_BehaviorStateMachines_State78 = StateMachines_BehaviorStateMachines_State78
        self.StateMachines_BehaviorStateMachines_State81 = StateMachines_BehaviorStateMachines_State81
        self.StateMachines_BehaviorStateMachines_State84 = StateMachines_BehaviorStateMachines_State84
        self.58 = 58 if 58 is not None else set()
        self.61 = 61 if 61 is not None else set()
        self.64 = 64
        self.67 = 67 if 67 is not None else set()
        self.StateMachines_BehaviorStateMachines_State = StateMachines_BehaviorStateMachines_State if StateMachines_BehaviorStateMachines_State is not None else set()
        self.StateMachines_BehaviorStateMachines_State72 = StateMachines_BehaviorStateMachines_State72
        
    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def StateMachines_BehaviorStateMachines_State81(self):
        return self.__StateMachines_BehaviorStateMachines_State81

    @StateMachines_BehaviorStateMachines_State81.setter
    def StateMachines_BehaviorStateMachines_State81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State81", None)
        self.__StateMachines_BehaviorStateMachines_State81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint82"):
                opp_val = getattr(old_value, "Constraint82", None)
                if opp_val == self:
                    setattr(old_value, "Constraint82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint82"):
                opp_val = getattr(value, "Constraint82", None)
                setattr(value, "Constraint82", self)

    @property
    def StateMachines_BehaviorStateMachines_State72(self):
        return self.__StateMachines_BehaviorStateMachines_State72

    @StateMachines_BehaviorStateMachines_State72.setter
    def StateMachines_BehaviorStateMachines_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State72", None)
        self.__StateMachines_BehaviorStateMachines_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior73"):
                opp_val = getattr(old_value, "Behavior73", None)
                if opp_val == self:
                    setattr(old_value, "Behavior73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior73"):
                opp_val = getattr(value, "Behavior73", None)
                setattr(value, "Behavior73", self)

    @property
    def StateMachines_BehaviorStateMachines_State78(self):
        return self.__StateMachines_BehaviorStateMachines_State78

    @StateMachines_BehaviorStateMachines_State78.setter
    def StateMachines_BehaviorStateMachines_State78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State78", None)
        self.__StateMachines_BehaviorStateMachines_State78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior79"):
                opp_val = getattr(old_value, "Behavior79", None)
                if opp_val == self:
                    setattr(old_value, "Behavior79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior79"):
                opp_val = getattr(value, "Behavior79", None)
                setattr(value, "Behavior79", self)

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
                if hasattr(item, "Trigger70"):
                    opp_val = getattr(item, "Trigger70", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger70"):
                    opp_val = getattr(item, "Trigger70", None)
                    
                    setattr(item, "Trigger70", self)
                    

    @property
    def 61(self):
        return self.__61

    @61.setter
    def 61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__61", None)
        self.__61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "62"):
                    opp_val = getattr(item, "62", None)
                    
                    if opp_val == self:
                        setattr(item, "62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "62"):
                    opp_val = getattr(item, "62", None)
                    
                    setattr(item, "62", self)
                    

    @property
    def 64(self):
        return self.__64

    @64.setter
    def 64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__64", None)
        self.__64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "65"):
                opp_val = getattr(old_value, "65", None)
                if opp_val == self:
                    setattr(old_value, "65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "65"):
                opp_val = getattr(value, "65", None)
                setattr(value, "65", self)

    @property
    def StateMachines_BehaviorStateMachines_State84(self):
        return self.__StateMachines_BehaviorStateMachines_State84

    @StateMachines_BehaviorStateMachines_State84.setter
    def StateMachines_BehaviorStateMachines_State84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State84", None)
        self.__StateMachines_BehaviorStateMachines_State84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def 67(self):
        return self.__67

    @67.setter
    def 67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__67", None)
        self.__67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "68"):
                    opp_val = getattr(item, "68", None)
                    
                    if opp_val == self:
                        setattr(item, "68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "68"):
                    opp_val = getattr(item, "68", None)
                    
                    setattr(item, "68", self)
                    

    @property
    def StateMachines_BehaviorStateMachines_State75(self):
        return self.__StateMachines_BehaviorStateMachines_State75

    @StateMachines_BehaviorStateMachines_State75.setter
    def StateMachines_BehaviorStateMachines_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__StateMachines_BehaviorStateMachines_State75", None)
        self.__StateMachines_BehaviorStateMachines_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior76"):
                opp_val = getattr(old_value, "Behavior76", None)
                if opp_val == self:
                    setattr(old_value, "Behavior76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior76"):
                opp_val = getattr(value, "Behavior76", None)
                setattr(value, "Behavior76", self)

    @property
    def 58(self):
        return self.__58

    @58.setter
    def 58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_BehaviorStateMachines_State__58", None)
        self.__58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "59"):
                    opp_val = getattr(item, "59", None)
                    
                    if opp_val == self:
                        setattr(item, "59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "59"):
                    opp_val = getattr(item, "59", None)
                    
                    setattr(item, "59", self)
                    

class StateMachines_BehaviorStateMachines_Region(BehaviorStateMachines_RedefinableElement, BehaviorStateMachines_Namespace):

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
class Pseudostate:

    pass