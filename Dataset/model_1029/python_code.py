from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
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
class fsm_DeepHistory(Pseudostate):

    pass
class fsm_ShallowHistory(Pseudostate):

    pass
class fsm_Conditional(Pseudostate):

    pass
class fsm_Junction(Pseudostate):

    pass
class fsm_InitialState(Pseudostate):

    pass
class Trigger:

    pass
class fsm_AndTrigger(Trigger):

    pass
class fsm_OrTrigger(Trigger):

    pass
class fsm_NotTrigger(Trigger):

    pass
class fsm_Constraint:

    pass
class fsm_Statement(ABC):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None, fsm_Trigger29: "fsm_NotTrigger" = None, fsm_Trigger31: "fsm_AndTrigger" = None, fsm_Trigger34: "fsm_AndTrigger" = None, fsm_Trigger36: "fsm_OrTrigger" = None, fsm_Trigger39: "fsm_OrTrigger" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        self.fsm_Trigger29 = fsm_Trigger29
        self.fsm_Trigger31 = fsm_Trigger31
        self.fsm_Trigger34 = fsm_Trigger34
        self.fsm_Trigger36 = fsm_Trigger36
        self.fsm_Trigger39 = fsm_Trigger39
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def fsm_Trigger29(self):
        return self.__fsm_Trigger29

    @fsm_Trigger29.setter
    def fsm_Trigger29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger29", None)
        self.__fsm_Trigger29 = value
        
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
    def fsm_Trigger31(self):
        return self.__fsm_Trigger31

    @fsm_Trigger31.setter
    def fsm_Trigger31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger31", None)
        self.__fsm_Trigger31 = value
        
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
    def fsm_Trigger39(self):
        return self.__fsm_Trigger39

    @fsm_Trigger39.setter
    def fsm_Trigger39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger39", None)
        self.__fsm_Trigger39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_OrTrigger38"):
                opp_val = getattr(old_value, "fsm_OrTrigger38", None)
                if opp_val == self:
                    setattr(old_value, "fsm_OrTrigger38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_OrTrigger38"):
                opp_val = getattr(value, "fsm_OrTrigger38", None)
                setattr(value, "fsm_OrTrigger38", self)

    @property
    def fsm_Trigger34(self):
        return self.__fsm_Trigger34

    @fsm_Trigger34.setter
    def fsm_Trigger34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger34", None)
        self.__fsm_Trigger34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AndTrigger33"):
                opp_val = getattr(old_value, "fsm_AndTrigger33", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AndTrigger33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AndTrigger33"):
                opp_val = getattr(value, "fsm_AndTrigger33", None)
                setattr(value, "fsm_AndTrigger33", self)

    @property
    def fsm_Trigger36(self):
        return self.__fsm_Trigger36

    @fsm_Trigger36.setter
    def fsm_Trigger36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger36", None)
        self.__fsm_Trigger36 = value
        
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
            if hasattr(old_value, "fsm_Transition19"):
                opp_val = getattr(old_value, "fsm_Transition19", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition19"):
                opp_val = getattr(value, "fsm_Transition19", None)
                setattr(value, "fsm_Transition19", self)

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
class fsm_Transition(NamedElement):

    pass
class fsm_AbstractState(NamedElement):

    pass
class fsm_Region(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass