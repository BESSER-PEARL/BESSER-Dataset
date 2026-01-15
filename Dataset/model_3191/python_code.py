from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BitShiftOperator(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class IncrementDecrementOperator(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class DataVariablePrefix(Enum):
    NONE = "NONE"
    CONST = "CONST"
    META = "META"
class CompareOperator(Enum):
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    UNEQUAL = "UNEQUAL"
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
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
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    IMPLY = "IMPLY"
class IncrementDecrementPosition(Enum):
    PRE = "PRE"
    POST = "POST"
class LocationKind(Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"
    COMMITED = "COMMITED"
class Quantifier(Enum):
    EXISTENTIAL = "EXISTENTIAL"
    UNIVERSAL = "UNIVERSAL"
class ArithmeticOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLICATE = "MULTIPLICATE"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
class MinMaxOperator(Enum):
    MIN = "MIN"
    MAX = "MAX"
class BuiltInType(Enum):
    INT = "INT"
    CLOCK = "CLOCK"
    CHAN = "CHAN"
    BOOL = "BOOL"
    VOID = "VOID"
class BitwiseOperator(Enum):
    AND = "AND"
    XOR = "XOR"
    OR = "OR"
class ColorKind(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    SELF_DEFINED = "SELF_DEFINED"
    DEFAULT = "DEFAULT"
    WHITE = "WHITE"
    LIGHTGREY = "LIGHTGREY"
    DARKGREY = "DARKGREY"
    BLACK = "BLACK"
    BLUE = "BLUE"
    CYAN = "CYAN"
    GREEN = "GREEN"
    MAGENTA = "MAGENTA"
    ORANGE = "ORANGE"
    PINK = "PINK"
class CallType(Enum):
    CALL_BY_VALUE = "CALL_BY_VALUE"
    CALL_BY_REFERENCE = "CALL_BY_REFERENCE"


############################################
# Definition of Classes
############################################

class uppaal_visuals_Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
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

    def __init__(self, color: str, colorCode: str):
        self.color = color
        self.colorCode = colorCode
        
    @property
    def colorCode(self) -> str:
        return self.__colorCode

    @colorCode.setter
    def colorCode(self, colorCode: str):
        self.__colorCode = colorCode

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class expressions_Expression:

    pass
class uppaal_expressions_Expression(ABC):

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

class uppaal_expressions_BitwiseExpression(BinaryExpression):

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

class uppaal_expressions_BitShiftExpression(BinaryExpression):

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

class uppaal_expressions_ArithmeticExpression(BinaryExpression):

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

class Statement:

    pass
class uppaal_statements_IfStatement(Statement):

    pass
class uppaal_statements_ExpressionStatement(Statement):

    pass
class uppaal_statements_ForLoop(Statement):

    pass
class uppaal_statements_DoWhileLoop(Statement):

    pass
class uppaal_statements_EmptyStatement(Statement):

    pass
class uppaal_statements_ReturnStatement(Statement):

    pass
class uppaal_statements_Block(Statement):

    pass
class uppaal_statements_WhileLoop(Statement):

    pass
class statements_Statement:

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
            if hasattr(old_value, "IdentifierExpression115"):
                opp_val = getattr(old_value, "IdentifierExpression115", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierExpression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierExpression115"):
                opp_val = getattr(value, "IdentifierExpression115", None)
                setattr(value, "IdentifierExpression115", self)

class Selection:

    pass
class Synchronization:

    pass
class uppaal_statements_Statement(ABC):

    pass
class visuals_ColoredElement:

    pass
class visuals_PlanarElement:

    pass
class system_TemplateDeclaration:

    pass
class visuals_LinearElement:

    pass
class Edge:

    pass
class Location:

    pass
class LocalDeclarations:

    pass
class uppaal_system_System:

    pass
class RedefinedTemplate:

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
class uppaal_global_ChannelPriorityItem(ABC):

    pass
class global_ChannelPriorityItem:

    pass
class uppaal_global_ChannelPriority:

    pass
class IdentifierExpression:

    pass
class ChannelPriorityItem:

    pass
class uppaal_global_DefaultChannelPriority(ChannelPriorityItem):

    pass
class uppaal_global_ChannelList(ChannelPriorityItem):

    pass
class uppaal_declarations_Initializer(ABC):

    pass
class Variable:

    pass
class uppaal_declarations_VariableContainer(ABC):

    pass
class uppaal_declarations_Parameter:

    def __init__(self, callType: str, uppaal_declarations_Parameter: "VariableDeclaration" = None):
        self.callType = callType
        self.uppaal_declarations_Parameter = uppaal_declarations_Parameter
        
    @property
    def callType(self) -> str:
        return self.__callType

    @callType.setter
    def callType(self, callType: str):
        self.__callType = callType

    @property
    def uppaal_declarations_Parameter(self):
        return self.__uppaal_declarations_Parameter

    @uppaal_declarations_Parameter.setter
    def uppaal_declarations_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_declarations_Parameter__uppaal_declarations_Parameter", None)
        self.__uppaal_declarations_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration"):
                opp_val = getattr(old_value, "VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration"):
                opp_val = getattr(value, "VariableDeclaration", None)
                setattr(value, "VariableDeclaration", self)

class VariableContainer:

    pass
class uppaal_templates_Selection(VariableContainer):

    pass
class DeclaredType:

    pass
class Function:

    pass
class Parameter:

    pass
class uppaal_declarations_Index(ABC):

    pass
class Initializer:

    pass
class uppaal_declarations_ArrayInitializer(Initializer):

    pass
class uppaal_declarations_ExpressionInitializer(Initializer):

    pass
class Block:

    pass
class global_ChannelPriority:

    pass
class Declarations:

    pass
class uppaal_declarations_LocalDeclarations(Declarations):

    pass
class uppaal_declarations_SystemDeclarations(Declarations):

    pass
class uppaal_declarations_GlobalDeclarations(Declarations):

    pass
class Declaration:

    pass
class uppaal_declarations_FunctionDeclaration(Declaration):

    pass
class uppaal_declarations_TypeDeclaration(Declaration):

    pass
class uppaal_system_TemplateDeclaration(Declaration):

    pass
class VariableDeclaration:

    pass
class uppaal_declarations_DataVariableDeclaration(VariableDeclaration):

    def __init__(self, prefix: str, VariableDeclaration: "uppaal_declarations_Parameter"):
        self.prefix = prefix
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

class uppaal_declarations_ClockVariableDeclaration(VariableDeclaration):

    pass
class uppaal_declarations_ChannelVariableDeclaration(VariableDeclaration):

    def __init__(self, urgent: bool, broadcast: bool, VariableDeclaration: "uppaal_declarations_Parameter"):
        self.urgent = urgent
        self.broadcast = broadcast
        
    @property
    def broadcast(self) -> bool:
        return self.__broadcast

    @broadcast.setter
    def broadcast(self, broadcast: bool):
        self.__broadcast = broadcast

    @property
    def urgent(self) -> bool:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent

class declarations_VariableContainer:

    pass
class uppaal_statements_Iteration(declarations_VariableContainer, statements_Statement):

    pass
class uppaal_expressions_QuantificationExpression(declarations_VariableContainer, expressions_Expression):

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
            if hasattr(old_value, "Expression189"):
                opp_val = getattr(old_value, "Expression189", None)
                if opp_val == self:
                    setattr(old_value, "Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression189"):
                opp_val = getattr(value, "Expression189", None)
                setattr(value, "Expression189", self)

class declarations_Declaration:

    pass
class uppaal_declarations_VariableDeclaration(declarations_VariableContainer, declarations_Declaration):

    pass
class uppaal_declarations_Declaration(ABC):

    pass
class system_ProgressMeasure:

    pass
class system_System:

    pass
class DataVariableDeclaration:

    pass
class Expression:

    pass
class uppaal_expressions_BinaryExpression(Expression):

    pass
class uppaal_expressions_IncrementDecrementExpression(Expression):

    def __init__(self, position: str, operator: str, uppaal_expressions_IncrementDecrementExpression: "Expression" = None, Expression124: "uppaal_statements_ForLoop", Expression127: "uppaal_statements_ForLoop", Expression95: "uppaal_templates_Location", Expression106: "uppaal_templates_Edge", Expression: "uppaal_types_ScalarTypeSpecification", Expression134: "uppaal_statements_WhileLoop", Expression169: "uppaal_expressions_IdentifierExpression", Expression162: "uppaal_expressions_BinaryExpression", Expression109: "uppaal_templates_Edge", Expression72: "uppaal_system_TemplateDeclaration", Expression76: "uppaal_system_ProgressMeasure", Expression156: "uppaal_expressions_NegationExpression", Expression154: "uppaal_statements_ExpressionStatement", Expression179: "uppaal_expressions_ConditionExpression", Expression30: "uppaal_types_IntegerBounds", Expression182: "uppaal_expressions_ConditionExpression", Expression160: "uppaal_expressions_MinusExpression", Expression27: "uppaal_types_IntegerBounds", Expression174: "uppaal_expressions_FunctionCallExpression", Expression158: "uppaal_expressions_PlusExpression", Expression191: "uppaal_expressions_IncrementDecrementExpression", Expression152: "uppaal_statements_ReturnStatement", Expression65: "uppaal_declarations_ExpressionInitializer", Expression184: "uppaal_expressions_ScopedIdentifierExpression", Expression144: "uppaal_statements_IfStatement", Expression176: "uppaal_expressions_ConditionExpression", Expression142: "uppaal_statements_DoWhileLoop", Expression56: "uppaal_declarations_ValueIndex", Expression189: "uppaal_expressions_QuantificationExpression", Expression121: "uppaal_statements_ForLoop", Expression165: "uppaal_expressions_BinaryExpression"):
        self.position = position
        self.operator = operator
        self.uppaal_expressions_IncrementDecrementExpression = uppaal_expressions_IncrementDecrementExpression
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

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
            if hasattr(old_value, "Expression191"):
                opp_val = getattr(old_value, "Expression191", None)
                if opp_val == self:
                    setattr(old_value, "Expression191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression191"):
                opp_val = getattr(value, "Expression191", None)
                setattr(value, "Expression191", self)

class uppaal_expressions_PlusExpression(Expression):

    pass
class uppaal_expressions_ScopedIdentifierExpression(Expression):

    pass
class uppaal_expressions_FunctionCallExpression(Expression):

    pass
class uppaal_expressions_IdentifierExpression(Expression):

    pass
class uppaal_expressions_LiteralExpression(Expression):

    def __init__(self, text: str, Expression124: "uppaal_statements_ForLoop", Expression127: "uppaal_statements_ForLoop", Expression95: "uppaal_templates_Location", Expression106: "uppaal_templates_Edge", Expression: "uppaal_types_ScalarTypeSpecification", Expression134: "uppaal_statements_WhileLoop", Expression169: "uppaal_expressions_IdentifierExpression", Expression162: "uppaal_expressions_BinaryExpression", Expression109: "uppaal_templates_Edge", Expression72: "uppaal_system_TemplateDeclaration", Expression76: "uppaal_system_ProgressMeasure", Expression156: "uppaal_expressions_NegationExpression", Expression154: "uppaal_statements_ExpressionStatement", Expression179: "uppaal_expressions_ConditionExpression", Expression30: "uppaal_types_IntegerBounds", Expression182: "uppaal_expressions_ConditionExpression", Expression160: "uppaal_expressions_MinusExpression", Expression27: "uppaal_types_IntegerBounds", Expression174: "uppaal_expressions_FunctionCallExpression", Expression158: "uppaal_expressions_PlusExpression", Expression191: "uppaal_expressions_IncrementDecrementExpression", Expression152: "uppaal_statements_ReturnStatement", Expression65: "uppaal_declarations_ExpressionInitializer", Expression184: "uppaal_expressions_ScopedIdentifierExpression", Expression144: "uppaal_statements_IfStatement", Expression176: "uppaal_expressions_ConditionExpression", Expression142: "uppaal_statements_DoWhileLoop", Expression56: "uppaal_declarations_ValueIndex", Expression189: "uppaal_expressions_QuantificationExpression", Expression121: "uppaal_statements_ForLoop", Expression165: "uppaal_expressions_BinaryExpression"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class uppaal_expressions_NegationExpression(Expression):

    pass
class uppaal_expressions_ConditionExpression(Expression):

    pass
class uppaal_expressions_MinusExpression(Expression):

    pass
class TypeSpecification:

    pass
class uppaal_types_StructTypeSpecification(TypeSpecification):

    pass
class uppaal_types_ScalarTypeSpecification(TypeSpecification):

    pass
class uppaal_declarations_Declarations(ABC):

    pass
class uppaal_types_IntegerBounds:

    pass
class IntegerBounds:

    pass
class uppaal_types_RangeTypeSpecification(TypeSpecification):

    pass
class Type:

    pass
class uppaal_types_PredefinedType(Type):

    def __init__(self, type: str, Type: "uppaal_types_TypeReference"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Index:

    pass
class uppaal_declarations_ValueIndex(Index):

    pass
class uppaal_declarations_TypeIndex(Index):

    pass
class NamedElement:

    pass
class uppaal_declarations_Function(NamedElement):

    pass
class uppaal_declarations_Variable(NamedElement):

    pass
class uppaal_types_Type(NamedElement):

    def __init__(self, baseType: str, uppaal_types_Type: set["Index"] = None, NamedElement: "uppaal_expressions_IdentifierExpression"):
        self.baseType = baseType
        self.uppaal_types_Type = uppaal_types_Type if uppaal_types_Type is not None else set()
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

    @property
    def uppaal_types_Type(self):
        return self.__uppaal_types_Type

    @uppaal_types_Type.setter
    def uppaal_types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_types_Type__uppaal_types_Type", None)
        self.__uppaal_types_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    if opp_val == self:
                        setattr(item, "Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    setattr(item, "Index", self)
                    

class uppaal_core_CommentableElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class uppaal_types_TypeDefinition(ABC):

    def __init__(self, baseType: str):
        self.baseType = baseType
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

class TypeDefinition:

    pass
class uppaal_types_TypeReference(TypeDefinition):

    pass
class uppaal_types_TypeSpecification(TypeDefinition):

    pass
class TypeDeclaration:

    pass
class uppaal_types_DeclaredType(Type):

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
class uppaal_templates_AbstractTemplate(core_CommentableElement, core_NamedElement):

    pass
class uppaal_templates_Location(visuals_ColoredElement, visuals_PlanarElement, core_CommentableElement, core_NamedElement):

    def __init__(self, locationTimeKind: str, Template92: "Template" = None, uppaal_templates_Location: "Expression" = None):
        self.locationTimeKind = locationTimeKind
        self.Template92 = Template92
        self.uppaal_templates_Location = uppaal_templates_Location
        
    @property
    def locationTimeKind(self) -> str:
        return self.__locationTimeKind

    @locationTimeKind.setter
    def locationTimeKind(self, locationTimeKind: str):
        self.__locationTimeKind = locationTimeKind

    @property
    def Template92(self):
        return self.__Template92

    @Template92.setter
    def Template92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__Template92", None)
        self.__Template92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "templates93"):
                opp_val = getattr(old_value, "templates93", None)
                if opp_val == self:
                    setattr(old_value, "templates93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templates93"):
                opp_val = getattr(value, "templates93", None)
                setattr(value, "templates93", self)

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
            if hasattr(old_value, "Expression95"):
                opp_val = getattr(old_value, "Expression95", None)
                if opp_val == self:
                    setattr(old_value, "Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression95"):
                opp_val = getattr(value, "Expression95", None)
                setattr(value, "Expression95", self)

class uppaal_NTA(core_CommentableElement, core_NamedElement):

    pass
class uppaal_core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PredefinedType:

    pass
class SystemDeclarations:

    pass