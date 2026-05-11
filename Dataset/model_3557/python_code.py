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

class ConsoleOutput:

    pass
class flowchartpck_Print(ConsoleOutput):

    pass
class flowchartpck_Println(ConsoleOutput):

    pass
class Statement:

    pass
class flowchartpck_ConsoleOutput(Statement):

    def __init__(self, input: str):
        self.input = input
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


class flowchartpck_VarDecl(Statement):

    def __init__(self, key: str, flowchartpck_VarDecl42: "flowchartpck_Expression" = None, flowchartpck_VarDecl: "flowchartpck_Assignation" = None):
        self.key = key
        self.flowchartpck_VarDecl42 = flowchartpck_VarDecl42
        self.flowchartpck_VarDecl = flowchartpck_VarDecl
        
        pass
    @property
    def key(self):
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
    def flowchartpck_VarDecl42(self):
        return self.__flowchartpck_VarDecl42

    @flowchartpck_VarDecl42.setter
    def flowchartpck_VarDecl42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_VarDecl__flowchartpck_VarDecl42", None)
        self.__flowchartpck_VarDecl42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression43"):
                opp_val = getattr(old_value, "flowchartpck_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression43"):
                opp_val = getattr(value, "flowchartpck_Expression43", None)
                setattr(value, "flowchartpck_Expression43", self)

class flowchartpck_Conditional(Statement):

    pass
class flowchartpck_Loop(Statement):

    pass
class flowchartpck_Assignation(Statement):

    pass
class flowchartpck_Statement(ABC):

    pass
class flowchartpck_Wait(Statement):

    def __init__(self, miliseconds: str):
        self.miliseconds = miliseconds
        
        pass
    @property
    def miliseconds(self):
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self, miliseconds: str):
        self.__miliseconds = miliseconds


class Literal:

    pass
class flowchartpck_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class flowchartpck_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class flowchartpck_IntegerLit(Literal):

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
class flowchartpck_ArithmeticExpression(Expression):

    def __init__(self, operator: str, flowchartpck_ArithmeticExpression: "flowchartpck_Expression" = None, flowchartpck_ArithmeticExpression15: "flowchartpck_Expression" = None):
        self.operator = operator
        self.flowchartpck_ArithmeticExpression = flowchartpck_ArithmeticExpression
        self.flowchartpck_ArithmeticExpression15 = flowchartpck_ArithmeticExpression15
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def flowchartpck_ArithmeticExpression15(self):
        return self.__flowchartpck_ArithmeticExpression15

    @flowchartpck_ArithmeticExpression15.setter
    def flowchartpck_ArithmeticExpression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_ArithmeticExpression__flowchartpck_ArithmeticExpression15", None)
        self.__flowchartpck_ArithmeticExpression15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowchartpck_Expression16"):
                opp_val = getattr(old_value, "flowchartpck_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression16"):
                opp_val = getattr(value, "flowchartpck_Expression16", None)
                setattr(value, "flowchartpck_Expression16", self)

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
            if hasattr(old_value, "flowchartpck_Expression13"):
                opp_val = getattr(old_value, "flowchartpck_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "flowchartpck_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowchartpck_Expression13"):
                opp_val = getattr(value, "flowchartpck_Expression13", None)
                setattr(value, "flowchartpck_Expression13", self)

class flowchartpck_VarReference(Expression):

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class flowchartpck_Literal(Expression):

    pass
class flowchartpck_Expression:

    pass
class Constraint:

    pass
class flowchartpck_RelationalConstraint(Constraint):

    pass
class flowchartpck_Constraint:

    pass
class flowchartpck_Program(Statement):

    pass
class Node:

    pass
class flowchartpck_Start(Node):

    pass
class flowchartpck_Decision(Node):

    pass
class flowchartpck_End(Node):

    pass
class flowchartpck_Action(Node):

    pass
class flowchartpck_RelationalExpression(Expression):

    def __init__(self, operator: str, flowchartpck_RelationalExpression: "flowchartpck_Expression" = None, flowchartpck_RelationalExpression20: "flowchartpck_Expression" = None):
        self.operator = operator
        self.flowchartpck_RelationalExpression = flowchartpck_RelationalExpression
        self.flowchartpck_RelationalExpression20 = flowchartpck_RelationalExpression20
        
        pass
    @property
    def operator(self):
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
    def flowchartpck_RelationalExpression20(self):
        return self.__flowchartpck_RelationalExpression20

    @flowchartpck_RelationalExpression20.setter
    def flowchartpck_RelationalExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flowchartpck_RelationalExpression__flowchartpck_RelationalExpression20", None)
        self.__flowchartpck_RelationalExpression20 = value
        
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

class NamedElement:

    pass
class flowchartpck_Node(NamedElement):

    pass
class flowchartpck_Flowchart(NamedElement):

    pass
class flowchartpck_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class flowchartpck_Arc:

    pass