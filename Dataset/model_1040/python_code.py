from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class fsm_RelationalExpression(Expression):

    pass
class Literal:

    pass
class fsm_Real(Literal):

    pass
class fsm_String(Literal):

    pass
class fsm_VarRef(Literal):

    def __init__(self, varId: str):
        self.varId = varId
        
    @property
    def varId(self) -> str:
        return self.__varId

    @varId.setter
    def varId(self, varId: str):
        self.__varId = varId

class fsm_Boolean(Literal):

    pass
class fsm_Integer(Literal):

    pass
class fsm_Literal(Expression):

    pass
class fsm_ArithmeticExpression(Expression):

    pass
class Statement:

    pass
class fsm_VarDecl(Statement):

    pass
class fsm_Assignation(Statement):

    pass
class fsm_Context:

    pass
class State:

    pass
class fsm_FinalState(State):

    pass
class fsm_Conditional(Statement):

    pass
class fsm_Expression(ABC):

    pass
class fsm_Loop(Statement):

    pass
class Trigger:

    pass
class fsm_AndTrigger(Trigger):

    pass
class fsm_NotTrigger(Trigger):

    pass
class Pseudostate:

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_ShallowHistory(Pseudostate):

    pass
class fsm_Junction(Pseudostate):

    pass
class fsm_DeepHistory(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_Condition(Pseudostate):

    pass
class fsm_InitialState(Pseudostate):

    pass
class fsm_OrTrigger(Trigger):

    pass
class fsm_Block(Statement):

    pass
class AbstractState:

    pass
class fsm_Pseudostate(AbstractState):

    pass
class fsm_State(AbstractState):

    pass
class fsm_Transition:

    pass
class fsm_AbstractState(ABC):

    pass
class fsm_Constraint:

    pass
class fsm_Statement(ABC):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None, fsm_Trigger30: "fsm_OrTrigger" = None, fsm_Trigger33: "fsm_OrTrigger" = None, fsm_Trigger23: "fsm_NotTrigger" = None, fsm_Trigger25: "fsm_AndTrigger" = None, fsm_Trigger28: "fsm_AndTrigger" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        self.fsm_Trigger30 = fsm_Trigger30
        self.fsm_Trigger33 = fsm_Trigger33
        self.fsm_Trigger23 = fsm_Trigger23
        self.fsm_Trigger25 = fsm_Trigger25
        self.fsm_Trigger28 = fsm_Trigger28
        
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
            if hasattr(old_value, "fsm_Transition13"):
                opp_val = getattr(old_value, "fsm_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition13"):
                opp_val = getattr(value, "fsm_Transition13", None)
                setattr(value, "fsm_Transition13", self)

    @property
    def fsm_Trigger25(self):
        return self.__fsm_Trigger25

    @fsm_Trigger25.setter
    def fsm_Trigger25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger25", None)
        self.__fsm_Trigger25 = value
        
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
    def fsm_Trigger33(self):
        return self.__fsm_Trigger33

    @fsm_Trigger33.setter
    def fsm_Trigger33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger33", None)
        self.__fsm_Trigger33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_OrTrigger32"):
                opp_val = getattr(old_value, "fsm_OrTrigger32", None)
                if opp_val == self:
                    setattr(old_value, "fsm_OrTrigger32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_OrTrigger32"):
                opp_val = getattr(value, "fsm_OrTrigger32", None)
                setattr(value, "fsm_OrTrigger32", self)

    @property
    def fsm_Trigger23(self):
        return self.__fsm_Trigger23

    @fsm_Trigger23.setter
    def fsm_Trigger23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger23", None)
        self.__fsm_Trigger23 = value
        
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
    def fsm_Trigger30(self):
        return self.__fsm_Trigger30

    @fsm_Trigger30.setter
    def fsm_Trigger30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger30", None)
        self.__fsm_Trigger30 = value
        
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
    def fsm_Trigger28(self):
        return self.__fsm_Trigger28

    @fsm_Trigger28.setter
    def fsm_Trigger28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger28", None)
        self.__fsm_Trigger28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AndTrigger27"):
                opp_val = getattr(old_value, "fsm_AndTrigger27", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AndTrigger27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AndTrigger27"):
                opp_val = getattr(value, "fsm_AndTrigger27", None)
                setattr(value, "fsm_AndTrigger27", self)

class fsm_Region:

    pass
class fsm_StateMachine:

    pass