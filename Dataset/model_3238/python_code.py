from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperation(Enum):
    ASSIGN_SUB = "ASSIGN_SUB"
    ASSIGN_MUL = "ASSIGN_MUL"
    ASSIGN_DIV = "ASSIGN_DIV"
    ASSIGN_MOD = "ASSIGN_MOD"
    DIFF = "DIFF"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    MOD = "MOD"
    LT = "LT"
    LE = "LE"
    EQ = "EQ"
    GE = "GE"
    GT = "GT"
    NE = "NE"
    AND = "AND"
    OR = "OR"
    ASSIGN = "ASSIGN"
    ASSIGN_ADD = "ASSIGN_ADD"
class UnaryOperation(Enum):
    NOT = "NOT"
    PLUS = "PLUS"
    MINUS = "MINUS"
class ResolvedType(Enum):
    integer = "integer"
    boolean = "boolean"
    natural = "natural"
    clock = "clock"
    float = "float"
    resource = "resource"
    unknown = "unknown"
class TernaryOperation(Enum):
    QUESTION = "QUESTION"


############################################
# Definition of Classes
############################################

class expressions_type_Type(ABC):

    def __init__(self):
        
    def getPrimitiveTypeIndex(self) -> int:
        # TODO: Implement getPrimitiveTypeIndex method
        pass

    def add(self, rightArgument: str) -> str:
        # TODO: Implement add method
        pass

class BaseType:

    pass
class expressions_type_BooleanType(BaseType):

    pass
class expressions_type_NaturalType(BaseType):

    pass
class expressions_type_ClockType(BaseType):

    pass
class expressions_type_ResourceType(BaseType):

    pass
class expressions_type_FloatType(BaseType):

    pass
class expressions_type_AnyType(BaseType):

    pass
class expressions_type_IntegerType(BaseType):

    pass
class Type:

    pass
class expressions_type_BaseType(Type):

    pass
class expressions_ast_AstVisitor(ABC):

    def __init__(self):
        
    def visitUnaryExpression(self, node: str):
        # TODO: Implement visitUnaryExpression method
        pass

    def visitConstant(self, node: str):
        # TODO: Implement visitConstant method
        pass

    def visitTernaryExpression(self, node: str):
        # TODO: Implement visitTernaryExpression method
        pass

    def visitLiteral(self, node: str):
        # TODO: Implement visitLiteral method
        pass

    def visitBinaryExpression(self, node: str):
        # TODO: Implement visitBinaryExpression method
        pass

    def visitVariableReference(self, node: str):
        # TODO: Implement visitVariableReference method
        pass

class ast_expressions_EObject:

    pass
class Expression:

    pass
