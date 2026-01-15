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

class errorstm_StateMachine:

    pass
class AbstractState:

    pass
class errorstm_InitialState(AbstractState):

    pass
class errorstm_SimpleState(AbstractState):

    pass
class errorstm_FinalState(AbstractState):

    pass
class errorstm_CompositeState(AbstractState):

    pass
class errorstm_Action:

    def __init__(self, kind: str, errorstm_Action: "errorstm_AbstractState" = None):
        self.kind = kind
        self.errorstm_Action = errorstm_Action
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def errorstm_Action(self):
        return self.__errorstm_Action

    @errorstm_Action.setter
    def errorstm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Action__errorstm_Action", None)
        self.__errorstm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorstm_AbstractState"):
                opp_val = getattr(old_value, "errorstm_AbstractState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorstm_AbstractState"):
                opp_val = getattr(value, "errorstm_AbstractState", None)
                if opp_val is None:
                    setattr(value, "errorstm_AbstractState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errorstm_AbstractState(ABC):

    def __init__(self, name: str, AbstractState: "errorstm_Transition" = None, from: set["errorstm_Transition"] = None, errorstm_AbstractState: set["errorstm_Action"] = None, errorstm_AbstractState8: "errorstm_CompositeState" = None, AbstractState2: "errorstm_Transition" = None, to: set["errorstm_Transition"] = None):
        self.name = name
        self.AbstractState = AbstractState
        self.from = from if from is not None else set()
        self.errorstm_AbstractState = errorstm_AbstractState if errorstm_AbstractState is not None else set()
        self.errorstm_AbstractState8 = errorstm_AbstractState8
        self.AbstractState2 = AbstractState2
        self.to = to if to is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errorstm_AbstractState8(self):
        return self.__errorstm_AbstractState8

    @errorstm_AbstractState8.setter
    def errorstm_AbstractState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__errorstm_AbstractState8", None)
        self.__errorstm_AbstractState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorstm_CompositeState"):
                opp_val = getattr(old_value, "errorstm_CompositeState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorstm_CompositeState"):
                opp_val = getattr(value, "errorstm_CompositeState", None)
                if opp_val is None:
                    setattr(value, "errorstm_CompositeState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def errorstm_AbstractState(self):
        return self.__errorstm_AbstractState

    @errorstm_AbstractState.setter
    def errorstm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__errorstm_AbstractState", None)
        self.__errorstm_AbstractState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errorstm_Action"):
                    opp_val = getattr(item, "errorstm_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "errorstm_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errorstm_Action"):
                    opp_val = getattr(item, "errorstm_Action", None)
                    
                    setattr(item, "errorstm_Action", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def AbstractState2(self):
        return self.__AbstractState2

    @AbstractState2.setter
    def AbstractState2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__AbstractState2", None)
        self.__AbstractState2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

class errorstm_Transition:

    def __init__(self, event: str, guard: str, name: str, outgoing: "errorstm_AbstractState" = None, Transition5: "errorstm_AbstractState" = None, errorstm_Transition: "errorstm_CompositeState" = None, incoming: "errorstm_AbstractState" = None, Transition: "errorstm_AbstractState" = None):
        self.event = event
        self.guard = guard
        self.name = name
        self.outgoing = outgoing
        self.Transition5 = Transition5
        self.errorstm_Transition = errorstm_Transition
        self.incoming = incoming
        self.Transition = Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def errorstm_Transition(self):
        return self.__errorstm_Transition

    @errorstm_Transition.setter
    def errorstm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Transition__errorstm_Transition", None)
        self.__errorstm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorstm_CompositeState10"):
                opp_val = getattr(old_value, "errorstm_CompositeState10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorstm_CompositeState10"):
                opp_val = getattr(value, "errorstm_CompositeState10", None)
                if opp_val is None:
                    setattr(value, "errorstm_CompositeState10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Transition__Transition", None)
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Transition__incoming", None)
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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Transition__Transition5", None)
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorstm_Transition__outgoing", None)
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
