from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionKind(Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"


############################################
# Definition of Classes
############################################

class statechart_StateMachine:

    pass
class AbstractState:

    pass
class statechart_InitialState(AbstractState):

    pass
class statechart_FinalState(AbstractState):

    pass
class statechart_SimpleState(AbstractState):

    pass
class statechart_CompositeState(AbstractState):

    pass
class statechart_Action:

    def __init__(self, kind: str, statechart_Action: "statechart_AbstractState" = None):
        self.kind = kind
        self.statechart_Action = statechart_Action
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def statechart_Action(self):
        return self.__statechart_Action

    @statechart_Action.setter
    def statechart_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Action__statechart_Action", None)
        self.__statechart_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_AbstractState"):
                opp_val = getattr(old_value, "statechart_AbstractState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_AbstractState"):
                opp_val = getattr(value, "statechart_AbstractState", None)
                if opp_val is None:
                    setattr(value, "statechart_AbstractState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ModelElement:

    pass
class statechart_AbstractState(ModelElement):

    pass
class statechart_Transition(ModelElement):

    def __init__(self, event: str, guard: str, outgoing: "statechart_AbstractState" = None, incoming: "statechart_AbstractState" = None, Transition: "statechart_AbstractState" = None, Transition5: "statechart_AbstractState" = None, statechart_Transition: "statechart_CompositeState" = None):
        self.event = event
        self.guard = guard
        self.outgoing = outgoing
        self.incoming = incoming
        self.Transition = Transition
        self.Transition5 = Transition5
        self.statechart_Transition = statechart_Transition
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState2"):
                opp_val = getattr(old_value, "AbstractState2", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState2"):
                opp_val = getattr(value, "AbstractState2", None)
                setattr(value, "AbstractState2", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState"):
                opp_val = getattr(old_value, "AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState"):
                opp_val = getattr(value, "AbstractState", None)
                setattr(value, "AbstractState", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart_Transition(self):
        return self.__statechart_Transition

    @statechart_Transition.setter
    def statechart_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__statechart_Transition", None)
        self.__statechart_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_CompositeState10"):
                opp_val = getattr(old_value, "statechart_CompositeState10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_CompositeState10"):
                opp_val = getattr(value, "statechart_CompositeState10", None)
                if opp_val is None:
                    setattr(value, "statechart_CompositeState10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart_ModelElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
