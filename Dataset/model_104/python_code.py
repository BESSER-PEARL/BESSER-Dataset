from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class Modifiers(Enum):
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
    enum = "enum"
    final = "final"
    interface = "interface"
    native = "native"
    private = "private"
    protected = "protected"
    public = "public"
    static = "static"
    strictfp = "strictfp"
class InfixExpressionOperatorKind(Enum):
    greater_equals = "greater_equals"
    or_ = "or_"
    right_shift_signed = "right_shift_signed"
    minus = "minus"
    xor = "xor"
    less_equals = "less_equals"
    equals = "equals"
    not_equals = "not_equals"
    and_ = "and_"
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
class PrefixExpressionOperatorKind(Enum):
    minus = "minus"
    not_ = "not_"
    decrement = "decrement"
    complement = "complement"
    increment = "increment"
    plus = "plus"
class PostfixExpressionOperatorKind(Enum):
    increment = "increment"
    decrement = "decrement"


############################################
# Definition of Classes
############################################

class Statement:

    pass
class DOM_Block(Statement):

    pass
class DOM_AssertStatement(Statement):

    pass
class ArrayType:

    pass
class TagElement:

    pass
class EnumConstantDeclaration:

    pass
class TypeParameter:

    pass
class ArrayInitializer:

    pass
class AnonymousClassDeclaration:

    pass
class VariableDeclarationFragment:

    pass
class Annotation:

    pass
class DOM_ExtendedModifier(ABC):

    pass
class Type:

    pass
class SimpleName:

    pass
class Name:

    pass
class AbstractTypeDeclaration:

    pass
class DOM_EnumDeclaration(AbstractTypeDeclaration):

    pass
class DOM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class DOM_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, DOM_TypeDeclaration: "Type" = None, DOM_TypeDeclaration160: set["Type"] = None, DOM_TypeDeclaration163: set["TypeParameter"] = None, AbstractTypeDeclaration: "DOM_CompilationUnit" = None, AbstractTypeDeclaration365: "DOM_TypeDeclarationStatement" = None):
        self.interface = interface
        self.DOM_TypeDeclaration = DOM_TypeDeclaration
        self.DOM_TypeDeclaration160 = DOM_TypeDeclaration160 if DOM_TypeDeclaration160 is not None else set()
        self.DOM_TypeDeclaration163 = DOM_TypeDeclaration163 if DOM_TypeDeclaration163 is not None else set()
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface


    @property
    def DOM_TypeDeclaration163(self):
        return self.__DOM_TypeDeclaration163

    @DOM_TypeDeclaration163.setter
    def DOM_TypeDeclaration163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration163", None)
        self.__DOM_TypeDeclaration163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter164"):
                    opp_val = getattr(item, "TypeParameter164", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter164"):
                    opp_val = getattr(item, "TypeParameter164", None)
                    
                    setattr(item, "TypeParameter164", self)
                    

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
            if hasattr(old_value, "Type158"):
                opp_val = getattr(old_value, "Type158", None)
                if opp_val == self:
                    setattr(old_value, "Type158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type158"):
                opp_val = getattr(value, "Type158", None)
                setattr(value, "Type158", self)

    @property
    def DOM_TypeDeclaration160(self):
        return self.__DOM_TypeDeclaration160

    @DOM_TypeDeclaration160.setter
    def DOM_TypeDeclaration160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration160", None)
        self.__DOM_TypeDeclaration160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type161"):
                    opp_val = getattr(item, "Type161", None)
                    
                    if opp_val == self:
                        setattr(item, "Type161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type161"):
                    opp_val = getattr(item, "Type161", None)
                    
                    setattr(item, "Type161", self)
                    

class ImportDeclaration:

    pass
class PackageDeclaration:

    pass
class Comment:

    pass
class DOM_LineComment(Comment):

    pass
class DOM_BlockComment(Comment):

    pass
class DOM_Javadoc(Comment):

    pass
class SingleVariableDeclaration:

    pass
class MethodRefParameter:

    pass
class Expression:

    pass
class DOM_CastExpression(Expression):

    pass
class DOM_ArrayAccess(Expression):

    pass
class DOM_NumberLiteral(Expression):

    def __init__(self, token: str, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.token = token
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


class DOM_PrefixExpression(Expression):

    def __init__(self, operator: str, DOM_PrefixExpression: "Expression" = None, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.operator = operator
        self.DOM_PrefixExpression = DOM_PrefixExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "Expression250"):
                opp_val = getattr(old_value, "Expression250", None)
                if opp_val == self:
                    setattr(old_value, "Expression250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression250"):
                opp_val = getattr(value, "Expression250", None)
                setattr(value, "Expression250", self)

class DOM_CharacterLiteral(Expression):

    def __init__(self, charValue: str, escapedValue: str, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.charValue = charValue
        self.escapedValue = escapedValue
        
        pass
    @property
    def charValue(self):
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue


    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


class DOM_Name(Expression):

    def __init__(self, fullyQualifiedName: str, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.fullyQualifiedName = fullyQualifiedName
        
        pass
    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


class DOM_ParenthesizedExpression(Expression):

    pass
class DOM_ArrayInitializer(Expression):

    pass
class DOM_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.escapedValue = escapedValue
        self.literalValue = literalValue
        
        pass
    @property
    def literalValue(self):
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue


    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


class DOM_SuperFieldAccess(Expression):

    pass
class DOM_FieldAccess(Expression):

    pass
class DOM_PostfixExpression(Expression):

    def __init__(self, operator: str, DOM_PostfixExpression: "Expression" = None, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.operator = operator
        self.DOM_PostfixExpression = DOM_PostfixExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "Expression248"):
                opp_val = getattr(old_value, "Expression248", None)
                if opp_val == self:
                    setattr(old_value, "Expression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression248"):
                opp_val = getattr(value, "Expression248", None)
                setattr(value, "Expression248", self)

class DOM_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue


class DOM_NullLiteral(Expression):

    pass
class DOM_ClassInstanceCreation(Expression):

    pass
class DOM_MethodInvocation(Expression):

    pass
class DOM_InstanceofExpression(Expression):

    pass
class DOM_ConditionalExpression(Expression):

    pass
class DOM_ArrayCreation(Expression):

    pass
class DOM_Assignment(Expression):

    def __init__(self, operator: str, DOM_Assignment: "Expression" = None, DOM_Assignment184: "Expression" = None, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.operator = operator
        self.DOM_Assignment = DOM_Assignment
        self.DOM_Assignment184 = DOM_Assignment184
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def DOM_Assignment184(self):
        return self.__DOM_Assignment184

    @DOM_Assignment184.setter
    def DOM_Assignment184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Assignment__DOM_Assignment184", None)
        self.__DOM_Assignment184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression185"):
                opp_val = getattr(old_value, "Expression185", None)
                if opp_val == self:
                    setattr(old_value, "Expression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression185"):
                opp_val = getattr(value, "Expression185", None)
                setattr(value, "Expression185", self)

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
            if hasattr(old_value, "Expression182"):
                opp_val = getattr(old_value, "Expression182", None)
                if opp_val == self:
                    setattr(old_value, "Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression182"):
                opp_val = getattr(value, "Expression182", None)
                setattr(value, "Expression182", self)

class DOM_InfixExpression(Expression):

    def __init__(self, operator: str, DOM_InfixExpression: set["Expression"] = None, DOM_InfixExpression221: "Expression" = None, DOM_InfixExpression224: "Expression" = None, Expression169: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression206: "DOM_ConditionalExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression209: "DOM_ConditionalExpression" = None, Expression212: "DOM_ConditionalExpression" = None, Expression319: "DOM_ForStatement" = None, Expression180: "DOM_ArrayInitializer" = None, Expression283: "DOM_AssertStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression298: "DOM_DoStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression280: "DOM_AssertStatement" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression324: "DOM_IfStatement" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression346: "DOM_SwitchStatement" = None, Expression344: "DOM_SwitchCase" = None, Expression: "DOM_MemberValuePair" = None, Expression104: "DOM_VariableDeclaration" = None, Expression214: "DOM_FieldAccess" = None, Expression308: "DOM_ExpressionStatement" = None, Expression187: "DOM_CastExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression313: "DOM_ForStatement" = None, Expression378: "DOM_WhileStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression222: "DOM_InfixExpression" = None, Expression185: "DOM_Assignment" = None, Expression232: "DOM_MethodInvocation" = None, Expression172: "DOM_ArrayAccess" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression316: "DOM_ForStatement" = None, Expression227: "DOM_InstanceofExpression" = None, Expression248: "DOM_PostfixExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression174: "DOM_ArrayCreation" = None, Expression235: "DOM_MethodInvocation" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression225: "DOM_InfixExpression" = None, Expression182: "DOM_Assignment" = None):
        self.operator = operator
        self.DOM_InfixExpression = DOM_InfixExpression if DOM_InfixExpression is not None else set()
        self.DOM_InfixExpression221 = DOM_InfixExpression221
        self.DOM_InfixExpression224 = DOM_InfixExpression224
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def DOM_InfixExpression224(self):
        return self.__DOM_InfixExpression224

    @DOM_InfixExpression224.setter
    def DOM_InfixExpression224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression224", None)
        self.__DOM_InfixExpression224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression225"):
                opp_val = getattr(old_value, "Expression225", None)
                if opp_val == self:
                    setattr(old_value, "Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression225"):
                opp_val = getattr(value, "Expression225", None)
                setattr(value, "Expression225", self)

    @property
    def DOM_InfixExpression221(self):
        return self.__DOM_InfixExpression221

    @DOM_InfixExpression221.setter
    def DOM_InfixExpression221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression221", None)
        self.__DOM_InfixExpression221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression222"):
                opp_val = getattr(old_value, "Expression222", None)
                if opp_val == self:
                    setattr(old_value, "Expression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression222"):
                opp_val = getattr(value, "Expression222", None)
                setattr(value, "Expression222", self)

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
                if hasattr(item, "Expression219"):
                    opp_val = getattr(item, "Expression219", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression219"):
                    opp_val = getattr(item, "Expression219", None)
                    
                    setattr(item, "Expression219", self)
                    

class DOM_SuperMethodInvocation(Expression):

    pass
class Core_Parameter:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Parameter:

    pass
class DOM_SingleMemberAnnotation(Annotation):

    pass
class MemberValuePair:

    pass
class VariableDeclaration:

    pass
class DOM_VariableDeclarationFragment(VariableDeclaration):

    pass
class DOM_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, DOM_SingleVariableDeclaration: "Type" = None, DOM_SingleVariableDeclaration401: set["ExtendedModifier"] = None):
        self.varargs = varargs
        self.DOM_SingleVariableDeclaration = DOM_SingleVariableDeclaration
        self.DOM_SingleVariableDeclaration401 = DOM_SingleVariableDeclaration401 if DOM_SingleVariableDeclaration401 is not None else set()
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


    @property
    def DOM_SingleVariableDeclaration401(self):
        return self.__DOM_SingleVariableDeclaration401

    @DOM_SingleVariableDeclaration401.setter
    def DOM_SingleVariableDeclaration401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration401", None)
        self.__DOM_SingleVariableDeclaration401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtendedModifier402"):
                    opp_val = getattr(item, "ExtendedModifier402", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtendedModifier402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtendedModifier402"):
                    opp_val = getattr(item, "ExtendedModifier402", None)
                    
                    setattr(item, "ExtendedModifier402", self)
                    

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
            if hasattr(old_value, "Type399"):
                opp_val = getattr(old_value, "Type399", None)
                if opp_val == self:
                    setattr(old_value, "Type399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type399"):
                opp_val = getattr(value, "Type399", None)
                setattr(value, "Type399", self)

class DOM_WildcardType(Type):

    def __init__(self, upperBound: str, DOM_WildcardType: "Type" = None, Type230: "DOM_InstanceofExpression" = None, Type380: "DOM_ArrayType" = None, Type158: "DOM_TypeDeclaration" = None, Type102: "DOM_TypeParameter" = None, Type201: "DOM_ClassInstanceCreation" = None, Type161: "DOM_TypeDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type397: "DOM_WildcardType" = None, Type270: "DOM_TypeLiteral" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type131: "DOM_FieldDeclaration" = None, Type385: "DOM_ParameterizedType" = None, Type190: "DOM_CastExpression" = None, Type266: "DOM_SuperMethodInvocation" = None, Type388: "DOM_ParameterizedType" = None, Type383: "DOM_ArrayType" = None, Type141: "DOM_MethodDeclaration" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type241: "DOM_MethodInvocation" = None, Type: "DOM_MethodRefParameter" = None, Type204: "DOM_ClassInstanceCreation" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type291: "DOM_ConstructorInvocation" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type393: "DOM_QualifiedType" = None):
        self.upperBound = upperBound
        self.DOM_WildcardType = DOM_WildcardType
        
        pass
    @property
    def upperBound(self):
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
            if hasattr(old_value, "Type397"):
                opp_val = getattr(old_value, "Type397", None)
                if opp_val == self:
                    setattr(old_value, "Type397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type397"):
                opp_val = getattr(value, "Type397", None)
                setattr(value, "Type397", self)

class DOM_SimpleType(Type):

    pass
class DOM_NormalAnnotation(Annotation):

    pass
class DOM_MarkerAnnotation(Annotation):

    pass
class DOM_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, Name167: "DOM_Annotation" = None, Name407: "DOM_QualifiedName" = None, Name260: "DOM_SuperMethodInvocation" = None, Name255: "DOM_SuperFieldAccess" = None, Name395: "DOM_SimpleType" = None, Name70: "DOM_MemberRef" = None, Name79: "DOM_MethodRef" = None, Name92: "DOM_PackageDeclaration" = None, Name147: "DOM_MethodDeclaration" = None, Name268: "DOM_ThisExpression" = None, Name: "DOM_ImportDeclaration" = None, Name263: "DOM_SuperMethodInvocation" = None):
        self.identifier = identifier
        self.declaration = declaration
        
        pass
    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class DOM_QualifiedName(Name):

    pass
class DOM_ParameterizedType(Type):

    pass
class DOM_ArrayType(Type):

    def __init__(self, dimensions: str, DOM_ArrayType: "Type" = None, DOM_ArrayType382: "Type" = None, Type230: "DOM_InstanceofExpression" = None, Type380: "DOM_ArrayType" = None, Type158: "DOM_TypeDeclaration" = None, Type102: "DOM_TypeParameter" = None, Type201: "DOM_ClassInstanceCreation" = None, Type161: "DOM_TypeDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type397: "DOM_WildcardType" = None, Type270: "DOM_TypeLiteral" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type131: "DOM_FieldDeclaration" = None, Type385: "DOM_ParameterizedType" = None, Type190: "DOM_CastExpression" = None, Type266: "DOM_SuperMethodInvocation" = None, Type388: "DOM_ParameterizedType" = None, Type383: "DOM_ArrayType" = None, Type141: "DOM_MethodDeclaration" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type241: "DOM_MethodInvocation" = None, Type: "DOM_MethodRefParameter" = None, Type204: "DOM_ClassInstanceCreation" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type291: "DOM_ConstructorInvocation" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type393: "DOM_QualifiedType" = None):
        self.dimensions = dimensions
        self.DOM_ArrayType = DOM_ArrayType
        self.DOM_ArrayType382 = DOM_ArrayType382
        
        pass
    @property
    def dimensions(self):
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
            if hasattr(old_value, "Type380"):
                opp_val = getattr(old_value, "Type380", None)
                if opp_val == self:
                    setattr(old_value, "Type380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type380"):
                opp_val = getattr(value, "Type380", None)
                setattr(value, "Type380", self)

    @property
    def DOM_ArrayType382(self):
        return self.__DOM_ArrayType382

    @DOM_ArrayType382.setter
    def DOM_ArrayType382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType382", None)
        self.__DOM_ArrayType382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type383"):
                opp_val = getattr(old_value, "Type383", None)
                if opp_val == self:
                    setattr(old_value, "Type383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type383"):
                opp_val = getattr(value, "Type383", None)
                setattr(value, "Type383", self)

class DOM_WhileStatement(Statement):

    pass
class DOM_QualifiedType(Type):

    pass
class DOM_PrimitiveType(Type):

    def __init__(self, code: str, Type230: "DOM_InstanceofExpression" = None, Type380: "DOM_ArrayType" = None, Type158: "DOM_TypeDeclaration" = None, Type102: "DOM_TypeParameter" = None, Type201: "DOM_ClassInstanceCreation" = None, Type161: "DOM_TypeDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type397: "DOM_WildcardType" = None, Type270: "DOM_TypeLiteral" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type131: "DOM_FieldDeclaration" = None, Type385: "DOM_ParameterizedType" = None, Type190: "DOM_CastExpression" = None, Type266: "DOM_SuperMethodInvocation" = None, Type388: "DOM_ParameterizedType" = None, Type383: "DOM_ArrayType" = None, Type141: "DOM_MethodDeclaration" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type241: "DOM_MethodInvocation" = None, Type: "DOM_MethodRefParameter" = None, Type204: "DOM_ClassInstanceCreation" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type291: "DOM_ConstructorInvocation" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type393: "DOM_QualifiedType" = None):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class CatchClause:

    pass
class DOM_TryStatement(Statement):

    pass
class DOM_ThrowStatement(Statement):

    pass
class DOM_SynchronizedStatement(Statement):

    pass
class DOM_VariableDeclarationStatement(Statement):

    pass
class DOM_TypeDeclarationStatement(Statement):

    pass
class DOM_SwitchCase(Statement):

    def __init__(self, default: str, DOM_SwitchCase: "Expression" = None, Statement300: "DOM_EnhancedForStatement" = None, Statement: "DOM_Block" = None, Statement321: "DOM_IfStatement" = None, Statement310: "DOM_ForStatement" = None, Statement349: "DOM_SwitchStatement" = None, Statement327: "DOM_IfStatement" = None, Statement329: "DOM_LabeledStatement" = None, Statement295: "DOM_DoStatement" = None, Statement375: "DOM_WhileStatement" = None):
        self.default = default
        self.DOM_SwitchCase = DOM_SwitchCase
        
        pass
    @property
    def default(self):
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
            if hasattr(old_value, "Expression344"):
                opp_val = getattr(old_value, "Expression344", None)
                if opp_val == self:
                    setattr(old_value, "Expression344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression344"):
                opp_val = getattr(value, "Expression344", None)
                setattr(value, "Expression344", self)

class DOM_SuperConstructorInvocation(Statement):

    pass
class DOM_ReturnStatement(Statement):

    pass
class DOM_SwitchStatement(Statement):

    pass
class DOM_IfStatement(Statement):

    pass
class DOM_ForStatement(Statement):

    pass
class DOM_LabeledStatement(Statement):

    pass
class DOM_DoStatement(Statement):

    pass
class DOM_ContinueStatement(Statement):

    pass
class DOM_ConstructorInvocation(Statement):

    pass
class DOM_BreakStatement(Statement):

    pass
class DOM_ExpressionStatement(Statement):

    pass
class DOM_EnhancedForStatement(Statement):

    pass
class DOM_EmptyStatement(Statement):

    pass
class DOM_VariableDeclarationExpression(Expression):

    pass
class DOM_TypeLiteral(Expression):

    pass
class DOM_ThisExpression(Expression):

    pass
class Block:

    pass
class Javadoc:

    pass
class ExtendedModifier:

    pass
class DOM_Annotation(ExtendedModifier, Expression):

    pass
class BodyDeclaration:

    pass
class DOM_EnumConstantDeclaration(BodyDeclaration):

    pass
class DOM_Initializer(BodyDeclaration):

    pass
class DOM_FieldDeclaration(BodyDeclaration):

    pass
class DOM_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, DOM_MethodDeclaration143: set["SingleVariableDeclaration"] = None, DOM_MethodDeclaration146: set["Name"] = None, DOM_MethodDeclaration149: set["TypeParameter"] = None, DOM_MethodDeclaration151: "IMethod" = None, DOM_MethodDeclaration: "Block" = None, DOM_MethodDeclaration137: "SimpleName" = None, DOM_MethodDeclaration140: "Type" = None, BodyDeclaration: "DOM_AnonymousClassDeclaration" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration" = None):
        self.extraDimensions = extraDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.DOM_MethodDeclaration143 = DOM_MethodDeclaration143 if DOM_MethodDeclaration143 is not None else set()
        self.DOM_MethodDeclaration146 = DOM_MethodDeclaration146 if DOM_MethodDeclaration146 is not None else set()
        self.DOM_MethodDeclaration149 = DOM_MethodDeclaration149 if DOM_MethodDeclaration149 is not None else set()
        self.DOM_MethodDeclaration151 = DOM_MethodDeclaration151
        self.DOM_MethodDeclaration = DOM_MethodDeclaration
        self.DOM_MethodDeclaration137 = DOM_MethodDeclaration137
        self.DOM_MethodDeclaration140 = DOM_MethodDeclaration140
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor


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
            if hasattr(old_value, "Block135"):
                opp_val = getattr(old_value, "Block135", None)
                if opp_val == self:
                    setattr(old_value, "Block135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Block135"):
                opp_val = getattr(value, "Block135", None)
                setattr(value, "Block135", self)

    @property
    def DOM_MethodDeclaration140(self):
        return self.__DOM_MethodDeclaration140

    @DOM_MethodDeclaration140.setter
    def DOM_MethodDeclaration140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration140", None)
        self.__DOM_MethodDeclaration140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type141"):
                opp_val = getattr(old_value, "Type141", None)
                if opp_val == self:
                    setattr(old_value, "Type141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type141"):
                opp_val = getattr(value, "Type141", None)
                setattr(value, "Type141", self)

    @property
    def DOM_MethodDeclaration151(self):
        return self.__DOM_MethodDeclaration151

    @DOM_MethodDeclaration151.setter
    def DOM_MethodDeclaration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration151", None)
        self.__DOM_MethodDeclaration151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IMethod152"):
                opp_val = getattr(old_value, "IMethod152", None)
                if opp_val == self:
                    setattr(old_value, "IMethod152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IMethod152"):
                opp_val = getattr(value, "IMethod152", None)
                setattr(value, "IMethod152", self)

    @property
    def DOM_MethodDeclaration149(self):
        return self.__DOM_MethodDeclaration149

    @DOM_MethodDeclaration149.setter
    def DOM_MethodDeclaration149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration149", None)
        self.__DOM_MethodDeclaration149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter"):
                    opp_val = getattr(item, "TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter"):
                    opp_val = getattr(item, "TypeParameter", None)
                    
                    setattr(item, "TypeParameter", self)
                    

    @property
    def DOM_MethodDeclaration146(self):
        return self.__DOM_MethodDeclaration146

    @DOM_MethodDeclaration146.setter
    def DOM_MethodDeclaration146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration146", None)
        self.__DOM_MethodDeclaration146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Name147"):
                    opp_val = getattr(item, "Name147", None)
                    
                    if opp_val == self:
                        setattr(item, "Name147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Name147"):
                    opp_val = getattr(item, "Name147", None)
                    
                    setattr(item, "Name147", self)
                    

    @property
    def DOM_MethodDeclaration143(self):
        return self.__DOM_MethodDeclaration143

    @DOM_MethodDeclaration143.setter
    def DOM_MethodDeclaration143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration143", None)
        self.__DOM_MethodDeclaration143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableDeclaration144"):
                    opp_val = getattr(item, "SingleVariableDeclaration144", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableDeclaration144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableDeclaration144"):
                    opp_val = getattr(item, "SingleVariableDeclaration144", None)
                    
                    setattr(item, "SingleVariableDeclaration144", self)
                    

    @property
    def DOM_MethodDeclaration137(self):
        return self.__DOM_MethodDeclaration137

    @DOM_MethodDeclaration137.setter
    def DOM_MethodDeclaration137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration137", None)
        self.__DOM_MethodDeclaration137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName138"):
                opp_val = getattr(old_value, "SimpleName138", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName138"):
                opp_val = getattr(value, "SimpleName138", None)
                setattr(value, "SimpleName138", self)

class DOM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class DOM_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, DOM_AbstractTypeDeclaration: set["BodyDeclaration"] = None, DOM_AbstractTypeDeclaration111: "SimpleName" = None, BodyDeclaration: "DOM_AnonymousClassDeclaration" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.DOM_AbstractTypeDeclaration = DOM_AbstractTypeDeclaration if DOM_AbstractTypeDeclaration is not None else set()
        self.DOM_AbstractTypeDeclaration111 = DOM_AbstractTypeDeclaration111
        
        pass
    @property
    def memberTypeDeclaration(self):
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration


    @property
    def packageMemberTypeDeclaration(self):
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration


    @property
    def localTypeDeclaration(self):
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration


    @property
    def DOM_AbstractTypeDeclaration111(self):
        return self.__DOM_AbstractTypeDeclaration111

    @DOM_AbstractTypeDeclaration111.setter
    def DOM_AbstractTypeDeclaration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration111", None)
        self.__DOM_AbstractTypeDeclaration111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName112"):
                opp_val = getattr(old_value, "SimpleName112", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName112"):
                opp_val = getattr(value, "SimpleName112", None)
                setattr(value, "SimpleName112", self)

    @property
    def DOM_AbstractTypeDeclaration(self):
        return self.__DOM_AbstractTypeDeclaration

    @DOM_AbstractTypeDeclaration.setter
    def DOM_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration", None)
        self.__DOM_AbstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BodyDeclaration109"):
                    opp_val = getattr(item, "BodyDeclaration109", None)
                    
                    if opp_val == self:
                        setattr(item, "BodyDeclaration109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BodyDeclaration109"):
                    opp_val = getattr(item, "BodyDeclaration109", None)
                    
                    setattr(item, "BodyDeclaration109", self)
                    

class DOM_ASTNode(ABC):

    pass
class ASTNode:

    pass
class DOM_TypeParameter(ASTNode):

    pass
class DOM_PackageDeclaration(ASTNode):

    pass
class DOM_Type(ASTNode):

    pass
class DOM_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, DOM_VariableDeclaration: "Expression" = None, DOM_VariableDeclaration106: "SimpleName" = None, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.extraDimensions = extraDimensions
        self.DOM_VariableDeclaration = DOM_VariableDeclaration
        self.DOM_VariableDeclaration106 = DOM_VariableDeclaration106
        
        pass
    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


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
            if hasattr(old_value, "Expression104"):
                opp_val = getattr(old_value, "Expression104", None)
                if opp_val == self:
                    setattr(old_value, "Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression104"):
                opp_val = getattr(value, "Expression104", None)
                setattr(value, "Expression104", self)

    @property
    def DOM_VariableDeclaration106(self):
        return self.__DOM_VariableDeclaration106

    @DOM_VariableDeclaration106.setter
    def DOM_VariableDeclaration106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_VariableDeclaration__DOM_VariableDeclaration106", None)
        self.__DOM_VariableDeclaration106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName107"):
                opp_val = getattr(old_value, "SimpleName107", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName107"):
                opp_val = getattr(value, "SimpleName107", None)
                setattr(value, "SimpleName107", self)

class DOM_MethodRef(ASTNode):

    pass
class DOM_MemberValuePair(ASTNode):

    pass
class DOM_Statement(ASTNode):

    pass
class DOM_Comment(ASTNode):

    pass
class DOM_TextElement(ASTNode):

    def __init__(self, text: str, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class DOM_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, DOM_MethodRefParameter: "SimpleName" = None, DOM_MethodRefParameter85: "Type" = None, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.varargs = varargs
        self.DOM_MethodRefParameter = DOM_MethodRefParameter
        self.DOM_MethodRefParameter85 = DOM_MethodRefParameter85
        
        pass
    @property
    def varargs(self):
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
            if hasattr(old_value, "SimpleName83"):
                opp_val = getattr(old_value, "SimpleName83", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName83"):
                opp_val = getattr(value, "SimpleName83", None)
                setattr(value, "SimpleName83", self)

    @property
    def DOM_MethodRefParameter85(self):
        return self.__DOM_MethodRefParameter85

    @DOM_MethodRefParameter85.setter
    def DOM_MethodRefParameter85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter85", None)
        self.__DOM_MethodRefParameter85 = value
        
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

class DOM_AnonymousClassDeclaration(ASTNode):

    pass
class DOM_MemberRef(ASTNode):

    pass
class DOM_CompilationUnit(ASTNode):

    pass
class DOM_CatchClause(ASTNode):

    pass
class DOM_BodyDeclaration(ASTNode):

    pass
class DOM_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, DOM_ImportDeclaration: "Name" = None, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.onDemand = onDemand
        self.static = static
        self.DOM_ImportDeclaration = DOM_ImportDeclaration
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def onDemand(self):
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
            if hasattr(old_value, "Name"):
                opp_val = getattr(old_value, "Name", None)
                if opp_val == self:
                    setattr(old_value, "Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name"):
                opp_val = getattr(value, "Name", None)
                setattr(value, "Name", self)

class DOM_Modifier(ExtendedModifier, ASTNode):

    def __init__(self, abstract: str, final: str, native: str, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None, ExtendedModifier275: "DOM_VariableDeclarationExpression" = None, ExtendedModifier: "DOM_BodyDeclaration" = None, ExtendedModifier402: "DOM_SingleVariableDeclaration" = None, ExtendedModifier370: "DOM_VariableDeclarationStatement" = None):
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
        
        pass
    @property
    def none(self):
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final


    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private


    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized


    @property
    def native(self):
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def strictfp(self):
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp


    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


class DOM_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, DOM_TagElement: set["ASTNode"] = None, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.tagName = tagName
        self.nested = nested
        self.DOM_TagElement = DOM_TagElement if DOM_TagElement is not None else set()
        
        pass
    @property
    def tagName(self):
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName


    @property
    def nested(self):
        return self.__nested

    @nested.setter
    def nested(self, nested: str):
        self.__nested = nested


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
                if hasattr(item, "ASTNode97"):
                    opp_val = getattr(item, "ASTNode97", None)
                    
                    if opp_val == self:
                        setattr(item, "ASTNode97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASTNode97"):
                    opp_val = getattr(item, "ASTNode97", None)
                    
                    setattr(item, "ASTNode97", self)
                    

class DOM_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, DOM_Expression: "IType" = None, ASTNode97: "DOM_TagElement" = None, ASTNode56: "DOM_Comment" = None, ASTNode: "DOM_AST" = None):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        self.DOM_Expression = DOM_Expression
        
        pass
    @property
    def resolveUnboxing(self):
        return self.__resolveUnboxing

    @resolveUnboxing.setter
    def resolveUnboxing(self, resolveUnboxing: str):
        self.__resolveUnboxing = resolveUnboxing


    @property
    def resolveBoxing(self):
        return self.__resolveBoxing

    @resolveBoxing.setter
    def resolveBoxing(self, resolveBoxing: str):
        self.__resolveBoxing = resolveBoxing


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
            if hasattr(old_value, "IType65"):
                opp_val = getattr(old_value, "IType65", None)
                if opp_val == self:
                    setattr(old_value, "IType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType65"):
                opp_val = getattr(value, "IType65", None)
                setattr(value, "IType65", self)

class DOM_AST:

    pass
class Core_ISourceRange:

    def __init__(self, length: str, offset: str):
        self.length = length
        self.offset = offset
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


class ISourceRange:

    pass
class Core_ISourceReference(ABC):

    def __init__(self, source: str, Core_ISourceReference: "ISourceRange" = None):
        self.source = source
        self.Core_ISourceReference = Core_ISourceReference
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def Core_ISourceReference(self):
        return self.__Core_ISourceReference

    @Core_ISourceReference.setter
    def Core_ISourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceReference__Core_ISourceReference", None)
        self.__Core_ISourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISourceRange"):
                opp_val = getattr(old_value, "ISourceRange", None)
                if opp_val == self:
                    setattr(old_value, "ISourceRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISourceRange"):
                opp_val = getattr(value, "ISourceRange", None)
                setattr(value, "ISourceRange", self)

class CompilationUnit:

    pass
class ITypeParameter:

    pass
class IMethod:

    pass
class IField:

    pass
class IInitializer:

    pass
class IMember:

    pass
class Core_IInitializer(IMember):

    pass
class Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        
        pass
    @property
    def typeSignature(self):
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature


    @property
    def isTransient(self):
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient


    @property
    def isVolatile(self):
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile


    @property
    def isEnumConstant(self):
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant


    @property
    def constant(self):
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant


class Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, Core_IMethod: set["Parameter"] = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.Core_IMethod = Core_IMethod if Core_IMethod is not None else set()
        
        pass
    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def isConstructor(self):
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor


    @property
    def isMainMethod(self):
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod


    @property
    def exceptionTypes(self):
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes


    @property
    def Core_IMethod(self):
        return self.__Core_IMethod

    @Core_IMethod.setter
    def Core_IMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod", None)
        self.__Core_IMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, Core_IType: set["IInitializer"] = None, Core_IType38: set["IField"] = None, Core_IType40: set["IMethod"] = None, Core_IType42: set["IType"] = None, Core_IType45: set["ITypeParameter"] = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.Core_IType = Core_IType if Core_IType is not None else set()
        self.Core_IType38 = Core_IType38 if Core_IType38 is not None else set()
        self.Core_IType40 = Core_IType40 if Core_IType40 is not None else set()
        self.Core_IType42 = Core_IType42 if Core_IType42 is not None else set()
        self.Core_IType45 = Core_IType45 if Core_IType45 is not None else set()
        
        pass
    @property
    def fullyQualifiedParametrizedName(self):
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName


    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


    @property
    def Core_IType45(self):
        return self.__Core_IType45

    @Core_IType45.setter
    def Core_IType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType45", None)
        self.__Core_IType45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ITypeParameter"):
                    opp_val = getattr(item, "ITypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ITypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ITypeParameter"):
                    opp_val = getattr(item, "ITypeParameter", None)
                    
                    setattr(item, "ITypeParameter", self)
                    

    @property
    def Core_IType(self):
        return self.__Core_IType

    @Core_IType.setter
    def Core_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType", None)
        self.__Core_IType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IInitializer"):
                    opp_val = getattr(item, "IInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "IInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IInitializer"):
                    opp_val = getattr(item, "IInitializer", None)
                    
                    setattr(item, "IInitializer", self)
                    

    @property
    def Core_IType42(self):
        return self.__Core_IType42

    @Core_IType42.setter
    def Core_IType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType42", None)
        self.__Core_IType42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IType43"):
                    opp_val = getattr(item, "IType43", None)
                    
                    if opp_val == self:
                        setattr(item, "IType43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IType43"):
                    opp_val = getattr(item, "IType43", None)
                    
                    setattr(item, "IType43", self)
                    

    @property
    def Core_IType40(self):
        return self.__Core_IType40

    @Core_IType40.setter
    def Core_IType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType40", None)
        self.__Core_IType40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IMethod"):
                    opp_val = getattr(item, "IMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "IMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IMethod"):
                    opp_val = getattr(item, "IMethod", None)
                    
                    setattr(item, "IMethod", self)
                    

    @property
    def Core_IType38(self):
        return self.__Core_IType38

    @Core_IType38.setter
    def Core_IType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType38", None)
        self.__Core_IType38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IField"):
                    opp_val = getattr(item, "IField", None)
                    
                    if opp_val == self:
                        setattr(item, "IField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IField"):
                    opp_val = getattr(item, "IField", None)
                    
                    setattr(item, "IField", self)
                    

class IPackageFragment:

    pass
class IJavaElement:

    pass
class IPackageFragmentRoot:

    pass
class Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class IJavaProject:

    pass
class PhysicalElement:

    pass
class Core_IJavaProject(PhysicalElement, IJavaElement):

    pass
class Core_IPackageFragmentRoot(PhysicalElement, IJavaElement):

    pass
class Core_IPackageFragment(PhysicalElement, IJavaElement):

    def __init__(self, isDefaultPackage: str, packageFragments: "IPackageFragmentRoot" = None, Core_IPackageFragment: set["IClassFile"] = None, Core_IPackageFragment16: set["ICompilationUnit"] = None):
        self.isDefaultPackage = isDefaultPackage
        self.packageFragments = packageFragments
        self.Core_IPackageFragment = Core_IPackageFragment if Core_IPackageFragment is not None else set()
        self.Core_IPackageFragment16 = Core_IPackageFragment16 if Core_IPackageFragment16 is not None else set()
        
        pass
    @property
    def isDefaultPackage(self):
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
        old_value = getattr(self, f"_Core_IPackageFragment__packageFragments", None)
        self.__packageFragments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IPackageFragmentRoot13"):
                opp_val = getattr(old_value, "IPackageFragmentRoot13", None)
                if opp_val == self:
                    setattr(old_value, "IPackageFragmentRoot13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IPackageFragmentRoot13"):
                opp_val = getattr(value, "IPackageFragmentRoot13", None)
                setattr(value, "IPackageFragmentRoot13", self)

    @property
    def Core_IPackageFragment16(self):
        return self.__Core_IPackageFragment16

    @Core_IPackageFragment16.setter
    def Core_IPackageFragment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment16", None)
        self.__Core_IPackageFragment16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ICompilationUnit"):
                    opp_val = getattr(item, "ICompilationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "ICompilationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ICompilationUnit"):
                    opp_val = getattr(item, "ICompilationUnit", None)
                    
                    setattr(item, "ICompilationUnit", self)
                    

    @property
    def Core_IPackageFragment(self):
        return self.__Core_IPackageFragment

    @Core_IPackageFragment.setter
    def Core_IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment", None)
        self.__Core_IPackageFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IClassFile"):
                    opp_val = getattr(item, "IClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "IClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IClassFile"):
                    opp_val = getattr(item, "IClassFile", None)
                    
                    setattr(item, "IClassFile", self)
                    

class Core_IJavaModel(PhysicalElement):

    pass
class Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


class IImportDeclaration:

    pass
class IType:

    pass
class ITypeRoot:

    pass
class Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, Core_IClassFile: "IType" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.Core_IClassFile = Core_IClassFile
        
        pass
    @property
    def isInterface(self):
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface


    @property
    def isClass(self):
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass


    @property
    def Core_IClassFile(self):
        return self.__Core_IClassFile

    @Core_IClassFile.setter
    def Core_IClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile", None)
        self.__Core_IClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IType29"):
                opp_val = getattr(old_value, "IType29", None)
                if opp_val == self:
                    setattr(old_value, "IType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType29"):
                opp_val = getattr(value, "IType29", None)
                setattr(value, "IType29", self)

class Core_ICompilationUnit(ITypeRoot):

    pass
class ISourceReference:

    pass
class Core_IImportDeclaration(IJavaElement, ISourceReference):

    def __init__(self, isOnDemand: str, isStatic: str):
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        
        pass
    @property
    def isOnDemand(self):
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic


class Core_ITypeParameter(IJavaElement, ISourceReference):

    def __init__(self, bounds: str):
        self.bounds = bounds
        
        pass
    @property
    def bounds(self):
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds


class Core_IMember(IJavaElement, ISourceReference):

    pass
class Core_ITypeRoot(PhysicalElement, IJavaElement, ISourceReference):

    pass
class ICompilationUnit:

    pass
class IClassFile:

    pass
class Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
        pass
    @property
    def elementName(self):
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

