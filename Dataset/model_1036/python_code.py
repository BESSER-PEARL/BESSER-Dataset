from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
class RelationalOperator(Enum):
    notEqual = "notEqual"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
    lessThan = "lessThan"
    greaterThan = "greaterThan"
    equals = "equals"
class ArithmeticOperator(Enum):
    plus = "plus"
    minus = "minus"
    mult = "mult"
    div = "div"


############################################
# Definition of Classes
############################################

class ConsoleOutput:

    pass
class fsm_Print(ConsoleOutput):

    pass
class fsm_Println(ConsoleOutput):

    pass
class Literal:

    pass
class fsm_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class fsm_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class fsm_IntegerLit(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Expression:

    pass
class fsm_VarReference(Expression):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class fsm_RelationalExpression(Expression):

    def __init__(self, operator: str, fsm_RelationalExpression: "fsm_Expression" = None, fsm_RelationalExpression54: "fsm_Expression" = None):
        self.operator = operator
        self.fsm_RelationalExpression = fsm_RelationalExpression
        self.fsm_RelationalExpression54 = fsm_RelationalExpression54
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def fsm_RelationalExpression54(self):
        return self.__fsm_RelationalExpression54

    @fsm_RelationalExpression54.setter
    def fsm_RelationalExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RelationalExpression__fsm_RelationalExpression54", None)
        self.__fsm_RelationalExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression55"):
                opp_val = getattr(old_value, "fsm_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression55"):
                opp_val = getattr(value, "fsm_Expression55", None)
                setattr(value, "fsm_Expression55", self)

    @property
    def fsm_RelationalExpression(self):
        return self.__fsm_RelationalExpression

    @fsm_RelationalExpression.setter
    def fsm_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RelationalExpression__fsm_RelationalExpression", None)
        self.__fsm_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression52"):
                opp_val = getattr(old_value, "fsm_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression52"):
                opp_val = getattr(value, "fsm_Expression52", None)
                setattr(value, "fsm_Expression52", self)

class fsm_ArithmeticExpression(Expression):

    def __init__(self, operator: str, fsm_ArithmeticExpression: "fsm_Expression" = None, fsm_ArithmeticExpression49: "fsm_Expression" = None):
        self.operator = operator
        self.fsm_ArithmeticExpression = fsm_ArithmeticExpression
        self.fsm_ArithmeticExpression49 = fsm_ArithmeticExpression49
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def fsm_ArithmeticExpression(self):
        return self.__fsm_ArithmeticExpression

    @fsm_ArithmeticExpression.setter
    def fsm_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_ArithmeticExpression__fsm_ArithmeticExpression", None)
        self.__fsm_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression47"):
                opp_val = getattr(old_value, "fsm_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression47"):
                opp_val = getattr(value, "fsm_Expression47", None)
                setattr(value, "fsm_Expression47", self)

    @property
    def fsm_ArithmeticExpression49(self):
        return self.__fsm_ArithmeticExpression49

    @fsm_ArithmeticExpression49.setter
    def fsm_ArithmeticExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_ArithmeticExpression__fsm_ArithmeticExpression49", None)
        self.__fsm_ArithmeticExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression50"):
                opp_val = getattr(old_value, "fsm_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression50"):
                opp_val = getattr(value, "fsm_Expression50", None)
                setattr(value, "fsm_Expression50", self)

class fsm_Literal(Expression):

    pass
class fsm_Statement(ABC):

    pass
class Statement:

    pass
class fsm_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
    @property
    def miliseconds(self) -> str:
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds

class fsm_VarDecl(Statement):

    def __init__(self, key: str, fsm_VarDecl: "fsm_Expression" = None, fsm_VarDecl57: "fsm_Assignation" = None):
        self.key = key
        self.fsm_VarDecl = fsm_VarDecl
        self.fsm_VarDecl57 = fsm_VarDecl57
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def fsm_VarDecl(self):
        return self.__fsm_VarDecl

    @fsm_VarDecl.setter
    def fsm_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_VarDecl__fsm_VarDecl", None)
        self.__fsm_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression45"):
                opp_val = getattr(old_value, "fsm_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression45"):
                opp_val = getattr(value, "fsm_Expression45", None)
                setattr(value, "fsm_Expression45", self)

    @property
    def fsm_VarDecl57(self):
        return self.__fsm_VarDecl57

    @fsm_VarDecl57.setter
    def fsm_VarDecl57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_VarDecl__fsm_VarDecl57", None)
        self.__fsm_VarDecl57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Assignation"):
                opp_val = getattr(old_value, "fsm_Assignation", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Assignation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Assignation"):
                opp_val = getattr(value, "fsm_Assignation", None)
                setattr(value, "fsm_Assignation", self)

class fsm_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

class fsm_Conditional(Statement):

    pass
class fsm_Loop(Statement):

    pass
class fsm_Assignation(Statement):

    pass
class fsm_Expression(ABC):

    pass
class Constraint:

    pass
class fsm_RelationalConstraint(Constraint):

    pass
class State:

    pass
class fsm_FinalState(State):

    pass
class fsm_Constraint(ABC):

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
            if hasattr(old_value, "fsm_Transition16"):
                opp_val = getattr(old_value, "fsm_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition16"):
                opp_val = getattr(value, "fsm_Transition16", None)
                setattr(value, "fsm_Transition16", self)

class fsm_Program(Statement):

    pass
class AbstractState:

    pass
class fsm_Pseudostate(AbstractState):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class fsm_State(AbstractState):

    pass
class fsm_Transition:

    pass
class fsm_AbstractState(ABC):

    def __init__(self, name: str, fsm_AbstractState: "fsm_StateMachine" = None, : set["fsm_Transition"] = None, 6: set["fsm_Transition"] = None, 19: "fsm_Transition" = None, 22: "fsm_Transition" = None):
        self.name = name
        self.fsm_AbstractState = fsm_AbstractState
        self. =  if  is not None else set()
        self.6 = 6 if 6 is not None else set()
        self.19 = 19
        self.22 = 22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

    @property
    def fsm_AbstractState(self):
        return self.__fsm_AbstractState

    @fsm_AbstractState.setter
    def fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__fsm_AbstractState", None)
        self.__fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine"):
                opp_val = getattr(old_value, "fsm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine"):
                opp_val = getattr(value, "fsm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

class fsm_StateMachine:

    def __init__(self, name: str, fsm_StateMachine: set["fsm_AbstractState"] = None, fsm_StateMachine2: set["fsm_Transition"] = None):
        self.name = name
        self.fsm_StateMachine = fsm_StateMachine if fsm_StateMachine is not None else set()
        self.fsm_StateMachine2 = fsm_StateMachine2 if fsm_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_StateMachine(self):
        return self.__fsm_StateMachine

    @fsm_StateMachine.setter
    def fsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine", None)
        self.__fsm_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_AbstractState"):
                    opp_val = getattr(item, "fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_AbstractState"):
                    opp_val = getattr(item, "fsm_AbstractState", None)
                    
                    setattr(item, "fsm_AbstractState", self)
                    

    @property
    def fsm_StateMachine2(self):
        return self.__fsm_StateMachine2

    @fsm_StateMachine2.setter
    def fsm_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine2", None)
        self.__fsm_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    
