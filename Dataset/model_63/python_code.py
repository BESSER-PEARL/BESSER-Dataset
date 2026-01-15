from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class InfixExpressionKind(Enum):
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
    LESS = "LESS"
    GREATER = "GREATER"
    LESS_EQUALS = "LESS_EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    XOR = "XOR"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
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
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
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
class AnnotationTypeDeclaration:

    pass
class UnresolvedItem:

    pass
class Java_UnresolvedInterfaceDeclaration(UnresolvedItem, InterfaceDeclaration):

    pass
class Java_UnresolvedVariableDeclarationFragment(VariableDeclarationFragment, UnresolvedItem):

    pass
class Java_UnresolvedLabeledStatement(UnresolvedItem, LabeledStatement):

    pass
class Java_UnresolvedClassDeclaration(UnresolvedItem, ClassDeclaration):

    pass
class Java_UnresolvedAnnotationDeclaration(AnnotationTypeDeclaration, UnresolvedItem):

    pass
class Java_UnresolvedMethodDeclaration(UnresolvedItem, MethodDeclaration):

    pass
class Java_UnresolvedAnnotationTypeMemberDeclaration(UnresolvedItem, AnnotationTypeMemberDeclaration):

    pass
class Java_UnresolvedEnumDeclaration(UnresolvedItem, EnumDeclaration):

    pass
class Java_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class Java_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class Java_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class PrimitiveType:

    pass
class Java_PrimitiveTypeByte(PrimitiveType):

    pass
class Java_PrimitiveTypeInt(PrimitiveType):

    pass
class Java_PrimitiveTypeDouble(PrimitiveType):

    pass
class Java_PrimitiveTypeVoid(PrimitiveType):

    pass
class Java_PrimitiveTypeFloat(PrimitiveType):

    pass
class Java_PrimitiveTypeChar(PrimitiveType):

    pass
class Java_PrimitiveTypeLong(PrimitiveType):

    pass
class Java_PrimitiveTypeShort(PrimitiveType):

    pass
