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
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"


############################################
# Definition of Classes
############################################

class umlstatemachineselect_Event:

    pass
class State:

    pass
class umlstatemachineselect_FinalState(State):

    pass
class Vertex:

    pass
class umlstatemachineselect_ConnectionPointReference(Vertex):

    pass
class umlstatemachineselect_Trigger:

    pass
class umlstatemachineselect_Constraint:

    pass
class umlstatemachineselect_Behavior:

    pass
class umlstatemachineselect_PseudoState(Vertex):

    def __init__(self, kind: str, PseudoState: "umlstatemachineselect_StateMachine" = None, connectionPoint: "umlstatemachineselect_StateMachine" = None, umlstatemachineselect_PseudoState: "umlstatemachineselect_ConnectionPointReference" = None, umlstatemachineselect_PseudoState55: "umlstatemachineselect_ConnectionPointReference" = None):
        self.kind = kind
        self.PseudoState = PseudoState
        self.connectionPoint = connectionPoint
        self.umlstatemachineselect_PseudoState = umlstatemachineselect_PseudoState
        self.umlstatemachineselect_PseudoState55 = umlstatemachineselect_PseudoState55
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def PseudoState(self):
        return self.__PseudoState

    @PseudoState.setter
    def PseudoState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_PseudoState__PseudoState", None)
        self.__PseudoState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine3"):
                opp_val = getattr(old_value, "stateMachine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine3"):
                opp_val = getattr(value, "stateMachine3", None)
                if opp_val is None:
                    setattr(value, "stateMachine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectionPoint(self):
        return self.__connectionPoint

    @connectionPoint.setter
    def connectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_PseudoState__connectionPoint", None)
        self.__connectionPoint = value
        
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
    def umlstatemachineselect_PseudoState55(self):
        return self.__umlstatemachineselect_PseudoState55

    @umlstatemachineselect_PseudoState55.setter
    def umlstatemachineselect_PseudoState55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_PseudoState__umlstatemachineselect_PseudoState55", None)
        self.__umlstatemachineselect_PseudoState55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_ConnectionPointReference54"):
                opp_val = getattr(old_value, "umlstatemachineselect_ConnectionPointReference54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_ConnectionPointReference54"):
                opp_val = getattr(value, "umlstatemachineselect_ConnectionPointReference54", None)
                if opp_val is None:
                    setattr(value, "umlstatemachineselect_ConnectionPointReference54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlstatemachineselect_PseudoState(self):
        return self.__umlstatemachineselect_PseudoState

    @umlstatemachineselect_PseudoState.setter
    def umlstatemachineselect_PseudoState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_PseudoState__umlstatemachineselect_PseudoState", None)
        self.__umlstatemachineselect_PseudoState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_ConnectionPointReference"):
                opp_val = getattr(old_value, "umlstatemachineselect_ConnectionPointReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_ConnectionPointReference"):
                opp_val = getattr(value, "umlstatemachineselect_ConnectionPointReference", None)
                if opp_val is None:
                    setattr(value, "umlstatemachineselect_ConnectionPointReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umlstatemachineselect_State(Vertex):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, State10: "umlstatemachineselect_Region" = None, State: "umlstatemachineselect_StateMachine" = None, umlstatemachineselect_State: "umlstatemachineselect_Behavior" = None, state: set["umlstatemachineselect_Region"] = None, state31: set["umlstatemachineselect_ConnectionPointReference"] = None, submachineState: "umlstatemachineselect_StateMachine" = None, State51: "umlstatemachineselect_ConnectionPointReference" = None, umlstatemachineselect_State37: "umlstatemachineselect_Behavior" = None, umlstatemachineselect_State40: "umlstatemachineselect_Behavior" = None, umlstatemachineselect_State43: "umlstatemachineselect_Constraint" = None, umlstatemachineselect_State46: set["umlstatemachineselect_Trigger"] = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.State10 = State10
        self.State = State
        self.umlstatemachineselect_State = umlstatemachineselect_State
        self.state = state if state is not None else set()
        self.state31 = state31 if state31 is not None else set()
        self.submachineState = submachineState
        self.State51 = State51
        self.umlstatemachineselect_State37 = umlstatemachineselect_State37
        self.umlstatemachineselect_State40 = umlstatemachineselect_State40
        self.umlstatemachineselect_State43 = umlstatemachineselect_State43
        self.umlstatemachineselect_State46 = umlstatemachineselect_State46 if umlstatemachineselect_State46 is not None else set()
        
    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region29"):
                    opp_val = getattr(item, "Region29", None)
                    
                    if opp_val == self:
                        setattr(item, "Region29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region29"):
                    opp_val = getattr(item, "Region29", None)
                    
                    setattr(item, "Region29", self)
                    

    @property
    def umlstatemachineselect_State37(self):
        return self.__umlstatemachineselect_State37

    @umlstatemachineselect_State37.setter
    def umlstatemachineselect_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__umlstatemachineselect_State37", None)
        self.__umlstatemachineselect_State37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Behavior38"):
                opp_val = getattr(old_value, "umlstatemachineselect_Behavior38", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Behavior38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Behavior38"):
                opp_val = getattr(value, "umlstatemachineselect_Behavior38", None)
                setattr(value, "umlstatemachineselect_Behavior38", self)

    @property
    def umlstatemachineselect_State(self):
        return self.__umlstatemachineselect_State

    @umlstatemachineselect_State.setter
    def umlstatemachineselect_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__umlstatemachineselect_State", None)
        self.__umlstatemachineselect_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Behavior35"):
                opp_val = getattr(old_value, "umlstatemachineselect_Behavior35", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Behavior35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Behavior35"):
                opp_val = getattr(value, "umlstatemachineselect_Behavior35", None)
                setattr(value, "umlstatemachineselect_Behavior35", self)

    @property
    def umlstatemachineselect_State46(self):
        return self.__umlstatemachineselect_State46

    @umlstatemachineselect_State46.setter
    def umlstatemachineselect_State46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__umlstatemachineselect_State46", None)
        self.__umlstatemachineselect_State46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlstatemachineselect_Trigger47"):
                    opp_val = getattr(item, "umlstatemachineselect_Trigger47", None)
                    
                    if opp_val == self:
                        setattr(item, "umlstatemachineselect_Trigger47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlstatemachineselect_Trigger47"):
                    opp_val = getattr(item, "umlstatemachineselect_Trigger47", None)
                    
                    setattr(item, "umlstatemachineselect_Trigger47", self)
                    

    @property
    def State51(self):
        return self.__State51

    @State51.setter
    def State51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__State51", None)
        self.__State51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection"):
                opp_val = getattr(old_value, "connection", None)
                if opp_val == self:
                    setattr(old_value, "connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection"):
                opp_val = getattr(value, "connection", None)
                setattr(value, "connection", self)

    @property
    def umlstatemachineselect_State40(self):
        return self.__umlstatemachineselect_State40

    @umlstatemachineselect_State40.setter
    def umlstatemachineselect_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__umlstatemachineselect_State40", None)
        self.__umlstatemachineselect_State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Behavior41"):
                opp_val = getattr(old_value, "umlstatemachineselect_Behavior41", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Behavior41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Behavior41"):
                opp_val = getattr(value, "umlstatemachineselect_Behavior41", None)
                setattr(value, "umlstatemachineselect_Behavior41", self)

    @property
    def umlstatemachineselect_State43(self):
        return self.__umlstatemachineselect_State43

    @umlstatemachineselect_State43.setter
    def umlstatemachineselect_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__umlstatemachineselect_State43", None)
        self.__umlstatemachineselect_State43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Constraint44"):
                opp_val = getattr(old_value, "umlstatemachineselect_Constraint44", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Constraint44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Constraint44"):
                opp_val = getattr(value, "umlstatemachineselect_Constraint44", None)
                setattr(value, "umlstatemachineselect_Constraint44", self)

    @property
    def state31(self):
        return self.__state31

    @state31.setter
    def state31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__state31", None)
        self.__state31 = value if value is not None else set()
        
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
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__submachineState", None)
        self.__submachineState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine33"):
                opp_val = getattr(old_value, "StateMachine33", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine33"):
                opp_val = getattr(value, "StateMachine33", None)
                setattr(value, "StateMachine33", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachine"):
                opp_val = getattr(old_value, "submachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachine"):
                opp_val = getattr(value, "submachine", None)
                if opp_val is None:
                    setattr(value, "submachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_State__State10", None)
        self.__State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region9"):
                opp_val = getattr(old_value, "region9", None)
                if opp_val == self:
                    setattr(old_value, "region9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region9"):
                opp_val = getattr(value, "region9", None)
                setattr(value, "region9", self)

class umlstatemachineselect_Transition:

    def __init__(self, kind: str, Transition: "umlstatemachineselect_Region" = None, incoming: "umlstatemachineselect_Vertex" = None, outgoing: "umlstatemachineselect_Vertex" = None, umlstatemachineselect_Transition: "umlstatemachineselect_Behavior" = None, umlstatemachineselect_Transition25: "umlstatemachineselect_Constraint" = None, umlstatemachineselect_Transition27: set["umlstatemachineselect_Trigger"] = None, Transition14: "umlstatemachineselect_Vertex" = None, Transition16: "umlstatemachineselect_Vertex" = None, transition: "umlstatemachineselect_Region" = None):
        self.kind = kind
        self.Transition = Transition
        self.incoming = incoming
        self.outgoing = outgoing
        self.umlstatemachineselect_Transition = umlstatemachineselect_Transition
        self.umlstatemachineselect_Transition25 = umlstatemachineselect_Transition25
        self.umlstatemachineselect_Transition27 = umlstatemachineselect_Transition27 if umlstatemachineselect_Transition27 is not None else set()
        self.Transition14 = Transition14
        self.Transition16 = Transition16
        self.transition = transition
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def umlstatemachineselect_Transition(self):
        return self.__umlstatemachineselect_Transition

    @umlstatemachineselect_Transition.setter
    def umlstatemachineselect_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__umlstatemachineselect_Transition", None)
        self.__umlstatemachineselect_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Behavior"):
                opp_val = getattr(old_value, "umlstatemachineselect_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Behavior"):
                opp_val = getattr(value, "umlstatemachineselect_Behavior", None)
                setattr(value, "umlstatemachineselect_Behavior", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region18"):
                opp_val = getattr(old_value, "Region18", None)
                if opp_val == self:
                    setattr(old_value, "Region18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region18"):
                opp_val = getattr(value, "Region18", None)
                setattr(value, "Region18", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container7"):
                opp_val = getattr(old_value, "container7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container7"):
                opp_val = getattr(value, "container7", None)
                if opp_val is None:
                    setattr(value, "container7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlstatemachineselect_Transition27(self):
        return self.__umlstatemachineselect_Transition27

    @umlstatemachineselect_Transition27.setter
    def umlstatemachineselect_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__umlstatemachineselect_Transition27", None)
        self.__umlstatemachineselect_Transition27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlstatemachineselect_Trigger"):
                    opp_val = getattr(item, "umlstatemachineselect_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "umlstatemachineselect_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlstatemachineselect_Trigger"):
                    opp_val = getattr(item, "umlstatemachineselect_Trigger", None)
                    
                    setattr(item, "umlstatemachineselect_Trigger", self)
                    

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__outgoing", None)
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
    def Transition14(self):
        return self.__Transition14

    @Transition14.setter
    def Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__Transition14", None)
        self.__Transition14 = value
        
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

    @property
    def Transition16(self):
        return self.__Transition16

    @Transition16.setter
    def Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__Transition16", None)
        self.__Transition16 = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex20"):
                opp_val = getattr(old_value, "Vertex20", None)
                if opp_val == self:
                    setattr(old_value, "Vertex20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex20"):
                opp_val = getattr(value, "Vertex20", None)
                setattr(value, "Vertex20", self)

    @property
    def umlstatemachineselect_Transition25(self):
        return self.__umlstatemachineselect_Transition25

    @umlstatemachineselect_Transition25.setter
    def umlstatemachineselect_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlstatemachineselect_Transition__umlstatemachineselect_Transition25", None)
        self.__umlstatemachineselect_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlstatemachineselect_Constraint"):
                opp_val = getattr(old_value, "umlstatemachineselect_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "umlstatemachineselect_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlstatemachineselect_Constraint"):
                opp_val = getattr(value, "umlstatemachineselect_Constraint", None)
                setattr(value, "umlstatemachineselect_Constraint", self)

class umlstatemachineselect_Vertex(ABC):

    pass
class umlstatemachineselect_Region:

    pass
class Behavior:

    pass
class umlstatemachineselect_StateMachine(Behavior):

    pass