from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_Constraint:

    pass
class fsm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Statement:

    pass
class State:

    pass
class fsm_FinalState(State):

    pass
class Pseudostate:

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_ShallowHistory(Pseudostate):

    pass
class fsm_Junction(Pseudostate):

    pass
class fsm_Conditional(Pseudostate):

    pass
class fsm_InitialState(Pseudostate):

    pass
class fsm_Statement(ABC):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

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
class fsm_Region(NamedElement):

    pass
class fsm_AbstractState(NamedElement):

    pass
class fsm_Transition(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass