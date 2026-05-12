from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationalOperator(Enum):
    notEqual = "notEqual"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
    lessThan = "lessThan"
    greaterThan = "greaterThan"
    equals = "equals"
class PseudostateKind(Enum):
    initial = "initial"
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
class fsm_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class fsm_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class fsm_IntegerLit(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Expression:

    pass
class fsm_VarReference(Expression):

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class fsm_ArithmeticExpression(Expression):

    def __init__(self, operator: str, fsm_ArithmeticExpression44: "fsm_Expression" = None, fsm_ArithmeticExpression: "fsm_Expression" = None):
        self.operator = operator
        self.fsm_ArithmeticExpression44 = fsm_ArithmeticExpression44
        self.fsm_ArithmeticExpression = fsm_ArithmeticExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def fsm_ArithmeticExpression44(self):
        return self.__fsm_ArithmeticExpression44

    @fsm_ArithmeticExpression44.setter
    def fsm_ArithmeticExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_ArithmeticExpression__fsm_ArithmeticExpression44", None)
        self.__fsm_ArithmeticExpression44 = value
        
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
    def fsm_ArithmeticExpression(self):
        return self.__fsm_ArithmeticExpression

    @fsm_ArithmeticExpression.setter
    def fsm_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_ArithmeticExpression__fsm_ArithmeticExpression", None)
        self.__fsm_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Expression42"):
                opp_val = getattr(old_value, "fsm_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression42"):
                opp_val = getattr(value, "fsm_Expression42", None)
                setattr(value, "fsm_Expression42", self)

class fsm_Literal(Expression):

    pass
class fsm_RelationalExpression(Expression):

    def __init__(self, operator: str, fsm_RelationalExpression: "fsm_Expression" = None, fsm_RelationalExpression49: "fsm_Expression" = None):
        self.operator = operator
        self.fsm_RelationalExpression = fsm_RelationalExpression
        self.fsm_RelationalExpression49 = fsm_RelationalExpression49
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
    def fsm_RelationalExpression49(self):
        return self.__fsm_RelationalExpression49

    @fsm_RelationalExpression49.setter
    def fsm_RelationalExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RelationalExpression__fsm_RelationalExpression49", None)
        self.__fsm_RelationalExpression49 = value
        
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
class Statement:

    pass
class fsm_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


class fsm_Loop(Statement):

    pass
class fsm_Conditional(Statement):

    pass
class fsm_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
        pass
    @property
    def miliseconds(self):
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds


class fsm_Assignation(Statement):

    pass
class fsm_VarDecl(Statement):

    def __init__(self, key: str, fsm_VarDecl: "fsm_Expression" = None, fsm_VarDecl52: "fsm_Assignation" = None):
        self.key = key
        self.fsm_VarDecl = fsm_VarDecl
        self.fsm_VarDecl52 = fsm_VarDecl52
        
        pass
    @property
    def key(self):
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
            if hasattr(old_value, "fsm_Expression40"):
                opp_val = getattr(old_value, "fsm_Expression40", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Expression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Expression40"):
                opp_val = getattr(value, "fsm_Expression40", None)
                setattr(value, "fsm_Expression40", self)

    @property
    def fsm_VarDecl52(self):
        return self.__fsm_VarDecl52

    @fsm_VarDecl52.setter
    def fsm_VarDecl52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_VarDecl__fsm_VarDecl52", None)
        self.__fsm_VarDecl52 = value
        
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

class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        
        pass
    @property
    def expression(self):
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
            if hasattr(old_value, "fsm_Transition14"):
                opp_val = getattr(old_value, "fsm_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition14"):
                opp_val = getattr(value, "fsm_Transition14", None)
                setattr(value, "fsm_Transition14", self)

class fsm_Constraint(ABC):

    pass
class fsm_Statement(ABC):

    pass
class fsm_Transition:

    pass
class fsm_Program(Statement):

    pass
class AbstractState:

    pass
class fsm_Pseudostate(AbstractState):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class fsm_State(AbstractState):

    pass
class fsm_AbstractState(ABC):

    def __init__(self, name: str, source: set["fsm_Transition"] = None, fsm_AbstractState: "fsm_StateMachine" = None, target: set["fsm_Transition"] = None, AbstractState: "fsm_Transition" = None, AbstractState17: "fsm_Transition" = None):
        self.name = name
        self.source = source if source is not None else set()
        self.fsm_AbstractState = fsm_AbstractState
        self.target = target if target is not None else set()
        self.AbstractState = AbstractState
        self.AbstractState17 = AbstractState17
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__target", None)
        self.__target = value if value is not None else set()
        
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
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
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
    def AbstractState17(self):
        return self.__AbstractState17

    @AbstractState17.setter
    def AbstractState17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__AbstractState17", None)
        self.__AbstractState17 = value
        
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

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__source", None)
        self.__source = value if value is not None else set()
        
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
                    

class fsm_StateMachine:

    def __init__(self, name: str, fsm_StateMachine: set["fsm_AbstractState"] = None, fsm_StateMachine2: set["fsm_Transition"] = None):
        self.name = name
        self.fsm_StateMachine = fsm_StateMachine if fsm_StateMachine is not None else set()
        self.fsm_StateMachine2 = fsm_StateMachine2 if fsm_StateMachine2 is not None else set()
        
        pass
    @property
    def name(self):
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
                    
