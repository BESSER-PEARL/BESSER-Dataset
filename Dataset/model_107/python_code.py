from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PostfixExpresssionOperatorKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class InfixExpressionOperatorKind(Enum):
    GREATER_EQUALS = "GREATER_EQUALS"
    OR = "OR"
    RIGHT_SHIFT_SIGNED = "RIGHT_SHIFT_SIGNED"
    MINUS = "MINUS"
    XOR = "XOR"
    LESS_EQUALS = "LESS_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    AND = "AND"
    PLUS = "PLUS"
    GREATER = "GREATER"
    CONDITIONAL_OR = "CONDITIONAL_OR"
    REMAINDER = "REMAINDER"
    LESS = "LESS"
    LEFT_SHIFT = "LEFT_SHIFT"
    RIGHT_SHIFT_UNSIGNED = "RIGHT_SHIFT_UNSIGNED"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
class AssignementOperatorKind(Enum):
    RIGHT_SHIFT_SIGNED_ASSIGN = "RIGHT_SHIFT_SIGNED_ASSIGN"
    BIT_XOR_ASSIGN = "BIT_XOR_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    LEFT_SHIFT_ASSIGN = "LEFT_SHIFT_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    ASSIGN = "ASSIGN"
    RIGHT_SHIFT_UNSIGNED_ASSIGN = "RIGHT_SHIFT_UNSIGNED_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    BIT_AND_ASSIGN = "BIT_AND_ASSIGN"
class PrefixExpresssionOperatorKind(Enum):
    NOT = "NOT"
    DECREMENT = "DECREMENT"
    COMPLEMENT = "COMPLEMENT"
    INCREMENT = "INCREMENT"
    PLUS = "PLUS"
    MINUS = "MINUS"


############################################
# Definition of Classes
############################################

class MemberValuePair:

    pass
class VariableDeclaration:

    pass
class JavaAbstractSyntax_VariableDeclarationFragment(VariableDeclaration):

    pass
