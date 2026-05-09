from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrefixExpresssionOperatorKind(Enum):
    MINUS = "MINUS"
    NOT = "NOT"
    DECREMENT = "DECREMENT"
    COMPLEMENT = "COMPLEMENT"
    INCREMENT = "INCREMENT"
    PLUS = "PLUS"
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


############################################
# Definition of Classes
############################################

class CompilationUnit:

    pass
class StructuralPackage:

    pass
class JavaAbstractSyntax_StructuralPackage:

    def __init__(self, name: str, JavaAbstractSyntax_StructuralPackage: set["StructuralPackage"] = None, JavaAbstractSyntax_StructuralPackage358: set["CompilationUnit"] = None):
        self.name = name
        self.JavaAbstractSyntax_StructuralPackage = JavaAbstractSyntax_StructuralPackage if JavaAbstractSyntax_StructuralPackage is not None else set()
        self.JavaAbstractSyntax_StructuralPackage358 = JavaAbstractSyntax_StructuralPackage358 if JavaAbstractSyntax_StructuralPackage358 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def JavaAbstractSyntax_StructuralPackage358(self):
        return self.__JavaAbstractSyntax_StructuralPackage358

    @JavaAbstractSyntax_StructuralPackage358.setter
    def JavaAbstractSyntax_StructuralPackage358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_StructuralPackage__JavaAbstractSyntax_StructuralPackage358", None)
        self.__JavaAbstractSyntax_StructuralPackage358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompilationUnit"):
                    opp_val = getattr(item, "CompilationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "CompilationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompilationUnit"):
                    opp_val = getattr(item, "CompilationUnit", None)
                    
                    setattr(item, "CompilationUnit", self)
                    

    @property
    def JavaAbstractSyntax_StructuralPackage(self):
        return self.__JavaAbstractSyntax_StructuralPackage

    @JavaAbstractSyntax_StructuralPackage.setter
    def JavaAbstractSyntax_StructuralPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_StructuralPackage__JavaAbstractSyntax_StructuralPackage", None)
        self.__JavaAbstractSyntax_StructuralPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralPackage"):
                    opp_val = getattr(item, "StructuralPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralPackage"):
                    opp_val = getattr(item, "StructuralPackage", None)
                    
                    setattr(item, "StructuralPackage", self)
                    

class MemberValuePair:

    pass
class VariableDeclaration:

    pass
class JavaAbstractSyntax_VariableDeclarationFragment(VariableDeclaration):

    pass
class JavaAbstractSyntax_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, JavaAbstractSyntax_SingleVariableDeclaration: "Type" = None, JavaAbstractSyntax_SingleVariableDeclaration346: set["ExtendedModifier"] = None):
        self.varargs = varargs
        self.JavaAbstractSyntax_SingleVariableDeclaration = JavaAbstractSyntax_SingleVariableDeclaration
        self.JavaAbstractSyntax_SingleVariableDeclaration346 = JavaAbstractSyntax_SingleVariableDeclaration346 if JavaAbstractSyntax_SingleVariableDeclaration346 is not None else set()
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


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
            if hasattr(old_value, "Type344"):
                opp_val = getattr(old_value, "Type344", None)
                if opp_val == self:
                    setattr(old_value, "Type344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type344"):
                opp_val = getattr(value, "Type344", None)
                setattr(value, "Type344", self)

    @property
    def JavaAbstractSyntax_SingleVariableDeclaration346(self):
        return self.__JavaAbstractSyntax_SingleVariableDeclaration346

    @JavaAbstractSyntax_SingleVariableDeclaration346.setter
    def JavaAbstractSyntax_SingleVariableDeclaration346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_SingleVariableDeclaration__JavaAbstractSyntax_SingleVariableDeclaration346", None)
        self.__JavaAbstractSyntax_SingleVariableDeclaration346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtendedModifier347"):
                    opp_val = getattr(item, "ExtendedModifier347", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtendedModifier347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtendedModifier347"):
                    opp_val = getattr(item, "ExtendedModifier347", None)
                    
                    setattr(item, "ExtendedModifier347", self)
                    

class CatchClause:

    pass
class Statement:

    pass
class JavaAbstractSyntax_ExpressionStatement(Statement):

    pass
class JavaAbstractSyntax_ThrowStatement(Statement):

    pass
class JavaAbstractSyntax_IfStatement(Statement):

    pass
class JavaAbstractSyntax_SynchronizedStatement(Statement):

    pass
class JavaAbstractSyntax_EnhancedForStatement(Statement):

    pass
class JavaAbstractSyntax_ReturnStatement(Statement):

    pass
class JavaAbstractSyntax_WhileStatement(Statement):

    pass
class JavaAbstractSyntax_EmptyStatement(Statement):

    pass
class JavaAbstractSyntax_VariableDeclarationStatement(Statement):

    pass
class JavaAbstractSyntax_SwitchCase(Statement):

    def __init__(self, default: str, JavaAbstractSyntax_SwitchCase: "Expression" = None, Statement245: "JavaAbstractSyntax_EnhancedForStatement" = None, Statement272: "JavaAbstractSyntax_IfStatement" = None, Statement320: "JavaAbstractSyntax_WhileStatement" = None, Statement274: "JavaAbstractSyntax_LabeledStatement" = None, Statement294: "JavaAbstractSyntax_SwitchStatement" = None, Statement240: "JavaAbstractSyntax_DoStatement" = None, Statement: "JavaAbstractSyntax_Block" = None, Statement266: "JavaAbstractSyntax_IfStatement" = None, Statement255: "JavaAbstractSyntax_ForStatement" = None):
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
            if hasattr(old_value, "Expression289"):
                opp_val = getattr(old_value, "Expression289", None)
                if opp_val == self:
                    setattr(old_value, "Expression289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression289"):
                opp_val = getattr(value, "Expression289", None)
                setattr(value, "Expression289", self)

class JavaAbstractSyntax_DoStatement(Statement):

    pass
class JavaAbstractSyntax_TypeDeclarationStatement(Statement):

    pass
class JavaAbstractSyntax_ForStatement(Statement):

    pass
class JavaAbstractSyntax_SuperConstructorInvocation(Statement):

    pass
class JavaAbstractSyntax_LabeledStatement(Statement):

    pass
class JavaAbstractSyntax_TryStatement(Statement):

    pass
class JavaAbstractSyntax_SwitchStatement(Statement):

    pass
class JavaAbstractSyntax_AssertStatement(Statement):

    pass
class JavaAbstractSyntax_ContinueStatement(Statement):

    pass
class JavaAbstractSyntax_ConstructorInvocation(Statement):

    pass
class JavaAbstractSyntax_BreakStatement(Statement):

    pass
class JavaAbstractSyntax_Block(Statement):

    pass
class TagElement:

    pass
class EnumConstantDeclaration:

    pass
class ArrayType:

    pass
class ArrayInitializer:

    pass
class VariableDeclarationFragment:

    pass
class AnonymousClassDeclaration:

    pass
class TypeParameter:

    pass
class Annotation:

    pass
class JavaAbstractSyntax_NormalAnnotation(Annotation):

    pass
class JavaAbstractSyntax_MarkerAnnotation(Annotation):

    pass
class JavaAbstractSyntax_SingleMemberAnnotation(Annotation):

    pass
class SimpleName:

    pass
class Name:

    pass
class JavaAbstractSyntax_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, Name21: "JavaAbstractSyntax_MemberRef" = None, Name: "JavaAbstractSyntax_ImportDeclaration" = None, Name30: "JavaAbstractSyntax_MethodRef" = None, Name208: "JavaAbstractSyntax_SuperMethodInvocation" = None, Name43: "JavaAbstractSyntax_PackageDeclaration" = None, Name352: "JavaAbstractSyntax_QualifiedName" = None, Name205: "JavaAbstractSyntax_SuperMethodInvocation" = None, Name200: "JavaAbstractSyntax_SuperFieldAccess" = None, Name213: "JavaAbstractSyntax_ThisExpression" = None, Name340: "JavaAbstractSyntax_SimpleType" = None, Name115: "JavaAbstractSyntax_Annotation" = None, Name95: "JavaAbstractSyntax_MethodDeclaration" = None):
        self.identifier = identifier
        self.declaration = declaration
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration


class JavaAbstractSyntax_QualifiedName(Name):

    pass
class AbstractTypeDeclaration:

    pass
class JavaAbstractSyntax_EnumDeclaration(AbstractTypeDeclaration):

    pass
class JavaAbstractSyntax_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, JavaAbstractSyntax_TypeDeclaration: "Type" = None, JavaAbstractSyntax_TypeDeclaration108: set["Type"] = None, JavaAbstractSyntax_TypeDeclaration111: set["TypeParameter"] = None, AbstractTypeDeclaration310: "JavaAbstractSyntax_TypeDeclarationStatement" = None, AbstractTypeDeclaration: "JavaAbstractSyntax_CompilationUnit" = None):
        self.interface = interface
        self.JavaAbstractSyntax_TypeDeclaration = JavaAbstractSyntax_TypeDeclaration
        self.JavaAbstractSyntax_TypeDeclaration108 = JavaAbstractSyntax_TypeDeclaration108 if JavaAbstractSyntax_TypeDeclaration108 is not None else set()
        self.JavaAbstractSyntax_TypeDeclaration111 = JavaAbstractSyntax_TypeDeclaration111 if JavaAbstractSyntax_TypeDeclaration111 is not None else set()
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface


    @property
    def JavaAbstractSyntax_TypeDeclaration111(self):
        return self.__JavaAbstractSyntax_TypeDeclaration111

    @JavaAbstractSyntax_TypeDeclaration111.setter
    def JavaAbstractSyntax_TypeDeclaration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_TypeDeclaration__JavaAbstractSyntax_TypeDeclaration111", None)
        self.__JavaAbstractSyntax_TypeDeclaration111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter112"):
                    opp_val = getattr(item, "TypeParameter112", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter112"):
                    opp_val = getattr(item, "TypeParameter112", None)
                    
                    setattr(item, "TypeParameter112", self)
                    

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
            if hasattr(old_value, "Type106"):
                opp_val = getattr(old_value, "Type106", None)
                if opp_val == self:
                    setattr(old_value, "Type106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type106"):
                opp_val = getattr(value, "Type106", None)
                setattr(value, "Type106", self)

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
                if hasattr(item, "Type109"):
                    opp_val = getattr(item, "Type109", None)
                    
                    if opp_val == self:
                        setattr(item, "Type109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type109"):
                    opp_val = getattr(item, "Type109", None)
                    
                    setattr(item, "Type109", self)
                    

class JavaAbstractSyntax_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class JavaAbstractSyntax_ExtendedModifier(ABC):

    pass
class Type:

    pass
class JavaAbstractSyntax_ParameterizedType(Type):

    pass
class JavaAbstractSyntax_ArrayType(Type):

    def __init__(self, dimensions: str, JavaAbstractSyntax_ArrayType: "Type" = None, JavaAbstractSyntax_ArrayType327: "Type" = None, Type189: "JavaAbstractSyntax_MethodInvocation" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type223: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type178: "JavaAbstractSyntax_InstanceofExpression" = None, Type138: "JavaAbstractSyntax_CastExpression" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type328: "JavaAbstractSyntax_ArrayType" = None, Type344: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type109: "JavaAbstractSyntax_TypeDeclaration" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type236: "JavaAbstractSyntax_ConstructorInvocation" = None, Type342: "JavaAbstractSyntax_WildcardType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type338: "JavaAbstractSyntax_QualifiedType" = None, Type287: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type215: "JavaAbstractSyntax_TypeLiteral" = None, Type152: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type333: "JavaAbstractSyntax_ParameterizedType" = None, Type318: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type211: "JavaAbstractSyntax_SuperMethodInvocation" = None):
        self.dimensions = dimensions
        self.JavaAbstractSyntax_ArrayType = JavaAbstractSyntax_ArrayType
        self.JavaAbstractSyntax_ArrayType327 = JavaAbstractSyntax_ArrayType327
        
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
            if hasattr(old_value, "Type325"):
                opp_val = getattr(old_value, "Type325", None)
                if opp_val == self:
                    setattr(old_value, "Type325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type325"):
                opp_val = getattr(value, "Type325", None)
                setattr(value, "Type325", self)

    @property
    def JavaAbstractSyntax_ArrayType327(self):
        return self.__JavaAbstractSyntax_ArrayType327

    @JavaAbstractSyntax_ArrayType327.setter
    def JavaAbstractSyntax_ArrayType327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_ArrayType__JavaAbstractSyntax_ArrayType327", None)
        self.__JavaAbstractSyntax_ArrayType327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type328"):
                opp_val = getattr(old_value, "Type328", None)
                if opp_val == self:
                    setattr(old_value, "Type328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type328"):
                opp_val = getattr(value, "Type328", None)
                setattr(value, "Type328", self)

class JavaAbstractSyntax_SimpleType(Type):

    pass
class JavaAbstractSyntax_QualifiedType(Type):

    pass
class JavaAbstractSyntax_WildcardType(Type):

    def __init__(self, upperBound: str, JavaAbstractSyntax_WildcardType: "Type" = None, Type189: "JavaAbstractSyntax_MethodInvocation" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type223: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type178: "JavaAbstractSyntax_InstanceofExpression" = None, Type138: "JavaAbstractSyntax_CastExpression" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type328: "JavaAbstractSyntax_ArrayType" = None, Type344: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type109: "JavaAbstractSyntax_TypeDeclaration" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type236: "JavaAbstractSyntax_ConstructorInvocation" = None, Type342: "JavaAbstractSyntax_WildcardType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type338: "JavaAbstractSyntax_QualifiedType" = None, Type287: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type215: "JavaAbstractSyntax_TypeLiteral" = None, Type152: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type333: "JavaAbstractSyntax_ParameterizedType" = None, Type318: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type211: "JavaAbstractSyntax_SuperMethodInvocation" = None):
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
            if hasattr(old_value, "Type342"):
                opp_val = getattr(old_value, "Type342", None)
                if opp_val == self:
                    setattr(old_value, "Type342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type342"):
                opp_val = getattr(value, "Type342", None)
                setattr(value, "Type342", self)

class JavaAbstractSyntax_PrimitiveType(Type):

    def __init__(self, code: str, Type189: "JavaAbstractSyntax_MethodInvocation" = None, Type79: "JavaAbstractSyntax_FieldDeclaration" = None, Type223: "JavaAbstractSyntax_VariableDeclarationExpression" = None, Type325: "JavaAbstractSyntax_ArrayType" = None, Type330: "JavaAbstractSyntax_ParameterizedType" = None, Type50: "JavaAbstractSyntax_TypeParameter" = None, Type: "JavaAbstractSyntax_MethodRefParameter" = None, Type178: "JavaAbstractSyntax_InstanceofExpression" = None, Type138: "JavaAbstractSyntax_CastExpression" = None, Type99: "JavaAbstractSyntax_EnumDeclaration" = None, Type328: "JavaAbstractSyntax_ArrayType" = None, Type344: "JavaAbstractSyntax_SingleVariableDeclaration" = None, Type109: "JavaAbstractSyntax_TypeDeclaration" = None, Type149: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type236: "JavaAbstractSyntax_ConstructorInvocation" = None, Type342: "JavaAbstractSyntax_WildcardType" = None, Type106: "JavaAbstractSyntax_TypeDeclaration" = None, Type338: "JavaAbstractSyntax_QualifiedType" = None, Type287: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Type89: "JavaAbstractSyntax_MethodDeclaration" = None, Type215: "JavaAbstractSyntax_TypeLiteral" = None, Type152: "JavaAbstractSyntax_ClassInstanceCreation" = None, Type333: "JavaAbstractSyntax_ParameterizedType" = None, Type318: "JavaAbstractSyntax_VariableDeclarationStatement" = None, Type68: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Type211: "JavaAbstractSyntax_SuperMethodInvocation" = None):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class MethodRefParameter:

    pass
class Expression:

    pass
class JavaAbstractSyntax_PrefixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_PrefixExpression: "Expression" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
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
            if hasattr(old_value, "Expression195"):
                opp_val = getattr(old_value, "Expression195", None)
                if opp_val == self:
                    setattr(old_value, "Expression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression195"):
                opp_val = getattr(value, "Expression195", None)
                setattr(value, "Expression195", self)

class JavaAbstractSyntax_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
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


class JavaAbstractSyntax_ClassInstanceCreation(Expression):

    pass
class JavaAbstractSyntax_ParenthesizedExpression(Expression):

    pass
class JavaAbstractSyntax_ArrayAccess(Expression):

    pass
class JavaAbstractSyntax_Assignment(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_Assignment: "Expression" = None, JavaAbstractSyntax_Assignment132: "Expression" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
        self.operator = operator
        self.JavaAbstractSyntax_Assignment = JavaAbstractSyntax_Assignment
        self.JavaAbstractSyntax_Assignment132 = JavaAbstractSyntax_Assignment132
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def JavaAbstractSyntax_Assignment132(self):
        return self.__JavaAbstractSyntax_Assignment132

    @JavaAbstractSyntax_Assignment132.setter
    def JavaAbstractSyntax_Assignment132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_Assignment__JavaAbstractSyntax_Assignment132", None)
        self.__JavaAbstractSyntax_Assignment132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression133"):
                opp_val = getattr(old_value, "Expression133", None)
                if opp_val == self:
                    setattr(old_value, "Expression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression133"):
                opp_val = getattr(value, "Expression133", None)
                setattr(value, "Expression133", self)

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
            if hasattr(old_value, "Expression130"):
                opp_val = getattr(old_value, "Expression130", None)
                if opp_val == self:
                    setattr(old_value, "Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression130"):
                opp_val = getattr(value, "Expression130", None)
                setattr(value, "Expression130", self)

class JavaAbstractSyntax_ConditionalExpression(Expression):

    pass
class JavaAbstractSyntax_VariableDeclarationExpression(Expression):

    pass
class JavaAbstractSyntax_ThisExpression(Expression):

    pass
class JavaAbstractSyntax_CharacterLiteral(Expression):

    def __init__(self, charValue: str, escapedValue: str, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
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


class JavaAbstractSyntax_ArrayCreation(Expression):

    pass
class JavaAbstractSyntax_Name(Expression):

    def __init__(self, fullyQualifiedName: str, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
        self.fullyQualifiedName = fullyQualifiedName
        
        pass
    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


class JavaAbstractSyntax_InfixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_InfixExpression169: "Expression" = None, JavaAbstractSyntax_InfixExpression172: "Expression" = None, JavaAbstractSyntax_InfixExpression: set["Expression"] = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
        self.operator = operator
        self.JavaAbstractSyntax_InfixExpression169 = JavaAbstractSyntax_InfixExpression169
        self.JavaAbstractSyntax_InfixExpression172 = JavaAbstractSyntax_InfixExpression172
        self.JavaAbstractSyntax_InfixExpression = JavaAbstractSyntax_InfixExpression if JavaAbstractSyntax_InfixExpression is not None else set()
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
                if hasattr(item, "Expression167"):
                    opp_val = getattr(item, "Expression167", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression167"):
                    opp_val = getattr(item, "Expression167", None)
                    
                    setattr(item, "Expression167", self)
                    

    @property
    def JavaAbstractSyntax_InfixExpression172(self):
        return self.__JavaAbstractSyntax_InfixExpression172

    @JavaAbstractSyntax_InfixExpression172.setter
    def JavaAbstractSyntax_InfixExpression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaAbstractSyntax_InfixExpression__JavaAbstractSyntax_InfixExpression172", None)
        self.__JavaAbstractSyntax_InfixExpression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression173"):
                opp_val = getattr(old_value, "Expression173", None)
                if opp_val == self:
                    setattr(old_value, "Expression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression173"):
                opp_val = getattr(value, "Expression173", None)
                setattr(value, "Expression173", self)

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

class JavaAbstractSyntax_SuperMethodInvocation(Expression):

    pass
class JavaAbstractSyntax_SuperFieldAccess(Expression):

    pass
class JavaAbstractSyntax_ArrayInitializer(Expression):

    pass
class JavaAbstractSyntax_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue


class JavaAbstractSyntax_NullLiteral(Expression):

    pass
class JavaAbstractSyntax_CastExpression(Expression):

    pass
class JavaAbstractSyntax_NumberLiteral(Expression):

    def __init__(self, token: str, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
        self.token = token
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


class JavaAbstractSyntax_TypeLiteral(Expression):

    pass
class JavaAbstractSyntax_PostfixExpression(Expression):

    def __init__(self, operator: str, JavaAbstractSyntax_PostfixExpression: "Expression" = None, Expression225: "JavaAbstractSyntax_AssertStatement" = None, Expression157: "JavaAbstractSyntax_ConditionalExpression" = None, Expression180: "JavaAbstractSyntax_MethodInvocation" = None, Expression323: "JavaAbstractSyntax_WhileStatement" = None, Expression173: "JavaAbstractSyntax_InfixExpression" = None, Expression: "JavaAbstractSyntax_MemberValuePair" = None, Expression120: "JavaAbstractSyntax_ArrayAccess" = None, Expression146: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression193: "JavaAbstractSyntax_PostfixExpression" = None, Expression117: "JavaAbstractSyntax_ArrayAccess" = None, Expression160: "JavaAbstractSyntax_ConditionalExpression" = None, Expression233: "JavaAbstractSyntax_ConstructorInvocation" = None, Expression279: "JavaAbstractSyntax_ReturnStatement" = None, Expression52: "JavaAbstractSyntax_VariableDeclaration" = None, Expression162: "JavaAbstractSyntax_FieldAccess" = None, Expression70: "JavaAbstractSyntax_EnumConstantDeclaration" = None, Expression128: "JavaAbstractSyntax_ArrayInitializer" = None, Expression202: "JavaAbstractSyntax_SuperMethodInvocation" = None, Expression284: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression228: "JavaAbstractSyntax_AssertStatement" = None, Expression253: "JavaAbstractSyntax_ExpressionStatement" = None, Expression167: "JavaAbstractSyntax_InfixExpression" = None, Expression355: "JavaAbstractSyntax_SingleMemberAnnotation" = None, Expression261: "JavaAbstractSyntax_ForStatement" = None, Expression130: "JavaAbstractSyntax_Assignment" = None, Expression269: "JavaAbstractSyntax_IfStatement" = None, Expression122: "JavaAbstractSyntax_ArrayCreation" = None, Expression291: "JavaAbstractSyntax_SwitchStatement" = None, Expression191: "JavaAbstractSyntax_ParenthesizedExpression" = None, Expression62: "JavaAbstractSyntax_AnnotationTypeMemberDeclaration" = None, Expression264: "JavaAbstractSyntax_ForStatement" = None, Expression183: "JavaAbstractSyntax_MethodInvocation" = None, Expression301: "JavaAbstractSyntax_ThrowStatement" = None, Expression140: "JavaAbstractSyntax_ClassInstanceCreation" = None, Expression299: "JavaAbstractSyntax_SynchronizedStatement" = None, Expression289: "JavaAbstractSyntax_SwitchCase" = None, Expression258: "JavaAbstractSyntax_ForStatement" = None, Expression154: "JavaAbstractSyntax_ConditionalExpression" = None, Expression170: "JavaAbstractSyntax_InfixExpression" = None, Expression135: "JavaAbstractSyntax_CastExpression" = None, Expression281: "JavaAbstractSyntax_SuperConstructorInvocation" = None, Expression195: "JavaAbstractSyntax_PrefixExpression" = None, Expression133: "JavaAbstractSyntax_Assignment" = None, Expression243: "JavaAbstractSyntax_DoStatement" = None, Expression248: "JavaAbstractSyntax_EnhancedForStatement" = None, Expression175: "JavaAbstractSyntax_InstanceofExpression" = None):
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
            if hasattr(old_value, "Expression193"):
                opp_val = getattr(old_value, "Expression193", None)
                if opp_val == self:
                    setattr(old_value, "Expression193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression193"):
                opp_val = getattr(value, "Expression193", None)
                setattr(value, "Expression193", self)

class JavaAbstractSyntax_MethodInvocation(Expression):

    pass
class JavaAbstractSyntax_FieldAccess(Expression):

    pass
class JavaAbstractSyntax_InstanceofExpression(Expression):

    pass
class BodyDeclaration:

    pass
class JavaAbstractSyntax_EnumConstantDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_Initializer(BodyDeclaration):

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
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


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
                    

class JavaAbstractSyntax_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, JavaAbstractSyntax_AbstractTypeDeclaration: set["BodyDeclaration"] = None, JavaAbstractSyntax_AbstractTypeDeclaration59: "SimpleName" = None, BodyDeclaration: "JavaAbstractSyntax_AnonymousClassDeclaration" = None, BodyDeclaration57: "JavaAbstractSyntax_AbstractTypeDeclaration" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.JavaAbstractSyntax_AbstractTypeDeclaration = JavaAbstractSyntax_AbstractTypeDeclaration if JavaAbstractSyntax_AbstractTypeDeclaration is not None else set()
        self.JavaAbstractSyntax_AbstractTypeDeclaration59 = JavaAbstractSyntax_AbstractTypeDeclaration59
        
        pass
    @property
    def memberTypeDeclaration(self):
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration


    @property
    def localTypeDeclaration(self):
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration


    @property
    def packageMemberTypeDeclaration(self):
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration


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
                    

class JavaAbstractSyntax_FieldDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class JavaAbstractSyntax_ASTNode(ABC):

    pass
class ASTNode:

    pass
class JavaAbstractSyntax_TextElement(ASTNode):

    def __init__(self, text: str, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class JavaAbstractSyntax_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, JavaAbstractSyntax_VariableDeclaration: "Expression" = None, JavaAbstractSyntax_VariableDeclaration54: "SimpleName" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
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

class JavaAbstractSyntax_Type(ASTNode):

    pass
class JavaAbstractSyntax_AnonymousClassDeclaration(ASTNode):

    pass
class JavaAbstractSyntax_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, JavaAbstractSyntax_ImportDeclaration: "Name" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.onDemand = onDemand
        self.static = static
        self.JavaAbstractSyntax_ImportDeclaration = JavaAbstractSyntax_ImportDeclaration
        
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

class JavaAbstractSyntax_PackageDeclaration(ASTNode):

    pass
class JavaAbstractSyntax_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, JavaAbstractSyntax_MethodRefParameter: "SimpleName" = None, JavaAbstractSyntax_MethodRefParameter36: "Type" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
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

class JavaAbstractSyntax_TypeParameter(ASTNode):

    pass
class JavaAbstractSyntax_Statement(ASTNode):

    pass
class JavaAbstractSyntax_MethodRef(ASTNode):

    pass
class JavaAbstractSyntax_MemberRef(ASTNode):

    pass
class JavaAbstractSyntax_MemberValuePair(ASTNode):

    pass
class JavaAbstractSyntax_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, JavaAbstractSyntax_TagElement: set["ASTNode"] = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
        self.tagName = tagName
        self.nested = nested
        self.JavaAbstractSyntax_TagElement = JavaAbstractSyntax_TagElement if JavaAbstractSyntax_TagElement is not None else set()
        
        pass
    @property
    def nested(self):
        return self.__nested

    @nested.setter
    def nested(self, nested: str):
        self.__nested = nested


    @property
    def tagName(self):
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName


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
                    

class JavaAbstractSyntax_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
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


class JavaAbstractSyntax_AST:

    pass
class ImportDeclaration:

    pass
class PackageDeclaration:

    pass
class Comment:

    pass
class JavaAbstractSyntax_Javadoc(Comment):

    pass
class JavaAbstractSyntax_LineComment(Comment):

    pass
class JavaAbstractSyntax_BlockComment(Comment):

    pass
class JavaAbstractSyntax_CompilationUnit(ASTNode):

    pass
class JavaAbstractSyntax_Comment(ASTNode):

    pass
class SingleVariableDeclaration:

    pass
class Block:

    pass
class JavaAbstractSyntax_CatchClause(ASTNode):

    pass
class Javadoc:

    pass
class ExtendedModifier:

    pass
class JavaAbstractSyntax_Annotation(Expression, ExtendedModifier):

    pass
class JavaAbstractSyntax_Modifier(ExtendedModifier, ASTNode):

    def __init__(self, abstract: str, final: str, native: str, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, ExtendedModifier220: "JavaAbstractSyntax_VariableDeclarationExpression" = None, ExtendedModifier315: "JavaAbstractSyntax_VariableDeclarationStatement" = None, ExtendedModifier: "JavaAbstractSyntax_BodyDeclaration" = None, ExtendedModifier347: "JavaAbstractSyntax_SingleVariableDeclaration" = None, ASTNode: "JavaAbstractSyntax_AST" = None, ASTNode9: "JavaAbstractSyntax_Comment" = None, ASTNode45: "JavaAbstractSyntax_TagElement" = None):
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
    def native(self):
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native


    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def none(self):
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none


    @property
    def strictfp(self):
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp


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


    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


class JavaAbstractSyntax_BodyDeclaration(ASTNode):

    pass