from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssignmentOperator(Enum):
    BIT_AND_EQUAL = "BIT_AND_EQUAL"
    BIT_OR_EQUAL = "BIT_OR_EQUAL"
    BIT_LEFT_EQUAL = "BIT_LEFT_EQUAL"
    BIT_RIGHT_EQUAL = "BIT_RIGHT_EQUAL"
    BIT_XOR_EQUAL = "BIT_XOR_EQUAL"
    EQUAL = "EQUAL"
    PLUS_EQUAL = "PLUS_EQUAL"
    MINUS_EQUAL = "MINUS_EQUAL"
    TIMES_EQUAL = "TIMES_EQUAL"
    DIVIDE_EQUAL = "DIVIDE_EQUAL"
    MODULO_EQUAL = "MODULO_EQUAL"
class CompareOperator(Enum):
    EQUAL = "EQUAL"
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    UNEQUAL = "UNEQUAL"
class SynchronizationKind(Enum):
    RECEIVE = "RECEIVE"
    SEND = "SEND"
class MinMaxOperator(Enum):
    MIN = "MIN"
    MAX = "MAX"
class LocationKind(Enum):
    NORMAL = "NORMAL"
    URGENT = "URGENT"
    COMMITED = "COMMITED"
class ColorKind(Enum):
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
    RED = "RED"
    YELLOW = "YELLOW"
    SELF_DEFINED = "SELF_DEFINED"
    DEFAULT = "DEFAULT"
class Quantifier(Enum):
    EXISTENTIAL = "EXISTENTIAL"
    UNIVERSAL = "UNIVERSAL"
class CallType(Enum):
    CALL_BY_VALUE = "CALL_BY_VALUE"
    CALL_BY_REFERENCE = "CALL_BY_REFERENCE"
class DataVariablePrefix(Enum):
    NONE = "NONE"
    CONST = "CONST"
    META = "META"
class BitwiseOperator(Enum):
    AND = "AND"
    XOR = "XOR"
    OR = "OR"
