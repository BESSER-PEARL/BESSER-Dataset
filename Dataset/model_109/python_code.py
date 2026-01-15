from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Modifiers(Enum):
    enum = "enum"
    final = "final"
    interface = "interface"
    native = "native"
    private = "private"
    protected = "protected"
    public = "public"
    static = "static"
    strictfp = "strictfp"
    super = "super"
    synchronized = "synchronized"
    synthetic = "synthetic"
    transient = "transient"
    varargs = "varargs"
    volatile = "volatile"
    abstract = "abstract"
    annotation = "annotation"
    bridge = "bridge"
    default = "default"
    deprecated = "deprecated"
class PrefixExpressionOperatorKind(Enum):
    minus = "minus"
    not = "not"
    decrement = "decrement"
    complement = "complement"
    increment = "increment"
    plus = "plus"
class InfixExpressionOperatorKind(Enum):
    less_equals = "less_equals"
    equals = "equals"
    not_equals = "not_equals"
    and = "and"
    plus = "plus"
    greater = "greater"
    conditional_or = "conditional_or"
    remainder = "remainder"
    less = "less"
    left_shift = "left_shift"
    right_shift_unsigned = "right_shift_unsigned"
    conditional_and = "conditional_and"
    times = "times"
    divide = "divide"
    greater_equals = "greater_equals"
    or = "or"
    right_shift_signed = "right_shift_signed"
    minus = "minus"
    xor = "xor"
class PostfixExpressionOperatorKind(Enum):
    increment = "increment"
    decrement = "decrement"
class AssignmentOperatorKind(Enum):
    right_shift_signed_assign = "right_shift_signed_assign"
    bit_xor_assign = "bit_xor_assign"
    times_assign = "times_assign"
    divide_assign = "divide_assign"
    minus_assign = "minus_assign"
    bit_or_assign = "bit_or_assign"
    plus_assign = "plus_assign"
    assign = "assign"
    right_shift_unsigned_assign = "right_shift_unsigned_assign"
    remainder_assign = "remainder_assign"
    bit_and_assign = "bit_and_assign"
    left_shift_assign = "left_shift_assign"


############################################
# Definition of Classes
############################################

class Annotation:

    pass
class JDTAST_NormalAnnotation(Annotation):

    pass
class JDTAST_SingleMemberAnnotation(Annotation):

    pass
class JDTAST_MarkerAnnotation(Annotation):

    pass
class VariableDeclaration:

    pass
class Name:

    pass
class JDTAST_QualifiedName(Name):

    pass
class Type:

    pass
class JDTAST_WildcardType(Type):

    def __init__(self, upperBound: str, JDTAST_WildcardType: "JDTAST_Type" = None):
        self.upperBound = upperBound
        self.JDTAST_WildcardType = JDTAST_WildcardType
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def JDTAST_WildcardType(self):
        return self.__JDTAST_WildcardType

    @JDTAST_WildcardType.setter
    def JDTAST_WildcardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_WildcardType__JDTAST_WildcardType", None)
        self.__JDTAST_WildcardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type419"):
                opp_val = getattr(old_value, "JDTAST_Type419", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type419"):
                opp_val = getattr(value, "JDTAST_Type419", None)
                setattr(value, "JDTAST_Type419", self)

class JDTAST_QualifiedType(Type):

    pass
class JDTAST_SimpleType(Type):

    pass
class JDTAST_PrimitiveType(Type):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class JDTAST_ParameterizedType(Type):

    pass
class Statement:

    pass
class JDTAST_IfStatement(Statement):

    pass
class JDTAST_SynchronizedStatement(Statement):

    pass
class JDTAST_SuperConstructorInvocation(Statement):

    pass
class JDTAST_SwitchCase(Statement):

    def __init__(self, default: str, JDTAST_SwitchCase: "JDTAST_Expression" = None):
        self.default = default
        self.JDTAST_SwitchCase = JDTAST_SwitchCase
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def JDTAST_SwitchCase(self):
        return self.__JDTAST_SwitchCase

    @JDTAST_SwitchCase.setter
    def JDTAST_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SwitchCase__JDTAST_SwitchCase", None)
        self.__JDTAST_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression364"):
                opp_val = getattr(old_value, "JDTAST_Expression364", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression364"):
                opp_val = getattr(value, "JDTAST_Expression364", None)
                setattr(value, "JDTAST_Expression364", self)

class JDTAST_ConstructorInvocation(Statement):

    pass
class JDTAST_ReturnStatement(Statement):

    pass
class JDTAST_DoStatement(Statement):

    pass
class JDTAST_EmptyStatement(Statement):

    pass
class JDTAST_SwitchStatement(Statement):

    pass
class JDTAST_ThrowStatement(Statement):

    pass
class JDTAST_TryStatement(Statement):

    pass
class JDTAST_ForStatement(Statement):

    pass
class JDTAST_ContinueStatement(Statement):

    pass
class JDTAST_ExpressionStatement(Statement):

    pass
class JDTAST_LabeledStatement(Statement):

    pass
class JDTAST_EnhancedForStatement(Statement):

    pass
class JDTAST_WhileStatement(Statement):

    pass
class JDTAST_VariableDeclarationStatement(Statement):

    pass
class JDTAST_TypeDeclarationStatement(Statement):

    pass
class JDTAST_AssertStatement(Statement):

    pass
class JDTAST_BreakStatement(Statement):

    pass
class Expression:

    pass
class JDTAST_Assignment(Expression):

    def __init__(self, operator: str, JDTAST_Assignment: "JDTAST_Expression" = None, JDTAST_Assignment203: "JDTAST_Expression" = None):
        self.operator = operator
        self.JDTAST_Assignment = JDTAST_Assignment
        self.JDTAST_Assignment203 = JDTAST_Assignment203
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JDTAST_Assignment(self):
        return self.__JDTAST_Assignment

    @JDTAST_Assignment.setter
    def JDTAST_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Assignment__JDTAST_Assignment", None)
        self.__JDTAST_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression201"):
                opp_val = getattr(old_value, "JDTAST_Expression201", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression201"):
                opp_val = getattr(value, "JDTAST_Expression201", None)
                setattr(value, "JDTAST_Expression201", self)

    @property
    def JDTAST_Assignment203(self):
        return self.__JDTAST_Assignment203

    @JDTAST_Assignment203.setter
    def JDTAST_Assignment203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Assignment__JDTAST_Assignment203", None)
        self.__JDTAST_Assignment203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression204"):
                opp_val = getattr(old_value, "JDTAST_Expression204", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression204"):
                opp_val = getattr(value, "JDTAST_Expression204", None)
                setattr(value, "JDTAST_Expression204", self)

class JDTAST_PostfixExpression(Expression):

    def __init__(self, operator: str, JDTAST_PostfixExpression: "JDTAST_Expression" = None):
        self.operator = operator
        self.JDTAST_PostfixExpression = JDTAST_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JDTAST_PostfixExpression(self):
        return self.__JDTAST_PostfixExpression

    @JDTAST_PostfixExpression.setter
    def JDTAST_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_PostfixExpression__JDTAST_PostfixExpression", None)
        self.__JDTAST_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression267"):
                opp_val = getattr(old_value, "JDTAST_Expression267", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression267"):
                opp_val = getattr(value, "JDTAST_Expression267", None)
                setattr(value, "JDTAST_Expression267", self)

class JDTAST_NumberLiteral(Expression):

    def __init__(self, token: str):
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

class JDTAST_ParenthesizedExpression(Expression):

    pass
class JDTAST_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> str:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue

class JDTAST_ClassInstanceCreation(Expression):

    pass
class JDTAST_TypeLiteral(Expression):

    pass
class JDTAST_FieldAccess(Expression):

    pass
class JDTAST_PrefixExpression(Expression):

    def __init__(self, operator: str, JDTAST_PrefixExpression: "JDTAST_Expression" = None):
        self.operator = operator
        self.JDTAST_PrefixExpression = JDTAST_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JDTAST_PrefixExpression(self):
        return self.__JDTAST_PrefixExpression

    @JDTAST_PrefixExpression.setter
    def JDTAST_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_PrefixExpression__JDTAST_PrefixExpression", None)
        self.__JDTAST_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression269"):
                opp_val = getattr(old_value, "JDTAST_Expression269", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression269"):
                opp_val = getattr(value, "JDTAST_Expression269", None)
                setattr(value, "JDTAST_Expression269", self)

class JDTAST_InfixExpression(Expression):

    def __init__(self, operator: str, JDTAST_InfixExpression: set["JDTAST_Expression"] = None, JDTAST_InfixExpression240: "JDTAST_Expression" = None, JDTAST_InfixExpression243: "JDTAST_Expression" = None):
        self.operator = operator
        self.JDTAST_InfixExpression = JDTAST_InfixExpression if JDTAST_InfixExpression is not None else set()
        self.JDTAST_InfixExpression240 = JDTAST_InfixExpression240
        self.JDTAST_InfixExpression243 = JDTAST_InfixExpression243
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JDTAST_InfixExpression(self):
        return self.__JDTAST_InfixExpression

    @JDTAST_InfixExpression.setter
    def JDTAST_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_InfixExpression__JDTAST_InfixExpression", None)
        self.__JDTAST_InfixExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_Expression238"):
                    opp_val = getattr(item, "JDTAST_Expression238", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_Expression238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_Expression238"):
                    opp_val = getattr(item, "JDTAST_Expression238", None)
                    
                    setattr(item, "JDTAST_Expression238", self)
                    

    @property
    def JDTAST_InfixExpression240(self):
        return self.__JDTAST_InfixExpression240

    @JDTAST_InfixExpression240.setter
    def JDTAST_InfixExpression240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_InfixExpression__JDTAST_InfixExpression240", None)
        self.__JDTAST_InfixExpression240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression241"):
                opp_val = getattr(old_value, "JDTAST_Expression241", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression241"):
                opp_val = getattr(value, "JDTAST_Expression241", None)
                setattr(value, "JDTAST_Expression241", self)

    @property
    def JDTAST_InfixExpression243(self):
        return self.__JDTAST_InfixExpression243

    @JDTAST_InfixExpression243.setter
    def JDTAST_InfixExpression243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_InfixExpression__JDTAST_InfixExpression243", None)
        self.__JDTAST_InfixExpression243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression244"):
                opp_val = getattr(old_value, "JDTAST_Expression244", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression244"):
                opp_val = getattr(value, "JDTAST_Expression244", None)
                setattr(value, "JDTAST_Expression244", self)

class JDTAST_ArrayAccess(Expression):

    pass
class JDTAST_VariableDeclarationExpression(Expression):

    pass
class JDTAST_ConditionalExpression(Expression):

    pass
class JDTAST_NullLiteral(Expression):

    pass
class JDTAST_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str, charValue: str):
        self.escapedValue = escapedValue
        self.charValue = charValue
        
    @property
    def charValue(self) -> str:
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class JDTAST_InstanceofExpression(Expression):

    pass
class JDTAST_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str):
        self.escapedValue = escapedValue
        self.literalValue = literalValue
        
    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class JDTAST_SuperMethodInvocation(Expression):

    pass
class JDTAST_SuperFieldAccess(Expression):

    pass
class JDTAST_CastExpression(Expression):

    pass
class JDTAST_ThisExpression(Expression):

    pass
class JDTAST_MethodInvocation(Expression):

    pass
class JDTAST_ArrayType(Type):

    def __init__(self, dimensions: str, JDTAST_ArrayType: "JDTAST_ArrayCreation" = None, JDTAST_ArrayType401: "JDTAST_Type" = None, JDTAST_ArrayType404: "JDTAST_Type" = None):
        self.dimensions = dimensions
        self.JDTAST_ArrayType = JDTAST_ArrayType
        self.JDTAST_ArrayType401 = JDTAST_ArrayType401
        self.JDTAST_ArrayType404 = JDTAST_ArrayType404
        
    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def JDTAST_ArrayType(self):
        return self.__JDTAST_ArrayType

    @JDTAST_ArrayType.setter
    def JDTAST_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ArrayType__JDTAST_ArrayType", None)
        self.__JDTAST_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ArrayCreation196"):
                opp_val = getattr(old_value, "JDTAST_ArrayCreation196", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ArrayCreation196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ArrayCreation196"):
                opp_val = getattr(value, "JDTAST_ArrayCreation196", None)
                setattr(value, "JDTAST_ArrayCreation196", self)

    @property
    def JDTAST_ArrayType404(self):
        return self.__JDTAST_ArrayType404

    @JDTAST_ArrayType404.setter
    def JDTAST_ArrayType404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ArrayType__JDTAST_ArrayType404", None)
        self.__JDTAST_ArrayType404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type405"):
                opp_val = getattr(old_value, "JDTAST_Type405", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type405"):
                opp_val = getattr(value, "JDTAST_Type405", None)
                setattr(value, "JDTAST_Type405", self)

    @property
    def JDTAST_ArrayType401(self):
        return self.__JDTAST_ArrayType401

    @JDTAST_ArrayType401.setter
    def JDTAST_ArrayType401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ArrayType__JDTAST_ArrayType401", None)
        self.__JDTAST_ArrayType401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type402"):
                opp_val = getattr(old_value, "JDTAST_Type402", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type402"):
                opp_val = getattr(value, "JDTAST_Type402", None)
                setattr(value, "JDTAST_Type402", self)

class JDTAST_ArrayInitializer(Expression):

    pass
class JDTAST_ArrayCreation(Expression):

    pass
class Comment:

    pass
class JDTAST_LineComment(Comment):

    pass
class JDTAST_BlockComment(Comment):

    pass
class AbstractTypeDeclaration:

    pass
class JDTAST_EnumDeclaration(AbstractTypeDeclaration):

    pass
class JDTAST_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, JDTAST_TypeDeclaration: "JDTAST_Type" = None, JDTAST_TypeDeclaration175: set["JDTAST_Type"] = None, JDTAST_TypeDeclaration178: set["JDTAST_TypeParameter"] = None):
        self.interface = interface
        self.JDTAST_TypeDeclaration = JDTAST_TypeDeclaration
        self.JDTAST_TypeDeclaration175 = JDTAST_TypeDeclaration175 if JDTAST_TypeDeclaration175 is not None else set()
        self.JDTAST_TypeDeclaration178 = JDTAST_TypeDeclaration178 if JDTAST_TypeDeclaration178 is not None else set()
        
    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def JDTAST_TypeDeclaration178(self):
        return self.__JDTAST_TypeDeclaration178

    @JDTAST_TypeDeclaration178.setter
    def JDTAST_TypeDeclaration178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_TypeDeclaration__JDTAST_TypeDeclaration178", None)
        self.__JDTAST_TypeDeclaration178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_TypeParameter179"):
                    opp_val = getattr(item, "JDTAST_TypeParameter179", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_TypeParameter179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_TypeParameter179"):
                    opp_val = getattr(item, "JDTAST_TypeParameter179", None)
                    
                    setattr(item, "JDTAST_TypeParameter179", self)
                    

    @property
    def JDTAST_TypeDeclaration(self):
        return self.__JDTAST_TypeDeclaration

    @JDTAST_TypeDeclaration.setter
    def JDTAST_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_TypeDeclaration__JDTAST_TypeDeclaration", None)
        self.__JDTAST_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type173"):
                opp_val = getattr(old_value, "JDTAST_Type173", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type173"):
                opp_val = getattr(value, "JDTAST_Type173", None)
                setattr(value, "JDTAST_Type173", self)

    @property
    def JDTAST_TypeDeclaration175(self):
        return self.__JDTAST_TypeDeclaration175

    @JDTAST_TypeDeclaration175.setter
    def JDTAST_TypeDeclaration175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_TypeDeclaration__JDTAST_TypeDeclaration175", None)
        self.__JDTAST_TypeDeclaration175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_Type176"):
                    opp_val = getattr(item, "JDTAST_Type176", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_Type176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_Type176"):
                    opp_val = getattr(item, "JDTAST_Type176", None)
                    
                    setattr(item, "JDTAST_Type176", self)
                    

class JDTAST_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class JDTAST_VariableDeclarationFragment(VariableDeclaration):

    pass
class BodyDeclaration:

    pass
class JDTAST_Initializer(BodyDeclaration):

    pass
class JDTAST_EnumConstantDeclaration(BodyDeclaration):

    pass
class JDTAST_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class JDTAST_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, JDTAST_MethodDeclaration: "JDTAST_Block" = None, JDTAST_MethodDeclaration150: "JDTAST_SimpleName" = None, JDTAST_MethodDeclaration153: "JDTAST_Type" = None, JDTAST_MethodDeclaration159: set["JDTAST_Name"] = None, JDTAST_MethodDeclaration162: set["JDTAST_TypeParameter"] = None, JDTAST_MethodDeclaration165: "JDTAST_IMethod" = None, JDTAST_MethodDeclaration156: set["JDTAST_SingleVariableDeclaration"] = None):
        self.extraDimensions = extraDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.JDTAST_MethodDeclaration = JDTAST_MethodDeclaration
        self.JDTAST_MethodDeclaration150 = JDTAST_MethodDeclaration150
        self.JDTAST_MethodDeclaration153 = JDTAST_MethodDeclaration153
        self.JDTAST_MethodDeclaration159 = JDTAST_MethodDeclaration159 if JDTAST_MethodDeclaration159 is not None else set()
        self.JDTAST_MethodDeclaration162 = JDTAST_MethodDeclaration162 if JDTAST_MethodDeclaration162 is not None else set()
        self.JDTAST_MethodDeclaration165 = JDTAST_MethodDeclaration165
        self.JDTAST_MethodDeclaration156 = JDTAST_MethodDeclaration156 if JDTAST_MethodDeclaration156 is not None else set()
        
    @property
    def extraDimensions(self) -> str:
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions

    @property
    def constructor(self) -> str:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor

    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def JDTAST_MethodDeclaration150(self):
        return self.__JDTAST_MethodDeclaration150

    @JDTAST_MethodDeclaration150.setter
    def JDTAST_MethodDeclaration150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration150", None)
        self.__JDTAST_MethodDeclaration150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SimpleName151"):
                opp_val = getattr(old_value, "JDTAST_SimpleName151", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SimpleName151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SimpleName151"):
                opp_val = getattr(value, "JDTAST_SimpleName151", None)
                setattr(value, "JDTAST_SimpleName151", self)

    @property
    def JDTAST_MethodDeclaration159(self):
        return self.__JDTAST_MethodDeclaration159

    @JDTAST_MethodDeclaration159.setter
    def JDTAST_MethodDeclaration159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration159", None)
        self.__JDTAST_MethodDeclaration159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_Name160"):
                    opp_val = getattr(item, "JDTAST_Name160", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_Name160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_Name160"):
                    opp_val = getattr(item, "JDTAST_Name160", None)
                    
                    setattr(item, "JDTAST_Name160", self)
                    

    @property
    def JDTAST_MethodDeclaration(self):
        return self.__JDTAST_MethodDeclaration

    @JDTAST_MethodDeclaration.setter
    def JDTAST_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration", None)
        self.__JDTAST_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Block148"):
                opp_val = getattr(old_value, "JDTAST_Block148", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Block148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Block148"):
                opp_val = getattr(value, "JDTAST_Block148", None)
                setattr(value, "JDTAST_Block148", self)

    @property
    def JDTAST_MethodDeclaration153(self):
        return self.__JDTAST_MethodDeclaration153

    @JDTAST_MethodDeclaration153.setter
    def JDTAST_MethodDeclaration153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration153", None)
        self.__JDTAST_MethodDeclaration153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type154"):
                opp_val = getattr(old_value, "JDTAST_Type154", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type154"):
                opp_val = getattr(value, "JDTAST_Type154", None)
                setattr(value, "JDTAST_Type154", self)

    @property
    def JDTAST_MethodDeclaration156(self):
        return self.__JDTAST_MethodDeclaration156

    @JDTAST_MethodDeclaration156.setter
    def JDTAST_MethodDeclaration156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration156", None)
        self.__JDTAST_MethodDeclaration156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_SingleVariableDeclaration157"):
                    opp_val = getattr(item, "JDTAST_SingleVariableDeclaration157", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_SingleVariableDeclaration157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_SingleVariableDeclaration157"):
                    opp_val = getattr(item, "JDTAST_SingleVariableDeclaration157", None)
                    
                    setattr(item, "JDTAST_SingleVariableDeclaration157", self)
                    

    @property
    def JDTAST_MethodDeclaration165(self):
        return self.__JDTAST_MethodDeclaration165

    @JDTAST_MethodDeclaration165.setter
    def JDTAST_MethodDeclaration165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration165", None)
        self.__JDTAST_MethodDeclaration165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IMethod166"):
                opp_val = getattr(old_value, "JDTAST_IMethod166", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IMethod166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IMethod166"):
                opp_val = getattr(value, "JDTAST_IMethod166", None)
                setattr(value, "JDTAST_IMethod166", self)

    @property
    def JDTAST_MethodDeclaration162(self):
        return self.__JDTAST_MethodDeclaration162

    @JDTAST_MethodDeclaration162.setter
    def JDTAST_MethodDeclaration162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodDeclaration__JDTAST_MethodDeclaration162", None)
        self.__JDTAST_MethodDeclaration162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_TypeParameter163"):
                    opp_val = getattr(item, "JDTAST_TypeParameter163", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_TypeParameter163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_TypeParameter163"):
                    opp_val = getattr(item, "JDTAST_TypeParameter163", None)
                    
                    setattr(item, "JDTAST_TypeParameter163", self)
                    

class JDTAST_FieldDeclaration(BodyDeclaration):

    pass
class ExtendedModifier:

    pass
class JDTAST_Annotation(Expression, ExtendedModifier):

    pass
class JDTAST_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, JDTAST_SimpleName: "JDTAST_MemberRef" = None, JDTAST_SimpleName85: "JDTAST_MethodRef" = None, JDTAST_SimpleName93: "JDTAST_MethodRefParameter" = None, JDTAST_SimpleName80: "JDTAST_MemberValuePair" = None, JDTAST_SimpleName110: "JDTAST_TypeParameter" = None, JDTAST_SimpleName124: "JDTAST_AbstractTypeDeclaration" = None, JDTAST_SimpleName118: "JDTAST_VariableDeclaration" = None, JDTAST_SimpleName140: "JDTAST_EnumConstantDeclaration" = None, JDTAST_SimpleName129: "JDTAST_AnnotationTypeMemberDeclaration" = None, JDTAST_SimpleName151: "JDTAST_MethodDeclaration" = None, JDTAST_SimpleName236: "JDTAST_FieldAccess" = None, JDTAST_SimpleName257: "JDTAST_MethodInvocation" = None, JDTAST_SimpleName271: "JDTAST_SuperFieldAccess" = None, JDTAST_SimpleName306: "JDTAST_BreakStatement" = None, JDTAST_SimpleName313: "JDTAST_ContinueStatement" = None, JDTAST_SimpleName352: "JDTAST_LabeledStatement" = None, JDTAST_SimpleName412: "JDTAST_QualifiedType" = None, JDTAST_SimpleName427: "JDTAST_QualifiedName" = None):
        self.identifier = identifier
        self.declaration = declaration
        self.JDTAST_SimpleName = JDTAST_SimpleName
        self.JDTAST_SimpleName85 = JDTAST_SimpleName85
        self.JDTAST_SimpleName93 = JDTAST_SimpleName93
        self.JDTAST_SimpleName80 = JDTAST_SimpleName80
        self.JDTAST_SimpleName110 = JDTAST_SimpleName110
        self.JDTAST_SimpleName124 = JDTAST_SimpleName124
        self.JDTAST_SimpleName118 = JDTAST_SimpleName118
        self.JDTAST_SimpleName140 = JDTAST_SimpleName140
        self.JDTAST_SimpleName129 = JDTAST_SimpleName129
        self.JDTAST_SimpleName151 = JDTAST_SimpleName151
        self.JDTAST_SimpleName236 = JDTAST_SimpleName236
        self.JDTAST_SimpleName257 = JDTAST_SimpleName257
        self.JDTAST_SimpleName271 = JDTAST_SimpleName271
        self.JDTAST_SimpleName306 = JDTAST_SimpleName306
        self.JDTAST_SimpleName313 = JDTAST_SimpleName313
        self.JDTAST_SimpleName352 = JDTAST_SimpleName352
        self.JDTAST_SimpleName412 = JDTAST_SimpleName412
        self.JDTAST_SimpleName427 = JDTAST_SimpleName427
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def JDTAST_SimpleName118(self):
        return self.__JDTAST_SimpleName118

    @JDTAST_SimpleName118.setter
    def JDTAST_SimpleName118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName118", None)
        self.__JDTAST_SimpleName118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_VariableDeclaration117"):
                opp_val = getattr(old_value, "JDTAST_VariableDeclaration117", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_VariableDeclaration117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_VariableDeclaration117"):
                opp_val = getattr(value, "JDTAST_VariableDeclaration117", None)
                setattr(value, "JDTAST_VariableDeclaration117", self)

    @property
    def JDTAST_SimpleName140(self):
        return self.__JDTAST_SimpleName140

    @JDTAST_SimpleName140.setter
    def JDTAST_SimpleName140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName140", None)
        self.__JDTAST_SimpleName140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_EnumConstantDeclaration139"):
                opp_val = getattr(old_value, "JDTAST_EnumConstantDeclaration139", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_EnumConstantDeclaration139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_EnumConstantDeclaration139"):
                opp_val = getattr(value, "JDTAST_EnumConstantDeclaration139", None)
                setattr(value, "JDTAST_EnumConstantDeclaration139", self)

    @property
    def JDTAST_SimpleName151(self):
        return self.__JDTAST_SimpleName151

    @JDTAST_SimpleName151.setter
    def JDTAST_SimpleName151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName151", None)
        self.__JDTAST_SimpleName151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodDeclaration150"):
                opp_val = getattr(old_value, "JDTAST_MethodDeclaration150", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodDeclaration150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodDeclaration150"):
                opp_val = getattr(value, "JDTAST_MethodDeclaration150", None)
                setattr(value, "JDTAST_MethodDeclaration150", self)

    @property
    def JDTAST_SimpleName352(self):
        return self.__JDTAST_SimpleName352

    @JDTAST_SimpleName352.setter
    def JDTAST_SimpleName352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName352", None)
        self.__JDTAST_SimpleName352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_LabeledStatement351"):
                opp_val = getattr(old_value, "JDTAST_LabeledStatement351", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_LabeledStatement351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_LabeledStatement351"):
                opp_val = getattr(value, "JDTAST_LabeledStatement351", None)
                setattr(value, "JDTAST_LabeledStatement351", self)

    @property
    def JDTAST_SimpleName110(self):
        return self.__JDTAST_SimpleName110

    @JDTAST_SimpleName110.setter
    def JDTAST_SimpleName110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName110", None)
        self.__JDTAST_SimpleName110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_TypeParameter"):
                opp_val = getattr(old_value, "JDTAST_TypeParameter", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_TypeParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_TypeParameter"):
                opp_val = getattr(value, "JDTAST_TypeParameter", None)
                setattr(value, "JDTAST_TypeParameter", self)

    @property
    def JDTAST_SimpleName306(self):
        return self.__JDTAST_SimpleName306

    @JDTAST_SimpleName306.setter
    def JDTAST_SimpleName306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName306", None)
        self.__JDTAST_SimpleName306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_BreakStatement"):
                opp_val = getattr(old_value, "JDTAST_BreakStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_BreakStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_BreakStatement"):
                opp_val = getattr(value, "JDTAST_BreakStatement", None)
                setattr(value, "JDTAST_BreakStatement", self)

    @property
    def JDTAST_SimpleName313(self):
        return self.__JDTAST_SimpleName313

    @JDTAST_SimpleName313.setter
    def JDTAST_SimpleName313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName313", None)
        self.__JDTAST_SimpleName313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ContinueStatement"):
                opp_val = getattr(old_value, "JDTAST_ContinueStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ContinueStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ContinueStatement"):
                opp_val = getattr(value, "JDTAST_ContinueStatement", None)
                setattr(value, "JDTAST_ContinueStatement", self)

    @property
    def JDTAST_SimpleName427(self):
        return self.__JDTAST_SimpleName427

    @JDTAST_SimpleName427.setter
    def JDTAST_SimpleName427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName427", None)
        self.__JDTAST_SimpleName427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_QualifiedName"):
                opp_val = getattr(old_value, "JDTAST_QualifiedName", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_QualifiedName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_QualifiedName"):
                opp_val = getattr(value, "JDTAST_QualifiedName", None)
                setattr(value, "JDTAST_QualifiedName", self)

    @property
    def JDTAST_SimpleName271(self):
        return self.__JDTAST_SimpleName271

    @JDTAST_SimpleName271.setter
    def JDTAST_SimpleName271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName271", None)
        self.__JDTAST_SimpleName271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperFieldAccess"):
                opp_val = getattr(old_value, "JDTAST_SuperFieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SuperFieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperFieldAccess"):
                opp_val = getattr(value, "JDTAST_SuperFieldAccess", None)
                setattr(value, "JDTAST_SuperFieldAccess", self)

    @property
    def JDTAST_SimpleName124(self):
        return self.__JDTAST_SimpleName124

    @JDTAST_SimpleName124.setter
    def JDTAST_SimpleName124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName124", None)
        self.__JDTAST_SimpleName124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_AbstractTypeDeclaration123"):
                opp_val = getattr(old_value, "JDTAST_AbstractTypeDeclaration123", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_AbstractTypeDeclaration123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_AbstractTypeDeclaration123"):
                opp_val = getattr(value, "JDTAST_AbstractTypeDeclaration123", None)
                setattr(value, "JDTAST_AbstractTypeDeclaration123", self)

    @property
    def JDTAST_SimpleName(self):
        return self.__JDTAST_SimpleName

    @JDTAST_SimpleName.setter
    def JDTAST_SimpleName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName", None)
        self.__JDTAST_SimpleName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MemberRef"):
                opp_val = getattr(old_value, "JDTAST_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MemberRef"):
                opp_val = getattr(value, "JDTAST_MemberRef", None)
                setattr(value, "JDTAST_MemberRef", self)

    @property
    def JDTAST_SimpleName129(self):
        return self.__JDTAST_SimpleName129

    @JDTAST_SimpleName129.setter
    def JDTAST_SimpleName129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName129", None)
        self.__JDTAST_SimpleName129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration128"):
                opp_val = getattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration128", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_AnnotationTypeMemberDeclaration128"):
                opp_val = getattr(value, "JDTAST_AnnotationTypeMemberDeclaration128", None)
                setattr(value, "JDTAST_AnnotationTypeMemberDeclaration128", self)

    @property
    def JDTAST_SimpleName412(self):
        return self.__JDTAST_SimpleName412

    @JDTAST_SimpleName412.setter
    def JDTAST_SimpleName412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName412", None)
        self.__JDTAST_SimpleName412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_QualifiedType"):
                opp_val = getattr(old_value, "JDTAST_QualifiedType", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_QualifiedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_QualifiedType"):
                opp_val = getattr(value, "JDTAST_QualifiedType", None)
                setattr(value, "JDTAST_QualifiedType", self)

    @property
    def JDTAST_SimpleName257(self):
        return self.__JDTAST_SimpleName257

    @JDTAST_SimpleName257.setter
    def JDTAST_SimpleName257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName257", None)
        self.__JDTAST_SimpleName257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodInvocation256"):
                opp_val = getattr(old_value, "JDTAST_MethodInvocation256", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodInvocation256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodInvocation256"):
                opp_val = getattr(value, "JDTAST_MethodInvocation256", None)
                setattr(value, "JDTAST_MethodInvocation256", self)

    @property
    def JDTAST_SimpleName93(self):
        return self.__JDTAST_SimpleName93

    @JDTAST_SimpleName93.setter
    def JDTAST_SimpleName93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName93", None)
        self.__JDTAST_SimpleName93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodRefParameter92"):
                opp_val = getattr(old_value, "JDTAST_MethodRefParameter92", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodRefParameter92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodRefParameter92"):
                opp_val = getattr(value, "JDTAST_MethodRefParameter92", None)
                setattr(value, "JDTAST_MethodRefParameter92", self)

    @property
    def JDTAST_SimpleName80(self):
        return self.__JDTAST_SimpleName80

    @JDTAST_SimpleName80.setter
    def JDTAST_SimpleName80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName80", None)
        self.__JDTAST_SimpleName80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MemberValuePair"):
                opp_val = getattr(old_value, "JDTAST_MemberValuePair", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MemberValuePair", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MemberValuePair"):
                opp_val = getattr(value, "JDTAST_MemberValuePair", None)
                setattr(value, "JDTAST_MemberValuePair", self)

    @property
    def JDTAST_SimpleName236(self):
        return self.__JDTAST_SimpleName236

    @JDTAST_SimpleName236.setter
    def JDTAST_SimpleName236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName236", None)
        self.__JDTAST_SimpleName236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_FieldAccess235"):
                opp_val = getattr(old_value, "JDTAST_FieldAccess235", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_FieldAccess235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_FieldAccess235"):
                opp_val = getattr(value, "JDTAST_FieldAccess235", None)
                setattr(value, "JDTAST_FieldAccess235", self)

    @property
    def JDTAST_SimpleName85(self):
        return self.__JDTAST_SimpleName85

    @JDTAST_SimpleName85.setter
    def JDTAST_SimpleName85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SimpleName__JDTAST_SimpleName85", None)
        self.__JDTAST_SimpleName85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodRef"):
                opp_val = getattr(old_value, "JDTAST_MethodRef", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodRef"):
                opp_val = getattr(value, "JDTAST_MethodRef", None)
                setattr(value, "JDTAST_MethodRef", self)

class JDTAST_Name(Expression):

    def __init__(self, fullyQualifiedName: str, JDTAST_Name: "JDTAST_ImportDeclaration" = None, JDTAST_Name78: "JDTAST_MemberRef" = None, JDTAST_Name88: "JDTAST_MethodRef" = None, JDTAST_Name103: "JDTAST_PackageDeclaration" = None, JDTAST_Name160: "JDTAST_MethodDeclaration" = None, JDTAST_Name185: "JDTAST_Annotation" = None, JDTAST_Name274: "JDTAST_SuperFieldAccess" = None, JDTAST_Name279: "JDTAST_SuperMethodInvocation" = None, JDTAST_Name282: "JDTAST_SuperMethodInvocation" = None, JDTAST_Name287: "JDTAST_ThisExpression" = None, JDTAST_Name417: "JDTAST_SimpleType" = None, JDTAST_Name430: "JDTAST_QualifiedName" = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.JDTAST_Name = JDTAST_Name
        self.JDTAST_Name78 = JDTAST_Name78
        self.JDTAST_Name88 = JDTAST_Name88
        self.JDTAST_Name103 = JDTAST_Name103
        self.JDTAST_Name160 = JDTAST_Name160
        self.JDTAST_Name185 = JDTAST_Name185
        self.JDTAST_Name274 = JDTAST_Name274
        self.JDTAST_Name279 = JDTAST_Name279
        self.JDTAST_Name282 = JDTAST_Name282
        self.JDTAST_Name287 = JDTAST_Name287
        self.JDTAST_Name417 = JDTAST_Name417
        self.JDTAST_Name430 = JDTAST_Name430
        
    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def JDTAST_Name430(self):
        return self.__JDTAST_Name430

    @JDTAST_Name430.setter
    def JDTAST_Name430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name430", None)
        self.__JDTAST_Name430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_QualifiedName429"):
                opp_val = getattr(old_value, "JDTAST_QualifiedName429", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_QualifiedName429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_QualifiedName429"):
                opp_val = getattr(value, "JDTAST_QualifiedName429", None)
                setattr(value, "JDTAST_QualifiedName429", self)

    @property
    def JDTAST_Name417(self):
        return self.__JDTAST_Name417

    @JDTAST_Name417.setter
    def JDTAST_Name417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name417", None)
        self.__JDTAST_Name417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SimpleType"):
                opp_val = getattr(old_value, "JDTAST_SimpleType", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SimpleType"):
                opp_val = getattr(value, "JDTAST_SimpleType", None)
                setattr(value, "JDTAST_SimpleType", self)

    @property
    def JDTAST_Name78(self):
        return self.__JDTAST_Name78

    @JDTAST_Name78.setter
    def JDTAST_Name78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name78", None)
        self.__JDTAST_Name78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MemberRef77"):
                opp_val = getattr(old_value, "JDTAST_MemberRef77", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MemberRef77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MemberRef77"):
                opp_val = getattr(value, "JDTAST_MemberRef77", None)
                setattr(value, "JDTAST_MemberRef77", self)

    @property
    def JDTAST_Name185(self):
        return self.__JDTAST_Name185

    @JDTAST_Name185.setter
    def JDTAST_Name185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name185", None)
        self.__JDTAST_Name185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Annotation184"):
                opp_val = getattr(old_value, "JDTAST_Annotation184", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Annotation184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Annotation184"):
                opp_val = getattr(value, "JDTAST_Annotation184", None)
                setattr(value, "JDTAST_Annotation184", self)

    @property
    def JDTAST_Name274(self):
        return self.__JDTAST_Name274

    @JDTAST_Name274.setter
    def JDTAST_Name274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name274", None)
        self.__JDTAST_Name274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperFieldAccess273"):
                opp_val = getattr(old_value, "JDTAST_SuperFieldAccess273", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SuperFieldAccess273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperFieldAccess273"):
                opp_val = getattr(value, "JDTAST_SuperFieldAccess273", None)
                setattr(value, "JDTAST_SuperFieldAccess273", self)

    @property
    def JDTAST_Name279(self):
        return self.__JDTAST_Name279

    @JDTAST_Name279.setter
    def JDTAST_Name279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name279", None)
        self.__JDTAST_Name279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperMethodInvocation278"):
                opp_val = getattr(old_value, "JDTAST_SuperMethodInvocation278", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SuperMethodInvocation278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperMethodInvocation278"):
                opp_val = getattr(value, "JDTAST_SuperMethodInvocation278", None)
                setattr(value, "JDTAST_SuperMethodInvocation278", self)

    @property
    def JDTAST_Name88(self):
        return self.__JDTAST_Name88

    @JDTAST_Name88.setter
    def JDTAST_Name88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name88", None)
        self.__JDTAST_Name88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodRef87"):
                opp_val = getattr(old_value, "JDTAST_MethodRef87", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodRef87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodRef87"):
                opp_val = getattr(value, "JDTAST_MethodRef87", None)
                setattr(value, "JDTAST_MethodRef87", self)

    @property
    def JDTAST_Name282(self):
        return self.__JDTAST_Name282

    @JDTAST_Name282.setter
    def JDTAST_Name282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name282", None)
        self.__JDTAST_Name282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperMethodInvocation281"):
                opp_val = getattr(old_value, "JDTAST_SuperMethodInvocation281", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SuperMethodInvocation281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperMethodInvocation281"):
                opp_val = getattr(value, "JDTAST_SuperMethodInvocation281", None)
                setattr(value, "JDTAST_SuperMethodInvocation281", self)

    @property
    def JDTAST_Name287(self):
        return self.__JDTAST_Name287

    @JDTAST_Name287.setter
    def JDTAST_Name287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name287", None)
        self.__JDTAST_Name287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ThisExpression"):
                opp_val = getattr(old_value, "JDTAST_ThisExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ThisExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ThisExpression"):
                opp_val = getattr(value, "JDTAST_ThisExpression", None)
                setattr(value, "JDTAST_ThisExpression", self)

    @property
    def JDTAST_Name103(self):
        return self.__JDTAST_Name103

    @JDTAST_Name103.setter
    def JDTAST_Name103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name103", None)
        self.__JDTAST_Name103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_PackageDeclaration102"):
                opp_val = getattr(old_value, "JDTAST_PackageDeclaration102", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_PackageDeclaration102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_PackageDeclaration102"):
                opp_val = getattr(value, "JDTAST_PackageDeclaration102", None)
                setattr(value, "JDTAST_PackageDeclaration102", self)

    @property
    def JDTAST_Name(self):
        return self.__JDTAST_Name

    @JDTAST_Name.setter
    def JDTAST_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name", None)
        self.__JDTAST_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ImportDeclaration74"):
                opp_val = getattr(old_value, "JDTAST_ImportDeclaration74", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ImportDeclaration74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ImportDeclaration74"):
                opp_val = getattr(value, "JDTAST_ImportDeclaration74", None)
                setattr(value, "JDTAST_ImportDeclaration74", self)

    @property
    def JDTAST_Name160(self):
        return self.__JDTAST_Name160

    @JDTAST_Name160.setter
    def JDTAST_Name160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Name__JDTAST_Name160", None)
        self.__JDTAST_Name160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodDeclaration159"):
                opp_val = getattr(old_value, "JDTAST_MethodDeclaration159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodDeclaration159"):
                opp_val = getattr(value, "JDTAST_MethodDeclaration159", None)
                if opp_val is None:
                    setattr(value, "JDTAST_MethodDeclaration159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, JDTAST_AbstractTypeDeclaration: "JDTAST_CompilationUnit" = None, JDTAST_AbstractTypeDeclaration120: set["JDTAST_BodyDeclaration"] = None, JDTAST_AbstractTypeDeclaration123: "JDTAST_SimpleName" = None, JDTAST_AbstractTypeDeclaration386: "JDTAST_TypeDeclarationStatement" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.JDTAST_AbstractTypeDeclaration = JDTAST_AbstractTypeDeclaration
        self.JDTAST_AbstractTypeDeclaration120 = JDTAST_AbstractTypeDeclaration120 if JDTAST_AbstractTypeDeclaration120 is not None else set()
        self.JDTAST_AbstractTypeDeclaration123 = JDTAST_AbstractTypeDeclaration123
        self.JDTAST_AbstractTypeDeclaration386 = JDTAST_AbstractTypeDeclaration386
        
    @property
    def packageMemberTypeDeclaration(self) -> str:
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration

    @property
    def localTypeDeclaration(self) -> str:
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration

    @property
    def memberTypeDeclaration(self) -> str:
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration

    @property
    def JDTAST_AbstractTypeDeclaration120(self):
        return self.__JDTAST_AbstractTypeDeclaration120

    @JDTAST_AbstractTypeDeclaration120.setter
    def JDTAST_AbstractTypeDeclaration120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration120", None)
        self.__JDTAST_AbstractTypeDeclaration120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_BodyDeclaration121"):
                    opp_val = getattr(item, "JDTAST_BodyDeclaration121", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_BodyDeclaration121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_BodyDeclaration121"):
                    opp_val = getattr(item, "JDTAST_BodyDeclaration121", None)
                    
                    setattr(item, "JDTAST_BodyDeclaration121", self)
                    

    @property
    def JDTAST_AbstractTypeDeclaration123(self):
        return self.__JDTAST_AbstractTypeDeclaration123

    @JDTAST_AbstractTypeDeclaration123.setter
    def JDTAST_AbstractTypeDeclaration123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration123", None)
        self.__JDTAST_AbstractTypeDeclaration123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SimpleName124"):
                opp_val = getattr(old_value, "JDTAST_SimpleName124", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SimpleName124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SimpleName124"):
                opp_val = getattr(value, "JDTAST_SimpleName124", None)
                setattr(value, "JDTAST_SimpleName124", self)

    @property
    def JDTAST_AbstractTypeDeclaration(self):
        return self.__JDTAST_AbstractTypeDeclaration

    @JDTAST_AbstractTypeDeclaration.setter
    def JDTAST_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration", None)
        self.__JDTAST_AbstractTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_CompilationUnit70"):
                opp_val = getattr(old_value, "JDTAST_CompilationUnit70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_CompilationUnit70"):
                opp_val = getattr(value, "JDTAST_CompilationUnit70", None)
                if opp_val is None:
                    setattr(value, "JDTAST_CompilationUnit70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_AbstractTypeDeclaration386(self):
        return self.__JDTAST_AbstractTypeDeclaration386

    @JDTAST_AbstractTypeDeclaration386.setter
    def JDTAST_AbstractTypeDeclaration386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_AbstractTypeDeclaration__JDTAST_AbstractTypeDeclaration386", None)
        self.__JDTAST_AbstractTypeDeclaration386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_TypeDeclarationStatement"):
                opp_val = getattr(old_value, "JDTAST_TypeDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_TypeDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_TypeDeclarationStatement"):
                opp_val = getattr(value, "JDTAST_TypeDeclarationStatement", None)
                setattr(value, "JDTAST_TypeDeclarationStatement", self)

class ASTNode:

    pass
class JDTAST_Comment(ASTNode):

    pass
class JDTAST_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, JDTAST_Expression: "JDTAST_IType" = None, JDTAST_Expression83: "JDTAST_MemberValuePair" = None, JDTAST_Expression115: "JDTAST_VariableDeclaration" = None, JDTAST_Expression134: "JDTAST_EnumConstantDeclaration" = None, JDTAST_Expression126: "JDTAST_AnnotationTypeMemberDeclaration" = None, JDTAST_Expression187: "JDTAST_ArrayAccess" = None, JDTAST_Expression190: "JDTAST_ArrayAccess" = None, JDTAST_Expression192: "JDTAST_ArrayCreation" = None, JDTAST_Expression199: "JDTAST_ArrayInitializer" = None, JDTAST_Expression206: "JDTAST_CastExpression" = None, JDTAST_Expression201: "JDTAST_Assignment" = None, JDTAST_Expression204: "JDTAST_Assignment" = None, JDTAST_Expression211: "JDTAST_ClassInstanceCreation" = None, JDTAST_Expression217: "JDTAST_ClassInstanceCreation" = None, JDTAST_Expression233: "JDTAST_FieldAccess" = None, JDTAST_Expression238: "JDTAST_InfixExpression" = None, JDTAST_Expression241: "JDTAST_InfixExpression" = None, JDTAST_Expression244: "JDTAST_InfixExpression" = None, JDTAST_Expression225: "JDTAST_ConditionalExpression" = None, JDTAST_Expression228: "JDTAST_ConditionalExpression" = None, JDTAST_Expression231: "JDTAST_ConditionalExpression" = None, JDTAST_Expression246: "JDTAST_InstanceofExpression" = None, JDTAST_Expression251: "JDTAST_MethodInvocation" = None, JDTAST_Expression254: "JDTAST_MethodInvocation" = None, JDTAST_Expression265: "JDTAST_ParenthesizedExpression" = None, JDTAST_Expression267: "JDTAST_PostfixExpression" = None, JDTAST_Expression269: "JDTAST_PrefixExpression" = None, JDTAST_Expression276: "JDTAST_SuperMethodInvocation" = None, JDTAST_Expression299: "JDTAST_AssertStatement" = None, JDTAST_Expression302: "JDTAST_AssertStatement" = None, JDTAST_Expression318: "JDTAST_DoStatement" = None, JDTAST_Expression308: "JDTAST_ConstructorInvocation" = None, JDTAST_Expression323: "JDTAST_EnhancedForStatement" = None, JDTAST_Expression328: "JDTAST_ExpressionStatement" = None, JDTAST_Expression333: "JDTAST_ForStatement" = None, JDTAST_Expression336: "JDTAST_ForStatement" = None, JDTAST_Expression344: "JDTAST_IfStatement" = None, JDTAST_Expression354: "JDTAST_ReturnStatement" = None, JDTAST_Expression339: "JDTAST_ForStatement" = None, JDTAST_Expression359: "JDTAST_SuperConstructorInvocation" = None, JDTAST_Expression364: "JDTAST_SwitchCase" = None, JDTAST_Expression366: "JDTAST_SwitchStatement" = None, JDTAST_Expression356: "JDTAST_SuperConstructorInvocation" = None, JDTAST_Expression374: "JDTAST_SynchronizedStatement" = None, JDTAST_Expression376: "JDTAST_ThrowStatement" = None, JDTAST_Expression399: "JDTAST_WhileStatement" = None, JDTAST_Expression434: "JDTAST_SingleMemberAnnotation" = None):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        self.JDTAST_Expression = JDTAST_Expression
        self.JDTAST_Expression83 = JDTAST_Expression83
        self.JDTAST_Expression115 = JDTAST_Expression115
        self.JDTAST_Expression134 = JDTAST_Expression134
        self.JDTAST_Expression126 = JDTAST_Expression126
        self.JDTAST_Expression187 = JDTAST_Expression187
        self.JDTAST_Expression190 = JDTAST_Expression190
        self.JDTAST_Expression192 = JDTAST_Expression192
        self.JDTAST_Expression199 = JDTAST_Expression199
        self.JDTAST_Expression206 = JDTAST_Expression206
        self.JDTAST_Expression201 = JDTAST_Expression201
        self.JDTAST_Expression204 = JDTAST_Expression204
        self.JDTAST_Expression211 = JDTAST_Expression211
        self.JDTAST_Expression217 = JDTAST_Expression217
        self.JDTAST_Expression233 = JDTAST_Expression233
        self.JDTAST_Expression238 = JDTAST_Expression238
        self.JDTAST_Expression241 = JDTAST_Expression241
        self.JDTAST_Expression244 = JDTAST_Expression244
        self.JDTAST_Expression225 = JDTAST_Expression225
        self.JDTAST_Expression228 = JDTAST_Expression228
        self.JDTAST_Expression231 = JDTAST_Expression231
        self.JDTAST_Expression246 = JDTAST_Expression246
        self.JDTAST_Expression251 = JDTAST_Expression251
        self.JDTAST_Expression254 = JDTAST_Expression254
        self.JDTAST_Expression265 = JDTAST_Expression265
        self.JDTAST_Expression267 = JDTAST_Expression267
        self.JDTAST_Expression269 = JDTAST_Expression269
        self.JDTAST_Expression276 = JDTAST_Expression276
        self.JDTAST_Expression299 = JDTAST_Expression299
        self.JDTAST_Expression302 = JDTAST_Expression302
        self.JDTAST_Expression318 = JDTAST_Expression318
        self.JDTAST_Expression308 = JDTAST_Expression308
        self.JDTAST_Expression323 = JDTAST_Expression323
        self.JDTAST_Expression328 = JDTAST_Expression328
        self.JDTAST_Expression333 = JDTAST_Expression333
        self.JDTAST_Expression336 = JDTAST_Expression336
        self.JDTAST_Expression344 = JDTAST_Expression344
        self.JDTAST_Expression354 = JDTAST_Expression354
        self.JDTAST_Expression339 = JDTAST_Expression339
        self.JDTAST_Expression359 = JDTAST_Expression359
        self.JDTAST_Expression364 = JDTAST_Expression364
        self.JDTAST_Expression366 = JDTAST_Expression366
        self.JDTAST_Expression356 = JDTAST_Expression356
        self.JDTAST_Expression374 = JDTAST_Expression374
        self.JDTAST_Expression376 = JDTAST_Expression376
        self.JDTAST_Expression399 = JDTAST_Expression399
        self.JDTAST_Expression434 = JDTAST_Expression434
        
    @property
    def resolveUnboxing(self) -> str:
        return self.__resolveUnboxing

    @resolveUnboxing.setter
    def resolveUnboxing(self, resolveUnboxing: str):
        self.__resolveUnboxing = resolveUnboxing

    @property
    def resolveBoxing(self) -> str:
        return self.__resolveBoxing

    @resolveBoxing.setter
    def resolveBoxing(self, resolveBoxing: str):
        self.__resolveBoxing = resolveBoxing

    @property
    def JDTAST_Expression204(self):
        return self.__JDTAST_Expression204

    @JDTAST_Expression204.setter
    def JDTAST_Expression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression204", None)
        self.__JDTAST_Expression204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Assignment203"):
                opp_val = getattr(old_value, "JDTAST_Assignment203", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Assignment203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Assignment203"):
                opp_val = getattr(value, "JDTAST_Assignment203", None)
                setattr(value, "JDTAST_Assignment203", self)

    @property
    def JDTAST_Expression364(self):
        return self.__JDTAST_Expression364

    @JDTAST_Expression364.setter
    def JDTAST_Expression364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression364", None)
        self.__JDTAST_Expression364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SwitchCase"):
                opp_val = getattr(old_value, "JDTAST_SwitchCase", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SwitchCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SwitchCase"):
                opp_val = getattr(value, "JDTAST_SwitchCase", None)
                setattr(value, "JDTAST_SwitchCase", self)

    @property
    def JDTAST_Expression126(self):
        return self.__JDTAST_Expression126

    @JDTAST_Expression126.setter
    def JDTAST_Expression126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression126", None)
        self.__JDTAST_Expression126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration"):
                opp_val = getattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_AnnotationTypeMemberDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_AnnotationTypeMemberDeclaration"):
                opp_val = getattr(value, "JDTAST_AnnotationTypeMemberDeclaration", None)
                setattr(value, "JDTAST_AnnotationTypeMemberDeclaration", self)

    @property
    def JDTAST_Expression251(self):
        return self.__JDTAST_Expression251

    @JDTAST_Expression251.setter
    def JDTAST_Expression251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression251", None)
        self.__JDTAST_Expression251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodInvocation"):
                opp_val = getattr(old_value, "JDTAST_MethodInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodInvocation"):
                opp_val = getattr(value, "JDTAST_MethodInvocation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_MethodInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression246(self):
        return self.__JDTAST_Expression246

    @JDTAST_Expression246.setter
    def JDTAST_Expression246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression246", None)
        self.__JDTAST_Expression246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_InstanceofExpression"):
                opp_val = getattr(old_value, "JDTAST_InstanceofExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_InstanceofExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_InstanceofExpression"):
                opp_val = getattr(value, "JDTAST_InstanceofExpression", None)
                setattr(value, "JDTAST_InstanceofExpression", self)

    @property
    def JDTAST_Expression434(self):
        return self.__JDTAST_Expression434

    @JDTAST_Expression434.setter
    def JDTAST_Expression434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression434", None)
        self.__JDTAST_Expression434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SingleMemberAnnotation"):
                opp_val = getattr(old_value, "JDTAST_SingleMemberAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SingleMemberAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SingleMemberAnnotation"):
                opp_val = getattr(value, "JDTAST_SingleMemberAnnotation", None)
                setattr(value, "JDTAST_SingleMemberAnnotation", self)

    @property
    def JDTAST_Expression336(self):
        return self.__JDTAST_Expression336

    @JDTAST_Expression336.setter
    def JDTAST_Expression336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression336", None)
        self.__JDTAST_Expression336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ForStatement335"):
                opp_val = getattr(old_value, "JDTAST_ForStatement335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ForStatement335"):
                opp_val = getattr(value, "JDTAST_ForStatement335", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ForStatement335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression199(self):
        return self.__JDTAST_Expression199

    @JDTAST_Expression199.setter
    def JDTAST_Expression199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression199", None)
        self.__JDTAST_Expression199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ArrayInitializer198"):
                opp_val = getattr(old_value, "JDTAST_ArrayInitializer198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ArrayInitializer198"):
                opp_val = getattr(value, "JDTAST_ArrayInitializer198", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ArrayInitializer198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression241(self):
        return self.__JDTAST_Expression241

    @JDTAST_Expression241.setter
    def JDTAST_Expression241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression241", None)
        self.__JDTAST_Expression241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_InfixExpression240"):
                opp_val = getattr(old_value, "JDTAST_InfixExpression240", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_InfixExpression240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_InfixExpression240"):
                opp_val = getattr(value, "JDTAST_InfixExpression240", None)
                setattr(value, "JDTAST_InfixExpression240", self)

    @property
    def JDTAST_Expression83(self):
        return self.__JDTAST_Expression83

    @JDTAST_Expression83.setter
    def JDTAST_Expression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression83", None)
        self.__JDTAST_Expression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MemberValuePair82"):
                opp_val = getattr(old_value, "JDTAST_MemberValuePair82", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MemberValuePair82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MemberValuePair82"):
                opp_val = getattr(value, "JDTAST_MemberValuePair82", None)
                setattr(value, "JDTAST_MemberValuePair82", self)

    @property
    def JDTAST_Expression254(self):
        return self.__JDTAST_Expression254

    @JDTAST_Expression254.setter
    def JDTAST_Expression254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression254", None)
        self.__JDTAST_Expression254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodInvocation253"):
                opp_val = getattr(old_value, "JDTAST_MethodInvocation253", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodInvocation253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodInvocation253"):
                opp_val = getattr(value, "JDTAST_MethodInvocation253", None)
                setattr(value, "JDTAST_MethodInvocation253", self)

    @property
    def JDTAST_Expression354(self):
        return self.__JDTAST_Expression354

    @JDTAST_Expression354.setter
    def JDTAST_Expression354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression354", None)
        self.__JDTAST_Expression354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ReturnStatement"):
                opp_val = getattr(old_value, "JDTAST_ReturnStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ReturnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ReturnStatement"):
                opp_val = getattr(value, "JDTAST_ReturnStatement", None)
                setattr(value, "JDTAST_ReturnStatement", self)

    @property
    def JDTAST_Expression201(self):
        return self.__JDTAST_Expression201

    @JDTAST_Expression201.setter
    def JDTAST_Expression201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression201", None)
        self.__JDTAST_Expression201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Assignment"):
                opp_val = getattr(old_value, "JDTAST_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Assignment"):
                opp_val = getattr(value, "JDTAST_Assignment", None)
                setattr(value, "JDTAST_Assignment", self)

    @property
    def JDTAST_Expression359(self):
        return self.__JDTAST_Expression359

    @JDTAST_Expression359.setter
    def JDTAST_Expression359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression359", None)
        self.__JDTAST_Expression359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperConstructorInvocation358"):
                opp_val = getattr(old_value, "JDTAST_SuperConstructorInvocation358", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SuperConstructorInvocation358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperConstructorInvocation358"):
                opp_val = getattr(value, "JDTAST_SuperConstructorInvocation358", None)
                setattr(value, "JDTAST_SuperConstructorInvocation358", self)

    @property
    def JDTAST_Expression206(self):
        return self.__JDTAST_Expression206

    @JDTAST_Expression206.setter
    def JDTAST_Expression206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression206", None)
        self.__JDTAST_Expression206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_CastExpression"):
                opp_val = getattr(old_value, "JDTAST_CastExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_CastExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_CastExpression"):
                opp_val = getattr(value, "JDTAST_CastExpression", None)
                setattr(value, "JDTAST_CastExpression", self)

    @property
    def JDTAST_Expression333(self):
        return self.__JDTAST_Expression333

    @JDTAST_Expression333.setter
    def JDTAST_Expression333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression333", None)
        self.__JDTAST_Expression333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ForStatement332"):
                opp_val = getattr(old_value, "JDTAST_ForStatement332", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ForStatement332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ForStatement332"):
                opp_val = getattr(value, "JDTAST_ForStatement332", None)
                setattr(value, "JDTAST_ForStatement332", self)

    @property
    def JDTAST_Expression376(self):
        return self.__JDTAST_Expression376

    @JDTAST_Expression376.setter
    def JDTAST_Expression376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression376", None)
        self.__JDTAST_Expression376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ThrowStatement"):
                opp_val = getattr(old_value, "JDTAST_ThrowStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ThrowStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ThrowStatement"):
                opp_val = getattr(value, "JDTAST_ThrowStatement", None)
                setattr(value, "JDTAST_ThrowStatement", self)

    @property
    def JDTAST_Expression233(self):
        return self.__JDTAST_Expression233

    @JDTAST_Expression233.setter
    def JDTAST_Expression233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression233", None)
        self.__JDTAST_Expression233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_FieldAccess"):
                opp_val = getattr(old_value, "JDTAST_FieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_FieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_FieldAccess"):
                opp_val = getattr(value, "JDTAST_FieldAccess", None)
                setattr(value, "JDTAST_FieldAccess", self)

    @property
    def JDTAST_Expression339(self):
        return self.__JDTAST_Expression339

    @JDTAST_Expression339.setter
    def JDTAST_Expression339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression339", None)
        self.__JDTAST_Expression339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ForStatement338"):
                opp_val = getattr(old_value, "JDTAST_ForStatement338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ForStatement338"):
                opp_val = getattr(value, "JDTAST_ForStatement338", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ForStatement338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression238(self):
        return self.__JDTAST_Expression238

    @JDTAST_Expression238.setter
    def JDTAST_Expression238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression238", None)
        self.__JDTAST_Expression238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_InfixExpression"):
                opp_val = getattr(old_value, "JDTAST_InfixExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_InfixExpression"):
                opp_val = getattr(value, "JDTAST_InfixExpression", None)
                if opp_val is None:
                    setattr(value, "JDTAST_InfixExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression299(self):
        return self.__JDTAST_Expression299

    @JDTAST_Expression299.setter
    def JDTAST_Expression299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression299", None)
        self.__JDTAST_Expression299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_AssertStatement"):
                opp_val = getattr(old_value, "JDTAST_AssertStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_AssertStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_AssertStatement"):
                opp_val = getattr(value, "JDTAST_AssertStatement", None)
                setattr(value, "JDTAST_AssertStatement", self)

    @property
    def JDTAST_Expression323(self):
        return self.__JDTAST_Expression323

    @JDTAST_Expression323.setter
    def JDTAST_Expression323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression323", None)
        self.__JDTAST_Expression323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_EnhancedForStatement322"):
                opp_val = getattr(old_value, "JDTAST_EnhancedForStatement322", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_EnhancedForStatement322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_EnhancedForStatement322"):
                opp_val = getattr(value, "JDTAST_EnhancedForStatement322", None)
                setattr(value, "JDTAST_EnhancedForStatement322", self)

    @property
    def JDTAST_Expression356(self):
        return self.__JDTAST_Expression356

    @JDTAST_Expression356.setter
    def JDTAST_Expression356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression356", None)
        self.__JDTAST_Expression356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperConstructorInvocation"):
                opp_val = getattr(old_value, "JDTAST_SuperConstructorInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperConstructorInvocation"):
                opp_val = getattr(value, "JDTAST_SuperConstructorInvocation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_SuperConstructorInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression115(self):
        return self.__JDTAST_Expression115

    @JDTAST_Expression115.setter
    def JDTAST_Expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression115", None)
        self.__JDTAST_Expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_VariableDeclaration"):
                opp_val = getattr(old_value, "JDTAST_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_VariableDeclaration"):
                opp_val = getattr(value, "JDTAST_VariableDeclaration", None)
                setattr(value, "JDTAST_VariableDeclaration", self)

    @property
    def JDTAST_Expression302(self):
        return self.__JDTAST_Expression302

    @JDTAST_Expression302.setter
    def JDTAST_Expression302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression302", None)
        self.__JDTAST_Expression302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_AssertStatement301"):
                opp_val = getattr(old_value, "JDTAST_AssertStatement301", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_AssertStatement301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_AssertStatement301"):
                opp_val = getattr(value, "JDTAST_AssertStatement301", None)
                setattr(value, "JDTAST_AssertStatement301", self)

    @property
    def JDTAST_Expression190(self):
        return self.__JDTAST_Expression190

    @JDTAST_Expression190.setter
    def JDTAST_Expression190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression190", None)
        self.__JDTAST_Expression190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ArrayAccess189"):
                opp_val = getattr(old_value, "JDTAST_ArrayAccess189", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ArrayAccess189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ArrayAccess189"):
                opp_val = getattr(value, "JDTAST_ArrayAccess189", None)
                setattr(value, "JDTAST_ArrayAccess189", self)

    @property
    def JDTAST_Expression328(self):
        return self.__JDTAST_Expression328

    @JDTAST_Expression328.setter
    def JDTAST_Expression328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression328", None)
        self.__JDTAST_Expression328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ExpressionStatement"):
                opp_val = getattr(old_value, "JDTAST_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ExpressionStatement"):
                opp_val = getattr(value, "JDTAST_ExpressionStatement", None)
                setattr(value, "JDTAST_ExpressionStatement", self)

    @property
    def JDTAST_Expression269(self):
        return self.__JDTAST_Expression269

    @JDTAST_Expression269.setter
    def JDTAST_Expression269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression269", None)
        self.__JDTAST_Expression269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_PrefixExpression"):
                opp_val = getattr(old_value, "JDTAST_PrefixExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_PrefixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_PrefixExpression"):
                opp_val = getattr(value, "JDTAST_PrefixExpression", None)
                setattr(value, "JDTAST_PrefixExpression", self)

    @property
    def JDTAST_Expression374(self):
        return self.__JDTAST_Expression374

    @JDTAST_Expression374.setter
    def JDTAST_Expression374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression374", None)
        self.__JDTAST_Expression374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SynchronizedStatement373"):
                opp_val = getattr(old_value, "JDTAST_SynchronizedStatement373", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SynchronizedStatement373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SynchronizedStatement373"):
                opp_val = getattr(value, "JDTAST_SynchronizedStatement373", None)
                setattr(value, "JDTAST_SynchronizedStatement373", self)

    @property
    def JDTAST_Expression217(self):
        return self.__JDTAST_Expression217

    @JDTAST_Expression217.setter
    def JDTAST_Expression217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression217", None)
        self.__JDTAST_Expression217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ClassInstanceCreation216"):
                opp_val = getattr(old_value, "JDTAST_ClassInstanceCreation216", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ClassInstanceCreation216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ClassInstanceCreation216"):
                opp_val = getattr(value, "JDTAST_ClassInstanceCreation216", None)
                setattr(value, "JDTAST_ClassInstanceCreation216", self)

    @property
    def JDTAST_Expression192(self):
        return self.__JDTAST_Expression192

    @JDTAST_Expression192.setter
    def JDTAST_Expression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression192", None)
        self.__JDTAST_Expression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ArrayCreation"):
                opp_val = getattr(old_value, "JDTAST_ArrayCreation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ArrayCreation"):
                opp_val = getattr(value, "JDTAST_ArrayCreation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ArrayCreation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression308(self):
        return self.__JDTAST_Expression308

    @JDTAST_Expression308.setter
    def JDTAST_Expression308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression308", None)
        self.__JDTAST_Expression308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ConstructorInvocation"):
                opp_val = getattr(old_value, "JDTAST_ConstructorInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ConstructorInvocation"):
                opp_val = getattr(value, "JDTAST_ConstructorInvocation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ConstructorInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression244(self):
        return self.__JDTAST_Expression244

    @JDTAST_Expression244.setter
    def JDTAST_Expression244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression244", None)
        self.__JDTAST_Expression244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_InfixExpression243"):
                opp_val = getattr(old_value, "JDTAST_InfixExpression243", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_InfixExpression243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_InfixExpression243"):
                opp_val = getattr(value, "JDTAST_InfixExpression243", None)
                setattr(value, "JDTAST_InfixExpression243", self)

    @property
    def JDTAST_Expression187(self):
        return self.__JDTAST_Expression187

    @JDTAST_Expression187.setter
    def JDTAST_Expression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression187", None)
        self.__JDTAST_Expression187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ArrayAccess"):
                opp_val = getattr(old_value, "JDTAST_ArrayAccess", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ArrayAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ArrayAccess"):
                opp_val = getattr(value, "JDTAST_ArrayAccess", None)
                setattr(value, "JDTAST_ArrayAccess", self)

    @property
    def JDTAST_Expression318(self):
        return self.__JDTAST_Expression318

    @JDTAST_Expression318.setter
    def JDTAST_Expression318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression318", None)
        self.__JDTAST_Expression318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_DoStatement317"):
                opp_val = getattr(old_value, "JDTAST_DoStatement317", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_DoStatement317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_DoStatement317"):
                opp_val = getattr(value, "JDTAST_DoStatement317", None)
                setattr(value, "JDTAST_DoStatement317", self)

    @property
    def JDTAST_Expression228(self):
        return self.__JDTAST_Expression228

    @JDTAST_Expression228.setter
    def JDTAST_Expression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression228", None)
        self.__JDTAST_Expression228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ConditionalExpression227"):
                opp_val = getattr(old_value, "JDTAST_ConditionalExpression227", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ConditionalExpression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ConditionalExpression227"):
                opp_val = getattr(value, "JDTAST_ConditionalExpression227", None)
                setattr(value, "JDTAST_ConditionalExpression227", self)

    @property
    def JDTAST_Expression134(self):
        return self.__JDTAST_Expression134

    @JDTAST_Expression134.setter
    def JDTAST_Expression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression134", None)
        self.__JDTAST_Expression134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_EnumConstantDeclaration"):
                opp_val = getattr(old_value, "JDTAST_EnumConstantDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_EnumConstantDeclaration"):
                opp_val = getattr(value, "JDTAST_EnumConstantDeclaration", None)
                if opp_val is None:
                    setattr(value, "JDTAST_EnumConstantDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression276(self):
        return self.__JDTAST_Expression276

    @JDTAST_Expression276.setter
    def JDTAST_Expression276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression276", None)
        self.__JDTAST_Expression276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SuperMethodInvocation"):
                opp_val = getattr(old_value, "JDTAST_SuperMethodInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SuperMethodInvocation"):
                opp_val = getattr(value, "JDTAST_SuperMethodInvocation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_SuperMethodInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_Expression225(self):
        return self.__JDTAST_Expression225

    @JDTAST_Expression225.setter
    def JDTAST_Expression225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression225", None)
        self.__JDTAST_Expression225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ConditionalExpression"):
                opp_val = getattr(old_value, "JDTAST_ConditionalExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ConditionalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ConditionalExpression"):
                opp_val = getattr(value, "JDTAST_ConditionalExpression", None)
                setattr(value, "JDTAST_ConditionalExpression", self)

    @property
    def JDTAST_Expression(self):
        return self.__JDTAST_Expression

    @JDTAST_Expression.setter
    def JDTAST_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression", None)
        self.__JDTAST_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType72"):
                opp_val = getattr(old_value, "JDTAST_IType72", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType72"):
                opp_val = getattr(value, "JDTAST_IType72", None)
                setattr(value, "JDTAST_IType72", self)

    @property
    def JDTAST_Expression265(self):
        return self.__JDTAST_Expression265

    @JDTAST_Expression265.setter
    def JDTAST_Expression265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression265", None)
        self.__JDTAST_Expression265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ParenthesizedExpression"):
                opp_val = getattr(old_value, "JDTAST_ParenthesizedExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ParenthesizedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ParenthesizedExpression"):
                opp_val = getattr(value, "JDTAST_ParenthesizedExpression", None)
                setattr(value, "JDTAST_ParenthesizedExpression", self)

    @property
    def JDTAST_Expression366(self):
        return self.__JDTAST_Expression366

    @JDTAST_Expression366.setter
    def JDTAST_Expression366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression366", None)
        self.__JDTAST_Expression366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SwitchStatement"):
                opp_val = getattr(old_value, "JDTAST_SwitchStatement", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SwitchStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SwitchStatement"):
                opp_val = getattr(value, "JDTAST_SwitchStatement", None)
                setattr(value, "JDTAST_SwitchStatement", self)

    @property
    def JDTAST_Expression267(self):
        return self.__JDTAST_Expression267

    @JDTAST_Expression267.setter
    def JDTAST_Expression267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression267", None)
        self.__JDTAST_Expression267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_PostfixExpression"):
                opp_val = getattr(old_value, "JDTAST_PostfixExpression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_PostfixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_PostfixExpression"):
                opp_val = getattr(value, "JDTAST_PostfixExpression", None)
                setattr(value, "JDTAST_PostfixExpression", self)

    @property
    def JDTAST_Expression344(self):
        return self.__JDTAST_Expression344

    @JDTAST_Expression344.setter
    def JDTAST_Expression344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression344", None)
        self.__JDTAST_Expression344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IfStatement343"):
                opp_val = getattr(old_value, "JDTAST_IfStatement343", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IfStatement343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IfStatement343"):
                opp_val = getattr(value, "JDTAST_IfStatement343", None)
                setattr(value, "JDTAST_IfStatement343", self)

    @property
    def JDTAST_Expression231(self):
        return self.__JDTAST_Expression231

    @JDTAST_Expression231.setter
    def JDTAST_Expression231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression231", None)
        self.__JDTAST_Expression231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ConditionalExpression230"):
                opp_val = getattr(old_value, "JDTAST_ConditionalExpression230", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ConditionalExpression230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ConditionalExpression230"):
                opp_val = getattr(value, "JDTAST_ConditionalExpression230", None)
                setattr(value, "JDTAST_ConditionalExpression230", self)

    @property
    def JDTAST_Expression399(self):
        return self.__JDTAST_Expression399

    @JDTAST_Expression399.setter
    def JDTAST_Expression399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression399", None)
        self.__JDTAST_Expression399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_WhileStatement398"):
                opp_val = getattr(old_value, "JDTAST_WhileStatement398", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_WhileStatement398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_WhileStatement398"):
                opp_val = getattr(value, "JDTAST_WhileStatement398", None)
                setattr(value, "JDTAST_WhileStatement398", self)

    @property
    def JDTAST_Expression211(self):
        return self.__JDTAST_Expression211

    @JDTAST_Expression211.setter
    def JDTAST_Expression211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Expression__JDTAST_Expression211", None)
        self.__JDTAST_Expression211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ClassInstanceCreation"):
                opp_val = getattr(old_value, "JDTAST_ClassInstanceCreation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ClassInstanceCreation"):
                opp_val = getattr(value, "JDTAST_ClassInstanceCreation", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ClassInstanceCreation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, JDTAST_MethodRefParameter: "JDTAST_MethodRef" = None, JDTAST_MethodRefParameter92: "JDTAST_SimpleName" = None, JDTAST_MethodRefParameter95: "JDTAST_Type" = None):
        self.varargs = varargs
        self.JDTAST_MethodRefParameter = JDTAST_MethodRefParameter
        self.JDTAST_MethodRefParameter92 = JDTAST_MethodRefParameter92
        self.JDTAST_MethodRefParameter95 = JDTAST_MethodRefParameter95
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def JDTAST_MethodRefParameter(self):
        return self.__JDTAST_MethodRefParameter

    @JDTAST_MethodRefParameter.setter
    def JDTAST_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodRefParameter__JDTAST_MethodRefParameter", None)
        self.__JDTAST_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodRef90"):
                opp_val = getattr(old_value, "JDTAST_MethodRef90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodRef90"):
                opp_val = getattr(value, "JDTAST_MethodRef90", None)
                if opp_val is None:
                    setattr(value, "JDTAST_MethodRef90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_MethodRefParameter95(self):
        return self.__JDTAST_MethodRefParameter95

    @JDTAST_MethodRefParameter95.setter
    def JDTAST_MethodRefParameter95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodRefParameter__JDTAST_MethodRefParameter95", None)
        self.__JDTAST_MethodRefParameter95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type"):
                opp_val = getattr(old_value, "JDTAST_Type", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type"):
                opp_val = getattr(value, "JDTAST_Type", None)
                setattr(value, "JDTAST_Type", self)

    @property
    def JDTAST_MethodRefParameter92(self):
        return self.__JDTAST_MethodRefParameter92

    @JDTAST_MethodRefParameter92.setter
    def JDTAST_MethodRefParameter92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_MethodRefParameter__JDTAST_MethodRefParameter92", None)
        self.__JDTAST_MethodRefParameter92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SimpleName93"):
                opp_val = getattr(old_value, "JDTAST_SimpleName93", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SimpleName93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SimpleName93"):
                opp_val = getattr(value, "JDTAST_SimpleName93", None)
                setattr(value, "JDTAST_SimpleName93", self)

class JDTAST_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, JDTAST_ImportDeclaration: "JDTAST_CompilationUnit" = None, JDTAST_ImportDeclaration74: "JDTAST_Name" = None):
        self.onDemand = onDemand
        self.static = static
        self.JDTAST_ImportDeclaration = JDTAST_ImportDeclaration
        self.JDTAST_ImportDeclaration74 = JDTAST_ImportDeclaration74
        
    @property
    def onDemand(self) -> str:
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: str):
        self.__onDemand = onDemand

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def JDTAST_ImportDeclaration(self):
        return self.__JDTAST_ImportDeclaration

    @JDTAST_ImportDeclaration.setter
    def JDTAST_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ImportDeclaration__JDTAST_ImportDeclaration", None)
        self.__JDTAST_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_CompilationUnit68"):
                opp_val = getattr(old_value, "JDTAST_CompilationUnit68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_CompilationUnit68"):
                opp_val = getattr(value, "JDTAST_CompilationUnit68", None)
                if opp_val is None:
                    setattr(value, "JDTAST_CompilationUnit68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_ImportDeclaration74(self):
        return self.__JDTAST_ImportDeclaration74

    @JDTAST_ImportDeclaration74.setter
    def JDTAST_ImportDeclaration74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ImportDeclaration__JDTAST_ImportDeclaration74", None)
        self.__JDTAST_ImportDeclaration74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Name"):
                opp_val = getattr(old_value, "JDTAST_Name", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Name"):
                opp_val = getattr(value, "JDTAST_Name", None)
                setattr(value, "JDTAST_Name", self)

class JDTAST_Statement(ASTNode):

    pass
class JDTAST_MemberRef(ASTNode):

    pass
class JDTAST_TagElement(ASTNode):

    def __init__(self, nested: str, tagName: str, JDTAST_TagElement: set["JDTAST_ASTNode"] = None, JDTAST_TagElement182: "JDTAST_Javadoc" = None):
        self.nested = nested
        self.tagName = tagName
        self.JDTAST_TagElement = JDTAST_TagElement if JDTAST_TagElement is not None else set()
        self.JDTAST_TagElement182 = JDTAST_TagElement182
        
    @property
    def nested(self) -> str:
        return self.__nested

    @nested.setter
    def nested(self, nested: str):
        self.__nested = nested

    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def JDTAST_TagElement(self):
        return self.__JDTAST_TagElement

    @JDTAST_TagElement.setter
    def JDTAST_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_TagElement__JDTAST_TagElement", None)
        self.__JDTAST_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_ASTNode108"):
                    opp_val = getattr(item, "JDTAST_ASTNode108", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_ASTNode108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_ASTNode108"):
                    opp_val = getattr(item, "JDTAST_ASTNode108", None)
                    
                    setattr(item, "JDTAST_ASTNode108", self)
                    

    @property
    def JDTAST_TagElement182(self):
        return self.__JDTAST_TagElement182

    @JDTAST_TagElement182.setter
    def JDTAST_TagElement182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_TagElement__JDTAST_TagElement182", None)
        self.__JDTAST_TagElement182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Javadoc181"):
                opp_val = getattr(old_value, "JDTAST_Javadoc181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Javadoc181"):
                opp_val = getattr(value, "JDTAST_Javadoc181", None)
                if opp_val is None:
                    setattr(value, "JDTAST_Javadoc181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_MethodRef(ASTNode):

    pass
class JDTAST_Type(ASTNode):

    pass
class JDTAST_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class JDTAST_PackageDeclaration(ASTNode):

    pass
class JDTAST_MemberValuePair(ASTNode):

    pass
class JDTAST_Modifier(ASTNode, ExtendedModifier):

    def __init__(self, abstract: str, final: str, native: str, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str):
        self.abstract = abstract
        self.final = final
        self.native = native
        self.none = none
        self.private = private
        self.protected = protected
        self.public = public
        self.static = static
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.transient = transient
        self.volatile = volatile
        
    @property
    def strictfp(self) -> str:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def native(self) -> str:
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native

    @property
    def none(self) -> str:
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none

    @property
    def synchronized(self) -> str:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def protected(self) -> str:
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected

    @property
    def private(self) -> str:
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def transient(self) -> str:
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def public(self) -> str:
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public

class JDTAST_TypeParameter(ASTNode):

    pass
class JDTAST_BodyDeclaration(ASTNode):

    pass
class JDTAST_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, JDTAST_VariableDeclaration: "JDTAST_Expression" = None, JDTAST_VariableDeclaration117: "JDTAST_SimpleName" = None):
        self.extraDimensions = extraDimensions
        self.JDTAST_VariableDeclaration = JDTAST_VariableDeclaration
        self.JDTAST_VariableDeclaration117 = JDTAST_VariableDeclaration117
        
    @property
    def extraDimensions(self) -> str:
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions

    @property
    def JDTAST_VariableDeclaration(self):
        return self.__JDTAST_VariableDeclaration

    @JDTAST_VariableDeclaration.setter
    def JDTAST_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_VariableDeclaration__JDTAST_VariableDeclaration", None)
        self.__JDTAST_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression115"):
                opp_val = getattr(old_value, "JDTAST_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression115"):
                opp_val = getattr(value, "JDTAST_Expression115", None)
                setattr(value, "JDTAST_Expression115", self)

    @property
    def JDTAST_VariableDeclaration117(self):
        return self.__JDTAST_VariableDeclaration117

    @JDTAST_VariableDeclaration117.setter
    def JDTAST_VariableDeclaration117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_VariableDeclaration__JDTAST_VariableDeclaration117", None)
        self.__JDTAST_VariableDeclaration117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_SimpleName118"):
                opp_val = getattr(old_value, "JDTAST_SimpleName118", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_SimpleName118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_SimpleName118"):
                opp_val = getattr(value, "JDTAST_SimpleName118", None)
                setattr(value, "JDTAST_SimpleName118", self)

class JDTAST_AnonymousClassDeclaration(ASTNode):

    pass
class JDTAST_ASTNode(ABC):

    pass
class JDTAST_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, JDTAST_SingleVariableDeclaration: "JDTAST_CatchClause" = None, JDTAST_SingleVariableDeclaration157: "JDTAST_MethodDeclaration" = None, JDTAST_SingleVariableDeclaration326: "JDTAST_EnhancedForStatement" = None, JDTAST_SingleVariableDeclaration421: "JDTAST_Type" = None, JDTAST_SingleVariableDeclaration424: set["JDTAST_ExtendedModifier"] = None):
        self.varargs = varargs
        self.JDTAST_SingleVariableDeclaration = JDTAST_SingleVariableDeclaration
        self.JDTAST_SingleVariableDeclaration157 = JDTAST_SingleVariableDeclaration157
        self.JDTAST_SingleVariableDeclaration326 = JDTAST_SingleVariableDeclaration326
        self.JDTAST_SingleVariableDeclaration421 = JDTAST_SingleVariableDeclaration421
        self.JDTAST_SingleVariableDeclaration424 = JDTAST_SingleVariableDeclaration424 if JDTAST_SingleVariableDeclaration424 is not None else set()
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def JDTAST_SingleVariableDeclaration326(self):
        return self.__JDTAST_SingleVariableDeclaration326

    @JDTAST_SingleVariableDeclaration326.setter
    def JDTAST_SingleVariableDeclaration326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SingleVariableDeclaration__JDTAST_SingleVariableDeclaration326", None)
        self.__JDTAST_SingleVariableDeclaration326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_EnhancedForStatement325"):
                opp_val = getattr(old_value, "JDTAST_EnhancedForStatement325", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_EnhancedForStatement325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_EnhancedForStatement325"):
                opp_val = getattr(value, "JDTAST_EnhancedForStatement325", None)
                setattr(value, "JDTAST_EnhancedForStatement325", self)

    @property
    def JDTAST_SingleVariableDeclaration157(self):
        return self.__JDTAST_SingleVariableDeclaration157

    @JDTAST_SingleVariableDeclaration157.setter
    def JDTAST_SingleVariableDeclaration157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SingleVariableDeclaration__JDTAST_SingleVariableDeclaration157", None)
        self.__JDTAST_SingleVariableDeclaration157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodDeclaration156"):
                opp_val = getattr(old_value, "JDTAST_MethodDeclaration156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodDeclaration156"):
                opp_val = getattr(value, "JDTAST_MethodDeclaration156", None)
                if opp_val is None:
                    setattr(value, "JDTAST_MethodDeclaration156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_SingleVariableDeclaration421(self):
        return self.__JDTAST_SingleVariableDeclaration421

    @JDTAST_SingleVariableDeclaration421.setter
    def JDTAST_SingleVariableDeclaration421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SingleVariableDeclaration__JDTAST_SingleVariableDeclaration421", None)
        self.__JDTAST_SingleVariableDeclaration421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Type422"):
                opp_val = getattr(old_value, "JDTAST_Type422", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Type422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Type422"):
                opp_val = getattr(value, "JDTAST_Type422", None)
                setattr(value, "JDTAST_Type422", self)

    @property
    def JDTAST_SingleVariableDeclaration424(self):
        return self.__JDTAST_SingleVariableDeclaration424

    @JDTAST_SingleVariableDeclaration424.setter
    def JDTAST_SingleVariableDeclaration424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SingleVariableDeclaration__JDTAST_SingleVariableDeclaration424", None)
        self.__JDTAST_SingleVariableDeclaration424 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_ExtendedModifier425"):
                    opp_val = getattr(item, "JDTAST_ExtendedModifier425", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_ExtendedModifier425", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_ExtendedModifier425"):
                    opp_val = getattr(item, "JDTAST_ExtendedModifier425", None)
                    
                    setattr(item, "JDTAST_ExtendedModifier425", self)
                    

    @property
    def JDTAST_SingleVariableDeclaration(self):
        return self.__JDTAST_SingleVariableDeclaration

    @JDTAST_SingleVariableDeclaration.setter
    def JDTAST_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_SingleVariableDeclaration__JDTAST_SingleVariableDeclaration", None)
        self.__JDTAST_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_CatchClause59"):
                opp_val = getattr(old_value, "JDTAST_CatchClause59", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_CatchClause59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_CatchClause59"):
                opp_val = getattr(value, "JDTAST_CatchClause59", None)
                setattr(value, "JDTAST_CatchClause59", self)

class JDTAST_Block(Statement):

    pass
class JDTAST_CatchClause(ASTNode):

    pass
class JDTAST_Javadoc(Comment):

    pass
class JDTAST_ExtendedModifier(ABC):

    pass
class JDTAST_AST:

    pass
class JDTAST_Parameter:

    def __init__(self, name: str, type: str, JDTAST_Parameter: "JDTAST_IMethod" = None):
        self.name = name
        self.type = type
        self.JDTAST_Parameter = JDTAST_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JDTAST_Parameter(self):
        return self.__JDTAST_Parameter

    @JDTAST_Parameter.setter
    def JDTAST_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_Parameter__JDTAST_Parameter", None)
        self.__JDTAST_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IMethod50"):
                opp_val = getattr(old_value, "JDTAST_IMethod50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IMethod50"):
                opp_val = getattr(value, "JDTAST_IMethod50", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IMethod50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IMember:

    pass
class JDTAST_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, JDTAST_IMethod: "JDTAST_IType" = None, JDTAST_IMethod50: set["JDTAST_Parameter"] = None, JDTAST_IMethod166: "JDTAST_MethodDeclaration" = None, JDTAST_IMethod263: "JDTAST_MethodInvocation" = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.JDTAST_IMethod = JDTAST_IMethod
        self.JDTAST_IMethod50 = JDTAST_IMethod50 if JDTAST_IMethod50 is not None else set()
        self.JDTAST_IMethod166 = JDTAST_IMethod166
        self.JDTAST_IMethod263 = JDTAST_IMethod263
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def isConstructor(self) -> str:
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor

    @property
    def isMainMethod(self) -> str:
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod

    @property
    def exceptionTypes(self) -> str:
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes

    @property
    def JDTAST_IMethod(self):
        return self.__JDTAST_IMethod

    @JDTAST_IMethod.setter
    def JDTAST_IMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IMethod__JDTAST_IMethod", None)
        self.__JDTAST_IMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType43"):
                opp_val = getattr(old_value, "JDTAST_IType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType43"):
                opp_val = getattr(value, "JDTAST_IType43", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_IMethod263(self):
        return self.__JDTAST_IMethod263

    @JDTAST_IMethod263.setter
    def JDTAST_IMethod263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IMethod__JDTAST_IMethod263", None)
        self.__JDTAST_IMethod263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodInvocation262"):
                opp_val = getattr(old_value, "JDTAST_MethodInvocation262", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodInvocation262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodInvocation262"):
                opp_val = getattr(value, "JDTAST_MethodInvocation262", None)
                setattr(value, "JDTAST_MethodInvocation262", self)

    @property
    def JDTAST_IMethod166(self):
        return self.__JDTAST_IMethod166

    @JDTAST_IMethod166.setter
    def JDTAST_IMethod166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IMethod__JDTAST_IMethod166", None)
        self.__JDTAST_IMethod166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_MethodDeclaration165"):
                opp_val = getattr(old_value, "JDTAST_MethodDeclaration165", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_MethodDeclaration165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_MethodDeclaration165"):
                opp_val = getattr(value, "JDTAST_MethodDeclaration165", None)
                setattr(value, "JDTAST_MethodDeclaration165", self)

    @property
    def JDTAST_IMethod50(self):
        return self.__JDTAST_IMethod50

    @JDTAST_IMethod50.setter
    def JDTAST_IMethod50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IMethod__JDTAST_IMethod50", None)
        self.__JDTAST_IMethod50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_Parameter"):
                    opp_val = getattr(item, "JDTAST_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_Parameter"):
                    opp_val = getattr(item, "JDTAST_Parameter", None)
                    
                    setattr(item, "JDTAST_Parameter", self)
                    

class JDTAST_IField(IMember):

    def __init__(self, isTransient: str, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, JDTAST_IField: "JDTAST_IType" = None):
        self.isTransient = isTransient
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.JDTAST_IField = JDTAST_IField
        
    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def typeSignature(self) -> str:
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature

    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

    @property
    def isEnumConstant(self) -> str:
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant

    @property
    def JDTAST_IField(self):
        return self.__JDTAST_IField

    @JDTAST_IField.setter
    def JDTAST_IField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IField__JDTAST_IField", None)
        self.__JDTAST_IField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType41"):
                opp_val = getattr(old_value, "JDTAST_IType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType41"):
                opp_val = getattr(value, "JDTAST_IType41", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_IInitializer(IMember):

    pass
class JDTAST_ISourceRange:

    def __init__(self, length: str, offset: str, JDTAST_ISourceRange: "JDTAST_ISourceReference" = None, JDTAST_ISourceRange34: "JDTAST_IMember" = None, JDTAST_ISourceRange37: "JDTAST_IMember" = None):
        self.length = length
        self.offset = offset
        self.JDTAST_ISourceRange = JDTAST_ISourceRange
        self.JDTAST_ISourceRange34 = JDTAST_ISourceRange34
        self.JDTAST_ISourceRange37 = JDTAST_ISourceRange37
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def JDTAST_ISourceRange(self):
        return self.__JDTAST_ISourceRange

    @JDTAST_ISourceRange.setter
    def JDTAST_ISourceRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ISourceRange__JDTAST_ISourceRange", None)
        self.__JDTAST_ISourceRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ISourceReference"):
                opp_val = getattr(old_value, "JDTAST_ISourceReference", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ISourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ISourceReference"):
                opp_val = getattr(value, "JDTAST_ISourceReference", None)
                setattr(value, "JDTAST_ISourceReference", self)

    @property
    def JDTAST_ISourceRange34(self):
        return self.__JDTAST_ISourceRange34

    @JDTAST_ISourceRange34.setter
    def JDTAST_ISourceRange34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ISourceRange__JDTAST_ISourceRange34", None)
        self.__JDTAST_ISourceRange34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IMember"):
                opp_val = getattr(old_value, "JDTAST_IMember", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IMember"):
                opp_val = getattr(value, "JDTAST_IMember", None)
                setattr(value, "JDTAST_IMember", self)

    @property
    def JDTAST_ISourceRange37(self):
        return self.__JDTAST_ISourceRange37

    @JDTAST_ISourceRange37.setter
    def JDTAST_ISourceRange37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ISourceRange__JDTAST_ISourceRange37", None)
        self.__JDTAST_ISourceRange37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IMember36"):
                opp_val = getattr(old_value, "JDTAST_IMember36", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IMember36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IMember36"):
                opp_val = getattr(value, "JDTAST_IMember36", None)
                setattr(value, "JDTAST_IMember36", self)

class JDTAST_ISourceReference(ABC):

    def __init__(self, source: str, JDTAST_ISourceReference: "JDTAST_ISourceRange" = None):
        self.source = source
        self.JDTAST_ISourceReference = JDTAST_ISourceReference
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def JDTAST_ISourceReference(self):
        return self.__JDTAST_ISourceReference

    @JDTAST_ISourceReference.setter
    def JDTAST_ISourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ISourceReference__JDTAST_ISourceReference", None)
        self.__JDTAST_ISourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ISourceRange"):
                opp_val = getattr(old_value, "JDTAST_ISourceRange", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_ISourceRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ISourceRange"):
                opp_val = getattr(value, "JDTAST_ISourceRange", None)
                setattr(value, "JDTAST_ISourceRange", self)

class ISourceReference:

    pass
class JDTAST_CompilationUnit(ASTNode):

    pass
class JDTAST_IType(IMember):

    def __init__(self, fullyQualifiedParametrizedName: str, fullyQualifiedName: str, JDTAST_IType: "JDTAST_ICompilationUnit" = None, JDTAST_IType23: "JDTAST_ICompilationUnit" = None, JDTAST_IType31: "JDTAST_IClassFile" = None, JDTAST_IType39: set["JDTAST_IInitializer"] = None, JDTAST_IType41: set["JDTAST_IField"] = None, JDTAST_IType43: set["JDTAST_IMethod"] = None, JDTAST_IType46: "JDTAST_IType" = None, JDTAST_IType44: set["JDTAST_IType"] = None, JDTAST_IType48: set["JDTAST_ITypeParameter"] = None, JDTAST_IType72: "JDTAST_Expression" = None):
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.fullyQualifiedName = fullyQualifiedName
        self.JDTAST_IType = JDTAST_IType
        self.JDTAST_IType23 = JDTAST_IType23
        self.JDTAST_IType31 = JDTAST_IType31
        self.JDTAST_IType39 = JDTAST_IType39 if JDTAST_IType39 is not None else set()
        self.JDTAST_IType41 = JDTAST_IType41 if JDTAST_IType41 is not None else set()
        self.JDTAST_IType43 = JDTAST_IType43 if JDTAST_IType43 is not None else set()
        self.JDTAST_IType46 = JDTAST_IType46
        self.JDTAST_IType44 = JDTAST_IType44 if JDTAST_IType44 is not None else set()
        self.JDTAST_IType48 = JDTAST_IType48 if JDTAST_IType48 is not None else set()
        self.JDTAST_IType72 = JDTAST_IType72
        
    @property
    def fullyQualifiedParametrizedName(self) -> str:
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName

    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def JDTAST_IType23(self):
        return self.__JDTAST_IType23

    @JDTAST_IType23.setter
    def JDTAST_IType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType23", None)
        self.__JDTAST_IType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ICompilationUnit22"):
                opp_val = getattr(old_value, "JDTAST_ICompilationUnit22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ICompilationUnit22"):
                opp_val = getattr(value, "JDTAST_ICompilationUnit22", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ICompilationUnit22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_IType72(self):
        return self.__JDTAST_IType72

    @JDTAST_IType72.setter
    def JDTAST_IType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType72", None)
        self.__JDTAST_IType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_Expression"):
                opp_val = getattr(old_value, "JDTAST_Expression", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_Expression"):
                opp_val = getattr(value, "JDTAST_Expression", None)
                setattr(value, "JDTAST_Expression", self)

    @property
    def JDTAST_IType48(self):
        return self.__JDTAST_IType48

    @JDTAST_IType48.setter
    def JDTAST_IType48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType48", None)
        self.__JDTAST_IType48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_ITypeParameter"):
                    opp_val = getattr(item, "JDTAST_ITypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_ITypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_ITypeParameter"):
                    opp_val = getattr(item, "JDTAST_ITypeParameter", None)
                    
                    setattr(item, "JDTAST_ITypeParameter", self)
                    

    @property
    def JDTAST_IType31(self):
        return self.__JDTAST_IType31

    @JDTAST_IType31.setter
    def JDTAST_IType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType31", None)
        self.__JDTAST_IType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IClassFile30"):
                opp_val = getattr(old_value, "JDTAST_IClassFile30", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IClassFile30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IClassFile30"):
                opp_val = getattr(value, "JDTAST_IClassFile30", None)
                setattr(value, "JDTAST_IClassFile30", self)

    @property
    def JDTAST_IType44(self):
        return self.__JDTAST_IType44

    @JDTAST_IType44.setter
    def JDTAST_IType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType44", None)
        self.__JDTAST_IType44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_IType46"):
                    opp_val = getattr(item, "JDTAST_IType46", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_IType46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_IType46"):
                    opp_val = getattr(item, "JDTAST_IType46", None)
                    
                    setattr(item, "JDTAST_IType46", self)
                    

    @property
    def JDTAST_IType(self):
        return self.__JDTAST_IType

    @JDTAST_IType.setter
    def JDTAST_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType", None)
        self.__JDTAST_IType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ICompilationUnit18"):
                opp_val = getattr(old_value, "JDTAST_ICompilationUnit18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ICompilationUnit18"):
                opp_val = getattr(value, "JDTAST_ICompilationUnit18", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ICompilationUnit18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_IType46(self):
        return self.__JDTAST_IType46

    @JDTAST_IType46.setter
    def JDTAST_IType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType46", None)
        self.__JDTAST_IType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType44"):
                opp_val = getattr(old_value, "JDTAST_IType44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType44"):
                opp_val = getattr(value, "JDTAST_IType44", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IType44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTAST_IType41(self):
        return self.__JDTAST_IType41

    @JDTAST_IType41.setter
    def JDTAST_IType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType41", None)
        self.__JDTAST_IType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_IField"):
                    opp_val = getattr(item, "JDTAST_IField", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_IField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_IField"):
                    opp_val = getattr(item, "JDTAST_IField", None)
                    
                    setattr(item, "JDTAST_IField", self)
                    

    @property
    def JDTAST_IType43(self):
        return self.__JDTAST_IType43

    @JDTAST_IType43.setter
    def JDTAST_IType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType43", None)
        self.__JDTAST_IType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_IMethod"):
                    opp_val = getattr(item, "JDTAST_IMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_IMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_IMethod"):
                    opp_val = getattr(item, "JDTAST_IMethod", None)
                    
                    setattr(item, "JDTAST_IMethod", self)
                    

    @property
    def JDTAST_IType39(self):
        return self.__JDTAST_IType39

    @JDTAST_IType39.setter
    def JDTAST_IType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IType__JDTAST_IType39", None)
        self.__JDTAST_IType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_IInitializer"):
                    opp_val = getattr(item, "JDTAST_IInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_IInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_IInitializer"):
                    opp_val = getattr(item, "JDTAST_IInitializer", None)
                    
                    setattr(item, "JDTAST_IInitializer", self)
                    

class ITypeRoot:

    pass
class JDTAST_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, JDTAST_IClassFile: "JDTAST_IPackageFragment" = None, JDTAST_IClassFile30: "JDTAST_IType" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.JDTAST_IClassFile = JDTAST_IClassFile
        self.JDTAST_IClassFile30 = JDTAST_IClassFile30
        
    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def isClass(self) -> str:
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass

    @property
    def JDTAST_IClassFile30(self):
        return self.__JDTAST_IClassFile30

    @JDTAST_IClassFile30.setter
    def JDTAST_IClassFile30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IClassFile__JDTAST_IClassFile30", None)
        self.__JDTAST_IClassFile30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType31"):
                opp_val = getattr(old_value, "JDTAST_IType31", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_IType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType31"):
                opp_val = getattr(value, "JDTAST_IType31", None)
                setattr(value, "JDTAST_IType31", self)

    @property
    def JDTAST_IClassFile(self):
        return self.__JDTAST_IClassFile

    @JDTAST_IClassFile.setter
    def JDTAST_IClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IClassFile__JDTAST_IClassFile", None)
        self.__JDTAST_IClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IPackageFragment"):
                opp_val = getattr(old_value, "JDTAST_IPackageFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IPackageFragment"):
                opp_val = getattr(value, "JDTAST_IPackageFragment", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IPackageFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_ICompilationUnit(ITypeRoot):

    pass
class IJavaElement:

    pass
class JDTAST_IMember(IJavaElement, ISourceReference):

    pass
class JDTAST_ITypeParameter(IJavaElement, ISourceReference):

    def __init__(self, bounds: str, JDTAST_ITypeParameter: "JDTAST_IType" = None):
        self.bounds = bounds
        self.JDTAST_ITypeParameter = JDTAST_ITypeParameter
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def JDTAST_ITypeParameter(self):
        return self.__JDTAST_ITypeParameter

    @JDTAST_ITypeParameter.setter
    def JDTAST_ITypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_ITypeParameter__JDTAST_ITypeParameter", None)
        self.__JDTAST_ITypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_IType48"):
                opp_val = getattr(old_value, "JDTAST_IType48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_IType48"):
                opp_val = getattr(value, "JDTAST_IType48", None)
                if opp_val is None:
                    setattr(value, "JDTAST_IType48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_IImportDeclaration(IJavaElement, ISourceReference):

    def __init__(self, isOnDemand: str, isStatic: str, JDTAST_IImportDeclaration: "JDTAST_ICompilationUnit" = None):
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        self.JDTAST_IImportDeclaration = JDTAST_IImportDeclaration
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def isOnDemand(self) -> str:
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand

    @property
    def JDTAST_IImportDeclaration(self):
        return self.__JDTAST_IImportDeclaration

    @JDTAST_IImportDeclaration.setter
    def JDTAST_IImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IImportDeclaration__JDTAST_IImportDeclaration", None)
        self.__JDTAST_IImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_ICompilationUnit20"):
                opp_val = getattr(old_value, "JDTAST_ICompilationUnit20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_ICompilationUnit20"):
                opp_val = getattr(value, "JDTAST_ICompilationUnit20", None)
                if opp_val is None:
                    setattr(value, "JDTAST_ICompilationUnit20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IPackageFragmentRoot:

    pass
class JDTAST_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class JDTAST_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class JDTAST_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

class PhysicalElement:

    pass
class JDTAST_ITypeRoot(IJavaElement, PhysicalElement, ISourceReference):

    pass
class JDTAST_IPackageFragmentRoot(IJavaElement, PhysicalElement):

    pass
class JDTAST_IJavaProject(IJavaElement, PhysicalElement):

    pass
class JDTAST_IPackageFragment(IJavaElement, PhysicalElement):

    def __init__(self, isDefaultPackage: str, IPackageFragment: "JDTAST_IPackageFragmentRoot" = None, packageFragments: "JDTAST_IPackageFragmentRoot" = None, JDTAST_IPackageFragment: set["JDTAST_IClassFile"] = None, JDTAST_IPackageFragment16: set["JDTAST_ICompilationUnit"] = None, JDTAST_IPackageFragment106: "JDTAST_PackageDeclaration" = None):
        self.isDefaultPackage = isDefaultPackage
        self.IPackageFragment = IPackageFragment
        self.packageFragments = packageFragments
        self.JDTAST_IPackageFragment = JDTAST_IPackageFragment if JDTAST_IPackageFragment is not None else set()
        self.JDTAST_IPackageFragment16 = JDTAST_IPackageFragment16 if JDTAST_IPackageFragment16 is not None else set()
        self.JDTAST_IPackageFragment106 = JDTAST_IPackageFragment106
        
    @property
    def isDefaultPackage(self) -> str:
        return self.__isDefaultPackage

    @isDefaultPackage.setter
    def isDefaultPackage(self, isDefaultPackage: str):
        self.__isDefaultPackage = isDefaultPackage

    @property
    def packageFragments(self):
        return self.__packageFragments

    @packageFragments.setter
    def packageFragments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IPackageFragment__packageFragments", None)
        self.__packageFragments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IPackageFragmentRoot"):
                opp_val = getattr(old_value, "IPackageFragmentRoot", None)
                if opp_val == self:
                    setattr(old_value, "IPackageFragmentRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IPackageFragmentRoot"):
                opp_val = getattr(value, "IPackageFragmentRoot", None)
                setattr(value, "IPackageFragmentRoot", self)

    @property
    def JDTAST_IPackageFragment(self):
        return self.__JDTAST_IPackageFragment

    @JDTAST_IPackageFragment.setter
    def JDTAST_IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IPackageFragment__JDTAST_IPackageFragment", None)
        self.__JDTAST_IPackageFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_IClassFile"):
                    opp_val = getattr(item, "JDTAST_IClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_IClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_IClassFile"):
                    opp_val = getattr(item, "JDTAST_IClassFile", None)
                    
                    setattr(item, "JDTAST_IClassFile", self)
                    

    @property
    def JDTAST_IPackageFragment16(self):
        return self.__JDTAST_IPackageFragment16

    @JDTAST_IPackageFragment16.setter
    def JDTAST_IPackageFragment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IPackageFragment__JDTAST_IPackageFragment16", None)
        self.__JDTAST_IPackageFragment16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTAST_ICompilationUnit"):
                    opp_val = getattr(item, "JDTAST_ICompilationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTAST_ICompilationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTAST_ICompilationUnit"):
                    opp_val = getattr(item, "JDTAST_ICompilationUnit", None)
                    
                    setattr(item, "JDTAST_ICompilationUnit", self)
                    

    @property
    def JDTAST_IPackageFragment106(self):
        return self.__JDTAST_IPackageFragment106

    @JDTAST_IPackageFragment106.setter
    def JDTAST_IPackageFragment106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IPackageFragment__JDTAST_IPackageFragment106", None)
        self.__JDTAST_IPackageFragment106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTAST_PackageDeclaration105"):
                opp_val = getattr(old_value, "JDTAST_PackageDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "JDTAST_PackageDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTAST_PackageDeclaration105"):
                opp_val = getattr(value, "JDTAST_PackageDeclaration105", None)
                setattr(value, "JDTAST_PackageDeclaration105", self)

    @property
    def IPackageFragment(self):
        return self.__IPackageFragment

    @IPackageFragment.setter
    def IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JDTAST_IPackageFragment__IPackageFragment", None)
        self.__IPackageFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageFragmentRoot"):
                opp_val = getattr(old_value, "packageFragmentRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageFragmentRoot"):
                opp_val = getattr(value, "packageFragmentRoot", None)
                if opp_val is None:
                    setattr(value, "packageFragmentRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JDTAST_IJavaModel(PhysicalElement):

    pass
class JDTAST_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path