class expressions_ast_UnaryExpression(Expression):

    def __init__(self, operation: str, expressions_ast_UnaryExpression: "Expression" = None, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.operation = operation
        self.expressions_ast_UnaryExpression = expressions_ast_UnaryExpression
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def expressions_ast_UnaryExpression(self):
        return self.__expressions_ast_UnaryExpression

    @expressions_ast_UnaryExpression.setter
    def expressions_ast_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_UnaryExpression__expressions_ast_UnaryExpression", None)
        self.__expressions_ast_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression20"):
                opp_val = getattr(old_value, "Expression20", None)
                if opp_val == self:
                    setattr(old_value, "Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression20"):
                opp_val = getattr(value, "Expression20", None)
                setattr(value, "Expression20", self)

class expressions_ast_Constant(Expression):

    def __init__(self, value: str, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_ast_BinaryExpression(Expression):

    def __init__(self, operation: str, expressions_ast_BinaryExpression: "Expression" = None, expressions_ast_BinaryExpression17: "Expression" = None, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.operation = operation
        self.expressions_ast_BinaryExpression = expressions_ast_BinaryExpression
        self.expressions_ast_BinaryExpression17 = expressions_ast_BinaryExpression17
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def expressions_ast_BinaryExpression17(self):
        return self.__expressions_ast_BinaryExpression17

    @expressions_ast_BinaryExpression17.setter
    def expressions_ast_BinaryExpression17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_BinaryExpression__expressions_ast_BinaryExpression17", None)
        self.__expressions_ast_BinaryExpression17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression18"):
                opp_val = getattr(old_value, "Expression18", None)
                if opp_val == self:
                    setattr(old_value, "Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression18"):
                opp_val = getattr(value, "Expression18", None)
                setattr(value, "Expression18", self)

    @property
    def expressions_ast_BinaryExpression(self):
        return self.__expressions_ast_BinaryExpression

    @expressions_ast_BinaryExpression.setter
    def expressions_ast_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_BinaryExpression__expressions_ast_BinaryExpression", None)
        self.__expressions_ast_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression15"):
                opp_val = getattr(old_value, "Expression15", None)
                if opp_val == self:
                    setattr(old_value, "Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression15"):
                opp_val = getattr(value, "Expression15", None)
                setattr(value, "Expression15", self)

class expressions_ast_Literal(Expression):

    def __init__(self, value: str, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_ast_VariableReference(Expression):

    def __init__(self, name: str, expressions_ast_VariableReference24: "ast_expressions_EObject" = None, expressions_ast_VariableReference: "Expression" = None, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.name = name
        self.expressions_ast_VariableReference24 = expressions_ast_VariableReference24
        self.expressions_ast_VariableReference = expressions_ast_VariableReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_ast_VariableReference24(self):
        return self.__expressions_ast_VariableReference24

    @expressions_ast_VariableReference24.setter
    def expressions_ast_VariableReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_VariableReference__expressions_ast_VariableReference24", None)
        self.__expressions_ast_VariableReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_expressions_EObject"):
                opp_val = getattr(old_value, "ast_expressions_EObject", None)
                if opp_val == self:
                    setattr(old_value, "ast_expressions_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_expressions_EObject"):
                opp_val = getattr(value, "ast_expressions_EObject", None)
                setattr(value, "ast_expressions_EObject", self)

    @property
    def expressions_ast_VariableReference(self):
        return self.__expressions_ast_VariableReference

    @expressions_ast_VariableReference.setter
    def expressions_ast_VariableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_VariableReference__expressions_ast_VariableReference", None)
        self.__expressions_ast_VariableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression22"):
                opp_val = getattr(old_value, "Expression22", None)
                if opp_val == self:
                    setattr(old_value, "Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression22"):
                opp_val = getattr(value, "Expression22", None)
                setattr(value, "Expression22", self)

class AbstractRoot:

    pass
class expressions_ast_ActionRoot(AbstractRoot):

    pass
class VariableReference:

    pass
class expressions_ast_TernaryExpression(Expression):

    def __init__(self, operation: str, expressions_ast_TernaryExpression: "Expression" = None, expressions_ast_TernaryExpression9: "Expression" = None, expressions_ast_TernaryExpression12: "Expression" = None, Expression22: "expressions_ast_VariableReference", Expression: "expressions_ast_ActionRoot", Expression3: "expressions_ast_LogicalRoot", Expression7: "expressions_ast_TernaryExpression", Expression13: "expressions_ast_TernaryExpression", Expression10: "expressions_ast_TernaryExpression", Expression18: "expressions_ast_BinaryExpression", Expression15: "expressions_ast_BinaryExpression", Expression20: "expressions_ast_UnaryExpression", Expression5: "expressions_ast_ResourceRoot"):
        self.operation = operation
        self.expressions_ast_TernaryExpression = expressions_ast_TernaryExpression
        self.expressions_ast_TernaryExpression9 = expressions_ast_TernaryExpression9
        self.expressions_ast_TernaryExpression12 = expressions_ast_TernaryExpression12
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def expressions_ast_TernaryExpression12(self):
        return self.__expressions_ast_TernaryExpression12

    @expressions_ast_TernaryExpression12.setter
    def expressions_ast_TernaryExpression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_TernaryExpression__expressions_ast_TernaryExpression12", None)
        self.__expressions_ast_TernaryExpression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression13"):
                opp_val = getattr(old_value, "Expression13", None)
                if opp_val == self:
                    setattr(old_value, "Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression13"):
                opp_val = getattr(value, "Expression13", None)
                setattr(value, "Expression13", self)

    @property
    def expressions_ast_TernaryExpression(self):
        return self.__expressions_ast_TernaryExpression

    @expressions_ast_TernaryExpression.setter
    def expressions_ast_TernaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_TernaryExpression__expressions_ast_TernaryExpression", None)
        self.__expressions_ast_TernaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression7"):
                opp_val = getattr(old_value, "Expression7", None)
                if opp_val == self:
                    setattr(old_value, "Expression7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression7"):
                opp_val = getattr(value, "Expression7", None)
                setattr(value, "Expression7", self)

    @property
    def expressions_ast_TernaryExpression9(self):
        return self.__expressions_ast_TernaryExpression9

    @expressions_ast_TernaryExpression9.setter
    def expressions_ast_TernaryExpression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_TernaryExpression__expressions_ast_TernaryExpression9", None)
        self.__expressions_ast_TernaryExpression9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression10"):
                opp_val = getattr(old_value, "Expression10", None)
                if opp_val == self:
                    setattr(old_value, "Expression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression10"):
                opp_val = getattr(value, "Expression10", None)
                setattr(value, "Expression10", self)

class expressions_ast_Expression(ABC):

    def __init__(self, type: str, text: str):
        self.type = type
        self.text = text
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    def visit(self, visitor: str):
        # TODO: Implement visit method
        pass

class expressions_ast_ResourceRoot(AbstractRoot):

    pass
class expressions_ast_LogicalRoot(AbstractRoot):

    pass
class expressions_ast_AbstractRoot(ABC):

    def __init__(self, type: str, expressions_ast_AbstractRoot: set["VariableReference"] = None):
        self.type = type
        self.expressions_ast_AbstractRoot = expressions_ast_AbstractRoot if expressions_ast_AbstractRoot is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressions_ast_AbstractRoot(self):
        return self.__expressions_ast_AbstractRoot

    @expressions_ast_AbstractRoot.setter
    def expressions_ast_AbstractRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ast_AbstractRoot__expressions_ast_AbstractRoot", None)
        self.__expressions_ast_AbstractRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableReference"):
                    opp_val = getattr(item, "VariableReference", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableReference"):
                    opp_val = getattr(item, "VariableReference", None)
                    
                    setattr(item, "VariableReference", self)
                    
