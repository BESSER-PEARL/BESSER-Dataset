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
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
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
class VariableDeclarationFragment:

    pass
class ClassDeclaration:

    pass
class AnnotationTypeMemberDeclaration:

    pass
class UnresolvedItem:

    pass
class java_UnresolvedVariableDeclarationFragment(VariableDeclarationFragment, UnresolvedItem):

    pass
class java_UnresolvedClassDeclaration(UnresolvedItem, ClassDeclaration):

    pass
class java_UnresolvedMethodDeclaration(UnresolvedItem, MethodDeclaration):

    pass
class java_UnresolvedEnumDeclaration(UnresolvedItem, EnumDeclaration):

    pass
class java_UnresolvedAnnotationTypeMemberDeclaration(UnresolvedItem, AnnotationTypeMemberDeclaration):

    pass
class java_UnresolvedLabeledStatement(UnresolvedItem, LabeledStatement):

    pass
class java_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class java_UnresolvedInterfaceDeclaration(UnresolvedItem, InterfaceDeclaration):

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
class java_PrimitiveTypeVoid(PrimitiveType):

    pass
class java_PrimitiveTypeFloat(PrimitiveType):

    pass
class java_PrimitiveTypeChar(PrimitiveType):

    pass
class java_PrimitiveTypeLong(PrimitiveType):

    pass
class java_PrimitiveTypeByte(PrimitiveType):

    pass
class java_PrimitiveTypeShort(PrimitiveType):

    pass
class java_PrimitiveTypeInt(PrimitiveType):

    pass
class java_PrimitiveTypeDouble(PrimitiveType):

    pass
