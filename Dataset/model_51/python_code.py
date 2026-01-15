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
    CONDITIONAL_OR = "CONDITIONAL_OR"
    OR = "OR"
    CONDITIONAL_AND = "CONDITIONAL_AND"
class PostfixExpressionKind(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class AssignmentKind(Enum):
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    DIVIDE_ASSIGN = "DIVIDE_ASSIGN"
    BIT_AND_ASSIGN = "BIT_AND_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"
    LEFT_SHIFT_ASSIGN = "LEFT_SHIFT_ASSIGN"
    RIGHT_SHIFT_SIGNED_ASSIGN = "RIGHT_SHIFT_SIGNED_ASSIGN"
    RIGHT_SHIFT_UNSIGNED_ASSIGN = "RIGHT_SHIFT_UNSIGNED_ASSIGN"
    BIT_OR_ASSIGN = "BIT_OR_ASSIGN"
    BIT_XOR_ASSIGN = "BIT_XOR_ASSIGN"
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    final = "final"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"


############################################
# Definition of Classes
############################################

class InterfaceDeclaration:

    pass
class EnumDeclaration:

    pass
class VariableDeclarationFragment:

    pass
class SingleVariableDeclaration:

    pass
class MethodDeclaration:

    pass
class LabeledStatement:

    pass
class ClassDeclaration:

    pass
class AnnotationTypeMemberDeclaration:

    pass
class UnresolvedItem:

    pass
class javaMM_UnresolvedLabeledStatement(UnresolvedItem, LabeledStatement):

    pass
class javaMM_UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class javaMM_UnresolvedEnumDeclaration(UnresolvedItem, EnumDeclaration):

    pass
class javaMM_UnresolvedAnnotationTypeMemberDeclaration(UnresolvedItem, AnnotationTypeMemberDeclaration):

    pass
class javaMM_UnresolvedClassDeclaration(UnresolvedItem, ClassDeclaration):

    pass
class javaMM_UnresolvedVariableDeclarationFragment(UnresolvedItem, VariableDeclarationFragment):

    pass
class javaMM_UnresolvedMethodDeclaration(MethodDeclaration, UnresolvedItem):

    pass
class javaMM_UnresolvedInterfaceDeclaration(UnresolvedItem, InterfaceDeclaration):

    pass
class AnnotationTypeDeclaration:

    pass
class javaMM_UnresolvedAnnotationDeclaration(UnresolvedItem, AnnotationTypeDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class javaMM_ThisExpression(AbstractTypeQualifiedExpression):

    pass
class javaMM_SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class PrimitiveType:

    pass
class javaMM_PrimitiveTypeFloat(PrimitiveType):

    pass
class javaMM_PrimitiveTypeShort(PrimitiveType):

    pass
class javaMM_PrimitiveTypeVoid(PrimitiveType):

    pass
class javaMM_PrimitiveTypeLong(PrimitiveType):

    pass
class javaMM_PrimitiveTypeByte(PrimitiveType):

    pass
class javaMM_PrimitiveTypeInt(PrimitiveType):

    pass
class javaMM_PrimitiveTypeDouble(PrimitiveType):

    pass
class javaMM_PrimitiveTypeChar(PrimitiveType):

    pass
class javaMM_PrimitiveTypeBoolean(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class javaMM_PackageAccess(NamespaceAccess):

    pass
class javaMM_Model:

    def __init__(self, name: str, javaMM_Model247: set["javaMM_Archive"] = None, model: set["javaMM_Package"] = None, javaMM_Model: set["javaMM_Type"] = None, javaMM_Model239: set["javaMM_UnresolvedItem"] = None, javaMM_Model241: set["javaMM_CompilationUnit"] = None, javaMM_Model244: set["javaMM_ClassFile"] = None, Model: "javaMM_Package" = None):
        self.name = name
        self.javaMM_Model247 = javaMM_Model247 if javaMM_Model247 is not None else set()
        self.model = model if model is not None else set()
        self.javaMM_Model = javaMM_Model if javaMM_Model is not None else set()
        self.javaMM_Model239 = javaMM_Model239 if javaMM_Model239 is not None else set()
        self.javaMM_Model241 = javaMM_Model241 if javaMM_Model241 is not None else set()
        self.javaMM_Model244 = javaMM_Model244 if javaMM_Model244 is not None else set()
        self.Model = Model
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class javaMM_ManifestEntry:

    def __init__(self, name: str, javaMM_ManifestEntry211: set["javaMM_ManifestAttribute"] = None, javaMM_ManifestEntry: "javaMM_Manifest" = None):
        self.name = name
        self.javaMM_ManifestEntry211 = javaMM_ManifestEntry211 if javaMM_ManifestEntry211 is not None else set()
        self.javaMM_ManifestEntry = javaMM_ManifestEntry
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class javaMM_ManifestAttribute:

    def __init__(self, key: str, value: str, javaMM_ManifestAttribute212: "javaMM_ManifestEntry" = None, javaMM_ManifestAttribute: "javaMM_Manifest" = None):
        self.key = key
        self.value = value
        self.javaMM_ManifestAttribute212 = javaMM_ManifestAttribute212
        self.javaMM_ManifestAttribute = javaMM_ManifestAttribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

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
                    

class javaMM_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class javaMM_SuperMethodInvocation(AbstractMethodInvocation, AbstractTypeQualifiedExpression):

    pass
class Comment:

    pass
class javaMM_LineComment(Comment):

    pass
class javaMM_Javadoc(Comment):

    pass
class javaMM_BlockComment(Comment):

    pass
class javaMM_ASTNode(ABC):

    pass
class Statement:

    pass
class javaMM_BreakStatement(Statement):

    pass
class javaMM_ForStatement(Statement):

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

class javaMM_ReturnStatement(Statement):

    pass
class javaMM_IfStatement(Statement):

    pass
class javaMM_ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class javaMM_CatchClause(Statement):

    pass
class javaMM_ThrowStatement(Statement):

    pass
class javaMM_SwitchCase(Statement):

    def __init__(self, default: bool, javaMM_SwitchCase: "javaMM_Expression" = None):
        self.default = default
        self.javaMM_SwitchCase = javaMM_SwitchCase
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
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

class javaMM_SwitchStatement(Statement):

    pass
class javaMM_SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class javaMM_WhileStatement(Statement):

    pass
class javaMM_ContinueStatement(Statement):

    pass
class javaMM_TypeDeclarationStatement(Statement):

    pass
class javaMM_EnhancedForStatement(Statement):

    pass
class javaMM_ExpressionStatement(Statement):

    pass
class javaMM_DoStatement(Statement):

    pass
class javaMM_EmptyStatement(Statement):

    pass
class javaMM_SynchronizedStatement(Statement):

    pass
class javaMM_TryStatement(Statement):

    pass
class javaMM_AssertStatement(Statement):

    pass
class javaMM_Manifest:

    pass
class NamedElement:

    pass
class javaMM_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, VariableDeclaration: "javaMM_SingleVariableAccess" = None, javaMM_VariableDeclaration: "javaMM_Expression" = None, variable: set["javaMM_SingleVariableAccess"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclaration = VariableDeclaration
        self.javaMM_VariableDeclaration = javaMM_VariableDeclaration
        self.variable = variable if variable is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

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

class javaMM_UnresolvedItem(NamedElement):

    pass
class javaMM_LabeledStatement(Statement, NamedElement):

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
                    

class javaMM_Type(NamedElement):

    pass
class javaMM_Archive(NamedElement):

    def __init__(self, originalFilePath: str, javaMM_Archive: set["javaMM_ClassFile"] = None, javaMM_Archive34: "javaMM_Manifest" = None, javaMM_Archive248: "javaMM_Model" = None):
        self.originalFilePath = originalFilePath
        self.javaMM_Archive = javaMM_Archive if javaMM_Archive is not None else set()
        self.javaMM_Archive34 = javaMM_Archive34
        self.javaMM_Archive248 = javaMM_Archive248
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

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

class javaMM_AnnotationMemberValuePair(NamedElement):

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
class Expression:

    pass
class javaMM_MethodInvocation(AbstractMethodInvocation, Expression):

    pass
class javaMM_FieldAccess(Expression):

    pass
class javaMM_ArrayLengthAccess(Expression):

    pass
class javaMM_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class javaMM_UnresolvedItemAccess(Expression, NamespaceAccess):

    pass
class javaMM_ArrayCreation(Expression):

    pass
class javaMM_CastExpression(Expression):

    pass
class javaMM_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

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

class javaMM_VariableDeclarationExpression(Expression, AbstractVariablesContainer):

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

class javaMM_ArrayInitializer(Expression):

    pass
class javaMM_ArrayAccess(Expression):

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

class javaMM_InstanceofExpression(Expression):

    pass
class javaMM_ConditionalExpression(Expression):

    pass
class javaMM_ClassInstanceCreation(AbstractMethodInvocation, Expression):

    pass
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

class javaMM_NullLiteral(Expression):

    pass
class javaMM_ParenthesizedExpression(Expression):

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

class javaMM_TypeLiteral(Expression):

    pass
class javaMM_SingleVariableAccess(Expression):

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

class javaMM_AbstractTypeQualifiedExpression(Expression):

    pass
class javaMM_Package(NamedElement):

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

class javaMM_UnresolvedType(UnresolvedItem, Type):

    pass
class javaMM_PrimitiveType(Type):

    pass
class javaMM_WildCardType(Type):

    def __init__(self, upperBound: bool, javaMM_WildCardType: "javaMM_TypeAccess" = None):
        self.upperBound = upperBound
        self.javaMM_WildCardType = javaMM_WildCardType
        
    @property
    def upperBound(self) -> bool:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: bool):
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

class javaMM_ParameterizedType(Type):

    pass
class javaMM_Annotation(Expression):

    pass
class javaMM_VariableDeclarationFragment(VariableDeclaration):

    pass
class javaMM_TypeParameter(Type):

    pass
class javaMM_TypeAccess(Expression, NamespaceAccess):

    pass
class javaMM_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "javaMM_AbstractMethodDeclaration" = None, SingleVariableDeclaration100: "javaMM_CatchClause" = None, SingleVariableDeclaration152: "javaMM_EnhancedForStatement" = None, SingleVariableDeclaration253: "javaMM_Modifier" = None, exception: "javaMM_CatchClause" = None, parameter: "javaMM_EnhancedForStatement" = None, singleVariableDeclaration: "javaMM_Modifier" = None, javaMM_SingleVariableDeclaration: "javaMM_TypeAccess" = None, javaMM_SingleVariableDeclaration298: set["javaMM_Annotation"] = None, parameters: "javaMM_AbstractMethodDeclaration" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration100 = SingleVariableDeclaration100
        self.SingleVariableDeclaration152 = SingleVariableDeclaration152
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.exception = exception
        self.parameter = parameter
        self.singleVariableDeclaration = singleVariableDeclaration
        self.javaMM_SingleVariableDeclaration = javaMM_SingleVariableDeclaration
        self.javaMM_SingleVariableDeclaration298 = javaMM_SingleVariableDeclaration298 if javaMM_SingleVariableDeclaration298 is not None else set()
        self.parameters = parameters
        
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

class javaMM_Block(Statement):

    pass
class BodyDeclaration:

    pass
class javaMM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class javaMM_EnumConstantDeclaration(VariableDeclaration, BodyDeclaration):

    pass
class javaMM_AbstractTypeDeclaration(Type, BodyDeclaration):

    pass
class javaMM_FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass
class javaMM_Initializer(BodyDeclaration):

    pass
class javaMM_AbstractMethodDeclaration(BodyDeclaration):

    pass
class ASTNode:

    pass
class javaMM_Expression(ASTNode):

    pass
class javaMM_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "javaMM_BodyDeclaration" = None, modifier: "javaMM_BodyDeclaration" = None, modifier252: "javaMM_SingleVariableDeclaration" = None, modifier255: "javaMM_VariableDeclarationStatement" = None, modifier257: "javaMM_VariableDeclarationExpression" = None, Modifier294: "javaMM_SingleVariableDeclaration" = None, Modifier360: "javaMM_VariableDeclarationStatement" = None, Modifier355: "javaMM_VariableDeclarationExpression" = None):
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
        self.Modifier360 = Modifier360
        self.Modifier355 = Modifier355
        
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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

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

class javaMM_AnonymousClassDeclaration(ASTNode):

    pass
class javaMM_MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: bool, javaMM_MethodRefParameter: "javaMM_MethodRef" = None, javaMM_MethodRefParameter233: "javaMM_TypeAccess" = None):
        self.name = name
        self.varargs = varargs
        self.javaMM_MethodRefParameter = javaMM_MethodRefParameter
        self.javaMM_MethodRefParameter233 = javaMM_MethodRefParameter233
        
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

class javaMM_AbstractVariablesContainer(ASTNode):

    pass
class javaMM_Statement(ASTNode):

    pass
class javaMM_MethodRef(ASTNode):

    pass
class javaMM_NamespaceAccess(ASTNode):

    pass
class javaMM_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, NamedElement: "javaMM_ImportDeclaration" = None, javaMM_NamedElement: "javaMM_MemberRef" = None, importedElement: set["javaMM_ImportDeclaration"] = None):
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
    def proxy(self) -> bool:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy

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
                    

