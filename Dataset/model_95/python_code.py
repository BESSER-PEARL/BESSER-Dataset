from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
class PrefixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    COMPLEMENT = "COMPLEMENT"
    NOT = "NOT"
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
class InfixExpressionKind(Enum):
    LESS = "LESS"
    GREATER = "GREATER"
    LESS_EQUALS = "LESS_EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    XOR = "XOR"
    AND = "AND"
    OR = "OR"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    CONDITIONAL_OR = "CONDITIONAL_OR"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    REMAINDER = "REMAINDER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    LEFT_SHIFT = "LEFT_SHIFT"
    RIGHT_SHIFT_SIGNED = "RIGHT_SHIFT_SIGNED"
    RIGHT_SHIFT_UNSIGNED = "RIGHT_SHIFT_UNSIGNED"
class AssignmentKind(Enum):
    ASSIGN = "ASSIGN"
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
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"


############################################
# Definition of Classes
############################################

class java_Model:

    def __init__(self, name: str, java_Model: set["java_CompilationUnit"] = None, java_Model254: set["java_Type"] = None, java_Model257: set["java_Archive"] = None, java_Model259: set["java_Package"] = None):
        self.name = name
        self.java_Model = java_Model if java_Model is not None else set()
        self.java_Model254 = java_Model254 if java_Model254 is not None else set()
        self.java_Model257 = java_Model257 if java_Model257 is not None else set()
        self.java_Model259 = java_Model259 if java_Model259 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                if hasattr(item, "java_CompilationUnit252"):
                    opp_val = getattr(item, "java_CompilationUnit252", None)
                    
                    if opp_val == self:
                        setattr(item, "java_CompilationUnit252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_CompilationUnit252"):
                    opp_val = getattr(item, "java_CompilationUnit252", None)
                    
                    setattr(item, "java_CompilationUnit252", self)
                    

    @property
    def java_Model257(self):
        return self.__java_Model257

    @java_Model257.setter
    def java_Model257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model257", None)
        self.__java_Model257 = value if value is not None else set()
        
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
                    

    @property
    def java_Model254(self):
        return self.__java_Model254

    @java_Model254.setter
    def java_Model254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model254", None)
        self.__java_Model254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Type255"):
                    opp_val = getattr(item, "java_Type255", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Type255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Type255"):
                    opp_val = getattr(item, "java_Type255", None)
                    
                    setattr(item, "java_Type255", self)
                    

    @property
    def java_Model259(self):
        return self.__java_Model259

    @java_Model259.setter
    def java_Model259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model259", None)
        self.__java_Model259 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Package260"):
                    opp_val = getattr(item, "java_Package260", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Package260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Package260"):
                    opp_val = getattr(item, "java_Package260", None)
                    
                    setattr(item, "java_Package260", self)
                    

class AbstractMethodDeclaration:

    pass
class java_MethodDeclaration(AbstractMethodDeclaration):

    pass
class java_ASTNode(ABC):

    pass
class NamespaceAccess:

    pass
class NamedElement:

    pass
class java_BodyDeclaration(NamedElement):

    pass
class java_ClassFile(NamedElement):

    pass
class java_Type(NamedElement):

    pass
class java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java_CompilationUnit: "java_ASTNode" = None, java_CompilationUnit123: set["java_ImportDeclaration"] = None, java_CompilationUnit126: set["java_AbstractTypeDeclaration"] = None, java_CompilationUnit252: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_CompilationUnit = java_CompilationUnit
        self.java_CompilationUnit123 = java_CompilationUnit123 if java_CompilationUnit123 is not None else set()
        self.java_CompilationUnit126 = java_CompilationUnit126 if java_CompilationUnit126 is not None else set()
        self.java_CompilationUnit252 = java_CompilationUnit252
        
        pass
    @property
    def originalFilePath(self):
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath


    @property
    def java_CompilationUnit252(self):
        return self.__java_CompilationUnit252

    @java_CompilationUnit252.setter
    def java_CompilationUnit252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit252", None)
        self.__java_CompilationUnit252 = value
        
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
    def java_CompilationUnit(self):
        return self.__java_CompilationUnit

    @java_CompilationUnit.setter
    def java_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit", None)
        self.__java_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode71"):
                opp_val = getattr(old_value, "java_ASTNode71", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode71"):
                opp_val = getattr(value, "java_ASTNode71", None)
                setattr(value, "java_ASTNode71", self)

    @property
    def java_CompilationUnit126(self):
        return self.__java_CompilationUnit126

    @java_CompilationUnit126.setter
    def java_CompilationUnit126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit126", None)
        self.__java_CompilationUnit126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AbstractTypeDeclaration127"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration127", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AbstractTypeDeclaration127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AbstractTypeDeclaration127"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration127", None)
                    
                    setattr(item, "java_AbstractTypeDeclaration127", self)
                    

    @property
    def java_CompilationUnit123(self):
        return self.__java_CompilationUnit123

    @java_CompilationUnit123.setter
    def java_CompilationUnit123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit123", None)
        self.__java_CompilationUnit123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ImportDeclaration124"):
                    opp_val = getattr(item, "java_ImportDeclaration124", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ImportDeclaration124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ImportDeclaration124"):
                    opp_val = getattr(item, "java_ImportDeclaration124", None)
                    
                    setattr(item, "java_ImportDeclaration124", self)
                    

class java_AnnotationMemberValuePair(NamedElement):

    pass
class BodyDeclaration:

    pass
class java_Initializer(BodyDeclaration):

    pass
class java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class Type:

    pass
class java_PrimitiveType(Type):

    pass
class java_AbstractTypeDeclaration(Type, BodyDeclaration):

    pass
class java_WildCardType(Type):

    pass
class VariableDeclaration:

    pass
class java_EnumConstantDeclaration(VariableDeclaration, BodyDeclaration):

    pass
class java_VariableDeclarationFragment(VariableDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class java_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class AbstractVariablesContainer:

    pass
class java_FieldDeclaration(AbstractVariablesContainer, BodyDeclaration):

    pass
class UnresolvedItem:

    pass
class TypeDeclaration:

    pass
class java_ClassDeclaration(TypeDeclaration):

    pass
class java_InterfaceDeclaration(TypeDeclaration):

    pass
class java_TypeParameter(Type):

    pass
class java_SingleVariableDeclaration(VariableDeclaration):

    pass
class java_AbstractMethodDeclaration(BodyDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class Statement:

    pass
class java_TypeDeclarationStatement(Statement):

    pass
class java_AssertStatement(Statement):

    pass
class java_ReturnStatement(Statement):

    pass
class java_ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java_ThrowStatement(Statement):

    pass
class java_EnhancedForStatement(Statement):

    pass
class java_VariableDeclarationStatement(Statement, AbstractVariablesContainer):

    pass
class java_SwitchCase(Statement):

    pass
class java_DoStatement(Statement):

    pass
class java_EmptyStatement(Statement):

    pass
class java_ContinueStatement(Statement):

    pass
class java_SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class ASTNode:

    pass
class java_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, java_NamedElement: "java_ImportDeclaration" = None):
        self.name = name
        self.proxy = proxy
        self.java_NamedElement = java_NamedElement
        
        pass
    @property
    def proxy(self):
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

    def __init__(self, static: bool, java_ImportDeclaration: "java_NamedElement" = None, java_ImportDeclaration124: "java_CompilationUnit" = None):
        self.static = static
        self.java_ImportDeclaration = java_ImportDeclaration
        self.java_ImportDeclaration124 = java_ImportDeclaration124
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


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

    @property
    def java_ImportDeclaration124(self):
        return self.__java_ImportDeclaration124

    @java_ImportDeclaration124.setter
    def java_ImportDeclaration124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration124", None)
        self.__java_ImportDeclaration124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit123"):
                opp_val = getattr(old_value, "java_CompilationUnit123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit123"):
                opp_val = getattr(value, "java_CompilationUnit123", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_AbstractVariablesContainer(ASTNode):

    pass
class java_Modifier(ASTNode):

    def __init__(self, static: bool, visibility: str, inheritance: str, java_Modifier: "java_SingleVariableDeclaration" = None, java_Modifier156: "java_BodyDeclaration" = None):
        self.static = static
        self.visibility = visibility
        self.inheritance = inheritance
        self.java_Modifier = java_Modifier
        self.java_Modifier156 = java_Modifier156
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def inheritance(self):
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance


    @property
    def java_Modifier156(self):
        return self.__java_Modifier156

    @java_Modifier156.setter
    def java_Modifier156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__java_Modifier156", None)
        self.__java_Modifier156 = value
        
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

class java_MemberRef(ASTNode):

    pass
class java_NamespaceAccess(ASTNode):

    pass
class java_Comment(ASTNode):

    def __init__(self, content: str, java_Comment: "java_AbstractTypeDeclaration" = None, java_Comment31: "java_AbstractTypeDeclaration" = None, java_Comment67: "java_ASTNode" = None):
        self.content = content
        self.java_Comment = java_Comment
        self.java_Comment31 = java_Comment31
        self.java_Comment67 = java_Comment67
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def java_Comment31(self):
        return self.__java_Comment31

    @java_Comment31.setter
    def java_Comment31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment31", None)
        self.__java_Comment31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration30"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration30"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration30", None)
                if opp_val is None:
                    setattr(value, "java_AbstractTypeDeclaration30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment67(self):
        return self.__java_Comment67

    @java_Comment67.setter
    def java_Comment67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment67", None)
        self.__java_Comment67 = value
        
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

class java_AbstractMethodInvocation(ASTNode):

    pass
class java_MethodRefParameter(ASTNode):

    pass
class java_Block(Statement):

    pass
class java_SynchronizedStatement(Statement):

    pass
class AbstractTypeDeclaration:

    pass
class java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class java_UnresolvedTypeDeclaration(UnresolvedItem, AbstractTypeDeclaration):

    pass
class java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class Expression:

    pass
class java_UnresolvedItemAccess(NamespaceAccess, Expression):

    pass
class java_ParenthesizedExpression(Expression):

    pass
class java_ClassInstanceCreation(Expression, AbstractMethodInvocation):

    pass
class java_TypeLiteral(Expression):

    pass
class java_MethodInvocation(Expression, AbstractMethodInvocation):

    pass
class java_Assignment(Expression):

    def __init__(self, operator: str, java_Assignment: "java_Expression" = None, java_Assignment46: "java_Expression" = None):
        self.operator = operator
        self.java_Assignment = java_Assignment
        self.java_Assignment46 = java_Assignment46
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "java_Expression44"):
                opp_val = getattr(old_value, "java_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression44"):
                opp_val = getattr(value, "java_Expression44", None)
                setattr(value, "java_Expression44", self)

    @property
    def java_Assignment46(self):
        return self.__java_Assignment46

    @java_Assignment46.setter
    def java_Assignment46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment46", None)
        self.__java_Assignment46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression47"):
                opp_val = getattr(old_value, "java_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression47"):
                opp_val = getattr(value, "java_Expression47", None)
                setattr(value, "java_Expression47", self)

class java_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
        pass
    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


class java_InstanceofExpression(Expression):

    pass
class java_CastExpression(Expression):

    pass
class java_AbstractTypeQualifiedExpression(Expression):

    pass
class java_VariableDeclarationExpression(AbstractVariablesContainer, Expression):

    pass
class java_FieldAccess(Expression):

    pass
class java_ArrayInitializer(Expression):

    pass
class java_PostfixExpression(Expression):

    def __init__(self, operator: str, java_PostfixExpression: "java_Expression" = None):
        self.operator = operator
        self.java_PostfixExpression = java_PostfixExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "java_Expression49"):
                opp_val = getattr(old_value, "java_Expression49", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression49"):
                opp_val = getattr(value, "java_Expression49", None)
                setattr(value, "java_Expression49", self)

class java_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
        pass
    @property
    def tokenValue(self):
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue


class java_TypeAccess(NamespaceAccess, Expression):

    pass
class java_PrefixExpression(Expression):

    def __init__(self, operator: str, java_PrefixExpression: "java_Expression" = None):
        self.operator = operator
        self.java_PrefixExpression = java_PrefixExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "java_Expression172"):
                opp_val = getattr(old_value, "java_Expression172", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression172"):
                opp_val = getattr(value, "java_Expression172", None)
                setattr(value, "java_Expression172", self)

class java_ArrayLengthAccess(Expression):

    pass
class java_ConditionalExpression(Expression):

    pass
class java_Annotation(Expression):

    pass
class java_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
        pass
    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


class java_Statement(ASTNode):

    pass
class java_WhileStatement(Statement):

    pass
class PrimitiveType:

    pass
class java_PrimitiveTypeByte(PrimitiveType):

    pass
class java_PrimitiveTypeVoid(PrimitiveType):

    pass
class java_PrimitiveTypeLong(PrimitiveType):

    pass
class java_PrimitiveTypeChar(PrimitiveType):

    pass
class java_PrimitiveTypeShort(PrimitiveType):

    pass
class java_PrimitiveTypeBoolean(PrimitiveType):

    pass
class java_PrimitiveTypeFloat(PrimitiveType):

    pass
class java_PrimitiveTypeDouble(PrimitiveType):

    pass
class java_MethodRef(ASTNode):

    pass
class java_Expression(ASTNode):

    pass
class java_PrimitiveTypeInt(PrimitiveType):

    pass
class java_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class java_ArrayAccess(Expression):

    pass
class java_ForStatement(Statement):

    pass
class java_NullLiteral(Expression):

    pass
class java_BreakStatement(Statement):

    pass
class java_Package(NamedElement):

    pass
class java_ParameterizedType(Type):

    pass
class java_SuperMethodInvocation(AbstractTypeQualifiedExpression, AbstractMethodInvocation):

    pass
class java_AnonymousClassDeclaration(ASTNode):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_ArrayType(Type):

    def __init__(self, dimensions: int, java_ArrayType: "java_TypeAccess" = None):
        self.dimensions = dimensions
        self.java_ArrayType = java_ArrayType
        
        pass
    @property
    def dimensions(self):
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
            if hasattr(old_value, "java_TypeAccess152"):
                opp_val = getattr(old_value, "java_TypeAccess152", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess152"):
                opp_val = getattr(value, "java_TypeAccess152", None)
                setattr(value, "java_TypeAccess152", self)

class java_TagElement(ASTNode):

    pass
class java_LabeledStatement(Statement, NamedElement):

    pass
class java_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, java_Archive: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_Archive = java_Archive
        
        pass
    @property
    def originalFilePath(self):
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
            if hasattr(old_value, "java_Model257"):
                opp_val = getattr(old_value, "java_Model257", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model257"):
                opp_val = getattr(value, "java_Model257", None)
                if opp_val is None:
                    setattr(value, "java_Model257", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_InfixExpression(Expression):

    def __init__(self, operator: str, java_InfixExpression: "java_Expression" = None, java_InfixExpression114: "java_Expression" = None, java_InfixExpression117: set["java_Expression"] = None):
        self.operator = operator
        self.java_InfixExpression = java_InfixExpression
        self.java_InfixExpression114 = java_InfixExpression114
        self.java_InfixExpression117 = java_InfixExpression117 if java_InfixExpression117 is not None else set()
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def java_InfixExpression114(self):
        return self.__java_InfixExpression114

    @java_InfixExpression114.setter
    def java_InfixExpression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression114", None)
        self.__java_InfixExpression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression115"):
                opp_val = getattr(old_value, "java_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression115"):
                opp_val = getattr(value, "java_Expression115", None)
                setattr(value, "java_Expression115", self)

    @property
    def java_InfixExpression117(self):
        return self.__java_InfixExpression117

    @java_InfixExpression117.setter
    def java_InfixExpression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression117", None)
        self.__java_InfixExpression117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Expression118"):
                    opp_val = getattr(item, "java_Expression118", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Expression118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Expression118"):
                    opp_val = getattr(item, "java_Expression118", None)
                    
                    setattr(item, "java_Expression118", self)
                    

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
            if hasattr(old_value, "java_Expression112"):
                opp_val = getattr(old_value, "java_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression112"):
                opp_val = getattr(value, "java_Expression112", None)
                setattr(value, "java_Expression112", self)

class java_CatchClause(Statement):

    pass
class java_TryStatement(Statement):

    pass
class java_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class java_VariableDeclaration(NamedElement):

    pass
class java_SingleVariableAccess(Expression):

    pass
class java_UnresolvedItem(NamedElement):

    pass
class java_ArrayCreation(Expression):

    pass
class java_SwitchStatement(Statement):

    pass
class java_IfStatement(Statement):

    pass