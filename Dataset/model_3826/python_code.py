from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Value:

    pass
class logo_value_BoolValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class logo_value_IntValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class BinaryExpression:

    pass
class logo_binary_Equals(BinaryExpression):

    pass
class logo_binary_Div(BinaryExpression):

    pass
class logo_binary_Plus(BinaryExpression):

    pass
class logo_binary_Mult(BinaryExpression):

    pass
class logo_binary_Greater(BinaryExpression):

    pass
class logo_binary_Minus(BinaryExpression):

    pass
class Symbol:

    pass
class logo_symbol_Procedure(Symbol):

    pass
class logo_symbol_Variable(Symbol):

    pass
class ExtendedExpression:

    pass
class logo_extended_Or(ExtendedExpression):

    pass
class logo_extended_And(ExtendedExpression):

    pass
class logo_binary_Lower(BinaryExpression):

    pass
class UnaryExpression:

    pass
class logo_unary_Opposite(UnaryExpression):

    pass
class logo_unary_Not(UnaryExpression):

    pass
class Constant:

    pass
class logo_constant_BoolValue(Constant):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class logo_constant_IntValue(Constant):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Block:

    pass
class expression_logo_Expression:

    pass
class Expression:

    pass
class logo_expression_VariableRead(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class logo_expression_UnaryExpression(Expression):

    pass
class logo_expression_Constant(Expression):

    pass
class logo_expression_ExtendedExpression(Expression):

    pass
class logo_expression_BinaryExpression(Expression):

    pass
class ProcedureDefinition:

    pass
class statement_logo_Statement:

    pass
class ControlStatement:

    pass
class logo_control_While(ControlStatement):

    pass
class logo_control_Repeat(ControlStatement):

    pass
class logo_control_If(ControlStatement):

    pass
class statement_logo_Expression:

    pass
class Statement:

    pass
class logo_statement_ControlStatement(Statement):

    pass
class logo_statement_Forward(Statement):

    pass
class logo_statement_Left(Statement):

    pass
class logo_statement_Block(Statement):

    pass
class logo_statement_ProcedureCall(Statement):

    pass
class logo_statement_Right(Statement):

    pass
class logo_Value(ABC):

    pass
class statement_logo_Parameter:

    pass
class logo_statement_ProcedureDefinition(Statement):

    def __init__(self, name: str, logo_statement_ProcedureDefinition: set["statement_logo_Parameter"] = None, logo_statement_ProcedureDefinition8: set["statement_logo_Statement"] = None):
        self.name = name
        self.logo_statement_ProcedureDefinition = logo_statement_ProcedureDefinition if logo_statement_ProcedureDefinition is not None else set()
        self.logo_statement_ProcedureDefinition8 = logo_statement_ProcedureDefinition8 if logo_statement_ProcedureDefinition8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logo_statement_ProcedureDefinition(self):
        return self.__logo_statement_ProcedureDefinition

    @logo_statement_ProcedureDefinition.setter
    def logo_statement_ProcedureDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_statement_ProcedureDefinition__logo_statement_ProcedureDefinition", None)
        self.__logo_statement_ProcedureDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statement_logo_Parameter"):
                    opp_val = getattr(item, "statement_logo_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "statement_logo_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statement_logo_Parameter"):
                    opp_val = getattr(item, "statement_logo_Parameter", None)
                    
                    setattr(item, "statement_logo_Parameter", self)
                    

    @property
    def logo_statement_ProcedureDefinition8(self):
        return self.__logo_statement_ProcedureDefinition8

    @logo_statement_ProcedureDefinition8.setter
    def logo_statement_ProcedureDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_statement_ProcedureDefinition__logo_statement_ProcedureDefinition8", None)
        self.__logo_statement_ProcedureDefinition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statement_logo_Statement"):
                    opp_val = getattr(item, "statement_logo_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "statement_logo_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statement_logo_Statement"):
                    opp_val = getattr(item, "statement_logo_Statement", None)
                    
                    setattr(item, "statement_logo_Statement", self)
                    

class logo_statement_PenUp(Statement):

    pass
class logo_statement_PenDown(Statement):

    pass
class logo_Logo:

    pass
class logo_Symbol(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class logo_Parameter:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class logo_Expression(ABC):

    pass
class logo_Statement(ABC):

    pass