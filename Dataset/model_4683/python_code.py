from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryOperator(Enum):
    MINUS = "MINUS"
    BNOT = "BNOT"
    NOT = "NOT"
class BinaryOperator(Enum):
    IMPLY = "IMPLY"
    OR = "OR"
    AND = "AND"
    BOR = "BOR"
    BAND = "BAND"
    BXOR = "BXOR"
    EQ = "EQ"
    NEQ = "NEQ"
    LT = "LT"
    LEQ = "LEQ"
    GT = "GT"
    GEQ = "GEQ"
    SHL = "SHL"
    SHR = "SHR"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULT = "MULT"
    DIV = "DIV"
    MOD = "MOD"


############################################
# Definition of Classes
############################################

class BooleanLiteral:

    pass
class DVE_model_FalseLiteral(BooleanLiteral):

    pass
class DVE_model_TrueLiteral(BooleanLiteral):

    pass
class Literal:

    pass
class DVE_model_ArrayLiteral(Literal):

    pass
class DVE_model_NumberLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DVE_model_BooleanLiteral(Literal):

    pass
class Reference:

    pass
class DVE_model_StateReference(Reference):

    pass
class DVE_model_ProcessReference(Reference):

    pass
class DVE_model_ChannelReference(Reference):

    pass
class DVE_model_VariableReference(Reference):

    pass
class model_StateReference:

    pass
class model_PrefixedReference:

    pass
class DVE_model_ProcessStateReference(model_PrefixedReference, model_StateReference):

    pass
class model_VariableReference:

    pass
class DVE_model_ProcessVariableReference(model_VariableReference, model_PrefixedReference):

    pass
class ProcessReference:

    pass
class SystemType:

    pass
class DVE_model_Synchronous(SystemType):

    pass
class DVE_model_Asynchronous(SystemType):

    pass
class ChannelReference:

    pass
class StateReference:

    pass
class State:

    pass
class System:

    pass
class ChannelDeclaration:

    pass
class DVE_model_TypedChannelDeclaration(ChannelDeclaration):

    pass
class VariableDeclaration:

    pass
class DVE_model_ConstantDeclaration(VariableDeclaration):

    pass
class Assignment:

    pass
class Synchronization:

    pass
class DVE_model_InputSynchronization(Synchronization):

    pass
class DVE_model_OutputSynchronization(Synchronization):

    pass
class Transition:

    pass
class Process:

    pass
class CompositeDeclaration:

    pass
class DVE_model_Process(CompositeDeclaration):

    pass
class DVE_model_System(CompositeDeclaration):

    pass
class NamedDeclaration:

    pass
class DVE_model_ChannelDeclaration(NamedDeclaration):

    pass
class DVE_model_State(NamedDeclaration):

    pass
class DVE_model_CompositeDeclaration(NamedDeclaration):

    pass
class Declaration:

    pass
class DVE_model_Transition(Declaration):

    pass
class DVE_model_NamedDeclaration(Declaration):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Element:

    pass
class DVE_model_Synchronization(Element):

    pass
class DVE_model_Expression(Element):

    pass
class DVE_model_SystemType(Element):

    pass
class DVE_model_SystemProperties(Element):

    pass
class DVE_model_Assignment(Element):

    pass
class DVE_model_Declaration(Element):

    pass
class DVE_model_Element(ABC):

    pass
class DVE_model_VariableDeclaration(NamedDeclaration):

    pass
class Expression:

    pass
class DVE_model_PrefixedReference(Expression):

    pass
class DVE_model_Reference(Expression):

    def __init__(self, refName: str, Expression52: "DVE_model_Assignment", Expression54: "DVE_model_UnaryExpression", Expression44: "DVE_model_Synchronization", Expression69: "DVE_model_IndexedExpression", Expression: "DVE_model_ArrayType", Expression49: "DVE_model_Assignment", Expression10: "DVE_model_VariableDeclaration", Expression66: "DVE_model_IndexedExpression", Expression36: "DVE_model_Transition", Expression71: "DVE_model_ArrayLiteral", Expression56: "DVE_model_BinaryExpression", Expression15: "DVE_model_TypedChannelDeclaration"):
        self.refName = refName
        
    @property
    def refName(self) -> str:
        return self.__refName

    @refName.setter
    def refName(self, refName: str):
        self.__refName = refName

class DVE_model_Literal(Expression):

    pass
class DVE_model_IndexedExpression(Expression):

    pass
class DVE_model_BinaryExpression(Expression):

    def __init__(self, operator: str, DVE_model_BinaryExpression: set["Expression"] = None, Expression52: "DVE_model_Assignment", Expression54: "DVE_model_UnaryExpression", Expression44: "DVE_model_Synchronization", Expression69: "DVE_model_IndexedExpression", Expression: "DVE_model_ArrayType", Expression49: "DVE_model_Assignment", Expression10: "DVE_model_VariableDeclaration", Expression66: "DVE_model_IndexedExpression", Expression36: "DVE_model_Transition", Expression71: "DVE_model_ArrayLiteral", Expression56: "DVE_model_BinaryExpression", Expression15: "DVE_model_TypedChannelDeclaration"):
        self.operator = operator
        self.DVE_model_BinaryExpression = DVE_model_BinaryExpression if DVE_model_BinaryExpression is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DVE_model_BinaryExpression(self):
        return self.__DVE_model_BinaryExpression

    @DVE_model_BinaryExpression.setter
    def DVE_model_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DVE_model_BinaryExpression__DVE_model_BinaryExpression", None)
        self.__DVE_model_BinaryExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression56"):
                    opp_val = getattr(item, "Expression56", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression56"):
                    opp_val = getattr(item, "Expression56", None)
                    
                    setattr(item, "Expression56", self)
                    

class DVE_model_UnaryExpression(Expression):

    def __init__(self, operator: str, DVE_model_UnaryExpression: "Expression" = None, Expression52: "DVE_model_Assignment", Expression54: "DVE_model_UnaryExpression", Expression44: "DVE_model_Synchronization", Expression69: "DVE_model_IndexedExpression", Expression: "DVE_model_ArrayType", Expression49: "DVE_model_Assignment", Expression10: "DVE_model_VariableDeclaration", Expression66: "DVE_model_IndexedExpression", Expression36: "DVE_model_Transition", Expression71: "DVE_model_ArrayLiteral", Expression56: "DVE_model_BinaryExpression", Expression15: "DVE_model_TypedChannelDeclaration"):
        self.operator = operator
        self.DVE_model_UnaryExpression = DVE_model_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DVE_model_UnaryExpression(self):
        return self.__DVE_model_UnaryExpression

    @DVE_model_UnaryExpression.setter
    def DVE_model_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DVE_model_UnaryExpression__DVE_model_UnaryExpression", None)
        self.__DVE_model_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression54"):
                opp_val = getattr(old_value, "Expression54", None)
                if opp_val == self:
                    setattr(old_value, "Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression54"):
                opp_val = getattr(value, "Expression54", None)
                setattr(value, "Expression54", self)

class Type:

    pass
class DVE_model_ByteType(Type):

    pass
class DVE_model_ArrayType(Type):

    pass
class DVE_model_IntegerType(Type):

    pass
class DVE_model_Type(Element):

    pass
class SystemProperties:

    pass