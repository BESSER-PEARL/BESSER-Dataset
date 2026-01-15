from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataVariablePrefix(Enum):
    CONST = "CONST"
    META = "META"
class CallType(Enum):
    CALL_BY_VALUE = "CALL_BY_VALUE"
    CALL_BY_REFERENCE = "CALL_BY_REFERENCE"
class BitwiseOperator(Enum):
    OR = "OR"
    AND = "AND"
    XOR = "XOR"
class MinMaxOperator(Enum):
    MIN = "MIN"
    MAX = "MAX"
class BitShiftOperator(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class ArithmeticOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLICATE = "MULTIPLICATE"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
class IncrementDecrementOperator(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class SynchronizationKind(Enum):
    RECEIVE = "RECEIVE"
    SEND = "SEND"
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
class Quantifier(Enum):
    EXISTENTIAL = "EXISTENTIAL"
    UNIVERSAL = "UNIVERSAL"
class CompareOperator(Enum):
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    UNEQUAL = "UNEQUAL"
class LocationKind(Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"
    COMMITED = "COMMITED"
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    IMPLY = "IMPLY"
class BuiltInType(Enum):
    INT = "INT"
    CLOCK = "CLOCK"
    CHAN = "CHAN"
    BOOL = "BOOL"
    VOID = "VOID"


############################################
# Definition of Classes
############################################

class Point:

    pass
class uppaal_visuals_PlanarElement(ABC):

    pass
class uppaal_visuals_ColoredElement(ABC):

    def __init__(self, colorCode: str):
        self.colorCode = colorCode
        
    @property
    def colorCode(self) -> str:
        return self.__colorCode

    @colorCode.setter
    def colorCode(self, colorCode: str):
        self.__colorCode = colorCode

class uppaal_visuals_Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

class uppaal_visuals_LinearElement(ABC):

    pass
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
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_CompareExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_BitwiseExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_ArithmeticExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_MinMaxExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_BitShiftExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_AssignmentExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class uppaal_expressions_Expression(ABC):

    pass
class statements_Statement:

    pass
class uppaal_statements_Statement(ABC):

    pass
class Statement:

    pass
class uppaal_statements_EmptyStatement(Statement):

    pass
class uppaal_statements_DoWhileLoop(Statement):

    pass
class uppaal_statements_ExpressionStatement(Statement):

    pass
class uppaal_statements_ReturnStatement(Statement):

    pass
class uppaal_statements_WhileLoop(Statement):

    pass
class uppaal_statements_IfStatement(Statement):

    pass
class uppaal_statements_ForLoop(Statement):

    pass
class uppaal_statements_Block(Statement):

    pass
class Selection:

    pass
class Synchronization:

    pass
class uppaal_templates_Synchronization:

    def __init__(self, kind: str, uppaal_templates_Synchronization: "IdentifierExpression" = None):
        self.kind = kind
        self.uppaal_templates_Synchronization = uppaal_templates_Synchronization
        
    @property
    def kind(self) -> str:
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
            if hasattr(old_value, "IdentifierExpression97"):
                opp_val = getattr(old_value, "IdentifierExpression97", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierExpression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierExpression97"):
                opp_val = getattr(value, "IdentifierExpression97", None)
                setattr(value, "IdentifierExpression97", self)

class visuals_LinearElement:

    pass
class visuals_ColoredElement:

    pass
class visuals_PlanarElement:

    pass
class Edge:

    pass
class Location:

    pass
class system_TemplateDeclaration:

    pass
class LocalDeclarations:

    pass
class uppaal_system_System:

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
class PriorityItem:

    pass
class uppaal_global_ChannelItem(PriorityItem):

    pass
class uppaal_global_PriorityItem(ABC):

    pass
class RedefinedTemplate:

    pass
class uppaal_global_DefaultItem(PriorityItem):

    pass
class IdentifierExpression:

    pass
class global_PriorityItem:

    pass
class uppaal_global_ChannelPriorityGroup:

    pass
class global_ChannelPriorityGroup:

    pass
class declarations_TypedElementContainer:

    pass
class uppaal_expressions_QuantificationExpression(declarations_TypedElementContainer, expressions_Expression):

    def __init__(self, quantifier: str, uppaal_expressions_QuantificationExpression: "Expression" = None):
        self.quantifier = quantifier
        self.uppaal_expressions_QuantificationExpression = uppaal_expressions_QuantificationExpression
        
    @property
    def quantifier(self) -> str:
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
            if hasattr(old_value, "Expression170"):
                opp_val = getattr(old_value, "Expression170", None)
                if opp_val == self:
                    setattr(old_value, "Expression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression170"):
                opp_val = getattr(value, "Expression170", None)
                setattr(value, "Expression170", self)

class uppaal_statements_Iteration(declarations_TypedElementContainer, statements_Statement):

    pass
class declarations_Declaration:

    pass
class uppaal_declarations_TypedDeclaration(declarations_TypedElementContainer, declarations_Declaration):

    pass
class uppaal_declarations_Initializer(ABC):

    pass
class Variable:

    pass
class uppaal_declarations_Parameter(Variable):

    def __init__(self, callType: str):
        self.callType = callType
        
    @property
    def callType(self) -> str:
        return self.__callType

    @callType.setter
    def callType(self, callType: str):
        self.__callType = callType

class TypedElement:

    pass
class uppaal_declarations_TypedElementContainer(ABC):

    pass
class Initializer:

    pass
class uppaal_declarations_ExpressionInitializer(Initializer):

    pass
class uppaal_declarations_ArrayInitializer(Initializer):

    pass
class DeclaredType:

    pass
class ParameterContainer:

    pass
class Block:

    pass
class core_TypedElement:

    pass
class uppaal_declarations_Declaration(ABC):

    pass
class system_ProgressMeasure:

    pass
class system_System:

    pass
class global_ChannelPriorityDeclaration:

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
class uppaal_system_TemplateDeclaration(Declaration):

    pass
class uppaal_global_ChannelPriorityDeclaration(Declaration):

    pass
class uppaal_declarations_TypeDeclaration(Declaration):

    pass
class uppaal_declarations_Declarations(ABC):

    pass
class PredefinedType:

    pass
class uppaal_types_Library:

    pass
class uppaal_types_IntegerBounds:

    pass
class IntegerBounds:

    pass
class TypedDeclaration:

    pass
class TypeExpression:

    pass
class uppaal_types_StructTypeSpecification(TypeExpression):

    pass
class uppaal_types_RangeTypeSpecification(TypeExpression):

    pass
class uppaal_types_ScalarTypeSpecification(TypeExpression):

    pass
class TypeDeclaration:

    pass
class Type:

    pass
class uppaal_types_DeclaredType(Type):

    pass
class uppaal_types_PredefinedType(Type):

    def __init__(self, type: str, Type: "uppaal_expressions_ChannelPrefixExpression"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class NamedElement:

    pass
class uppaal_templates_AbstractTemplate(NamedElement):

    pass
class uppaal_types_Type(NamedElement):

    def __init__(self, baseType: str, NamedElement: "uppaal_expressions_IdentifierExpression"):
        self.baseType = baseType
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

class Expression:

    pass
class uppaal_expressions_IdentifierExpression(Expression):

    pass
class uppaal_expressions_ChannelPrefixExpression(Expression):

    def __init__(self, urgent: bool, broadcast: bool, uppaal_expressions_ChannelPrefixExpression: "Type" = None, Expression147: "uppaal_expressions_BinaryExpression", Expression71: "uppaal_templates_Location", Expression103: "uppaal_statements_ForLoop", Expression168: "uppaal_expressions_ConditionExpression", Expression153: "uppaal_expressions_ScopedIdentifierExpression", Expression165: "uppaal_expressions_ConditionExpression", Expression138: "uppaal_expressions_NegationExpression", Expression106: "uppaal_statements_ForLoop", Expression37: "uppaal_declarations_TypedElementContainer", Expression175: "uppaal_expressions_DataPrefixExpression", Expression19: "uppaal_types_IntegerBounds", Expression142: "uppaal_expressions_MinusExpression", Expression: "uppaal_core_TypedElement", Expression12: "uppaal_types_ScalarTypeSpecification", Expression160: "uppaal_expressions_FunctionCallExpression", Expression91: "uppaal_templates_Edge", Expression136: "uppaal_statements_ExpressionStatement", Expression40: "uppaal_declarations_ExpressionInitializer", Expression88: "uppaal_templates_Edge", Expression31: "uppaal_declarations_TypeDeclaration", Expression162: "uppaal_expressions_ConditionExpression", Expression16: "uppaal_types_IntegerBounds", Expression124: "uppaal_statements_DoWhileLoop", Expression116: "uppaal_statements_WhileLoop", Expression172: "uppaal_expressions_IncrementDecrementExpression", Expression109: "uppaal_statements_ForLoop", Expression151: "uppaal_expressions_IdentifierExpression", Expression126: "uppaal_statements_IfStatement", Expression48: "uppaal_system_TemplateDeclaration", Expression52: "uppaal_system_ProgressMeasure", Expression10: "uppaal_types_DeclaredType", Expression170: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_expressions_PlusExpression", Expression134: "uppaal_statements_ReturnStatement", Expression33: "uppaal_declarations_Variable", Expression144: "uppaal_expressions_BinaryExpression"):
        self.urgent = urgent
        self.broadcast = broadcast
        self.uppaal_expressions_ChannelPrefixExpression = uppaal_expressions_ChannelPrefixExpression
        
    @property
    def urgent(self) -> bool:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent

    @property
    def broadcast(self) -> bool:
        return self.__broadcast

    @broadcast.setter
    def broadcast(self, broadcast: bool):
        self.__broadcast = broadcast

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

class uppaal_expressions_MinusExpression(Expression):

    pass
class uppaal_expressions_BinaryExpression(Expression):

    pass
class uppaal_expressions_NegationExpression(Expression):

    pass
class uppaal_expressions_ScopedIdentifierExpression(Expression):

    pass
class uppaal_expressions_ConditionExpression(Expression):

    pass
class uppaal_expressions_DataPrefixExpression(Expression):

    def __init__(self, prefix: str, uppaal_expressions_DataPrefixExpression: "Expression" = None, Expression147: "uppaal_expressions_BinaryExpression", Expression71: "uppaal_templates_Location", Expression103: "uppaal_statements_ForLoop", Expression168: "uppaal_expressions_ConditionExpression", Expression153: "uppaal_expressions_ScopedIdentifierExpression", Expression165: "uppaal_expressions_ConditionExpression", Expression138: "uppaal_expressions_NegationExpression", Expression106: "uppaal_statements_ForLoop", Expression37: "uppaal_declarations_TypedElementContainer", Expression175: "uppaal_expressions_DataPrefixExpression", Expression19: "uppaal_types_IntegerBounds", Expression142: "uppaal_expressions_MinusExpression", Expression: "uppaal_core_TypedElement", Expression12: "uppaal_types_ScalarTypeSpecification", Expression160: "uppaal_expressions_FunctionCallExpression", Expression91: "uppaal_templates_Edge", Expression136: "uppaal_statements_ExpressionStatement", Expression40: "uppaal_declarations_ExpressionInitializer", Expression88: "uppaal_templates_Edge", Expression31: "uppaal_declarations_TypeDeclaration", Expression162: "uppaal_expressions_ConditionExpression", Expression16: "uppaal_types_IntegerBounds", Expression124: "uppaal_statements_DoWhileLoop", Expression116: "uppaal_statements_WhileLoop", Expression172: "uppaal_expressions_IncrementDecrementExpression", Expression109: "uppaal_statements_ForLoop", Expression151: "uppaal_expressions_IdentifierExpression", Expression126: "uppaal_statements_IfStatement", Expression48: "uppaal_system_TemplateDeclaration", Expression52: "uppaal_system_ProgressMeasure", Expression10: "uppaal_types_DeclaredType", Expression170: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_expressions_PlusExpression", Expression134: "uppaal_statements_ReturnStatement", Expression33: "uppaal_declarations_Variable", Expression144: "uppaal_expressions_BinaryExpression"):
        self.prefix = prefix
        self.uppaal_expressions_DataPrefixExpression = uppaal_expressions_DataPrefixExpression
        
    @property
    def prefix(self) -> str:
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
            if hasattr(old_value, "Expression175"):
                opp_val = getattr(old_value, "Expression175", None)
                if opp_val == self:
                    setattr(old_value, "Expression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression175"):
                opp_val = getattr(value, "Expression175", None)
                setattr(value, "Expression175", self)

class uppaal_expressions_PlusExpression(Expression):

    pass
class uppaal_expressions_FunctionCallExpression(Expression):

    pass
class uppaal_types_TypeExpression(Expression):

    pass
class uppaal_expressions_IncrementDecrementExpression(Expression):

    def __init__(self, operator: str, uppaal_expressions_IncrementDecrementExpression: "Expression" = None, Expression147: "uppaal_expressions_BinaryExpression", Expression71: "uppaal_templates_Location", Expression103: "uppaal_statements_ForLoop", Expression168: "uppaal_expressions_ConditionExpression", Expression153: "uppaal_expressions_ScopedIdentifierExpression", Expression165: "uppaal_expressions_ConditionExpression", Expression138: "uppaal_expressions_NegationExpression", Expression106: "uppaal_statements_ForLoop", Expression37: "uppaal_declarations_TypedElementContainer", Expression175: "uppaal_expressions_DataPrefixExpression", Expression19: "uppaal_types_IntegerBounds", Expression142: "uppaal_expressions_MinusExpression", Expression: "uppaal_core_TypedElement", Expression12: "uppaal_types_ScalarTypeSpecification", Expression160: "uppaal_expressions_FunctionCallExpression", Expression91: "uppaal_templates_Edge", Expression136: "uppaal_statements_ExpressionStatement", Expression40: "uppaal_declarations_ExpressionInitializer", Expression88: "uppaal_templates_Edge", Expression31: "uppaal_declarations_TypeDeclaration", Expression162: "uppaal_expressions_ConditionExpression", Expression16: "uppaal_types_IntegerBounds", Expression124: "uppaal_statements_DoWhileLoop", Expression116: "uppaal_statements_WhileLoop", Expression172: "uppaal_expressions_IncrementDecrementExpression", Expression109: "uppaal_statements_ForLoop", Expression151: "uppaal_expressions_IdentifierExpression", Expression126: "uppaal_statements_IfStatement", Expression48: "uppaal_system_TemplateDeclaration", Expression52: "uppaal_system_ProgressMeasure", Expression10: "uppaal_types_DeclaredType", Expression170: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_expressions_PlusExpression", Expression134: "uppaal_statements_ReturnStatement", Expression33: "uppaal_declarations_Variable", Expression144: "uppaal_expressions_BinaryExpression"):
        self.operator = operator
        self.uppaal_expressions_IncrementDecrementExpression = uppaal_expressions_IncrementDecrementExpression
        
    @property
    def operator(self) -> str:
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
            if hasattr(old_value, "Expression172"):
                opp_val = getattr(old_value, "Expression172", None)
                if opp_val == self:
                    setattr(old_value, "Expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression172"):
                opp_val = getattr(value, "Expression172", None)
                setattr(value, "Expression172", self)

class uppaal_expressions_LiteralExpression(Expression):

    def __init__(self, text: str, Expression147: "uppaal_expressions_BinaryExpression", Expression71: "uppaal_templates_Location", Expression103: "uppaal_statements_ForLoop", Expression168: "uppaal_expressions_ConditionExpression", Expression153: "uppaal_expressions_ScopedIdentifierExpression", Expression165: "uppaal_expressions_ConditionExpression", Expression138: "uppaal_expressions_NegationExpression", Expression106: "uppaal_statements_ForLoop", Expression37: "uppaal_declarations_TypedElementContainer", Expression175: "uppaal_expressions_DataPrefixExpression", Expression19: "uppaal_types_IntegerBounds", Expression142: "uppaal_expressions_MinusExpression", Expression: "uppaal_core_TypedElement", Expression12: "uppaal_types_ScalarTypeSpecification", Expression160: "uppaal_expressions_FunctionCallExpression", Expression91: "uppaal_templates_Edge", Expression136: "uppaal_statements_ExpressionStatement", Expression40: "uppaal_declarations_ExpressionInitializer", Expression88: "uppaal_templates_Edge", Expression31: "uppaal_declarations_TypeDeclaration", Expression162: "uppaal_expressions_ConditionExpression", Expression16: "uppaal_types_IntegerBounds", Expression124: "uppaal_statements_DoWhileLoop", Expression116: "uppaal_statements_WhileLoop", Expression172: "uppaal_expressions_IncrementDecrementExpression", Expression109: "uppaal_statements_ForLoop", Expression151: "uppaal_expressions_IdentifierExpression", Expression126: "uppaal_statements_IfStatement", Expression48: "uppaal_system_TemplateDeclaration", Expression52: "uppaal_system_ProgressMeasure", Expression10: "uppaal_types_DeclaredType", Expression170: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_expressions_PlusExpression", Expression134: "uppaal_statements_ReturnStatement", Expression33: "uppaal_declarations_Variable", Expression144: "uppaal_expressions_BinaryExpression"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class uppaal_core_TypedElement(ABC):

    pass
class uppaal_core_CommentableElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class uppaal_core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SystemDeclarations:

    pass
class Template:

    pass
class GlobalDeclarations:

    pass
class core_CommentableElement:

    pass
class uppaal_templates_Edge(visuals_ColoredElement, core_CommentableElement, visuals_LinearElement):

    pass
class core_NamedElement:

    pass
class uppaal_declarations_Function(core_TypedElement, core_NamedElement):

    pass
class uppaal_declarations_Variable(core_TypedElement, core_NamedElement):

    pass
class uppaal_templates_Location(visuals_PlanarElement, core_NamedElement, core_CommentableElement, visuals_ColoredElement):

    def __init__(self, locationTimeKind: str, uppaal_templates_Location: "Expression" = None, Edge73: set["Edge"] = None, Edge76: set["Edge"] = None, Template68: "Template" = None):
        self.locationTimeKind = locationTimeKind
        self.uppaal_templates_Location = uppaal_templates_Location
        self.Edge73 = Edge73 if Edge73 is not None else set()
        self.Edge76 = Edge76 if Edge76 is not None else set()
        self.Template68 = Template68
        
    @property
    def locationTimeKind(self) -> str:
        return self.__locationTimeKind

    @locationTimeKind.setter
    def locationTimeKind(self, locationTimeKind: str):
        self.__locationTimeKind = locationTimeKind

    @property
    def Template68(self):
        return self.__Template68

    @Template68.setter
    def Template68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__Template68", None)
        self.__Template68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "templates69"):
                opp_val = getattr(old_value, "templates69", None)
                if opp_val == self:
                    setattr(old_value, "templates69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templates69"):
                opp_val = getattr(value, "templates69", None)
                setattr(value, "templates69", self)

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
            if hasattr(old_value, "Expression71"):
                opp_val = getattr(old_value, "Expression71", None)
                if opp_val == self:
                    setattr(old_value, "Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression71"):
                opp_val = getattr(value, "Expression71", None)
                setattr(value, "Expression71", self)

    @property
    def Edge73(self):
        return self.__Edge73

    @Edge73.setter
    def Edge73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__Edge73", None)
        self.__Edge73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "templates74"):
                    opp_val = getattr(item, "templates74", None)
                    
                    if opp_val == self:
                        setattr(item, "templates74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "templates74"):
                    opp_val = getattr(item, "templates74", None)
                    
                    setattr(item, "templates74", self)
                    

    @property
    def Edge76(self):
        return self.__Edge76

    @Edge76.setter
    def Edge76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__Edge76", None)
        self.__Edge76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "templates77"):
                    opp_val = getattr(item, "templates77", None)
                    
                    if opp_val == self:
                        setattr(item, "templates77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "templates77"):
                    opp_val = getattr(item, "templates77", None)
                    
                    setattr(item, "templates77", self)
                    

class uppaal_NTA(core_NamedElement, core_CommentableElement):

    pass
class TypedElementContainer:

    pass
class uppaal_templates_Selection(TypedElementContainer):

    pass
class uppaal_declarations_ParameterContainer(TypedElementContainer):

    pass