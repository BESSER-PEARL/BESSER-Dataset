from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"


############################################
# Definition of Classes
############################################

class State:

    pass
class fsmcore_FinalState(State):

    pass
class Statement:

    pass
class fsmcore_Loop(Statement):

    pass
class fsmcore_VarDecl(Statement):

    pass
class fsmcore_Conditional(Statement):

    pass
class fsmcore_Statement(ABC):

    def __init__(self, fsmcore_Statement: "fsmcore_Program" = None):
        self.fsmcore_Statement = fsmcore_Statement
        
    @property
    def fsmcore_Statement(self):
        return self.__fsmcore_Statement

    @fsmcore_Statement.setter
    def fsmcore_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Statement__fsmcore_Statement", None)
        self.__fsmcore_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_Program32"):
                opp_val = getattr(old_value, "fsmcore_Program32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_Program32"):
                opp_val = getattr(value, "fsmcore_Program32", None)
                if opp_val is None:
                    setattr(value, "fsmcore_Program32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eval(self, context: str):
        # TODO: Implement eval method
        pass

class fsmcore_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fsmcore_Constraint:

    def __init__(self, fsmcore_Constraint: "fsmcore_Transition" = None):
        self.fsmcore_Constraint = fsmcore_Constraint
        
    @property
    def fsmcore_Constraint(self):
        return self.__fsmcore_Constraint

    @fsmcore_Constraint.setter
    def fsmcore_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Constraint__fsmcore_Constraint", None)
        self.__fsmcore_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_Transition30"):
                opp_val = getattr(old_value, "fsmcore_Transition30", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_Transition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_Transition30"):
                opp_val = getattr(value, "fsmcore_Transition30", None)
                setattr(value, "fsmcore_Transition30", self)

    def evalConstraint(self, context: str):
        # TODO: Implement evalConstraint method
        pass

class AbstractState:

    pass
class fsmcore_Pseudostate(AbstractState):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class fsmcore_State(AbstractState):

    pass
class fsmcore_Trigger:

    def __init__(self, expression: bool, fsmcore_Trigger: "fsmcore_Transition" = None):
        self.expression = expression
        self.fsmcore_Trigger = fsmcore_Trigger
        
    @property
    def expression(self) -> bool:
        return self.__expression

    @expression.setter
    def expression(self, expression: bool):
        self.__expression = expression

    @property
    def fsmcore_Trigger(self):
        return self.__fsmcore_Trigger

    @fsmcore_Trigger.setter
    def fsmcore_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Trigger__fsmcore_Trigger", None)
        self.__fsmcore_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_Transition22"):
                opp_val = getattr(old_value, "fsmcore_Transition22", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_Transition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_Transition22"):
                opp_val = getattr(value, "fsmcore_Transition22", None)
                setattr(value, "fsmcore_Transition22", self)

class fsmcore_Program:

    def __init__(self, fsmcore_Program: "fsmcore_State" = None, fsmcore_Program17: "fsmcore_State" = None, fsmcore_Program20: "fsmcore_State" = None, fsmcore_Program32: set["fsmcore_Statement"] = None):
        self.fsmcore_Program = fsmcore_Program
        self.fsmcore_Program17 = fsmcore_Program17
        self.fsmcore_Program20 = fsmcore_Program20
        self.fsmcore_Program32 = fsmcore_Program32 if fsmcore_Program32 is not None else set()
        
    @property
    def fsmcore_Program(self):
        return self.__fsmcore_Program

    @fsmcore_Program.setter
    def fsmcore_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Program__fsmcore_Program", None)
        self.__fsmcore_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_State"):
                opp_val = getattr(old_value, "fsmcore_State", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_State"):
                opp_val = getattr(value, "fsmcore_State", None)
                setattr(value, "fsmcore_State", self)

    @property
    def fsmcore_Program17(self):
        return self.__fsmcore_Program17

    @fsmcore_Program17.setter
    def fsmcore_Program17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Program__fsmcore_Program17", None)
        self.__fsmcore_Program17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_State16"):
                opp_val = getattr(old_value, "fsmcore_State16", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_State16"):
                opp_val = getattr(value, "fsmcore_State16", None)
                setattr(value, "fsmcore_State16", self)

    @property
    def fsmcore_Program32(self):
        return self.__fsmcore_Program32

    @fsmcore_Program32.setter
    def fsmcore_Program32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Program__fsmcore_Program32", None)
        self.__fsmcore_Program32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmcore_Statement"):
                    opp_val = getattr(item, "fsmcore_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmcore_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmcore_Statement"):
                    opp_val = getattr(item, "fsmcore_Statement", None)
                    
                    setattr(item, "fsmcore_Statement", self)
                    

    @property
    def fsmcore_Program20(self):
        return self.__fsmcore_Program20

    @fsmcore_Program20.setter
    def fsmcore_Program20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Program__fsmcore_Program20", None)
        self.__fsmcore_Program20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_State19"):
                opp_val = getattr(old_value, "fsmcore_State19", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_State19"):
                opp_val = getattr(value, "fsmcore_State19", None)
                setattr(value, "fsmcore_State19", self)

    def eval(self, context: str):
        # TODO: Implement eval method
        pass

class NamedElement:

    pass
class fsmcore_AbstractState(NamedElement):

    pass
class fsmcore_Transition(NamedElement):

    pass
class fsmcore_Region(NamedElement):

    pass
class fsmcore_StateMachine(NamedElement):

    pass