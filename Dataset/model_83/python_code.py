from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrefixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    COMPLEMENT = "COMPLEMENT"
    NOT = "NOT"
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
class AssignmentKind(Enum):
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
    BIT_XOR_ASSIGN = "BIT_XOR_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"
    LEFT_SHIFT_ASSIGN = "LEFT_SHIFT_ASSIGN"
    RIGHT_SHIFT_SIGNED_ASSIGN = "RIGHT_SHIFT_SIGNED_ASSIGN"
    RIGHT_SHIFT_UNSIGNED_ASSIGN = "RIGHT_SHIFT_UNSIGNED_ASSIGN"
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    BIT_AND_ASSIGN = "BIT_AND_ASSIGN"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
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


############################################
# Definition of Classes
############################################

class VariableDeclarationFragment:

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
class AnnotationTypeMemberDeclaration:

    pass
class UnresolvedItem:

    pass
class java_UnresolvedVariableDeclarationFragment(VariableDeclarationFragment, UnresolvedItem):

    pass
class java_UnresolvedLabeledStatement(LabeledStatement, UnresolvedItem):

    pass
class java_UnresolvedClassDeclaration(UnresolvedItem, ClassDeclaration):

    pass
class java_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class java_UnresolvedAnnotationTypeMemberDeclaration(AnnotationTypeMemberDeclaration, UnresolvedItem):

    pass
class java_UnresolvedEnumDeclaration(EnumDeclaration, UnresolvedItem):

    pass
class java_UnresolvedMethodDeclaration(MethodDeclaration, UnresolvedItem):

    pass
class java_UnresolvedInterfaceDeclaration(InterfaceDeclaration, UnresolvedItem):

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
class java_PrimitiveTypeChar(PrimitiveType):

    pass
class java_PrimitiveTypeInt(PrimitiveType):

    pass
class java_PrimitiveTypeFloat(PrimitiveType):

    pass
class java_PrimitiveTypeDouble(PrimitiveType):

    pass
class java_PrimitiveTypeLong(PrimitiveType):

    pass
class java_PrimitiveTypeVoid(PrimitiveType):

    pass
