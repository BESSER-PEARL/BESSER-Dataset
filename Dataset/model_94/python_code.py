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
class AssignmentKind(Enum):
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
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
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
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"


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
class AnnotationTypeMemberDeclaration:

    pass
class UnresolvedItem:

    pass
class javaMM_UnresolvedAnnotationTypeMemberDeclaration(UnresolvedItem, AnnotationTypeMemberDeclaration):

    pass
class javaMM_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class javaMM_UnresolvedInterfaceDeclaration(UnresolvedItem, InterfaceDeclaration):

    pass
class javaMM_UnresolvedMethodDeclaration(UnresolvedItem, MethodDeclaration):

    pass
class javaMM_UnresolvedEnumDeclaration(UnresolvedItem, EnumDeclaration):

    pass
class javaMM_UnresolvedVariableDeclarationFragment(UnresolvedItem, VariableDeclarationFragment):

    pass
class javaMM_UnresolvedLabeledStatement(UnresolvedItem, LabeledStatement):

    pass
class AnnotationTypeDeclaration:

    pass
class javaMM_UnresolvedAnnotationDeclaration(UnresolvedItem, AnnotationTypeDeclaration):

    pass
class ClassDeclaration:

    pass
class javaMM_UnresolvedClassDeclaration(UnresolvedItem, ClassDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class javaMM_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class javaMM_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class PrimitiveType:

    pass
class javaMM_PrimitiveTypeByte(PrimitiveType):

    pass
class javaMM_PrimitiveTypeBoolean(PrimitiveType):

    pass
class javaMM_PrimitiveTypeVoid(PrimitiveType):

    pass
class javaMM_PrimitiveTypeLong(PrimitiveType):

    pass
class javaMM_PrimitiveTypeInt(PrimitiveType):

    pass
class javaMM_PrimitiveTypeFloat(PrimitiveType):

    pass
class javaMM_PrimitiveTypeShort(PrimitiveType):

    pass
class javaMM_PrimitiveTypeDouble(PrimitiveType):

    pass
class javaMM_PrimitiveTypeChar(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class javaMM_PackageAccess(NamespaceAccess):

    pass
class javaMM_Model:

    def __init__(self, name: str, model: set["javaMM_Package"] = None, javaMM_Model: set["javaMM_Type"] = None, javaMM_Model239: set["javaMM_UnresolvedItem"] = None, javaMM_Model241: set["javaMM_CompilationUnit"] = None, javaMM_Model244: set["javaMM_ClassFile"] = None, javaMM_Model247: set["javaMM_Archive"] = None, Model: "javaMM_Package" = None):
        self.name = name
        self.model = model if model is not None else set()
        self.javaMM_Model = javaMM_Model if javaMM_Model is not None else set()
        self.javaMM_Model239 = javaMM_Model239 if javaMM_Model239 is not None else set()
        self.javaMM_Model241 = javaMM_Model241 if javaMM_Model241 is not None else set()
        self.javaMM_Model244 = javaMM_Model244 if javaMM_Model244 is not None else set()
        self.javaMM_Model247 = javaMM_Model247 if javaMM_Model247 is not None else set()
        self.Model = Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaMM_Model247(self):
        return self.__javaMM_Model247

    @javaMM_Model247.setter
    def javaMM_Model247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__javaMM_Model247", None)
        self.__javaMM_Model247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Archive248"):
                    opp_val = getattr(item, "javaMM_Archive248", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Archive248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Archive248"):
                    opp_val = getattr(item, "javaMM_Archive248", None)
                    
                    setattr(item, "javaMM_Archive248", self)
                    

    @property
    def javaMM_Model239(self):
        return self.__javaMM_Model239

    @javaMM_Model239.setter
    def javaMM_Model239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__javaMM_Model239", None)
        self.__javaMM_Model239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_UnresolvedItem"):
                    opp_val = getattr(item, "javaMM_UnresolvedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_UnresolvedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_UnresolvedItem"):
                    opp_val = getattr(item, "javaMM_UnresolvedItem", None)
                    
                    setattr(item, "javaMM_UnresolvedItem", self)
                    

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__Model", None)
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
    def javaMM_Model241(self):
        return self.__javaMM_Model241

    @javaMM_Model241.setter
    def javaMM_Model241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__javaMM_Model241", None)
        self.__javaMM_Model241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_CompilationUnit242"):
                    opp_val = getattr(item, "javaMM_CompilationUnit242", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_CompilationUnit242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_CompilationUnit242"):
                    opp_val = getattr(item, "javaMM_CompilationUnit242", None)
                    
                    setattr(item, "javaMM_CompilationUnit242", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__model", None)
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
    def javaMM_Model244(self):
        return self.__javaMM_Model244

    @javaMM_Model244.setter
    def javaMM_Model244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__javaMM_Model244", None)
        self.__javaMM_Model244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_ClassFile245"):
                    opp_val = getattr(item, "javaMM_ClassFile245", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_ClassFile245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_ClassFile245"):
                    opp_val = getattr(item, "javaMM_ClassFile245", None)
                    
                    setattr(item, "javaMM_ClassFile245", self)
                    

    @property
    def javaMM_Model(self):
        return self.__javaMM_Model

    @javaMM_Model.setter
    def javaMM_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Model__javaMM_Model", None)
        self.__javaMM_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Type"):
                    opp_val = getattr(item, "javaMM_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Type"):
                    opp_val = getattr(item, "javaMM_Type", None)
                    
                    setattr(item, "javaMM_Type", self)
                    

class javaMM_ManifestEntry:

    def __init__(self, name: str, javaMM_ManifestEntry: "javaMM_Manifest" = None, javaMM_ManifestEntry211: set["javaMM_ManifestAttribute"] = None):
        self.name = name
        self.javaMM_ManifestEntry = javaMM_ManifestEntry
        self.javaMM_ManifestEntry211 = javaMM_ManifestEntry211 if javaMM_ManifestEntry211 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaMM_ManifestEntry(self):
        return self.__javaMM_ManifestEntry

    @javaMM_ManifestEntry.setter
    def javaMM_ManifestEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ManifestEntry__javaMM_ManifestEntry", None)
        self.__javaMM_ManifestEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Manifest209"):
                opp_val = getattr(old_value, "javaMM_Manifest209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Manifest209"):
                opp_val = getattr(value, "javaMM_Manifest209", None)
                if opp_val is None:
                    setattr(value, "javaMM_Manifest209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_ManifestEntry211(self):
        return self.__javaMM_ManifestEntry211

    @javaMM_ManifestEntry211.setter
    def javaMM_ManifestEntry211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ManifestEntry__javaMM_ManifestEntry211", None)
        self.__javaMM_ManifestEntry211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_ManifestAttribute212"):
                    opp_val = getattr(item, "javaMM_ManifestAttribute212", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_ManifestAttribute212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_ManifestAttribute212"):
                    opp_val = getattr(item, "javaMM_ManifestAttribute212", None)
                    
                    setattr(item, "javaMM_ManifestAttribute212", self)
                    

class javaMM_ManifestAttribute:

    def __init__(self, key: str, value: str, javaMM_ManifestAttribute: "javaMM_Manifest" = None, javaMM_ManifestAttribute212: "javaMM_ManifestEntry" = None):
        self.key = key
        self.value = value
        self.javaMM_ManifestAttribute = javaMM_ManifestAttribute
        self.javaMM_ManifestAttribute212 = javaMM_ManifestAttribute212
        
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
    def javaMM_ManifestAttribute(self):
        return self.__javaMM_ManifestAttribute

    @javaMM_ManifestAttribute.setter
    def javaMM_ManifestAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ManifestAttribute__javaMM_ManifestAttribute", None)
        self.__javaMM_ManifestAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Manifest207"):
                opp_val = getattr(old_value, "javaMM_Manifest207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Manifest207"):
                opp_val = getattr(value, "javaMM_Manifest207", None)
                if opp_val is None:
                    setattr(value, "javaMM_Manifest207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_ManifestAttribute212(self):
        return self.__javaMM_ManifestAttribute212

    @javaMM_ManifestAttribute212.setter
    def javaMM_ManifestAttribute212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ManifestAttribute__javaMM_ManifestAttribute212", None)
        self.__javaMM_ManifestAttribute212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ManifestEntry211"):
                opp_val = getattr(old_value, "javaMM_ManifestEntry211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ManifestEntry211"):
                opp_val = getattr(value, "javaMM_ManifestEntry211", None)
                if opp_val is None:
                    setattr(value, "javaMM_ManifestEntry211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractVariablesContainer:

    pass
class VariableDeclaration:

    pass
class TypeDeclaration:

    pass
class javaMM_InterfaceDeclaration(TypeDeclaration):

    pass
class javaMM_ClassDeclaration(TypeDeclaration):

    def __init__(self, javaMM_ClassDeclaration: "javaMM_TypeAccess" = None):
        self.javaMM_ClassDeclaration = javaMM_ClassDeclaration
        
    @property
    def javaMM_ClassDeclaration(self):
        return self.__javaMM_ClassDeclaration

    @javaMM_ClassDeclaration.setter
    def javaMM_ClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassDeclaration__javaMM_ClassDeclaration", None)
        self.__javaMM_ClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess127"):
                opp_val = getattr(old_value, "javaMM_TypeAccess127", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess127"):
                opp_val = getattr(value, "javaMM_TypeAccess127", None)
                setattr(value, "javaMM_TypeAccess127", self)

    def noCovariantCompareTo(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement noCovariantCompareTo method
        pass

    def serialUIDInSerializableClass(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement serialUIDInSerializableClass method
        pass

    def noObscuredVariables(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noObscuredVariables method
        pass

    def getMethods(self) -> str:
        # TODO: Implement getMethods method
        pass

    def noRedundantInterfaceImpl(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement noRedundantInterfaceImpl method
        pass

    def comparatorImplementsSerializable(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement comparatorImplementsSerializable method
        pass

    def hashCodeAndEquals(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hashCodeAndEquals method
        pass

    def cloneInCloneable(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement cloneInCloneable method
        pass

    def hasEquals(self) -> str:
        # TODO: Implement hasEquals method
        pass

    def equalsAndCompareTo(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement equalsAndCompareTo method
        pass

    def hasCompareTo(self) -> str:
        # TODO: Implement hasCompareTo method
        pass

    def hasHashcode(self) -> str:
        # TODO: Implement hasHashcode method
        pass

    def noCovariantEquals(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noCovariantEquals method
        pass

class AbstractMethodDeclaration:

    pass
class javaMM_MethodDeclaration(AbstractMethodDeclaration):

    def __init__(self, extraArrayDimensions: int, javaMM_MethodDeclaration: "javaMM_TypeAccess" = None, MethodDeclaration: "javaMM_MethodDeclaration" = None, redefinitions: "javaMM_MethodDeclaration" = None, MethodDeclaration223: "javaMM_MethodDeclaration" = None, redefinedMethodDeclaration: set["javaMM_MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.javaMM_MethodDeclaration = javaMM_MethodDeclaration
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
    def redefinedMethodDeclaration(self):
        return self.__redefinedMethodDeclaration

    @redefinedMethodDeclaration.setter
    def redefinedMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodDeclaration__redefinedMethodDeclaration", None)
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
        old_value = getattr(self, f"_javaMM_MethodDeclaration__redefinitions", None)
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
    def javaMM_MethodDeclaration(self):
        return self.__javaMM_MethodDeclaration

    @javaMM_MethodDeclaration.setter
    def javaMM_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodDeclaration__javaMM_MethodDeclaration", None)
        self.__javaMM_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess218"):
                opp_val = getattr(old_value, "javaMM_TypeAccess218", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess218"):
                opp_val = getattr(value, "javaMM_TypeAccess218", None)
                setattr(value, "javaMM_TypeAccess218", self)

    @property
    def MethodDeclaration(self):
        return self.__MethodDeclaration

    @MethodDeclaration.setter
    def MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodDeclaration__MethodDeclaration", None)
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
        old_value = getattr(self, f"_javaMM_MethodDeclaration__MethodDeclaration223", None)
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

    def shouldStartWithLowerCase(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement shouldStartWithLowerCase method
        pass

class javaMM_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class javaMM_SuperMethodInvocation(AbstractTypeQualifiedExpression, AbstractMethodInvocation):

    pass
class Comment:

    pass
class javaMM_LineComment(Comment):

    pass
class javaMM_Javadoc(Comment):

    pass
class javaMM_BlockComment(Comment):

    pass
class AbstractTypeDeclaration:

    pass
class javaMM_UnresolvedTypeDeclaration(UnresolvedItem, AbstractTypeDeclaration):

    pass
class javaMM_TypeDeclaration(AbstractTypeDeclaration):

    pass
class javaMM_EnumDeclaration(AbstractTypeDeclaration):

    pass
class javaMM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class javaMM_ASTNode(ABC):

    pass
class Statement:

    pass
class javaMM_VariableDeclarationStatement(Statement, AbstractVariablesContainer):

    def __init__(self, extraArrayDimensions: int, VariableDeclarationStatement: "javaMM_Modifier" = None, variableDeclarationStatement: "javaMM_Modifier" = None, javaMM_VariableDeclarationStatement: set["javaMM_Annotation"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclarationStatement = VariableDeclarationStatement
        self.variableDeclarationStatement = variableDeclarationStatement
        self.javaMM_VariableDeclarationStatement = javaMM_VariableDeclarationStatement if javaMM_VariableDeclarationStatement is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def javaMM_VariableDeclarationStatement(self):
        return self.__javaMM_VariableDeclarationStatement

    @javaMM_VariableDeclarationStatement.setter
    def javaMM_VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationStatement__javaMM_VariableDeclarationStatement", None)
        self.__javaMM_VariableDeclarationStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Annotation362"):
                    opp_val = getattr(item, "javaMM_Annotation362", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Annotation362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Annotation362"):
                    opp_val = getattr(item, "javaMM_Annotation362", None)
                    
                    setattr(item, "javaMM_Annotation362", self)
                    

    @property
    def variableDeclarationStatement(self):
        return self.__variableDeclarationStatement

    @variableDeclarationStatement.setter
    def variableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationStatement__variableDeclarationStatement", None)
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
    def VariableDeclarationStatement(self):
        return self.__VariableDeclarationStatement

    @VariableDeclarationStatement.setter
    def VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationStatement__VariableDeclarationStatement", None)
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

    def publicVariableIsFinal(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement publicVariableIsFinal method
        pass

class javaMM_SwitchStatement(Statement):

    def __init__(self, javaMM_SwitchStatement: "javaMM_Expression" = None, javaMM_SwitchStatement313: set["javaMM_Statement"] = None):
        self.javaMM_SwitchStatement = javaMM_SwitchStatement
        self.javaMM_SwitchStatement313 = javaMM_SwitchStatement313 if javaMM_SwitchStatement313 is not None else set()
        
    @property
    def javaMM_SwitchStatement(self):
        return self.__javaMM_SwitchStatement

    @javaMM_SwitchStatement.setter
    def javaMM_SwitchStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SwitchStatement__javaMM_SwitchStatement", None)
        self.__javaMM_SwitchStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression311"):
                opp_val = getattr(old_value, "javaMM_Expression311", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression311"):
                opp_val = getattr(value, "javaMM_Expression311", None)
                setattr(value, "javaMM_Expression311", self)

    @property
    def javaMM_SwitchStatement313(self):
        return self.__javaMM_SwitchStatement313

    @javaMM_SwitchStatement313.setter
    def javaMM_SwitchStatement313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SwitchStatement__javaMM_SwitchStatement313", None)
        self.__javaMM_SwitchStatement313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Statement314"):
                    opp_val = getattr(item, "javaMM_Statement314", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Statement314", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Statement314"):
                    opp_val = getattr(item, "javaMM_Statement314", None)
                    
                    setattr(item, "javaMM_Statement314", self)
                    

    def moreThan3Cases(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement moreThan3Cases method
        pass

class javaMM_ReturnStatement(Statement):

    pass
class javaMM_SwitchCase(Statement):

    def __init__(self, default: str, javaMM_SwitchCase: "javaMM_Expression" = None):
        self.default = default
        self.javaMM_SwitchCase = javaMM_SwitchCase
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def javaMM_SwitchCase(self):
        return self.__javaMM_SwitchCase

    @javaMM_SwitchCase.setter
    def javaMM_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SwitchCase__javaMM_SwitchCase", None)
        self.__javaMM_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression309"):
                opp_val = getattr(old_value, "javaMM_Expression309", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression309"):
                opp_val = getattr(value, "javaMM_Expression309", None)
                setattr(value, "javaMM_Expression309", self)

class javaMM_ExpressionStatement(Statement):

    pass
class javaMM_SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    def __init__(self, javaMM_SuperConstructorInvocation: "javaMM_Expression" = None):
        self.javaMM_SuperConstructorInvocation = javaMM_SuperConstructorInvocation
        
    @property
    def javaMM_SuperConstructorInvocation(self):
        return self.__javaMM_SuperConstructorInvocation

    @javaMM_SuperConstructorInvocation.setter
    def javaMM_SuperConstructorInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SuperConstructorInvocation__javaMM_SuperConstructorInvocation", None)
        self.__javaMM_SuperConstructorInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression305"):
                opp_val = getattr(old_value, "javaMM_Expression305", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression305"):
                opp_val = getattr(value, "javaMM_Expression305", None)
                setattr(value, "javaMM_Expression305", self)

    def noRedundantSuperCall(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement noRedundantSuperCall method
        pass

class javaMM_ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class javaMM_IfStatement(Statement):

    def __init__(self, javaMM_IfStatement: "javaMM_Expression" = None, javaMM_IfStatement179: "javaMM_Statement" = None, javaMM_IfStatement182: "javaMM_Statement" = None):
        self.javaMM_IfStatement = javaMM_IfStatement
        self.javaMM_IfStatement179 = javaMM_IfStatement179
        self.javaMM_IfStatement182 = javaMM_IfStatement182
        
    @property
    def javaMM_IfStatement182(self):
        return self.__javaMM_IfStatement182

    @javaMM_IfStatement182.setter
    def javaMM_IfStatement182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_IfStatement__javaMM_IfStatement182", None)
        self.__javaMM_IfStatement182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Statement183"):
                opp_val = getattr(old_value, "javaMM_Statement183", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Statement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Statement183"):
                opp_val = getattr(value, "javaMM_Statement183", None)
                setattr(value, "javaMM_Statement183", self)

    @property
    def javaMM_IfStatement(self):
        return self.__javaMM_IfStatement

    @javaMM_IfStatement.setter
    def javaMM_IfStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_IfStatement__javaMM_IfStatement", None)
        self.__javaMM_IfStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression177"):
                opp_val = getattr(old_value, "javaMM_Expression177", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression177"):
                opp_val = getattr(value, "javaMM_Expression177", None)
                setattr(value, "javaMM_Expression177", self)

    @property
    def javaMM_IfStatement179(self):
        return self.__javaMM_IfStatement179

    @javaMM_IfStatement179.setter
    def javaMM_IfStatement179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_IfStatement__javaMM_IfStatement179", None)
        self.__javaMM_IfStatement179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Statement180"):
                opp_val = getattr(old_value, "javaMM_Statement180", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Statement180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Statement180"):
                opp_val = getattr(value, "javaMM_Statement180", None)
                setattr(value, "javaMM_Statement180", self)

    def noDeadCode(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noDeadCode method
        pass

    def noUselessControlFlow(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noUselessControlFlow method
        pass

class javaMM_TypeDeclarationStatement(Statement):

    pass
class javaMM_CatchClause(Statement):

    def __init__(self, catchClause: "javaMM_SingleVariableDeclaration" = None, javaMM_CatchClause: "javaMM_Block" = None, CatchClause: "javaMM_SingleVariableDeclaration" = None, javaMM_CatchClause332: "javaMM_TryStatement" = None):
        self.catchClause = catchClause
        self.javaMM_CatchClause = javaMM_CatchClause
        self.CatchClause = CatchClause
        self.javaMM_CatchClause332 = javaMM_CatchClause332
        
    @property
    def javaMM_CatchClause(self):
        return self.__javaMM_CatchClause

    @javaMM_CatchClause.setter
    def javaMM_CatchClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CatchClause__javaMM_CatchClause", None)
        self.__javaMM_CatchClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Block102"):
                opp_val = getattr(old_value, "javaMM_Block102", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Block102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Block102"):
                opp_val = getattr(value, "javaMM_Block102", None)
                setattr(value, "javaMM_Block102", self)

    @property
    def catchClause(self):
        return self.__catchClause

    @catchClause.setter
    def catchClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CatchClause__catchClause", None)
        self.__catchClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleVariableDeclaration100"):
                opp_val = getattr(old_value, "SingleVariableDeclaration100", None)
                if opp_val == self:
                    setattr(old_value, "SingleVariableDeclaration100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleVariableDeclaration100"):
                opp_val = getattr(value, "SingleVariableDeclaration100", None)
                setattr(value, "SingleVariableDeclaration100", self)

    @property
    def CatchClause(self):
        return self.__CatchClause

    @CatchClause.setter
    def CatchClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CatchClause__CatchClause", None)
        self.__CatchClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exception"):
                opp_val = getattr(old_value, "exception", None)
                if opp_val == self:
                    setattr(old_value, "exception", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exception"):
                opp_val = getattr(value, "exception", None)
                setattr(value, "exception", self)

    @property
    def javaMM_CatchClause332(self):
        return self.__javaMM_CatchClause332

    @javaMM_CatchClause332.setter
    def javaMM_CatchClause332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CatchClause__javaMM_CatchClause332", None)
        self.__javaMM_CatchClause332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TryStatement331"):
                opp_val = getattr(old_value, "javaMM_TryStatement331", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TryStatement331"):
                opp_val = getattr(value, "javaMM_TryStatement331", None)
                if opp_val is None:
                    setattr(value, "javaMM_TryStatement331", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def exceptionIsUsed(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement exceptionIsUsed method
        pass

    def doesNotCatchDubiousExceptions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement doesNotCatchDubiousExceptions method
        pass

class javaMM_TryStatement(Statement):

    pass
class javaMM_DoStatement(Statement):

    pass
class javaMM_EnhancedForStatement(Statement):

    pass
class javaMM_SynchronizedStatement(Statement):

    def __init__(self, javaMM_SynchronizedStatement: "javaMM_Block" = None, javaMM_SynchronizedStatement318: "javaMM_Expression" = None):
        self.javaMM_SynchronizedStatement = javaMM_SynchronizedStatement
        self.javaMM_SynchronizedStatement318 = javaMM_SynchronizedStatement318
        
    @property
    def javaMM_SynchronizedStatement(self):
        return self.__javaMM_SynchronizedStatement

    @javaMM_SynchronizedStatement.setter
    def javaMM_SynchronizedStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SynchronizedStatement__javaMM_SynchronizedStatement", None)
        self.__javaMM_SynchronizedStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Block316"):
                opp_val = getattr(old_value, "javaMM_Block316", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Block316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Block316"):
                opp_val = getattr(value, "javaMM_Block316", None)
                setattr(value, "javaMM_Block316", self)

    @property
    def javaMM_SynchronizedStatement318(self):
        return self.__javaMM_SynchronizedStatement318

    @javaMM_SynchronizedStatement318.setter
    def javaMM_SynchronizedStatement318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SynchronizedStatement__javaMM_SynchronizedStatement318", None)
        self.__javaMM_SynchronizedStatement318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression319"):
                opp_val = getattr(old_value, "javaMM_Expression319", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression319"):
                opp_val = getattr(value, "javaMM_Expression319", None)
                setattr(value, "javaMM_Expression319", self)

    def hasStatements(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasStatements method
        pass

class javaMM_BreakStatement(Statement):

    pass
class javaMM_ForStatement(Statement):

    pass
class javaMM_EmptyStatement(Statement):

    pass
class javaMM_WhileStatement(Statement):

    pass
class javaMM_ThrowStatement(Statement):

    pass
class javaMM_ContinueStatement(Statement):

    pass
class javaMM_AssertStatement(Statement):

    pass
class javaMM_Manifest:

    pass
class NamedElement:

    pass
class javaMM_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, VariableDeclaration: "javaMM_SingleVariableAccess" = None, variable: set["javaMM_SingleVariableAccess"] = None, javaMM_VariableDeclaration: "javaMM_Expression" = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclaration = VariableDeclaration
        self.variable = variable if variable is not None else set()
        self.javaMM_VariableDeclaration = javaMM_VariableDeclaration
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclaration__VariableDeclaration", None)
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
        old_value = getattr(self, f"_javaMM_VariableDeclaration__variable", None)
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
    def javaMM_VariableDeclaration(self):
        return self.__javaMM_VariableDeclaration

    @javaMM_VariableDeclaration.setter
    def javaMM_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclaration__javaMM_VariableDeclaration", None)
        self.__javaMM_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression352"):
                opp_val = getattr(old_value, "javaMM_Expression352", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression352"):
                opp_val = getattr(value, "javaMM_Expression352", None)
                setattr(value, "javaMM_Expression352", self)

    def variableIsUsed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement variableIsUsed method
        pass

class javaMM_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, javaMM_CompilationUnit: "javaMM_ASTNode" = None, javaMM_CompilationUnit108: "javaMM_ClassFile" = None, javaMM_CompilationUnit129: set["javaMM_Comment"] = None, javaMM_CompilationUnit132: set["javaMM_ImportDeclaration"] = None, javaMM_CompilationUnit134: "javaMM_Package" = None, javaMM_CompilationUnit137: set["javaMM_AbstractTypeDeclaration"] = None, javaMM_CompilationUnit242: "javaMM_Model" = None):
        self.originalFilePath = originalFilePath
        self.javaMM_CompilationUnit = javaMM_CompilationUnit
        self.javaMM_CompilationUnit108 = javaMM_CompilationUnit108
        self.javaMM_CompilationUnit129 = javaMM_CompilationUnit129 if javaMM_CompilationUnit129 is not None else set()
        self.javaMM_CompilationUnit132 = javaMM_CompilationUnit132 if javaMM_CompilationUnit132 is not None else set()
        self.javaMM_CompilationUnit134 = javaMM_CompilationUnit134
        self.javaMM_CompilationUnit137 = javaMM_CompilationUnit137 if javaMM_CompilationUnit137 is not None else set()
        self.javaMM_CompilationUnit242 = javaMM_CompilationUnit242
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def javaMM_CompilationUnit129(self):
        return self.__javaMM_CompilationUnit129

    @javaMM_CompilationUnit129.setter
    def javaMM_CompilationUnit129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit129", None)
        self.__javaMM_CompilationUnit129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Comment130"):
                    opp_val = getattr(item, "javaMM_Comment130", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Comment130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Comment130"):
                    opp_val = getattr(item, "javaMM_Comment130", None)
                    
                    setattr(item, "javaMM_Comment130", self)
                    

    @property
    def javaMM_CompilationUnit242(self):
        return self.__javaMM_CompilationUnit242

    @javaMM_CompilationUnit242.setter
    def javaMM_CompilationUnit242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit242", None)
        self.__javaMM_CompilationUnit242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Model241"):
                opp_val = getattr(old_value, "javaMM_Model241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Model241"):
                opp_val = getattr(value, "javaMM_Model241", None)
                if opp_val is None:
                    setattr(value, "javaMM_Model241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_CompilationUnit108(self):
        return self.__javaMM_CompilationUnit108

    @javaMM_CompilationUnit108.setter
    def javaMM_CompilationUnit108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit108", None)
        self.__javaMM_CompilationUnit108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ClassFile107"):
                opp_val = getattr(old_value, "javaMM_ClassFile107", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_ClassFile107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ClassFile107"):
                opp_val = getattr(value, "javaMM_ClassFile107", None)
                setattr(value, "javaMM_ClassFile107", self)

    @property
    def javaMM_CompilationUnit(self):
        return self.__javaMM_CompilationUnit

    @javaMM_CompilationUnit.setter
    def javaMM_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit", None)
        self.__javaMM_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ASTNode43"):
                opp_val = getattr(old_value, "javaMM_ASTNode43", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_ASTNode43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ASTNode43"):
                opp_val = getattr(value, "javaMM_ASTNode43", None)
                setattr(value, "javaMM_ASTNode43", self)

    @property
    def javaMM_CompilationUnit137(self):
        return self.__javaMM_CompilationUnit137

    @javaMM_CompilationUnit137.setter
    def javaMM_CompilationUnit137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit137", None)
        self.__javaMM_CompilationUnit137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "javaMM_AbstractTypeDeclaration138", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_AbstractTypeDeclaration138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "javaMM_AbstractTypeDeclaration138", None)
                    
                    setattr(item, "javaMM_AbstractTypeDeclaration138", self)
                    

    @property
    def javaMM_CompilationUnit134(self):
        return self.__javaMM_CompilationUnit134

    @javaMM_CompilationUnit134.setter
    def javaMM_CompilationUnit134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit134", None)
        self.__javaMM_CompilationUnit134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Package135"):
                opp_val = getattr(old_value, "javaMM_Package135", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Package135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Package135"):
                opp_val = getattr(value, "javaMM_Package135", None)
                setattr(value, "javaMM_Package135", self)

    @property
    def javaMM_CompilationUnit132(self):
        return self.__javaMM_CompilationUnit132

    @javaMM_CompilationUnit132.setter
    def javaMM_CompilationUnit132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_CompilationUnit__javaMM_CompilationUnit132", None)
        self.__javaMM_CompilationUnit132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_ImportDeclaration"):
                    opp_val = getattr(item, "javaMM_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_ImportDeclaration"):
                    opp_val = getattr(item, "javaMM_ImportDeclaration", None)
                    
                    setattr(item, "javaMM_ImportDeclaration", self)
                    

class javaMM_UnresolvedItem(NamedElement):

    pass
class javaMM_ClassFile(NamedElement):

    def __init__(self, originalFilePath: str, javaMM_ClassFile: "javaMM_Archive" = None, javaMM_ClassFile46: "javaMM_ASTNode" = None, javaMM_ClassFile104: "javaMM_AbstractTypeDeclaration" = None, javaMM_ClassFile107: "javaMM_CompilationUnit" = None, javaMM_ClassFile110: "javaMM_Package" = None, javaMM_ClassFile245: "javaMM_Model" = None):
        self.originalFilePath = originalFilePath
        self.javaMM_ClassFile = javaMM_ClassFile
        self.javaMM_ClassFile46 = javaMM_ClassFile46
        self.javaMM_ClassFile104 = javaMM_ClassFile104
        self.javaMM_ClassFile107 = javaMM_ClassFile107
        self.javaMM_ClassFile110 = javaMM_ClassFile110
        self.javaMM_ClassFile245 = javaMM_ClassFile245
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def javaMM_ClassFile46(self):
        return self.__javaMM_ClassFile46

    @javaMM_ClassFile46.setter
    def javaMM_ClassFile46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile46", None)
        self.__javaMM_ClassFile46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ASTNode45"):
                opp_val = getattr(old_value, "javaMM_ASTNode45", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_ASTNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ASTNode45"):
                opp_val = getattr(value, "javaMM_ASTNode45", None)
                setattr(value, "javaMM_ASTNode45", self)

    @property
    def javaMM_ClassFile(self):
        return self.__javaMM_ClassFile

    @javaMM_ClassFile.setter
    def javaMM_ClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile", None)
        self.__javaMM_ClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Archive"):
                opp_val = getattr(old_value, "javaMM_Archive", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Archive"):
                opp_val = getattr(value, "javaMM_Archive", None)
                if opp_val is None:
                    setattr(value, "javaMM_Archive", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_ClassFile107(self):
        return self.__javaMM_ClassFile107

    @javaMM_ClassFile107.setter
    def javaMM_ClassFile107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile107", None)
        self.__javaMM_ClassFile107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_CompilationUnit108"):
                opp_val = getattr(old_value, "javaMM_CompilationUnit108", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_CompilationUnit108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_CompilationUnit108"):
                opp_val = getattr(value, "javaMM_CompilationUnit108", None)
                setattr(value, "javaMM_CompilationUnit108", self)

    @property
    def javaMM_ClassFile110(self):
        return self.__javaMM_ClassFile110

    @javaMM_ClassFile110.setter
    def javaMM_ClassFile110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile110", None)
        self.__javaMM_ClassFile110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Package"):
                opp_val = getattr(old_value, "javaMM_Package", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Package"):
                opp_val = getattr(value, "javaMM_Package", None)
                setattr(value, "javaMM_Package", self)

    @property
    def javaMM_ClassFile104(self):
        return self.__javaMM_ClassFile104

    @javaMM_ClassFile104.setter
    def javaMM_ClassFile104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile104", None)
        self.__javaMM_ClassFile104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_AbstractTypeDeclaration105"):
                opp_val = getattr(old_value, "javaMM_AbstractTypeDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_AbstractTypeDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_AbstractTypeDeclaration105"):
                opp_val = getattr(value, "javaMM_AbstractTypeDeclaration105", None)
                setattr(value, "javaMM_AbstractTypeDeclaration105", self)

    @property
    def javaMM_ClassFile245(self):
        return self.__javaMM_ClassFile245

    @javaMM_ClassFile245.setter
    def javaMM_ClassFile245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ClassFile__javaMM_ClassFile245", None)
        self.__javaMM_ClassFile245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Model244"):
                opp_val = getattr(old_value, "javaMM_Model244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Model244"):
                opp_val = getattr(value, "javaMM_Model244", None)
                if opp_val is None:
                    setattr(value, "javaMM_Model244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaMM_Type(NamedElement):

    pass
class javaMM_LabeledStatement(Statement, NamedElement):

    pass
class javaMM_Archive(NamedElement):

    def __init__(self, originalFilePath: str, javaMM_Archive34: "javaMM_Manifest" = None, javaMM_Archive: set["javaMM_ClassFile"] = None, javaMM_Archive248: "javaMM_Model" = None):
        self.originalFilePath = originalFilePath
        self.javaMM_Archive34 = javaMM_Archive34
        self.javaMM_Archive = javaMM_Archive if javaMM_Archive is not None else set()
        self.javaMM_Archive248 = javaMM_Archive248
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def javaMM_Archive248(self):
        return self.__javaMM_Archive248

    @javaMM_Archive248.setter
    def javaMM_Archive248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Archive__javaMM_Archive248", None)
        self.__javaMM_Archive248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Model247"):
                opp_val = getattr(old_value, "javaMM_Model247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Model247"):
                opp_val = getattr(value, "javaMM_Model247", None)
                if opp_val is None:
                    setattr(value, "javaMM_Model247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_Archive(self):
        return self.__javaMM_Archive

    @javaMM_Archive.setter
    def javaMM_Archive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Archive__javaMM_Archive", None)
        self.__javaMM_Archive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_ClassFile"):
                    opp_val = getattr(item, "javaMM_ClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_ClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_ClassFile"):
                    opp_val = getattr(item, "javaMM_ClassFile", None)
                    
                    setattr(item, "javaMM_ClassFile", self)
                    

    @property
    def javaMM_Archive34(self):
        return self.__javaMM_Archive34

    @javaMM_Archive34.setter
    def javaMM_Archive34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Archive__javaMM_Archive34", None)
        self.__javaMM_Archive34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Manifest"):
                opp_val = getattr(old_value, "javaMM_Manifest", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Manifest"):
                opp_val = getattr(value, "javaMM_Manifest", None)
                setattr(value, "javaMM_Manifest", self)

class javaMM_AnnotationMemberValuePair(NamedElement):

    pass
class javaMM_VariableDeclarationFragment(VariableDeclaration):

    pass
class javaMM_Package(NamedElement):

    pass
class Expression:

    pass
class javaMM_ArrayInitializer(Expression):

    pass
class javaMM_ArrayCreation(Expression):

    pass
class javaMM_VariableDeclarationExpression(Expression, AbstractVariablesContainer):

    def __init__(self, VariableDeclarationExpression: "javaMM_Modifier" = None, variableDeclarationExpression: "javaMM_Modifier" = None, javaMM_VariableDeclarationExpression: set["javaMM_Annotation"] = None):
        self.VariableDeclarationExpression = VariableDeclarationExpression
        self.variableDeclarationExpression = variableDeclarationExpression
        self.javaMM_VariableDeclarationExpression = javaMM_VariableDeclarationExpression if javaMM_VariableDeclarationExpression is not None else set()
        
    @property
    def VariableDeclarationExpression(self):
        return self.__VariableDeclarationExpression

    @VariableDeclarationExpression.setter
    def VariableDeclarationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationExpression__VariableDeclarationExpression", None)
        self.__VariableDeclarationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifier257"):
                opp_val = getattr(old_value, "modifier257", None)
                if opp_val == self:
                    setattr(old_value, "modifier257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifier257"):
                opp_val = getattr(value, "modifier257", None)
                setattr(value, "modifier257", self)

    @property
    def variableDeclarationExpression(self):
        return self.__variableDeclarationExpression

    @variableDeclarationExpression.setter
    def variableDeclarationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationExpression__variableDeclarationExpression", None)
        self.__variableDeclarationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Modifier355"):
                opp_val = getattr(old_value, "Modifier355", None)
                if opp_val == self:
                    setattr(old_value, "Modifier355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifier355"):
                opp_val = getattr(value, "Modifier355", None)
                setattr(value, "Modifier355", self)

    @property
    def javaMM_VariableDeclarationExpression(self):
        return self.__javaMM_VariableDeclarationExpression

    @javaMM_VariableDeclarationExpression.setter
    def javaMM_VariableDeclarationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_VariableDeclarationExpression__javaMM_VariableDeclarationExpression", None)
        self.__javaMM_VariableDeclarationExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Annotation357"):
                    opp_val = getattr(item, "javaMM_Annotation357", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Annotation357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Annotation357"):
                    opp_val = getattr(item, "javaMM_Annotation357", None)
                    
                    setattr(item, "javaMM_Annotation357", self)
                    

    def publicVariableIsFinal(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement publicVariableIsFinal method
        pass

class javaMM_ArrayAccess(Expression):

    pass
class javaMM_ConditionalExpression(Expression):

    pass
class javaMM_NullLiteral(Expression):

    pass
class javaMM_Annotation(Expression):

    pass
class javaMM_SingleVariableAccess(Expression):

    pass
class javaMM_ClassInstanceCreation(AbstractMethodInvocation, Expression):

    pass
class javaMM_PrefixExpression(Expression):

    def __init__(self, operator: str, javaMM_PrefixExpression: "javaMM_Expression" = None):
        self.operator = operator
        self.javaMM_PrefixExpression = javaMM_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaMM_PrefixExpression(self):
        return self.__javaMM_PrefixExpression

    @javaMM_PrefixExpression.setter
    def javaMM_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_PrefixExpression__javaMM_PrefixExpression", None)
        self.__javaMM_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression286"):
                opp_val = getattr(old_value, "javaMM_Expression286", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression286"):
                opp_val = getattr(value, "javaMM_Expression286", None)
                setattr(value, "javaMM_Expression286", self)

class javaMM_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class javaMM_MethodInvocation(AbstractMethodInvocation, Expression):

    def __init__(self, javaMM_MethodInvocation: "javaMM_Expression" = None):
        self.javaMM_MethodInvocation = javaMM_MethodInvocation
        
    @property
    def javaMM_MethodInvocation(self):
        return self.__javaMM_MethodInvocation

    @javaMM_MethodInvocation.setter
    def javaMM_MethodInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodInvocation__javaMM_MethodInvocation", None)
        self.__javaMM_MethodInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression225"):
                opp_val = getattr(old_value, "javaMM_Expression225", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression225"):
                opp_val = getattr(value, "javaMM_Expression225", None)
                setattr(value, "javaMM_Expression225", self)

    def doesNotCallExit(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement doesNotCallExit method
        pass

    def doesNotCallFinalize(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement doesNotCallFinalize method
        pass

    def doesNotCallRunFinalizers(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement doesNotCallRunFinalizers method
        pass

class javaMM_PostfixExpression(Expression):

    def __init__(self, operator: str, javaMM_PostfixExpression: "javaMM_Expression" = None):
        self.operator = operator
        self.javaMM_PostfixExpression = javaMM_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaMM_PostfixExpression(self):
        return self.__javaMM_PostfixExpression

    @javaMM_PostfixExpression.setter
    def javaMM_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_PostfixExpression__javaMM_PostfixExpression", None)
        self.__javaMM_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression284"):
                opp_val = getattr(old_value, "javaMM_Expression284", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression284"):
                opp_val = getattr(value, "javaMM_Expression284", None)
                setattr(value, "javaMM_Expression284", self)

class javaMM_CastExpression(Expression):

    pass
class javaMM_TypeLiteral(Expression):

    pass
class javaMM_Assignment(Expression):

    def __init__(self, operator: str, javaMM_Assignment: "javaMM_Expression" = None, javaMM_Assignment83: "javaMM_Expression" = None):
        self.operator = operator
        self.javaMM_Assignment = javaMM_Assignment
        self.javaMM_Assignment83 = javaMM_Assignment83
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaMM_Assignment(self):
        return self.__javaMM_Assignment

    @javaMM_Assignment.setter
    def javaMM_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Assignment__javaMM_Assignment", None)
        self.__javaMM_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression81"):
                opp_val = getattr(old_value, "javaMM_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression81"):
                opp_val = getattr(value, "javaMM_Expression81", None)
                setattr(value, "javaMM_Expression81", self)

    @property
    def javaMM_Assignment83(self):
        return self.__javaMM_Assignment83

    @javaMM_Assignment83.setter
    def javaMM_Assignment83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Assignment__javaMM_Assignment83", None)
        self.__javaMM_Assignment83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression84"):
                opp_val = getattr(old_value, "javaMM_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression84"):
                opp_val = getattr(value, "javaMM_Expression84", None)
                setattr(value, "javaMM_Expression84", self)

    def noRedundantAssignment(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement noRedundantAssignment method
        pass

class javaMM_FieldAccess(Expression):

    pass
class javaMM_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class javaMM_ParenthesizedExpression(Expression):

    pass
class javaMM_UnresolvedItemAccess(NamespaceAccess, Expression):

    pass
class javaMM_InstanceofExpression(Expression):

    pass
class javaMM_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class javaMM_BooleanLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class javaMM_InfixExpression(Expression):

    def __init__(self, operator: str, javaMM_InfixExpression: "javaMM_Expression" = None, javaMM_InfixExpression188: "javaMM_Expression" = None, javaMM_InfixExpression191: set["javaMM_Expression"] = None):
        self.operator = operator
        self.javaMM_InfixExpression = javaMM_InfixExpression
        self.javaMM_InfixExpression188 = javaMM_InfixExpression188
        self.javaMM_InfixExpression191 = javaMM_InfixExpression191 if javaMM_InfixExpression191 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaMM_InfixExpression188(self):
        return self.__javaMM_InfixExpression188

    @javaMM_InfixExpression188.setter
    def javaMM_InfixExpression188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_InfixExpression__javaMM_InfixExpression188", None)
        self.__javaMM_InfixExpression188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression189"):
                opp_val = getattr(old_value, "javaMM_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression189"):
                opp_val = getattr(value, "javaMM_Expression189", None)
                setattr(value, "javaMM_Expression189", self)

    @property
    def javaMM_InfixExpression(self):
        return self.__javaMM_InfixExpression

    @javaMM_InfixExpression.setter
    def javaMM_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_InfixExpression__javaMM_InfixExpression", None)
        self.__javaMM_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Expression186"):
                opp_val = getattr(old_value, "javaMM_Expression186", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Expression186"):
                opp_val = getattr(value, "javaMM_Expression186", None)
                setattr(value, "javaMM_Expression186", self)

    @property
    def javaMM_InfixExpression191(self):
        return self.__javaMM_InfixExpression191

    @javaMM_InfixExpression191.setter
    def javaMM_InfixExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_InfixExpression__javaMM_InfixExpression191", None)
        self.__javaMM_InfixExpression191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Expression192"):
                    opp_val = getattr(item, "javaMM_Expression192", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Expression192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Expression192"):
                    opp_val = getattr(item, "javaMM_Expression192", None)
                    
                    setattr(item, "javaMM_Expression192", self)
                    

    def equalsNotOnStrings(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement equalsNotOnStrings method
        pass

    def noRedundantComparison(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement noRedundantComparison method
        pass

    def operatorIsEquality(self) -> str:
        # TODO: Implement operatorIsEquality method
        pass

    def equalsNotOnLiterals(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement equalsNotOnLiterals method
        pass

class javaMM_ArrayLengthAccess(Expression):

    pass
class javaMM_AbstractTypeQualifiedExpression(Expression):

    pass
class javaMM_TypeAccess(NamespaceAccess, Expression):

    pass
class javaMM_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, SingleVariableDeclaration: "javaMM_AbstractMethodDeclaration" = None, SingleVariableDeclaration100: "javaMM_CatchClause" = None, SingleVariableDeclaration152: "javaMM_EnhancedForStatement" = None, SingleVariableDeclaration253: "javaMM_Modifier" = None, singleVariableDeclaration: "javaMM_Modifier" = None, javaMM_SingleVariableDeclaration: "javaMM_TypeAccess" = None, javaMM_SingleVariableDeclaration298: set["javaMM_Annotation"] = None, parameters: "javaMM_AbstractMethodDeclaration" = None, exception: "javaMM_CatchClause" = None, parameter: "javaMM_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration100 = SingleVariableDeclaration100
        self.SingleVariableDeclaration152 = SingleVariableDeclaration152
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.singleVariableDeclaration = singleVariableDeclaration
        self.javaMM_SingleVariableDeclaration = javaMM_SingleVariableDeclaration
        self.javaMM_SingleVariableDeclaration298 = javaMM_SingleVariableDeclaration298 if javaMM_SingleVariableDeclaration298 is not None else set()
        self.parameters = parameters
        self.exception = exception
        self.parameter = parameter
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def singleVariableDeclaration(self):
        return self.__singleVariableDeclaration

    @singleVariableDeclaration.setter
    def singleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__singleVariableDeclaration", None)
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
    def javaMM_SingleVariableDeclaration298(self):
        return self.__javaMM_SingleVariableDeclaration298

    @javaMM_SingleVariableDeclaration298.setter
    def javaMM_SingleVariableDeclaration298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__javaMM_SingleVariableDeclaration298", None)
        self.__javaMM_SingleVariableDeclaration298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Annotation299"):
                    opp_val = getattr(item, "javaMM_Annotation299", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Annotation299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Annotation299"):
                    opp_val = getattr(item, "javaMM_Annotation299", None)
                    
                    setattr(item, "javaMM_Annotation299", self)
                    

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__parameter", None)
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
    def javaMM_SingleVariableDeclaration(self):
        return self.__javaMM_SingleVariableDeclaration

    @javaMM_SingleVariableDeclaration.setter
    def javaMM_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__javaMM_SingleVariableDeclaration", None)
        self.__javaMM_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess296"):
                opp_val = getattr(old_value, "javaMM_TypeAccess296", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess296"):
                opp_val = getattr(value, "javaMM_TypeAccess296", None)
                setattr(value, "javaMM_TypeAccess296", self)

    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__exception", None)
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
    def SingleVariableDeclaration253(self):
        return self.__SingleVariableDeclaration253

    @SingleVariableDeclaration253.setter
    def SingleVariableDeclaration253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__SingleVariableDeclaration253", None)
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
    def SingleVariableDeclaration100(self):
        return self.__SingleVariableDeclaration100

    @SingleVariableDeclaration100.setter
    def SingleVariableDeclaration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__SingleVariableDeclaration100", None)
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
    def SingleVariableDeclaration(self):
        return self.__SingleVariableDeclaration

    @SingleVariableDeclaration.setter
    def SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__SingleVariableDeclaration", None)
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
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__parameters", None)
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
    def SingleVariableDeclaration152(self):
        return self.__SingleVariableDeclaration152

    @SingleVariableDeclaration152.setter
    def SingleVariableDeclaration152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_SingleVariableDeclaration__SingleVariableDeclaration152", None)
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

class javaMM_Block(Statement):

    def __init__(self, javaMM_Block: "javaMM_AbstractMethodDeclaration" = None, javaMM_Block92: set["javaMM_Statement"] = None, javaMM_Block102: "javaMM_CatchClause" = None, javaMM_Block194: "javaMM_Initializer" = None, javaMM_Block326: "javaMM_TryStatement" = None, javaMM_Block329: "javaMM_TryStatement" = None, javaMM_Block316: "javaMM_SynchronizedStatement" = None):
        self.javaMM_Block = javaMM_Block
        self.javaMM_Block92 = javaMM_Block92 if javaMM_Block92 is not None else set()
        self.javaMM_Block102 = javaMM_Block102
        self.javaMM_Block194 = javaMM_Block194
        self.javaMM_Block326 = javaMM_Block326
        self.javaMM_Block329 = javaMM_Block329
        self.javaMM_Block316 = javaMM_Block316
        
    @property
    def javaMM_Block316(self):
        return self.__javaMM_Block316

    @javaMM_Block316.setter
    def javaMM_Block316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block316", None)
        self.__javaMM_Block316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_SynchronizedStatement"):
                opp_val = getattr(old_value, "javaMM_SynchronizedStatement", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_SynchronizedStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_SynchronizedStatement"):
                opp_val = getattr(value, "javaMM_SynchronizedStatement", None)
                setattr(value, "javaMM_SynchronizedStatement", self)

    @property
    def javaMM_Block102(self):
        return self.__javaMM_Block102

    @javaMM_Block102.setter
    def javaMM_Block102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block102", None)
        self.__javaMM_Block102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_CatchClause"):
                opp_val = getattr(old_value, "javaMM_CatchClause", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_CatchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_CatchClause"):
                opp_val = getattr(value, "javaMM_CatchClause", None)
                setattr(value, "javaMM_CatchClause", self)

    @property
    def javaMM_Block(self):
        return self.__javaMM_Block

    @javaMM_Block.setter
    def javaMM_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block", None)
        self.__javaMM_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_AbstractMethodDeclaration"):
                opp_val = getattr(old_value, "javaMM_AbstractMethodDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_AbstractMethodDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_AbstractMethodDeclaration"):
                opp_val = getattr(value, "javaMM_AbstractMethodDeclaration", None)
                setattr(value, "javaMM_AbstractMethodDeclaration", self)

    @property
    def javaMM_Block194(self):
        return self.__javaMM_Block194

    @javaMM_Block194.setter
    def javaMM_Block194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block194", None)
        self.__javaMM_Block194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Initializer"):
                opp_val = getattr(old_value, "javaMM_Initializer", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Initializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Initializer"):
                opp_val = getattr(value, "javaMM_Initializer", None)
                setattr(value, "javaMM_Initializer", self)

    @property
    def javaMM_Block329(self):
        return self.__javaMM_Block329

    @javaMM_Block329.setter
    def javaMM_Block329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block329", None)
        self.__javaMM_Block329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TryStatement328"):
                opp_val = getattr(old_value, "javaMM_TryStatement328", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TryStatement328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TryStatement328"):
                opp_val = getattr(value, "javaMM_TryStatement328", None)
                setattr(value, "javaMM_TryStatement328", self)

    @property
    def javaMM_Block92(self):
        return self.__javaMM_Block92

    @javaMM_Block92.setter
    def javaMM_Block92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block92", None)
        self.__javaMM_Block92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Statement"):
                    opp_val = getattr(item, "javaMM_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Statement"):
                    opp_val = getattr(item, "javaMM_Statement", None)
                    
                    setattr(item, "javaMM_Statement", self)
                    

    @property
    def javaMM_Block326(self):
        return self.__javaMM_Block326

    @javaMM_Block326.setter
    def javaMM_Block326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Block__javaMM_Block326", None)
        self.__javaMM_Block326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TryStatement"):
                opp_val = getattr(old_value, "javaMM_TryStatement", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TryStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TryStatement"):
                opp_val = getattr(value, "javaMM_TryStatement", None)
                setattr(value, "javaMM_TryStatement", self)

    def emptyBlockIsDocumented(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement emptyBlockIsDocumented method
        pass

class javaMM_BodyDeclaration(NamedElement):

    pass
class Type:

    pass
class javaMM_ArrayType(Type):

    def __init__(self, dimensions: int, javaMM_ArrayType: "javaMM_TypeAccess" = None):
        self.dimensions = dimensions
        self.javaMM_ArrayType = javaMM_ArrayType
        
    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions

    @property
    def javaMM_ArrayType(self):
        return self.__javaMM_ArrayType

    @javaMM_ArrayType.setter
    def javaMM_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ArrayType__javaMM_ArrayType", None)
        self.__javaMM_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess79"):
                opp_val = getattr(old_value, "javaMM_TypeAccess79", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess79"):
                opp_val = getattr(value, "javaMM_TypeAccess79", None)
                setattr(value, "javaMM_TypeAccess79", self)

class javaMM_TypeParameter(Type):

    pass
class javaMM_PrimitiveType(Type):

    pass
class javaMM_WildCardType(Type):

    def __init__(self, upperBound: str, javaMM_WildCardType: "javaMM_TypeAccess" = None):
        self.upperBound = upperBound
        self.javaMM_WildCardType = javaMM_WildCardType
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def javaMM_WildCardType(self):
        return self.__javaMM_WildCardType

    @javaMM_WildCardType.setter
    def javaMM_WildCardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_WildCardType__javaMM_WildCardType", None)
        self.__javaMM_WildCardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess364"):
                opp_val = getattr(old_value, "javaMM_TypeAccess364", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess364"):
                opp_val = getattr(value, "javaMM_TypeAccess364", None)
                setattr(value, "javaMM_TypeAccess364", self)

class javaMM_UnresolvedType(UnresolvedItem, Type):

    pass
class javaMM_ParameterizedType(Type):

    pass
class ASTNode:

    pass
class javaMM_Expression(ASTNode):

    pass
class javaMM_Statement(ASTNode):

    pass
class javaMM_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: str, NamedElement: "javaMM_ImportDeclaration" = None, javaMM_NamedElement: "javaMM_MemberRef" = None, importedElement: set["javaMM_ImportDeclaration"] = None):
        self.name = name
        self.proxy = proxy
        self.NamedElement = NamedElement
        self.javaMM_NamedElement = javaMM_NamedElement
        self.importedElement = importedElement if importedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def proxy(self) -> str:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: str):
        self.__proxy = proxy

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_NamedElement__NamedElement", None)
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
        old_value = getattr(self, f"_javaMM_NamedElement__importedElement", None)
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
    def javaMM_NamedElement(self):
        return self.__javaMM_NamedElement

    @javaMM_NamedElement.setter
    def javaMM_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_NamedElement__javaMM_NamedElement", None)
        self.__javaMM_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_MemberRef"):
                opp_val = getattr(old_value, "javaMM_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_MemberRef"):
                opp_val = getattr(value, "javaMM_MemberRef", None)
                setattr(value, "javaMM_MemberRef", self)

class javaMM_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class javaMM_AbstractVariablesContainer(ASTNode):

    pass
class javaMM_MemberRef(ASTNode):

    pass
class javaMM_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: str, transient: str, volatile: str, native: str, strictfp: str, synchronized: str, Modifier: "javaMM_BodyDeclaration" = None, modifier252: "javaMM_SingleVariableDeclaration" = None, modifier255: "javaMM_VariableDeclarationStatement" = None, modifier257: "javaMM_VariableDeclarationExpression" = None, modifier: "javaMM_BodyDeclaration" = None, Modifier294: "javaMM_SingleVariableDeclaration" = None, Modifier360: "javaMM_VariableDeclarationStatement" = None, Modifier355: "javaMM_VariableDeclarationExpression" = None):
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
        self.modifier257 = modifier257
        self.modifier = modifier
        self.Modifier294 = Modifier294
        self.Modifier360 = Modifier360
        self.Modifier355 = Modifier355
        
    @property
    def native(self) -> str:
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def synchronized(self) -> str:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized

    @property
    def Modifier(self):
        return self.__Modifier

    @Modifier.setter
    def Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__Modifier", None)
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
    def Modifier360(self):
        return self.__Modifier360

    @Modifier360.setter
    def Modifier360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__Modifier360", None)
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
        old_value = getattr(self, f"_javaMM_Modifier__modifier257", None)
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
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__modifier", None)
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
    def Modifier355(self):
        return self.__Modifier355

    @Modifier355.setter
    def Modifier355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__Modifier355", None)
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
    def modifier255(self):
        return self.__modifier255

    @modifier255.setter
    def modifier255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__modifier255", None)
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
        old_value = getattr(self, f"_javaMM_Modifier__modifier252", None)
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
    def Modifier294(self):
        return self.__Modifier294

    @Modifier294.setter
    def Modifier294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Modifier__Modifier294", None)
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

    def isLocal(self) -> str:
        # TODO: Implement isLocal method
        pass

class javaMM_TagElement(ASTNode):

    def __init__(self, tagName: str, javaMM_TagElement: "javaMM_Javadoc" = None, javaMM_TagElement321: set["javaMM_ASTNode"] = None):
        self.tagName = tagName
        self.javaMM_TagElement = javaMM_TagElement
        self.javaMM_TagElement321 = javaMM_TagElement321 if javaMM_TagElement321 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def javaMM_TagElement321(self):
        return self.__javaMM_TagElement321

    @javaMM_TagElement321.setter
    def javaMM_TagElement321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_TagElement__javaMM_TagElement321", None)
        self.__javaMM_TagElement321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_ASTNode322"):
                    opp_val = getattr(item, "javaMM_ASTNode322", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_ASTNode322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_ASTNode322"):
                    opp_val = getattr(item, "javaMM_ASTNode322", None)
                    
                    setattr(item, "javaMM_ASTNode322", self)
                    

    @property
    def javaMM_TagElement(self):
        return self.__javaMM_TagElement

    @javaMM_TagElement.setter
    def javaMM_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_TagElement__javaMM_TagElement", None)
        self.__javaMM_TagElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Javadoc"):
                opp_val = getattr(old_value, "javaMM_Javadoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Javadoc"):
                opp_val = getattr(value, "javaMM_Javadoc", None)
                if opp_val is None:
                    setattr(value, "javaMM_Javadoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaMM_NamespaceAccess(ASTNode):

    pass
class javaMM_AnonymousClassDeclaration(ASTNode):

    pass
class javaMM_ImportDeclaration(ASTNode):

    def __init__(self, static: str, javaMM_ImportDeclaration: "javaMM_CompilationUnit" = None, usagesInImports: "javaMM_NamedElement" = None, ImportDeclaration: "javaMM_NamedElement" = None):
        self.static = static
        self.javaMM_ImportDeclaration = javaMM_ImportDeclaration
        self.usagesInImports = usagesInImports
        self.ImportDeclaration = ImportDeclaration
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def javaMM_ImportDeclaration(self):
        return self.__javaMM_ImportDeclaration

    @javaMM_ImportDeclaration.setter
    def javaMM_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ImportDeclaration__javaMM_ImportDeclaration", None)
        self.__javaMM_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_CompilationUnit132"):
                opp_val = getattr(old_value, "javaMM_CompilationUnit132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_CompilationUnit132"):
                opp_val = getattr(value, "javaMM_CompilationUnit132", None)
                if opp_val is None:
                    setattr(value, "javaMM_CompilationUnit132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ImportDeclaration(self):
        return self.__ImportDeclaration

    @ImportDeclaration.setter
    def ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ImportDeclaration__ImportDeclaration", None)
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
    def usagesInImports(self):
        return self.__usagesInImports

    @usagesInImports.setter
    def usagesInImports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_ImportDeclaration__usagesInImports", None)
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

class javaMM_MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: str, javaMM_MethodRefParameter: "javaMM_MethodRef" = None, javaMM_MethodRefParameter233: "javaMM_TypeAccess" = None):
        self.name = name
        self.varargs = varargs
        self.javaMM_MethodRefParameter = javaMM_MethodRefParameter
        self.javaMM_MethodRefParameter233 = javaMM_MethodRefParameter233
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaMM_MethodRefParameter(self):
        return self.__javaMM_MethodRefParameter

    @javaMM_MethodRefParameter.setter
    def javaMM_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodRefParameter__javaMM_MethodRefParameter", None)
        self.__javaMM_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_MethodRef231"):
                opp_val = getattr(old_value, "javaMM_MethodRef231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_MethodRef231"):
                opp_val = getattr(value, "javaMM_MethodRef231", None)
                if opp_val is None:
                    setattr(value, "javaMM_MethodRef231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_MethodRefParameter233(self):
        return self.__javaMM_MethodRefParameter233

    @javaMM_MethodRefParameter233.setter
    def javaMM_MethodRefParameter233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_MethodRefParameter__javaMM_MethodRefParameter233", None)
        self.__javaMM_MethodRefParameter233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeAccess234"):
                opp_val = getattr(old_value, "javaMM_TypeAccess234", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeAccess234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeAccess234"):
                opp_val = getattr(value, "javaMM_TypeAccess234", None)
                setattr(value, "javaMM_TypeAccess234", self)

class javaMM_Comment(ASTNode):

    def __init__(self, content: str, enclosedByParent: str, prefixOfParent: str, javaMM_Comment: "javaMM_AbstractTypeDeclaration" = None, javaMM_Comment18: "javaMM_AbstractTypeDeclaration" = None, javaMM_Comment41: "javaMM_ASTNode" = None, javaMM_Comment130: "javaMM_CompilationUnit" = None):
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.javaMM_Comment = javaMM_Comment
        self.javaMM_Comment18 = javaMM_Comment18
        self.javaMM_Comment41 = javaMM_Comment41
        self.javaMM_Comment130 = javaMM_Comment130
        
    @property
    def prefixOfParent(self) -> str:
        return self.__prefixOfParent

    @prefixOfParent.setter
    def prefixOfParent(self, prefixOfParent: str):
        self.__prefixOfParent = prefixOfParent

    @property
    def enclosedByParent(self) -> str:
        return self.__enclosedByParent

    @enclosedByParent.setter
    def enclosedByParent(self, enclosedByParent: str):
        self.__enclosedByParent = enclosedByParent

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def javaMM_Comment41(self):
        return self.__javaMM_Comment41

    @javaMM_Comment41.setter
    def javaMM_Comment41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Comment__javaMM_Comment41", None)
        self.__javaMM_Comment41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ASTNode"):
                opp_val = getattr(old_value, "javaMM_ASTNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ASTNode"):
                opp_val = getattr(value, "javaMM_ASTNode", None)
                if opp_val is None:
                    setattr(value, "javaMM_ASTNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_Comment130(self):
        return self.__javaMM_Comment130

    @javaMM_Comment130.setter
    def javaMM_Comment130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Comment__javaMM_Comment130", None)
        self.__javaMM_Comment130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_CompilationUnit129"):
                opp_val = getattr(old_value, "javaMM_CompilationUnit129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_CompilationUnit129"):
                opp_val = getattr(value, "javaMM_CompilationUnit129", None)
                if opp_val is None:
                    setattr(value, "javaMM_CompilationUnit129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_Comment18(self):
        return self.__javaMM_Comment18

    @javaMM_Comment18.setter
    def javaMM_Comment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Comment__javaMM_Comment18", None)
        self.__javaMM_Comment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_AbstractTypeDeclaration17"):
                opp_val = getattr(old_value, "javaMM_AbstractTypeDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_AbstractTypeDeclaration17"):
                opp_val = getattr(value, "javaMM_AbstractTypeDeclaration17", None)
                if opp_val is None:
                    setattr(value, "javaMM_AbstractTypeDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_Comment(self):
        return self.__javaMM_Comment

    @javaMM_Comment.setter
    def javaMM_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_Comment__javaMM_Comment", None)
        self.__javaMM_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "javaMM_AbstractTypeDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_AbstractTypeDeclaration"):
                opp_val = getattr(value, "javaMM_AbstractTypeDeclaration", None)
                if opp_val is None:
                    setattr(value, "javaMM_AbstractTypeDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaMM_AbstractMethodInvocation(ASTNode):

    pass
class javaMM_MethodRef(ASTNode):

    pass
class BodyDeclaration:

    pass
class javaMM_Initializer(BodyDeclaration):

    pass
class javaMM_AbstractTypeDeclaration(Type, BodyDeclaration):

    def __init__(self, abstractTypeDeclaration: set["javaMM_BodyDeclaration"] = None, ownedElements: "javaMM_Package" = None, javaMM_AbstractTypeDeclaration21: set["javaMM_TypeAccess"] = None, javaMM_AbstractTypeDeclaration: set["javaMM_Comment"] = None, javaMM_AbstractTypeDeclaration17: set["javaMM_Comment"] = None, AbstractTypeDeclaration: "javaMM_BodyDeclaration" = None, javaMM_AbstractTypeDeclaration105: "javaMM_ClassFile" = None, javaMM_AbstractTypeDeclaration138: "javaMM_CompilationUnit" = None, AbstractTypeDeclaration260: "javaMM_Package" = None, javaMM_AbstractTypeDeclaration340: "javaMM_TypeDeclarationStatement" = None):
        self.abstractTypeDeclaration = abstractTypeDeclaration if abstractTypeDeclaration is not None else set()
        self.ownedElements = ownedElements
        self.javaMM_AbstractTypeDeclaration21 = javaMM_AbstractTypeDeclaration21 if javaMM_AbstractTypeDeclaration21 is not None else set()
        self.javaMM_AbstractTypeDeclaration = javaMM_AbstractTypeDeclaration if javaMM_AbstractTypeDeclaration is not None else set()
        self.javaMM_AbstractTypeDeclaration17 = javaMM_AbstractTypeDeclaration17 if javaMM_AbstractTypeDeclaration17 is not None else set()
        self.AbstractTypeDeclaration = AbstractTypeDeclaration
        self.javaMM_AbstractTypeDeclaration105 = javaMM_AbstractTypeDeclaration105
        self.javaMM_AbstractTypeDeclaration138 = javaMM_AbstractTypeDeclaration138
        self.AbstractTypeDeclaration260 = AbstractTypeDeclaration260
        self.javaMM_AbstractTypeDeclaration340 = javaMM_AbstractTypeDeclaration340
        
    @property
    def javaMM_AbstractTypeDeclaration105(self):
        return self.__javaMM_AbstractTypeDeclaration105

    @javaMM_AbstractTypeDeclaration105.setter
    def javaMM_AbstractTypeDeclaration105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration105", None)
        self.__javaMM_AbstractTypeDeclaration105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_ClassFile104"):
                opp_val = getattr(old_value, "javaMM_ClassFile104", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_ClassFile104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_ClassFile104"):
                opp_val = getattr(value, "javaMM_ClassFile104", None)
                setattr(value, "javaMM_ClassFile104", self)

    @property
    def javaMM_AbstractTypeDeclaration340(self):
        return self.__javaMM_AbstractTypeDeclaration340

    @javaMM_AbstractTypeDeclaration340.setter
    def javaMM_AbstractTypeDeclaration340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration340", None)
        self.__javaMM_AbstractTypeDeclaration340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_TypeDeclarationStatement"):
                opp_val = getattr(old_value, "javaMM_TypeDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_TypeDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_TypeDeclarationStatement"):
                opp_val = getattr(value, "javaMM_TypeDeclarationStatement", None)
                setattr(value, "javaMM_TypeDeclarationStatement", self)

    @property
    def AbstractTypeDeclaration(self):
        return self.__AbstractTypeDeclaration

    @AbstractTypeDeclaration.setter
    def AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__AbstractTypeDeclaration", None)
        self.__AbstractTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bodyDeclarations"):
                opp_val = getattr(old_value, "bodyDeclarations", None)
                if opp_val == self:
                    setattr(old_value, "bodyDeclarations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bodyDeclarations"):
                opp_val = getattr(value, "bodyDeclarations", None)
                setattr(value, "bodyDeclarations", self)

    @property
    def javaMM_AbstractTypeDeclaration17(self):
        return self.__javaMM_AbstractTypeDeclaration17

    @javaMM_AbstractTypeDeclaration17.setter
    def javaMM_AbstractTypeDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration17", None)
        self.__javaMM_AbstractTypeDeclaration17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Comment18"):
                    opp_val = getattr(item, "javaMM_Comment18", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Comment18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Comment18"):
                    opp_val = getattr(item, "javaMM_Comment18", None)
                    
                    setattr(item, "javaMM_Comment18", self)
                    

    @property
    def ownedElements(self):
        return self.__ownedElements

    @ownedElements.setter
    def ownedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__ownedElements", None)
        self.__ownedElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def javaMM_AbstractTypeDeclaration21(self):
        return self.__javaMM_AbstractTypeDeclaration21

    @javaMM_AbstractTypeDeclaration21.setter
    def javaMM_AbstractTypeDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration21", None)
        self.__javaMM_AbstractTypeDeclaration21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_TypeAccess22"):
                    opp_val = getattr(item, "javaMM_TypeAccess22", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_TypeAccess22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_TypeAccess22"):
                    opp_val = getattr(item, "javaMM_TypeAccess22", None)
                    
                    setattr(item, "javaMM_TypeAccess22", self)
                    

    @property
    def javaMM_AbstractTypeDeclaration(self):
        return self.__javaMM_AbstractTypeDeclaration

    @javaMM_AbstractTypeDeclaration.setter
    def javaMM_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration", None)
        self.__javaMM_AbstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_Comment"):
                    opp_val = getattr(item, "javaMM_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_Comment"):
                    opp_val = getattr(item, "javaMM_Comment", None)
                    
                    setattr(item, "javaMM_Comment", self)
                    

    @property
    def AbstractTypeDeclaration260(self):
        return self.__AbstractTypeDeclaration260

    @AbstractTypeDeclaration260.setter
    def AbstractTypeDeclaration260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__AbstractTypeDeclaration260", None)
        self.__AbstractTypeDeclaration260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaMM_AbstractTypeDeclaration138(self):
        return self.__javaMM_AbstractTypeDeclaration138

    @javaMM_AbstractTypeDeclaration138.setter
    def javaMM_AbstractTypeDeclaration138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__javaMM_AbstractTypeDeclaration138", None)
        self.__javaMM_AbstractTypeDeclaration138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_CompilationUnit137"):
                opp_val = getattr(old_value, "javaMM_CompilationUnit137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_CompilationUnit137"):
                opp_val = getattr(value, "javaMM_CompilationUnit137", None)
                if opp_val is None:
                    setattr(value, "javaMM_CompilationUnit137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abstractTypeDeclaration(self):
        return self.__abstractTypeDeclaration

    @abstractTypeDeclaration.setter
    def abstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractTypeDeclaration__abstractTypeDeclaration", None)
        self.__abstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BodyDeclaration"):
                    opp_val = getattr(item, "BodyDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "BodyDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BodyDeclaration"):
                    opp_val = getattr(item, "BodyDeclaration", None)
                    
                    setattr(item, "BodyDeclaration", self)
                    

    def implements(self, type: str) -> str:
        # TODO: Implement implements method
        pass

class javaMM_FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass
class javaMM_EnumConstantDeclaration(VariableDeclaration, BodyDeclaration):

    pass
class javaMM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class javaMM_AbstractMethodDeclaration(BodyDeclaration):

    def __init__(self, method: set["javaMM_MethodRef"] = None, method8: set["javaMM_AbstractMethodInvocation"] = None, AbstractMethodDeclaration: "javaMM_AbstractMethodInvocation" = None, javaMM_AbstractMethodDeclaration: "javaMM_Block" = None, methodDeclaration: set["javaMM_SingleVariableDeclaration"] = None, javaMM_AbstractMethodDeclaration3: set["javaMM_TypeAccess"] = None, javaMM_AbstractMethodDeclaration5: set["javaMM_TypeParameter"] = None, AbstractMethodDeclaration227: "javaMM_MethodRef" = None, AbstractMethodDeclaration301: "javaMM_SingleVariableDeclaration" = None):
        self.method = method if method is not None else set()
        self.method8 = method8 if method8 is not None else set()
        self.AbstractMethodDeclaration = AbstractMethodDeclaration
        self.javaMM_AbstractMethodDeclaration = javaMM_AbstractMethodDeclaration
        self.methodDeclaration = methodDeclaration if methodDeclaration is not None else set()
        self.javaMM_AbstractMethodDeclaration3 = javaMM_AbstractMethodDeclaration3 if javaMM_AbstractMethodDeclaration3 is not None else set()
        self.javaMM_AbstractMethodDeclaration5 = javaMM_AbstractMethodDeclaration5 if javaMM_AbstractMethodDeclaration5 is not None else set()
        self.AbstractMethodDeclaration227 = AbstractMethodDeclaration227
        self.AbstractMethodDeclaration301 = AbstractMethodDeclaration301
        
    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__method", None)
        self.__method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodRef"):
                    opp_val = getattr(item, "MethodRef", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodRef"):
                    opp_val = getattr(item, "MethodRef", None)
                    
                    setattr(item, "MethodRef", self)
                    

    @property
    def AbstractMethodDeclaration(self):
        return self.__AbstractMethodDeclaration

    @AbstractMethodDeclaration.setter
    def AbstractMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__AbstractMethodDeclaration", None)
        self.__AbstractMethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usages"):
                opp_val = getattr(old_value, "usages", None)
                if opp_val == self:
                    setattr(old_value, "usages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usages"):
                opp_val = getattr(value, "usages", None)
                setattr(value, "usages", self)

    @property
    def javaMM_AbstractMethodDeclaration3(self):
        return self.__javaMM_AbstractMethodDeclaration3

    @javaMM_AbstractMethodDeclaration3.setter
    def javaMM_AbstractMethodDeclaration3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__javaMM_AbstractMethodDeclaration3", None)
        self.__javaMM_AbstractMethodDeclaration3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_TypeAccess"):
                    opp_val = getattr(item, "javaMM_TypeAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_TypeAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_TypeAccess"):
                    opp_val = getattr(item, "javaMM_TypeAccess", None)
                    
                    setattr(item, "javaMM_TypeAccess", self)
                    

    @property
    def AbstractMethodDeclaration227(self):
        return self.__AbstractMethodDeclaration227

    @AbstractMethodDeclaration227.setter
    def AbstractMethodDeclaration227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__AbstractMethodDeclaration227", None)
        self.__AbstractMethodDeclaration227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usagesInDocComments"):
                opp_val = getattr(old_value, "usagesInDocComments", None)
                if opp_val == self:
                    setattr(old_value, "usagesInDocComments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usagesInDocComments"):
                opp_val = getattr(value, "usagesInDocComments", None)
                setattr(value, "usagesInDocComments", self)

    @property
    def javaMM_AbstractMethodDeclaration(self):
        return self.__javaMM_AbstractMethodDeclaration

    @javaMM_AbstractMethodDeclaration.setter
    def javaMM_AbstractMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__javaMM_AbstractMethodDeclaration", None)
        self.__javaMM_AbstractMethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaMM_Block"):
                opp_val = getattr(old_value, "javaMM_Block", None)
                if opp_val == self:
                    setattr(old_value, "javaMM_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaMM_Block"):
                opp_val = getattr(value, "javaMM_Block", None)
                setattr(value, "javaMM_Block", self)

    @property
    def javaMM_AbstractMethodDeclaration5(self):
        return self.__javaMM_AbstractMethodDeclaration5

    @javaMM_AbstractMethodDeclaration5.setter
    def javaMM_AbstractMethodDeclaration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__javaMM_AbstractMethodDeclaration5", None)
        self.__javaMM_AbstractMethodDeclaration5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaMM_TypeParameter"):
                    opp_val = getattr(item, "javaMM_TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "javaMM_TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaMM_TypeParameter"):
                    opp_val = getattr(item, "javaMM_TypeParameter", None)
                    
                    setattr(item, "javaMM_TypeParameter", self)
                    

    @property
    def methodDeclaration(self):
        return self.__methodDeclaration

    @methodDeclaration.setter
    def methodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__methodDeclaration", None)
        self.__methodDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableDeclaration"):
                    opp_val = getattr(item, "SingleVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableDeclaration"):
                    opp_val = getattr(item, "SingleVariableDeclaration", None)
                    
                    setattr(item, "SingleVariableDeclaration", self)
                    

    @property
    def method8(self):
        return self.__method8

    @method8.setter
    def method8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__method8", None)
        self.__method8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractMethodInvocation"):
                    opp_val = getattr(item, "AbstractMethodInvocation", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractMethodInvocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractMethodInvocation"):
                    opp_val = getattr(item, "AbstractMethodInvocation", None)
                    
                    setattr(item, "AbstractMethodInvocation", self)
                    

    @property
    def AbstractMethodDeclaration301(self):
        return self.__AbstractMethodDeclaration301

    @AbstractMethodDeclaration301.setter
    def AbstractMethodDeclaration301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMM_AbstractMethodDeclaration__AbstractMethodDeclaration301", None)
        self.__AbstractMethodDeclaration301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    def parametersEffectivelyFinal(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement parametersEffectivelyFinal method
        pass

    def localMethodIsUsed(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement localMethodIsUsed method
        pass
