from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "fsm_Transition10"):
                opp_val = getattr(old_value, "fsm_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition10"):
                opp_val = getattr(value, "fsm_Transition10", None)
                setattr(value, "fsm_Transition10", self)

class AbstractState:

    pass
class fsm_State(AbstractState):

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

class State:

    pass
class fsm_FinalState(State):

    pass
class Pseudostate:

    pass
class fsm_InitialState(Pseudostate):

    pass
class fsm_Pseudostate(AbstractState):

    pass
class fsm_Constraint:

    def __init__(self, fsm_Constraint: "fsm_Transition" = None):
        self.fsm_Constraint = fsm_Constraint
        
    @property
    def fsm_Constraint(self):
        return self.__fsm_Constraint

    @fsm_Constraint.setter
    def fsm_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Constraint__fsm_Constraint", None)
        self.__fsm_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition16"):
                opp_val = getattr(old_value, "fsm_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition16"):
                opp_val = getattr(value, "fsm_Transition16", None)
                setattr(value, "fsm_Transition16", self)

    def eval(self, context: str) -> bool:
        # TODO: Implement eval method
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