class java_PrimitiveTypeBoolean(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class java_PackageAccess(NamespaceAccess):

    pass
class java_Model:

    def __init__(self, name: str, model: set["java_Package"] = None, java_Model: set["java_Type"] = None, java_Model239: set["java_UnresolvedItem"] = None, java_Model241: set["java_CompilationUnit"] = None, java_Model244: set["java_ClassFile"] = None, java_Model247: set["java_Archive"] = None, Model: "java_Package" = None):
        self.name = name
        self.model = model if model is not None else set()
        self.java_Model = java_Model if java_Model is not None else set()
        self.java_Model239 = java_Model239 if java_Model239 is not None else set()
        self.java_Model241 = java_Model241 if java_Model241 is not None else set()
        self.java_Model244 = java_Model244 if java_Model244 is not None else set()
        self.java_Model247 = java_Model247 if java_Model247 is not None else set()
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
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElements262"):
                opp_val = getattr(old_value, "ownedElements262", None)
                if opp_val == self:
                    setattr(old_value, "ownedElements262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElements262"):
                opp_val = getattr(value, "ownedElements262", None)
                setattr(value, "ownedElements262", self)

class java_ManifestEntry:

    def __init__(self, name: str, java_ManifestEntry: "java_Manifest" = None, java_ManifestEntry211: set["java_ManifestAttribute"] = None):
        self.name = name
        self.java_ManifestEntry = java_ManifestEntry
        self.java_ManifestEntry211 = java_ManifestEntry211 if java_ManifestEntry211 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_ManifestEntry211(self):
        return self.__java_ManifestEntry211

    @java_ManifestEntry211.setter
    def java_ManifestEntry211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestEntry__java_ManifestEntry211", None)
        self.__java_ManifestEntry211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ManifestAttribute212"):
                    opp_val = getattr(item, "java_ManifestAttribute212", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ManifestAttribute212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ManifestAttribute212"):
                    opp_val = getattr(item, "java_ManifestAttribute212", None)
                    
                    setattr(item, "java_ManifestAttribute212", self)
                    

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
            if hasattr(old_value, "java_Manifest209"):
                opp_val = getattr(old_value, "java_Manifest209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Manifest209"):
                opp_val = getattr(value, "java_Manifest209", None)
                if opp_val is None:
                    setattr(value, "java_Manifest209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_ManifestAttribute:

    def __init__(self, key: str, value: str, java_ManifestAttribute: "java_Manifest" = None, java_ManifestAttribute212: "java_ManifestEntry" = None):
        self.key = key
        self.value = value
        self.java_ManifestAttribute = java_ManifestAttribute
        self.java_ManifestAttribute212 = java_ManifestAttribute212
        
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
    def java_ManifestAttribute212(self):
        return self.__java_ManifestAttribute212

    @java_ManifestAttribute212.setter
    def java_ManifestAttribute212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ManifestAttribute__java_ManifestAttribute212", None)
        self.__java_ManifestAttribute212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ManifestEntry211"):
                opp_val = getattr(old_value, "java_ManifestEntry211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ManifestEntry211"):
                opp_val = getattr(value, "java_ManifestEntry211", None)
                if opp_val is None:
                    setattr(value, "java_ManifestEntry211", set([self]))
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

    def __init__(self, extraArrayDimensions: int, java_MethodDeclaration: "java_TypeAccess" = None, MethodDeclaration: "java_MethodDeclaration" = None, redefinitions: "java_MethodDeclaration" = None, MethodDeclaration223: "java_MethodDeclaration" = None, redefinedMethodDeclaration: set["java_MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.java_MethodDeclaration = java_MethodDeclaration
        self.MethodDeclaration = MethodDeclaration
        self.redefinitions = redefinitions
        self.MethodDeclaration223 = MethodDeclaration223
        self.redefinedMethodDeclaration = redefinedMethodDeclaration if redefinedMethodDeclaration is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

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
            if hasattr(old_value, "java_TypeAccess218"):
                opp_val = getattr(old_value, "java_TypeAccess218", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess218"):
                opp_val = getattr(value, "java_TypeAccess218", None)
                setattr(value, "java_TypeAccess218", self)

    @property
    def MethodDeclaration223(self):
        return self.__MethodDeclaration223

    @MethodDeclaration223.setter
    def MethodDeclaration223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MethodDeclaration__MethodDeclaration223", None)
        self.__MethodDeclaration223 = value
        
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
                if hasattr(item, "MethodDeclaration223"):
                    opp_val = getattr(item, "MethodDeclaration223", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodDeclaration223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodDeclaration223"):
                    opp_val = getattr(item, "MethodDeclaration223", None)
                    
                    setattr(item, "MethodDeclaration223", self)
                    

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

class java_ConstructorDeclaration(AbstractMethodDeclaration):

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
class java_UnresolvedTypeDeclaration(UnresolvedItem, AbstractTypeDeclaration):

    pass
class java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class java_ASTNode(ABC):

    pass
class Statement:

    pass
class java_SwitchStatement(Statement):

    pass
class java_TryStatement(Statement):

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
                if hasattr(item, "java_Annotation362"):
                    opp_val = getattr(item, "java_Annotation362", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation362"):
                    opp_val = getattr(item, "java_Annotation362", None)
                    
                    setattr(item, "java_Annotation362", self)
                    

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
            if hasattr(old_value, "Modifier360"):
                opp_val = getattr(old_value, "Modifier360", None)
                if opp_val == self:
                    setattr(old_value, "Modifier360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier360"):
                opp_val = getattr(value, "Modifier360", None)
                setattr(value, "Modifier360", self)

class java_EmptyStatement(Statement):

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
            if hasattr(old_value, "java_Expression309"):
                opp_val = getattr(old_value, "java_Expression309", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression309"):
                opp_val = getattr(value, "java_Expression309", None)
                setattr(value, "java_Expression309", self)

class java_ContinueStatement(Statement):

    pass
class java_WhileStatement(Statement):

    pass
class java_ThrowStatement(Statement):

    pass
class java_BreakStatement(Statement):

    pass
class java_IfStatement(Statement):

    pass
class java_TypeDeclarationStatement(Statement):

    pass
class java_CatchClause(Statement):

    pass
class java_SynchronizedStatement(Statement):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_DoStatement(Statement):

    pass
class java_ConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class java_SuperConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class java_ReturnStatement(Statement):

    pass
class java_ForStatement(Statement):

    pass
class java_EnhancedForStatement(Statement):

    pass
class java_AssertStatement(Statement):

    pass
class java_Manifest:

    pass
class java_VariableDeclarationFragment(VariableDeclaration):

    pass
class Expression:

    pass
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

class java_ArrayInitializer(Expression):

    pass
class java_ParenthesizedExpression(Expression):

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

class java_InstanceofExpression(Expression):

    pass
class java_NullLiteral(Expression):

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
            if hasattr(old_value, "java_Expression286"):
                opp_val = getattr(old_value, "java_Expression286", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression286"):
                opp_val = getattr(value, "java_Expression286", None)
                setattr(value, "java_Expression286", self)

class java_UnresolvedItemAccess(NamespaceAccess, Expression):

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
            if hasattr(old_value, "java_Expression284"):
                opp_val = getattr(old_value, "java_Expression284", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression284"):
                opp_val = getattr(value, "java_Expression284", None)
                setattr(value, "java_Expression284", self)

class java_MethodInvocation(AbstractMethodInvocation, Expression):

    pass
class java_VariableDeclarationExpression(AbstractVariablesContainer, Expression):

    pass
class java_ArrayLengthAccess(Expression):

    pass
class java_FieldAccess(Expression):

    pass
class java_TypeLiteral(Expression):

    pass
class java_ArrayCreation(Expression):

    pass
class java_CastExpression(Expression):

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

    def __init__(self, operator: str, java_InfixExpression191: set["java_Expression"] = None, java_InfixExpression: "java_Expression" = None, java_InfixExpression188: "java_Expression" = None):
        self.operator = operator
        self.java_InfixExpression191 = java_InfixExpression191 if java_InfixExpression191 is not None else set()
        self.java_InfixExpression = java_InfixExpression
        self.java_InfixExpression188 = java_InfixExpression188
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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

class java_Assignment(Expression):

    def __init__(self, operator: str, java_Assignment: "java_Expression" = None, java_Assignment83: "java_Expression" = None):
        self.operator = operator
        self.java_Assignment = java_Assignment
        self.java_Assignment83 = java_Assignment83
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java_Assignment83(self):
        return self.__java_Assignment83

    @java_Assignment83.setter
    def java_Assignment83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Assignment__java_Assignment83", None)
        self.__java_Assignment83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression84"):
                opp_val = getattr(old_value, "java_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression84"):
                opp_val = getattr(value, "java_Expression84", None)
                setattr(value, "java_Expression84", self)

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
            if hasattr(old_value, "java_Expression81"):
                opp_val = getattr(old_value, "java_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression81"):
                opp_val = getattr(value, "java_Expression81", None)
                setattr(value, "java_Expression81", self)

class java_SingleVariableAccess(Expression):

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

class java_ArrayAccess(Expression):

    pass
class java_ClassInstanceCreation(AbstractMethodInvocation, Expression):

    pass
class java_AbstractTypeQualifiedExpression(Expression):

    pass
class Type:

    pass
class java_ParameterizedType(Type):

    pass
class java_PrimitiveType(Type):

    pass
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
            if hasattr(old_value, "java_TypeAccess364"):
                opp_val = getattr(old_value, "java_TypeAccess364", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess364"):
                opp_val = getattr(value, "java_TypeAccess364", None)
                setattr(value, "java_TypeAccess364", self)

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
            if hasattr(old_value, "java_TypeAccess79"):
                opp_val = getattr(old_value, "java_TypeAccess79", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess79"):
                opp_val = getattr(value, "java_TypeAccess79", None)
                setattr(value, "java_TypeAccess79", self)

class java_UnresolvedType(UnresolvedItem, Type):

    pass
class ASTNode:

    pass
class java_AnonymousClassDeclaration(ASTNode):

    pass
class java_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "java_BodyDeclaration" = None, modifier: "java_BodyDeclaration" = None, modifier252: "java_SingleVariableDeclaration" = None, modifier255: "java_VariableDeclarationStatement" = None, modifier257: "java_VariableDeclarationExpression" = None, Modifier294: "java_SingleVariableDeclaration" = None, Modifier355: "java_VariableDeclarationExpression" = None, Modifier360: "java_VariableDeclarationStatement" = None):
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
        self.Modifier294 = Modifier294
        self.Modifier355 = Modifier355
        self.Modifier360 = Modifier360
        
    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def Modifier355(self):
        return self.__Modifier355

    @Modifier355.setter
    def Modifier355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier355", None)
        self.__Modifier355 = value
        
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
    def Modifier294(self):
        return self.__Modifier294

    @Modifier294.setter
    def Modifier294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier294", None)
        self.__Modifier294 = value
        
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
    def Modifier360(self):
        return self.__Modifier360

    @Modifier360.setter
    def Modifier360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Modifier__Modifier360", None)
        self.__Modifier360 = value
        
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

class java_MemberRef(ASTNode):

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

class java_TagElement(ASTNode):

    def __init__(self, tagName: str, java_TagElement: "java_Javadoc" = None, java_TagElement321: set["java_ASTNode"] = None):
        self.tagName = tagName
        self.java_TagElement = java_TagElement
        self.java_TagElement321 = java_TagElement321 if java_TagElement321 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def java_TagElement321(self):
        return self.__java_TagElement321

    @java_TagElement321.setter
    def java_TagElement321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TagElement__java_TagElement321", None)
        self.__java_TagElement321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ASTNode322"):
                    opp_val = getattr(item, "java_ASTNode322", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ASTNode322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ASTNode322"):
                    opp_val = getattr(item, "java_ASTNode322", None)
                    
                    setattr(item, "java_ASTNode322", self)
                    

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

class java_Expression(ASTNode):

    pass
class java_NamespaceAccess(ASTNode):

    pass
class java_MethodRefParameter(ASTNode):

    def __init__(self, varargs: bool, name: str, java_MethodRefParameter: "java_MethodRef" = None, java_MethodRefParameter233: "java_TypeAccess" = None):
        self.varargs = varargs
        self.name = name
        self.java_MethodRefParameter = java_MethodRefParameter
        self.java_MethodRefParameter233 = java_MethodRefParameter233
        
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

class java_Statement(ASTNode):

    pass
class java_Comment(ASTNode):

    def __init__(self, prefixOfParent: bool, content: str, enclosedByParent: bool, java_Comment: "java_AbstractTypeDeclaration" = None, java_Comment18: "java_AbstractTypeDeclaration" = None, java_Comment41: "java_ASTNode" = None, java_Comment130: "java_CompilationUnit" = None):
        self.prefixOfParent = prefixOfParent
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.java_Comment = java_Comment
        self.java_Comment18 = java_Comment18
        self.java_Comment41 = java_Comment41
        self.java_Comment130 = java_Comment130
        
    @property
    def prefixOfParent(self) -> bool:
        return self.__prefixOfParent

    @prefixOfParent.setter
    def prefixOfParent(self, prefixOfParent: bool):
        self.__prefixOfParent = prefixOfParent

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def enclosedByParent(self) -> bool:
        return self.__enclosedByParent

    @enclosedByParent.setter
    def enclosedByParent(self, enclosedByParent: bool):
        self.__enclosedByParent = enclosedByParent

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
    def java_Comment41(self):
        return self.__java_Comment41

    @java_Comment41.setter
    def java_Comment41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment41", None)
        self.__java_Comment41 = value
        
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
    def java_Comment130(self):
        return self.__java_Comment130

    @java_Comment130.setter
    def java_Comment130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Comment__java_Comment130", None)
        self.__java_Comment130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit129"):
                opp_val = getattr(old_value, "java_CompilationUnit129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit129"):
                opp_val = getattr(value, "java_CompilationUnit129", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_NamedElement(ASTNode):

    def __init__(self, proxy: bool, name: str, NamedElement: "java_ImportDeclaration" = None, java_NamedElement: "java_MemberRef" = None, importedElement: set["java_ImportDeclaration"] = None):
        self.proxy = proxy
        self.name = name
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
                    

class java_AbstractVariablesContainer(ASTNode):

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
    def java_ImportDeclaration(self):
        return self.__java_ImportDeclaration

    @java_ImportDeclaration.setter
    def java_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportDeclaration__java_ImportDeclaration", None)
        self.__java_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit132"):
                opp_val = getattr(old_value, "java_CompilationUnit132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit132"):
                opp_val = getattr(value, "java_CompilationUnit132", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class NamedElement:

    pass
class java_Type(NamedElement):

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
    def java_VariableDeclaration(self):
        return self.__java_VariableDeclaration

    @java_VariableDeclaration.setter
    def java_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_VariableDeclaration__java_VariableDeclaration", None)
        self.__java_VariableDeclaration = value
        
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
                    

class java_ClassFile(NamedElement):

    def __init__(self, originalFilePath: str, java_ClassFile: "java_Archive" = None, java_ClassFile46: "java_ASTNode" = None, java_ClassFile104: "java_AbstractTypeDeclaration" = None, java_ClassFile107: "java_CompilationUnit" = None, java_ClassFile110: "java_Package" = None, java_ClassFile245: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_ClassFile = java_ClassFile
        self.java_ClassFile46 = java_ClassFile46
        self.java_ClassFile104 = java_ClassFile104
        self.java_ClassFile107 = java_ClassFile107
        self.java_ClassFile110 = java_ClassFile110
        self.java_ClassFile245 = java_ClassFile245
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_ClassFile107(self):
        return self.__java_ClassFile107

    @java_ClassFile107.setter
    def java_ClassFile107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile107", None)
        self.__java_ClassFile107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit108"):
                opp_val = getattr(old_value, "java_CompilationUnit108", None)
                if opp_val == self:
                    setattr(old_value, "java_CompilationUnit108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit108"):
                opp_val = getattr(value, "java_CompilationUnit108", None)
                setattr(value, "java_CompilationUnit108", self)

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
    def java_ClassFile104(self):
        return self.__java_ClassFile104

    @java_ClassFile104.setter
    def java_ClassFile104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile104", None)
        self.__java_ClassFile104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AbstractTypeDeclaration105"):
                opp_val = getattr(old_value, "java_AbstractTypeDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "java_AbstractTypeDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AbstractTypeDeclaration105"):
                opp_val = getattr(value, "java_AbstractTypeDeclaration105", None)
                setattr(value, "java_AbstractTypeDeclaration105", self)

    @property
    def java_ClassFile110(self):
        return self.__java_ClassFile110

    @java_ClassFile110.setter
    def java_ClassFile110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile110", None)
        self.__java_ClassFile110 = value
        
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
    def java_ClassFile46(self):
        return self.__java_ClassFile46

    @java_ClassFile46.setter
    def java_ClassFile46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ClassFile__java_ClassFile46", None)
        self.__java_ClassFile46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode45"):
                opp_val = getattr(old_value, "java_ASTNode45", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode45"):
                opp_val = getattr(value, "java_ASTNode45", None)
                setattr(value, "java_ASTNode45", self)

class java_Package(NamedElement):

    pass
class java_BodyDeclaration(NamedElement):

    pass
class java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java_CompilationUnit: "java_ASTNode" = None, java_CompilationUnit108: "java_ClassFile" = None, java_CompilationUnit129: set["java_Comment"] = None, java_CompilationUnit132: set["java_ImportDeclaration"] = None, java_CompilationUnit134: "java_Package" = None, java_CompilationUnit137: set["java_AbstractTypeDeclaration"] = None, java_CompilationUnit242: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_CompilationUnit = java_CompilationUnit
        self.java_CompilationUnit108 = java_CompilationUnit108
        self.java_CompilationUnit129 = java_CompilationUnit129 if java_CompilationUnit129 is not None else set()
        self.java_CompilationUnit132 = java_CompilationUnit132 if java_CompilationUnit132 is not None else set()
        self.java_CompilationUnit134 = java_CompilationUnit134
        self.java_CompilationUnit137 = java_CompilationUnit137 if java_CompilationUnit137 is not None else set()
        self.java_CompilationUnit242 = java_CompilationUnit242
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java_CompilationUnit134(self):
        return self.__java_CompilationUnit134

    @java_CompilationUnit134.setter
    def java_CompilationUnit134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit134", None)
        self.__java_CompilationUnit134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Package135"):
                opp_val = getattr(old_value, "java_Package135", None)
                if opp_val == self:
                    setattr(old_value, "java_Package135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Package135"):
                opp_val = getattr(value, "java_Package135", None)
                setattr(value, "java_Package135", self)

    @property
    def java_CompilationUnit137(self):
        return self.__java_CompilationUnit137

    @java_CompilationUnit137.setter
    def java_CompilationUnit137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit137", None)
        self.__java_CompilationUnit137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration138", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AbstractTypeDeclaration138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "java_AbstractTypeDeclaration138", None)
                    
                    setattr(item, "java_AbstractTypeDeclaration138", self)
                    

    @property
    def java_CompilationUnit132(self):
        return self.__java_CompilationUnit132

    @java_CompilationUnit132.setter
    def java_CompilationUnit132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit132", None)
        self.__java_CompilationUnit132 = value if value is not None else set()
        
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
    def java_CompilationUnit(self):
        return self.__java_CompilationUnit

    @java_CompilationUnit.setter
    def java_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit", None)
        self.__java_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ASTNode43"):
                opp_val = getattr(old_value, "java_ASTNode43", None)
                if opp_val == self:
                    setattr(old_value, "java_ASTNode43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ASTNode43"):
                opp_val = getattr(value, "java_ASTNode43", None)
                setattr(value, "java_ASTNode43", self)

    @property
    def java_CompilationUnit129(self):
        return self.__java_CompilationUnit129

    @java_CompilationUnit129.setter
    def java_CompilationUnit129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit129", None)
        self.__java_CompilationUnit129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Comment130"):
                    opp_val = getattr(item, "java_Comment130", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Comment130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Comment130"):
                    opp_val = getattr(item, "java_Comment130", None)
                    
                    setattr(item, "java_Comment130", self)
                    

    @property
    def java_CompilationUnit108(self):
        return self.__java_CompilationUnit108

    @java_CompilationUnit108.setter
    def java_CompilationUnit108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit108", None)
        self.__java_CompilationUnit108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ClassFile107"):
                opp_val = getattr(old_value, "java_ClassFile107", None)
                if opp_val == self:
                    setattr(old_value, "java_ClassFile107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ClassFile107"):
                opp_val = getattr(value, "java_ClassFile107", None)
                setattr(value, "java_ClassFile107", self)

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

class java_UnresolvedItem(NamedElement):

    pass
class java_LabeledStatement(NamedElement, Statement):

    pass
class java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, java_Archive: set["java_ClassFile"] = None, java_Archive34: "java_Manifest" = None, java_Archive248: "java_Model" = None):
        self.originalFilePath = originalFilePath
        self.java_Archive = java_Archive if java_Archive is not None else set()
        self.java_Archive34 = java_Archive34
        self.java_Archive248 = java_Archive248
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

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
    def java_Archive34(self):
        return self.__java_Archive34

    @java_Archive34.setter
    def java_Archive34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Archive__java_Archive34", None)
        self.__java_Archive34 = value
        
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
class java_TypeAccess(NamespaceAccess, Expression):

    pass
class java_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "java_AbstractMethodDeclaration" = None, SingleVariableDeclaration100: "java_CatchClause" = None, SingleVariableDeclaration152: "java_EnhancedForStatement" = None, SingleVariableDeclaration253: "java_Modifier" = None, singleVariableDeclaration: "java_Modifier" = None, java_SingleVariableDeclaration: "java_TypeAccess" = None, java_SingleVariableDeclaration298: set["java_Annotation"] = None, parameters: "java_AbstractMethodDeclaration" = None, exception: "java_CatchClause" = None, parameter: "java_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration100 = SingleVariableDeclaration100
        self.SingleVariableDeclaration152 = SingleVariableDeclaration152
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.singleVariableDeclaration = singleVariableDeclaration
        self.java_SingleVariableDeclaration = java_SingleVariableDeclaration
        self.java_SingleVariableDeclaration298 = java_SingleVariableDeclaration298 if java_SingleVariableDeclaration298 is not None else set()
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
    def SingleVariableDeclaration152(self):
        return self.__SingleVariableDeclaration152

    @SingleVariableDeclaration152.setter
    def SingleVariableDeclaration152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration152", None)
        self.__SingleVariableDeclaration152 = value
        
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
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMethodDeclaration301"):
                opp_val = getattr(old_value, "AbstractMethodDeclaration301", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMethodDeclaration301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMethodDeclaration301"):
                opp_val = getattr(value, "AbstractMethodDeclaration301", None)
                setattr(value, "AbstractMethodDeclaration301", self)

    @property
    def SingleVariableDeclaration100(self):
        return self.__SingleVariableDeclaration100

    @SingleVariableDeclaration100.setter
    def SingleVariableDeclaration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__SingleVariableDeclaration100", None)
        self.__SingleVariableDeclaration100 = value
        
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
    def java_SingleVariableDeclaration298(self):
        return self.__java_SingleVariableDeclaration298

    @java_SingleVariableDeclaration298.setter
    def java_SingleVariableDeclaration298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration298", None)
        self.__java_SingleVariableDeclaration298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Annotation299"):
                    opp_val = getattr(item, "java_Annotation299", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Annotation299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Annotation299"):
                    opp_val = getattr(item, "java_Annotation299", None)
                    
                    setattr(item, "java_Annotation299", self)
                    

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
            if hasattr(old_value, "Modifier294"):
                opp_val = getattr(old_value, "Modifier294", None)
                if opp_val == self:
                    setattr(old_value, "Modifier294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier294"):
                opp_val = getattr(value, "Modifier294", None)
                setattr(value, "Modifier294", self)

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
    def java_SingleVariableDeclaration(self):
        return self.__java_SingleVariableDeclaration

    @java_SingleVariableDeclaration.setter
    def java_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_SingleVariableDeclaration__java_SingleVariableDeclaration", None)
        self.__java_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeAccess296"):
                opp_val = getattr(old_value, "java_TypeAccess296", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeAccess296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeAccess296"):
                opp_val = getattr(value, "java_TypeAccess296", None)
                setattr(value, "java_TypeAccess296", self)

class java_Block(Statement):

    pass
class BodyDeclaration:

    pass
class java_Initializer(BodyDeclaration):

    pass
class java_AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class java_EnumConstantDeclaration(VariableDeclaration, BodyDeclaration):

    pass
class java_FieldDeclaration(AbstractVariablesContainer, BodyDeclaration):

    pass
class java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class java_AbstractMethodDeclaration(BodyDeclaration):

    pass
class java_MethodRef(ASTNode):

    pass
class java_TypeParameter(Type):

    pass