class Java_PrimitiveTypeBoolean(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class Java_PackageAccess(NamespaceAccess):

    pass
class Java_Model:

    def __init__(self, name: str, model: set["Java_Package"] = None, Java_Model: set["Java_Type"] = None, Java_Model239: set["Java_UnresolvedItem"] = None, Java_Model241: set["Java_CompilationUnit"] = None, Java_Model244: set["Java_ClassFile"] = None, Java_Model247: set["Java_Archive"] = None, Model: "Java_Package" = None):
        self.name = name
        self.model = model if model is not None else set()
        self.Java_Model = Java_Model if Java_Model is not None else set()
        self.Java_Model239 = Java_Model239 if Java_Model239 is not None else set()
        self.Java_Model241 = Java_Model241 if Java_Model241 is not None else set()
        self.Java_Model244 = Java_Model244 if Java_Model244 is not None else set()
        self.Java_Model247 = Java_Model247 if Java_Model247 is not None else set()
        self.Model = Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Java_Model244(self):
        return self.__Java_Model244

    @Java_Model244.setter
    def Java_Model244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Java_Model244", None)
        self.__Java_Model244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_ClassFile245"):
                    opp_val = getattr(item, "Java_ClassFile245", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_ClassFile245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_ClassFile245"):
                    opp_val = getattr(item, "Java_ClassFile245", None)
                    
                    setattr(item, "Java_ClassFile245", self)
                    

    @property
    def Java_Model241(self):
        return self.__Java_Model241

    @Java_Model241.setter
    def Java_Model241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Java_Model241", None)
        self.__Java_Model241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_CompilationUnit242"):
                    opp_val = getattr(item, "Java_CompilationUnit242", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_CompilationUnit242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_CompilationUnit242"):
                    opp_val = getattr(item, "Java_CompilationUnit242", None)
                    
                    setattr(item, "Java_CompilationUnit242", self)
                    

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Model", None)
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

    @property
    def Java_Model239(self):
        return self.__Java_Model239

    @Java_Model239.setter
    def Java_Model239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Java_Model239", None)
        self.__Java_Model239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_UnresolvedItem"):
                    opp_val = getattr(item, "Java_UnresolvedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_UnresolvedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_UnresolvedItem"):
                    opp_val = getattr(item, "Java_UnresolvedItem", None)
                    
                    setattr(item, "Java_UnresolvedItem", self)
                    

    @property
    def Java_Model(self):
        return self.__Java_Model

    @Java_Model.setter
    def Java_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Java_Model", None)
        self.__Java_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Type"):
                    opp_val = getattr(item, "Java_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Type"):
                    opp_val = getattr(item, "Java_Type", None)
                    
                    setattr(item, "Java_Type", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__model", None)
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
    def Java_Model247(self):
        return self.__Java_Model247

    @Java_Model247.setter
    def Java_Model247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Model__Java_Model247", None)
        self.__Java_Model247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Archive248"):
                    opp_val = getattr(item, "Java_Archive248", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Archive248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Archive248"):
                    opp_val = getattr(item, "Java_Archive248", None)
                    
                    setattr(item, "Java_Archive248", self)
                    

class Java_ManifestEntry:

    def __init__(self, name: str, Java_ManifestEntry211: set["Java_ManifestAttribute"] = None, Java_ManifestEntry: "Java_Manifest" = None):
        self.name = name
        self.Java_ManifestEntry211 = Java_ManifestEntry211 if Java_ManifestEntry211 is not None else set()
        self.Java_ManifestEntry = Java_ManifestEntry
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Java_ManifestEntry(self):
        return self.__Java_ManifestEntry

    @Java_ManifestEntry.setter
    def Java_ManifestEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ManifestEntry__Java_ManifestEntry", None)
        self.__Java_ManifestEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Manifest209"):
                opp_val = getattr(old_value, "Java_Manifest209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Manifest209"):
                opp_val = getattr(value, "Java_Manifest209", None)
                if opp_val is None:
                    setattr(value, "Java_Manifest209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_ManifestEntry211(self):
        return self.__Java_ManifestEntry211

    @Java_ManifestEntry211.setter
    def Java_ManifestEntry211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ManifestEntry__Java_ManifestEntry211", None)
        self.__Java_ManifestEntry211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_ManifestAttribute212"):
                    opp_val = getattr(item, "Java_ManifestAttribute212", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_ManifestAttribute212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_ManifestAttribute212"):
                    opp_val = getattr(item, "Java_ManifestAttribute212", None)
                    
                    setattr(item, "Java_ManifestAttribute212", self)
                    

class Java_ManifestAttribute:

    def __init__(self, value: str, key: str, Java_ManifestAttribute212: "Java_ManifestEntry" = None, Java_ManifestAttribute: "Java_Manifest" = None):
        self.value = value
        self.key = key
        self.Java_ManifestAttribute212 = Java_ManifestAttribute212
        self.Java_ManifestAttribute = Java_ManifestAttribute
        
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
    def Java_ManifestAttribute(self):
        return self.__Java_ManifestAttribute

    @Java_ManifestAttribute.setter
    def Java_ManifestAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ManifestAttribute__Java_ManifestAttribute", None)
        self.__Java_ManifestAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Manifest207"):
                opp_val = getattr(old_value, "Java_Manifest207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Manifest207"):
                opp_val = getattr(value, "Java_Manifest207", None)
                if opp_val is None:
                    setattr(value, "Java_Manifest207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_ManifestAttribute212(self):
        return self.__Java_ManifestAttribute212

    @Java_ManifestAttribute212.setter
    def Java_ManifestAttribute212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ManifestAttribute__Java_ManifestAttribute212", None)
        self.__Java_ManifestAttribute212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_ManifestEntry211"):
                opp_val = getattr(old_value, "Java_ManifestEntry211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_ManifestEntry211"):
                opp_val = getattr(value, "Java_ManifestEntry211", None)
                if opp_val is None:
                    setattr(value, "Java_ManifestEntry211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractVariablesContainer:

    pass
class VariableDeclaration:

    pass
class TypeDeclaration:

    pass
class Java_InterfaceDeclaration(TypeDeclaration):

    pass
class Java_ClassDeclaration(TypeDeclaration):

    pass
class AbstractMethodDeclaration:

    pass
class Java_MethodDeclaration(AbstractMethodDeclaration):

    def __init__(self, extraArrayDimensions: int, Java_MethodDeclaration: "Java_TypeAccess" = None, MethodDeclaration: "Java_MethodDeclaration" = None, redefinitions: "Java_MethodDeclaration" = None, MethodDeclaration223: "Java_MethodDeclaration" = None, redefinedMethodDeclaration: set["Java_MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.Java_MethodDeclaration = Java_MethodDeclaration
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
    def Java_MethodDeclaration(self):
        return self.__Java_MethodDeclaration

    @Java_MethodDeclaration.setter
    def Java_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodDeclaration__Java_MethodDeclaration", None)
        self.__Java_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_TypeAccess218"):
                opp_val = getattr(old_value, "Java_TypeAccess218", None)
                if opp_val == self:
                    setattr(old_value, "Java_TypeAccess218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_TypeAccess218"):
                opp_val = getattr(value, "Java_TypeAccess218", None)
                setattr(value, "Java_TypeAccess218", self)

    @property
    def redefinedMethodDeclaration(self):
        return self.__redefinedMethodDeclaration

    @redefinedMethodDeclaration.setter
    def redefinedMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodDeclaration__redefinedMethodDeclaration", None)
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
    def redefinitions(self):
        return self.__redefinitions

    @redefinitions.setter
    def redefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodDeclaration__redefinitions", None)
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
    def MethodDeclaration(self):
        return self.__MethodDeclaration

    @MethodDeclaration.setter
    def MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodDeclaration__MethodDeclaration", None)
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
    def MethodDeclaration223(self):
        return self.__MethodDeclaration223

    @MethodDeclaration223.setter
    def MethodDeclaration223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodDeclaration__MethodDeclaration223", None)
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

class Java_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class Java_SuperMethodInvocation(AbstractMethodInvocation, AbstractTypeQualifiedExpression):

    pass
class Comment:

    pass
class Java_LineComment(Comment):

    pass
class Java_Javadoc(Comment):

    pass
class Java_BlockComment(Comment):

    pass
class Java_ASTNode(ABC):

    pass
class AbstractTypeDeclaration:

    pass
class Java_TypeDeclaration(AbstractTypeDeclaration):

    pass
class Java_EnumDeclaration(AbstractTypeDeclaration):

    pass
class Java_UnresolvedTypeDeclaration(AbstractTypeDeclaration, UnresolvedItem):

    pass
class Java_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class NamedElement:

    pass
class Java_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, Java_CompilationUnit: "Java_ASTNode" = None, Java_CompilationUnit108: "Java_ClassFile" = None, Java_CompilationUnit129: set["Java_Comment"] = None, Java_CompilationUnit132: set["Java_ImportDeclaration"] = None, Java_CompilationUnit134: "Java_Package" = None, Java_CompilationUnit137: set["Java_AbstractTypeDeclaration"] = None, Java_CompilationUnit242: "Java_Model" = None):
        self.originalFilePath = originalFilePath
        self.Java_CompilationUnit = Java_CompilationUnit
        self.Java_CompilationUnit108 = Java_CompilationUnit108
        self.Java_CompilationUnit129 = Java_CompilationUnit129 if Java_CompilationUnit129 is not None else set()
        self.Java_CompilationUnit132 = Java_CompilationUnit132 if Java_CompilationUnit132 is not None else set()
        self.Java_CompilationUnit134 = Java_CompilationUnit134
        self.Java_CompilationUnit137 = Java_CompilationUnit137 if Java_CompilationUnit137 is not None else set()
        self.Java_CompilationUnit242 = Java_CompilationUnit242
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def Java_CompilationUnit108(self):
        return self.__Java_CompilationUnit108

    @Java_CompilationUnit108.setter
    def Java_CompilationUnit108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit108", None)
        self.__Java_CompilationUnit108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_ClassFile107"):
                opp_val = getattr(old_value, "Java_ClassFile107", None)
                if opp_val == self:
                    setattr(old_value, "Java_ClassFile107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_ClassFile107"):
                opp_val = getattr(value, "Java_ClassFile107", None)
                setattr(value, "Java_ClassFile107", self)

    @property
    def Java_CompilationUnit242(self):
        return self.__Java_CompilationUnit242

    @Java_CompilationUnit242.setter
    def Java_CompilationUnit242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit242", None)
        self.__Java_CompilationUnit242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Model241"):
                opp_val = getattr(old_value, "Java_Model241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Model241"):
                opp_val = getattr(value, "Java_Model241", None)
                if opp_val is None:
                    setattr(value, "Java_Model241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_CompilationUnit137(self):
        return self.__Java_CompilationUnit137

    @Java_CompilationUnit137.setter
    def Java_CompilationUnit137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit137", None)
        self.__Java_CompilationUnit137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "Java_AbstractTypeDeclaration138", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_AbstractTypeDeclaration138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "Java_AbstractTypeDeclaration138", None)
                    
                    setattr(item, "Java_AbstractTypeDeclaration138", self)
                    

    @property
    def Java_CompilationUnit134(self):
        return self.__Java_CompilationUnit134

    @Java_CompilationUnit134.setter
    def Java_CompilationUnit134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit134", None)
        self.__Java_CompilationUnit134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Package135"):
                opp_val = getattr(old_value, "Java_Package135", None)
                if opp_val == self:
                    setattr(old_value, "Java_Package135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Package135"):
                opp_val = getattr(value, "Java_Package135", None)
                setattr(value, "Java_Package135", self)

    @property
    def Java_CompilationUnit129(self):
        return self.__Java_CompilationUnit129

    @Java_CompilationUnit129.setter
    def Java_CompilationUnit129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit129", None)
        self.__Java_CompilationUnit129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Comment130"):
                    opp_val = getattr(item, "Java_Comment130", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Comment130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Comment130"):
                    opp_val = getattr(item, "Java_Comment130", None)
                    
                    setattr(item, "Java_Comment130", self)
                    

    @property
    def Java_CompilationUnit(self):
        return self.__Java_CompilationUnit

    @Java_CompilationUnit.setter
    def Java_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit", None)
        self.__Java_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_ASTNode43"):
                opp_val = getattr(old_value, "Java_ASTNode43", None)
                if opp_val == self:
                    setattr(old_value, "Java_ASTNode43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_ASTNode43"):
                opp_val = getattr(value, "Java_ASTNode43", None)
                setattr(value, "Java_ASTNode43", self)

    @property
    def Java_CompilationUnit132(self):
        return self.__Java_CompilationUnit132

    @Java_CompilationUnit132.setter
    def Java_CompilationUnit132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_CompilationUnit__Java_CompilationUnit132", None)
        self.__Java_CompilationUnit132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_ImportDeclaration"):
                    opp_val = getattr(item, "Java_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_ImportDeclaration"):
                    opp_val = getattr(item, "Java_ImportDeclaration", None)
                    
                    setattr(item, "Java_ImportDeclaration", self)
                    

class Java_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, VariableDeclaration: "Java_SingleVariableAccess" = None, variable: set["Java_SingleVariableAccess"] = None, Java_VariableDeclaration: "Java_Expression" = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclaration = VariableDeclaration
        self.variable = variable if variable is not None else set()
        self.Java_VariableDeclaration = Java_VariableDeclaration
        
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
        old_value = getattr(self, f"_Java_VariableDeclaration__variable", None)
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
    def Java_VariableDeclaration(self):
        return self.__Java_VariableDeclaration

    @Java_VariableDeclaration.setter
    def Java_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_VariableDeclaration__Java_VariableDeclaration", None)
        self.__Java_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression352"):
                opp_val = getattr(old_value, "Java_Expression352", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression352"):
                opp_val = getattr(value, "Java_Expression352", None)
                setattr(value, "Java_Expression352", self)

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_VariableDeclaration__VariableDeclaration", None)
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

class Java_UnresolvedItem(NamedElement):

    pass
class Java_Type(NamedElement):

    pass
class Java_Archive(NamedElement):

    def __init__(self, originalFilePath: str, Java_Archive: set["Java_ClassFile"] = None, Java_Archive34: "Java_Manifest" = None, Java_Archive248: "Java_Model" = None):
        self.originalFilePath = originalFilePath
        self.Java_Archive = Java_Archive if Java_Archive is not None else set()
        self.Java_Archive34 = Java_Archive34
        self.Java_Archive248 = Java_Archive248
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def Java_Archive(self):
        return self.__Java_Archive

    @Java_Archive.setter
    def Java_Archive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Archive__Java_Archive", None)
        self.__Java_Archive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_ClassFile"):
                    opp_val = getattr(item, "Java_ClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_ClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_ClassFile"):
                    opp_val = getattr(item, "Java_ClassFile", None)
                    
                    setattr(item, "Java_ClassFile", self)
                    

    @property
    def Java_Archive34(self):
        return self.__Java_Archive34

    @Java_Archive34.setter
    def Java_Archive34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Archive__Java_Archive34", None)
        self.__Java_Archive34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Manifest"):
                opp_val = getattr(old_value, "Java_Manifest", None)
                if opp_val == self:
                    setattr(old_value, "Java_Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Manifest"):
                opp_val = getattr(value, "Java_Manifest", None)
                setattr(value, "Java_Manifest", self)

    @property
    def Java_Archive248(self):
        return self.__Java_Archive248

    @Java_Archive248.setter
    def Java_Archive248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Archive__Java_Archive248", None)
        self.__Java_Archive248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Model247"):
                opp_val = getattr(old_value, "Java_Model247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Model247"):
                opp_val = getattr(value, "Java_Model247", None)
                if opp_val is None:
                    setattr(value, "Java_Model247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java_AnnotationMemberValuePair(NamedElement):

    pass
class Java_VariableDeclarationFragment(VariableDeclaration):

    pass
class Statement:

    pass
class Java_VariableDeclarationStatement(AbstractVariablesContainer, Statement):

    def __init__(self, extraArrayDimensions: int, VariableDeclarationStatement: "Java_Modifier" = None, variableDeclarationStatement: "Java_Modifier" = None, Java_VariableDeclarationStatement: set["Java_Annotation"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclarationStatement = VariableDeclarationStatement
        self.variableDeclarationStatement = variableDeclarationStatement
        self.Java_VariableDeclarationStatement = Java_VariableDeclarationStatement if Java_VariableDeclarationStatement is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def VariableDeclarationStatement(self):
        return self.__VariableDeclarationStatement

    @VariableDeclarationStatement.setter
    def VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_VariableDeclarationStatement__VariableDeclarationStatement", None)
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
        old_value = getattr(self, f"_Java_VariableDeclarationStatement__variableDeclarationStatement", None)
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

    @property
    def Java_VariableDeclarationStatement(self):
        return self.__Java_VariableDeclarationStatement

    @Java_VariableDeclarationStatement.setter
    def Java_VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_VariableDeclarationStatement__Java_VariableDeclarationStatement", None)
        self.__Java_VariableDeclarationStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Annotation362"):
                    opp_val = getattr(item, "Java_Annotation362", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Annotation362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Annotation362"):
                    opp_val = getattr(item, "Java_Annotation362", None)
                    
                    setattr(item, "Java_Annotation362", self)
                    

class Java_SwitchStatement(Statement):

    pass
class Java_ContinueStatement(Statement):

    pass
class Java_SwitchCase(Statement):

    def __init__(self, default: bool, Java_SwitchCase: "Java_Expression" = None):
        self.default = default
        self.Java_SwitchCase = Java_SwitchCase
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def Java_SwitchCase(self):
        return self.__Java_SwitchCase

    @Java_SwitchCase.setter
    def Java_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SwitchCase__Java_SwitchCase", None)
        self.__Java_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression309"):
                opp_val = getattr(old_value, "Java_Expression309", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression309"):
                opp_val = getattr(value, "Java_Expression309", None)
                setattr(value, "Java_Expression309", self)

class Java_WhileStatement(Statement):

    pass
class Java_ThrowStatement(Statement):

    pass
class Java_DoStatement(Statement):

    pass
class Java_ExpressionStatement(Statement):

    pass
class Java_IfStatement(Statement):

    pass
class Java_TypeDeclarationStatement(Statement):

    pass
class Java_EnhancedForStatement(Statement):

    pass
class Java_BreakStatement(Statement):

    pass
class Java_EmptyStatement(Statement):

    pass
class Java_SynchronizedStatement(Statement):

    pass
class Java_ConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class Java_ForStatement(Statement):

    pass
class Java_TryStatement(Statement):

    pass
class Java_LabeledStatement(Statement, NamedElement):

    pass
class Java_CatchClause(Statement):

    pass
class Java_SuperConstructorInvocation(AbstractMethodInvocation, Statement):

    pass
class Java_ReturnStatement(Statement):

    pass
class Java_AssertStatement(Statement):

    pass
class Java_Manifest:

    pass
class Java_ClassFile(NamedElement):

    def __init__(self, originalFilePath: str, Java_ClassFile: "Java_Archive" = None, Java_ClassFile46: "Java_ASTNode" = None, Java_ClassFile104: "Java_AbstractTypeDeclaration" = None, Java_ClassFile107: "Java_CompilationUnit" = None, Java_ClassFile110: "Java_Package" = None, Java_ClassFile245: "Java_Model" = None):
        self.originalFilePath = originalFilePath
        self.Java_ClassFile = Java_ClassFile
        self.Java_ClassFile46 = Java_ClassFile46
        self.Java_ClassFile104 = Java_ClassFile104
        self.Java_ClassFile107 = Java_ClassFile107
        self.Java_ClassFile110 = Java_ClassFile110
        self.Java_ClassFile245 = Java_ClassFile245
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def Java_ClassFile110(self):
        return self.__Java_ClassFile110

    @Java_ClassFile110.setter
    def Java_ClassFile110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile110", None)
        self.__Java_ClassFile110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Package"):
                opp_val = getattr(old_value, "Java_Package", None)
                if opp_val == self:
                    setattr(old_value, "Java_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Package"):
                opp_val = getattr(value, "Java_Package", None)
                setattr(value, "Java_Package", self)

    @property
    def Java_ClassFile107(self):
        return self.__Java_ClassFile107

    @Java_ClassFile107.setter
    def Java_ClassFile107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile107", None)
        self.__Java_ClassFile107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_CompilationUnit108"):
                opp_val = getattr(old_value, "Java_CompilationUnit108", None)
                if opp_val == self:
                    setattr(old_value, "Java_CompilationUnit108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_CompilationUnit108"):
                opp_val = getattr(value, "Java_CompilationUnit108", None)
                setattr(value, "Java_CompilationUnit108", self)

    @property
    def Java_ClassFile(self):
        return self.__Java_ClassFile

    @Java_ClassFile.setter
    def Java_ClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile", None)
        self.__Java_ClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Archive"):
                opp_val = getattr(old_value, "Java_Archive", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Archive"):
                opp_val = getattr(value, "Java_Archive", None)
                if opp_val is None:
                    setattr(value, "Java_Archive", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_ClassFile46(self):
        return self.__Java_ClassFile46

    @Java_ClassFile46.setter
    def Java_ClassFile46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile46", None)
        self.__Java_ClassFile46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_ASTNode45"):
                opp_val = getattr(old_value, "Java_ASTNode45", None)
                if opp_val == self:
                    setattr(old_value, "Java_ASTNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_ASTNode45"):
                opp_val = getattr(value, "Java_ASTNode45", None)
                setattr(value, "Java_ASTNode45", self)

    @property
    def Java_ClassFile104(self):
        return self.__Java_ClassFile104

    @Java_ClassFile104.setter
    def Java_ClassFile104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile104", None)
        self.__Java_ClassFile104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_AbstractTypeDeclaration105"):
                opp_val = getattr(old_value, "Java_AbstractTypeDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "Java_AbstractTypeDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_AbstractTypeDeclaration105"):
                opp_val = getattr(value, "Java_AbstractTypeDeclaration105", None)
                setattr(value, "Java_AbstractTypeDeclaration105", self)

    @property
    def Java_ClassFile245(self):
        return self.__Java_ClassFile245

    @Java_ClassFile245.setter
    def Java_ClassFile245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ClassFile__Java_ClassFile245", None)
        self.__Java_ClassFile245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Model244"):
                opp_val = getattr(old_value, "Java_Model244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Model244"):
                opp_val = getattr(value, "Java_Model244", None)
                if opp_val is None:
                    setattr(value, "Java_Model244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java_BodyDeclaration(NamedElement):

    pass
class Type:

    pass
class Java_ArrayType(Type):

    def __init__(self, dimensions: int, Java_ArrayType: "Java_TypeAccess" = None):
        self.dimensions = dimensions
        self.Java_ArrayType = Java_ArrayType
        
    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions

    @property
    def Java_ArrayType(self):
        return self.__Java_ArrayType

    @Java_ArrayType.setter
    def Java_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ArrayType__Java_ArrayType", None)
        self.__Java_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_TypeAccess79"):
                opp_val = getattr(old_value, "Java_TypeAccess79", None)
                if opp_val == self:
                    setattr(old_value, "Java_TypeAccess79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_TypeAccess79"):
                opp_val = getattr(value, "Java_TypeAccess79", None)
                setattr(value, "Java_TypeAccess79", self)

class Java_UnresolvedType(Type, UnresolvedItem):

    pass
class Java_ParameterizedType(Type):

    pass
class Java_WildCardType(Type):

    def __init__(self, upperBound: bool, Java_WildCardType: "Java_TypeAccess" = None):
        self.upperBound = upperBound
        self.Java_WildCardType = Java_WildCardType
        
    @property
    def upperBound(self) -> bool:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: bool):
        self.__upperBound = upperBound

    @property
    def Java_WildCardType(self):
        return self.__Java_WildCardType

    @Java_WildCardType.setter
    def Java_WildCardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_WildCardType__Java_WildCardType", None)
        self.__Java_WildCardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_TypeAccess364"):
                opp_val = getattr(old_value, "Java_TypeAccess364", None)
                if opp_val == self:
                    setattr(old_value, "Java_TypeAccess364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_TypeAccess364"):
                opp_val = getattr(value, "Java_TypeAccess364", None)
                setattr(value, "Java_TypeAccess364", self)

class Java_PrimitiveType(Type):

    pass
class ASTNode:

    pass
class Java_MemberRef(ASTNode):

    pass
class Java_TagElement(ASTNode):

    def __init__(self, tagName: str, Java_TagElement: "Java_Javadoc" = None, Java_TagElement321: set["Java_ASTNode"] = None):
        self.tagName = tagName
        self.Java_TagElement = Java_TagElement
        self.Java_TagElement321 = Java_TagElement321 if Java_TagElement321 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def Java_TagElement321(self):
        return self.__Java_TagElement321

    @Java_TagElement321.setter
    def Java_TagElement321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_TagElement__Java_TagElement321", None)
        self.__Java_TagElement321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_ASTNode322"):
                    opp_val = getattr(item, "Java_ASTNode322", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_ASTNode322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_ASTNode322"):
                    opp_val = getattr(item, "Java_ASTNode322", None)
                    
                    setattr(item, "Java_ASTNode322", self)
                    

    @property
    def Java_TagElement(self):
        return self.__Java_TagElement

    @Java_TagElement.setter
    def Java_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_TagElement__Java_TagElement", None)
        self.__Java_TagElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Javadoc"):
                opp_val = getattr(old_value, "Java_Javadoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Javadoc"):
                opp_val = getattr(value, "Java_Javadoc", None)
                if opp_val is None:
                    setattr(value, "Java_Javadoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "Java_BodyDeclaration" = None, modifier252: "Java_SingleVariableDeclaration" = None, modifier255: "Java_VariableDeclarationStatement" = None, modifier: "Java_BodyDeclaration" = None, modifier257: "Java_VariableDeclarationExpression" = None, Modifier294: "Java_SingleVariableDeclaration" = None, Modifier355: "Java_VariableDeclarationExpression" = None, Modifier360: "Java_VariableDeclarationStatement" = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.native = native
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.Modifier = Modifier
        self.modifier252 = modifier252
        self.modifier255 = modifier255
        self.modifier = modifier
        self.modifier257 = modifier257
        self.Modifier294 = Modifier294
        self.Modifier355 = Modifier355
        self.Modifier360 = Modifier360
        
    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

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
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def modifier255(self):
        return self.__modifier255

    @modifier255.setter
    def modifier255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__modifier255", None)
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
    def Modifier355(self):
        return self.__Modifier355

    @Modifier355.setter
    def Modifier355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__Modifier355", None)
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
    def modifier252(self):
        return self.__modifier252

    @modifier252.setter
    def modifier252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__modifier252", None)
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
        old_value = getattr(self, f"_Java_Modifier__Modifier", None)
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
    def Modifier294(self):
        return self.__Modifier294

    @Modifier294.setter
    def Modifier294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__Modifier294", None)
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
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__modifier", None)
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
    def Modifier360(self):
        return self.__Modifier360

    @Modifier360.setter
    def Modifier360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__Modifier360", None)
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
    def modifier257(self):
        return self.__modifier257

    @modifier257.setter
    def modifier257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Modifier__modifier257", None)
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

class Java_AnonymousClassDeclaration(ASTNode):

    pass
class Java_Expression(ASTNode):

    pass
class Java_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, NamedElement: "Java_ImportDeclaration" = None, Java_NamedElement: "Java_MemberRef" = None, importedElement: set["Java_ImportDeclaration"] = None):
        self.name = name
        self.proxy = proxy
        self.NamedElement = NamedElement
        self.Java_NamedElement = Java_NamedElement
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
        old_value = getattr(self, f"_Java_NamedElement__importedElement", None)
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
    def Java_NamedElement(self):
        return self.__Java_NamedElement

    @Java_NamedElement.setter
    def Java_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_NamedElement__Java_NamedElement", None)
        self.__Java_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_MemberRef"):
                opp_val = getattr(old_value, "Java_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "Java_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_MemberRef"):
                opp_val = getattr(value, "Java_MemberRef", None)
                setattr(value, "Java_MemberRef", self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_NamedElement__NamedElement", None)
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

class Java_MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: bool, Java_MethodRefParameter: "Java_MethodRef" = None, Java_MethodRefParameter233: "Java_TypeAccess" = None):
        self.name = name
        self.varargs = varargs
        self.Java_MethodRefParameter = Java_MethodRefParameter
        self.Java_MethodRefParameter233 = Java_MethodRefParameter233
        
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
    def Java_MethodRefParameter(self):
        return self.__Java_MethodRefParameter

    @Java_MethodRefParameter.setter
    def Java_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodRefParameter__Java_MethodRefParameter", None)
        self.__Java_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_MethodRef231"):
                opp_val = getattr(old_value, "Java_MethodRef231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_MethodRef231"):
                opp_val = getattr(value, "Java_MethodRef231", None)
                if opp_val is None:
                    setattr(value, "Java_MethodRef231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_MethodRefParameter233(self):
        return self.__Java_MethodRefParameter233

    @Java_MethodRefParameter233.setter
    def Java_MethodRefParameter233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodRefParameter__Java_MethodRefParameter233", None)
        self.__Java_MethodRefParameter233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_TypeAccess234"):
                opp_val = getattr(old_value, "Java_TypeAccess234", None)
                if opp_val == self:
                    setattr(old_value, "Java_TypeAccess234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_TypeAccess234"):
                opp_val = getattr(value, "Java_TypeAccess234", None)
                setattr(value, "Java_TypeAccess234", self)

class Java_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, Java_ImportDeclaration: "Java_CompilationUnit" = None, usagesInImports: "Java_NamedElement" = None, ImportDeclaration: "Java_NamedElement" = None):
        self.static = static
        self.Java_ImportDeclaration = Java_ImportDeclaration
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
        old_value = getattr(self, f"_Java_ImportDeclaration__usagesInImports", None)
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
        old_value = getattr(self, f"_Java_ImportDeclaration__ImportDeclaration", None)
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

    @property
    def Java_ImportDeclaration(self):
        return self.__Java_ImportDeclaration

    @Java_ImportDeclaration.setter
    def Java_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_ImportDeclaration__Java_ImportDeclaration", None)
        self.__Java_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_CompilationUnit132"):
                opp_val = getattr(old_value, "Java_CompilationUnit132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_CompilationUnit132"):
                opp_val = getattr(value, "Java_CompilationUnit132", None)
                if opp_val is None:
                    setattr(value, "Java_CompilationUnit132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Java_Statement(ASTNode):

    pass
class Java_Comment(ASTNode):

    def __init__(self, content: str, enclosedByParent: bool, prefixOfParent: bool, Java_Comment18: "Java_AbstractTypeDeclaration" = None, Java_Comment: "Java_AbstractTypeDeclaration" = None, Java_Comment41: "Java_ASTNode" = None, Java_Comment130: "Java_CompilationUnit" = None):
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.Java_Comment18 = Java_Comment18
        self.Java_Comment = Java_Comment
        self.Java_Comment41 = Java_Comment41
        self.Java_Comment130 = Java_Comment130
        
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
    def Java_Comment41(self):
        return self.__Java_Comment41

    @Java_Comment41.setter
    def Java_Comment41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Comment__Java_Comment41", None)
        self.__Java_Comment41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_ASTNode"):
                opp_val = getattr(old_value, "Java_ASTNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_ASTNode"):
                opp_val = getattr(value, "Java_ASTNode", None)
                if opp_val is None:
                    setattr(value, "Java_ASTNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_Comment130(self):
        return self.__Java_Comment130

    @Java_Comment130.setter
    def Java_Comment130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Comment__Java_Comment130", None)
        self.__Java_Comment130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_CompilationUnit129"):
                opp_val = getattr(old_value, "Java_CompilationUnit129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_CompilationUnit129"):
                opp_val = getattr(value, "Java_CompilationUnit129", None)
                if opp_val is None:
                    setattr(value, "Java_CompilationUnit129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_Comment18(self):
        return self.__Java_Comment18

    @Java_Comment18.setter
    def Java_Comment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Comment__Java_Comment18", None)
        self.__Java_Comment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_AbstractTypeDeclaration17"):
                opp_val = getattr(old_value, "Java_AbstractTypeDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_AbstractTypeDeclaration17"):
                opp_val = getattr(value, "Java_AbstractTypeDeclaration17", None)
                if opp_val is None:
                    setattr(value, "Java_AbstractTypeDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java_Comment(self):
        return self.__Java_Comment

    @Java_Comment.setter
    def Java_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Comment__Java_Comment", None)
        self.__Java_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "Java_AbstractTypeDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_AbstractTypeDeclaration"):
                opp_val = getattr(value, "Java_AbstractTypeDeclaration", None)
                if opp_val is None:
                    setattr(value, "Java_AbstractTypeDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java_AbstractVariablesContainer(ASTNode):

    pass
class Java_NamespaceAccess(ASTNode):

    pass
class Expression:

    pass
class Java_PostfixExpression(Expression):

    def __init__(self, operator: str, Java_PostfixExpression: "Java_Expression" = None):
        self.operator = operator
        self.Java_PostfixExpression = Java_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java_PostfixExpression(self):
        return self.__Java_PostfixExpression

    @Java_PostfixExpression.setter
    def Java_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_PostfixExpression__Java_PostfixExpression", None)
        self.__Java_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression284"):
                opp_val = getattr(old_value, "Java_Expression284", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression284"):
                opp_val = getattr(value, "Java_Expression284", None)
                setattr(value, "Java_Expression284", self)

class Java_ConditionalExpression(Expression):

    pass
class Java_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class Java_SingleVariableAccess(Expression):

    pass
class Java_Annotation(Expression):

    pass
class Java_ArrayInitializer(Expression):

    pass
class Java_Assignment(Expression):

    def __init__(self, operator: str, Java_Assignment: "Java_Expression" = None, Java_Assignment83: "Java_Expression" = None):
        self.operator = operator
        self.Java_Assignment = Java_Assignment
        self.Java_Assignment83 = Java_Assignment83
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java_Assignment83(self):
        return self.__Java_Assignment83

    @Java_Assignment83.setter
    def Java_Assignment83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Assignment__Java_Assignment83", None)
        self.__Java_Assignment83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression84"):
                opp_val = getattr(old_value, "Java_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression84"):
                opp_val = getattr(value, "Java_Expression84", None)
                setattr(value, "Java_Expression84", self)

    @property
    def Java_Assignment(self):
        return self.__Java_Assignment

    @Java_Assignment.setter
    def Java_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Assignment__Java_Assignment", None)
        self.__Java_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression81"):
                opp_val = getattr(old_value, "Java_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression81"):
                opp_val = getattr(value, "Java_Expression81", None)
                setattr(value, "Java_Expression81", self)

class Java_InstanceofExpression(Expression):

    pass
class Java_MethodInvocation(AbstractMethodInvocation, Expression):

    pass
class Java_VariableDeclarationExpression(AbstractVariablesContainer, Expression):

    pass
class Java_ClassInstanceCreation(AbstractMethodInvocation, Expression):

    pass
class Java_InfixExpression(Expression):

    def __init__(self, operator: str, Java_InfixExpression: "Java_Expression" = None, Java_InfixExpression188: "Java_Expression" = None, Java_InfixExpression191: set["Java_Expression"] = None):
        self.operator = operator
        self.Java_InfixExpression = Java_InfixExpression
        self.Java_InfixExpression188 = Java_InfixExpression188
        self.Java_InfixExpression191 = Java_InfixExpression191 if Java_InfixExpression191 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java_InfixExpression188(self):
        return self.__Java_InfixExpression188

    @Java_InfixExpression188.setter
    def Java_InfixExpression188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_InfixExpression__Java_InfixExpression188", None)
        self.__Java_InfixExpression188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression189"):
                opp_val = getattr(old_value, "Java_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression189"):
                opp_val = getattr(value, "Java_Expression189", None)
                setattr(value, "Java_Expression189", self)

    @property
    def Java_InfixExpression(self):
        return self.__Java_InfixExpression

    @Java_InfixExpression.setter
    def Java_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_InfixExpression__Java_InfixExpression", None)
        self.__Java_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression186"):
                opp_val = getattr(old_value, "Java_Expression186", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression186"):
                opp_val = getattr(value, "Java_Expression186", None)
                setattr(value, "Java_Expression186", self)

    @property
    def Java_InfixExpression191(self):
        return self.__Java_InfixExpression191

    @Java_InfixExpression191.setter
    def Java_InfixExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_InfixExpression__Java_InfixExpression191", None)
        self.__Java_InfixExpression191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Expression192"):
                    opp_val = getattr(item, "Java_Expression192", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Expression192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Expression192"):
                    opp_val = getattr(item, "Java_Expression192", None)
                    
                    setattr(item, "Java_Expression192", self)
                    

class Java_UnresolvedItemAccess(Expression, NamespaceAccess):

    pass
class Java_PrefixExpression(Expression):

    def __init__(self, operator: str, Java_PrefixExpression: "Java_Expression" = None):
        self.operator = operator
        self.Java_PrefixExpression = Java_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java_PrefixExpression(self):
        return self.__Java_PrefixExpression

    @Java_PrefixExpression.setter
    def Java_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_PrefixExpression__Java_PrefixExpression", None)
        self.__Java_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_Expression286"):
                opp_val = getattr(old_value, "Java_Expression286", None)
                if opp_val == self:
                    setattr(old_value, "Java_Expression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_Expression286"):
                opp_val = getattr(value, "Java_Expression286", None)
                setattr(value, "Java_Expression286", self)

class Java_ArrayLengthAccess(Expression):

    pass
class Java_TypeLiteral(Expression):

    pass
class Java_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Java_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class Java_ArrayCreation(Expression):

    pass
class Java_ArrayAccess(Expression):

    pass
class Java_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class Java_FieldAccess(Expression):

    pass
class Java_NullLiteral(Expression):

    pass
class Java_CastExpression(Expression):

    pass
class Java_ParenthesizedExpression(Expression):

    pass
class Java_AbstractTypeQualifiedExpression(Expression):

    pass
class Java_Package(NamedElement):

    pass
class Java_TypeAccess(Expression, NamespaceAccess):

    pass
class Java_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "Java_AbstractMethodDeclaration" = None, SingleVariableDeclaration100: "Java_CatchClause" = None, SingleVariableDeclaration152: "Java_EnhancedForStatement" = None, SingleVariableDeclaration253: "Java_Modifier" = None, singleVariableDeclaration: "Java_Modifier" = None, Java_SingleVariableDeclaration: "Java_TypeAccess" = None, Java_SingleVariableDeclaration298: set["Java_Annotation"] = None, parameters: "Java_AbstractMethodDeclaration" = None, exception: "Java_CatchClause" = None, parameter: "Java_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration100 = SingleVariableDeclaration100
        self.SingleVariableDeclaration152 = SingleVariableDeclaration152
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.singleVariableDeclaration = singleVariableDeclaration
        self.Java_SingleVariableDeclaration = Java_SingleVariableDeclaration
        self.Java_SingleVariableDeclaration298 = Java_SingleVariableDeclaration298 if Java_SingleVariableDeclaration298 is not None else set()
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
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__parameters", None)
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
    def Java_SingleVariableDeclaration298(self):
        return self.__Java_SingleVariableDeclaration298

    @Java_SingleVariableDeclaration298.setter
    def Java_SingleVariableDeclaration298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__Java_SingleVariableDeclaration298", None)
        self.__Java_SingleVariableDeclaration298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java_Annotation299"):
                    opp_val = getattr(item, "Java_Annotation299", None)
                    
                    if opp_val == self:
                        setattr(item, "Java_Annotation299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java_Annotation299"):
                    opp_val = getattr(item, "Java_Annotation299", None)
                    
                    setattr(item, "Java_Annotation299", self)
                    

    @property
    def SingleVariableDeclaration100(self):
        return self.__SingleVariableDeclaration100

    @SingleVariableDeclaration100.setter
    def SingleVariableDeclaration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__SingleVariableDeclaration100", None)
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
    def singleVariableDeclaration(self):
        return self.__singleVariableDeclaration

    @singleVariableDeclaration.setter
    def singleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__singleVariableDeclaration", None)
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
    def SingleVariableDeclaration253(self):
        return self.__SingleVariableDeclaration253

    @SingleVariableDeclaration253.setter
    def SingleVariableDeclaration253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__SingleVariableDeclaration253", None)
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
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__parameter", None)
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
    def SingleVariableDeclaration152(self):
        return self.__SingleVariableDeclaration152

    @SingleVariableDeclaration152.setter
    def SingleVariableDeclaration152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__SingleVariableDeclaration152", None)
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
    def Java_SingleVariableDeclaration(self):
        return self.__Java_SingleVariableDeclaration

    @Java_SingleVariableDeclaration.setter
    def Java_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__Java_SingleVariableDeclaration", None)
        self.__Java_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java_TypeAccess296"):
                opp_val = getattr(old_value, "Java_TypeAccess296", None)
                if opp_val == self:
                    setattr(old_value, "Java_TypeAccess296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java_TypeAccess296"):
                opp_val = getattr(value, "Java_TypeAccess296", None)
                setattr(value, "Java_TypeAccess296", self)

    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__exception", None)
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
        old_value = getattr(self, f"_Java_SingleVariableDeclaration__SingleVariableDeclaration", None)
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

class Java_Block(Statement):

    pass
class BodyDeclaration:

    pass
class Java_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class Java_EnumConstantDeclaration(BodyDeclaration, VariableDeclaration):

    pass
class Java_Initializer(BodyDeclaration):

    pass
class Java_AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class Java_FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass
class Java_AbstractMethodDeclaration(BodyDeclaration):

    pass
class Java_AbstractMethodInvocation(ASTNode):

    pass
class Java_MethodRef(ASTNode):

    pass
class Java_TypeParameter(Type):

    pass