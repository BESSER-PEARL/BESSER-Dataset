from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArithmeticOperator(Enum):
    plus = "plus"
    minus = "minus"
    mult = "mult"
    div = "div"
class RelationalOperator(Enum):
    lessThan = "lessThan"
    greaterThan = "greaterThan"
    equals = "equals"
    notEqual = "notEqual"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"


############################################
# Definition of Classes
############################################

class Trigger:

    pass
class CompleteDSLPckg_OrTrigger(Trigger):

    pass
class CompleteDSLPckg_NotTrigger(Trigger):

    pass
class CompleteDSLPckg_NamedElement:

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
class CompleteDSLPckg_FinalState(State):

    pass
class Pseudostate:

    pass
class CompleteDSLPckg_InitialState(Pseudostate):

    pass
class CompleteDSLPckg_AndTrigger(Trigger):

    pass
class CompleteDSLPckg_Trigger:

    def __init__(self, expression: str, CompleteDSLPckg_Trigger: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Trigger61: "CompleteDSLPckg_NotTrigger" = None, CompleteDSLPckg_Trigger63: "CompleteDSLPckg_AndTrigger" = None, CompleteDSLPckg_Trigger66: "CompleteDSLPckg_AndTrigger" = None, CompleteDSLPckg_Trigger68: "CompleteDSLPckg_OrTrigger" = None, CompleteDSLPckg_Trigger71: "CompleteDSLPckg_OrTrigger" = None):
        self.expression = expression
        self.CompleteDSLPckg_Trigger = CompleteDSLPckg_Trigger
        self.CompleteDSLPckg_Trigger61 = CompleteDSLPckg_Trigger61
        self.CompleteDSLPckg_Trigger63 = CompleteDSLPckg_Trigger63
        self.CompleteDSLPckg_Trigger66 = CompleteDSLPckg_Trigger66
        self.CompleteDSLPckg_Trigger68 = CompleteDSLPckg_Trigger68
        self.CompleteDSLPckg_Trigger71 = CompleteDSLPckg_Trigger71
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def CompleteDSLPckg_Trigger66(self):
        return self.__CompleteDSLPckg_Trigger66

    @CompleteDSLPckg_Trigger66.setter
    def CompleteDSLPckg_Trigger66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger66", None)
        self.__CompleteDSLPckg_Trigger66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_AndTrigger65"):
                opp_val = getattr(old_value, "CompleteDSLPckg_AndTrigger65", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_AndTrigger65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_AndTrigger65"):
                opp_val = getattr(value, "CompleteDSLPckg_AndTrigger65", None)
                setattr(value, "CompleteDSLPckg_AndTrigger65", self)

    @property
    def CompleteDSLPckg_Trigger61(self):
        return self.__CompleteDSLPckg_Trigger61

    @CompleteDSLPckg_Trigger61.setter
    def CompleteDSLPckg_Trigger61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger61", None)
        self.__CompleteDSLPckg_Trigger61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_NotTrigger"):
                opp_val = getattr(old_value, "CompleteDSLPckg_NotTrigger", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_NotTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_NotTrigger"):
                opp_val = getattr(value, "CompleteDSLPckg_NotTrigger", None)
                setattr(value, "CompleteDSLPckg_NotTrigger", self)

    @property
    def CompleteDSLPckg_Trigger(self):
        return self.__CompleteDSLPckg_Trigger

    @CompleteDSLPckg_Trigger.setter
    def CompleteDSLPckg_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger", None)
        self.__CompleteDSLPckg_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition53"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition53", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition53"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition53", None)
                setattr(value, "CompleteDSLPckg_Transition53", self)

    @property
    def CompleteDSLPckg_Trigger63(self):
        return self.__CompleteDSLPckg_Trigger63

    @CompleteDSLPckg_Trigger63.setter
    def CompleteDSLPckg_Trigger63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger63", None)
        self.__CompleteDSLPckg_Trigger63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_AndTrigger"):
                opp_val = getattr(old_value, "CompleteDSLPckg_AndTrigger", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_AndTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_AndTrigger"):
                opp_val = getattr(value, "CompleteDSLPckg_AndTrigger", None)
                setattr(value, "CompleteDSLPckg_AndTrigger", self)

    @property
    def CompleteDSLPckg_Trigger71(self):
        return self.__CompleteDSLPckg_Trigger71

    @CompleteDSLPckg_Trigger71.setter
    def CompleteDSLPckg_Trigger71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger71", None)
        self.__CompleteDSLPckg_Trigger71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OrTrigger70"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OrTrigger70", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OrTrigger70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OrTrigger70"):
                opp_val = getattr(value, "CompleteDSLPckg_OrTrigger70", None)
                setattr(value, "CompleteDSLPckg_OrTrigger70", self)

    @property
    def CompleteDSLPckg_Trigger68(self):
        return self.__CompleteDSLPckg_Trigger68

    @CompleteDSLPckg_Trigger68.setter
    def CompleteDSLPckg_Trigger68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Trigger__CompleteDSLPckg_Trigger68", None)
        self.__CompleteDSLPckg_Trigger68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OrTrigger"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OrTrigger", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OrTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OrTrigger"):
                opp_val = getattr(value, "CompleteDSLPckg_OrTrigger", None)
                setattr(value, "CompleteDSLPckg_OrTrigger", self)

class AbstractState:

    pass
class CompleteDSLPckg_Pseudostate(AbstractState):

    pass
class CompleteDSLPckg_State(AbstractState):

    pass
class NamedElement:

    pass
class CompleteDSLPckg_Region(NamedElement):

    pass
class CompleteDSLPckg_StateMachine(NamedElement):

    pass
class CompleteDSLPckg_Transition(NamedElement):

    pass
class CompleteDSLPckg_AbstractState(NamedElement):

    pass
class ConsoleOutput:

    pass
class CompleteDSLPckg_Print(ConsoleOutput):

    pass
class CompleteDSLPckg_Println(ConsoleOutput):

    pass
class Statement:

    pass
class CompleteDSLPckg_Loop(Statement):

    pass
class CompleteDSLPckg_Assignation(Statement):

    pass
class CompleteDSLPckg_VarDecl(Statement):

    def __init__(self, name: str, CompleteDSLPckg_VarDecl: "CompleteDSLPckg_Expression" = None, CompleteDSLPckg_VarDecl23: "CompleteDSLPckg_Assignation" = None):
        self.name = name
        self.CompleteDSLPckg_VarDecl = CompleteDSLPckg_VarDecl
        self.CompleteDSLPckg_VarDecl23 = CompleteDSLPckg_VarDecl23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompleteDSLPckg_VarDecl(self):
        return self.__CompleteDSLPckg_VarDecl

    @CompleteDSLPckg_VarDecl.setter
    def CompleteDSLPckg_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_VarDecl__CompleteDSLPckg_VarDecl", None)
        self.__CompleteDSLPckg_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Expression21"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Expression21"):
                opp_val = getattr(value, "CompleteDSLPckg_Expression21", None)
                setattr(value, "CompleteDSLPckg_Expression21", self)

    @property
    def CompleteDSLPckg_VarDecl23(self):
        return self.__CompleteDSLPckg_VarDecl23

    @CompleteDSLPckg_VarDecl23.setter
    def CompleteDSLPckg_VarDecl23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_VarDecl__CompleteDSLPckg_VarDecl23", None)
        self.__CompleteDSLPckg_VarDecl23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Assignation"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Assignation", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Assignation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Assignation"):
                opp_val = getattr(value, "CompleteDSLPckg_Assignation", None)
                setattr(value, "CompleteDSLPckg_Assignation", self)

class CompleteDSLPckg_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
    @property
    def miliseconds(self) -> str:
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds

class CompleteDSLPckg_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

class CompleteDSLPckg_Conditional(Statement):

    pass
class CompleteDSLPckg_Statement(ABC):

    pass
class CompleteDSLPckg_Block:

    pass
class Literal:

    pass
class CompleteDSLPckg_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class CompleteDSLPckg_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CompleteDSLPckg_IntegerLit(Literal):

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
class CompleteDSLPckg_VarRef(Expression):

    def __init__(self, ref: str):
        self.ref = ref
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

class CompleteDSLPckg_ArithmeticExpression(Expression):

    def __init__(self, operator: str, CompleteDSLPckg_ArithmeticExpression: "CompleteDSLPckg_Expression" = None, CompleteDSLPckg_ArithmeticExpression2: "CompleteDSLPckg_Expression" = None):
        self.operator = operator
        self.CompleteDSLPckg_ArithmeticExpression = CompleteDSLPckg_ArithmeticExpression
        self.CompleteDSLPckg_ArithmeticExpression2 = CompleteDSLPckg_ArithmeticExpression2
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def CompleteDSLPckg_ArithmeticExpression(self):
        return self.__CompleteDSLPckg_ArithmeticExpression

    @CompleteDSLPckg_ArithmeticExpression.setter
    def CompleteDSLPckg_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ArithmeticExpression__CompleteDSLPckg_ArithmeticExpression", None)
        self.__CompleteDSLPckg_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Expression"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Expression", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Expression"):
                opp_val = getattr(value, "CompleteDSLPckg_Expression", None)
                setattr(value, "CompleteDSLPckg_Expression", self)

    @property
    def CompleteDSLPckg_ArithmeticExpression2(self):
        return self.__CompleteDSLPckg_ArithmeticExpression2

    @CompleteDSLPckg_ArithmeticExpression2.setter
    def CompleteDSLPckg_ArithmeticExpression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ArithmeticExpression__CompleteDSLPckg_ArithmeticExpression2", None)
        self.__CompleteDSLPckg_ArithmeticExpression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Expression3"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Expression3", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Expression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Expression3"):
                opp_val = getattr(value, "CompleteDSLPckg_Expression3", None)
                setattr(value, "CompleteDSLPckg_Expression3", self)

class CompleteDSLPckg_RelationalExpression(Expression):

    def __init__(self, operator: str, CompleteDSLPckg_RelationalExpression: "CompleteDSLPckg_Expression" = None, CompleteDSLPckg_RelationalExpression7: "CompleteDSLPckg_Expression" = None):
        self.operator = operator
        self.CompleteDSLPckg_RelationalExpression = CompleteDSLPckg_RelationalExpression
        self.CompleteDSLPckg_RelationalExpression7 = CompleteDSLPckg_RelationalExpression7
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def CompleteDSLPckg_RelationalExpression(self):
        return self.__CompleteDSLPckg_RelationalExpression

    @CompleteDSLPckg_RelationalExpression.setter
    def CompleteDSLPckg_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RelationalExpression__CompleteDSLPckg_RelationalExpression", None)
        self.__CompleteDSLPckg_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Expression5"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Expression5", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Expression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Expression5"):
                opp_val = getattr(value, "CompleteDSLPckg_Expression5", None)
                setattr(value, "CompleteDSLPckg_Expression5", self)

    @property
    def CompleteDSLPckg_RelationalExpression7(self):
        return self.__CompleteDSLPckg_RelationalExpression7

    @CompleteDSLPckg_RelationalExpression7.setter
    def CompleteDSLPckg_RelationalExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RelationalExpression__CompleteDSLPckg_RelationalExpression7", None)
        self.__CompleteDSLPckg_RelationalExpression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Expression8"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Expression8"):
                opp_val = getattr(value, "CompleteDSLPckg_Expression8", None)
                setattr(value, "CompleteDSLPckg_Expression8", self)

class CompleteDSLPckg_Literal(Expression):

    pass
class CompleteDSLPckg_Expression(ABC):

    pass