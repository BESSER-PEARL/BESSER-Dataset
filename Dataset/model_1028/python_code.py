from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Statement:

    pass
class State:

    pass
class fsm_FinalState(State):

    pass
class Pseudostate:

    pass
class fsm_DeepHistory(Pseudostate):

    pass
class fsm_ShallowHistory(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_Choice(Pseudostate):

    pass
class fsm_Junction(Pseudostate):

    pass
class fsm_InitialState(Pseudostate):

    pass
class Trigger:

    pass
class fsm_AndTrigger(Trigger):

    pass
class fsm_Constraint:

    pass
class fsm_Statement(ABC):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None, fsm_Trigger40: "fsm_AndTrigger" = None, fsm_Trigger43: "fsm_AndTrigger" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        self.fsm_Trigger40 = fsm_Trigger40
        self.fsm_Trigger43 = fsm_Trigger43
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def fsm_Trigger40(self):
        return self.__fsm_Trigger40

    @fsm_Trigger40.setter
    def fsm_Trigger40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger40", None)
        self.__fsm_Trigger40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AndTrigger"):
                opp_val = getattr(old_value, "fsm_AndTrigger", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AndTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AndTrigger"):
                opp_val = getattr(value, "fsm_AndTrigger", None)
                setattr(value, "fsm_AndTrigger", self)

    @property
    def fsm_Trigger(self):
        return self.__fsm_Trigger

    @fsm_Trigger.setter
    def fsm_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger", None)
        self.__fsm_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition28"):
                opp_val = getattr(old_value, "fsm_Transition28", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition28"):
                opp_val = getattr(value, "fsm_Transition28", None)
                setattr(value, "fsm_Transition28", self)

    @property
    def fsm_Trigger43(self):
        return self.__fsm_Trigger43

    @fsm_Trigger43.setter
    def fsm_Trigger43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger43", None)
        self.__fsm_Trigger43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AndTrigger42"):
                opp_val = getattr(old_value, "fsm_AndTrigger42", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AndTrigger42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AndTrigger42"):
                opp_val = getattr(value, "fsm_AndTrigger42", None)
                setattr(value, "fsm_AndTrigger42", self)

class fsm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fsm_Program(Statement):

    pass
class AbstractState:

    pass
class fsm_Pseudostate(AbstractState):

    pass
class fsm_State(AbstractState):

    pass
class NamedElement:

    pass
class fsm_AbstractState(NamedElement):

    pass
class fsm_Transition(NamedElement):

    pass
class fsm_Region(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass