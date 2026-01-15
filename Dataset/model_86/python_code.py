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
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class AssignmentKind(Enum):
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"
    LEFT_SHIFT_ASSIGN = "LEFT_SHIFT_ASSIGN"
    RIGHT_SHIFT_SIGNED_ASSIGN = "RIGHT_SHIFT_SIGNED_ASSIGN"
    RIGHT_SHIFT_UNSIGNED_ASSIGN = "RIGHT_SHIFT_UNSIGNED_ASSIGN"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    BIT_AND_ASSIGN = "BIT_AND_ASSIGN"
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
    BIT_XOR_ASSIGN = "BIT_XOR_ASSIGN"
class InfixExpressionKind(Enum):
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    REMAINDER = "REMAINDER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    LEFT_SHIFT = "LEFT_SHIFT"
    RIGHT_SHIFT_SIGNED = "RIGHT_SHIFT_SIGNED"
    RIGHT_SHIFT_UNSIGNED = "RIGHT_SHIFT_UNSIGNED"
    LESS = "LESS"
    AND = "AND"
    OR = "OR"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    CONDITIONAL_OR = "CONDITIONAL_OR"
    GREATER = "GREATER"
    LESS_EQUALS = "LESS_EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    XOR = "XOR"
class PrefixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    COMPLEMENT = "COMPLEMENT"
    NOT = "NOT"


############################################
# Definition of Classes
############################################

class VariableDeclarationFragment:

    pass
class AnnotationTypeMemberDeclaration:

    pass
class SingleVariableDeclaration:

    pass
class MethodDeclaration:

    pass
class LabeledStatement:

    pass
class InterfaceDeclaration:

    pass
class EnumDeclaration:

    pass
class ClassDeclaration:

    pass
class UnresolvedItem:

    pass
class java_UnresolvedEnumDeclaration(EnumDeclaration, UnresolvedItem):

    pass
class java_UnresolvedInterfaceDeclaration(UnresolvedItem, InterfaceDeclaration):

    pass
class java_UnresolvedVariableDeclarationFragment(VariableDeclarationFragment, UnresolvedItem):

    pass
class java_UnresolvedAnnotationTypeMemberDeclaration(AnnotationTypeMemberDeclaration, UnresolvedItem):

    pass
class java_UnresolvedMethodDeclaration(UnresolvedItem, MethodDeclaration):

    pass
class java_UnresolvedLabeledStatement(LabeledStatement, UnresolvedItem):

    pass
class java_UnresolvedClassDeclaration(ClassDeclaration, UnresolvedItem):

    pass
class java_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class AnnotationTypeDeclaration:

    pass
class java_UnresolvedAnnotationDeclaration(AnnotationTypeDeclaration, UnresolvedItem):

    pass
class AbstractTypeQualifiedExpression:

    pass
class java_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class java_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class PrimitiveType:

    pass
class java_PrimitiveTypeByte(PrimitiveType):

    pass
class java_PrimitiveTypeDouble(PrimitiveType):

    pass
class java_PrimitiveTypeChar(PrimitiveType):

    pass
class java_PrimitiveTypeVoid(PrimitiveType):

    pass
class java_PrimitiveTypeLong(PrimitiveType):

    pass
class java_PrimitiveTypeInt(PrimitiveType):

    pass
class java_PrimitiveTypeFloat(PrimitiveType):

    pass
class java_PrimitiveTypeShort(PrimitiveType):

    pass
class java_PrimitiveTypeBoolean(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class java_PackageAccess(NamespaceAccess):

    pass
class java_Model:

    def __init__(self, name: str, java_Model219: set["java_CompilationUnit"] = None, java_Model222: set["java_Archive"] = None, model: set["java_Package"] = None, java_Model: set["java_Type"] = None, java_Model217: set["java_UnresolvedItem"] = None, Model: "java_Package" = None):
        self.name = name
        self.java_Model219 = java_Model219 if java_Model219 is not None else set()
        self.java_Model222 = java_Model222 if java_Model222 is not None else set()
        self.model = model if model is not None else set()
        self.java_Model = java_Model if java_Model is not None else set()
        self.java_Model217 = java_Model217 if java_Model217 is not None else set()
        self.Model = Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package214"):
                    opp_val = getattr(item, "Package214", None)
                    
                    if opp_val == self:
                        setattr(item, "Package214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package214"):
                    opp_val = getattr(item, "Package214", None)
                    
                    setattr(item, "Package214", self)
                    

    @property
    def java_Model222(self):
        return self.__java_Model222

    @java_Model222.setter
    def java_Model222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model222", None)
        self.__java_Model222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Archive223"):
                    opp_val = getattr(item, "java_Archive223", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Archive223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Archive223"):
                    opp_val = getattr(item, "java_Archive223", None)
                    
                    setattr(item, "java_Archive223", self)
                    

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElements237"):
                opp_val = getattr(old_value, "ownedElements237", None)
                if opp_val == self:
                    setattr(old_value, "ownedElements237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElements237"):
                opp_val = getattr(value, "ownedElements237", None)
                setattr(value, "ownedElements237", self)

    @property
    def java_Model217(self):
        return self.__java_Model217

    @java_Model217.setter
    def java_Model217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model217", None)
        self.__java_Model217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_UnresolvedItem"):
                    opp_val = getattr(item, "java_UnresolvedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "java_UnresolvedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_UnresolvedItem"):
                    opp_val = getattr(item, "java_UnresolvedItem", None)
                    
                    setattr(item, "java_UnresolvedItem", self)
                    

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
                if hasattr(item, "java_Type"):
                    opp_val = getattr(item, "java_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Type"):
                    opp_val = getattr(item, "java_Type", None)
                    
                    setattr(item, "java_Type", self)
                    

    @property
    def java_Model219(self):
        return self.__java_Model219

    @java_Model219.setter
    def java_Model219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model219", None)
        self.__java_Model219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_CompilationUnit220"):
                    opp_val = getattr(item, "java_CompilationUnit220", None)
                    
                    if opp_val == self:
                        setattr(item, "java_CompilationUnit220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_CompilationUnit220"):
                    opp_val = getattr(item, "java_CompilationUnit220", None)
                    
                    setattr(item, "java_CompilationUnit220", self)
                    

class java_ManifestEntry:

    def __init__(self, name: str, java_ManifestEntry: "java_Manifest" = None, java_ManifestEntry189: set["java_ManifestAttribute"] = None):
        self.name = name
        self.java_ManifestEntry = java_ManifestEntry
        self.java_ManifestEntry189 = java_ManifestEntry189 if java_ManifestEntry189 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_ManifestEntry189(self):
        return self.__java_ManifestEntry189

    @java_ManifestEntry189.setter
    def java_ManifestEntry189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestEntry__java_ManifestEntry189", None)
        self.__java_ManifestEntry189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ManifestAttribute190"):
                    opp_val = getattr(item, "java_ManifestAttribute190", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ManifestAttribute190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ManifestAttribute190"):
                    opp_val = getattr(item, "java_ManifestAttribute190", None)
                    
                    setattr(item, "java_ManifestAttribute190", self)
                    

    @property
    def java_ManifestEntry(self):
        return self.__java_ManifestEntry

    @java_ManifestEntry.setter
    def java_ManifestEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestEntry__java_ManifestEntry", None)
        self.__java_ManifestEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Manifest187"):
                opp_val = getattr(old_value, "java_Manifest187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest187"):
                opp_val = getattr(value, "java_Manifest187", None)
                if opp_val is None:
                    setattr(value, "java_Manifest187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_ManifestAttribute:

    def __init__(self, key: str, value: str, java_ManifestAttribute: "java_Manifest" = None, java_ManifestAttribute190: "java_ManifestEntry" = None):
        self.key = key
        self.value = value
        self.java_ManifestAttribute = java_ManifestAttribute
        self.java_ManifestAttribute190 = java_ManifestAttribute190
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def java_ManifestAttribute(self):
        return self.__java_ManifestAttribute

    @java_ManifestAttribute.setter
    def java_ManifestAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestAttribute__java_ManifestAttribute", None)
        self.__java_ManifestAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Manifest185"):
                opp_val = getattr(old_value, "java_Manifest185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest185"):
                opp_val = getattr(value, "java_Manifest185", None)
                if opp_val is None:
                    setattr(value, "java_Manifest185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ManifestAttribute190(self):
        return self.__java_ManifestAttribute190

    @java_ManifestAttribute190.setter
    def java_ManifestAttribute190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestAttribute__java_ManifestAttribute190", None)
        self.__java_ManifestAttribute190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ManifestEntry189"):
                opp_val = getattr(old_value, "java_ManifestEntry189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ManifestEntry189"):
                opp_val = getattr(value, "java_ManifestEntry189", None)
                if opp_val is None:
                    setattr(value, "java_ManifestEntry189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractVariablesContainer:

    pass
class VariableDeclaration:

    pass
class TypeDeclaration:

    pass
class java_InterfaceDeclaration(TypeDeclaration):

    pass
class java_ClassDeclaration(TypeDeclaration):

    pass
class AbstractMethodDeclaration:

    pass
class java_MethodDeclaration(AbstractMethodDeclaration):

    def __init__(self, extraArrayDimensions: int, java_MethodDeclaration: "java_TypeAccess" = None, MethodDeclaration: "java_MethodDeclaration" = None, redefinitions: "java_MethodDeclaration" = None, MethodDeclaration201: "java_MethodDeclaration" = None, redefinedMethodDeclaration: set["java_MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.java_MethodDeclaration = java_MethodDeclaration
        self.MethodDeclaration = MethodDeclaration
        self.redefinitions = redefinitions
        self.MethodDeclaration201 = MethodDeclaration201
        self.redefinedMethodDeclaration = redefinedMethodDeclaration if redefinedMethodDeclaration is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def MethodDeclaration(self):
        return self.__MethodDeclaration

    @MethodDeclaration.setter
    def MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__MethodDeclaration", None)
        self.__MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redefinitions"):
                opp_val = getattr(old_value, "redefinitions", None)
                if opp_val == self:
                    setattr(old_value, "redefinitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redefinitions"):
                opp_val = getattr(value, "redefinitions", None)
                setattr(value, "redefinitions", self)

    @property
    def java_MethodDeclaration(self):
        return self.__java_MethodDeclaration

    @java_MethodDeclaration.setter
    def java_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__java_MethodDeclaration", None)
        self.__java_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess196"):
                opp_val = getattr(old_value, "java_TypeAccess196", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess196"):
                opp_val = getattr(value, "java_TypeAccess196", None)
                setattr(value, "java_TypeAccess196", self)

    @property
    def redefinitions(self):
        return self.__redefinitions

    @redefinitions.setter
    def redefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__redefinitions", None)
        self.__redefinitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodDeclaration"):
                opp_val = getattr(old_value, "MethodDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "MethodDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodDeclaration"):
                opp_val = getattr(value, "MethodDeclaration", None)
                setattr(value, "MethodDeclaration", self)

    @property
    def redefinedMethodDeclaration(self):
        return self.__redefinedMethodDeclaration

    @redefinedMethodDeclaration.setter
    def redefinedMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__redefinedMethodDeclaration", None)
        self.__redefinedMethodDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodDeclaration201"):
                    opp_val = getattr(item, "MethodDeclaration201", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodDeclaration201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodDeclaration201"):
                    opp_val = getattr(item, "MethodDeclaration201", None)
                    
                    setattr(item, "MethodDeclaration201", self)
                    

    @property
    def MethodDeclaration201(self):
        return self.__MethodDeclaration201

    @MethodDeclaration201.setter
    def MethodDeclaration201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__MethodDeclaration201", None)
        self.__MethodDeclaration201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redefinedMethodDeclaration"):
                opp_val = getattr(old_value, "redefinedMethodDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redefinedMethodDeclaration"):
                opp_val = getattr(value, "redefinedMethodDeclaration", None)
                if opp_val is None:
                    setattr(value, "redefinedMethodDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class java_SuperMethodInvocation(AbstractTypeQualifiedExpression, AbstractMethodInvocation):

    pass
class Comment:

    pass
class java_Javadoc(Comment):

    pass
class java_LineComment(Comment):

    pass
class java_BlockComment(Comment):

    pass
class java_ASTNode(ABC):

    pass
class AbstractTypeDeclaration:

    pass
class java_UnresolvedTypeDeclaration(UnresolvedItem, AbstractTypeDeclaration):

    pass
class java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class Expression:

    pass
class java_NullLiteral(Expression):

    pass
class java_TypeLiteral(Expression):

    pass
class java_SingleVariableAccess(Expression):

    pass
class java_UnresolvedItemAccess(Expression, NamespaceAccess):

    pass
class java_ArrayInitializer(Expression):

    pass
class java_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class java_InstanceofExpression(Expression):

    pass
class java_ArrayCreation(Expression):

    pass
class java_MethodInvocation(Expression, AbstractMethodInvocation):

    pass
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
            if hasattr(old_value, "java_Expression261"):
                opp_val = getattr(old_value, "java_Expression261", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression261"):
                opp_val = getattr(value, "java_Expression261", None)
                setattr(value, "java_Expression261", self)

class java_FieldAccess(Expression):

    pass
class java_InfixExpression(Expression):

    def __init__(self, operator: str, java_InfixExpression: "java_Expression" = None, java_InfixExpression166: "java_Expression" = None, java_InfixExpression169: set["java_Expression"] = None):
        self.operator = operator
        self.java_InfixExpression = java_InfixExpression
        self.java_InfixExpression166 = java_InfixExpression166
        self.java_InfixExpression169 = java_InfixExpression169 if java_InfixExpression169 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_InfixExpression169(self):
        return self.__java_InfixExpression169

    @java_InfixExpression169.setter
    def java_InfixExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression169", None)
        self.__java_InfixExpression169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Expression170"):
                    opp_val = getattr(item, "java_Expression170", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Expression170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Expression170"):
                    opp_val = getattr(item, "java_Expression170", None)
                    
                    setattr(item, "java_Expression170", self)
                    

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
            if hasattr(old_value, "java_Expression164"):
                opp_val = getattr(old_value, "java_Expression164", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression164"):
                opp_val = getattr(value, "java_Expression164", None)
                setattr(value, "java_Expression164", self)

    @property
    def java_InfixExpression166(self):
        return self.__java_InfixExpression166

    @java_InfixExpression166.setter
    def java_InfixExpression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression166", None)
        self.__java_InfixExpression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression167"):
                opp_val = getattr(old_value, "java_Expression167", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression167"):
                opp_val = getattr(value, "java_Expression167", None)
                setattr(value, "java_Expression167", self)

class java_ConditionalExpression(Expression):

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

class java_Assignment(Expression):

    def __init__(self, operator: str, java_Assignment: "java_Expression" = None, java_Assignment77: "java_Expression" = None):
        self.operator = operator
        self.java_Assignment = java_Assignment
        self.java_Assignment77 = java_Assignment77
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_Assignment77(self):
        return self.__java_Assignment77

    @java_Assignment77.setter
    def java_Assignment77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment77", None)
        self.__java_Assignment77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression78"):
                opp_val = getattr(old_value, "java_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression78"):
                opp_val = getattr(value, "java_Expression78", None)
                setattr(value, "java_Expression78", self)

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
            if hasattr(old_value, "java_Expression75"):
                opp_val = getattr(old_value, "java_Expression75", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression75"):
                opp_val = getattr(value, "java_Expression75", None)
                setattr(value, "java_Expression75", self)

class java_ArrayAccess(Expression):

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
            if hasattr(old_value, "java_Expression259"):
                opp_val = getattr(old_value, "java_Expression259", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression259"):
                opp_val = getattr(value, "java_Expression259", None)
                setattr(value, "java_Expression259", self)

class java_ParenthesizedExpression(Expression):

    pass
class java_VariableDeclarationExpression(Expression, AbstractVariablesContainer):

    pass
class java_ArrayLengthAccess(Expression):

    pass
class java_CastExpression(Expression):

    pass
class java_AbstractTypeQualifiedExpression(Expression):

    pass
class Statement:

    pass
class java_DoStatement(Statement):

    pass
class java_CatchClause(Statement):

    pass
class java_TryStatement(Statement):

    pass
class java_ReturnStatement(Statement):

    pass
class java_TypeDeclarationStatement(Statement):

    pass
class java_ForStatement(Statement):

    pass
class java_SynchronizedStatement(Statement):

    pass
class java_EmptyStatement(Statement):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_BreakStatement(Statement):

    pass
class java_SwitchStatement(Statement):

    pass
class java_EnhancedForStatement(Statement):

    pass
class java_ContinueStatement(Statement):

    pass
class java_VariableDeclarationStatement(Statement, AbstractVariablesContainer):

    def __init__(self, extraArrayDimensions: int, VariableDeclarationStatement: "java_Modifier" = None, variableDeclarationStatement: "java_Modifier" = None, java_VariableDeclarationStatement: set["java_Annotation"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclarationStatement = VariableDeclarationStatement
        self.variableDeclarationStatement = variableDeclarationStatement
        self.java_VariableDeclarationStatement = java_VariableDeclarationStatement if java_VariableDeclarationStatement is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def variableDeclarationStatement(self):
        return self.__variableDeclarationStatement

    @variableDeclarationStatement.setter
    def variableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclarationStatement__variableDeclarationStatement", None)
        self.__variableDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Modifier335"):
                opp_val = getattr(old_value, "Modifier335", None)
                if opp_val == self:
                    setattr(old_value, "Modifier335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier335"):
                opp_val = getattr(value, "Modifier335", None)
                setattr(value, "Modifier335", self)

    @property
    def VariableDeclarationStatement(self):
        return self.__VariableDeclarationStatement

    @VariableDeclarationStatement.setter
    def VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclarationStatement__VariableDeclarationStatement", None)
        self.__VariableDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifier230"):
                opp_val = getattr(old_value, "modifier230", None)
                if opp_val == self:
                    setattr(old_value, "modifier230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifier230"):
                opp_val = getattr(value, "modifier230", None)
                setattr(value, "modifier230", self)

    @property
    def java_VariableDeclarationStatement(self):
        return self.__java_VariableDeclarationStatement

    @java_VariableDeclarationStatement.setter
    def java_VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclarationStatement__java_VariableDeclarationStatement", None)
        self.__java_VariableDeclarationStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Annotation337"):
                    opp_val = getattr(item, "java_Annotation337", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation337"):
                    opp_val = getattr(item, "java_Annotation337", None)
                    
                    setattr(item, "java_Annotation337", self)
                    

class java_IfStatement(Statement):

    pass
class java_SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java_ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java_SwitchCase(Statement):

    def __init__(self, default: bool, java_SwitchCase: "java_Expression" = None):
        self.default = default
        self.java_SwitchCase = java_SwitchCase
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def java_SwitchCase(self):
        return self.__java_SwitchCase

    @java_SwitchCase.setter
    def java_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SwitchCase__java_SwitchCase", None)
        self.__java_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression284"):
                opp_val = getattr(old_value, "java_Expression284", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression284"):
                opp_val = getattr(value, "java_Expression284", None)
                setattr(value, "java_Expression284", self)

class java_ThrowStatement(Statement):

    pass
class java_WhileStatement(Statement):

    pass
class java_AssertStatement(Statement):

    pass
class java_Manifest:

    pass
class NamedElement:

    pass
class java_Package(NamedElement):

    pass
class java_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, VariableDeclaration: "java_SingleVariableAccess" = None, java_VariableDeclaration: "java_Expression" = None, variable: set["java_SingleVariableAccess"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclaration = VariableDeclaration
        self.java_VariableDeclaration = java_VariableDeclaration
        self.variable = variable if variable is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclaration__variable", None)
        self.__variable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableAccess"):
                    opp_val = getattr(item, "SingleVariableAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableAccess"):
                    opp_val = getattr(item, "SingleVariableAccess", None)
                    
                    setattr(item, "SingleVariableAccess", self)
                    

    @property
    def java_VariableDeclaration(self):
        return self.__java_VariableDeclaration

    @java_VariableDeclaration.setter
    def java_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclaration__java_VariableDeclaration", None)
        self.__java_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression327"):
                opp_val = getattr(old_value, "java_Expression327", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression327"):
                opp_val = getattr(value, "java_Expression327", None)
                setattr(value, "java_Expression327", self)

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclaration__VariableDeclaration", None)
        self.__VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usageInVariableAccess"):
                opp_val = getattr(old_value, "usageInVariableAccess", None)
                if opp_val == self:
                    setattr(old_value, "usageInVariableAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usageInVariableAccess"):
                opp_val = getattr(value, "usageInVariableAccess", None)
                setattr(value, "usageInVariableAccess", self)

class java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java_CompilationUnit: "java_ASTNode" = None, java_CompilationUnit108: set["java_Comment"] = None, java_CompilationUnit115: set["java_AbstractTypeDeclaration"] = None, java_CompilationUnit111: set["java_ImportDeclaration"] = None, java_CompilationUnit113: "java_Package" = None, java_CompilationUnit220: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_CompilationUnit = java_CompilationUnit
        self.java_CompilationUnit108 = java_CompilationUnit108 if java_CompilationUnit108 is not None else set()
        self.java_CompilationUnit115 = java_CompilationUnit115 if java_CompilationUnit115 is not None else set()
        self.java_CompilationUnit111 = java_CompilationUnit111 if java_CompilationUnit111 is not None else set()
        self.java_CompilationUnit113 = java_CompilationUnit113
        self.java_CompilationUnit220 = java_CompilationUnit220
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_CompilationUnit115(self):
        return self.__java_CompilationUnit115

    @java_CompilationUnit115.setter
    def java_CompilationUnit115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit115", None)
        self.__java_CompilationUnit115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AbstractTypeDeclaration116"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration116", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AbstractTypeDeclaration116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AbstractTypeDeclaration116"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration116", None)
                    
                    setattr(item, "java_AbstractTypeDeclaration116", self)
                    

    @property
    def java_CompilationUnit113(self):
        return self.__java_CompilationUnit113

    @java_CompilationUnit113.setter
    def java_CompilationUnit113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit113", None)
        self.__java_CompilationUnit113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Package"):
                opp_val = getattr(old_value, "java_Package", None)
                if opp_val == self:
                    setattr(old_value, "java_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Package"):
                opp_val = getattr(value, "java_Package", None)
                setattr(value, "java_Package", self)

    @property
    def java_CompilationUnit111(self):
        return self.__java_CompilationUnit111

    @java_CompilationUnit111.setter
    def java_CompilationUnit111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit111", None)
        self.__java_CompilationUnit111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ImportDeclaration"):
                    opp_val = getattr(item, "java_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ImportDeclaration"):
                    opp_val = getattr(item, "java_ImportDeclaration", None)
                    
                    setattr(item, "java_ImportDeclaration", self)
                    

    @property
    def java_CompilationUnit220(self):
        return self.__java_CompilationUnit220

    @java_CompilationUnit220.setter
    def java_CompilationUnit220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit220", None)
        self.__java_CompilationUnit220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model219"):
                opp_val = getattr(old_value, "java_Model219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model219"):
                opp_val = getattr(value, "java_Model219", None)
                if opp_val is None:
                    setattr(value, "java_Model219", set([self]))
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
            if hasattr(old_value, "java_ASTNode41"):
                opp_val = getattr(old_value, "java_ASTNode41", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode41"):
                opp_val = getattr(value, "java_ASTNode41", None)
                setattr(value, "java_ASTNode41", self)

    @property
    def java_CompilationUnit108(self):
        return self.__java_CompilationUnit108

    @java_CompilationUnit108.setter
    def java_CompilationUnit108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit108", None)
        self.__java_CompilationUnit108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Comment109"):
                    opp_val = getattr(item, "java_Comment109", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Comment109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Comment109"):
                    opp_val = getattr(item, "java_Comment109", None)
                    
                    setattr(item, "java_Comment109", self)
                    

class java_LabeledStatement(Statement, NamedElement):

    pass
class java_UnresolvedItem(NamedElement):

    pass
class java_Type(NamedElement):

    pass
class java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, java_Archive: "java_Manifest" = None, java_Archive223: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_Archive = java_Archive
        self.java_Archive223 = java_Archive223
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_Archive223(self):
        return self.__java_Archive223

    @java_Archive223.setter
    def java_Archive223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Archive__java_Archive223", None)
        self.__java_Archive223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model222"):
                opp_val = getattr(old_value, "java_Model222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model222"):
                opp_val = getattr(value, "java_Model222", None)
                if opp_val is None:
                    setattr(value, "java_Model222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "java_Manifest"):
                opp_val = getattr(old_value, "java_Manifest", None)
                if opp_val == self:
                    setattr(old_value, "java_Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest"):
                opp_val = getattr(value, "java_Manifest", None)
                setattr(value, "java_Manifest", self)

class java_AnnotationMemberValuePair(NamedElement):

    pass
class java_Annotation(Expression):

    pass
class java_VariableDeclarationFragment(VariableDeclaration):

    pass
class java_TypeAccess(Expression, NamespaceAccess):

    pass
class java_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "java_AbstractMethodDeclaration" = None, SingleVariableDeclaration94: "java_CatchClause" = None, SingleVariableDeclaration130: "java_EnhancedForStatement" = None, SingleVariableDeclaration228: "java_Modifier" = None, singleVariableDeclaration: "java_Modifier" = None, java_SingleVariableDeclaration: "java_TypeAccess" = None, java_SingleVariableDeclaration273: set["java_Annotation"] = None, parameters: "java_AbstractMethodDeclaration" = None, exception: "java_CatchClause" = None, parameter: "java_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration94 = SingleVariableDeclaration94
        self.SingleVariableDeclaration130 = SingleVariableDeclaration130
        self.SingleVariableDeclaration228 = SingleVariableDeclaration228
        self.singleVariableDeclaration = singleVariableDeclaration
        self.java_SingleVariableDeclaration = java_SingleVariableDeclaration
        self.java_SingleVariableDeclaration273 = java_SingleVariableDeclaration273 if java_SingleVariableDeclaration273 is not None else set()
        self.parameters = parameters
        self.exception = exception
        self.parameter = parameter
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__exception", None)
        self.__exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CatchClause"):
                opp_val = getattr(old_value, "CatchClause", None)
                if opp_val == self:
                    setattr(old_value, "CatchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CatchClause"):
                opp_val = getattr(value, "CatchClause", None)
                setattr(value, "CatchClause", self)

    @property
    def SingleVariableDeclaration94(self):
        return self.__SingleVariableDeclaration94

    @SingleVariableDeclaration94.setter
    def SingleVariableDeclaration94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration94", None)
        self.__SingleVariableDeclaration94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catchClause"):
                opp_val = getattr(old_value, "catchClause", None)
                if opp_val == self:
                    setattr(old_value, "catchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catchClause"):
                opp_val = getattr(value, "catchClause", None)
                setattr(value, "catchClause", self)

    @property
    def java_SingleVariableDeclaration273(self):
        return self.__java_SingleVariableDeclaration273

    @java_SingleVariableDeclaration273.setter
    def java_SingleVariableDeclaration273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration273", None)
        self.__java_SingleVariableDeclaration273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Annotation274"):
                    opp_val = getattr(item, "java_Annotation274", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation274"):
                    opp_val = getattr(item, "java_Annotation274", None)
                    
                    setattr(item, "java_Annotation274", self)
                    

    @property
    def singleVariableDeclaration(self):
        return self.__singleVariableDeclaration

    @singleVariableDeclaration.setter
    def singleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__singleVariableDeclaration", None)
        self.__singleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Modifier269"):
                opp_val = getattr(old_value, "Modifier269", None)
                if opp_val == self:
                    setattr(old_value, "Modifier269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier269"):
                opp_val = getattr(value, "Modifier269", None)
                setattr(value, "Modifier269", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnhancedForStatement"):
                opp_val = getattr(old_value, "EnhancedForStatement", None)
                if opp_val == self:
                    setattr(old_value, "EnhancedForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnhancedForStatement"):
                opp_val = getattr(value, "EnhancedForStatement", None)
                setattr(value, "EnhancedForStatement", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMethodDeclaration276"):
                opp_val = getattr(old_value, "AbstractMethodDeclaration276", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMethodDeclaration276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMethodDeclaration276"):
                opp_val = getattr(value, "AbstractMethodDeclaration276", None)
                setattr(value, "AbstractMethodDeclaration276", self)

    @property
    def SingleVariableDeclaration228(self):
        return self.__SingleVariableDeclaration228

    @SingleVariableDeclaration228.setter
    def SingleVariableDeclaration228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration228", None)
        self.__SingleVariableDeclaration228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifier227"):
                opp_val = getattr(old_value, "modifier227", None)
                if opp_val == self:
                    setattr(old_value, "modifier227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifier227"):
                opp_val = getattr(value, "modifier227", None)
                setattr(value, "modifier227", self)

    @property
    def java_SingleVariableDeclaration(self):
        return self.__java_SingleVariableDeclaration

    @java_SingleVariableDeclaration.setter
    def java_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration", None)
        self.__java_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess271"):
                opp_val = getattr(old_value, "java_TypeAccess271", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess271"):
                opp_val = getattr(value, "java_TypeAccess271", None)
                setattr(value, "java_TypeAccess271", self)

    @property
    def SingleVariableDeclaration(self):
        return self.__SingleVariableDeclaration

    @SingleVariableDeclaration.setter
    def SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration", None)
        self.__SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodDeclaration"):
                opp_val = getattr(old_value, "methodDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodDeclaration"):
                opp_val = getattr(value, "methodDeclaration", None)
                if opp_val is None:
                    setattr(value, "methodDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SingleVariableDeclaration130(self):
        return self.__SingleVariableDeclaration130

    @SingleVariableDeclaration130.setter
    def SingleVariableDeclaration130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration130", None)
        self.__SingleVariableDeclaration130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enhancedForStatement"):
                opp_val = getattr(old_value, "enhancedForStatement", None)
                if opp_val == self:
                    setattr(old_value, "enhancedForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enhancedForStatement"):
                opp_val = getattr(value, "enhancedForStatement", None)
                setattr(value, "enhancedForStatement", self)

class java_Block(Statement):

    pass
class java_BodyDeclaration(NamedElement):

    pass
class Type:

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
            if hasattr(old_value, "java_TypeAccess73"):
                opp_val = getattr(old_value, "java_TypeAccess73", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess73"):
                opp_val = getattr(value, "java_TypeAccess73", None)
                setattr(value, "java_TypeAccess73", self)

class java_WildCardType(Type):

    def __init__(self, upperBound: bool, java_WildCardType: "java_TypeAccess" = None):
        self.upperBound = upperBound
        self.java_WildCardType = java_WildCardType
        
    @property
    def upperBound(self) -> bool:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: bool):
        self.__upperBound = upperBound

    @property
    def java_WildCardType(self):
        return self.__java_WildCardType

    @java_WildCardType.setter
    def java_WildCardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_WildCardType__java_WildCardType", None)
        self.__java_WildCardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess339"):
                opp_val = getattr(old_value, "java_TypeAccess339", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess339"):
                opp_val = getattr(value, "java_TypeAccess339", None)
                setattr(value, "java_TypeAccess339", self)

class java_PrimitiveType(Type):

    pass
class java_ParameterizedType(Type):

    pass
class java_UnresolvedType(UnresolvedItem, Type):

    pass
class ASTNode:

    pass
class java_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, NamedElement: "java_ImportDeclaration" = None, java_NamedElement: "java_MemberRef" = None, importedElement: set["java_ImportDeclaration"] = None):
        self.name = name
        self.proxy = proxy
        self.NamedElement = NamedElement
        self.java_NamedElement = java_NamedElement
        self.importedElement = importedElement if importedElement is not None else set()
        
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
    def importedElement(self):
        return self.__importedElement

    @importedElement.setter
    def importedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_NamedElement__importedElement", None)
        self.__importedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ImportDeclaration"):
                    opp_val = getattr(item, "ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ImportDeclaration"):
                    opp_val = getattr(item, "ImportDeclaration", None)
                    
                    setattr(item, "ImportDeclaration", self)
                    

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagesInImports"):
                opp_val = getattr(old_value, "usagesInImports", None)
                if opp_val == self:
                    setattr(old_value, "usagesInImports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagesInImports"):
                opp_val = getattr(value, "usagesInImports", None)
                setattr(value, "usagesInImports", self)

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
            if hasattr(old_value, "java_MemberRef"):
                opp_val = getattr(old_value, "java_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "java_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_MemberRef"):
                opp_val = getattr(value, "java_MemberRef", None)
                setattr(value, "java_MemberRef", self)

class java_AnonymousClassDeclaration(ASTNode):

    pass
class java_MemberRef(ASTNode):

    pass
class java_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "java_BodyDeclaration" = None, modifier227: "java_SingleVariableDeclaration" = None, modifier230: "java_VariableDeclarationStatement" = None, modifier232: "java_VariableDeclarationExpression" = None, modifier: "java_BodyDeclaration" = None, Modifier269: "java_SingleVariableDeclaration" = None, Modifier335: "java_VariableDeclarationStatement" = None, Modifier330: "java_VariableDeclarationExpression" = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.native = native
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.Modifier = Modifier
        self.modifier227 = modifier227
        self.modifier230 = modifier230
        self.modifier232 = modifier232
        self.modifier = modifier
        self.Modifier269 = Modifier269
        self.Modifier335 = Modifier335
        self.Modifier330 = Modifier330
        
    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def modifier227(self):
        return self.__modifier227

    @modifier227.setter
    def modifier227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier227", None)
        self.__modifier227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleVariableDeclaration228"):
                opp_val = getattr(old_value, "SingleVariableDeclaration228", None)
                if opp_val == self:
                    setattr(old_value, "SingleVariableDeclaration228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleVariableDeclaration228"):
                opp_val = getattr(value, "SingleVariableDeclaration228", None)
                setattr(value, "SingleVariableDeclaration228", self)

    @property
    def modifier230(self):
        return self.__modifier230

    @modifier230.setter
    def modifier230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier230", None)
        self.__modifier230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationStatement"):
                opp_val = getattr(old_value, "VariableDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationStatement"):
                opp_val = getattr(value, "VariableDeclarationStatement", None)
                setattr(value, "VariableDeclarationStatement", self)

    @property
    def Modifier335(self):
        return self.__Modifier335

    @Modifier335.setter
    def Modifier335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier335", None)
        self.__Modifier335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variableDeclarationStatement"):
                opp_val = getattr(old_value, "variableDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "variableDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variableDeclarationStatement"):
                opp_val = getattr(value, "variableDeclarationStatement", None)
                setattr(value, "variableDeclarationStatement", self)

    @property
    def Modifier269(self):
        return self.__Modifier269

    @Modifier269.setter
    def Modifier269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier269", None)
        self.__Modifier269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "singleVariableDeclaration"):
                opp_val = getattr(old_value, "singleVariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "singleVariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "singleVariableDeclaration"):
                opp_val = getattr(value, "singleVariableDeclaration", None)
                setattr(value, "singleVariableDeclaration", self)

    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier", None)
        self.__modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyDeclaration225"):
                opp_val = getattr(old_value, "BodyDeclaration225", None)
                if opp_val == self:
                    setattr(old_value, "BodyDeclaration225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyDeclaration225"):
                opp_val = getattr(value, "BodyDeclaration225", None)
                setattr(value, "BodyDeclaration225", self)

    @property
    def Modifier330(self):
        return self.__Modifier330

    @Modifier330.setter
    def Modifier330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier330", None)
        self.__Modifier330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variableDeclarationExpression"):
                opp_val = getattr(old_value, "variableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "variableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variableDeclarationExpression"):
                opp_val = getattr(value, "variableDeclarationExpression", None)
                setattr(value, "variableDeclarationExpression", self)

    @property
    def modifier232(self):
        return self.__modifier232

    @modifier232.setter
    def modifier232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier232", None)
        self.__modifier232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationExpression"):
                opp_val = getattr(old_value, "VariableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationExpression"):
                opp_val = getattr(value, "VariableDeclarationExpression", None)
                setattr(value, "VariableDeclarationExpression", self)

    @property
    def Modifier(self):
        return self.__Modifier

    @Modifier.setter
    def Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier", None)
        self.__Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bodyDeclaration"):
                opp_val = getattr(old_value, "bodyDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "bodyDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bodyDeclaration"):
                opp_val = getattr(value, "bodyDeclaration", None)
                setattr(value, "bodyDeclaration", self)

class java_Comment(ASTNode):

    def __init__(self, content: str, enclosedByParent: bool, prefixOfParent: bool, java_Comment: "java_AbstractTypeDeclaration" = None, java_Comment18: "java_AbstractTypeDeclaration" = None, java_Comment39: "java_ASTNode" = None, java_Comment109: "java_CompilationUnit" = None):
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.java_Comment = java_Comment
        self.java_Comment18 = java_Comment18
        self.java_Comment39 = java_Comment39
        self.java_Comment109 = java_Comment109
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def prefixOfParent(self) -> bool:
        return self.__prefixOfParent

    @prefixOfParent.setter
    def prefixOfParent(self, prefixOfParent: bool):
        self.__prefixOfParent = prefixOfParent

    @property
    def enclosedByParent(self) -> bool:
        return self.__enclosedByParent

    @enclosedByParent.setter
    def enclosedByParent(self, enclosedByParent: bool):
        self.__enclosedByParent = enclosedByParent

    @property
    def java_Comment109(self):
        return self.__java_Comment109

    @java_Comment109.setter
    def java_Comment109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment109", None)
        self.__java_Comment109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit108"):
                opp_val = getattr(old_value, "java_CompilationUnit108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit108"):
                opp_val = getattr(value, "java_CompilationUnit108", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment18(self):
        return self.__java_Comment18

    @java_Comment18.setter
    def java_Comment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment18", None)
        self.__java_Comment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration17"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration17"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration17", None)
                if opp_val is None:
                    setattr(value, "java_AbstractTypeDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment39(self):
        return self.__java_Comment39

    @java_Comment39.setter
    def java_Comment39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment39", None)
        self.__java_Comment39 = value
        
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

class java_TagElement(ASTNode):

    def __init__(self, tagName: str, java_TagElement: "java_Javadoc" = None, java_TagElement296: set["java_ASTNode"] = None):
        self.tagName = tagName
        self.java_TagElement = java_TagElement
        self.java_TagElement296 = java_TagElement296 if java_TagElement296 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def java_TagElement(self):
        return self.__java_TagElement

    @java_TagElement.setter
    def java_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TagElement__java_TagElement", None)
        self.__java_TagElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Javadoc"):
                opp_val = getattr(old_value, "java_Javadoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Javadoc"):
                opp_val = getattr(value, "java_Javadoc", None)
                if opp_val is None:
                    setattr(value, "java_Javadoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TagElement296(self):
        return self.__java_TagElement296

    @java_TagElement296.setter
    def java_TagElement296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TagElement__java_TagElement296", None)
        self.__java_TagElement296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ASTNode297"):
                    opp_val = getattr(item, "java_ASTNode297", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ASTNode297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ASTNode297"):
                    opp_val = getattr(item, "java_ASTNode297", None)
                    
                    setattr(item, "java_ASTNode297", self)
                    

class java_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class java_NamespaceAccess(ASTNode):

    pass
class java_MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: bool, java_MethodRefParameter: "java_MethodRef" = None, java_MethodRefParameter211: "java_TypeAccess" = None):
        self.name = name
        self.varargs = varargs
        self.java_MethodRefParameter = java_MethodRefParameter
        self.java_MethodRefParameter211 = java_MethodRefParameter211
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def java_MethodRefParameter211(self):
        return self.__java_MethodRefParameter211

    @java_MethodRefParameter211.setter
    def java_MethodRefParameter211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodRefParameter__java_MethodRefParameter211", None)
        self.__java_MethodRefParameter211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess212"):
                opp_val = getattr(old_value, "java_TypeAccess212", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess212"):
                opp_val = getattr(value, "java_TypeAccess212", None)
                setattr(value, "java_TypeAccess212", self)

    @property
    def java_MethodRefParameter(self):
        return self.__java_MethodRefParameter

    @java_MethodRefParameter.setter
    def java_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodRefParameter__java_MethodRefParameter", None)
        self.__java_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_MethodRef209"):
                opp_val = getattr(old_value, "java_MethodRef209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_MethodRef209"):
                opp_val = getattr(value, "java_MethodRef209", None)
                if opp_val is None:
                    setattr(value, "java_MethodRef209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_AbstractVariablesContainer(ASTNode):

    pass
class java_Statement(ASTNode):

    pass
class java_Expression(ASTNode):

    pass
class java_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, java_ImportDeclaration: "java_CompilationUnit" = None, usagesInImports: "java_NamedElement" = None, ImportDeclaration: "java_NamedElement" = None):
        self.static = static
        self.java_ImportDeclaration = java_ImportDeclaration
        self.usagesInImports = usagesInImports
        self.ImportDeclaration = ImportDeclaration
        
    @property
    def static(self) -> bool:
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
            if hasattr(old_value, "java_CompilationUnit111"):
                opp_val = getattr(old_value, "java_CompilationUnit111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit111"):
                opp_val = getattr(value, "java_CompilationUnit111", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def usagesInImports(self):
        return self.__usagesInImports

    @usagesInImports.setter
    def usagesInImports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__usagesInImports", None)
        self.__usagesInImports = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedElement"):
                opp_val = getattr(old_value, "NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedElement"):
                opp_val = getattr(value, "NamedElement", None)
                setattr(value, "NamedElement", self)

    @property
    def ImportDeclaration(self):
        return self.__ImportDeclaration

    @ImportDeclaration.setter
    def ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__ImportDeclaration", None)
        self.__ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importedElement"):
                opp_val = getattr(old_value, "importedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importedElement"):
                opp_val = getattr(value, "importedElement", None)
                if opp_val is None:
                    setattr(value, "importedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_AbstractMethodInvocation(ASTNode):

    pass
class java_MethodRef(ASTNode):

    pass
class java_TypeParameter(Type):

    pass
class BodyDeclaration:

    pass
class java_FieldDeclaration(AbstractVariablesContainer, BodyDeclaration):

    pass
class java_AbstractTypeDeclaration(Type, BodyDeclaration):

    pass
class java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class java_Initializer(BodyDeclaration):

    pass
class java_EnumConstantDeclaration(VariableDeclaration, BodyDeclaration):

    pass
class java_AbstractMethodDeclaration(BodyDeclaration):

    pass