class JavaAbstractSyntax_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, JavaAbstractSyntax_SingleVariableDeclaration343: set["ExtendedModifier"] = None, JavaAbstractSyntax_SingleVariableDeclaration: "Type" = None):
        self.varargs = varargs
        self.JavaAbstractSyntax_SingleVariableDeclaration343 = JavaAbstractSyntax_SingleVariableDeclaration343 if JavaAbstractSyntax_SingleVariableDeclaration343 is not None else set()
        self.JavaAbstractSyntax_SingleVariableDeclaration = JavaAbstractSyntax_SingleVariableDeclaration
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


    @property
    def JavaAbstractSyntax_SingleVariableDeclaration343(self):
        return self.__JavaAbstractSyntax_SingleVariableDeclaration343

    @JavaAbstractSyntax_SingleVariableDeclaration343.setter
    def JavaAbstractSyntax_SingleVariableDeclaration343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_SingleVariableDeclaration__JavaAbstractSyntax_SingleVariableDeclaration343", None)
        self.__JavaAbstractSyntax_SingleVariableDeclaration343 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtendedModifier344"):
                    opp_val = getattr(item, "ExtendedModifier344", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtendedModifier344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtendedModifier344"):
                    opp_val = getattr(item, "ExtendedModifier344", None)
                    
                    setattr(item, "ExtendedModifier344", self)
                    

    @property
    def JavaAbstractSyntax_SingleVariableDeclaration(self):
        return self.__JavaAbstractSyntax_SingleVariableDeclaration

    @JavaAbstractSyntax_SingleVariableDeclaration.setter
    def JavaAbstractSyntax_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_SingleVariableDeclaration__JavaAbstractSyntax_SingleVariableDeclaration", None)
        self.__JavaAbstractSyntax_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type341"):
                opp_val = getattr(old_value, "Type341", None)
                if opp_val == self:
                    setattr(old_value, "Type341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type341"):
                opp_val = getattr(value, "Type341", None)
                setattr(value, "Type341", self)

class CatchClause:

    pass
class Statement:

    pass
class JavaAbstractSyntax_ForStatement(Statement):

    pass
class JavaAbstractSyntax_ExpressionStatement(Statement):

    pass
class JavaAbstractSyntax_DoStatement(Statement):

    pass
class JavaAbstractSyntax_WhileStatement(Statement):

    pass
class JavaAbstractSyntax_TypeDeclarationStatement(Statement):

    pass
class JavaAbstractSyntax_IfStatement(Statement):

    pass
class JavaAbstractSyntax_SuperConstructorInvocation(Statement):

    pass
class JavaAbstractSyntax_ContinueStatement(Statement):

    pass
class JavaAbstractSyntax_ThrowStatement(Statement):

    pass
class JavaAbstractSyntax_SwitchCase(Statement):

    def __init__(self, default: str, JavaAbstractSyntax_SwitchCase: "Expression" = None, Statement317: "JavaAbstractSyntax_WhileStatement" = None, Statement271: "JavaAbstractSyntax_LabeledStatement" = None, Statement: "JavaAbstractSyntax_Block" = None, Statement291: "JavaAbstractSyntax_SwitchStatement" = None, Statement269: "JavaAbstractSyntax_IfStatement" = None, Statement252: "JavaAbstractSyntax_ForStatement" = None, Statement242: "JavaAbstractSyntax_EnhancedForStatement" = None, Statement263: "JavaAbstractSyntax_IfStatement" = None, Statement237: "JavaAbstractSyntax_DoStatement" = None):
        self.default = default
        self.JavaAbstractSyntax_SwitchCase = JavaAbstractSyntax_SwitchCase
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def JavaAbstractSyntax_SwitchCase(self):
        return self.__JavaAbstractSyntax_SwitchCase

    @JavaAbstractSyntax_SwitchCase.setter
    def JavaAbstractSyntax_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_SwitchCase__JavaAbstractSyntax_SwitchCase", None)
        self.__JavaAbstractSyntax_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression286"):
                opp_val = getattr(old_value, "Expression286", None)
                if opp_val == self:
                    setattr(old_value, "Expression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression286"):
                opp_val = getattr(value, "Expression286", None)
                setattr(value, "Expression286", self)

class JavaAbstractSyntax_ReturnStatement(Statement):

    pass
class JavaAbstractSyntax_LabeledStatement(Statement):

    pass
class JavaAbstractSyntax_EmptyStatement(Statement):

    pass
class JavaAbstractSyntax_ConstructorInvocation(Statement):

    pass
class JavaAbstractSyntax_VariableDeclarationStatement(Statement):

    pass
class JavaAbstractSyntax_TryStatement(Statement):

    pass
class JavaAbstractSyntax_Block(Statement):

    pass
class JavaAbstractSyntax_EnhancedForStatement(Statement):

    pass
class JavaAbstractSyntax_SynchronizedStatement(Statement):

    pass
class JavaAbstractSyntax_BreakStatement(Statement):

    pass
class JavaAbstractSyntax_SwitchStatement(Statement):

    pass
class JavaAbstractSyntax_AssertStatement(Statement):

    pass
class TypeParameter:

    pass
class ArrayType:

    pass
class ArrayInitializer:

    pass
class TagElement:

    pass
class EnumConstantDeclaration:

    pass
class VariableDeclarationFragment:

    pass
class AnonymousClassDeclaration:

    pass
class JavaAbstractSyntax_ExtendedModifier(ABC):

    pass
class Type:

    pass
class JavaAbstractSyntax_ParameterizedType(Type):

    pass
class JavaAbstractSyntax_SimpleType(Type):

    pass
class JavaAbstractSyntax_WildcardType(Type):

    def __init__(self, upperBound: str, JavaAbstractSyntax_WildcardType: "Type" = None, Type322: "JavaAbstractSyntax_ArrayType" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type335: "JavaAbstractSyntax_QualifiedType" = None, Type341: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type103: "JavaAbstractSyntax_TypeDeclaration" = None, Type175: "JavaAbstractSyntax_InstanceofExpression" = None, Type220: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type186: "JavaAbstractSyntax_MethodInvocation" = None, Type315: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type135: "JavaAbstractSyntax_CastExpression" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type233: "JavaAbstractSyntax_ConstructorInvocation" = None, Type327: "JavaAbstractSyntax_ParameterizedType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type212: "JavaAbstractSyntax_TypeLiteral" = None, Type208: "JavaAbstractSyntax_SuperMethodInvocation" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type339: "JavaAbstractSyntax_WildcardType" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None):
        self.upperBound = upperBound
        self.JavaAbstractSyntax_WildcardType = JavaAbstractSyntax_WildcardType
        
        pass
    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound


    @property
    def JavaAbstractSyntax_WildcardType(self):
        return self.__JavaAbstractSyntax_WildcardType

    @JavaAbstractSyntax_WildcardType.setter
    def JavaAbstractSyntax_WildcardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_WildcardType__JavaAbstractSyntax_WildcardType", None)
        self.__JavaAbstractSyntax_WildcardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type339"):
                opp_val = getattr(old_value, "Type339", None)
                if opp_val == self:
                    setattr(old_value, "Type339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type339"):
                opp_val = getattr(value, "Type339", None)
                setattr(value, "Type339", self)

class JavaAbstractSyntax_ArrayType(Type):

    def __init__(self, dimensions: str, JavaAbstractSyntax_ArrayType: "Type" = None, JavaAbstractSyntax_ArrayType324: "Type" = None, Type322: "JavaAbstractSyntax_ArrayType" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type335: "JavaAbstractSyntax_QualifiedType" = None, Type341: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type103: "JavaAbstractSyntax_TypeDeclaration" = None, Type175: "JavaAbstractSyntax_InstanceofExpression" = None, Type220: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type186: "JavaAbstractSyntax_MethodInvocation" = None, Type315: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type135: "JavaAbstractSyntax_CastExpression" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type233: "JavaAbstractSyntax_ConstructorInvocation" = None, Type327: "JavaAbstractSyntax_ParameterizedType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type212: "JavaAbstractSyntax_TypeLiteral" = None, Type208: "JavaAbstractSyntax_SuperMethodInvocation" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type339: "JavaAbstractSyntax_WildcardType" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None):
        self.dimensions = dimensions
        self.JavaAbstractSyntax_ArrayType = JavaAbstractSyntax_ArrayType
        self.JavaAbstractSyntax_ArrayType324 = JavaAbstractSyntax_ArrayType324
        
        pass
    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions


    @property
    def JavaAbstractSyntax_ArrayType(self):
        return self.__JavaAbstractSyntax_ArrayType

    @JavaAbstractSyntax_ArrayType.setter
    def JavaAbstractSyntax_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_ArrayType__JavaAbstractSyntax_ArrayType", None)
        self.__JavaAbstractSyntax_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type322"):
                opp_val = getattr(old_value, "Type322", None)
                if opp_val == self:
                    setattr(old_value, "Type322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type322"):
                opp_val = getattr(value, "Type322", None)
                setattr(value, "Type322", self)

    @property
    def JavaAbstractSyntax_ArrayType324(self):
        return self.__JavaAbstractSyntax_ArrayType324

    @JavaAbstractSyntax_ArrayType324.setter
    def JavaAbstractSyntax_ArrayType324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_ArrayType__JavaAbstractSyntax_ArrayType324", None)
        self.__JavaAbstractSyntax_ArrayType324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type325"):
                opp_val = getattr(old_value, "Type325", None)
                if opp_val == self:
                    setattr(old_value, "Type325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type325"):
                opp_val = getattr(value, "Type325", None)
                setattr(value, "Type325", self)

class JavaAbstractSyntax_PrimitiveType(Type):

    def __init__(self, code: str, Type322: "JavaAbstractSyntax_ArrayType" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type335: "JavaAbstractSyntax_QualifiedType" = None, Type341: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type103: "JavaAbstractSyntax_TypeDeclaration" = None, Type175: "JavaAbstractSyntax_InstanceofExpression" = None, Type220: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type186: "JavaAbstractSyntax_MethodInvocation" = None, Type315: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type135: "JavaAbstractSyntax_CastExpression" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type233: "JavaAbstractSyntax_ConstructorInvocation" = None, Type327: "JavaAbstractSyntax_ParameterizedType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type212: "JavaAbstractSyntax_TypeLiteral" = None, Type208: "JavaAbstractSyntax_SuperMethodInvocation" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type339: "JavaAbstractSyntax_WildcardType" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class JavaAbstractSyntax_QualifiedType(Type):

    pass
class Annotation:

    pass
class JavaAbstractSyntax_NormalAnnotation(Annotation):

    pass
class JavaAbstractSyntax_SingleMemberAnnotation(Annotation):

    pass
class JavaAbstractSyntax_MarkerAnnotation(Annotation):

    pass
class Comment:

    pass
class JavaAbstractSyntax_LineComment(Comment):

    pass
class JavaAbstractSyntax_Javadoc(Comment):

    pass
class JavaAbstractSyntax_BlockComment(Comment):

    pass
class SingleVariableDeclaration:

    pass
class MethodRefParameter:

    pass
class Expression:

    pass
class JavaAbstractSyntax_SuperMethodInvocation(Expression):

    pass
class JavaAbstractSyntax_TypeLiteral(Expression):

    pass
class JavaAbstractSyntax_CharacterLiteral(Expression):

    def __init__(self, charValue: str, escapedValue: str, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.charValue = charValue
        self.escapedValue = escapedValue
        
        pass
    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


    @property
    def charValue(self):
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue


class JavaAbstractSyntax_ParenthesizedExpression(Expression):

    pass
class JavaAbstractSyntax_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
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


class JavaAbstractSyntax_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue


class JavaAbstractSyntax_InstanceofExpression(Expression):

    pass
class JavaAbstractSyntax_ArrayAccess(Expression):

    pass
class JavaAbstractSyntax_FieldAccess(Expression):

    pass
class JavaAbstractSyntax_ArrayCreation(Expression):

    pass
class JavaAbstractSyntax_ClassInstanceCreation(Expression):

    pass
class JavaAbstractSyntax_Name(Expression):

    def __init__(self, fullyQualifiedName: str, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.fullyQualifiedName = fullyQualifiedName
        
        pass
    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


class JavaAbstractSyntax_ArrayInitializer(Expression):

    pass
class JavaAbstractSyntax_NumberLiteral(Expression):

    def __init__(self, token: str, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.token = token
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


class JavaAbstractSyntax_SuperFieldAccess(Expression):

    pass
class JavaAbstractSyntax_PrefixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_PrefixExpression: "Expression" = None, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.operator = operator
        self.JavaAbstractSyntax_PrefixExpression = JavaAbstractSyntax_PrefixExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def JavaAbstractSyntax_PrefixExpression(self):
        return self.__JavaAbstractSyntax_PrefixExpression

    @JavaAbstractSyntax_PrefixExpression.setter
    def JavaAbstractSyntax_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_PrefixExpression__JavaAbstractSyntax_PrefixExpression", None)
        self.__JavaAbstractSyntax_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression192"):
                opp_val = getattr(old_value, "Expression192", None)
                if opp_val == self:
                    setattr(old_value, "Expression192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression192"):
                opp_val = getattr(value, "Expression192", None)
                setattr(value, "Expression192", self)

class JavaAbstractSyntax_ThisExpression(Expression):

    pass
class JavaAbstractSyntax_PostfixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_PostfixExpression: "Expression" = None, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.operator = operator
        self.JavaAbstractSyntax_PostfixExpression = JavaAbstractSyntax_PostfixExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def JavaAbstractSyntax_PostfixExpression(self):
        return self.__JavaAbstractSyntax_PostfixExpression

    @JavaAbstractSyntax_PostfixExpression.setter
    def JavaAbstractSyntax_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_PostfixExpression__JavaAbstractSyntax_PostfixExpression", None)
        self.__JavaAbstractSyntax_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression190"):
                opp_val = getattr(old_value, "Expression190", None)
                if opp_val == self:
                    setattr(old_value, "Expression190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression190"):
                opp_val = getattr(value, "Expression190", None)
                setattr(value, "Expression190", self)

class JavaAbstractSyntax_MethodInvocation(Expression):

    pass
class JavaAbstractSyntax_CastExpression(Expression):

    pass
class JavaAbstractSyntax_Assignment(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_Assignment129: "Expression" = None, JavaAbstractSyntax_Assignment: "Expression" = None, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.operator = operator
        self.JavaAbstractSyntax_Assignment129 = JavaAbstractSyntax_Assignment129
        self.JavaAbstractSyntax_Assignment = JavaAbstractSyntax_Assignment
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def JavaAbstractSyntax_Assignment(self):
        return self.__JavaAbstractSyntax_Assignment

    @JavaAbstractSyntax_Assignment.setter
    def JavaAbstractSyntax_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_Assignment__JavaAbstractSyntax_Assignment", None)
        self.__JavaAbstractSyntax_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression127"):
                opp_val = getattr(old_value, "Expression127", None)
                if opp_val == self:
                    setattr(old_value, "Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression127"):
                opp_val = getattr(value, "Expression127", None)
                setattr(value, "Expression127", self)

    @property
    def JavaAbstractSyntax_Assignment129(self):
        return self.__JavaAbstractSyntax_Assignment129

    @JavaAbstractSyntax_Assignment129.setter
    def JavaAbstractSyntax_Assignment129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_Assignment__JavaAbstractSyntax_Assignment129", None)
        self.__JavaAbstractSyntax_Assignment129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression130"):
                opp_val = getattr(old_value, "Expression130", None)
                if opp_val == self:
                    setattr(old_value, "Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression130"):
                opp_val = getattr(value, "Expression130", None)
                setattr(value, "Expression130", self)

class JavaAbstractSyntax_NullLiteral(Expression):

    pass
class JavaAbstractSyntax_InfixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_InfixExpression: set["Expression"] = None, JavaAbstractSyntax_InfixExpression166: "Expression" = None, JavaAbstractSyntax_InfixExpression169: "Expression" = None, Expression125: "JavaAbstractSyntax_ArrayInitializer" = None, Expression199: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression151: "JavaAbstractSyntax_ConditionalExpression" = None, Expression230: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression266: "JavaAbstractSyntax_IfStatement" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression114: "JavaAbstractSyntax_ArrayAccess" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression245: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression222: "JavaAbstractSyntax_AssertStatement" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression190: "JavaAbstractSyntax_PostfixExpression" = None, Expression177: "JavaAbstractSyntax_MethodInvocation" = None, Expression286: "JavaAbstractSyntax_SwitchCase" = None, Expression250: "JavaAbstractSyntax_ExpressionStatement" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression352: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression296: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression164: "JavaAbstractSyntax_InfixExpression" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression276: "JavaAbstractSyntax_ReturnStatement" = None, Expression298: "JavaAbstractSyntax_ThrowStatement" = None, Expression119: "JavaAbstractSyntax_ArrayCreation" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression192: "JavaAbstractSyntax_PrefixExpression" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression278: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression127: "JavaAbstractSyntax_Assignment" = None, Expression132: "JavaAbstractSyntax_CastExpression" = None, Expression240: "JavaAbstractSyntax_DoStatement" = None, Expression255: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression188: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression172: "JavaAbstractSyntax_InstanceofExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression159: "JavaAbstractSyntax_FieldAccess" = None, Expression137: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression288: "JavaAbstractSyntax_SwitchStatement" = None, Expression320: "JavaAbstractSyntax_WhileStatement" = None, Expression143: "JavaAbstractSyntax_ClassInstanceCreation" = None):
        self.operator = operator
        self.JavaAbstractSyntax_InfixExpression = JavaAbstractSyntax_InfixExpression if JavaAbstractSyntax_InfixExpression is not None else set()
        self.JavaAbstractSyntax_InfixExpression166 = JavaAbstractSyntax_InfixExpression166
        self.JavaAbstractSyntax_InfixExpression169 = JavaAbstractSyntax_InfixExpression169
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def JavaAbstractSyntax_InfixExpression166(self):
        return self.__JavaAbstractSyntax_InfixExpression166

    @JavaAbstractSyntax_InfixExpression166.setter
    def JavaAbstractSyntax_InfixExpression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_InfixExpression__JavaAbstractSyntax_InfixExpression166", None)
        self.__JavaAbstractSyntax_InfixExpression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression167"):
                opp_val = getattr(old_value, "Expression167", None)
                if opp_val == self:
                    setattr(old_value, "Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression167"):
                opp_val = getattr(value, "Expression167", None)
                setattr(value, "Expression167", self)

    @property
    def JavaAbstractSyntax_InfixExpression169(self):
        return self.__JavaAbstractSyntax_InfixExpression169

    @JavaAbstractSyntax_InfixExpression169.setter
    def JavaAbstractSyntax_InfixExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_InfixExpression__JavaAbstractSyntax_InfixExpression169", None)
        self.__JavaAbstractSyntax_InfixExpression169 = value
        
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

    @property
    def JavaAbstractSyntax_InfixExpression(self):
        return self.__JavaAbstractSyntax_InfixExpression

    @JavaAbstractSyntax_InfixExpression.setter
    def JavaAbstractSyntax_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_InfixExpression__JavaAbstractSyntax_InfixExpression", None)
        self.__JavaAbstractSyntax_InfixExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression164"):
                    opp_val = getattr(item, "Expression164", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression164"):
                    opp_val = getattr(item, "Expression164", None)
                    
                    setattr(item, "Expression164", self)
                    

class JavaAbstractSyntax_VariableDeclarationExpression(Expression):

    pass
class JavaAbstractSyntax_ConditionalExpression(Expression):

    pass
class SimpleName:

    pass
class Name:

    pass
class JavaAbstractSyntax_QualifiedName(Name):

    pass
class JavaAbstractSyntax_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, Name197: "JavaAbstractSyntax_SuperFieldAccess" = None, Name30: "JavaAbstractSyntax_MethodRef" = None, Name337: "JavaAbstractSyntax_SimpleType" = None, Name43: "JavaAbstractSyntax_PackageDeclaration" = None, Name112: "JavaAbstractSyntax_Annotation" = None, Name210: "JavaAbstractSyntax_ThisExpression" = None, Name: "JavaAbstractSyntax_ImportDeclaration" = None, Name205: "JavaAbstractSyntax_SuperMethodInvocation" = None, Name349: "JavaAbstractSyntax_QualifiedName" = None, Name21: "JavaAbstractSyntax_MemberRef" = None, Name202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Name95: "JavaAbstractSyntax_MethodDeclaration" = None):
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


class AbstractTypeDeclaration:

    pass
class JavaAbstractSyntax_EnumDeclaration(AbstractTypeDeclaration):

    pass
class JavaAbstractSyntax_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, JavaAbstractSyntax_TypeDeclaration: "Type" = None, JavaAbstractSyntax_TypeDeclaration105: set["Type"] = None, JavaAbstractSyntax_TypeDeclaration108: set["TypeParameter"] = None, AbstractTypeDeclaration307: "JavaAbstractSyntax_TypeDeclarationStatement" = None, AbstractTypeDeclaration: "JavaAbstractSyntax_CompilationUnit" = None):
        self.interface = interface
        self.JavaAbstractSyntax_TypeDeclaration = JavaAbstractSyntax_TypeDeclaration
        self.JavaAbstractSyntax_TypeDeclaration105 = JavaAbstractSyntax_TypeDeclaration105 if JavaAbstractSyntax_TypeDeclaration105 is not None else set()
        self.JavaAbstractSyntax_TypeDeclaration108 = JavaAbstractSyntax_TypeDeclaration108 if JavaAbstractSyntax_TypeDeclaration108 is not None else set()
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface


    @property
    def JavaAbstractSyntax_TypeDeclaration105(self):
        return self.__JavaAbstractSyntax_TypeDeclaration105

    @JavaAbstractSyntax_TypeDeclaration105.setter
    def JavaAbstractSyntax_TypeDeclaration105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_TypeDeclaration__JavaAbstractSyntax_TypeDeclaration105", None)
        self.__JavaAbstractSyntax_TypeDeclaration105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type106"):
                    opp_val = getattr(item, "Type106", None)
                    
                    if opp_val == self:
                        setattr(item, "Type106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type106"):
                    opp_val = getattr(item, "Type106", None)
                    
                    setattr(item, "Type106", self)
                    

    @property
    def JavaAbstractSyntax_TypeDeclaration108(self):
        return self.__JavaAbstractSyntax_TypeDeclaration108

    @JavaAbstractSyntax_TypeDeclaration108.setter
    def JavaAbstractSyntax_TypeDeclaration108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_TypeDeclaration__JavaAbstractSyntax_TypeDeclaration108", None)
        self.__JavaAbstractSyntax_TypeDeclaration108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter109"):
                    opp_val = getattr(item, "TypeParameter109", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter109"):
                    opp_val = getattr(item, "TypeParameter109", None)
                    
                    setattr(item, "TypeParameter109", self)
                    

    @property
    def JavaAbstractSyntax_TypeDeclaration(self):
        return self.__JavaAbstractSyntax_TypeDeclaration

    @JavaAbstractSyntax_TypeDeclaration.setter
    def JavaAbstractSyntax_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_TypeDeclaration__JavaAbstractSyntax_TypeDeclaration", None)
        self.__JavaAbstractSyntax_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type103"):
                opp_val = getattr(old_value, "Type103", None)
                if opp_val == self:
                    setattr(old_value, "Type103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type103"):
                opp_val = getattr(value, "Type103", None)
                setattr(value, "Type103", self)

class JavaAbstractSyntax_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class ImportDeclaration:

    pass
class PackageDeclaration:

    pass
class Block:

    pass
class Javadoc:

    pass
class ExtendedModifier:

    pass
class JavaAbstractSyntax_Annotation(ExtendedModifier, Expression):

    pass
class BodyDeclaration:

    pass
class JavaAbstractSyntax_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, JavaAbstractSyntax_AbstractTypeDeclaration59: "SimpleName" = None, JavaAbstractSyntax_AbstractTypeDeclaration: set["BodyDeclaration"] = None, BodyDeclaration: "JavaAbstractSyntax_AnonymousClassDeclaration" = None, BodyDeclaration57: "JavaAbstractSyntax_AbstractTypeDeclaration" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.JavaAbstractSyntax_AbstractTypeDeclaration59 = JavaAbstractSyntax_AbstractTypeDeclaration59
        self.JavaAbstractSyntax_AbstractTypeDeclaration = JavaAbstractSyntax_AbstractTypeDeclaration if JavaAbstractSyntax_AbstractTypeDeclaration is not None else set()
        
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
    def JavaAbstractSyntax_AbstractTypeDeclaration59(self):
        return self.__JavaAbstractSyntax_AbstractTypeDeclaration59

    @JavaAbstractSyntax_AbstractTypeDeclaration59.setter
    def JavaAbstractSyntax_AbstractTypeDeclaration59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_AbstractTypeDeclaration__JavaAbstractSyntax_AbstractTypeDeclaration59", None)
        self.__JavaAbstractSyntax_AbstractTypeDeclaration59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName60"):
                opp_val = getattr(old_value, "SimpleName60", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName60"):
                opp_val = getattr(value, "SimpleName60", None)
                setattr(value, "SimpleName60", self)

    @property
    def JavaAbstractSyntax_AbstractTypeDeclaration(self):
        return self.__JavaAbstractSyntax_AbstractTypeDeclaration

    @JavaAbstractSyntax_AbstractTypeDeclaration.setter
    def JavaAbstractSyntax_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_AbstractTypeDeclaration__JavaAbstractSyntax_AbstractTypeDeclaration", None)
        self.__JavaAbstractSyntax_AbstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BodyDeclaration57"):
                    opp_val = getattr(item, "BodyDeclaration57", None)
                    
                    if opp_val == self:
                        setattr(item, "BodyDeclaration57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BodyDeclaration57"):
                    opp_val = getattr(item, "BodyDeclaration57", None)
                    
                    setattr(item, "BodyDeclaration57", self)
                    

class JavaAbstractSyntax_EnumConstantDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, JavaAbstractSyntax_MethodDeclaration: "Block" = None, JavaAbstractSyntax_MethodDeclaration85: "SimpleName" = None, JavaAbstractSyntax_MethodDeclaration88: "Type" = None, JavaAbstractSyntax_MethodDeclaration91: set["SingleVariableDeclaration"] = None, JavaAbstractSyntax_MethodDeclaration94: set["Name"] = None, JavaAbstractSyntax_MethodDeclaration97: set["TypeParameter"] = None, BodyDeclaration: "JavaAbstractSyntax_AnonymousClassDeclaration" = None, BodyDeclaration57: "JavaAbstractSyntax_AbstractTypeDeclaration" = None):
        self.extraDimensions = extraDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.JavaAbstractSyntax_MethodDeclaration = JavaAbstractSyntax_MethodDeclaration
        self.JavaAbstractSyntax_MethodDeclaration85 = JavaAbstractSyntax_MethodDeclaration85
        self.JavaAbstractSyntax_MethodDeclaration88 = JavaAbstractSyntax_MethodDeclaration88
        self.JavaAbstractSyntax_MethodDeclaration91 = JavaAbstractSyntax_MethodDeclaration91 if JavaAbstractSyntax_MethodDeclaration91 is not None else set()
        self.JavaAbstractSyntax_MethodDeclaration94 = JavaAbstractSyntax_MethodDeclaration94 if JavaAbstractSyntax_MethodDeclaration94 is not None else set()
        self.JavaAbstractSyntax_MethodDeclaration97 = JavaAbstractSyntax_MethodDeclaration97 if JavaAbstractSyntax_MethodDeclaration97 is not None else set()
        
        pass
    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor


    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


    @property
    def JavaAbstractSyntax_MethodDeclaration94(self):
        return self.__JavaAbstractSyntax_MethodDeclaration94

    @JavaAbstractSyntax_MethodDeclaration94.setter
    def JavaAbstractSyntax_MethodDeclaration94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration94", None)
        self.__JavaAbstractSyntax_MethodDeclaration94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Name95"):
                    opp_val = getattr(item, "Name95", None)
                    
                    if opp_val == self:
                        setattr(item, "Name95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Name95"):
                    opp_val = getattr(item, "Name95", None)
                    
                    setattr(item, "Name95", self)
                    

    @property
    def JavaAbstractSyntax_MethodDeclaration85(self):
        return self.__JavaAbstractSyntax_MethodDeclaration85

    @JavaAbstractSyntax_MethodDeclaration85.setter
    def JavaAbstractSyntax_MethodDeclaration85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration85", None)
        self.__JavaAbstractSyntax_MethodDeclaration85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName86"):
                opp_val = getattr(old_value, "SimpleName86", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName86"):
                opp_val = getattr(value, "SimpleName86", None)
                setattr(value, "SimpleName86", self)

    @property
    def JavaAbstractSyntax_MethodDeclaration(self):
        return self.__JavaAbstractSyntax_MethodDeclaration

    @JavaAbstractSyntax_MethodDeclaration.setter
    def JavaAbstractSyntax_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration", None)
        self.__JavaAbstractSyntax_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Block83"):
                opp_val = getattr(old_value, "Block83", None)
                if opp_val == self:
                    setattr(old_value, "Block83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Block83"):
                opp_val = getattr(value, "Block83", None)
                setattr(value, "Block83", self)

    @property
    def JavaAbstractSyntax_MethodDeclaration88(self):
        return self.__JavaAbstractSyntax_MethodDeclaration88

    @JavaAbstractSyntax_MethodDeclaration88.setter
    def JavaAbstractSyntax_MethodDeclaration88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration88", None)
        self.__JavaAbstractSyntax_MethodDeclaration88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type89"):
                opp_val = getattr(old_value, "Type89", None)
                if opp_val == self:
                    setattr(old_value, "Type89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type89"):
                opp_val = getattr(value, "Type89", None)
                setattr(value, "Type89", self)

    @property
    def JavaAbstractSyntax_MethodDeclaration97(self):
        return self.__JavaAbstractSyntax_MethodDeclaration97

    @JavaAbstractSyntax_MethodDeclaration97.setter
    def JavaAbstractSyntax_MethodDeclaration97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration97", None)
        self.__JavaAbstractSyntax_MethodDeclaration97 = value if value is not None else set()
        
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
    def JavaAbstractSyntax_MethodDeclaration91(self):
        return self.__JavaAbstractSyntax_MethodDeclaration91

    @JavaAbstractSyntax_MethodDeclaration91.setter
    def JavaAbstractSyntax_MethodDeclaration91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodDeclaration__JavaAbstractSyntax_MethodDeclaration91", None)
        self.__JavaAbstractSyntax_MethodDeclaration91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableDeclaration92"):
                    opp_val = getattr(item, "SingleVariableDeclaration92", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableDeclaration92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableDeclaration92"):
                    opp_val = getattr(item, "SingleVariableDeclaration92", None)
                    
                    setattr(item, "SingleVariableDeclaration92", self)
                    

class JavaAbstractSyntax_Initializer(BodyDeclaration):

    pass
class JavaAbstractSyntax_FieldDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_ASTNode(ABC):

    pass
class ASTNode:

    pass
class JavaAbstractSyntax_PackageDeclaration(ASTNode):

    pass
class JavaAbstractSyntax_MethodRef(ASTNode):

    pass
class JavaAbstractSyntax_BodyDeclaration(ASTNode):

    pass
class JavaAbstractSyntax_Type(ASTNode):

    pass
class JavaAbstractSyntax_Statement(ASTNode):

    pass
class JavaAbstractSyntax_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, JavaAbstractSyntax_MethodRefParameter: "SimpleName" = None, JavaAbstractSyntax_MethodRefParameter36: "Type" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.varargs = varargs
        self.JavaAbstractSyntax_MethodRefParameter = JavaAbstractSyntax_MethodRefParameter
        self.JavaAbstractSyntax_MethodRefParameter36 = JavaAbstractSyntax_MethodRefParameter36
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


    @property
    def JavaAbstractSyntax_MethodRefParameter36(self):
        return self.__JavaAbstractSyntax_MethodRefParameter36

    @JavaAbstractSyntax_MethodRefParameter36.setter
    def JavaAbstractSyntax_MethodRefParameter36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodRefParameter__JavaAbstractSyntax_MethodRefParameter36", None)
        self.__JavaAbstractSyntax_MethodRefParameter36 = value
        
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

    @property
    def JavaAbstractSyntax_MethodRefParameter(self):
        return self.__JavaAbstractSyntax_MethodRefParameter

    @JavaAbstractSyntax_MethodRefParameter.setter
    def JavaAbstractSyntax_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_MethodRefParameter__JavaAbstractSyntax_MethodRefParameter", None)
        self.__JavaAbstractSyntax_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName34"):
                opp_val = getattr(old_value, "SimpleName34", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName34"):
                opp_val = getattr(value, "SimpleName34", None)
                setattr(value, "SimpleName34", self)

class JavaAbstractSyntax_CompilationUnit(ASTNode):

    pass
class JavaAbstractSyntax_CatchClause(ASTNode):

    pass
class JavaAbstractSyntax_TypeParameter(ASTNode):

    pass
class JavaAbstractSyntax_Modifier(ASTNode, ExtendedModifier):

    def __init__(self, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, abstract: str, final: str, native: str, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None, ExtendedModifier: "JavaAbstractSyntax_BodyDeclaration" = None, ExtendedModifier217: "JavaAbstractSyntax_VariableDeclarationExpression" = None, ExtendedModifier344: "JavaAbstractSyntax_SingleVariableDeclaration" = None, ExtendedModifier312: "JavaAbstractSyntax_VariableDeclarationStatement" = None):
        self.none = none
        self.private = private
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
        
        pass
    @property
    def none(self):
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


    @property
    def strictfp(self):
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp


    @property
    def native(self):
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native


    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized


    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final


    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


class JavaAbstractSyntax_MemberRef(ASTNode):

    pass
class JavaAbstractSyntax_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, JavaAbstractSyntax_ImportDeclaration: "Name" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.onDemand = onDemand
        self.static = static
        self.JavaAbstractSyntax_ImportDeclaration = JavaAbstractSyntax_ImportDeclaration
        
        pass
    @property
    def onDemand(self):
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: str):
        self.__onDemand = onDemand


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def JavaAbstractSyntax_ImportDeclaration(self):
        return self.__JavaAbstractSyntax_ImportDeclaration

    @JavaAbstractSyntax_ImportDeclaration.setter
    def JavaAbstractSyntax_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_ImportDeclaration__JavaAbstractSyntax_ImportDeclaration", None)
        self.__JavaAbstractSyntax_ImportDeclaration = value
        
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

class JavaAbstractSyntax_Comment(ASTNode):

    pass
class JavaAbstractSyntax_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        
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


class JavaAbstractSyntax_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, JavaAbstractSyntax_TagElement: set["ASTNode"] = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.tagName = tagName
        self.nested = nested
        self.JavaAbstractSyntax_TagElement = JavaAbstractSyntax_TagElement if JavaAbstractSyntax_TagElement is not None else set()
        
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
    def JavaAbstractSyntax_TagElement(self):
        return self.__JavaAbstractSyntax_TagElement

    @JavaAbstractSyntax_TagElement.setter
    def JavaAbstractSyntax_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_TagElement__JavaAbstractSyntax_TagElement", None)
        self.__JavaAbstractSyntax_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASTNode45"):
                    opp_val = getattr(item, "ASTNode45", None)
                    
                    if opp_val == self:
                        setattr(item, "ASTNode45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASTNode45"):
                    opp_val = getattr(item, "ASTNode45", None)
                    
                    setattr(item, "ASTNode45", self)
                    

class JavaAbstractSyntax_TextElement(ASTNode):

    def __init__(self, text: str, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class JavaAbstractSyntax_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, JavaAbstractSyntax_VariableDeclaration: "Expression" = None, JavaAbstractSyntax_VariableDeclaration54: "SimpleName" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.extraDimensions = extraDimensions
        self.JavaAbstractSyntax_VariableDeclaration = JavaAbstractSyntax_VariableDeclaration
        self.JavaAbstractSyntax_VariableDeclaration54 = JavaAbstractSyntax_VariableDeclaration54
        
        pass
    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


    @property
    def JavaAbstractSyntax_VariableDeclaration54(self):
        return self.__JavaAbstractSyntax_VariableDeclaration54

    @JavaAbstractSyntax_VariableDeclaration54.setter
    def JavaAbstractSyntax_VariableDeclaration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_VariableDeclaration__JavaAbstractSyntax_VariableDeclaration54", None)
        self.__JavaAbstractSyntax_VariableDeclaration54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName55"):
                opp_val = getattr(old_value, "SimpleName55", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName55"):
                opp_val = getattr(value, "SimpleName55", None)
                setattr(value, "SimpleName55", self)

    @property
    def JavaAbstractSyntax_VariableDeclaration(self):
        return self.__JavaAbstractSyntax_VariableDeclaration

    @JavaAbstractSyntax_VariableDeclaration.setter
    def JavaAbstractSyntax_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_VariableDeclaration__JavaAbstractSyntax_VariableDeclaration", None)
        self.__JavaAbstractSyntax_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression52"):
                opp_val = getattr(old_value, "Expression52", None)
                if opp_val == self:
                    setattr(old_value, "Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression52"):
                opp_val = getattr(value, "Expression52", None)
                setattr(value, "Expression52", self)

class JavaAbstractSyntax_AnonymousClassDeclaration(ASTNode):

    pass
class JavaAbstractSyntax_MemberValuePair(ASTNode):

    pass
class JavaAbstractSyntax_AST:

    pass