class javaMM_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, javaMM_ImportDeclaration: "javaMM_CompilationUnit" = None, usagesInImports: "javaMM_NamedElement" = None, ImportDeclaration: "javaMM_NamedElement" = None):
        self.static = static
        self.javaMM_ImportDeclaration = javaMM_ImportDeclaration
        self.usagesInImports = usagesInImports
        self.ImportDeclaration = ImportDeclaration
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
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

class javaMM_AbstractMethodInvocation(ASTNode):

    pass
class javaMM_Comment(ASTNode):

    def __init__(self, content: str, enclosedByParent: bool, prefixOfParent: bool, javaMM_Comment: "javaMM_AbstractTypeDeclaration" = None, javaMM_Comment18: "javaMM_AbstractTypeDeclaration" = None, javaMM_Comment41: "javaMM_ASTNode" = None, javaMM_Comment130: "javaMM_CompilationUnit" = None):
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.javaMM_Comment = javaMM_Comment
        self.javaMM_Comment18 = javaMM_Comment18
        self.javaMM_Comment41 = javaMM_Comment41
        self.javaMM_Comment130 = javaMM_Comment130
        
    @property
    def enclosedByParent(self) -> bool:
        return self.__enclosedByParent

    @enclosedByParent.setter
    def enclosedByParent(self, enclosedByParent: bool):
        self.__enclosedByParent = enclosedByParent

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

class javaMM_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class javaMM_MemberRef(ASTNode):

    pass