class IncrementDecrementOperator(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class ArithmeticOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLICATE = "MULTIPLICATE"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
class BitShiftOperator(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
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
class IncrementDecrementPosition(Enum):
    PRE = "PRE"
    POST = "POST"


############################################
# Definition of Classes
############################################

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

class uppaal_visuals_ColoredElement(ABC):

    def __init__(self, color: str, colorCode: str):
        self.color = color
        self.colorCode = colorCode
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def colorCode(self) -> str:
        return self.__colorCode

    @colorCode.setter
    def colorCode(self, colorCode: str):
        self.__colorCode = colorCode

class uppaal_visuals_LinearElement(ABC):

    pass
class Point:

    pass
class uppaal_visuals_PlanarElement(ABC):

    pass
class expressions_Expression:

    pass
class BinaryExpression:

    pass
class uppaal_expressions_BitShiftExpression(BinaryExpression):

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

class uppaal_expressions_MinMaxExpression(BinaryExpression):

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
class Statement:

    pass
class uppaal_statements_IfStatement(Statement):

    pass
class uppaal_statements_ForLoop(Statement):

    pass
class uppaal_statements_WhileLoop(Statement):

    pass
class uppaal_statements_DoWhileLoop(Statement):

    pass
class uppaal_statements_EmptyStatement(Statement):

    pass
class uppaal_statements_ExpressionStatement(Statement):

    pass
class uppaal_statements_ReturnStatement(Statement):

    pass
class uppaal_statements_Block(Statement):

    pass
class uppaal_statements_Statement(ABC):

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
            if hasattr(old_value, "IdentifierExpression121"):
                opp_val = getattr(old_value, "IdentifierExpression121", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierExpression121"):
                opp_val = getattr(value, "IdentifierExpression121", None)
                setattr(value, "IdentifierExpression121", self)

class Selection:

    pass
class Synchronization:

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
class uppaal_system_InstantiationList:

    pass
class system_InstantiationList:

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
class IdentifierExpression:

    pass
class RedefinedTemplate:

    pass
class uppaal_declarations_Initializer(ABC):

    pass
class ChannelPriorityItem:

    pass
class uppaal_global_DefaultChannelPriority(ChannelPriorityItem):

    pass
class uppaal_global_ChannelList(ChannelPriorityItem):

    pass
class uppaal_global_ChannelPriorityItem(ABC):

    pass
class global_ChannelPriorityItem:

    pass
class uppaal_global_ChannelPriority:

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

class Variable:

    pass
class uppaal_declarations_VariableContainer(ABC):

    pass
class uppaal_declarations_Index(ABC):

    pass
class Initializer:

    pass
class uppaal_declarations_ArrayInitializer(Initializer):

    pass
class uppaal_declarations_ExpressionInitializer(Initializer):

    pass
class VariableContainer:

    pass
class uppaal_templates_Selection(VariableContainer):

    pass
class DeclaredType:

    pass
class Parameter:

    pass
class Function:

    pass
class Block:

    pass
class VariableDeclaration:

    pass
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
class uppaal_expressions_QuantificationExpression(expressions_Expression, declarations_VariableContainer):

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
            if hasattr(old_value, "Expression195"):
                opp_val = getattr(old_value, "Expression195", None)
                if opp_val == self:
                    setattr(old_value, "Expression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression195"):
                opp_val = getattr(value, "Expression195", None)
                setattr(value, "Expression195", self)

class uppaal_statements_Iteration(statements_Statement, declarations_VariableContainer):

    pass
class declarations_Declaration:

    pass
class uppaal_declarations_VariableDeclaration(declarations_VariableContainer, declarations_Declaration):

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

class system_System:

    pass
class global_ChannelPriority:

    pass
class uppaal_declarations_Declaration(ABC):

    pass
class system_ProgressMeasure:

    pass
class uppaal_declarations_Declarations(ABC):

    pass
class uppaal_types_Library:

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
class uppaal_system_TemplateDeclaration(Declaration):

    pass
class uppaal_declarations_FunctionDeclaration(Declaration):

    pass
class uppaal_declarations_TypeDeclaration(Declaration):

    pass
class DataVariableDeclaration:

    pass
class Expression:

    pass
class uppaal_expressions_ConditionExpression(Expression):

    pass
class uppaal_expressions_PlusExpression(Expression):

    pass
class uppaal_expressions_FunctionCallExpression(Expression):

    pass
class uppaal_expressions_BinaryExpression(Expression):

    pass
class uppaal_expressions_LiteralExpression(Expression):

    def __init__(self, text: str, Expression185: "uppaal_expressions_ConditionExpression", Expression133: "uppaal_statements_ForLoop", Expression34: "uppaal_types_IntegerBounds", Expression115: "uppaal_templates_Edge", Expression188: "uppaal_expressions_ConditionExpression", Expression175: "uppaal_expressions_IdentifierExpression", Expression197: "uppaal_expressions_IncrementDecrementExpression", Expression71: "uppaal_declarations_ExpressionInitializer", Expression31: "uppaal_types_IntegerBounds", Expression195: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_statements_WhileLoop", Expression78: "uppaal_system_TemplateDeclaration", Expression182: "uppaal_expressions_ConditionExpression", Expression112: "uppaal_templates_Edge", Expression148: "uppaal_statements_DoWhileLoop", Expression164: "uppaal_expressions_PlusExpression", Expression168: "uppaal_expressions_BinaryExpression", Expression166: "uppaal_expressions_MinusExpression", Expression190: "uppaal_expressions_ScopedIdentifierExpression", Expression82: "uppaal_system_ProgressMeasure", Expression127: "uppaal_statements_ForLoop", Expression158: "uppaal_statements_ReturnStatement", Expression171: "uppaal_expressions_BinaryExpression", Expression130: "uppaal_statements_ForLoop", Expression62: "uppaal_declarations_ValueIndex", Expression150: "uppaal_statements_IfStatement", Expression180: "uppaal_expressions_FunctionCallExpression", Expression: "uppaal_types_ScalarTypeSpecification", Expression101: "uppaal_templates_Location", Expression162: "uppaal_expressions_NegationExpression", Expression160: "uppaal_statements_ExpressionStatement"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class uppaal_expressions_ScopedIdentifierExpression(Expression):

    pass
class uppaal_expressions_IdentifierExpression(Expression):

    pass
class uppaal_expressions_IncrementDecrementExpression(Expression):

    def __init__(self, position: str, operator: str, uppaal_expressions_IncrementDecrementExpression: "Expression" = None, Expression185: "uppaal_expressions_ConditionExpression", Expression133: "uppaal_statements_ForLoop", Expression34: "uppaal_types_IntegerBounds", Expression115: "uppaal_templates_Edge", Expression188: "uppaal_expressions_ConditionExpression", Expression175: "uppaal_expressions_IdentifierExpression", Expression197: "uppaal_expressions_IncrementDecrementExpression", Expression71: "uppaal_declarations_ExpressionInitializer", Expression31: "uppaal_types_IntegerBounds", Expression195: "uppaal_expressions_QuantificationExpression", Expression140: "uppaal_statements_WhileLoop", Expression78: "uppaal_system_TemplateDeclaration", Expression182: "uppaal_expressions_ConditionExpression", Expression112: "uppaal_templates_Edge", Expression148: "uppaal_statements_DoWhileLoop", Expression164: "uppaal_expressions_PlusExpression", Expression168: "uppaal_expressions_BinaryExpression", Expression166: "uppaal_expressions_MinusExpression", Expression190: "uppaal_expressions_ScopedIdentifierExpression", Expression82: "uppaal_system_ProgressMeasure", Expression127: "uppaal_statements_ForLoop", Expression158: "uppaal_statements_ReturnStatement", Expression171: "uppaal_expressions_BinaryExpression", Expression130: "uppaal_statements_ForLoop", Expression62: "uppaal_declarations_ValueIndex", Expression150: "uppaal_statements_IfStatement", Expression180: "uppaal_expressions_FunctionCallExpression", Expression: "uppaal_types_ScalarTypeSpecification", Expression101: "uppaal_templates_Location", Expression162: "uppaal_expressions_NegationExpression", Expression160: "uppaal_statements_ExpressionStatement"):
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
            if hasattr(old_value, "Expression197"):
                opp_val = getattr(old_value, "Expression197", None)
                if opp_val == self:
                    setattr(old_value, "Expression197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression197"):
                opp_val = getattr(value, "Expression197", None)
                setattr(value, "Expression197", self)

class uppaal_expressions_MinusExpression(Expression):

    pass
class uppaal_expressions_NegationExpression(Expression):

    pass
class uppaal_types_IntegerBounds:

    pass
class IntegerBounds:

    pass
class uppaal_types_TypeDefinition(ABC):

    def __init__(self, baseType: str, uppaal_types_TypeDefinition: "TypeSpecification" = None):
        self.baseType = baseType
        self.uppaal_types_TypeDefinition = uppaal_types_TypeDefinition
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

    @property
    def uppaal_types_TypeDefinition(self):
        return self.__uppaal_types_TypeDefinition

    @uppaal_types_TypeDefinition.setter
    def uppaal_types_TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_types_TypeDefinition__uppaal_types_TypeDefinition", None)
        self.__uppaal_types_TypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeSpecification25"):
                opp_val = getattr(old_value, "TypeSpecification25", None)
                if opp_val == self:
                    setattr(old_value, "TypeSpecification25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeSpecification25"):
                opp_val = getattr(value, "TypeSpecification25", None)
                setattr(value, "TypeSpecification25", self)

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

class TypeSpecification:

    pass
class uppaal_types_StructTypeSpecification(TypeSpecification):

    pass
class uppaal_types_RangeTypeSpecification(TypeSpecification):

    pass
class uppaal_types_ScalarTypeSpecification(TypeSpecification):

    pass
class TypeDefinition:

    pass
class uppaal_types_TypeSpecification(TypeDefinition):

    pass
class uppaal_types_TypeReference(TypeDefinition):

    pass
class TypeDeclaration:

    pass
class uppaal_types_DeclaredType(Type):

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

class Index:

    pass
class uppaal_declarations_TypeIndex(Index):

    pass
class uppaal_declarations_ValueIndex(Index):

    pass
class NamedElement:

    pass
class uppaal_declarations_Variable(NamedElement):

    pass
class uppaal_declarations_Function(NamedElement):

    pass
class uppaal_types_Type(NamedElement):

    def __init__(self, baseType: str, uppaal_types_Type: set["Index"] = None, uppaal_types_Type21: "TypeSpecification" = None, NamedElement: "uppaal_expressions_IdentifierExpression"):
        self.baseType = baseType
        self.uppaal_types_Type = uppaal_types_Type if uppaal_types_Type is not None else set()
        self.uppaal_types_Type21 = uppaal_types_Type21
        
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
                    

    @property
    def uppaal_types_Type21(self):
        return self.__uppaal_types_Type21

    @uppaal_types_Type21.setter
    def uppaal_types_Type21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_types_Type__uppaal_types_Type21", None)
        self.__uppaal_types_Type21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeSpecification"):
                opp_val = getattr(old_value, "TypeSpecification", None)
                if opp_val == self:
                    setattr(old_value, "TypeSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeSpecification"):
                opp_val = getattr(value, "TypeSpecification", None)
                setattr(value, "TypeSpecification", self)

class PredefinedType:

    pass
class core_CommentableElement:

    pass
class uppaal_templates_Edge(visuals_ColoredElement, visuals_LinearElement, core_CommentableElement):

    pass
class core_NamedElement:

    pass
class uppaal_templates_AbstractTemplate(core_NamedElement, core_CommentableElement):

    pass
class uppaal_templates_Location(visuals_ColoredElement, core_NamedElement, visuals_PlanarElement, core_CommentableElement):

    def __init__(self, locationTimeKind: str, Template98: "Template" = None, uppaal_templates_Location: "Expression" = None):
        self.locationTimeKind = locationTimeKind
        self.Template98 = Template98
        self.uppaal_templates_Location = uppaal_templates_Location
        
    @property
    def locationTimeKind(self) -> str:
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
            if hasattr(old_value, "Expression101"):
                opp_val = getattr(old_value, "Expression101", None)
                if opp_val == self:
                    setattr(old_value, "Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression101"):
                opp_val = getattr(value, "Expression101", None)
                setattr(value, "Expression101", self)

    @property
    def Template98(self):
        return self.__Template98

    @Template98.setter
    def Template98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaal_templates_Location__Template98", None)
        self.__Template98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "templates99"):
                opp_val = getattr(old_value, "templates99", None)
                if opp_val == self:
                    setattr(old_value, "templates99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "templates99"):
                opp_val = getattr(value, "templates99", None)
                setattr(value, "templates99", self)

class uppaal_NTA(core_NamedElement, core_CommentableElement):

    pass
class SystemDeclarations:

    pass
class Template:

    pass
class GlobalDeclarations:

    pass