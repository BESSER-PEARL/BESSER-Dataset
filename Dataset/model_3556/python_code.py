from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationalOperator(Enum):
    lessThan = "lessThan"
    greaterThan = "greaterThan"
    equals = "equals"
    notEqual = "notEqual"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
class ArithmeticOperator(Enum):
    plus = "plus"
    minus = "minus"
    mult = "mult"
    div = "div"


############################################
# Definition of Classes
############################################

class Statement:

    pass
class flowchartpck_Conditional(Statement):

    pass
class flowchartpck_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

class flowchartpck_Loop(Statement):

    pass
class flowchartpck_Statement(ABC):

    pass
class flowchartpck_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
    @property
    def miliseconds(self) -> str:
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds

class flowchartpck_VarDecl(Statement):

    def __init__(self, key: str, flowchartpck_VarDecl: "flowchartpck_Assignation" = None, flowchartpck_VarDecl47: "flowchartpck_Expression" = None):
        self.key = key
        self.flowchartpck_VarDecl = flowchartpck_VarDecl
        self.flowchartpck_VarDecl47 = flowchartpck_VarDecl47
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def flowchartpck_VarDecl(self):
        return self.__flowchartpck_VarDecl

    @flowchartpck_VarDecl.setter
    def flowchartpck_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_VarDecl__flowchartpck_VarDecl", None)
        self.__flowchartpck_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Assignation"):
                opp_val = getattr(old_value, "flowchartpck_Assignation", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Assignation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Assignation"):
                opp_val = getattr(value, "flowchartpck_Assignation", None)
                setattr(value, "flowchartpck_Assignation", self)

    @property
    def flowchartpck_VarDecl47(self):
        return self.__flowchartpck_VarDecl47

    @flowchartpck_VarDecl47.setter
    def flowchartpck_VarDecl47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_VarDecl__flowchartpck_VarDecl47", None)
        self.__flowchartpck_VarDecl47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression48"):
                opp_val = getattr(old_value, "flowchartpck_Expression48", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression48"):
                opp_val = getattr(value, "flowchartpck_Expression48", None)
                setattr(value, "flowchartpck_Expression48", self)

class flowchartpck_Assignation(Statement):

    pass
class ConsoleOutput:

    pass
class flowchartpck_Print(ConsoleOutput):

    pass
class flowchartpck_Println(ConsoleOutput):

    pass
class Expression:

    pass
class flowchartpck_VarReference(Expression):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class flowchartpck_ArithmeticExpression(Expression):

    def __init__(self, operator: str, flowchartpck_ArithmeticExpression: "flowchartpck_Expression" = None, flowchartpck_ArithmeticExpression20: "flowchartpck_Expression" = None):
        self.operator = operator
        self.flowchartpck_ArithmeticExpression = flowchartpck_ArithmeticExpression
        self.flowchartpck_ArithmeticExpression20 = flowchartpck_ArithmeticExpression20
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flowchartpck_ArithmeticExpression(self):
        return self.__flowchartpck_ArithmeticExpression

    @flowchartpck_ArithmeticExpression.setter
    def flowchartpck_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_ArithmeticExpression__flowchartpck_ArithmeticExpression", None)
        self.__flowchartpck_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression18"):
                opp_val = getattr(old_value, "flowchartpck_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression18"):
                opp_val = getattr(value, "flowchartpck_Expression18", None)
                setattr(value, "flowchartpck_Expression18", self)

    @property
    def flowchartpck_ArithmeticExpression20(self):
        return self.__flowchartpck_ArithmeticExpression20

    @flowchartpck_ArithmeticExpression20.setter
    def flowchartpck_ArithmeticExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_ArithmeticExpression__flowchartpck_ArithmeticExpression20", None)
        self.__flowchartpck_ArithmeticExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression21"):
                opp_val = getattr(old_value, "flowchartpck_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression21"):
                opp_val = getattr(value, "flowchartpck_Expression21", None)
                setattr(value, "flowchartpck_Expression21", self)

class flowchartpck_RelationalExpression(Expression):

    def __init__(self, operator: str, flowchartpck_RelationalExpression: "flowchartpck_Expression" = None, flowchartpck_RelationalExpression25: "flowchartpck_Expression" = None):
        self.operator = operator
        self.flowchartpck_RelationalExpression = flowchartpck_RelationalExpression
        self.flowchartpck_RelationalExpression25 = flowchartpck_RelationalExpression25
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flowchartpck_RelationalExpression(self):
        return self.__flowchartpck_RelationalExpression

    @flowchartpck_RelationalExpression.setter
    def flowchartpck_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_RelationalExpression__flowchartpck_RelationalExpression", None)
        self.__flowchartpck_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression23"):
                opp_val = getattr(old_value, "flowchartpck_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression23"):
                opp_val = getattr(value, "flowchartpck_Expression23", None)
                setattr(value, "flowchartpck_Expression23", self)

    @property
    def flowchartpck_RelationalExpression25(self):
        return self.__flowchartpck_RelationalExpression25

    @flowchartpck_RelationalExpression25.setter
    def flowchartpck_RelationalExpression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_RelationalExpression__flowchartpck_RelationalExpression25", None)
        self.__flowchartpck_RelationalExpression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression26"):
                opp_val = getattr(old_value, "flowchartpck_Expression26", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression26"):
                opp_val = getattr(value, "flowchartpck_Expression26", None)
                setattr(value, "flowchartpck_Expression26", self)

class flowchartpck_Literal(Expression):

    pass
class flowchartpck_Expression:

    pass
class Constraint:

    pass
class flowchartpck_RelationalConstraint(Constraint):

    pass
class Literal:

    pass
class flowchartpck_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class flowchartpck_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class flowchartpck_IntegerLit(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class flowchartpck_Program(Statement):

    pass
class Node:

    pass
class flowchartpck_Start(Node):

    pass
class flowchartpck_End(Node):

    pass
class flowchartpck_Decision(Node):

    pass
class flowchartpck_Action(Node):

    pass
class flowchartpck_Constraint:

    pass
class flowchartpck_Arc:

    pass
class NamedElement:

    pass
class flowchartpck_Flowchart(NamedElement):

    pass
class flowchartpck_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class flowchartpck_Node(NamedElement):

    pass