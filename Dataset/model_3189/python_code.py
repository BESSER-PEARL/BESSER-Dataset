from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataVariablePrefix(Enum):
    CONST = "CONST"
    META = "META"
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    IMPLY = "IMPLY"
class Quantifier(Enum):
    EXISTENTIAL = "EXISTENTIAL"
    UNIVERSAL = "UNIVERSAL"
class MinMaxOperator(Enum):
    MIN = "MIN"
    MAX = "MAX"
class AssignmentOperator(Enum):
    EQUAL = "EQUAL"
    PLUS_EQUAL = "PLUS_EQUAL"
    MINUS_EQUAL = "MINUS_EQUAL"
    TIMES_EQUAL = "TIMES_EQUAL"
    DIVIDE_EQUAL = "DIVIDE_EQUAL"
    MODULO_EQUAL = "MODULO_EQUAL"
    BIT_AND_EQUAL = "BIT_AND_EQUAL"
    BIT_OR_EQUAL = "BIT_OR_EQUAL"
    BIT_LEFT_EQUAL = "BIT_LEFT_EQUAL"
    BIT_RIGHT_EQUAL = "BIT_RIGHT_EQUAL"
    BIT_XOR_EQUAL = "BIT_XOR_EQUAL"
class BuiltInType(Enum):
    INT = "INT"
    CLOCK = "CLOCK"
    CHAN = "CHAN"
    BOOL = "BOOL"
    VOID = "VOID"