class java_PrimitiveTypeByte(PrimitiveType):

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

    def __init__(self, name: str, java_Model247: set["java_Archive"] = None, model: set["java_Package"] = None, java_Model: set["java_Type"] = None, java_Model239: set["java_UnresolvedItem"] = None, java_Model241: set["java_CompilationUnit"] = None, java_Model244: set["java_ClassFile"] = None, Model: "java_Package" = None):
        self.name = name
        self.java_Model247 = java_Model247 if java_Model247 is not None else set()
        self.model = model if model is not None else set()
        self.java_Model = java_Model if java_Model is not None else set()
        self.java_Model239 = java_Model239 if java_Model239 is not None else set()
        self.java_Model241 = java_Model241 if java_Model241 is not None else set()
        self.java_Model244 = java_Model244 if java_Model244 is not None else set()
        self.Model = Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Model241(self):
        return self.__java_Model241

    @java_Model241.setter
    def java_Model241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model241", None)
        self.__java_Model241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_CompilationUnit242"):
                    opp_val = getattr(item, "java_CompilationUnit242", None)
                    
                    if opp_val == self:
                        setattr(item, "java_CompilationUnit242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_CompilationUnit242"):
                    opp_val = getattr(item, "java_CompilationUnit242", None)
                    
                    setattr(item, "java_CompilationUnit242", self)
                    

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
                if hasattr(item, "Package236"):
                    opp_val = getattr(item, "Package236", None)
                    
                    if opp_val == self:
                        setattr(item, "Package236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package236"):
                    opp_val = getattr(item, "Package236", None)
                    
                    setattr(item, "Package236", self)
                    

    @property
    def java_Model239(self):
        return self.__java_Model239

    @java_Model239.setter
    def java_Model239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model239", None)
        self.__java_Model239 = value if value is not None else set()
        
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
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElements261"):
                opp_val = getattr(old_value, "ownedElements261", None)
                if opp_val == self:
                    setattr(old_value, "ownedElements261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElements261"):
                opp_val = getattr(value, "ownedElements261", None)
                setattr(value, "ownedElements261", self)

    @property
    def java_Model247(self):
        return self.__java_Model247

    @java_Model247.setter
    def java_Model247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model247", None)
        self.__java_Model247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Archive248"):
                    opp_val = getattr(item, "java_Archive248", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Archive248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Archive248"):
                    opp_val = getattr(item, "java_Archive248", None)
                    
                    setattr(item, "java_Archive248", self)
                    

    @property
    def java_Model244(self):
        return self.__java_Model244

    @java_Model244.setter
    def java_Model244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__java_Model244", None)
        self.__java_Model244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ClassFile245"):
                    opp_val = getattr(item, "java_ClassFile245", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ClassFile245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ClassFile245"):
                    opp_val = getattr(item, "java_ClassFile245", None)
                    
                    setattr(item, "java_ClassFile245", self)
                    

class java_ManifestEntry:

    def __init__(self, name: str, java_ManifestEntry209: set["java_ManifestAttribute"] = None, java_ManifestEntry: "java_Manifest" = None):
        self.name = name
        self.java_ManifestEntry209 = java_ManifestEntry209 if java_ManifestEntry209 is not None else set()
        self.java_ManifestEntry = java_ManifestEntry
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "java_Manifest207"):
                opp_val = getattr(old_value, "java_Manifest207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest207"):
                opp_val = getattr(value, "java_Manifest207", None)
                if opp_val is None:
                    setattr(value, "java_Manifest207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ManifestEntry209(self):
        return self.__java_ManifestEntry209

    @java_ManifestEntry209.setter
    def java_ManifestEntry209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestEntry__java_ManifestEntry209", None)
        self.__java_ManifestEntry209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ManifestAttribute210"):
                    opp_val = getattr(item, "java_ManifestAttribute210", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ManifestAttribute210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ManifestAttribute210"):
                    opp_val = getattr(item, "java_ManifestAttribute210", None)
                    
                    setattr(item, "java_ManifestAttribute210", self)
                    

class java_ManifestAttribute:

    def __init__(self, key: str, value: str, java_ManifestAttribute210: "java_ManifestEntry" = None, java_ManifestAttribute: "java_Manifest" = None):
        self.key = key
        self.value = value
        self.java_ManifestAttribute210 = java_ManifestAttribute210
        self.java_ManifestAttribute = java_ManifestAttribute
        
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
            if hasattr(old_value, "java_Manifest205"):
                opp_val = getattr(old_value, "java_Manifest205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest205"):
                opp_val = getattr(value, "java_Manifest205", None)
                if opp_val is None:
                    setattr(value, "java_Manifest205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ManifestAttribute210(self):
        return self.__java_ManifestAttribute210

    @java_ManifestAttribute210.setter
    def java_ManifestAttribute210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestAttribute__java_ManifestAttribute210", None)
        self.__java_ManifestAttribute210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ManifestEntry209"):
                opp_val = getattr(old_value, "java_ManifestEntry209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ManifestEntry209"):
                opp_val = getattr(value, "java_ManifestEntry209", None)
                if opp_val is None:
                    setattr(value, "java_ManifestEntry209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractVariablesContainer:

    pass
class VariableDeclaration:

    pass
class AbstractMethodDeclaration:

    pass
class java_MethodDeclaration(AbstractMethodDeclaration):

    def __init__(self, extraArrayDimensions: int, java_MethodDeclaration: "java_TypeAccess" = None, MethodDeclaration: "java_MethodDeclaration" = None, redefinitions: "java_MethodDeclaration" = None, MethodDeclaration222: "java_MethodDeclaration" = None, redefinedMethodDeclaration: set["java_MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.java_MethodDeclaration = java_MethodDeclaration
        self.MethodDeclaration = MethodDeclaration
        self.redefinitions = redefinitions
        self.MethodDeclaration222 = MethodDeclaration222
        self.redefinedMethodDeclaration = redefinedMethodDeclaration if redefinedMethodDeclaration is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

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
                if hasattr(item, "MethodDeclaration222"):
                    opp_val = getattr(item, "MethodDeclaration222", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodDeclaration222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodDeclaration222"):
                    opp_val = getattr(item, "MethodDeclaration222", None)
                    
                    setattr(item, "MethodDeclaration222", self)
                    

    @property
    def MethodDeclaration222(self):
        return self.__MethodDeclaration222

    @MethodDeclaration222.setter
    def MethodDeclaration222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__MethodDeclaration222", None)
        self.__MethodDeclaration222 = value
        
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
            if hasattr(old_value, "java_TypeAccess217"):
                opp_val = getattr(old_value, "java_TypeAccess217", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess217"):
                opp_val = getattr(value, "java_TypeAccess217", None)
                setattr(value, "java_TypeAccess217", self)

class java_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class TypeDeclaration:

    pass
class java_InterfaceDeclaration(TypeDeclaration):

    pass
class java_ClassDeclaration(TypeDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class java_SuperMethodInvocation(AbstractMethodInvocation, AbstractTypeQualifiedExpression):

    pass
class Comment:

    pass
class java_LineComment(Comment):

    pass
class java_Javadoc(Comment):

    pass
class java_BlockComment(Comment):

    pass
class AbstractTypeDeclaration:

    pass
class java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class java_UnresolvedTypeDeclaration(AbstractTypeDeclaration, UnresolvedItem):

    pass
class java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class java_Manifest:

    pass
class NamedElement:

    pass
class java_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, java_VariableDeclaration: "java_SingleVariableAccess" = None, java_VariableDeclaration351: "java_Expression" = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.java_VariableDeclaration = java_VariableDeclaration
        self.java_VariableDeclaration351 = java_VariableDeclaration351
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def java_VariableDeclaration351(self):
        return self.__java_VariableDeclaration351

    @java_VariableDeclaration351.setter
    def java_VariableDeclaration351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclaration__java_VariableDeclaration351", None)
        self.__java_VariableDeclaration351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression352"):
                opp_val = getattr(old_value, "java_Expression352", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression352"):
                opp_val = getattr(value, "java_Expression352", None)
                setattr(value, "java_Expression352", self)

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
            if hasattr(old_value, "java_SingleVariableAccess288"):
                opp_val = getattr(old_value, "java_SingleVariableAccess288", None)
                if opp_val == self:
                    setattr(old_value, "java_SingleVariableAccess288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_SingleVariableAccess288"):
                opp_val = getattr(value, "java_SingleVariableAccess288", None)
                setattr(value, "java_SingleVariableAccess288", self)

class java_Type(NamedElement):

    pass
class java_UnresolvedItem(NamedElement):

    pass
class java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java_CompilationUnit: "java_ASTNode" = None, java_CompilationUnit107: "java_ClassFile" = None, java_CompilationUnit133: "java_Package" = None, java_CompilationUnit136: set["java_AbstractTypeDeclaration"] = None, java_CompilationUnit128: set["java_Comment"] = None, java_CompilationUnit131: set["java_ImportDeclaration"] = None, java_CompilationUnit242: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_CompilationUnit = java_CompilationUnit
        self.java_CompilationUnit107 = java_CompilationUnit107
        self.java_CompilationUnit133 = java_CompilationUnit133
        self.java_CompilationUnit136 = java_CompilationUnit136 if java_CompilationUnit136 is not None else set()
        self.java_CompilationUnit128 = java_CompilationUnit128 if java_CompilationUnit128 is not None else set()
        self.java_CompilationUnit131 = java_CompilationUnit131 if java_CompilationUnit131 is not None else set()
        self.java_CompilationUnit242 = java_CompilationUnit242
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_CompilationUnit131(self):
        return self.__java_CompilationUnit131

    @java_CompilationUnit131.setter
    def java_CompilationUnit131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit131", None)
        self.__java_CompilationUnit131 = value if value is not None else set()
        
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
    def java_CompilationUnit107(self):
        return self.__java_CompilationUnit107

    @java_CompilationUnit107.setter
    def java_CompilationUnit107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit107", None)
        self.__java_CompilationUnit107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ClassFile106"):
                opp_val = getattr(old_value, "java_ClassFile106", None)
                if opp_val == self:
                    setattr(old_value, "java_ClassFile106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ClassFile106"):
                opp_val = getattr(value, "java_ClassFile106", None)
                setattr(value, "java_ClassFile106", self)

    @property
    def java_CompilationUnit128(self):
        return self.__java_CompilationUnit128

    @java_CompilationUnit128.setter
    def java_CompilationUnit128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit128", None)
        self.__java_CompilationUnit128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Comment129"):
                    opp_val = getattr(item, "java_Comment129", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Comment129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Comment129"):
                    opp_val = getattr(item, "java_Comment129", None)
                    
                    setattr(item, "java_Comment129", self)
                    

    @property
    def java_CompilationUnit133(self):
        return self.__java_CompilationUnit133

    @java_CompilationUnit133.setter
    def java_CompilationUnit133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit133", None)
        self.__java_CompilationUnit133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Package134"):
                opp_val = getattr(old_value, "java_Package134", None)
                if opp_val == self:
                    setattr(old_value, "java_Package134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Package134"):
                opp_val = getattr(value, "java_Package134", None)
                setattr(value, "java_Package134", self)

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
            if hasattr(old_value, "java_ASTNode42"):
                opp_val = getattr(old_value, "java_ASTNode42", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode42"):
                opp_val = getattr(value, "java_ASTNode42", None)
                setattr(value, "java_ASTNode42", self)

    @property
    def java_CompilationUnit242(self):
        return self.__java_CompilationUnit242

    @java_CompilationUnit242.setter
    def java_CompilationUnit242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit242", None)
        self.__java_CompilationUnit242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model241"):
                opp_val = getattr(old_value, "java_Model241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model241"):
                opp_val = getattr(value, "java_Model241", None)
                if opp_val is None:
                    setattr(value, "java_Model241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_CompilationUnit136(self):
        return self.__java_CompilationUnit136

    @java_CompilationUnit136.setter
    def java_CompilationUnit136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit136", None)
        self.__java_CompilationUnit136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AbstractTypeDeclaration137"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration137", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AbstractTypeDeclaration137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AbstractTypeDeclaration137"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration137", None)
                    
                    setattr(item, "java_AbstractTypeDeclaration137", self)
                    

class java_ClassFile(NamedElement):

    def __init__(self, originalFilePath: str, java_ClassFile: "java_Archive" = None, java_ClassFile45: "java_ASTNode" = None, java_ClassFile106: "java_CompilationUnit" = None, java_ClassFile109: "java_Package" = None, java_ClassFile103: "java_AbstractTypeDeclaration" = None, java_ClassFile245: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_ClassFile = java_ClassFile
        self.java_ClassFile45 = java_ClassFile45
        self.java_ClassFile106 = java_ClassFile106
        self.java_ClassFile109 = java_ClassFile109
        self.java_ClassFile103 = java_ClassFile103
        self.java_ClassFile245 = java_ClassFile245
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_ClassFile109(self):
        return self.__java_ClassFile109

    @java_ClassFile109.setter
    def java_ClassFile109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile109", None)
        self.__java_ClassFile109 = value
        
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
    def java_ClassFile106(self):
        return self.__java_ClassFile106

    @java_ClassFile106.setter
    def java_ClassFile106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile106", None)
        self.__java_ClassFile106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit107"):
                opp_val = getattr(old_value, "java_CompilationUnit107", None)
                if opp_val == self:
                    setattr(old_value, "java_CompilationUnit107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit107"):
                opp_val = getattr(value, "java_CompilationUnit107", None)
                setattr(value, "java_CompilationUnit107", self)

    @property
    def java_ClassFile245(self):
        return self.__java_ClassFile245

    @java_ClassFile245.setter
    def java_ClassFile245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile245", None)
        self.__java_ClassFile245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model244"):
                opp_val = getattr(old_value, "java_Model244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model244"):
                opp_val = getattr(value, "java_Model244", None)
                if opp_val is None:
                    setattr(value, "java_Model244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ClassFile(self):
        return self.__java_ClassFile

    @java_ClassFile.setter
    def java_ClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile", None)
        self.__java_ClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Archive"):
                opp_val = getattr(old_value, "java_Archive", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Archive"):
                opp_val = getattr(value, "java_Archive", None)
                if opp_val is None:
                    setattr(value, "java_Archive", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ClassFile45(self):
        return self.__java_ClassFile45

    @java_ClassFile45.setter
    def java_ClassFile45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile45", None)
        self.__java_ClassFile45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode44"):
                opp_val = getattr(old_value, "java_ASTNode44", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode44"):
                opp_val = getattr(value, "java_ASTNode44", None)
                setattr(value, "java_ASTNode44", self)

    @property
    def java_ClassFile103(self):
        return self.__java_ClassFile103

    @java_ClassFile103.setter
    def java_ClassFile103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile103", None)
        self.__java_ClassFile103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration104"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration104", None)
                if opp_val == self:
                    setattr(old_value, "java_AbstractTypeDeclaration104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration104"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration104", None)
                setattr(value, "java_AbstractTypeDeclaration104", self)

class java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, java_Archive33: "java_Manifest" = None, java_Archive: set["java_ClassFile"] = None, java_Archive248: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_Archive33 = java_Archive33
        self.java_Archive = java_Archive if java_Archive is not None else set()
        self.java_Archive248 = java_Archive248
        
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
        self.__java_Archive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ClassFile"):
                    opp_val = getattr(item, "java_ClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ClassFile"):
                    opp_val = getattr(item, "java_ClassFile", None)
                    
                    setattr(item, "java_ClassFile", self)
                    

    @property
    def java_Archive248(self):
        return self.__java_Archive248

    @java_Archive248.setter
    def java_Archive248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Archive__java_Archive248", None)
        self.__java_Archive248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model247"):
                opp_val = getattr(old_value, "java_Model247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model247"):
                opp_val = getattr(value, "java_Model247", None)
                if opp_val is None:
                    setattr(value, "java_Model247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Archive33(self):
        return self.__java_Archive33

    @java_Archive33.setter
    def java_Archive33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Archive__java_Archive33", None)
        self.__java_Archive33 = value
        
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
class java_VariableDeclarationFragment(VariableDeclaration):

    pass
class java_ASTNode(ABC):

    pass
class Statement:

    pass
class java_VariableDeclarationStatement(AbstractVariablesContainer, Statement):

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
            if hasattr(old_value, "Modifier359"):
                opp_val = getattr(old_value, "Modifier359", None)
                if opp_val == self:
                    setattr(old_value, "Modifier359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier359"):
                opp_val = getattr(value, "Modifier359", None)
                setattr(value, "Modifier359", self)

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
                if hasattr(item, "java_Annotation361"):
                    opp_val = getattr(item, "java_Annotation361", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation361"):
                    opp_val = getattr(item, "java_Annotation361", None)
                    
                    setattr(item, "java_Annotation361", self)
                    

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
            if hasattr(old_value, "modifier255"):
                opp_val = getattr(old_value, "modifier255", None)
                if opp_val == self:
                    setattr(old_value, "modifier255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifier255"):
                opp_val = getattr(value, "modifier255", None)
                setattr(value, "modifier255", self)

class java_ForStatement(Statement):

    pass
class java_ContinueStatement(Statement):

    pass
class java_TryStatement(Statement):

    pass
class java_SuperConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_ReturnStatement(Statement):

    pass
class java_LabeledStatement(NamedElement, Statement):

    pass
class java_WhileStatement(Statement):

    pass
class java_BreakStatement(Statement):

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
            if hasattr(old_value, "java_Expression307"):
                opp_val = getattr(old_value, "java_Expression307", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression307"):
                opp_val = getattr(value, "java_Expression307", None)
                setattr(value, "java_Expression307", self)

class java_SynchronizedStatement(Statement):

    pass
class java_EmptyStatement(Statement):

    pass
class java_SwitchStatement(Statement):

    pass
class java_TypeDeclarationStatement(Statement):

    pass
class java_EnhancedForStatement(Statement):

    pass
class java_IfStatement(Statement):

    pass
class java_ThrowStatement(Statement):

    pass
class java_ConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class java_CatchClause(Statement):

    pass
class java_DoStatement(Statement):

    pass
class java_AssertStatement(Statement):

    pass
class java_Package(NamedElement):

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
            if hasattr(old_value, "java_TypeAccess78"):
                opp_val = getattr(old_value, "java_TypeAccess78", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess78"):
                opp_val = getattr(value, "java_TypeAccess78", None)
                setattr(value, "java_TypeAccess78", self)

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
            if hasattr(old_value, "java_TypeAccess363"):
                opp_val = getattr(old_value, "java_TypeAccess363", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess363"):
                opp_val = getattr(value, "java_TypeAccess363", None)
                setattr(value, "java_TypeAccess363", self)

class java_UnresolvedType(Type, UnresolvedItem):

    pass
class java_ParameterizedType(Type):

    pass
class java_PrimitiveType(Type):

    pass
class Expression:

    pass
class java_NullLiteral(Expression):

    pass
class java_VariableDeclarationExpression(Expression, AbstractVariablesContainer):

    pass
class java_ClassInstanceCreation(AbstractMethodInvocation, Expression):

    pass
class java_Assignment(Expression):

    def __init__(self, operator: str, java_Assignment: "java_Expression" = None, java_Assignment82: "java_Expression" = None):
        self.operator = operator
        self.java_Assignment = java_Assignment
        self.java_Assignment82 = java_Assignment82
        
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
            if hasattr(old_value, "java_Expression80"):
                opp_val = getattr(old_value, "java_Expression80", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression80"):
                opp_val = getattr(value, "java_Expression80", None)
                setattr(value, "java_Expression80", self)

    @property
    def java_Assignment82(self):
        return self.__java_Assignment82

    @java_Assignment82.setter
    def java_Assignment82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment82", None)
        self.__java_Assignment82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression83"):
                opp_val = getattr(old_value, "java_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression83"):
                opp_val = getattr(value, "java_Expression83", None)
                setattr(value, "java_Expression83", self)

class java_ArrayAccess(Expression):

    pass
class java_CastExpression(Expression):

    pass
class java_MethodInvocation(AbstractMethodInvocation, Expression):

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
            if hasattr(old_value, "java_Expression282"):
                opp_val = getattr(old_value, "java_Expression282", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression282"):
                opp_val = getattr(value, "java_Expression282", None)
                setattr(value, "java_Expression282", self)

class java_ArrayLengthAccess(Expression):

    pass
class java_Annotation(Expression):

    pass
class java_InstanceofExpression(Expression):

    pass
class java_ConditionalExpression(Expression):

    pass
class java_TypeLiteral(Expression):

    pass
class java_ParenthesizedExpression(Expression):

    pass
class java_ArrayInitializer(Expression):

    pass
class java_SingleVariableAccess(Expression):

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
            if hasattr(old_value, "java_Expression284"):
                opp_val = getattr(old_value, "java_Expression284", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression284"):
                opp_val = getattr(value, "java_Expression284", None)
                setattr(value, "java_Expression284", self)

class java_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

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
class java_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java_ArrayCreation(Expression):

    pass
class java_UnresolvedItemAccess(Expression, NamespaceAccess):

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

class java_InfixExpression(Expression):

    def __init__(self, operator: str, java_InfixExpression: "java_Expression" = None, java_InfixExpression188: "java_Expression" = None, java_InfixExpression191: set["java_Expression"] = None):
        self.operator = operator
        self.java_InfixExpression = java_InfixExpression
        self.java_InfixExpression188 = java_InfixExpression188
        self.java_InfixExpression191 = java_InfixExpression191 if java_InfixExpression191 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_InfixExpression191(self):
        return self.__java_InfixExpression191

    @java_InfixExpression191.setter
    def java_InfixExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression191", None)
        self.__java_InfixExpression191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Expression192"):
                    opp_val = getattr(item, "java_Expression192", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Expression192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Expression192"):
                    opp_val = getattr(item, "java_Expression192", None)
                    
                    setattr(item, "java_Expression192", self)
                    

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
            if hasattr(old_value, "java_Expression186"):
                opp_val = getattr(old_value, "java_Expression186", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression186"):
                opp_val = getattr(value, "java_Expression186", None)
                setattr(value, "java_Expression186", self)

    @property
    def java_InfixExpression188(self):
        return self.__java_InfixExpression188

    @java_InfixExpression188.setter
    def java_InfixExpression188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_InfixExpression__java_InfixExpression188", None)
        self.__java_InfixExpression188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression189"):
                opp_val = getattr(old_value, "java_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression189"):
                opp_val = getattr(value, "java_Expression189", None)
                setattr(value, "java_Expression189", self)

class java_AbstractTypeQualifiedExpression(Expression):

    pass
class java_TypeAccess(Expression, NamespaceAccess):

    pass
class java_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "java_AbstractMethodDeclaration" = None, SingleVariableDeclaration99: "java_CatchClause" = None, SingleVariableDeclaration151: "java_EnhancedForStatement" = None, SingleVariableDeclaration253: "java_Modifier" = None, singleVariableDeclaration: "java_Modifier" = None, java_SingleVariableDeclaration: "java_TypeAccess" = None, java_SingleVariableDeclaration297: set["java_Annotation"] = None, parameters: "java_AbstractMethodDeclaration" = None, exception: "java_CatchClause" = None, parameter: "java_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration99 = SingleVariableDeclaration99
        self.SingleVariableDeclaration151 = SingleVariableDeclaration151
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.singleVariableDeclaration = singleVariableDeclaration
        self.java_SingleVariableDeclaration = java_SingleVariableDeclaration
        self.java_SingleVariableDeclaration297 = java_SingleVariableDeclaration297 if java_SingleVariableDeclaration297 is not None else set()
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
    def SingleVariableDeclaration99(self):
        return self.__SingleVariableDeclaration99

    @SingleVariableDeclaration99.setter
    def SingleVariableDeclaration99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration99", None)
        self.__SingleVariableDeclaration99 = value
        
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
    def java_SingleVariableDeclaration(self):
        return self.__java_SingleVariableDeclaration

    @java_SingleVariableDeclaration.setter
    def java_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration", None)
        self.__java_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess295"):
                opp_val = getattr(old_value, "java_TypeAccess295", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess295"):
                opp_val = getattr(value, "java_TypeAccess295", None)
                setattr(value, "java_TypeAccess295", self)

    @property
    def java_SingleVariableDeclaration297(self):
        return self.__java_SingleVariableDeclaration297

    @java_SingleVariableDeclaration297.setter
    def java_SingleVariableDeclaration297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration297", None)
        self.__java_SingleVariableDeclaration297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Annotation298"):
                    opp_val = getattr(item, "java_Annotation298", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation298"):
                    opp_val = getattr(item, "java_Annotation298", None)
                    
                    setattr(item, "java_Annotation298", self)
                    

    @property
    def SingleVariableDeclaration151(self):
        return self.__SingleVariableDeclaration151

    @SingleVariableDeclaration151.setter
    def SingleVariableDeclaration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration151", None)
        self.__SingleVariableDeclaration151 = value
        
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
            if hasattr(old_value, "Modifier293"):
                opp_val = getattr(old_value, "Modifier293", None)
                if opp_val == self:
                    setattr(old_value, "Modifier293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier293"):
                opp_val = getattr(value, "Modifier293", None)
                setattr(value, "Modifier293", self)

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
            if hasattr(old_value, "AbstractMethodDeclaration"):
                opp_val = getattr(old_value, "AbstractMethodDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMethodDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMethodDeclaration"):
                opp_val = getattr(value, "AbstractMethodDeclaration", None)
                setattr(value, "AbstractMethodDeclaration", self)

    @property
    def SingleVariableDeclaration253(self):
        return self.__SingleVariableDeclaration253

    @SingleVariableDeclaration253.setter
    def SingleVariableDeclaration253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration253", None)
        self.__SingleVariableDeclaration253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifier252"):
                opp_val = getattr(old_value, "modifier252", None)
                if opp_val == self:
                    setattr(old_value, "modifier252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifier252"):
                opp_val = getattr(value, "modifier252", None)
                setattr(value, "modifier252", self)

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

class java_Block(Statement):

    pass
class BodyDeclaration:

    pass
class java_AbstractTypeDeclaration(Type, BodyDeclaration):

    pass
class java_FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass
class java_Initializer(BodyDeclaration):

    pass
class java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class java_EnumConstantDeclaration(BodyDeclaration, VariableDeclaration):

    pass
class java_AbstractMethodDeclaration(BodyDeclaration):

    pass
class ASTNode:

    pass
class java_MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: bool, java_MethodRefParameter233: "java_TypeAccess" = None, java_MethodRefParameter: "java_MethodRef" = None):
        self.name = name
        self.varargs = varargs
        self.java_MethodRefParameter233 = java_MethodRefParameter233
        self.java_MethodRefParameter = java_MethodRefParameter
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_MethodRefParameter233(self):
        return self.__java_MethodRefParameter233

    @java_MethodRefParameter233.setter
    def java_MethodRefParameter233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodRefParameter__java_MethodRefParameter233", None)
        self.__java_MethodRefParameter233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess234"):
                opp_val = getattr(old_value, "java_TypeAccess234", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess234"):
                opp_val = getattr(value, "java_TypeAccess234", None)
                setattr(value, "java_TypeAccess234", self)

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
            if hasattr(old_value, "java_MethodRef231"):
                opp_val = getattr(old_value, "java_MethodRef231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_MethodRef231"):
                opp_val = getattr(value, "java_MethodRef231", None)
                if opp_val is None:
                    setattr(value, "java_MethodRef231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_MemberRef(ASTNode):

    pass
class java_Expression(ASTNode):

    pass
class java_MethodRef(ASTNode):

    pass
class java_NamespaceAccess(ASTNode):

    pass
class java_AnonymousClassDeclaration(ASTNode):

    pass
class java_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class java_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, java_NamedElement: "java_ImportDeclaration" = None, java_NamedElement212: "java_MemberRef" = None):
        self.name = name
        self.proxy = proxy
        self.java_NamedElement = java_NamedElement
        self.java_NamedElement212 = java_NamedElement212
        
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
            if hasattr(old_value, "java_ImportDeclaration184"):
                opp_val = getattr(old_value, "java_ImportDeclaration184", None)
                if opp_val == self:
                    setattr(old_value, "java_ImportDeclaration184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ImportDeclaration184"):
                opp_val = getattr(value, "java_ImportDeclaration184", None)
                setattr(value, "java_ImportDeclaration184", self)

    @property
    def java_NamedElement212(self):
        return self.__java_NamedElement212

    @java_NamedElement212.setter
    def java_NamedElement212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_NamedElement__java_NamedElement212", None)
        self.__java_NamedElement212 = value
        
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

class java_AbstractVariablesContainer(ASTNode):

    pass
class java_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, java_ImportDeclaration: "java_CompilationUnit" = None, java_ImportDeclaration184: "java_NamedElement" = None):
        self.static = static
        self.java_ImportDeclaration = java_ImportDeclaration
        self.java_ImportDeclaration184 = java_ImportDeclaration184
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def java_ImportDeclaration184(self):
        return self.__java_ImportDeclaration184

    @java_ImportDeclaration184.setter
    def java_ImportDeclaration184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration184", None)
        self.__java_ImportDeclaration184 = value
        
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
    def java_ImportDeclaration(self):
        return self.__java_ImportDeclaration

    @java_ImportDeclaration.setter
    def java_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration", None)
        self.__java_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit131"):
                opp_val = getattr(old_value, "java_CompilationUnit131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit131"):
                opp_val = getattr(value, "java_CompilationUnit131", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_TagElement(ASTNode):

    def __init__(self, tagName: str, java_TagElement: "java_Javadoc" = None, java_TagElement319: set["java_ASTNode"] = None):
        self.tagName = tagName
        self.java_TagElement = java_TagElement
        self.java_TagElement319 = java_TagElement319 if java_TagElement319 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def java_TagElement319(self):
        return self.__java_TagElement319

    @java_TagElement319.setter
    def java_TagElement319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TagElement__java_TagElement319", None)
        self.__java_TagElement319 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ASTNode320"):
                    opp_val = getattr(item, "java_ASTNode320", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ASTNode320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ASTNode320"):
                    opp_val = getattr(item, "java_ASTNode320", None)
                    
                    setattr(item, "java_ASTNode320", self)
                    

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

class java_Comment(ASTNode):

    def __init__(self, content: str, enclosedByParent: bool, prefixOfParent: bool, java_Comment: "java_AbstractTypeDeclaration" = None, java_Comment17: "java_AbstractTypeDeclaration" = None, java_Comment40: "java_ASTNode" = None, java_Comment129: "java_CompilationUnit" = None):
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.java_Comment = java_Comment
        self.java_Comment17 = java_Comment17
        self.java_Comment40 = java_Comment40
        self.java_Comment129 = java_Comment129
        
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
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def java_Comment129(self):
        return self.__java_Comment129

    @java_Comment129.setter
    def java_Comment129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment129", None)
        self.__java_Comment129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit128"):
                opp_val = getattr(old_value, "java_CompilationUnit128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit128"):
                opp_val = getattr(value, "java_CompilationUnit128", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Comment17(self):
        return self.__java_Comment17

    @java_Comment17.setter
    def java_Comment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment17", None)
        self.__java_Comment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration16"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration16"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration16", None)
                if opp_val is None:
                    setattr(value, "java_AbstractTypeDeclaration16", set([self]))
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
    def java_Comment40(self):
        return self.__java_Comment40

    @java_Comment40.setter
    def java_Comment40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment40", None)
        self.__java_Comment40 = value
        
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

class java_Statement(ASTNode):

    pass
class java_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "java_BodyDeclaration" = None, modifier: "java_BodyDeclaration" = None, modifier252: "java_SingleVariableDeclaration" = None, modifier255: "java_VariableDeclarationStatement" = None, modifier257: "java_VariableDeclarationExpression" = None, Modifier293: "java_SingleVariableDeclaration" = None, Modifier354: "java_VariableDeclarationExpression" = None, Modifier359: "java_VariableDeclarationStatement" = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.native = native
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.Modifier = Modifier
        self.modifier = modifier
        self.modifier252 = modifier252
        self.modifier255 = modifier255
        self.modifier257 = modifier257
        self.Modifier293 = Modifier293
        self.Modifier354 = Modifier354
        self.Modifier359 = Modifier359
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

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
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def Modifier354(self):
        return self.__Modifier354

    @Modifier354.setter
    def Modifier354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier354", None)
        self.__Modifier354 = value
        
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
    def Modifier293(self):
        return self.__Modifier293

    @Modifier293.setter
    def Modifier293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier293", None)
        self.__Modifier293 = value
        
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
            if hasattr(old_value, "BodyDeclaration250"):
                opp_val = getattr(old_value, "BodyDeclaration250", None)
                if opp_val == self:
                    setattr(old_value, "BodyDeclaration250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyDeclaration250"):
                opp_val = getattr(value, "BodyDeclaration250", None)
                setattr(value, "BodyDeclaration250", self)

    @property
    def modifier252(self):
        return self.__modifier252

    @modifier252.setter
    def modifier252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier252", None)
        self.__modifier252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleVariableDeclaration253"):
                opp_val = getattr(old_value, "SingleVariableDeclaration253", None)
                if opp_val == self:
                    setattr(old_value, "SingleVariableDeclaration253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleVariableDeclaration253"):
                opp_val = getattr(value, "SingleVariableDeclaration253", None)
                setattr(value, "SingleVariableDeclaration253", self)

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

    @property
    def modifier257(self):
        return self.__modifier257

    @modifier257.setter
    def modifier257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier257", None)
        self.__modifier257 = value
        
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
    def modifier255(self):
        return self.__modifier255

    @modifier255.setter
    def modifier255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__modifier255", None)
        self.__modifier255 = value
        
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
    def Modifier359(self):
        return self.__Modifier359

    @Modifier359.setter
    def Modifier359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier359", None)
        self.__Modifier359 = value
        
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

class java_AbstractMethodInvocation(ASTNode):

    pass
class java_TypeParameter(Type):

    pass