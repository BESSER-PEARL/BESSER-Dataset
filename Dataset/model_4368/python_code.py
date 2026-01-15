from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Operator:

    pass
class klangexpr_BinaryOperator(Operator):

    pass
class klangexpr_UnaryOperator(Operator):

    pass
class Expression:

    pass
class klangexpr_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class klangexpr_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class klangexpr_Operator(Expression):

    pass
class klangexpr_IntegerLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class klangexpr_VariableReference(Expression):

    def __init__(self, variableName: str):
        self.variableName = variableName
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class klangexpr_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class UnaryOperator:

    pass
class klangexpr_ToInt(UnaryOperator):

    pass
class klangexpr_UnaryMinus(UnaryOperator):

    pass
class klangexpr_ToDouble(UnaryOperator):

    pass
class klangexpr_Not(UnaryOperator):

    pass
class BinaryOperator:

    pass
class klangexpr_Multiply(BinaryOperator):

    pass
class klangexpr_Plus(BinaryOperator):

    pass
class klangexpr_And(BinaryOperator):

    pass
class klangexpr_LessThanOrEqual(BinaryOperator):

    pass
class klangexpr_Equal(BinaryOperator):

    pass
class klangexpr_Minus(BinaryOperator):

    pass
class klangexpr_LessThan(BinaryOperator):

    pass
class klangexpr_Divide(BinaryOperator):

    pass
class klangexpr_GreaterThanOrEqual(BinaryOperator):

    pass
class klangexpr_GreaterThan(BinaryOperator):

    pass
class klangexpr_Or(BinaryOperator):

    pass
class klangexpr_Statement:

    pass
class klangexpr_Expression:

    pass
class Statement:

    pass
class klangexpr_If(Statement):

    pass
class klangexpr_ForeverLoop(Statement):

    pass
class klangexpr_Sleep(Statement):

    pass
class klangexpr_FunctionCall(Expression, Statement):

    def __init__(self, name: str, klangexpr_FunctionCall: set["klangexpr_Expression"] = None):
        self.name = name
        self.klangexpr_FunctionCall = klangexpr_FunctionCall if klangexpr_FunctionCall is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def klangexpr_FunctionCall(self):
        return self.__klangexpr_FunctionCall

    @klangexpr_FunctionCall.setter
    def klangexpr_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klangexpr_FunctionCall__klangexpr_FunctionCall", None)
        self.__klangexpr_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "klangexpr_Expression23"):
                    opp_val = getattr(item, "klangexpr_Expression23", None)
                    
                    if opp_val == self:
                        setattr(item, "klangexpr_Expression23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "klangexpr_Expression23"):
                    opp_val = getattr(item, "klangexpr_Expression23", None)
                    
                    setattr(item, "klangexpr_Expression23", self)
                    

class klangexpr_SendMessage(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class klangexpr_Yield(Statement):

    pass
class klangexpr_VariableAssignment(Statement):

    def __init__(self, variableName: str, klangexpr_VariableAssignment: "klangexpr_Expression" = None):
        self.variableName = variableName
        self.klangexpr_VariableAssignment = klangexpr_VariableAssignment
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def klangexpr_VariableAssignment(self):
        return self.__klangexpr_VariableAssignment

    @klangexpr_VariableAssignment.setter
    def klangexpr_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_klangexpr_VariableAssignment__klangexpr_VariableAssignment", None)
        self.__klangexpr_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "klangexpr_Expression14"):
                opp_val = getattr(old_value, "klangexpr_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "klangexpr_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "klangexpr_Expression14"):
                opp_val = getattr(value, "klangexpr_Expression14", None)
                setattr(value, "klangexpr_Expression14", self)

class klangexpr_WhileLoop(Statement):

    pass