class BitShiftOperator(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class LocationKind(Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"
    COMMITED = "COMMITED"
class SynchronizationKind(Enum):
    RECEIVE = "RECEIVE"
    SEND = "SEND"
class BitwiseOperator(Enum):
    AND = "AND"
    XOR = "XOR"
    OR = "OR"
class CompareOperator(Enum):
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    UNEQUAL = "UNEQUAL"
class CallType(Enum):
    CALL_BY_VALUE = "CALL_BY_VALUE"
    CALL_BY_REFERENCE = "CALL_BY_REFERENCE"
class IncrementDecrementOperator(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class ArithmeticOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLICATE = "MULTIPLICATE"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"


############################################
# Definition of Classes
############################################

class uppaal_visuals_Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class uppaal_visuals_LinearElement(ABC):

    pass
class Point:

    pass
class uppaal_visuals_PlanarElement(ABC):

    pass
class uppaal_visuals_ColoredElement(ABC):

    def __init__(self, colorCode: str):
        self.colorCode = colorCode
        
        pass
    @property
    def colorCode(self):
        return self.__colorCode

    @colorCode.setter
    def colorCode(self, colorCode: str):
        self.__colorCode = colorCode


class IncrementDecrementExpression:

    pass
class uppaal_expressions_PostIncrementDecrementExpression(IncrementDecrementExpression):

    pass
class uppaal_expressions_PreIncrementDecrementExpression(IncrementDecrementExpression):

    pass
class expressions_Expression:

    pass
class Function:

    pass
class BinaryExpression:

    pass
class uppaal_expressions_LogicalExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_ArithmeticExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_BitShiftExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_BitwiseExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_MinMaxExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_CompareExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_AssignmentExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class uppaal_expressions_Expression(ABC):

    pass
class statements_Statement:

    pass
class uppaal_templates_Synchronization:

    def __init__(self, kind: str, uppaal_templates_Synchronization: "IdentifierExpression" = None):
        self.kind = kind
        self.uppaal_templates_Synchronization = uppaal_templates_Synchronization
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def uppaal_templates_Synchronization(self):
        return self.__uppaal_templates_Synchronization

    @uppaal_templates_Synchronization.setter
    def uppaal_templates_Synchronization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Synchronization__uppaal_templates_Synchronization", None)
        self.__uppaal_templates_Synchronization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifierExpression88"):
                opp_val = getattr(old_value, "IdentifierExpression88", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierExpression88"):
                opp_val = getattr(value, "IdentifierExpression88", None)
                setattr(value, "IdentifierExpression88", self)

class Statement:

    pass
class uppaal_statements_DoWhileLoop(Statement):

    pass
class uppaal_statements_EmptyStatement(Statement):

    pass
class uppaal_statements_ReturnStatement(Statement):

    pass
class uppaal_statements_IfStatement(Statement):

    pass
class uppaal_statements_ForLoop(Statement):

    pass
class uppaal_statements_ExpressionStatement(Statement):

    pass
class uppaal_statements_WhileLoop(Statement):

    pass
class uppaal_statements_Block(Statement):

    pass
class uppaal_statements_Statement(ABC):

    pass
class visuals_LinearElement:

    pass
class Selection:

    pass
class Synchronization:

    pass
class Location:

    pass
class LocalDeclarations:

    pass
class visuals_ColoredElement:

    pass
class visuals_PlanarElement:

    pass
class system_TemplateDeclaration:

    pass
class Edge:

    pass
class RedefinedTemplate:

    pass
class IdentifierExpression:

    pass
class PriorityItem:

    pass
class uppaal_global_DefaultItem(PriorityItem):

    pass
class uppaal_global_ChannelItem(PriorityItem):

    pass
class uppaal_global_PriorityItem(ABC):

    pass
class global_PriorityItem:

    pass
class uppaal_global_ChannelPriorityGroup:

    pass
class uppaal_system_ProgressMeasure:

    pass
class AbstractTemplate:

    pass
class uppaal_templates_RedefinedTemplate(AbstractTemplate):

    pass
class uppaal_templates_Template(AbstractTemplate):

    pass
class uppaal_system_InstantiationList:

    pass
class system_InstantiationList:

    pass
class uppaal_system_System:

    pass
class uppaal_declarations_Initializer(ABC):

    pass
class Variable:

    pass
class uppaal_declarations_Parameter(Variable):

    def __init__(self, callType: str):
        self.callType = callType
        
        pass
    @property
    def callType(self):
        return self.__callType

    @callType.setter
    def callType(self, callType: str):
        self.__callType = callType


class TypedElement:

    pass
class uppaal_declarations_TypedElementContainer(ABC):

    pass
class global_ChannelPriorityGroup:

    pass
class Initializer:

    pass
class uppaal_declarations_ArrayInitializer(Initializer):

    pass
class uppaal_declarations_ExpressionInitializer(Initializer):

    pass
class declarations_TypedElementContainer:

    pass
class uppaal_statements_Iteration(declarations_TypedElementContainer, statements_Statement):

    pass
class uppaal_expressions_QuantificationExpression(expressions_Expression, declarations_TypedElementContainer):

    def __init__(self, quantifier: str, uppaal_expressions_QuantificationExpression: "Expression" = None):
        self.quantifier = quantifier
        self.uppaal_expressions_QuantificationExpression = uppaal_expressions_QuantificationExpression
        
        pass
    @property
    def quantifier(self):
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier


    @property
    def uppaal_expressions_QuantificationExpression(self):
        return self.__uppaal_expressions_QuantificationExpression

    @uppaal_expressions_QuantificationExpression.setter
    def uppaal_expressions_QuantificationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_expressions_QuantificationExpression__uppaal_expressions_QuantificationExpression", None)
        self.__uppaal_expressions_QuantificationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression161"):
                opp_val = getattr(old_value, "Expression161", None)
                if opp_val == self:
                    setattr(old_value, "Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression161"):
                opp_val = getattr(value, "Expression161", None)
                setattr(value, "Expression161", self)

class declarations_Declaration:

    pass
class uppaal_declarations_TypedDeclaration(declarations_Declaration, declarations_TypedElementContainer):

    pass
class DeclaredType:

    pass
class uppaal_declarations_Declaration(ABC):

    pass
class system_ProgressMeasure:

    pass
class system_System:

    pass
class global_ChannelPriorityDeclaration:

    pass
class ParameterContainer:

    pass
class Block:

    pass
class core_TypedElement:

    pass
class uppaal_types_IntegerBounds:

    pass
class IntegerBounds:

    pass
class TypedDeclaration:

    pass
class TypeExpression:

    pass
class uppaal_types_RangeTypeSpecification(TypeExpression):

    pass
class uppaal_types_StructTypeSpecification(TypeExpression):

    pass
class uppaal_types_ScalarTypeSpecification(TypeExpression):

    pass
class Declarations:

    pass
class uppaal_declarations_SystemDeclarations(Declarations):

    pass
class uppaal_declarations_LocalDeclarations(Declarations):

    pass
class uppaal_declarations_GlobalDeclarations(Declarations):

    pass
class Declaration:

    pass
class uppaal_declarations_TypeDeclaration(Declaration):

    pass
class uppaal_global_ChannelPriorityDeclaration(Declaration):

    pass
class uppaal_system_TemplateDeclaration(Declaration):

    pass
class uppaal_declarations_Declarations(ABC):

    pass
class PredefinedType:

    pass
class uppaal_types_Library:

    pass
class NamedElement:

    pass
class uppaal_templates_AbstractTemplate(NamedElement):

    pass
class uppaal_types_Type(NamedElement):

    def __init__(self, baseType: str, NamedElement: "uppaal_expressions_IdentifierExpression" = None):
        self.baseType = baseType
        
        pass
    @property
    def baseType(self):
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType


class Expression:

    pass
class uppaal_expressions_ConditionExpression(Expression):

    pass
class uppaal_expressions_BinaryExpression(Expression):

    pass
class uppaal_expressions_PlusExpression(Expression):

    pass
class uppaal_expressions_FunctionCallExpression(Expression):

    pass
class uppaal_expressions_IdentifierExpression(Expression):

    pass
class uppaal_expressions_NegationExpression(Expression):

    pass
class uppaal_types_TypeExpression(Expression):

    pass
class uppaal_expressions_ChannelPrefixExpression(Expression):

    def __init__(self, urgent: bool, broadcast: bool, uppaal_expressions_ChannelPrefixExpression: "Type" = None, Expression133: "uppaal_expressions_MinusExpression" = None, Expression138: "uppaal_expressions_BinaryExpression" = None, Expression36: "uppaal_declarations_TypedElementContainer" = None, Expression32: "uppaal_declarations_Variable" = None, Expression153: "uppaal_expressions_ConditionExpression" = None, Expression18: "uppaal_types_IntegerBounds" = None, Expression115: "uppaal_statements_DoWhileLoop" = None, Expression11: "uppaal_types_ScalarTypeSpecification" = None, Expression161: "uppaal_expressions_QuantificationExpression" = None, Expression51: "uppaal_system_ProgressMeasure" = None, Expression97: "uppaal_statements_ForLoop" = None, Expression163: "uppaal_expressions_IncrementDecrementExpression" = None, Expression144: "uppaal_expressions_ScopedIdentifierExpression" = None, Expression100: "uppaal_statements_ForLoop" = None, Expression159: "uppaal_expressions_ConditionExpression" = None, Expression9: "uppaal_types_DeclaredType" = None, Expression142: "uppaal_expressions_IdentifierExpression" = None, Expression79: "uppaal_templates_Edge" = None, Expression117: "uppaal_statements_IfStatement" = None, Expression: "uppaal_core_TypedElement" = None, Expression125: "uppaal_statements_ReturnStatement" = None, Expression15: "uppaal_types_IntegerBounds" = None, Expression127: "uppaal_statements_ExpressionStatement" = None, Expression47: "uppaal_system_TemplateDeclaration" = None, Expression39: "uppaal_declarations_ExpressionInitializer" = None, Expression135: "uppaal_expressions_BinaryExpression" = None, Expression107: "uppaal_statements_WhileLoop" = None, Expression82: "uppaal_templates_Edge" = None, Expression30: "uppaal_declarations_TypeDeclaration" = None, Expression129: "uppaal_expressions_NegationExpression" = None, Expression131: "uppaal_expressions_PlusExpression" = None, Expression166: "uppaal_expressions_DataPrefixExpression" = None, Expression94: "uppaal_statements_ForLoop" = None, Expression67: "uppaal_templates_Location" = None, Expression151: "uppaal_expressions_FunctionCallExpression" = None, Expression156: "uppaal_expressions_ConditionExpression" = None):
        self.urgent = urgent
        self.broadcast = broadcast
        self.uppaal_expressions_ChannelPrefixExpression = uppaal_expressions_ChannelPrefixExpression
        
        pass
    @property
    def broadcast(self):
        return self.__broadcast

    @broadcast.setter
    def broadcast(self, broadcast: bool):
        self.__broadcast = broadcast


    @property
    def urgent(self):
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent


    @property
    def uppaal_expressions_ChannelPrefixExpression(self):
        return self.__uppaal_expressions_ChannelPrefixExpression

    @uppaal_expressions_ChannelPrefixExpression.setter
    def uppaal_expressions_ChannelPrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_expressions_ChannelPrefixExpression__uppaal_expressions_ChannelPrefixExpression", None)
        self.__uppaal_expressions_ChannelPrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

class uppaal_expressions_DataPrefixExpression(Expression):

    def __init__(self, prefix: str, uppaal_expressions_DataPrefixExpression: "Expression" = None, Expression133: "uppaal_expressions_MinusExpression" = None, Expression138: "uppaal_expressions_BinaryExpression" = None, Expression36: "uppaal_declarations_TypedElementContainer" = None, Expression32: "uppaal_declarations_Variable" = None, Expression153: "uppaal_expressions_ConditionExpression" = None, Expression18: "uppaal_types_IntegerBounds" = None, Expression115: "uppaal_statements_DoWhileLoop" = None, Expression11: "uppaal_types_ScalarTypeSpecification" = None, Expression161: "uppaal_expressions_QuantificationExpression" = None, Expression51: "uppaal_system_ProgressMeasure" = None, Expression97: "uppaal_statements_ForLoop" = None, Expression163: "uppaal_expressions_IncrementDecrementExpression" = None, Expression144: "uppaal_expressions_ScopedIdentifierExpression" = None, Expression100: "uppaal_statements_ForLoop" = None, Expression159: "uppaal_expressions_ConditionExpression" = None, Expression9: "uppaal_types_DeclaredType" = None, Expression142: "uppaal_expressions_IdentifierExpression" = None, Expression79: "uppaal_templates_Edge" = None, Expression117: "uppaal_statements_IfStatement" = None, Expression: "uppaal_core_TypedElement" = None, Expression125: "uppaal_statements_ReturnStatement" = None, Expression15: "uppaal_types_IntegerBounds" = None, Expression127: "uppaal_statements_ExpressionStatement" = None, Expression47: "uppaal_system_TemplateDeclaration" = None, Expression39: "uppaal_declarations_ExpressionInitializer" = None, Expression135: "uppaal_expressions_BinaryExpression" = None, Expression107: "uppaal_statements_WhileLoop" = None, Expression82: "uppaal_templates_Edge" = None, Expression30: "uppaal_declarations_TypeDeclaration" = None, Expression129: "uppaal_expressions_NegationExpression" = None, Expression131: "uppaal_expressions_PlusExpression" = None, Expression166: "uppaal_expressions_DataPrefixExpression" = None, Expression94: "uppaal_statements_ForLoop" = None, Expression67: "uppaal_templates_Location" = None, Expression151: "uppaal_expressions_FunctionCallExpression" = None, Expression156: "uppaal_expressions_ConditionExpression" = None):
        self.prefix = prefix
        self.uppaal_expressions_DataPrefixExpression = uppaal_expressions_DataPrefixExpression
        
        pass
    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def uppaal_expressions_DataPrefixExpression(self):
        return self.__uppaal_expressions_DataPrefixExpression

    @uppaal_expressions_DataPrefixExpression.setter
    def uppaal_expressions_DataPrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_expressions_DataPrefixExpression__uppaal_expressions_DataPrefixExpression", None)
        self.__uppaal_expressions_DataPrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression166"):
                opp_val = getattr(old_value, "Expression166", None)
                if opp_val == self:
                    setattr(old_value, "Expression166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression166"):
                opp_val = getattr(value, "Expression166", None)
                setattr(value, "Expression166", self)

class uppaal_expressions_MinusExpression(Expression):

    pass
class uppaal_expressions_ScopedIdentifierExpression(Expression):

    pass
class uppaal_expressions_IncrementDecrementExpression(Expression):

    def __init__(self, operator: str, uppaal_expressions_IncrementDecrementExpression: "Expression" = None, Expression133: "uppaal_expressions_MinusExpression" = None, Expression138: "uppaal_expressions_BinaryExpression" = None, Expression36: "uppaal_declarations_TypedElementContainer" = None, Expression32: "uppaal_declarations_Variable" = None, Expression153: "uppaal_expressions_ConditionExpression" = None, Expression18: "uppaal_types_IntegerBounds" = None, Expression115: "uppaal_statements_DoWhileLoop" = None, Expression11: "uppaal_types_ScalarTypeSpecification" = None, Expression161: "uppaal_expressions_QuantificationExpression" = None, Expression51: "uppaal_system_ProgressMeasure" = None, Expression97: "uppaal_statements_ForLoop" = None, Expression163: "uppaal_expressions_IncrementDecrementExpression" = None, Expression144: "uppaal_expressions_ScopedIdentifierExpression" = None, Expression100: "uppaal_statements_ForLoop" = None, Expression159: "uppaal_expressions_ConditionExpression" = None, Expression9: "uppaal_types_DeclaredType" = None, Expression142: "uppaal_expressions_IdentifierExpression" = None, Expression79: "uppaal_templates_Edge" = None, Expression117: "uppaal_statements_IfStatement" = None, Expression: "uppaal_core_TypedElement" = None, Expression125: "uppaal_statements_ReturnStatement" = None, Expression15: "uppaal_types_IntegerBounds" = None, Expression127: "uppaal_statements_ExpressionStatement" = None, Expression47: "uppaal_system_TemplateDeclaration" = None, Expression39: "uppaal_declarations_ExpressionInitializer" = None, Expression135: "uppaal_expressions_BinaryExpression" = None, Expression107: "uppaal_statements_WhileLoop" = None, Expression82: "uppaal_templates_Edge" = None, Expression30: "uppaal_declarations_TypeDeclaration" = None, Expression129: "uppaal_expressions_NegationExpression" = None, Expression131: "uppaal_expressions_PlusExpression" = None, Expression166: "uppaal_expressions_DataPrefixExpression" = None, Expression94: "uppaal_statements_ForLoop" = None, Expression67: "uppaal_templates_Location" = None, Expression151: "uppaal_expressions_FunctionCallExpression" = None, Expression156: "uppaal_expressions_ConditionExpression" = None):
        self.operator = operator
        self.uppaal_expressions_IncrementDecrementExpression = uppaal_expressions_IncrementDecrementExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def uppaal_expressions_IncrementDecrementExpression(self):
        return self.__uppaal_expressions_IncrementDecrementExpression

    @uppaal_expressions_IncrementDecrementExpression.setter
    def uppaal_expressions_IncrementDecrementExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_expressions_IncrementDecrementExpression__uppaal_expressions_IncrementDecrementExpression", None)
        self.__uppaal_expressions_IncrementDecrementExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression163"):
                opp_val = getattr(old_value, "Expression163", None)
                if opp_val == self:
                    setattr(old_value, "Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression163"):
                opp_val = getattr(value, "Expression163", None)
                setattr(value, "Expression163", self)

class uppaal_expressions_LiteralExpression(Expression):

    def __init__(self, text: str, Expression133: "uppaal_expressions_MinusExpression" = None, Expression138: "uppaal_expressions_BinaryExpression" = None, Expression36: "uppaal_declarations_TypedElementContainer" = None, Expression32: "uppaal_declarations_Variable" = None, Expression153: "uppaal_expressions_ConditionExpression" = None, Expression18: "uppaal_types_IntegerBounds" = None, Expression115: "uppaal_statements_DoWhileLoop" = None, Expression11: "uppaal_types_ScalarTypeSpecification" = None, Expression161: "uppaal_expressions_QuantificationExpression" = None, Expression51: "uppaal_system_ProgressMeasure" = None, Expression97: "uppaal_statements_ForLoop" = None, Expression163: "uppaal_expressions_IncrementDecrementExpression" = None, Expression144: "uppaal_expressions_ScopedIdentifierExpression" = None, Expression100: "uppaal_statements_ForLoop" = None, Expression159: "uppaal_expressions_ConditionExpression" = None, Expression9: "uppaal_types_DeclaredType" = None, Expression142: "uppaal_expressions_IdentifierExpression" = None, Expression79: "uppaal_templates_Edge" = None, Expression117: "uppaal_statements_IfStatement" = None, Expression: "uppaal_core_TypedElement" = None, Expression125: "uppaal_statements_ReturnStatement" = None, Expression15: "uppaal_types_IntegerBounds" = None, Expression127: "uppaal_statements_ExpressionStatement" = None, Expression47: "uppaal_system_TemplateDeclaration" = None, Expression39: "uppaal_declarations_ExpressionInitializer" = None, Expression135: "uppaal_expressions_BinaryExpression" = None, Expression107: "uppaal_statements_WhileLoop" = None, Expression82: "uppaal_templates_Edge" = None, Expression30: "uppaal_declarations_TypeDeclaration" = None, Expression129: "uppaal_expressions_NegationExpression" = None, Expression131: "uppaal_expressions_PlusExpression" = None, Expression166: "uppaal_expressions_DataPrefixExpression" = None, Expression94: "uppaal_statements_ForLoop" = None, Expression67: "uppaal_templates_Location" = None, Expression151: "uppaal_expressions_FunctionCallExpression" = None, Expression156: "uppaal_expressions_ConditionExpression" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class TypedElementContainer:

    pass
class uppaal_templates_Selection(TypedElementContainer):

    pass
class uppaal_declarations_ParameterContainer(TypedElementContainer):

    pass
class uppaal_core_TypedElement(ABC):

    pass
class uppaal_core_CommentableElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


class uppaal_core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class TypeDeclaration:

    pass
class Type:

    pass
class uppaal_types_DeclaredType(Type):

    pass
class uppaal_types_PredefinedType(Type):

    def __init__(self, type: str, Type: "uppaal_expressions_ChannelPrefixExpression" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class core_CommentableElement:

    pass
class uppaal_templates_Edge(visuals_LinearElement, core_CommentableElement, visuals_ColoredElement):

    pass
class core_NamedElement:

    pass
class uppaal_templates_Location(visuals_PlanarElement, core_NamedElement, core_CommentableElement, visuals_ColoredElement):

    def __init__(self, locationTimeKind: str, location: "Template" = None, uppaal_templates_Location: "Expression" = None, target: set["Edge"] = None, source: set["Edge"] = None):
        self.locationTimeKind = locationTimeKind
        self.location = location
        self.uppaal_templates_Location = uppaal_templates_Location
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
        pass
    @property
    def locationTimeKind(self):
        return self.__locationTimeKind

    @locationTimeKind.setter
    def locationTimeKind(self, locationTimeKind: str):
        self.__locationTimeKind = locationTimeKind


    @property
    def uppaal_templates_Location(self):
        return self.__uppaal_templates_Location

    @uppaal_templates_Location.setter
    def uppaal_templates_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__uppaal_templates_Location", None)
        self.__uppaal_templates_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression67"):
                opp_val = getattr(old_value, "Expression67", None)
                if opp_val == self:
                    setattr(old_value, "Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression67"):
                opp_val = getattr(value, "Expression67", None)
                setattr(value, "Expression67", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge71"):
                    opp_val = getattr(item, "Edge71", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge71"):
                    opp_val = getattr(item, "Edge71", None)
                    
                    setattr(item, "Edge71", self)
                    

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__location", None)
        self.__location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Template65"):
                opp_val = getattr(old_value, "Template65", None)
                if opp_val == self:
                    setattr(old_value, "Template65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Template65"):
                opp_val = getattr(value, "Template65", None)
                setattr(value, "Template65", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge69"):
                    opp_val = getattr(item, "Edge69", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge69"):
                    opp_val = getattr(item, "Edge69", None)
                    
                    setattr(item, "Edge69", self)
                    

class uppaal_declarations_Function(core_NamedElement, core_TypedElement):

    pass
class uppaal_declarations_Variable(core_NamedElement, core_TypedElement):

    pass
class uppaal_NTA(core_NamedElement, core_CommentableElement):

    pass
class SystemDeclarations:

    pass
class Template:

    pass
class GlobalDeclarations:

    pass