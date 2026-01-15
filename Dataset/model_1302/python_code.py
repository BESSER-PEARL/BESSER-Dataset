from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class PseudoStateKind(Enum):
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"


############################################
# Definition of Classes
############################################

class State:

    pass
class StateMachines_FinalState(State):

    pass
class StateMachines_Behavior:

    pass
class Vertex:

    pass
class StateMachines_State(Vertex):

    pass
class StateMachines_ConnectionPointReference(Vertex):

    pass
class StateMachines_Pseudostate(Vertex):

    def __init__(self, kind: str, StateMachines_Pseudostate: "StateMachines_State" = None, StateMachines_Pseudostate35: "StateMachines_ConnectionPointReference" = None, StateMachines_Pseudostate38: "StateMachines_ConnectionPointReference" = None):
        self.kind = kind
        self.StateMachines_Pseudostate = StateMachines_Pseudostate
        self.StateMachines_Pseudostate35 = StateMachines_Pseudostate35
        self.StateMachines_Pseudostate38 = StateMachines_Pseudostate38
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def StateMachines_Pseudostate38(self):
        return self.__StateMachines_Pseudostate38

    @StateMachines_Pseudostate38.setter
    def StateMachines_Pseudostate38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Pseudostate__StateMachines_Pseudostate38", None)
        self.__StateMachines_Pseudostate38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_ConnectionPointReference37"):
                opp_val = getattr(old_value, "StateMachines_ConnectionPointReference37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_ConnectionPointReference37"):
                opp_val = getattr(value, "StateMachines_ConnectionPointReference37", None)
                if opp_val is None:
                    setattr(value, "StateMachines_ConnectionPointReference37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachines_Pseudostate35(self):
        return self.__StateMachines_Pseudostate35

    @StateMachines_Pseudostate35.setter
    def StateMachines_Pseudostate35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Pseudostate__StateMachines_Pseudostate35", None)
        self.__StateMachines_Pseudostate35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_ConnectionPointReference34"):
                opp_val = getattr(old_value, "StateMachines_ConnectionPointReference34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_ConnectionPointReference34"):
                opp_val = getattr(value, "StateMachines_ConnectionPointReference34", None)
                if opp_val is None:
                    setattr(value, "StateMachines_ConnectionPointReference34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachines_Pseudostate(self):
        return self.__StateMachines_Pseudostate

    @StateMachines_Pseudostate.setter
    def StateMachines_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Pseudostate__StateMachines_Pseudostate", None)
        self.__StateMachines_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_State16"):
                opp_val = getattr(old_value, "StateMachines_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_State16"):
                opp_val = getattr(value, "StateMachines_State16", None)
                if opp_val is None:
                    setattr(value, "StateMachines_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachines_Trigger:

    pass
class StateMachines_Transition:

    def __init__(self, kind: str, StateMachines_Transition10: "StateMachines_Vertex" = None, StateMachines_Transition: "StateMachines_Region" = None, StateMachines_Transition7: "StateMachines_Vertex" = None, StateMachines_Transition12: set["StateMachines_Trigger"] = None):
        self.kind = kind
        self.StateMachines_Transition10 = StateMachines_Transition10
        self.StateMachines_Transition = StateMachines_Transition
        self.StateMachines_Transition7 = StateMachines_Transition7
        self.StateMachines_Transition12 = StateMachines_Transition12 if StateMachines_Transition12 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def StateMachines_Transition(self):
        return self.__StateMachines_Transition

    @StateMachines_Transition.setter
    def StateMachines_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Transition__StateMachines_Transition", None)
        self.__StateMachines_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_Region4"):
                opp_val = getattr(old_value, "StateMachines_Region4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_Region4"):
                opp_val = getattr(value, "StateMachines_Region4", None)
                if opp_val is None:
                    setattr(value, "StateMachines_Region4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachines_Transition7(self):
        return self.__StateMachines_Transition7

    @StateMachines_Transition7.setter
    def StateMachines_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Transition__StateMachines_Transition7", None)
        self.__StateMachines_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_Vertex6"):
                opp_val = getattr(old_value, "StateMachines_Vertex6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_Vertex6"):
                opp_val = getattr(value, "StateMachines_Vertex6", None)
                if opp_val is None:
                    setattr(value, "StateMachines_Vertex6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachines_Transition10(self):
        return self.__StateMachines_Transition10

    @StateMachines_Transition10.setter
    def StateMachines_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Transition__StateMachines_Transition10", None)
        self.__StateMachines_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachines_Vertex9"):
                opp_val = getattr(old_value, "StateMachines_Vertex9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachines_Vertex9"):
                opp_val = getattr(value, "StateMachines_Vertex9", None)
                if opp_val is None:
                    setattr(value, "StateMachines_Vertex9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachines_Transition12(self):
        return self.__StateMachines_Transition12

    @StateMachines_Transition12.setter
    def StateMachines_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachines_Transition__StateMachines_Transition12", None)
        self.__StateMachines_Transition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachines_Trigger"):
                    opp_val = getattr(item, "StateMachines_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachines_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachines_Trigger"):
                    opp_val = getattr(item, "StateMachines_Trigger", None)
                    
                    setattr(item, "StateMachines_Trigger", self)
                    

class StateMachines_Vertex:

    pass
class StateMachines_Region:

    pass
class StateMachines_StateMachine:

    pass