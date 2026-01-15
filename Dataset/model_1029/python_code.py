from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Pseudostate:

    pass
class fsm_ShallowHistory(Pseudostate):

    pass
class fsm_DeepHistory(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_InitialState(Pseudostate):

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
class fsm_Conditional(Pseudostate):

    pass
class fsm_Junction(Pseudostate):

    pass
class fsm_Program(Statement):

    pass
class AbstractState:

    pass
class fsm_Pseudostate(AbstractState):

    pass
class Trigger:

    pass
class fsm_OrTrigger(Trigger):

    pass
class fsm_AndTrigger(Trigger):

    pass
class fsm_NotTrigger(Trigger):

    pass
class fsm_Constraint:

    pass
class fsm_Statement(ABC):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None, fsm_Trigger40: "fsm_NotTrigger" = None, fsm_Trigger42: "fsm_AndTrigger" = None, fsm_Trigger45: "fsm_AndTrigger" = None, fsm_Trigger47: "fsm_OrTrigger" = None, fsm_Trigger50: "fsm_OrTrigger" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        self.fsm_Trigger40 = fsm_Trigger40
        self.fsm_Trigger42 = fsm_Trigger42
        self.fsm_Trigger45 = fsm_Trigger45
        self.fsm_Trigger47 = fsm_Trigger47
        self.fsm_Trigger50 = fsm_Trigger50
        
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

    @property
    def fsm_Trigger50(self):
        return self.__fsm_Trigger50

    @fsm_Trigger50.setter
    def fsm_Trigger50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger50", None)
        self.__fsm_Trigger50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_OrTrigger49"):
                opp_val = getattr(old_value, "fsm_OrTrigger49", None)
                if opp_val == self:
                    setattr(old_value, "fsm_OrTrigger49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_OrTrigger49"):
                opp_val = getattr(value, "fsm_OrTrigger49", None)
                setattr(value, "fsm_OrTrigger49", self)

    @property
    def fsm_Trigger45(self):
        return self.__fsm_Trigger45

    @fsm_Trigger45.setter
    def fsm_Trigger45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger45", None)
        self.__fsm_Trigger45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AndTrigger44"):
                opp_val = getattr(old_value, "fsm_AndTrigger44", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AndTrigger44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AndTrigger44"):
                opp_val = getattr(value, "fsm_AndTrigger44", None)
                setattr(value, "fsm_AndTrigger44", self)

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
            if hasattr(old_value, "fsm_NotTrigger"):
                opp_val = getattr(old_value, "fsm_NotTrigger", None)
                if opp_val == self:
                    setattr(old_value, "fsm_NotTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_NotTrigger"):
                opp_val = getattr(value, "fsm_NotTrigger", None)
                setattr(value, "fsm_NotTrigger", self)

    @property
    def fsm_Trigger42(self):
        return self.__fsm_Trigger42

    @fsm_Trigger42.setter
    def fsm_Trigger42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger42", None)
        self.__fsm_Trigger42 = value
        
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
    def fsm_Trigger47(self):
        return self.__fsm_Trigger47

    @fsm_Trigger47.setter
    def fsm_Trigger47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger47", None)
        self.__fsm_Trigger47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_OrTrigger"):
                opp_val = getattr(old_value, "fsm_OrTrigger", None)
                if opp_val == self:
                    setattr(old_value, "fsm_OrTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_OrTrigger"):
                opp_val = getattr(value, "fsm_OrTrigger", None)
                setattr(value, "fsm_OrTrigger", self)

class fsm_State(AbstractState):

    pass
class NamedElement:

    pass
class fsm_Transition(NamedElement):

    pass
class fsm_AbstractState(NamedElement):

    pass
class fsm_Region(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass