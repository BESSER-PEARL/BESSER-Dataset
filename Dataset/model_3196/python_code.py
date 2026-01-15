from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FixedExpressionType(Enum):
    Deadlock = "Deadlock"
    True = "True"
    False = "False"
class TypePrefix(Enum):
    CONSTANT = "CONSTANT"
    NONE = "NONE"
    URGENT = "URGENT"
    BROADCAST = "BROADCAST"
    META = "META"
class PriorityOperator(Enum):
    Seperator = "Seperator"
    LessThan = "LessThan"
class UnaryOperator(Enum):
    NOT = "NOT"
    PLUS = "PLUS"
    MINUS = "MINUS"
class TypeId(Enum):
    Integer = "Integer"
    Clock = "Clock"
    Channel = "Channel"
    Boolean = "Boolean"
    Void = "Void"
class AssignOperator(Enum):
    ASSIGN = "ASSIGN"
    ADD_ASIGN = "ADD_ASIGN"
    SUB_ASSIGN = "SUB_ASSIGN"
    DIV_ASSIGN = "DIV_ASSIGN"
    MULT_ASSIGN = "MULT_ASSIGN"
    MOD_ASSIGN = "MOD_ASSIGN"
class BinaryOperator(Enum):
    NOT_EQUALS = "NOT_EQUALS"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    LOGICAL_NEGATION = "LOGICAL_NEGATION"
    ADDITION = "ADDITION"
    SUBSTRACTION = "SUBSTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    MODULO = "MODULO"
    LEFT_BITSHIFT = "LEFT_BITSHIFT"
    NONE = "NONE"
    EQUALS = "EQUALS"
    RIGHT_BITSHIFT = "RIGHT_BITSHIFT"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"
    BITWISE_AND = "BITWISE_AND"
    BITWISE_XOR = "BITWISE_XOR"
    BITWISE_OR = "BITWISE_OR"
    LOGICAL_AND = "LOGICAL_AND"
    LOGICAL_OR = "LOGICAL_OR"
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    BITWISE_OR_ASSIGN = "BITWISE_OR_ASSIGN"
    BITWISE_AND_ASSIGN = "BITWISE_AND_ASSIGN"
    BITWISE_XOR_ASIGN = "BITWISE_XOR_ASIGN"
    LEFT_BITSHIFT_ASSIGN = "LEFT_BITSHIFT_ASSIGN"
    RIGHT_BITSHIFT_ASSIGN = "RIGHT_BITSHIFT_ASSIGN"
    IMPLY = "IMPLY"


############################################
# Definition of Classes
############################################

class expressions_Selection:

    pass
class timedAutomata_core_TemplateInstantiation:

    pass
class timedAutomata_core_System(ABC):

    pass
class System:

    pass
class timedAutomata_core_SimpleSystem(System):

    pass
class timedAutomata_core_ComplexSystem(System):

    def __init__(self, operator: str, timedAutomata_core_ComplexSystem: "System" = None, timedAutomata_core_ComplexSystem218: "System" = None, System: "timedAutomata_core_SystemDefinition", System219: "timedAutomata_core_ComplexSystem", System216: "timedAutomata_core_ComplexSystem"):
        self.operator = operator
        self.timedAutomata_core_ComplexSystem = timedAutomata_core_ComplexSystem
        self.timedAutomata_core_ComplexSystem218 = timedAutomata_core_ComplexSystem218
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def timedAutomata_core_ComplexSystem218(self):
        return self.__timedAutomata_core_ComplexSystem218

    @timedAutomata_core_ComplexSystem218.setter
    def timedAutomata_core_ComplexSystem218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_ComplexSystem__timedAutomata_core_ComplexSystem218", None)
        self.__timedAutomata_core_ComplexSystem218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System219"):
                opp_val = getattr(old_value, "System219", None)
                if opp_val == self:
                    setattr(old_value, "System219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System219"):
                opp_val = getattr(value, "System219", None)
                setattr(value, "System219", self)

    @property
    def timedAutomata_core_ComplexSystem(self):
        return self.__timedAutomata_core_ComplexSystem

    @timedAutomata_core_ComplexSystem.setter
    def timedAutomata_core_ComplexSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_ComplexSystem__timedAutomata_core_ComplexSystem", None)
        self.__timedAutomata_core_ComplexSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System216"):
                opp_val = getattr(old_value, "System216", None)
                if opp_val == self:
                    setattr(old_value, "System216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System216"):
                opp_val = getattr(value, "System216", None)
                setattr(value, "System216", self)

class TemplateInstantiation:

    pass
class Selections:

    pass
class Guards:

    pass
class Edge:

    pass
class timedAutomata_core_SystemDefinition:

    pass
class core_timedAutomata_Label:

    pass
class base_Commentable:

    pass
class core_timedAutomata_Nail:

    pass
class Updates:

    pass
class declarations_FieldDeclaration:

    pass
class core_timedAutomata_Parameter:

    pass
class Location:

    pass
class base_Identifyable:

    pass
class base_Nameable:

    pass
class timedAutomata_core_TAElement(base_Nameable, base_Commentable):

    pass
class core_TAElement:

    pass
class timedAutomata_core_Template(base_Nameable, base_Identifyable, core_TAElement):

    pass
class SystemDefinition:

    pass
class Template:

    pass
class TAElement:

    pass
class timedAutomata_core_Project(TAElement):

    def __init__(self, id: str, timedAutomata_core_Project: set["declarations_Declaration"] = None, timedAutomata_core_Project177: set["Template"] = None, timedAutomata_core_Project179: "SystemDefinition" = None):
        self.id = id
        self.timedAutomata_core_Project = timedAutomata_core_Project if timedAutomata_core_Project is not None else set()
        self.timedAutomata_core_Project177 = timedAutomata_core_Project177 if timedAutomata_core_Project177 is not None else set()
        self.timedAutomata_core_Project179 = timedAutomata_core_Project179
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def timedAutomata_core_Project179(self):
        return self.__timedAutomata_core_Project179

    @timedAutomata_core_Project179.setter
    def timedAutomata_core_Project179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_Project__timedAutomata_core_Project179", None)
        self.__timedAutomata_core_Project179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemDefinition"):
                opp_val = getattr(old_value, "SystemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "SystemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemDefinition"):
                opp_val = getattr(value, "SystemDefinition", None)
                setattr(value, "SystemDefinition", self)

    @property
    def timedAutomata_core_Project177(self):
        return self.__timedAutomata_core_Project177

    @timedAutomata_core_Project177.setter
    def timedAutomata_core_Project177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_Project__timedAutomata_core_Project177", None)
        self.__timedAutomata_core_Project177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Template"):
                    opp_val = getattr(item, "Template", None)
                    
                    if opp_val == self:
                        setattr(item, "Template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Template"):
                    opp_val = getattr(item, "Template", None)
                    
                    setattr(item, "Template", self)
                    

    @property
    def timedAutomata_core_Project(self):
        return self.__timedAutomata_core_Project

    @timedAutomata_core_Project.setter
    def timedAutomata_core_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_Project__timedAutomata_core_Project", None)
        self.__timedAutomata_core_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "declarations_Declaration175"):
                    opp_val = getattr(item, "declarations_Declaration175", None)
                    
                    if opp_val == self:
                        setattr(item, "declarations_Declaration175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "declarations_Declaration175"):
                    opp_val = getattr(item, "declarations_Declaration175", None)
                    
                    setattr(item, "declarations_Declaration175", self)
                    

class declarations_ChannelExpression:

    pass
class ChannelPriority:

    pass
class timedAutomata_declarations_SimpleChannelPriority(ChannelPriority):

    pass
class timedAutomata_declarations_ComplexChannelPriority(ChannelPriority):

    def __init__(self, channelOperator: str, timedAutomata_declarations_ComplexChannelPriority: "declarations_ChannelExpression" = None, timedAutomata_declarations_ComplexChannelPriority155: "declarations_ChannelPriority" = None):
        self.channelOperator = channelOperator
        self.timedAutomata_declarations_ComplexChannelPriority = timedAutomata_declarations_ComplexChannelPriority
        self.timedAutomata_declarations_ComplexChannelPriority155 = timedAutomata_declarations_ComplexChannelPriority155
        
    @property
    def channelOperator(self) -> str:
        return self.__channelOperator

    @channelOperator.setter
    def channelOperator(self, channelOperator: str):
        self.__channelOperator = channelOperator

    @property
    def timedAutomata_declarations_ComplexChannelPriority155(self):
        return self.__timedAutomata_declarations_ComplexChannelPriority155

    @timedAutomata_declarations_ComplexChannelPriority155.setter
    def timedAutomata_declarations_ComplexChannelPriority155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_declarations_ComplexChannelPriority__timedAutomata_declarations_ComplexChannelPriority155", None)
        self.__timedAutomata_declarations_ComplexChannelPriority155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarations_ChannelPriority156"):
                opp_val = getattr(old_value, "declarations_ChannelPriority156", None)
                if opp_val == self:
                    setattr(old_value, "declarations_ChannelPriority156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarations_ChannelPriority156"):
                opp_val = getattr(value, "declarations_ChannelPriority156", None)
                setattr(value, "declarations_ChannelPriority156", self)

    @property
    def timedAutomata_declarations_ComplexChannelPriority(self):
        return self.__timedAutomata_declarations_ComplexChannelPriority

    @timedAutomata_declarations_ComplexChannelPriority.setter
    def timedAutomata_declarations_ComplexChannelPriority(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_declarations_ComplexChannelPriority__timedAutomata_declarations_ComplexChannelPriority", None)
        self.__timedAutomata_declarations_ComplexChannelPriority = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarations_ChannelExpression153"):
                opp_val = getattr(old_value, "declarations_ChannelExpression153", None)
                if opp_val == self:
                    setattr(old_value, "declarations_ChannelExpression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarations_ChannelExpression153"):
                opp_val = getattr(value, "declarations_ChannelExpression153", None)
                setattr(value, "declarations_ChannelExpression153", self)

class timedAutomata_declarations_DefaultChannelPriority(ChannelPriority):

    pass
class timedAutomata_declarations_ChannelPriority(ABC):

    pass
class Type:

    pass
class timedAutomata_types_SimpleType(Type):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class timedAutomata_types_Struct(Type):

    pass
class timedAutomata_types_Scalar(Type):

    pass
class timedAutomata_types_IntegerRange(Type):

    pass
class timedAutomata_types_IdentifierType(Type):

    pass
class timedAutomata_types_Type(ABC):

    def __init__(self, prefix: str):
        self.prefix = prefix
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

class ChannelExpression:

    pass
class timedAutomata_declarations_ExpressionChannelExpression(ChannelExpression):

    pass
class timedAutomata_declarations_IdentifierChannelExpression(ChannelExpression):

    pass
class timedAutomata_declarations_ChannelExpression(ABC):

    pass
class declarations_Declaration:

    pass
class timedAutomata_declarations_Block:

    pass
class TAParameter:

    pass
class timedAutomata_declarations_CallByReferenceParameter(TAParameter):

    pass
class timedAutomata_declarations_CallByValueParameter(TAParameter):

    pass
class timedAutomata_declarations_TAParameter(ABC):

    pass
class Statement:

    pass
class timedAutomata_declarations_DoWhileLoopStatement(Statement):

    pass
class timedAutomata_declarations_WhileLoopStatement(Statement):

    pass
class timedAutomata_declarations_ForLoopStatement(Statement):

    pass
class timedAutomata_declarations_IfStatement(Statement):

    pass
class timedAutomata_declarations_IterationStatement(Statement):

    pass
class timedAutomata_declarations_ReturnStatement(Statement):

    pass
class timedAutomata_declarations_ExpressionStatement(Statement):

    pass
class timedAutomata_declarations_Statement(ABC):

    pass
class declarations_Statement:

    pass
class ArrayDeclarationType:

    pass
class timedAutomata_declarations_ArrayExpressionType(ArrayDeclarationType):

    pass
class timedAutomata_declarations_ArrayDeclarationType:

    pass
class timedAutomata_declarations_ArrayDeclaration:

    pass
class Initialiser:

    pass
class timedAutomata_declarations_ArrayInitialiser(Initialiser):

    pass
class timedAutomata_declarations_ExpressionInitialiser(Initialiser):

    pass
class timedAutomata_declarations_Initialiser(ABC):

    pass
class timedAutomata_declarations_ArrayTypeType(ArrayDeclarationType):

    pass
class declarations_ArrayDeclaration:

    pass
class declarations_Initialiser:

    pass
class declarations_ArrayDeclarationType:

    pass
class timedAutomata_declarations_VariableIdentifier:

    pass
class declarations_VariableIdentifier:

    pass
class Declaration:

    pass
class timedAutomata_declarations_TypeDeclaration(Declaration):

    pass
class timedAutomata_declarations_VariableDeclaration(Declaration):

    pass
class timedAutomata_expressions_Selection:

    pass
class timedAutomata_declarations_FieldDeclaration:

    pass
class declarations_ChannelPriority:

    pass
class timedAutomata_declarations_ChannelPriorityDeclaration(Declaration):

    pass
class declarations_Block:

    pass
class timedAutomata_declarations_BlockStatement(declarations_Statement, declarations_Block):

    pass
class declarations_TAParameter:

    pass
class timedAutomata_declarations_FunctionDeclaration(Declaration):

    pass
class types_Type:

    pass
class Identifier:

    pass
class Expression:

    pass
class timedAutomata_expressions_ExistsExpression(Expression):

    pass
class timedAutomata_expressions_UnaryExpression(Expression):

    def __init__(self, operator: str, timedAutomata_expressions_UnaryExpression: "expressions_Expression" = None):
        self.operator = operator
        self.timedAutomata_expressions_UnaryExpression = timedAutomata_expressions_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def timedAutomata_expressions_UnaryExpression(self):
        return self.__timedAutomata_expressions_UnaryExpression

    @timedAutomata_expressions_UnaryExpression.setter
    def timedAutomata_expressions_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_UnaryExpression__timedAutomata_expressions_UnaryExpression", None)
        self.__timedAutomata_expressions_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression22"):
                opp_val = getattr(old_value, "expressions_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression22"):
                opp_val = getattr(value, "expressions_Expression22", None)
                setattr(value, "expressions_Expression22", self)

class timedAutomata_expressions_PointExpression(Expression):

    pass
class timedAutomata_expressions_AssignmentExpression(Expression):

    def __init__(self, operator: str, timedAutomata_expressions_AssignmentExpression: "expressions_Expression" = None, timedAutomata_expressions_AssignmentExpression19: "expressions_Expression" = None):
        self.operator = operator
        self.timedAutomata_expressions_AssignmentExpression = timedAutomata_expressions_AssignmentExpression
        self.timedAutomata_expressions_AssignmentExpression19 = timedAutomata_expressions_AssignmentExpression19
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def timedAutomata_expressions_AssignmentExpression19(self):
        return self.__timedAutomata_expressions_AssignmentExpression19

    @timedAutomata_expressions_AssignmentExpression19.setter
    def timedAutomata_expressions_AssignmentExpression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_AssignmentExpression__timedAutomata_expressions_AssignmentExpression19", None)
        self.__timedAutomata_expressions_AssignmentExpression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression20"):
                opp_val = getattr(old_value, "expressions_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression20"):
                opp_val = getattr(value, "expressions_Expression20", None)
                setattr(value, "expressions_Expression20", self)

    @property
    def timedAutomata_expressions_AssignmentExpression(self):
        return self.__timedAutomata_expressions_AssignmentExpression

    @timedAutomata_expressions_AssignmentExpression.setter
    def timedAutomata_expressions_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_AssignmentExpression__timedAutomata_expressions_AssignmentExpression", None)
        self.__timedAutomata_expressions_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression17"):
                opp_val = getattr(old_value, "expressions_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression17"):
                opp_val = getattr(value, "expressions_Expression17", None)
                setattr(value, "expressions_Expression17", self)

class timedAutomata_expressions_VariableExpression(Expression):

    pass
class timedAutomata_expressions_WithArgumentsExpression(Expression):

    pass
class timedAutomata_expressions_IncDecExpression(Expression):

    def __init__(self, beforeExpression: bool, increment: bool, timedAutomata_expressions_IncDecExpression: "expressions_Expression" = None):
        self.beforeExpression = beforeExpression
        self.increment = increment
        self.timedAutomata_expressions_IncDecExpression = timedAutomata_expressions_IncDecExpression
        
    @property
    def beforeExpression(self) -> bool:
        return self.__beforeExpression

    @beforeExpression.setter
    def beforeExpression(self, beforeExpression: bool):
        self.__beforeExpression = beforeExpression

    @property
    def increment(self) -> bool:
        return self.__increment

    @increment.setter
    def increment(self, increment: bool):
        self.__increment = increment

    @property
    def timedAutomata_expressions_IncDecExpression(self):
        return self.__timedAutomata_expressions_IncDecExpression

    @timedAutomata_expressions_IncDecExpression.setter
    def timedAutomata_expressions_IncDecExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_IncDecExpression__timedAutomata_expressions_IncDecExpression", None)
        self.__timedAutomata_expressions_IncDecExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression8"):
                opp_val = getattr(old_value, "expressions_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression8"):
                opp_val = getattr(value, "expressions_Expression8", None)
                setattr(value, "expressions_Expression8", self)

class timedAutomata_expressions_ForallExpression(Expression):

    pass
class timedAutomata_expressions_FixedExpression(Expression):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class timedAutomata_expressions_SimpleIfExpression(Expression):

    pass
class timedAutomata_expressions_ArrayVariableExpression(Expression):

    pass
class timedAutomata_expressions_IdentifierExpression(Expression):

    pass
class timedAutomata_expressions_BinaryExpression(Expression):

    def __init__(self, operator: str, timedAutomata_expressions_BinaryExpression: "expressions_Expression" = None, timedAutomata_expressions_BinaryExpression14: "expressions_Expression" = None):
        self.operator = operator
        self.timedAutomata_expressions_BinaryExpression = timedAutomata_expressions_BinaryExpression
        self.timedAutomata_expressions_BinaryExpression14 = timedAutomata_expressions_BinaryExpression14
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def timedAutomata_expressions_BinaryExpression14(self):
        return self.__timedAutomata_expressions_BinaryExpression14

    @timedAutomata_expressions_BinaryExpression14.setter
    def timedAutomata_expressions_BinaryExpression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_BinaryExpression__timedAutomata_expressions_BinaryExpression14", None)
        self.__timedAutomata_expressions_BinaryExpression14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression15"):
                opp_val = getattr(old_value, "expressions_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression15"):
                opp_val = getattr(value, "expressions_Expression15", None)
                setattr(value, "expressions_Expression15", self)

    @property
    def timedAutomata_expressions_BinaryExpression(self):
        return self.__timedAutomata_expressions_BinaryExpression

    @timedAutomata_expressions_BinaryExpression.setter
    def timedAutomata_expressions_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_expressions_BinaryExpression__timedAutomata_expressions_BinaryExpression", None)
        self.__timedAutomata_expressions_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression12"):
                opp_val = getattr(old_value, "expressions_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression12"):
                opp_val = getattr(value, "expressions_Expression12", None)
                setattr(value, "expressions_Expression12", self)

class timedAutomata_expressions_GroupingExpression(Expression):

    pass
class timedAutomata_expressions_ConstantExpression(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Commentable:

    pass
class timedAutomata_declarations_Declaration(Commentable):

    pass
class timedAutomata_expressions_Expression(Commentable):

    pass
class Position:

    pass
class timedAutomata_core_Edge(Position, core_TAElement):

    pass
class timedAutomata_core_Selections(Position):

    pass
class timedAutomata_core_Updates(Position):

    pass
class timedAutomata_core_Guards(Position):

    pass
class timedAutomata_core_Location(Position, core_TAElement):

    def __init__(self, urgent: str, committed: str, timedAutomata_core_Location: "expressions_Expression" = None, timedAutomata_core_Location209: "core_timedAutomata_Label" = None):
        self.urgent = urgent
        self.committed = committed
        self.timedAutomata_core_Location = timedAutomata_core_Location
        self.timedAutomata_core_Location209 = timedAutomata_core_Location209
        
    @property
    def urgent(self) -> str:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: str):
        self.__urgent = urgent

    @property
    def committed(self) -> str:
        return self.__committed

    @committed.setter
    def committed(self, committed: str):
        self.__committed = committed

    @property
    def timedAutomata_core_Location(self):
        return self.__timedAutomata_core_Location

    @timedAutomata_core_Location.setter
    def timedAutomata_core_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_Location__timedAutomata_core_Location", None)
        self.__timedAutomata_core_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression207"):
                opp_val = getattr(old_value, "expressions_Expression207", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression207"):
                opp_val = getattr(value, "expressions_Expression207", None)
                setattr(value, "expressions_Expression207", self)

    @property
    def timedAutomata_core_Location209(self):
        return self.__timedAutomata_core_Location209

    @timedAutomata_core_Location209.setter
    def timedAutomata_core_Location209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timedAutomata_core_Location__timedAutomata_core_Location209", None)
        self.__timedAutomata_core_Location209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_timedAutomata_Label"):
                opp_val = getattr(old_value, "core_timedAutomata_Label", None)
                if opp_val == self:
                    setattr(old_value, "core_timedAutomata_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_timedAutomata_Label"):
                opp_val = getattr(value, "core_timedAutomata_Label", None)
                setattr(value, "core_timedAutomata_Label", self)

class timedAutomata_bnf_Synchronisation(Position):

    pass
class timedAutomata_bnf_Identifier:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class timedAutomata_base_Nameable:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Synchronisation:

    pass
class timedAutomata_bnf_ReceiveSynchronisation(Synchronisation):

    pass
class timedAutomata_bnf_SendSynchronisation(Synchronisation):

    pass
class expressions_Expression:

    pass
class timedAutomata_base_Identifyable:

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class timedAutomata_base_Commentable(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment
