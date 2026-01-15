from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
class InfixExpressionKind(Enum):
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    REMAINDER = "REMAINDER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    LEFT_SHIFT = "LEFT_SHIFT"
    RIGHT_SHIFT_SIGNED = "RIGHT_SHIFT_SIGNED"
    RIGHT_SHIFT_UNSIGNED = "RIGHT_SHIFT_UNSIGNED"
    XOR = "XOR"
    AND = "AND"
    OR = "OR"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    CONDITIONAL_OR = "CONDITIONAL_OR"
    LESS = "LESS"
    GREATER = "GREATER"
    LESS_EQUALS = "LESS_EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
class AssignmentKind(Enum):
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    BIT_AND_ASSIGN = "BIT_AND_ASSIGN"
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
    BIT_XOR_ASSIGN = "BIT_XOR_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"
    LEFT_SHIFT_ASSIGN = "LEFT_SHIFT_ASSIGN"
    RIGHT_SHIFT_SIGNED_ASSIGN = "RIGHT_SHIFT_SIGNED_ASSIGN"
    RIGHT_SHIFT_UNSIGNED_ASSIGN = "RIGHT_SHIFT_UNSIGNED_ASSIGN"
    ASSIGN = "ASSIGN"
class PrefixExpressionKind(Enum):
    MINUS = "MINUS"
    COMPLEMENT = "COMPLEMENT"
    NOT = "NOT"
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    PLUS = "PLUS"
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"


############################################
# Definition of Classes
############################################

class java_Model:

    def __init__(self, name: str, java_Model: set["java_CompilationUnit"] = None, java_Model267: set["java_Type"] = None, java_Model270: set["java_Archive"] = None, java_Model272: set["java_Package"] = None):
        self.name = name
        self.java_Model = java_Model if java_Model is not None else set()
        self.java_Model267 = java_Model267 if java_Model267 is not None else set()
        self.java_Model270 = java_Model270 if java_Model270 is not None else set()
        self.java_Model272 = java_Model272 if java_Model272 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Model267(self):
        return self.__java_Model267

    @java_Model267.setter
    def java_Model267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model267", None)
        self.__java_Model267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Type268"):
                    opp_val = getattr(item, "java_Type268", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Type268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Type268"):
                    opp_val = getattr(item, "java_Type268", None)
                    
                    setattr(item, "java_Type268", self)
                    

    @property
    def java_Model(self):
        return self.__java_Model

    @java_Model.setter
    def java_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model", None)
        self.__java_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_CompilationUnit265"):
                    opp_val = getattr(item, "java_CompilationUnit265", None)
                    
                    if opp_val == self:
                        setattr(item, "java_CompilationUnit265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_CompilationUnit265"):
                    opp_val = getattr(item, "java_CompilationUnit265", None)
                    
                    setattr(item, "java_CompilationUnit265", self)
                    

    @property
    def java_Model272(self):
        return self.__java_Model272

    @java_Model272.setter
    def java_Model272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model272", None)
        self.__java_Model272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Package273"):
                    opp_val = getattr(item, "java_Package273", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Package273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Package273"):
                    opp_val = getattr(item, "java_Package273", None)
                    
                    setattr(item, "java_Package273", self)
                    

    @property
    def java_Model270(self):
        return self.__java_Model270

    @java_Model270.setter
    def java_Model270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model270", None)
        self.__java_Model270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Archive"):
                    opp_val = getattr(item, "java_Archive", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Archive", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Archive"):
                    opp_val = getattr(item, "java_Archive", None)
                    
                    setattr(item, "java_Archive", self)
                    

class AbstractMethodDeclaration:

    pass
class java_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class java_MethodDeclaration(AbstractMethodDeclaration):

    pass
class NamespaceAccess:

    pass
class NamedElement:

    pass
class java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, java_Archive: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_Archive = java_Archive
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_Archive(self):
        return self.__java_Archive

    @java_Archive.setter
    def java_Archive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Archive__java_Archive", None)
        self.__java_Archive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model270"):
                opp_val = getattr(old_value, "java_Model270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model270"):
                opp_val = getattr(value, "java_Model270", None)
                if opp_val is None:
                    setattr(value, "java_Model270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Type(NamedElement):

    pass
class java_VariableDeclaration(NamedElement):

    pass
class java_UnresolvedItem(NamedElement):

    pass
class java_Package(NamedElement):

    pass
class java_ClassFile(NamedElement):

    pass
class java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java_CompilationUnit: "java_ASTNode" = None, java_CompilationUnit130: set["java_ImportDeclaration"] = None, java_CompilationUnit133: set["java_AbstractTypeDeclaration"] = None, java_CompilationUnit265: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_CompilationUnit = java_CompilationUnit
        self.java_CompilationUnit130 = java_CompilationUnit130 if java_CompilationUnit130 is not None else set()
        self.java_CompilationUnit133 = java_CompilationUnit133 if java_CompilationUnit133 is not None else set()
        self.java_CompilationUnit265 = java_CompilationUnit265
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_CompilationUnit(self):
        return self.__java_CompilationUnit

    @java_CompilationUnit.setter
    def java_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit", None)
        self.__java_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode78"):
                opp_val = getattr(old_value, "java_ASTNode78", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode78"):
                opp_val = getattr(value, "java_ASTNode78", None)
                setattr(value, "java_ASTNode78", self)

    @property
    def java_CompilationUnit265(self):
        return self.__java_CompilationUnit265

    @java_CompilationUnit265.setter
    def java_CompilationUnit265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit265", None)
        self.__java_CompilationUnit265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model"):
                opp_val = getattr(old_value, "java_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model"):
                opp_val = getattr(value, "java_Model", None)
                if opp_val is None:
                    setattr(value, "java_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_CompilationUnit130(self):
        return self.__java_CompilationUnit130

    @java_CompilationUnit130.setter
    def java_CompilationUnit130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit130", None)
        self.__java_CompilationUnit130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ImportDeclaration131"):
                    opp_val = getattr(item, "java_ImportDeclaration131", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ImportDeclaration131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ImportDeclaration131"):
                    opp_val = getattr(item, "java_ImportDeclaration131", None)
                    
                    setattr(item, "java_ImportDeclaration131", self)
                    

    @property
    def java_CompilationUnit133(self):
        return self.__java_CompilationUnit133

    @java_CompilationUnit133.setter
    def java_CompilationUnit133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit133", None)
        self.__java_CompilationUnit133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AbstractTypeDeclaration134"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration134", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AbstractTypeDeclaration134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AbstractTypeDeclaration134"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration134", None)
                    
                    setattr(item, "java_AbstractTypeDeclaration134", self)
                    

class java_AnnotationMemberValuePair(NamedElement):

    pass
class java_ASTNode(ABC):

    pass
class java_BodyDeclaration(NamedElement):

    pass
class AbstractVariablesContainer:

    pass
class BodyDeclaration:

    pass
class java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class java_AbstractMethodDeclaration(BodyDeclaration):

    pass
class java_Initializer(BodyDeclaration):

    pass
class java_FieldDeclaration(AbstractVariablesContainer, BodyDeclaration):

    pass
class Type:

    pass
class java_PrimitiveType(Type):

    pass
class java_ParameterizedType(Type):

    pass
class java_AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class java_ArrayType(Type):

    def __init__(self, dimensions: int, java_ArrayType: "java_TypeAccess" = None):
        self.dimensions = dimensions
        self.java_ArrayType = java_ArrayType
        
    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions

    @property
    def java_ArrayType(self):
        return self.__java_ArrayType

    @java_ArrayType.setter
    def java_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ArrayType__java_ArrayType", None)
        self.__java_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess159"):
                opp_val = getattr(old_value, "java_TypeAccess159", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess159"):
                opp_val = getattr(value, "java_TypeAccess159", None)
                setattr(value, "java_TypeAccess159", self)

class java_WildCardType(Type):

    pass
class VariableDeclaration:

    pass
class java_EnumConstantDeclaration(BodyDeclaration, VariableDeclaration):

    pass
class java_SingleVariableDeclaration(VariableDeclaration):

    pass
class java_VariableDeclarationFragment(VariableDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class java_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class java_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class AbstractTypeDeclaration:

    pass
class java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class Expression:

    pass
class java_Assignment(Expression):

    def __init__(self, operator: str, java_Assignment: "java_Expression" = None, java_Assignment53: "java_Expression" = None):
        self.operator = operator
        self.java_Assignment = java_Assignment
        self.java_Assignment53 = java_Assignment53
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_Assignment(self):
        return self.__java_Assignment

    @java_Assignment.setter
    def java_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment", None)
        self.__java_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression51"):
                opp_val = getattr(old_value, "java_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression51"):
                opp_val = getattr(value, "java_Expression51", None)
                setattr(value, "java_Expression51", self)

    @property
    def java_Assignment53(self):
        return self.__java_Assignment53

    @java_Assignment53.setter
    def java_Assignment53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment53", None)
        self.__java_Assignment53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression54"):
                opp_val = getattr(old_value, "java_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression54"):
                opp_val = getattr(value, "java_Expression54", None)
                setattr(value, "java_Expression54", self)

class java_UnresolvedItemAccess(Expression, NamespaceAccess):

    pass
class java_SingleVariableAccess(Expression):

    pass
class java_VariableDeclarationExpression(AbstractVariablesContainer, Expression):

    pass
class java_PostfixExpression(Expression):

    def __init__(self, operator: str, java_PostfixExpression: "java_Expression" = None):
        self.operator = operator
        self.java_PostfixExpression = java_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_PostfixExpression(self):
        return self.__java_PostfixExpression

    @java_PostfixExpression.setter
    def java_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_PostfixExpression__java_PostfixExpression", None)
        self.__java_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression56"):
                opp_val = getattr(old_value, "java_Expression56", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression56"):
                opp_val = getattr(value, "java_Expression56", None)
                setattr(value, "java_Expression56", self)

class java_PrefixExpression(Expression):

    def __init__(self, operator: str, java_PrefixExpression: "java_Expression" = None):
        self.operator = operator
        self.java_PrefixExpression = java_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_PrefixExpression(self):
        return self.__java_PrefixExpression

    @java_PrefixExpression.setter
    def java_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_PrefixExpression__java_PrefixExpression", None)
        self.__java_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression182"):
                opp_val = getattr(old_value, "java_Expression182", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression182"):
                opp_val = getattr(value, "java_Expression182", None)
                setattr(value, "java_Expression182", self)

class java_ParenthesizedExpression(Expression):

    pass
class java_Annotation(Expression):

    pass
class java_ArrayCreation(Expression):

    pass
class java_InstanceofExpression(Expression):

    pass
class java_ArrayAccess(Expression):

    pass
class java_ArrayInitializer(Expression):

    pass
class java_AbstractTypeQualifiedExpression(Expression):

    pass
class java_ConditionalExpression(Expression):

    pass
class java_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class java_TypeAccess(Expression, NamespaceAccess):

    pass
class java_ArrayLengthAccess(Expression):

    pass
class java_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class java_FieldAccess(Expression):

    pass
class java_NullLiteral(Expression):

    pass
class java_InfixExpression(Expression):

    def __init__(self, operator: str, java_InfixExpression: "java_Expression" = None, java_InfixExpression121: "java_Expression" = None, java_InfixExpression124: set["java_Expression"] = None):
        self.operator = operator
        self.java_InfixExpression = java_InfixExpression
        self.java_InfixExpression121 = java_InfixExpression121
        self.java_InfixExpression124 = java_InfixExpression124 if java_InfixExpression124 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_InfixExpression124(self):
        return self.__java_InfixExpression124

    @java_InfixExpression124.setter
    def java_InfixExpression124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression124", None)
        self.__java_InfixExpression124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Expression125"):
                    opp_val = getattr(item, "java_Expression125", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Expression125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Expression125"):
                    opp_val = getattr(item, "java_Expression125", None)
                    
                    setattr(item, "java_Expression125", self)
                    

    @property
    def java_InfixExpression121(self):
        return self.__java_InfixExpression121

    @java_InfixExpression121.setter
    def java_InfixExpression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression121", None)
        self.__java_InfixExpression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression122"):
                opp_val = getattr(old_value, "java_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression122"):
                opp_val = getattr(value, "java_Expression122", None)
                setattr(value, "java_Expression122", self)

    @property
    def java_InfixExpression(self):
        return self.__java_InfixExpression

    @java_InfixExpression.setter
    def java_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression", None)
        self.__java_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression119"):
                opp_val = getattr(old_value, "java_Expression119", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression119"):
                opp_val = getattr(value, "java_Expression119", None)
                setattr(value, "java_Expression119", self)

class java_TypeLiteral(Expression):

    pass
class java_CastExpression(Expression):

    pass
class java_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class UnresolvedItem:

    pass
class java_UnresolvedTypeDeclaration(AbstractTypeDeclaration, UnresolvedItem):

    pass
class TypeDeclaration:

    pass
class java_ClassDeclaration(TypeDeclaration):

    pass
class java_InterfaceDeclaration(TypeDeclaration):

    pass
class java_TypeParameter(Type):

    pass
class AbstractMethodInvocation:

    pass
class java_ClassInstanceCreation(Expression, AbstractMethodInvocation):

    pass
class java_SuperMethodInvocation(AbstractTypeQualifiedExpression, AbstractMethodInvocation):

    pass
class java_MethodInvocation(Expression, AbstractMethodInvocation):

    pass
class Statement:

    pass
class java_EnhancedForStatement(Statement):

    pass
class java_CatchClause(Statement):

    pass
class java_ReturnStatement(Statement):

    pass
class java_SynchronizedStatement(Statement):

    pass
class java_VariableDeclarationStatement(AbstractVariablesContainer, Statement):

    pass
class java_ThrowStatement(Statement):

    pass
class java_BreakStatement(Statement):

    pass
class java_TryStatement(Statement):

    pass
class java_ForStatement(Statement):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_Block(Statement):

    pass
class java_ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java_DoStatement(Statement):

    pass
class java_SwitchCase(Statement):

    pass
class java_AssertStatement(Statement):

    pass
class java_TypeDeclarationStatement(Statement):

    pass
class java_LabeledStatement(Statement, NamedElement):

    pass
class java_SwitchStatement(Statement):

    pass
class java_ContinueStatement(Statement):

    pass
class java_EmptyStatement(Statement):

    pass
class java_IfStatement(Statement):

    pass
class java_SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class ASTNode:

    pass
class java_NamespaceAccess(ASTNode):

    pass
class java_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, java_NamedElement: "java_ImportDeclaration" = None):
        self.name = name
        self.proxy = proxy
        self.java_NamedElement = java_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def proxy(self) -> bool:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy

    @property
    def java_NamedElement(self):
        return self.__java_NamedElement

    @java_NamedElement.setter
    def java_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_NamedElement__java_NamedElement", None)
        self.__java_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ImportDeclaration"):
                opp_val = getattr(old_value, "java_ImportDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "java_ImportDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ImportDeclaration"):
                opp_val = getattr(value, "java_ImportDeclaration", None)
                setattr(value, "java_ImportDeclaration", self)

class java_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, java_ImportDeclaration: "java_NamedElement" = None, java_ImportDeclaration131: "java_CompilationUnit" = None):
        self.static = static
        self.java_ImportDeclaration = java_ImportDeclaration
        self.java_ImportDeclaration131 = java_ImportDeclaration131
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def java_ImportDeclaration131(self):
        return self.__java_ImportDeclaration131

    @java_ImportDeclaration131.setter
    def java_ImportDeclaration131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration131", None)
        self.__java_ImportDeclaration131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit130"):
                opp_val = getattr(old_value, "java_CompilationUnit130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit130"):
                opp_val = getattr(value, "java_CompilationUnit130", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ImportDeclaration(self):
        return self.__java_ImportDeclaration

    @java_ImportDeclaration.setter
    def java_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration", None)
        self.__java_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_NamedElement"):
                opp_val = getattr(old_value, "java_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "java_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_NamedElement"):
                opp_val = getattr(value, "java_NamedElement", None)
                setattr(value, "java_NamedElement", self)

class java_Expression(ASTNode):

    pass
class java_MemberRef(ASTNode):

    pass
class java_AbstractMethodInvocation(ASTNode):

    pass
class java_Modifier(ASTNode):

    def __init__(self, static: bool, visibility: str, inheritance: str, java_Modifier: "java_SingleVariableDeclaration" = None, java_Modifier163: "java_BodyDeclaration" = None):
        self.static = static
        self.visibility = visibility
        self.inheritance = inheritance
        self.java_Modifier = java_Modifier
        self.java_Modifier163 = java_Modifier163
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def java_Modifier(self):
        return self.__java_Modifier

    @java_Modifier.setter
    def java_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__java_Modifier", None)
        self.__java_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_SingleVariableDeclaration"):
                opp_val = getattr(old_value, "java_SingleVariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "java_SingleVariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_SingleVariableDeclaration"):
                opp_val = getattr(value, "java_SingleVariableDeclaration", None)
                setattr(value, "java_SingleVariableDeclaration", self)

    @property
    def java_Modifier163(self):
        return self.__java_Modifier163

    @java_Modifier163.setter
    def java_Modifier163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__java_Modifier163", None)
        self.__java_Modifier163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_BodyDeclaration"):
                opp_val = getattr(old_value, "java_BodyDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "java_BodyDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_BodyDeclaration"):
                opp_val = getattr(value, "java_BodyDeclaration", None)
                setattr(value, "java_BodyDeclaration", self)

class java_TagElement(ASTNode):

    pass
class java_AnonymousClassDeclaration(ASTNode):

    pass
class java_Comment(ASTNode):

    def __init__(self, content: str, java_Comment: "java_AbstractTypeDeclaration" = None, java_Comment36: "java_AbstractTypeDeclaration" = None, java_Comment74: "java_ASTNode" = None):
        self.content = content
        self.java_Comment = java_Comment
        self.java_Comment36 = java_Comment36
        self.java_Comment74 = java_Comment74
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def java_Comment74(self):
        return self.__java_Comment74

    @java_Comment74.setter
    def java_Comment74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment74", None)
        self.__java_Comment74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode"):
                opp_val = getattr(old_value, "java_ASTNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode"):
                opp_val = getattr(value, "java_ASTNode", None)
                if opp_val is None:
                    setattr(value, "java_ASTNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment(self):
        return self.__java_Comment

    @java_Comment.setter
    def java_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment", None)
        self.__java_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration", None)
                if opp_val is None:
                    setattr(value, "java_AbstractTypeDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment36(self):
        return self.__java_Comment36

    @java_Comment36.setter
    def java_Comment36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment36", None)
        self.__java_Comment36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration35"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration35"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration35", None)
                if opp_val is None:
                    setattr(value, "java_AbstractTypeDeclaration35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_AbstractVariablesContainer(ASTNode):

    pass
class java_MethodRefParameter(ASTNode):

    pass
class java_Statement(ASTNode):

    pass
class java_WhileStatement(Statement):

    pass
class PrimitiveType:

    pass
class java_PrimitiveTypeFloat(PrimitiveType):

    pass
class java_PrimitiveTypeLong(PrimitiveType):

    pass
class java_PrimitiveTypeBoolean(PrimitiveType):

    pass
class java_PrimitiveTypeShort(PrimitiveType):

    pass
class java_PrimitiveTypeInt(PrimitiveType):

    pass
class java_PrimitiveTypeByte(PrimitiveType):

    pass
class java_PrimitiveTypeChar(PrimitiveType):

    pass
class java_PrimitiveTypeVoid(PrimitiveType):

    pass
class java_PrimitiveTypeDouble(PrimitiveType):

    pass
class java_MethodRef(ASTNode):

    pass