from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "fsm_Transition17"):
                opp_val = getattr(old_value, "fsm_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition17"):
                opp_val = getattr(value, "fsm_Transition17", None)
                setattr(value, "fsm_Transition17", self)

class fsm_Block:

    def __init__(self, fsm_Block: "fsm_State" = None, fsm_Block12: "fsm_State" = None, fsm_Block15: "fsm_State" = None):
        self.fsm_Block = fsm_Block
        self.fsm_Block12 = fsm_Block12
        self.fsm_Block15 = fsm_Block15
        
    @property
    def fsm_Block15(self):
        return self.__fsm_Block15

    @fsm_Block15.setter
    def fsm_Block15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Block__fsm_Block15", None)
        self.__fsm_Block15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State14"):
                opp_val = getattr(old_value, "fsm_State14", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State14"):
                opp_val = getattr(value, "fsm_State14", None)
                setattr(value, "fsm_State14", self)

    @property
    def fsm_Block(self):
        return self.__fsm_Block

    @fsm_Block.setter
    def fsm_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Block__fsm_Block", None)
        self.__fsm_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def fsm_Block12(self):
        return self.__fsm_Block12

    @fsm_Block12.setter
    def fsm_Block12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Block__fsm_Block12", None)
        self.__fsm_Block12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State11"):
                opp_val = getattr(old_value, "fsm_State11", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State11"):
                opp_val = getattr(value, "fsm_State11", None)
                setattr(value, "fsm_State11", self)

    def evalStatement(self, context: str):
        # TODO: Implement evalStatement method
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
class fsm_Region(NamedElement):

    pass
class fsm_Transition(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass