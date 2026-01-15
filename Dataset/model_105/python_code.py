from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InfixExpressionOperatorKind(Enum):
    or = "or"
    right_shift_signed = "right_shift_signed"
    minus = "minus"
    xor = "xor"
    less_equals = "less_equals"
    equals = "equals"
    not_equals = "not_equals"
    and = "and"
    plus = "plus"
    greater_equals = "greater_equals"
    greater = "greater"
    conditional_or = "conditional_or"
    remainder = "remainder"
    less = "less"
    left_shift = "left_shift"
    right_shift_unsigned = "right_shift_unsigned"
    conditional_and = "conditional_and"
    times = "times"
    divide = "divide"
class PrefixExpressionOperatorKind(Enum):
    minus = "minus"
    not = "not"
    decrement = "decrement"
    complement = "complement"
    increment = "increment"
    plus = "plus"
class AssignmentOperatorKind(Enum):
    plus_assign = "plus_assign"
    assign = "assign"
    right_shift_unsigned_assign = "right_shift_unsigned_assign"
    remainder_assign = "remainder_assign"
    bit_and_assign = "bit_and_assign"
    left_shift_assign = "left_shift_assign"
    right_shift_signed_assign = "right_shift_signed_assign"
    bit_xor_assign = "bit_xor_assign"
    times_assign = "times_assign"
    divide_assign = "divide_assign"
    minus_assign = "minus_assign"
    bit_or_assign = "bit_or_assign"
class PostfixExpressionOperatorKind(Enum):
    increment = "increment"
    decrement = "decrement"


############################################
# Definition of Classes
############################################

class Name:

    pass
class DOM_QualifiedName(Name):

    pass
class Annotation:

    pass
class DOM_NormalAnnotation(Annotation):

    pass
class DOM_SingleMemberAnnotation(Annotation):

    pass
class DOM_MarkerAnnotation(Annotation):

    pass
class VariableDeclaration:

    pass
class Type:

    pass
class DOM_QualifiedType(Type):

    pass
class DOM_WildcardType(Type):

    def __init__(self, upperBound: str, DOM_WildcardType: "DOM_Type" = None):
        self.upperBound = upperBound
        self.DOM_WildcardType = DOM_WildcardType
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def DOM_WildcardType(self):
        return self.__DOM_WildcardType

    @DOM_WildcardType.setter
    def DOM_WildcardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_WildcardType__DOM_WildcardType", None)
        self.__DOM_WildcardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type364"):
                opp_val = getattr(old_value, "DOM_Type364", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type364"):
                opp_val = getattr(value, "DOM_Type364", None)
                setattr(value, "DOM_Type364", self)

class DOM_SimpleType(Type):

    pass
class DOM_PrimitiveType(Type):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class DOM_ParameterizedType(Type):

    pass
class Statement:

    pass
class DOM_EnhancedForStatement(Statement):

    pass
class DOM_TypeDeclarationStatement(Statement):

    pass
class DOM_ThrowStatement(Statement):

    pass
class DOM_LabeledStatement(Statement):

    pass
class DOM_BreakStatement(Statement):

    pass
class DOM_SwitchStatement(Statement):

    pass
class DOM_WhileStatement(Statement):

    pass
class DOM_ForStatement(Statement):

    pass
class DOM_EmptyStatement(Statement):

    pass
class DOM_ContinueStatement(Statement):

    pass
class DOM_SwitchCase(Statement):

    def __init__(self, default: str, DOM_SwitchCase: "DOM_Expression" = None):
        self.default = default
        self.DOM_SwitchCase = DOM_SwitchCase
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def DOM_SwitchCase(self):
        return self.__DOM_SwitchCase

    @DOM_SwitchCase.setter
    def DOM_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SwitchCase__DOM_SwitchCase", None)
        self.__DOM_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression309"):
                opp_val = getattr(old_value, "DOM_Expression309", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression309"):
                opp_val = getattr(value, "DOM_Expression309", None)
                setattr(value, "DOM_Expression309", self)

class DOM_SynchronizedStatement(Statement):

    pass
class DOM_IfStatement(Statement):

    pass
class DOM_ReturnStatement(Statement):

    pass
class DOM_DoStatement(Statement):

    pass
class DOM_ExpressionStatement(Statement):

    pass
class DOM_TryStatement(Statement):

    pass
class DOM_VariableDeclarationStatement(Statement):

    pass
class DOM_SuperConstructorInvocation(Statement):

    pass
class DOM_AssertStatement(Statement):

    pass
class DOM_ConstructorInvocation(Statement):

    pass
class DOM_ArrayType(Type):

    def __init__(self, dimensions: str, DOM_ArrayType: "DOM_ArrayCreation" = None, DOM_ArrayType346: "DOM_Type" = None, DOM_ArrayType349: "DOM_Type" = None):
        self.dimensions = dimensions
        self.DOM_ArrayType = DOM_ArrayType
        self.DOM_ArrayType346 = DOM_ArrayType346
        self.DOM_ArrayType349 = DOM_ArrayType349
        
    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def DOM_ArrayType(self):
        return self.__DOM_ArrayType

    @DOM_ArrayType.setter
    def DOM_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType", None)
        self.__DOM_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ArrayCreation141"):
                opp_val = getattr(old_value, "DOM_ArrayCreation141", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ArrayCreation141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ArrayCreation141"):
                opp_val = getattr(value, "DOM_ArrayCreation141", None)
                setattr(value, "DOM_ArrayCreation141", self)

    @property
    def DOM_ArrayType346(self):
        return self.__DOM_ArrayType346

    @DOM_ArrayType346.setter
    def DOM_ArrayType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType346", None)
        self.__DOM_ArrayType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type347"):
                opp_val = getattr(old_value, "DOM_Type347", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type347"):
                opp_val = getattr(value, "DOM_Type347", None)
                setattr(value, "DOM_Type347", self)

    @property
    def DOM_ArrayType349(self):
        return self.__DOM_ArrayType349

    @DOM_ArrayType349.setter
    def DOM_ArrayType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType349", None)
        self.__DOM_ArrayType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type350"):
                opp_val = getattr(old_value, "DOM_Type350", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type350"):
                opp_val = getattr(value, "DOM_Type350", None)
                setattr(value, "DOM_Type350", self)

class Comment:

    pass
class DOM_BlockComment(Comment):

    pass
class Expression:

    pass
class DOM_Assignment(Expression):

    def __init__(self, operator: str, DOM_Assignment: "DOM_Expression" = None, DOM_Assignment148: "DOM_Expression" = None):
        self.operator = operator
        self.DOM_Assignment = DOM_Assignment
        self.DOM_Assignment148 = DOM_Assignment148
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_Assignment148(self):
        return self.__DOM_Assignment148

    @DOM_Assignment148.setter
    def DOM_Assignment148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Assignment__DOM_Assignment148", None)
        self.__DOM_Assignment148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression149"):
                opp_val = getattr(old_value, "DOM_Expression149", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression149"):
                opp_val = getattr(value, "DOM_Expression149", None)
                setattr(value, "DOM_Expression149", self)

    @property
    def DOM_Assignment(self):
        return self.__DOM_Assignment

    @DOM_Assignment.setter
    def DOM_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Assignment__DOM_Assignment", None)
        self.__DOM_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression146"):
                opp_val = getattr(old_value, "DOM_Expression146", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression146"):
                opp_val = getattr(value, "DOM_Expression146", None)
                setattr(value, "DOM_Expression146", self)

class DOM_PostfixExpression(Expression):

    def __init__(self, operator: str, DOM_PostfixExpression: "DOM_Expression" = None):
        self.operator = operator
        self.DOM_PostfixExpression = DOM_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_PostfixExpression(self):
        return self.__DOM_PostfixExpression

    @DOM_PostfixExpression.setter
    def DOM_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_PostfixExpression__DOM_PostfixExpression", None)
        self.__DOM_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression212"):
                opp_val = getattr(old_value, "DOM_Expression212", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression212"):
                opp_val = getattr(value, "DOM_Expression212", None)
                setattr(value, "DOM_Expression212", self)

class DOM_ArrayInitializer(Expression):

    pass
class DOM_ParenthesizedExpression(Expression):

    pass
class DOM_VariableDeclarationExpression(Expression):

    pass
class DOM_CharacterLiteral(Expression):

    def __init__(self, charValue: str, escapedValue: str):
        self.charValue = charValue
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

    @property
    def charValue(self) -> str:
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue

class DOM_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str):
        self.escapedValue = escapedValue
        self.literalValue = literalValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

class DOM_ConditionalExpression(Expression):

    pass
class DOM_TypeLiteral(Expression):

    pass
class DOM_NullLiteral(Expression):

    pass
class DOM_SuperFieldAccess(Expression):

    pass
class DOM_InfixExpression(Expression):

    def __init__(self, operator: str, DOM_InfixExpression: set["DOM_Expression"] = None, DOM_InfixExpression185: "DOM_Expression" = None, DOM_InfixExpression188: "DOM_Expression" = None):
        self.operator = operator
        self.DOM_InfixExpression = DOM_InfixExpression if DOM_InfixExpression is not None else set()
        self.DOM_InfixExpression185 = DOM_InfixExpression185
        self.DOM_InfixExpression188 = DOM_InfixExpression188
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_InfixExpression(self):
        return self.__DOM_InfixExpression

    @DOM_InfixExpression.setter
    def DOM_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression", None)
        self.__DOM_InfixExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_Expression183"):
                    opp_val = getattr(item, "DOM_Expression183", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_Expression183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_Expression183"):
                    opp_val = getattr(item, "DOM_Expression183", None)
                    
                    setattr(item, "DOM_Expression183", self)
                    

    @property
    def DOM_InfixExpression188(self):
        return self.__DOM_InfixExpression188

    @DOM_InfixExpression188.setter
    def DOM_InfixExpression188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression188", None)
        self.__DOM_InfixExpression188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression189"):
                opp_val = getattr(old_value, "DOM_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression189"):
                opp_val = getattr(value, "DOM_Expression189", None)
                setattr(value, "DOM_Expression189", self)

    @property
    def DOM_InfixExpression185(self):
        return self.__DOM_InfixExpression185

    @DOM_InfixExpression185.setter
    def DOM_InfixExpression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression185", None)
        self.__DOM_InfixExpression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression186"):
                opp_val = getattr(old_value, "DOM_Expression186", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression186"):
                opp_val = getattr(value, "DOM_Expression186", None)
                setattr(value, "DOM_Expression186", self)

class DOM_FieldAccess(Expression):

    pass
class DOM_PrefixExpression(Expression):

    def __init__(self, operator: str, DOM_PrefixExpression: "DOM_Expression" = None):
        self.operator = operator
        self.DOM_PrefixExpression = DOM_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_PrefixExpression(self):
        return self.__DOM_PrefixExpression

    @DOM_PrefixExpression.setter
    def DOM_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_PrefixExpression__DOM_PrefixExpression", None)
        self.__DOM_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression214"):
                opp_val = getattr(old_value, "DOM_Expression214", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression214"):
                opp_val = getattr(value, "DOM_Expression214", None)
                setattr(value, "DOM_Expression214", self)

class DOM_CastExpression(Expression):

    pass
class DOM_InstanceofExpression(Expression):

    pass
class DOM_ClassInstanceCreation(Expression):

    pass
class DOM_ArrayAccess(Expression):

    pass
class DOM_MethodInvocation(Expression):

    pass
class DOM_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> str:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue

class DOM_ArrayCreation(Expression):

    pass
class DOM_ThisExpression(Expression):

    pass
class DOM_NumberLiteral(Expression):

    def __init__(self, token: str):
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

class DOM_SuperMethodInvocation(Expression):

    pass
class DOM_LineComment(Comment):

    pass
class DOM_IMethod:

    pass
class AbstractTypeDeclaration:

    pass
class DOM_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, DOM_TypeDeclaration: "DOM_Type" = None, DOM_TypeDeclaration120: set["DOM_Type"] = None, DOM_TypeDeclaration123: set["DOM_TypeParameter"] = None):
        self.interface = interface
        self.DOM_TypeDeclaration = DOM_TypeDeclaration
        self.DOM_TypeDeclaration120 = DOM_TypeDeclaration120 if DOM_TypeDeclaration120 is not None else set()
        self.DOM_TypeDeclaration123 = DOM_TypeDeclaration123 if DOM_TypeDeclaration123 is not None else set()
        
    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def DOM_TypeDeclaration120(self):
        return self.__DOM_TypeDeclaration120

    @DOM_TypeDeclaration120.setter
    def DOM_TypeDeclaration120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration120", None)
        self.__DOM_TypeDeclaration120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_Type121"):
                    opp_val = getattr(item, "DOM_Type121", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_Type121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_Type121"):
                    opp_val = getattr(item, "DOM_Type121", None)
                    
                    setattr(item, "DOM_Type121", self)
                    

    @property
    def DOM_TypeDeclaration123(self):
        return self.__DOM_TypeDeclaration123

    @DOM_TypeDeclaration123.setter
    def DOM_TypeDeclaration123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration123", None)
        self.__DOM_TypeDeclaration123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_TypeParameter124"):
                    opp_val = getattr(item, "DOM_TypeParameter124", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_TypeParameter124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_TypeParameter124"):
                    opp_val = getattr(item, "DOM_TypeParameter124", None)
                    
                    setattr(item, "DOM_TypeParameter124", self)
                    

    @property
    def DOM_TypeDeclaration(self):
        return self.__DOM_TypeDeclaration

    @DOM_TypeDeclaration.setter
    def DOM_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration", None)
        self.__DOM_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type118"):
                opp_val = getattr(old_value, "DOM_Type118", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type118"):
                opp_val = getattr(value, "DOM_Type118", None)
                setattr(value, "DOM_Type118", self)

class DOM_EnumDeclaration(AbstractTypeDeclaration):

    pass
class DOM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class DOM_VariableDeclarationFragment(VariableDeclaration):

    pass
class BodyDeclaration:

    pass
class DOM_EnumConstantDeclaration(BodyDeclaration):

    pass
class DOM_Initializer(BodyDeclaration):

    pass
class DOM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class DOM_FieldDeclaration(BodyDeclaration):

    pass
class DOM_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, DOM_MethodDeclaration: "DOM_Block" = None, DOM_MethodDeclaration96: "DOM_SimpleName" = None, DOM_MethodDeclaration99: "DOM_Type" = None, DOM_MethodDeclaration111: "DOM_IMethod" = None, DOM_MethodDeclaration102: set["DOM_SingleVariableDeclaration"] = None, DOM_MethodDeclaration105: set["DOM_Name"] = None, DOM_MethodDeclaration108: set["DOM_TypeParameter"] = None):
        self.extraDimensions = extraDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.DOM_MethodDeclaration = DOM_MethodDeclaration
        self.DOM_MethodDeclaration96 = DOM_MethodDeclaration96
        self.DOM_MethodDeclaration99 = DOM_MethodDeclaration99
        self.DOM_MethodDeclaration111 = DOM_MethodDeclaration111
        self.DOM_MethodDeclaration102 = DOM_MethodDeclaration102 if DOM_MethodDeclaration102 is not None else set()
        self.DOM_MethodDeclaration105 = DOM_MethodDeclaration105 if DOM_MethodDeclaration105 is not None else set()
        self.DOM_MethodDeclaration108 = DOM_MethodDeclaration108 if DOM_MethodDeclaration108 is not None else set()
        
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
    def DOM_MethodDeclaration102(self):
        return self.__DOM_MethodDeclaration102

    @DOM_MethodDeclaration102.setter
    def DOM_MethodDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration102", None)
        self.__DOM_MethodDeclaration102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_SingleVariableDeclaration103"):
                    opp_val = getattr(item, "DOM_SingleVariableDeclaration103", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_SingleVariableDeclaration103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_SingleVariableDeclaration103"):
                    opp_val = getattr(item, "DOM_SingleVariableDeclaration103", None)
                    
                    setattr(item, "DOM_SingleVariableDeclaration103", self)
                    

    @property
    def DOM_MethodDeclaration105(self):
        return self.__DOM_MethodDeclaration105

    @DOM_MethodDeclaration105.setter
    def DOM_MethodDeclaration105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration105", None)
        self.__DOM_MethodDeclaration105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_Name106"):
                    opp_val = getattr(item, "DOM_Name106", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_Name106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_Name106"):
                    opp_val = getattr(item, "DOM_Name106", None)
                    
                    setattr(item, "DOM_Name106", self)
                    

    @property
    def DOM_MethodDeclaration(self):
        return self.__DOM_MethodDeclaration

    @DOM_MethodDeclaration.setter
    def DOM_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration", None)
        self.__DOM_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Block94"):
                opp_val = getattr(old_value, "DOM_Block94", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Block94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Block94"):
                opp_val = getattr(value, "DOM_Block94", None)
                setattr(value, "DOM_Block94", self)

    @property
    def DOM_MethodDeclaration96(self):
        return self.__DOM_MethodDeclaration96

    @DOM_MethodDeclaration96.setter
    def DOM_MethodDeclaration96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration96", None)
        self.__DOM_MethodDeclaration96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SimpleName97"):
                opp_val = getattr(old_value, "DOM_SimpleName97", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SimpleName97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SimpleName97"):
                opp_val = getattr(value, "DOM_SimpleName97", None)
                setattr(value, "DOM_SimpleName97", self)

    @property
    def DOM_MethodDeclaration108(self):
        return self.__DOM_MethodDeclaration108

    @DOM_MethodDeclaration108.setter
    def DOM_MethodDeclaration108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration108", None)
        self.__DOM_MethodDeclaration108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_TypeParameter109"):
                    opp_val = getattr(item, "DOM_TypeParameter109", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_TypeParameter109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_TypeParameter109"):
                    opp_val = getattr(item, "DOM_TypeParameter109", None)
                    
                    setattr(item, "DOM_TypeParameter109", self)
                    

    @property
    def DOM_MethodDeclaration111(self):
        return self.__DOM_MethodDeclaration111

    @DOM_MethodDeclaration111.setter
    def DOM_MethodDeclaration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration111", None)
        self.__DOM_MethodDeclaration111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_IMethod"):
                opp_val = getattr(old_value, "DOM_IMethod", None)
                if opp_val == self:
                    setattr(old_value, "DOM_IMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_IMethod"):
                opp_val = getattr(value, "DOM_IMethod", None)
                setattr(value, "DOM_IMethod", self)

    @property
    def DOM_MethodDeclaration99(self):
        return self.__DOM_MethodDeclaration99

    @DOM_MethodDeclaration99.setter
    def DOM_MethodDeclaration99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration99", None)
        self.__DOM_MethodDeclaration99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type100"):
                opp_val = getattr(old_value, "DOM_Type100", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type100"):
                opp_val = getattr(value, "DOM_Type100", None)
                setattr(value, "DOM_Type100", self)

class DOM_IPackageFragment:

    pass
class ExtendedModifier:

    pass
class DOM_Annotation(ExtendedModifier, Expression):

    pass
class DOM_IType:

    pass
class DOM_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, DOM_SimpleName: "DOM_MemberRef" = None, DOM_SimpleName40: "DOM_MethodRefParameter" = None, DOM_SimpleName27: "DOM_MemberValuePair" = None, DOM_SimpleName32: "DOM_MethodRef" = None, DOM_SimpleName64: "DOM_VariableDeclaration" = None, DOM_SimpleName56: "DOM_TypeParameter" = None, DOM_SimpleName70: "DOM_AbstractTypeDeclaration" = None, DOM_SimpleName86: "DOM_EnumConstantDeclaration" = None, DOM_SimpleName75: "DOM_AnnotationTypeMemberDeclaration" = None, DOM_SimpleName97: "DOM_MethodDeclaration" = None, DOM_SimpleName181: "DOM_FieldAccess" = None, DOM_SimpleName202: "DOM_MethodInvocation" = None, DOM_SimpleName216: "DOM_SuperFieldAccess" = None, DOM_SimpleName251: "DOM_BreakStatement" = None, DOM_SimpleName258: "DOM_ContinueStatement" = None, DOM_SimpleName297: "DOM_LabeledStatement" = None, DOM_SimpleName357: "DOM_QualifiedType" = None, DOM_SimpleName372: "DOM_QualifiedName" = None):
        self.identifier = identifier
        self.declaration = declaration
        self.DOM_SimpleName = DOM_SimpleName
        self.DOM_SimpleName40 = DOM_SimpleName40
        self.DOM_SimpleName27 = DOM_SimpleName27
        self.DOM_SimpleName32 = DOM_SimpleName32
        self.DOM_SimpleName64 = DOM_SimpleName64
        self.DOM_SimpleName56 = DOM_SimpleName56
        self.DOM_SimpleName70 = DOM_SimpleName70
        self.DOM_SimpleName86 = DOM_SimpleName86
        self.DOM_SimpleName75 = DOM_SimpleName75
        self.DOM_SimpleName97 = DOM_SimpleName97
        self.DOM_SimpleName181 = DOM_SimpleName181
        self.DOM_SimpleName202 = DOM_SimpleName202
        self.DOM_SimpleName216 = DOM_SimpleName216
        self.DOM_SimpleName251 = DOM_SimpleName251
        self.DOM_SimpleName258 = DOM_SimpleName258
        self.DOM_SimpleName297 = DOM_SimpleName297
        self.DOM_SimpleName357 = DOM_SimpleName357
        self.DOM_SimpleName372 = DOM_SimpleName372
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def DOM_SimpleName202(self):
        return self.__DOM_SimpleName202

    @DOM_SimpleName202.setter
    def DOM_SimpleName202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName202", None)
        self.__DOM_SimpleName202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodInvocation201"):
                opp_val = getattr(old_value, "DOM_MethodInvocation201", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodInvocation201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodInvocation201"):
                opp_val = getattr(value, "DOM_MethodInvocation201", None)
                setattr(value, "DOM_MethodInvocation201", self)

    @property
    def DOM_SimpleName258(self):
        return self.__DOM_SimpleName258

    @DOM_SimpleName258.setter
    def DOM_SimpleName258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName258", None)
        self.__DOM_SimpleName258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ContinueStatement"):
                opp_val = getattr(old_value, "DOM_ContinueStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ContinueStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ContinueStatement"):
                opp_val = getattr(value, "DOM_ContinueStatement", None)
                setattr(value, "DOM_ContinueStatement", self)

    @property
    def DOM_SimpleName(self):
        return self.__DOM_SimpleName

    @DOM_SimpleName.setter
    def DOM_SimpleName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName", None)
        self.__DOM_SimpleName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MemberRef"):
                opp_val = getattr(old_value, "DOM_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MemberRef"):
                opp_val = getattr(value, "DOM_MemberRef", None)
                setattr(value, "DOM_MemberRef", self)

    @property
    def DOM_SimpleName27(self):
        return self.__DOM_SimpleName27

    @DOM_SimpleName27.setter
    def DOM_SimpleName27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName27", None)
        self.__DOM_SimpleName27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MemberValuePair"):
                opp_val = getattr(old_value, "DOM_MemberValuePair", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MemberValuePair", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MemberValuePair"):
                opp_val = getattr(value, "DOM_MemberValuePair", None)
                setattr(value, "DOM_MemberValuePair", self)

    @property
    def DOM_SimpleName216(self):
        return self.__DOM_SimpleName216

    @DOM_SimpleName216.setter
    def DOM_SimpleName216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName216", None)
        self.__DOM_SimpleName216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperFieldAccess"):
                opp_val = getattr(old_value, "DOM_SuperFieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SuperFieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperFieldAccess"):
                opp_val = getattr(value, "DOM_SuperFieldAccess", None)
                setattr(value, "DOM_SuperFieldAccess", self)

    @property
    def DOM_SimpleName70(self):
        return self.__DOM_SimpleName70

    @DOM_SimpleName70.setter
    def DOM_SimpleName70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName70", None)
        self.__DOM_SimpleName70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_AbstractTypeDeclaration69"):
                opp_val = getattr(old_value, "DOM_AbstractTypeDeclaration69", None)
                if opp_val == self:
                    setattr(old_value, "DOM_AbstractTypeDeclaration69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_AbstractTypeDeclaration69"):
                opp_val = getattr(value, "DOM_AbstractTypeDeclaration69", None)
                setattr(value, "DOM_AbstractTypeDeclaration69", self)

    @property
    def DOM_SimpleName64(self):
        return self.__DOM_SimpleName64

    @DOM_SimpleName64.setter
    def DOM_SimpleName64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName64", None)
        self.__DOM_SimpleName64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_VariableDeclaration63"):
                opp_val = getattr(old_value, "DOM_VariableDeclaration63", None)
                if opp_val == self:
                    setattr(old_value, "DOM_VariableDeclaration63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_VariableDeclaration63"):
                opp_val = getattr(value, "DOM_VariableDeclaration63", None)
                setattr(value, "DOM_VariableDeclaration63", self)

    @property
    def DOM_SimpleName372(self):
        return self.__DOM_SimpleName372

    @DOM_SimpleName372.setter
    def DOM_SimpleName372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName372", None)
        self.__DOM_SimpleName372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_QualifiedName"):
                opp_val = getattr(old_value, "DOM_QualifiedName", None)
                if opp_val == self:
                    setattr(old_value, "DOM_QualifiedName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_QualifiedName"):
                opp_val = getattr(value, "DOM_QualifiedName", None)
                setattr(value, "DOM_QualifiedName", self)

    @property
    def DOM_SimpleName32(self):
        return self.__DOM_SimpleName32

    @DOM_SimpleName32.setter
    def DOM_SimpleName32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName32", None)
        self.__DOM_SimpleName32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodRef"):
                opp_val = getattr(old_value, "DOM_MethodRef", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodRef"):
                opp_val = getattr(value, "DOM_MethodRef", None)
                setattr(value, "DOM_MethodRef", self)

    @property
    def DOM_SimpleName181(self):
        return self.__DOM_SimpleName181

    @DOM_SimpleName181.setter
    def DOM_SimpleName181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName181", None)
        self.__DOM_SimpleName181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_FieldAccess180"):
                opp_val = getattr(old_value, "DOM_FieldAccess180", None)
                if opp_val == self:
                    setattr(old_value, "DOM_FieldAccess180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_FieldAccess180"):
                opp_val = getattr(value, "DOM_FieldAccess180", None)
                setattr(value, "DOM_FieldAccess180", self)

    @property
    def DOM_SimpleName75(self):
        return self.__DOM_SimpleName75

    @DOM_SimpleName75.setter
    def DOM_SimpleName75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName75", None)
        self.__DOM_SimpleName75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_AnnotationTypeMemberDeclaration74"):
                opp_val = getattr(old_value, "DOM_AnnotationTypeMemberDeclaration74", None)
                if opp_val == self:
                    setattr(old_value, "DOM_AnnotationTypeMemberDeclaration74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_AnnotationTypeMemberDeclaration74"):
                opp_val = getattr(value, "DOM_AnnotationTypeMemberDeclaration74", None)
                setattr(value, "DOM_AnnotationTypeMemberDeclaration74", self)

    @property
    def DOM_SimpleName56(self):
        return self.__DOM_SimpleName56

    @DOM_SimpleName56.setter
    def DOM_SimpleName56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName56", None)
        self.__DOM_SimpleName56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_TypeParameter"):
                opp_val = getattr(old_value, "DOM_TypeParameter", None)
                if opp_val == self:
                    setattr(old_value, "DOM_TypeParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_TypeParameter"):
                opp_val = getattr(value, "DOM_TypeParameter", None)
                setattr(value, "DOM_TypeParameter", self)

    @property
    def DOM_SimpleName40(self):
        return self.__DOM_SimpleName40

    @DOM_SimpleName40.setter
    def DOM_SimpleName40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName40", None)
        self.__DOM_SimpleName40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodRefParameter39"):
                opp_val = getattr(old_value, "DOM_MethodRefParameter39", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodRefParameter39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodRefParameter39"):
                opp_val = getattr(value, "DOM_MethodRefParameter39", None)
                setattr(value, "DOM_MethodRefParameter39", self)

    @property
    def DOM_SimpleName357(self):
        return self.__DOM_SimpleName357

    @DOM_SimpleName357.setter
    def DOM_SimpleName357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName357", None)
        self.__DOM_SimpleName357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_QualifiedType"):
                opp_val = getattr(old_value, "DOM_QualifiedType", None)
                if opp_val == self:
                    setattr(old_value, "DOM_QualifiedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_QualifiedType"):
                opp_val = getattr(value, "DOM_QualifiedType", None)
                setattr(value, "DOM_QualifiedType", self)

    @property
    def DOM_SimpleName97(self):
        return self.__DOM_SimpleName97

    @DOM_SimpleName97.setter
    def DOM_SimpleName97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName97", None)
        self.__DOM_SimpleName97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodDeclaration96"):
                opp_val = getattr(old_value, "DOM_MethodDeclaration96", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodDeclaration96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodDeclaration96"):
                opp_val = getattr(value, "DOM_MethodDeclaration96", None)
                setattr(value, "DOM_MethodDeclaration96", self)

    @property
    def DOM_SimpleName86(self):
        return self.__DOM_SimpleName86

    @DOM_SimpleName86.setter
    def DOM_SimpleName86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName86", None)
        self.__DOM_SimpleName86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_EnumConstantDeclaration85"):
                opp_val = getattr(old_value, "DOM_EnumConstantDeclaration85", None)
                if opp_val == self:
                    setattr(old_value, "DOM_EnumConstantDeclaration85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_EnumConstantDeclaration85"):
                opp_val = getattr(value, "DOM_EnumConstantDeclaration85", None)
                setattr(value, "DOM_EnumConstantDeclaration85", self)

    @property
    def DOM_SimpleName251(self):
        return self.__DOM_SimpleName251

    @DOM_SimpleName251.setter
    def DOM_SimpleName251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName251", None)
        self.__DOM_SimpleName251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_BreakStatement"):
                opp_val = getattr(old_value, "DOM_BreakStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_BreakStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_BreakStatement"):
                opp_val = getattr(value, "DOM_BreakStatement", None)
                setattr(value, "DOM_BreakStatement", self)

    @property
    def DOM_SimpleName297(self):
        return self.__DOM_SimpleName297

    @DOM_SimpleName297.setter
    def DOM_SimpleName297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SimpleName__DOM_SimpleName297", None)
        self.__DOM_SimpleName297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_LabeledStatement296"):
                opp_val = getattr(old_value, "DOM_LabeledStatement296", None)
                if opp_val == self:
                    setattr(old_value, "DOM_LabeledStatement296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_LabeledStatement296"):
                opp_val = getattr(value, "DOM_LabeledStatement296", None)
                setattr(value, "DOM_LabeledStatement296", self)

class DOM_Name(Expression):

    def __init__(self, fullyQualifiedName: str, DOM_Name: "DOM_ImportDeclaration" = None, DOM_Name25: "DOM_MemberRef" = None, DOM_Name35: "DOM_MethodRef" = None, DOM_Name50: "DOM_PackageDeclaration" = None, DOM_Name106: "DOM_MethodDeclaration" = None, DOM_Name130: "DOM_Annotation" = None, DOM_Name224: "DOM_SuperMethodInvocation" = None, DOM_Name227: "DOM_SuperMethodInvocation" = None, DOM_Name219: "DOM_SuperFieldAccess" = None, DOM_Name232: "DOM_ThisExpression" = None, DOM_Name362: "DOM_SimpleType" = None, DOM_Name375: "DOM_QualifiedName" = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.DOM_Name = DOM_Name
        self.DOM_Name25 = DOM_Name25
        self.DOM_Name35 = DOM_Name35
        self.DOM_Name50 = DOM_Name50
        self.DOM_Name106 = DOM_Name106
        self.DOM_Name130 = DOM_Name130
        self.DOM_Name224 = DOM_Name224
        self.DOM_Name227 = DOM_Name227
        self.DOM_Name219 = DOM_Name219
        self.DOM_Name232 = DOM_Name232
        self.DOM_Name362 = DOM_Name362
        self.DOM_Name375 = DOM_Name375
        
    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def DOM_Name106(self):
        return self.__DOM_Name106

    @DOM_Name106.setter
    def DOM_Name106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name106", None)
        self.__DOM_Name106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodDeclaration105"):
                opp_val = getattr(old_value, "DOM_MethodDeclaration105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodDeclaration105"):
                opp_val = getattr(value, "DOM_MethodDeclaration105", None)
                if opp_val is None:
                    setattr(value, "DOM_MethodDeclaration105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Name227(self):
        return self.__DOM_Name227

    @DOM_Name227.setter
    def DOM_Name227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name227", None)
        self.__DOM_Name227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperMethodInvocation226"):
                opp_val = getattr(old_value, "DOM_SuperMethodInvocation226", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SuperMethodInvocation226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperMethodInvocation226"):
                opp_val = getattr(value, "DOM_SuperMethodInvocation226", None)
                setattr(value, "DOM_SuperMethodInvocation226", self)

    @property
    def DOM_Name219(self):
        return self.__DOM_Name219

    @DOM_Name219.setter
    def DOM_Name219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name219", None)
        self.__DOM_Name219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperFieldAccess218"):
                opp_val = getattr(old_value, "DOM_SuperFieldAccess218", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SuperFieldAccess218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperFieldAccess218"):
                opp_val = getattr(value, "DOM_SuperFieldAccess218", None)
                setattr(value, "DOM_SuperFieldAccess218", self)

    @property
    def DOM_Name25(self):
        return self.__DOM_Name25

    @DOM_Name25.setter
    def DOM_Name25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name25", None)
        self.__DOM_Name25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MemberRef24"):
                opp_val = getattr(old_value, "DOM_MemberRef24", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MemberRef24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MemberRef24"):
                opp_val = getattr(value, "DOM_MemberRef24", None)
                setattr(value, "DOM_MemberRef24", self)

    @property
    def DOM_Name375(self):
        return self.__DOM_Name375

    @DOM_Name375.setter
    def DOM_Name375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name375", None)
        self.__DOM_Name375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_QualifiedName374"):
                opp_val = getattr(old_value, "DOM_QualifiedName374", None)
                if opp_val == self:
                    setattr(old_value, "DOM_QualifiedName374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_QualifiedName374"):
                opp_val = getattr(value, "DOM_QualifiedName374", None)
                setattr(value, "DOM_QualifiedName374", self)

    @property
    def DOM_Name232(self):
        return self.__DOM_Name232

    @DOM_Name232.setter
    def DOM_Name232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name232", None)
        self.__DOM_Name232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ThisExpression"):
                opp_val = getattr(old_value, "DOM_ThisExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ThisExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ThisExpression"):
                opp_val = getattr(value, "DOM_ThisExpression", None)
                setattr(value, "DOM_ThisExpression", self)

    @property
    def DOM_Name(self):
        return self.__DOM_Name

    @DOM_Name.setter
    def DOM_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name", None)
        self.__DOM_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ImportDeclaration21"):
                opp_val = getattr(old_value, "DOM_ImportDeclaration21", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ImportDeclaration21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ImportDeclaration21"):
                opp_val = getattr(value, "DOM_ImportDeclaration21", None)
                setattr(value, "DOM_ImportDeclaration21", self)

    @property
    def DOM_Name35(self):
        return self.__DOM_Name35

    @DOM_Name35.setter
    def DOM_Name35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name35", None)
        self.__DOM_Name35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodRef34"):
                opp_val = getattr(old_value, "DOM_MethodRef34", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodRef34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodRef34"):
                opp_val = getattr(value, "DOM_MethodRef34", None)
                setattr(value, "DOM_MethodRef34", self)

    @property
    def DOM_Name50(self):
        return self.__DOM_Name50

    @DOM_Name50.setter
    def DOM_Name50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name50", None)
        self.__DOM_Name50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_PackageDeclaration49"):
                opp_val = getattr(old_value, "DOM_PackageDeclaration49", None)
                if opp_val == self:
                    setattr(old_value, "DOM_PackageDeclaration49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_PackageDeclaration49"):
                opp_val = getattr(value, "DOM_PackageDeclaration49", None)
                setattr(value, "DOM_PackageDeclaration49", self)

    @property
    def DOM_Name130(self):
        return self.__DOM_Name130

    @DOM_Name130.setter
    def DOM_Name130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name130", None)
        self.__DOM_Name130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Annotation129"):
                opp_val = getattr(old_value, "DOM_Annotation129", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Annotation129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Annotation129"):
                opp_val = getattr(value, "DOM_Annotation129", None)
                setattr(value, "DOM_Annotation129", self)

    @property
    def DOM_Name362(self):
        return self.__DOM_Name362

    @DOM_Name362.setter
    def DOM_Name362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name362", None)
        self.__DOM_Name362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SimpleType"):
                opp_val = getattr(old_value, "DOM_SimpleType", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SimpleType"):
                opp_val = getattr(value, "DOM_SimpleType", None)
                setattr(value, "DOM_SimpleType", self)

    @property
    def DOM_Name224(self):
        return self.__DOM_Name224

    @DOM_Name224.setter
    def DOM_Name224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Name__DOM_Name224", None)
        self.__DOM_Name224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperMethodInvocation223"):
                opp_val = getattr(old_value, "DOM_SuperMethodInvocation223", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SuperMethodInvocation223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperMethodInvocation223"):
                opp_val = getattr(value, "DOM_SuperMethodInvocation223", None)
                setattr(value, "DOM_SuperMethodInvocation223", self)

class DOM_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, DOM_SingleVariableDeclaration: "DOM_CatchClause" = None, DOM_SingleVariableDeclaration103: "DOM_MethodDeclaration" = None, DOM_SingleVariableDeclaration271: "DOM_EnhancedForStatement" = None, DOM_SingleVariableDeclaration366: "DOM_Type" = None, DOM_SingleVariableDeclaration369: set["DOM_ExtendedModifier"] = None):
        self.varargs = varargs
        self.DOM_SingleVariableDeclaration = DOM_SingleVariableDeclaration
        self.DOM_SingleVariableDeclaration103 = DOM_SingleVariableDeclaration103
        self.DOM_SingleVariableDeclaration271 = DOM_SingleVariableDeclaration271
        self.DOM_SingleVariableDeclaration366 = DOM_SingleVariableDeclaration366
        self.DOM_SingleVariableDeclaration369 = DOM_SingleVariableDeclaration369 if DOM_SingleVariableDeclaration369 is not None else set()
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def DOM_SingleVariableDeclaration271(self):
        return self.__DOM_SingleVariableDeclaration271

    @DOM_SingleVariableDeclaration271.setter
    def DOM_SingleVariableDeclaration271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration271", None)
        self.__DOM_SingleVariableDeclaration271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_EnhancedForStatement270"):
                opp_val = getattr(old_value, "DOM_EnhancedForStatement270", None)
                if opp_val == self:
                    setattr(old_value, "DOM_EnhancedForStatement270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_EnhancedForStatement270"):
                opp_val = getattr(value, "DOM_EnhancedForStatement270", None)
                setattr(value, "DOM_EnhancedForStatement270", self)

    @property
    def DOM_SingleVariableDeclaration369(self):
        return self.__DOM_SingleVariableDeclaration369

    @DOM_SingleVariableDeclaration369.setter
    def DOM_SingleVariableDeclaration369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration369", None)
        self.__DOM_SingleVariableDeclaration369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_ExtendedModifier370"):
                    opp_val = getattr(item, "DOM_ExtendedModifier370", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_ExtendedModifier370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_ExtendedModifier370"):
                    opp_val = getattr(item, "DOM_ExtendedModifier370", None)
                    
                    setattr(item, "DOM_ExtendedModifier370", self)
                    

    @property
    def DOM_SingleVariableDeclaration(self):
        return self.__DOM_SingleVariableDeclaration

    @DOM_SingleVariableDeclaration.setter
    def DOM_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration", None)
        self.__DOM_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_CatchClause8"):
                opp_val = getattr(old_value, "DOM_CatchClause8", None)
                if opp_val == self:
                    setattr(old_value, "DOM_CatchClause8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_CatchClause8"):
                opp_val = getattr(value, "DOM_CatchClause8", None)
                setattr(value, "DOM_CatchClause8", self)

    @property
    def DOM_SingleVariableDeclaration366(self):
        return self.__DOM_SingleVariableDeclaration366

    @DOM_SingleVariableDeclaration366.setter
    def DOM_SingleVariableDeclaration366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration366", None)
        self.__DOM_SingleVariableDeclaration366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type367"):
                opp_val = getattr(old_value, "DOM_Type367", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type367"):
                opp_val = getattr(value, "DOM_Type367", None)
                setattr(value, "DOM_Type367", self)

    @property
    def DOM_SingleVariableDeclaration103(self):
        return self.__DOM_SingleVariableDeclaration103

    @DOM_SingleVariableDeclaration103.setter
    def DOM_SingleVariableDeclaration103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration103", None)
        self.__DOM_SingleVariableDeclaration103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodDeclaration102"):
                opp_val = getattr(old_value, "DOM_MethodDeclaration102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodDeclaration102"):
                opp_val = getattr(value, "DOM_MethodDeclaration102", None)
                if opp_val is None:
                    setattr(value, "DOM_MethodDeclaration102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DOM_Block(Statement):

    pass
class DOM_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, DOM_AbstractTypeDeclaration: "DOM_CompilationUnit" = None, DOM_AbstractTypeDeclaration66: set["DOM_BodyDeclaration"] = None, DOM_AbstractTypeDeclaration69: "DOM_SimpleName" = None, DOM_AbstractTypeDeclaration331: "DOM_TypeDeclarationStatement" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.DOM_AbstractTypeDeclaration = DOM_AbstractTypeDeclaration
        self.DOM_AbstractTypeDeclaration66 = DOM_AbstractTypeDeclaration66 if DOM_AbstractTypeDeclaration66 is not None else set()
        self.DOM_AbstractTypeDeclaration69 = DOM_AbstractTypeDeclaration69
        self.DOM_AbstractTypeDeclaration331 = DOM_AbstractTypeDeclaration331
        
    @property
    def packageMemberTypeDeclaration(self) -> str:
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration

    @property
    def memberTypeDeclaration(self) -> str:
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration

    @property
    def localTypeDeclaration(self) -> str:
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration

    @property
    def DOM_AbstractTypeDeclaration69(self):
        return self.__DOM_AbstractTypeDeclaration69

    @DOM_AbstractTypeDeclaration69.setter
    def DOM_AbstractTypeDeclaration69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration69", None)
        self.__DOM_AbstractTypeDeclaration69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SimpleName70"):
                opp_val = getattr(old_value, "DOM_SimpleName70", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SimpleName70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SimpleName70"):
                opp_val = getattr(value, "DOM_SimpleName70", None)
                setattr(value, "DOM_SimpleName70", self)

    @property
    def DOM_AbstractTypeDeclaration(self):
        return self.__DOM_AbstractTypeDeclaration

    @DOM_AbstractTypeDeclaration.setter
    def DOM_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration", None)
        self.__DOM_AbstractTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_CompilationUnit18"):
                opp_val = getattr(old_value, "DOM_CompilationUnit18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_CompilationUnit18"):
                opp_val = getattr(value, "DOM_CompilationUnit18", None)
                if opp_val is None:
                    setattr(value, "DOM_CompilationUnit18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_AbstractTypeDeclaration66(self):
        return self.__DOM_AbstractTypeDeclaration66

    @DOM_AbstractTypeDeclaration66.setter
    def DOM_AbstractTypeDeclaration66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration66", None)
        self.__DOM_AbstractTypeDeclaration66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_BodyDeclaration67"):
                    opp_val = getattr(item, "DOM_BodyDeclaration67", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_BodyDeclaration67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_BodyDeclaration67"):
                    opp_val = getattr(item, "DOM_BodyDeclaration67", None)
                    
                    setattr(item, "DOM_BodyDeclaration67", self)
                    

    @property
    def DOM_AbstractTypeDeclaration331(self):
        return self.__DOM_AbstractTypeDeclaration331

    @DOM_AbstractTypeDeclaration331.setter
    def DOM_AbstractTypeDeclaration331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration331", None)
        self.__DOM_AbstractTypeDeclaration331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_TypeDeclarationStatement"):
                opp_val = getattr(old_value, "DOM_TypeDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_TypeDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_TypeDeclarationStatement"):
                opp_val = getattr(value, "DOM_TypeDeclarationStatement", None)
                setattr(value, "DOM_TypeDeclarationStatement", self)

class DOM_Javadoc(Comment):

    pass
class DOM_ASTNode(ABC):

    pass
class DOM_AST:

    pass
class DOM_ExtendedModifier(ABC):

    pass
class ASTNode:

    pass
class DOM_TypeParameter(ASTNode):

    pass
class DOM_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, DOM_VariableDeclaration63: "DOM_SimpleName" = None, DOM_VariableDeclaration: "DOM_Expression" = None):
        self.extraDimensions = extraDimensions
        self.DOM_VariableDeclaration63 = DOM_VariableDeclaration63
        self.DOM_VariableDeclaration = DOM_VariableDeclaration
        
    @property
    def extraDimensions(self) -> str:
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions

    @property
    def DOM_VariableDeclaration63(self):
        return self.__DOM_VariableDeclaration63

    @DOM_VariableDeclaration63.setter
    def DOM_VariableDeclaration63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_VariableDeclaration__DOM_VariableDeclaration63", None)
        self.__DOM_VariableDeclaration63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SimpleName64"):
                opp_val = getattr(old_value, "DOM_SimpleName64", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SimpleName64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SimpleName64"):
                opp_val = getattr(value, "DOM_SimpleName64", None)
                setattr(value, "DOM_SimpleName64", self)

    @property
    def DOM_VariableDeclaration(self):
        return self.__DOM_VariableDeclaration

    @DOM_VariableDeclaration.setter
    def DOM_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_VariableDeclaration__DOM_VariableDeclaration", None)
        self.__DOM_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Expression61"):
                opp_val = getattr(old_value, "DOM_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Expression61"):
                opp_val = getattr(value, "DOM_Expression61", None)
                setattr(value, "DOM_Expression61", self)

class DOM_Modifier(ExtendedModifier, ASTNode):

    def __init__(self, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, abstract: str, final: str, native: str, none: str, private: str):
        self.protected = protected
        self.public = public
        self.static = static
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.transient = transient
        self.volatile = volatile
        self.abstract = abstract
        self.final = final
        self.native = native
        self.none = none
        self.private = private
        
    @property
    def none(self) -> str:
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def native(self) -> str:
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native

    @property
    def public(self) -> str:
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public

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
    def strictfp(self) -> str:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp

    @property
    def transient(self) -> str:
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient

    @property
    def synchronized(self) -> str:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized

    @property
    def private(self) -> str:
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

class DOM_PackageDeclaration(ASTNode):

    pass
class DOM_MemberRef(ASTNode):

    pass
class DOM_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, DOM_MethodRefParameter: "DOM_MethodRef" = None, DOM_MethodRefParameter39: "DOM_SimpleName" = None, DOM_MethodRefParameter42: "DOM_Type" = None):
        self.varargs = varargs
        self.DOM_MethodRefParameter = DOM_MethodRefParameter
        self.DOM_MethodRefParameter39 = DOM_MethodRefParameter39
        self.DOM_MethodRefParameter42 = DOM_MethodRefParameter42
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def DOM_MethodRefParameter(self):
        return self.__DOM_MethodRefParameter

    @DOM_MethodRefParameter.setter
    def DOM_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter", None)
        self.__DOM_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodRef37"):
                opp_val = getattr(old_value, "DOM_MethodRef37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodRef37"):
                opp_val = getattr(value, "DOM_MethodRef37", None)
                if opp_val is None:
                    setattr(value, "DOM_MethodRef37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_MethodRefParameter42(self):
        return self.__DOM_MethodRefParameter42

    @DOM_MethodRefParameter42.setter
    def DOM_MethodRefParameter42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter42", None)
        self.__DOM_MethodRefParameter42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Type"):
                opp_val = getattr(old_value, "DOM_Type", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Type"):
                opp_val = getattr(value, "DOM_Type", None)
                setattr(value, "DOM_Type", self)

    @property
    def DOM_MethodRefParameter39(self):
        return self.__DOM_MethodRefParameter39

    @DOM_MethodRefParameter39.setter
    def DOM_MethodRefParameter39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter39", None)
        self.__DOM_MethodRefParameter39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SimpleName40"):
                opp_val = getattr(old_value, "DOM_SimpleName40", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SimpleName40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SimpleName40"):
                opp_val = getattr(value, "DOM_SimpleName40", None)
                setattr(value, "DOM_SimpleName40", self)

class DOM_BodyDeclaration(ASTNode):

    pass
class DOM_Statement(ASTNode):

    pass
class DOM_CompilationUnit(ASTNode):

    pass
class DOM_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, DOM_Expression: "DOM_IType" = None, DOM_Expression30: "DOM_MemberValuePair" = None, DOM_Expression61: "DOM_VariableDeclaration" = None, DOM_Expression80: "DOM_EnumConstantDeclaration" = None, DOM_Expression72: "DOM_AnnotationTypeMemberDeclaration" = None, DOM_Expression144: "DOM_ArrayInitializer" = None, DOM_Expression146: "DOM_Assignment" = None, DOM_Expression132: "DOM_ArrayAccess" = None, DOM_Expression135: "DOM_ArrayAccess" = None, DOM_Expression137: "DOM_ArrayCreation" = None, DOM_Expression151: "DOM_CastExpression" = None, DOM_Expression149: "DOM_Assignment" = None, DOM_Expression156: "DOM_ClassInstanceCreation" = None, DOM_Expression162: "DOM_ClassInstanceCreation" = None, DOM_Expression178: "DOM_FieldAccess" = None, DOM_Expression183: "DOM_InfixExpression" = None, DOM_Expression170: "DOM_ConditionalExpression" = None, DOM_Expression173: "DOM_ConditionalExpression" = None, DOM_Expression176: "DOM_ConditionalExpression" = None, DOM_Expression186: "DOM_InfixExpression" = None, DOM_Expression196: "DOM_MethodInvocation" = None, DOM_Expression189: "DOM_InfixExpression" = None, DOM_Expression191: "DOM_InstanceofExpression" = None, DOM_Expression210: "DOM_ParenthesizedExpression" = None, DOM_Expression199: "DOM_MethodInvocation" = None, DOM_Expression212: "DOM_PostfixExpression" = None, DOM_Expression214: "DOM_PrefixExpression" = None, DOM_Expression221: "DOM_SuperMethodInvocation" = None, DOM_Expression253: "DOM_ConstructorInvocation" = None, DOM_Expression244: "DOM_AssertStatement" = None, DOM_Expression247: "DOM_AssertStatement" = None, DOM_Expression263: "DOM_DoStatement" = None, DOM_Expression281: "DOM_ForStatement" = None, DOM_Expression268: "DOM_EnhancedForStatement" = None, DOM_Expression273: "DOM_ExpressionStatement" = None, DOM_Expression278: "DOM_ForStatement" = None, DOM_Expression284: "DOM_ForStatement" = None, DOM_Expression289: "DOM_IfStatement" = None, DOM_Expression299: "DOM_ReturnStatement" = None, DOM_Expression301: "DOM_SuperConstructorInvocation" = None, DOM_Expression304: "DOM_SuperConstructorInvocation" = None, DOM_Expression319: "DOM_SynchronizedStatement" = None, DOM_Expression309: "DOM_SwitchCase" = None, DOM_Expression311: "DOM_SwitchStatement" = None, DOM_Expression321: "DOM_ThrowStatement" = None, DOM_Expression344: "DOM_WhileStatement" = None, DOM_Expression379: "DOM_SingleMemberAnnotation" = None):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        self.DOM_Expression = DOM_Expression
        self.DOM_Expression30 = DOM_Expression30
        self.DOM_Expression61 = DOM_Expression61
        self.DOM_Expression80 = DOM_Expression80
        self.DOM_Expression72 = DOM_Expression72
        self.DOM_Expression144 = DOM_Expression144
        self.DOM_Expression146 = DOM_Expression146
        self.DOM_Expression132 = DOM_Expression132
        self.DOM_Expression135 = DOM_Expression135
        self.DOM_Expression137 = DOM_Expression137
        self.DOM_Expression151 = DOM_Expression151
        self.DOM_Expression149 = DOM_Expression149
        self.DOM_Expression156 = DOM_Expression156
        self.DOM_Expression162 = DOM_Expression162
        self.DOM_Expression178 = DOM_Expression178
        self.DOM_Expression183 = DOM_Expression183
        self.DOM_Expression170 = DOM_Expression170
        self.DOM_Expression173 = DOM_Expression173
        self.DOM_Expression176 = DOM_Expression176
        self.DOM_Expression186 = DOM_Expression186
        self.DOM_Expression196 = DOM_Expression196
        self.DOM_Expression189 = DOM_Expression189
        self.DOM_Expression191 = DOM_Expression191
        self.DOM_Expression210 = DOM_Expression210
        self.DOM_Expression199 = DOM_Expression199
        self.DOM_Expression212 = DOM_Expression212
        self.DOM_Expression214 = DOM_Expression214
        self.DOM_Expression221 = DOM_Expression221
        self.DOM_Expression253 = DOM_Expression253
        self.DOM_Expression244 = DOM_Expression244
        self.DOM_Expression247 = DOM_Expression247
        self.DOM_Expression263 = DOM_Expression263
        self.DOM_Expression281 = DOM_Expression281
        self.DOM_Expression268 = DOM_Expression268
        self.DOM_Expression273 = DOM_Expression273
        self.DOM_Expression278 = DOM_Expression278
        self.DOM_Expression284 = DOM_Expression284
        self.DOM_Expression289 = DOM_Expression289
        self.DOM_Expression299 = DOM_Expression299
        self.DOM_Expression301 = DOM_Expression301
        self.DOM_Expression304 = DOM_Expression304
        self.DOM_Expression319 = DOM_Expression319
        self.DOM_Expression309 = DOM_Expression309
        self.DOM_Expression311 = DOM_Expression311
        self.DOM_Expression321 = DOM_Expression321
        self.DOM_Expression344 = DOM_Expression344
        self.DOM_Expression379 = DOM_Expression379
        
    @property
    def resolveBoxing(self) -> str:
        return self.__resolveBoxing

    @resolveBoxing.setter
    def resolveBoxing(self, resolveBoxing: str):
        self.__resolveBoxing = resolveBoxing

    @property
    def resolveUnboxing(self) -> str:
        return self.__resolveUnboxing

    @resolveUnboxing.setter
    def resolveUnboxing(self, resolveUnboxing: str):
        self.__resolveUnboxing = resolveUnboxing

    @property
    def DOM_Expression183(self):
        return self.__DOM_Expression183

    @DOM_Expression183.setter
    def DOM_Expression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression183", None)
        self.__DOM_Expression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_InfixExpression"):
                opp_val = getattr(old_value, "DOM_InfixExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_InfixExpression"):
                opp_val = getattr(value, "DOM_InfixExpression", None)
                if opp_val is None:
                    setattr(value, "DOM_InfixExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression268(self):
        return self.__DOM_Expression268

    @DOM_Expression268.setter
    def DOM_Expression268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression268", None)
        self.__DOM_Expression268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_EnhancedForStatement267"):
                opp_val = getattr(old_value, "DOM_EnhancedForStatement267", None)
                if opp_val == self:
                    setattr(old_value, "DOM_EnhancedForStatement267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_EnhancedForStatement267"):
                opp_val = getattr(value, "DOM_EnhancedForStatement267", None)
                setattr(value, "DOM_EnhancedForStatement267", self)

    @property
    def DOM_Expression170(self):
        return self.__DOM_Expression170

    @DOM_Expression170.setter
    def DOM_Expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression170", None)
        self.__DOM_Expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ConditionalExpression"):
                opp_val = getattr(old_value, "DOM_ConditionalExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ConditionalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ConditionalExpression"):
                opp_val = getattr(value, "DOM_ConditionalExpression", None)
                setattr(value, "DOM_ConditionalExpression", self)

    @property
    def DOM_Expression210(self):
        return self.__DOM_Expression210

    @DOM_Expression210.setter
    def DOM_Expression210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression210", None)
        self.__DOM_Expression210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ParenthesizedExpression"):
                opp_val = getattr(old_value, "DOM_ParenthesizedExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ParenthesizedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ParenthesizedExpression"):
                opp_val = getattr(value, "DOM_ParenthesizedExpression", None)
                setattr(value, "DOM_ParenthesizedExpression", self)

    @property
    def DOM_Expression301(self):
        return self.__DOM_Expression301

    @DOM_Expression301.setter
    def DOM_Expression301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression301", None)
        self.__DOM_Expression301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperConstructorInvocation"):
                opp_val = getattr(old_value, "DOM_SuperConstructorInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperConstructorInvocation"):
                opp_val = getattr(value, "DOM_SuperConstructorInvocation", None)
                if opp_val is None:
                    setattr(value, "DOM_SuperConstructorInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression212(self):
        return self.__DOM_Expression212

    @DOM_Expression212.setter
    def DOM_Expression212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression212", None)
        self.__DOM_Expression212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_PostfixExpression"):
                opp_val = getattr(old_value, "DOM_PostfixExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_PostfixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_PostfixExpression"):
                opp_val = getattr(value, "DOM_PostfixExpression", None)
                setattr(value, "DOM_PostfixExpression", self)

    @property
    def DOM_Expression132(self):
        return self.__DOM_Expression132

    @DOM_Expression132.setter
    def DOM_Expression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression132", None)
        self.__DOM_Expression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ArrayAccess"):
                opp_val = getattr(old_value, "DOM_ArrayAccess", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ArrayAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ArrayAccess"):
                opp_val = getattr(value, "DOM_ArrayAccess", None)
                setattr(value, "DOM_ArrayAccess", self)

    @property
    def DOM_Expression309(self):
        return self.__DOM_Expression309

    @DOM_Expression309.setter
    def DOM_Expression309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression309", None)
        self.__DOM_Expression309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SwitchCase"):
                opp_val = getattr(old_value, "DOM_SwitchCase", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SwitchCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SwitchCase"):
                opp_val = getattr(value, "DOM_SwitchCase", None)
                setattr(value, "DOM_SwitchCase", self)

    @property
    def DOM_Expression146(self):
        return self.__DOM_Expression146

    @DOM_Expression146.setter
    def DOM_Expression146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression146", None)
        self.__DOM_Expression146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Assignment"):
                opp_val = getattr(old_value, "DOM_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Assignment"):
                opp_val = getattr(value, "DOM_Assignment", None)
                setattr(value, "DOM_Assignment", self)

    @property
    def DOM_Expression253(self):
        return self.__DOM_Expression253

    @DOM_Expression253.setter
    def DOM_Expression253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression253", None)
        self.__DOM_Expression253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ConstructorInvocation"):
                opp_val = getattr(old_value, "DOM_ConstructorInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ConstructorInvocation"):
                opp_val = getattr(value, "DOM_ConstructorInvocation", None)
                if opp_val is None:
                    setattr(value, "DOM_ConstructorInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression162(self):
        return self.__DOM_Expression162

    @DOM_Expression162.setter
    def DOM_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression162", None)
        self.__DOM_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ClassInstanceCreation161"):
                opp_val = getattr(old_value, "DOM_ClassInstanceCreation161", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ClassInstanceCreation161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ClassInstanceCreation161"):
                opp_val = getattr(value, "DOM_ClassInstanceCreation161", None)
                setattr(value, "DOM_ClassInstanceCreation161", self)

    @property
    def DOM_Expression(self):
        return self.__DOM_Expression

    @DOM_Expression.setter
    def DOM_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression", None)
        self.__DOM_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_IType"):
                opp_val = getattr(old_value, "DOM_IType", None)
                if opp_val == self:
                    setattr(old_value, "DOM_IType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_IType"):
                opp_val = getattr(value, "DOM_IType", None)
                setattr(value, "DOM_IType", self)

    @property
    def DOM_Expression319(self):
        return self.__DOM_Expression319

    @DOM_Expression319.setter
    def DOM_Expression319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression319", None)
        self.__DOM_Expression319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SynchronizedStatement318"):
                opp_val = getattr(old_value, "DOM_SynchronizedStatement318", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SynchronizedStatement318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SynchronizedStatement318"):
                opp_val = getattr(value, "DOM_SynchronizedStatement318", None)
                setattr(value, "DOM_SynchronizedStatement318", self)

    @property
    def DOM_Expression189(self):
        return self.__DOM_Expression189

    @DOM_Expression189.setter
    def DOM_Expression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression189", None)
        self.__DOM_Expression189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_InfixExpression188"):
                opp_val = getattr(old_value, "DOM_InfixExpression188", None)
                if opp_val == self:
                    setattr(old_value, "DOM_InfixExpression188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_InfixExpression188"):
                opp_val = getattr(value, "DOM_InfixExpression188", None)
                setattr(value, "DOM_InfixExpression188", self)

    @property
    def DOM_Expression304(self):
        return self.__DOM_Expression304

    @DOM_Expression304.setter
    def DOM_Expression304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression304", None)
        self.__DOM_Expression304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperConstructorInvocation303"):
                opp_val = getattr(old_value, "DOM_SuperConstructorInvocation303", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SuperConstructorInvocation303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperConstructorInvocation303"):
                opp_val = getattr(value, "DOM_SuperConstructorInvocation303", None)
                setattr(value, "DOM_SuperConstructorInvocation303", self)

    @property
    def DOM_Expression156(self):
        return self.__DOM_Expression156

    @DOM_Expression156.setter
    def DOM_Expression156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression156", None)
        self.__DOM_Expression156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ClassInstanceCreation"):
                opp_val = getattr(old_value, "DOM_ClassInstanceCreation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ClassInstanceCreation"):
                opp_val = getattr(value, "DOM_ClassInstanceCreation", None)
                if opp_val is None:
                    setattr(value, "DOM_ClassInstanceCreation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression191(self):
        return self.__DOM_Expression191

    @DOM_Expression191.setter
    def DOM_Expression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression191", None)
        self.__DOM_Expression191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_InstanceofExpression"):
                opp_val = getattr(old_value, "DOM_InstanceofExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_InstanceofExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_InstanceofExpression"):
                opp_val = getattr(value, "DOM_InstanceofExpression", None)
                setattr(value, "DOM_InstanceofExpression", self)

    @property
    def DOM_Expression299(self):
        return self.__DOM_Expression299

    @DOM_Expression299.setter
    def DOM_Expression299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression299", None)
        self.__DOM_Expression299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ReturnStatement"):
                opp_val = getattr(old_value, "DOM_ReturnStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ReturnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ReturnStatement"):
                opp_val = getattr(value, "DOM_ReturnStatement", None)
                setattr(value, "DOM_ReturnStatement", self)

    @property
    def DOM_Expression278(self):
        return self.__DOM_Expression278

    @DOM_Expression278.setter
    def DOM_Expression278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression278", None)
        self.__DOM_Expression278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ForStatement277"):
                opp_val = getattr(old_value, "DOM_ForStatement277", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ForStatement277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ForStatement277"):
                opp_val = getattr(value, "DOM_ForStatement277", None)
                setattr(value, "DOM_ForStatement277", self)

    @property
    def DOM_Expression30(self):
        return self.__DOM_Expression30

    @DOM_Expression30.setter
    def DOM_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression30", None)
        self.__DOM_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MemberValuePair29"):
                opp_val = getattr(old_value, "DOM_MemberValuePair29", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MemberValuePair29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MemberValuePair29"):
                opp_val = getattr(value, "DOM_MemberValuePair29", None)
                setattr(value, "DOM_MemberValuePair29", self)

    @property
    def DOM_Expression149(self):
        return self.__DOM_Expression149

    @DOM_Expression149.setter
    def DOM_Expression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression149", None)
        self.__DOM_Expression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Assignment148"):
                opp_val = getattr(old_value, "DOM_Assignment148", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Assignment148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Assignment148"):
                opp_val = getattr(value, "DOM_Assignment148", None)
                setattr(value, "DOM_Assignment148", self)

    @property
    def DOM_Expression80(self):
        return self.__DOM_Expression80

    @DOM_Expression80.setter
    def DOM_Expression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression80", None)
        self.__DOM_Expression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_EnumConstantDeclaration"):
                opp_val = getattr(old_value, "DOM_EnumConstantDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_EnumConstantDeclaration"):
                opp_val = getattr(value, "DOM_EnumConstantDeclaration", None)
                if opp_val is None:
                    setattr(value, "DOM_EnumConstantDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression263(self):
        return self.__DOM_Expression263

    @DOM_Expression263.setter
    def DOM_Expression263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression263", None)
        self.__DOM_Expression263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_DoStatement262"):
                opp_val = getattr(old_value, "DOM_DoStatement262", None)
                if opp_val == self:
                    setattr(old_value, "DOM_DoStatement262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_DoStatement262"):
                opp_val = getattr(value, "DOM_DoStatement262", None)
                setattr(value, "DOM_DoStatement262", self)

    @property
    def DOM_Expression247(self):
        return self.__DOM_Expression247

    @DOM_Expression247.setter
    def DOM_Expression247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression247", None)
        self.__DOM_Expression247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_AssertStatement246"):
                opp_val = getattr(old_value, "DOM_AssertStatement246", None)
                if opp_val == self:
                    setattr(old_value, "DOM_AssertStatement246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_AssertStatement246"):
                opp_val = getattr(value, "DOM_AssertStatement246", None)
                setattr(value, "DOM_AssertStatement246", self)

    @property
    def DOM_Expression173(self):
        return self.__DOM_Expression173

    @DOM_Expression173.setter
    def DOM_Expression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression173", None)
        self.__DOM_Expression173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ConditionalExpression172"):
                opp_val = getattr(old_value, "DOM_ConditionalExpression172", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ConditionalExpression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ConditionalExpression172"):
                opp_val = getattr(value, "DOM_ConditionalExpression172", None)
                setattr(value, "DOM_ConditionalExpression172", self)

    @property
    def DOM_Expression214(self):
        return self.__DOM_Expression214

    @DOM_Expression214.setter
    def DOM_Expression214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression214", None)
        self.__DOM_Expression214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_PrefixExpression"):
                opp_val = getattr(old_value, "DOM_PrefixExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_PrefixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_PrefixExpression"):
                opp_val = getattr(value, "DOM_PrefixExpression", None)
                setattr(value, "DOM_PrefixExpression", self)

    @property
    def DOM_Expression281(self):
        return self.__DOM_Expression281

    @DOM_Expression281.setter
    def DOM_Expression281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression281", None)
        self.__DOM_Expression281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ForStatement280"):
                opp_val = getattr(old_value, "DOM_ForStatement280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ForStatement280"):
                opp_val = getattr(value, "DOM_ForStatement280", None)
                if opp_val is None:
                    setattr(value, "DOM_ForStatement280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression311(self):
        return self.__DOM_Expression311

    @DOM_Expression311.setter
    def DOM_Expression311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression311", None)
        self.__DOM_Expression311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SwitchStatement"):
                opp_val = getattr(old_value, "DOM_SwitchStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SwitchStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SwitchStatement"):
                opp_val = getattr(value, "DOM_SwitchStatement", None)
                setattr(value, "DOM_SwitchStatement", self)

    @property
    def DOM_Expression196(self):
        return self.__DOM_Expression196

    @DOM_Expression196.setter
    def DOM_Expression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression196", None)
        self.__DOM_Expression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodInvocation"):
                opp_val = getattr(old_value, "DOM_MethodInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodInvocation"):
                opp_val = getattr(value, "DOM_MethodInvocation", None)
                if opp_val is None:
                    setattr(value, "DOM_MethodInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression72(self):
        return self.__DOM_Expression72

    @DOM_Expression72.setter
    def DOM_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression72", None)
        self.__DOM_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_AnnotationTypeMemberDeclaration"):
                opp_val = getattr(old_value, "DOM_AnnotationTypeMemberDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "DOM_AnnotationTypeMemberDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_AnnotationTypeMemberDeclaration"):
                opp_val = getattr(value, "DOM_AnnotationTypeMemberDeclaration", None)
                setattr(value, "DOM_AnnotationTypeMemberDeclaration", self)

    @property
    def DOM_Expression144(self):
        return self.__DOM_Expression144

    @DOM_Expression144.setter
    def DOM_Expression144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression144", None)
        self.__DOM_Expression144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ArrayInitializer143"):
                opp_val = getattr(old_value, "DOM_ArrayInitializer143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ArrayInitializer143"):
                opp_val = getattr(value, "DOM_ArrayInitializer143", None)
                if opp_val is None:
                    setattr(value, "DOM_ArrayInitializer143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression289(self):
        return self.__DOM_Expression289

    @DOM_Expression289.setter
    def DOM_Expression289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression289", None)
        self.__DOM_Expression289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_IfStatement288"):
                opp_val = getattr(old_value, "DOM_IfStatement288", None)
                if opp_val == self:
                    setattr(old_value, "DOM_IfStatement288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_IfStatement288"):
                opp_val = getattr(value, "DOM_IfStatement288", None)
                setattr(value, "DOM_IfStatement288", self)

    @property
    def DOM_Expression151(self):
        return self.__DOM_Expression151

    @DOM_Expression151.setter
    def DOM_Expression151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression151", None)
        self.__DOM_Expression151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_CastExpression"):
                opp_val = getattr(old_value, "DOM_CastExpression", None)
                if opp_val == self:
                    setattr(old_value, "DOM_CastExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_CastExpression"):
                opp_val = getattr(value, "DOM_CastExpression", None)
                setattr(value, "DOM_CastExpression", self)

    @property
    def DOM_Expression379(self):
        return self.__DOM_Expression379

    @DOM_Expression379.setter
    def DOM_Expression379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression379", None)
        self.__DOM_Expression379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SingleMemberAnnotation"):
                opp_val = getattr(old_value, "DOM_SingleMemberAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "DOM_SingleMemberAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SingleMemberAnnotation"):
                opp_val = getattr(value, "DOM_SingleMemberAnnotation", None)
                setattr(value, "DOM_SingleMemberAnnotation", self)

    @property
    def DOM_Expression176(self):
        return self.__DOM_Expression176

    @DOM_Expression176.setter
    def DOM_Expression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression176", None)
        self.__DOM_Expression176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ConditionalExpression175"):
                opp_val = getattr(old_value, "DOM_ConditionalExpression175", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ConditionalExpression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ConditionalExpression175"):
                opp_val = getattr(value, "DOM_ConditionalExpression175", None)
                setattr(value, "DOM_ConditionalExpression175", self)

    @property
    def DOM_Expression284(self):
        return self.__DOM_Expression284

    @DOM_Expression284.setter
    def DOM_Expression284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression284", None)
        self.__DOM_Expression284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ForStatement283"):
                opp_val = getattr(old_value, "DOM_ForStatement283", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ForStatement283"):
                opp_val = getattr(value, "DOM_ForStatement283", None)
                if opp_val is None:
                    setattr(value, "DOM_ForStatement283", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression135(self):
        return self.__DOM_Expression135

    @DOM_Expression135.setter
    def DOM_Expression135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression135", None)
        self.__DOM_Expression135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ArrayAccess134"):
                opp_val = getattr(old_value, "DOM_ArrayAccess134", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ArrayAccess134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ArrayAccess134"):
                opp_val = getattr(value, "DOM_ArrayAccess134", None)
                setattr(value, "DOM_ArrayAccess134", self)

    @property
    def DOM_Expression178(self):
        return self.__DOM_Expression178

    @DOM_Expression178.setter
    def DOM_Expression178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression178", None)
        self.__DOM_Expression178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_FieldAccess"):
                opp_val = getattr(old_value, "DOM_FieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "DOM_FieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_FieldAccess"):
                opp_val = getattr(value, "DOM_FieldAccess", None)
                setattr(value, "DOM_FieldAccess", self)

    @property
    def DOM_Expression221(self):
        return self.__DOM_Expression221

    @DOM_Expression221.setter
    def DOM_Expression221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression221", None)
        self.__DOM_Expression221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_SuperMethodInvocation"):
                opp_val = getattr(old_value, "DOM_SuperMethodInvocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_SuperMethodInvocation"):
                opp_val = getattr(value, "DOM_SuperMethodInvocation", None)
                if opp_val is None:
                    setattr(value, "DOM_SuperMethodInvocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression199(self):
        return self.__DOM_Expression199

    @DOM_Expression199.setter
    def DOM_Expression199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression199", None)
        self.__DOM_Expression199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_MethodInvocation198"):
                opp_val = getattr(old_value, "DOM_MethodInvocation198", None)
                if opp_val == self:
                    setattr(old_value, "DOM_MethodInvocation198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_MethodInvocation198"):
                opp_val = getattr(value, "DOM_MethodInvocation198", None)
                setattr(value, "DOM_MethodInvocation198", self)

    @property
    def DOM_Expression244(self):
        return self.__DOM_Expression244

    @DOM_Expression244.setter
    def DOM_Expression244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression244", None)
        self.__DOM_Expression244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_AssertStatement"):
                opp_val = getattr(old_value, "DOM_AssertStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_AssertStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_AssertStatement"):
                opp_val = getattr(value, "DOM_AssertStatement", None)
                setattr(value, "DOM_AssertStatement", self)

    @property
    def DOM_Expression344(self):
        return self.__DOM_Expression344

    @DOM_Expression344.setter
    def DOM_Expression344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression344", None)
        self.__DOM_Expression344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_WhileStatement343"):
                opp_val = getattr(old_value, "DOM_WhileStatement343", None)
                if opp_val == self:
                    setattr(old_value, "DOM_WhileStatement343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_WhileStatement343"):
                opp_val = getattr(value, "DOM_WhileStatement343", None)
                setattr(value, "DOM_WhileStatement343", self)

    @property
    def DOM_Expression321(self):
        return self.__DOM_Expression321

    @DOM_Expression321.setter
    def DOM_Expression321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression321", None)
        self.__DOM_Expression321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ThrowStatement"):
                opp_val = getattr(old_value, "DOM_ThrowStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ThrowStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ThrowStatement"):
                opp_val = getattr(value, "DOM_ThrowStatement", None)
                setattr(value, "DOM_ThrowStatement", self)

    @property
    def DOM_Expression273(self):
        return self.__DOM_Expression273

    @DOM_Expression273.setter
    def DOM_Expression273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression273", None)
        self.__DOM_Expression273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ExpressionStatement"):
                opp_val = getattr(old_value, "DOM_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "DOM_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ExpressionStatement"):
                opp_val = getattr(value, "DOM_ExpressionStatement", None)
                setattr(value, "DOM_ExpressionStatement", self)

    @property
    def DOM_Expression186(self):
        return self.__DOM_Expression186

    @DOM_Expression186.setter
    def DOM_Expression186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression186", None)
        self.__DOM_Expression186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_InfixExpression185"):
                opp_val = getattr(old_value, "DOM_InfixExpression185", None)
                if opp_val == self:
                    setattr(old_value, "DOM_InfixExpression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_InfixExpression185"):
                opp_val = getattr(value, "DOM_InfixExpression185", None)
                setattr(value, "DOM_InfixExpression185", self)

    @property
    def DOM_Expression137(self):
        return self.__DOM_Expression137

    @DOM_Expression137.setter
    def DOM_Expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression137", None)
        self.__DOM_Expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_ArrayCreation"):
                opp_val = getattr(old_value, "DOM_ArrayCreation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_ArrayCreation"):
                opp_val = getattr(value, "DOM_ArrayCreation", None)
                if opp_val is None:
                    setattr(value, "DOM_ArrayCreation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_Expression61(self):
        return self.__DOM_Expression61

    @DOM_Expression61.setter
    def DOM_Expression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression61", None)
        self.__DOM_Expression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_VariableDeclaration"):
                opp_val = getattr(old_value, "DOM_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "DOM_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_VariableDeclaration"):
                opp_val = getattr(value, "DOM_VariableDeclaration", None)
                setattr(value, "DOM_VariableDeclaration", self)

class DOM_Type(ASTNode):

    pass
class DOM_MethodRef(ASTNode):

    pass
class DOM_CatchClause(ASTNode):

    pass
class DOM_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, DOM_ImportDeclaration: "DOM_CompilationUnit" = None, DOM_ImportDeclaration21: "DOM_Name" = None):
        self.onDemand = onDemand
        self.static = static
        self.DOM_ImportDeclaration = DOM_ImportDeclaration
        self.DOM_ImportDeclaration21 = DOM_ImportDeclaration21
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def onDemand(self) -> str:
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: str):
        self.__onDemand = onDemand

    @property
    def DOM_ImportDeclaration(self):
        return self.__DOM_ImportDeclaration

    @DOM_ImportDeclaration.setter
    def DOM_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ImportDeclaration__DOM_ImportDeclaration", None)
        self.__DOM_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_CompilationUnit16"):
                opp_val = getattr(old_value, "DOM_CompilationUnit16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_CompilationUnit16"):
                opp_val = getattr(value, "DOM_CompilationUnit16", None)
                if opp_val is None:
                    setattr(value, "DOM_CompilationUnit16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_ImportDeclaration21(self):
        return self.__DOM_ImportDeclaration21

    @DOM_ImportDeclaration21.setter
    def DOM_ImportDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ImportDeclaration__DOM_ImportDeclaration21", None)
        self.__DOM_ImportDeclaration21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Name"):
                opp_val = getattr(old_value, "DOM_Name", None)
                if opp_val == self:
                    setattr(old_value, "DOM_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Name"):
                opp_val = getattr(value, "DOM_Name", None)
                setattr(value, "DOM_Name", self)

class DOM_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, DOM_TagElement: set["DOM_ASTNode"] = None, DOM_TagElement127: "DOM_Javadoc" = None):
        self.tagName = tagName
        self.nested = nested
        self.DOM_TagElement = DOM_TagElement if DOM_TagElement is not None else set()
        self.DOM_TagElement127 = DOM_TagElement127
        
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
    def DOM_TagElement127(self):
        return self.__DOM_TagElement127

    @DOM_TagElement127.setter
    def DOM_TagElement127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TagElement__DOM_TagElement127", None)
        self.__DOM_TagElement127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOM_Javadoc126"):
                opp_val = getattr(old_value, "DOM_Javadoc126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOM_Javadoc126"):
                opp_val = getattr(value, "DOM_Javadoc126", None)
                if opp_val is None:
                    setattr(value, "DOM_Javadoc126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DOM_TagElement(self):
        return self.__DOM_TagElement

    @DOM_TagElement.setter
    def DOM_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TagElement__DOM_TagElement", None)
        self.__DOM_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DOM_ASTNode54"):
                    opp_val = getattr(item, "DOM_ASTNode54", None)
                    
                    if opp_val == self:
                        setattr(item, "DOM_ASTNode54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DOM_ASTNode54"):
                    opp_val = getattr(item, "DOM_ASTNode54", None)
                    
                    setattr(item, "DOM_ASTNode54", self)
                    

class DOM_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class DOM_MemberValuePair(ASTNode):

    pass
class DOM_Comment(ASTNode):

    pass
class DOM_AnonymousClassDeclaration(ASTNode):

    pass