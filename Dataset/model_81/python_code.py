from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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

class java__QueryCollection:

    def __init__(self):
        
    def grabats09(self) -> TypeDeclaration:
        # TODO: Implement grabats09 method
        pass

    def thrownExceptions(self) -> BodyDeclaration:
        # TODO: Implement thrownExceptions method
        pass

    def textElementInJavadoc(self, self_: str) -> ASTNode:
        # TODO: Implement textElementInJavadoc method
        pass

    def emptyTextElementInJavadoc(self, self_: str) -> ASTNode:
        # TODO: Implement emptyTextElementInJavadoc method
        pass

    def invisibleMethods(self) -> BodyDeclaration:
        # TODO: Implement invisibleMethods method
        pass

class VariableDeclarationFragment:

    pass
class MethodDeclaration:

    pass
class LabeledStatement:

    pass
class InterfaceDeclaration:

    pass
class EnumDeclaration:

    pass
class SingleVariableDeclaration:

    pass
class ClassDeclaration:

    pass
class AnnotationTypeMemberDeclaration:

    pass
class UnresolvedItem:

    pass
class java__UnresolvedInterfaceDeclaration(InterfaceDeclaration, UnresolvedItem):

    pass
class java__UnresolvedSingleVariableDeclaration(UnresolvedItem, SingleVariableDeclaration):

    pass
class java__UnresolvedEnumDeclaration(EnumDeclaration, UnresolvedItem):

    pass
class java__UnresolvedMethodDeclaration(UnresolvedItem, MethodDeclaration):

    pass
class java__UnresolvedLabeledStatement(LabeledStatement, UnresolvedItem):

    pass
class java__UnresolvedClassDeclaration(ClassDeclaration, UnresolvedItem):

    pass
class java__UnresolvedVariableDeclarationFragment(UnresolvedItem, VariableDeclarationFragment):

    pass
class java__UnresolvedAnnotationTypeMemberDeclaration(AnnotationTypeMemberDeclaration, UnresolvedItem):

    pass
class AnnotationTypeDeclaration:

    pass
class java__UnresolvedAnnotationDeclaration(UnresolvedItem, AnnotationTypeDeclaration):

    pass
class AbstractTypeQualifiedExpression:

    pass
class java__ThisExpression(AbstractTypeQualifiedExpression):

    pass
class java__SuperFieldAccess(AbstractTypeQualifiedExpression):

    pass
class PrimitiveType:

    pass
class java__PrimitiveTypeShort(PrimitiveType):

    pass
class java__PrimitiveTypeChar(PrimitiveType):

    pass
class java__PrimitiveTypeDouble(PrimitiveType):

    pass
class java__PrimitiveTypeByte(PrimitiveType):

    pass
class java__PrimitiveTypeBoolean(PrimitiveType):

    pass
class java__PrimitiveTypeVoid(PrimitiveType):

    pass
class java__PrimitiveTypeLong(PrimitiveType):

    pass
class java__PrimitiveTypeInt(PrimitiveType):

    pass
class java__PrimitiveTypeFloat(PrimitiveType):

    pass
class NamespaceAccess:

    pass
class java__PackageAccess(NamespaceAccess):

    pass
class java__Model:

    def __init__(self, name: str, java__Model: set["java__Type"] = None, java__Model239: set["java__UnresolvedItem"] = None, java__Model241: set["java__CompilationUnit"] = None, java__Model244: set["java__ClassFile"] = None, java__Model247: set["java__Archive"] = None, model: set["java__Package"] = None, Model: "java__Package" = None):
        self.name = name
        self.java__Model = java__Model if java__Model is not None else set()
        self.java__Model239 = java__Model239 if java__Model239 is not None else set()
        self.java__Model241 = java__Model241 if java__Model241 is not None else set()
        self.java__Model244 = java__Model244 if java__Model244 is not None else set()
        self.java__Model247 = java__Model247 if java__Model247 is not None else set()
        self.model = model if model is not None else set()
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
        old_value = getattr(self, f"_java__Model__model", None)
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
    def java__Model247(self):
        return self.__java__Model247

    @java__Model247.setter
    def java__Model247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__java__Model247", None)
        self.__java__Model247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Archive248"):
                    opp_val = getattr(item, "java__Archive248", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Archive248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Archive248"):
                    opp_val = getattr(item, "java__Archive248", None)
                    
                    setattr(item, "java__Archive248", self)
                    

    @property
    def java__Model241(self):
        return self.__java__Model241

    @java__Model241.setter
    def java__Model241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__java__Model241", None)
        self.__java__Model241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__CompilationUnit242"):
                    opp_val = getattr(item, "java__CompilationUnit242", None)
                    
                    if opp_val == self:
                        setattr(item, "java__CompilationUnit242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__CompilationUnit242"):
                    opp_val = getattr(item, "java__CompilationUnit242", None)
                    
                    setattr(item, "java__CompilationUnit242", self)
                    

    @property
    def java__Model244(self):
        return self.__java__Model244

    @java__Model244.setter
    def java__Model244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__java__Model244", None)
        self.__java__Model244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__ClassFile245"):
                    opp_val = getattr(item, "java__ClassFile245", None)
                    
                    if opp_val == self:
                        setattr(item, "java__ClassFile245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__ClassFile245"):
                    opp_val = getattr(item, "java__ClassFile245", None)
                    
                    setattr(item, "java__ClassFile245", self)
                    

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__Model", None)
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
    def java__Model239(self):
        return self.__java__Model239

    @java__Model239.setter
    def java__Model239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__java__Model239", None)
        self.__java__Model239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__UnresolvedItem"):
                    opp_val = getattr(item, "java__UnresolvedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "java__UnresolvedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__UnresolvedItem"):
                    opp_val = getattr(item, "java__UnresolvedItem", None)
                    
                    setattr(item, "java__UnresolvedItem", self)
                    

    @property
    def java__Model(self):
        return self.__java__Model

    @java__Model.setter
    def java__Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Model__java__Model", None)
        self.__java__Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Type"):
                    opp_val = getattr(item, "java__Type", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Type"):
                    opp_val = getattr(item, "java__Type", None)
                    
                    setattr(item, "java__Type", self)
                    

class java__ManifestEntry:

    def __init__(self, name: str, java__ManifestEntry: "java__Manifest" = None, java__ManifestEntry211: set["java__ManifestAttribute"] = None):
        self.name = name
        self.java__ManifestEntry = java__ManifestEntry
        self.java__ManifestEntry211 = java__ManifestEntry211 if java__ManifestEntry211 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java__ManifestEntry211(self):
        return self.__java__ManifestEntry211

    @java__ManifestEntry211.setter
    def java__ManifestEntry211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ManifestEntry__java__ManifestEntry211", None)
        self.__java__ManifestEntry211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__ManifestAttribute212"):
                    opp_val = getattr(item, "java__ManifestAttribute212", None)
                    
                    if opp_val == self:
                        setattr(item, "java__ManifestAttribute212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__ManifestAttribute212"):
                    opp_val = getattr(item, "java__ManifestAttribute212", None)
                    
                    setattr(item, "java__ManifestAttribute212", self)
                    

    @property
    def java__ManifestEntry(self):
        return self.__java__ManifestEntry

    @java__ManifestEntry.setter
    def java__ManifestEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ManifestEntry__java__ManifestEntry", None)
        self.__java__ManifestEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Manifest209"):
                opp_val = getattr(old_value, "java__Manifest209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Manifest209"):
                opp_val = getattr(value, "java__Manifest209", None)
                if opp_val is None:
                    setattr(value, "java__Manifest209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java__ManifestAttribute:

    def __init__(self, key: str, value: str, java__ManifestAttribute: "java__Manifest" = None, java__ManifestAttribute212: "java__ManifestEntry" = None):
        self.key = key
        self.value = value
        self.java__ManifestAttribute = java__ManifestAttribute
        self.java__ManifestAttribute212 = java__ManifestAttribute212
        
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
    def java__ManifestAttribute212(self):
        return self.__java__ManifestAttribute212

    @java__ManifestAttribute212.setter
    def java__ManifestAttribute212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ManifestAttribute__java__ManifestAttribute212", None)
        self.__java__ManifestAttribute212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__ManifestEntry211"):
                opp_val = getattr(old_value, "java__ManifestEntry211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__ManifestEntry211"):
                opp_val = getattr(value, "java__ManifestEntry211", None)
                if opp_val is None:
                    setattr(value, "java__ManifestEntry211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__ManifestAttribute(self):
        return self.__java__ManifestAttribute

    @java__ManifestAttribute.setter
    def java__ManifestAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ManifestAttribute__java__ManifestAttribute", None)
        self.__java__ManifestAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Manifest207"):
                opp_val = getattr(old_value, "java__Manifest207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Manifest207"):
                opp_val = getattr(value, "java__Manifest207", None)
                if opp_val is None:
                    setattr(value, "java__Manifest207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractVariablesContainer:

    pass
class VariableDeclaration:

    pass
class TypeDeclaration:

    pass
class java__InterfaceDeclaration(TypeDeclaration):

    pass
class java__ClassDeclaration(TypeDeclaration):

    pass
class AbstractMethodInvocation:

    pass
class java__SuperMethodInvocation(AbstractTypeQualifiedExpression, AbstractMethodInvocation):

    pass
class AbstractMethodDeclaration:

    pass
class java__MethodDeclaration(AbstractMethodDeclaration):

    def __init__(self, extraArrayDimensions: int, java__MethodDeclaration: "java__TypeAccess" = None, MethodDeclaration: "java__MethodDeclaration" = None, redefinitions: "java__MethodDeclaration" = None, MethodDeclaration223: "java__MethodDeclaration" = None, redefinedMethodDeclaration: set["java__MethodDeclaration"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.java__MethodDeclaration = java__MethodDeclaration
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
        old_value = getattr(self, f"_java__MethodDeclaration__MethodDeclaration", None)
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
    def redefinedMethodDeclaration(self):
        return self.__redefinedMethodDeclaration

    @redefinedMethodDeclaration.setter
    def redefinedMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__MethodDeclaration__redefinedMethodDeclaration", None)
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
        old_value = getattr(self, f"_java__MethodDeclaration__redefinitions", None)
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
    def MethodDeclaration223(self):
        return self.__MethodDeclaration223

    @MethodDeclaration223.setter
    def MethodDeclaration223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__MethodDeclaration__MethodDeclaration223", None)
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
    def java__MethodDeclaration(self):
        return self.__java__MethodDeclaration

    @java__MethodDeclaration.setter
    def java__MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__MethodDeclaration__java__MethodDeclaration", None)
        self.__java__MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__TypeAccess218"):
                opp_val = getattr(old_value, "java__TypeAccess218", None)
                if opp_val == self:
                    setattr(old_value, "java__TypeAccess218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__TypeAccess218"):
                opp_val = getattr(value, "java__TypeAccess218", None)
                setattr(value, "java__TypeAccess218", self)

class java__ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class Comment:

    pass
class java__Javadoc(Comment):

    pass
class java__LineComment(Comment):

    pass
class java__BlockComment(Comment):

    pass
class AbstractTypeDeclaration:

    pass
class java__UnresolvedTypeDeclaration(AbstractTypeDeclaration, UnresolvedItem):

    pass
class java__TypeDeclaration(AbstractTypeDeclaration):

    pass
class java__EnumDeclaration(AbstractTypeDeclaration):

    pass
class java__AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class java__ASTNode(ABC):

    pass
class Statement:

    pass
class java__SwitchStatement(Statement):

    pass
class java__ReturnStatement(Statement):

    pass
class java__TryStatement(Statement):

    pass
class java__SuperConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java__VariableDeclarationStatement(Statement, AbstractVariablesContainer):

    def __init__(self, extraArrayDimensions: int, VariableDeclarationStatement: "java__Modifier" = None, variableDeclarationStatement: "java__Modifier" = None, java__VariableDeclarationStatement: set["java__Annotation"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclarationStatement = VariableDeclarationStatement
        self.variableDeclarationStatement = variableDeclarationStatement
        self.java__VariableDeclarationStatement = java__VariableDeclarationStatement if java__VariableDeclarationStatement is not None else set()
        
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
        old_value = getattr(self, f"_java__VariableDeclarationStatement__VariableDeclarationStatement", None)
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
    def java__VariableDeclarationStatement(self):
        return self.__java__VariableDeclarationStatement

    @java__VariableDeclarationStatement.setter
    def java__VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__VariableDeclarationStatement__java__VariableDeclarationStatement", None)
        self.__java__VariableDeclarationStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Annotation362"):
                    opp_val = getattr(item, "java__Annotation362", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Annotation362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Annotation362"):
                    opp_val = getattr(item, "java__Annotation362", None)
                    
                    setattr(item, "java__Annotation362", self)
                    

    @property
    def variableDeclarationStatement(self):
        return self.__variableDeclarationStatement

    @variableDeclarationStatement.setter
    def variableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__VariableDeclarationStatement__variableDeclarationStatement", None)
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

class java__BreakStatement(Statement):

    pass
class java__EnhancedForStatement(Statement):

    pass
class java__ConstructorInvocation(Statement, AbstractMethodInvocation):

    pass
class java__EmptyStatement(Statement):

    pass
class java__WhileStatement(Statement):

    pass
class java__ForStatement(Statement):

    pass
class java__CatchClause(Statement):

    pass
class java__ExpressionStatement(Statement):

    pass
class java__DoStatement(Statement):

    pass
class java__IfStatement(Statement):

    pass
class java__SynchronizedStatement(Statement):

    pass
class java__ContinueStatement(Statement):

    pass
class java__SwitchCase(Statement):

    def __init__(self, default: bool, java__SwitchCase: "java__Expression" = None):
        self.default = default
        self.java__SwitchCase = java__SwitchCase
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def java__SwitchCase(self):
        return self.__java__SwitchCase

    @java__SwitchCase.setter
    def java__SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SwitchCase__java__SwitchCase", None)
        self.__java__SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression309"):
                opp_val = getattr(old_value, "java__Expression309", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression309"):
                opp_val = getattr(value, "java__Expression309", None)
                setattr(value, "java__Expression309", self)

class java__TypeDeclarationStatement(Statement):

    pass
class java__ThrowStatement(Statement):

    pass
class java__AssertStatement(Statement):

    pass
class Expression:

    pass
class java__ArrayCreation(Expression):

    pass
class java__ArrayLengthAccess(Expression):

    pass
class java__CastExpression(Expression):

    pass
class java__NullLiteral(Expression):

    pass
class java__PrefixExpression(Expression):

    def __init__(self, operator: str, java__PrefixExpression: "java__Expression" = None):
        self.operator = operator
        self.java__PrefixExpression = java__PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java__PrefixExpression(self):
        return self.__java__PrefixExpression

    @java__PrefixExpression.setter
    def java__PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__PrefixExpression__java__PrefixExpression", None)
        self.__java__PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression286"):
                opp_val = getattr(old_value, "java__Expression286", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression286"):
                opp_val = getattr(value, "java__Expression286", None)
                setattr(value, "java__Expression286", self)

class java__CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java__InfixExpression(Expression):

    def __init__(self, operator: str, java__InfixExpression: "java__Expression" = None, java__InfixExpression188: "java__Expression" = None, java__InfixExpression191: set["java__Expression"] = None):
        self.operator = operator
        self.java__InfixExpression = java__InfixExpression
        self.java__InfixExpression188 = java__InfixExpression188
        self.java__InfixExpression191 = java__InfixExpression191 if java__InfixExpression191 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java__InfixExpression(self):
        return self.__java__InfixExpression

    @java__InfixExpression.setter
    def java__InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__InfixExpression__java__InfixExpression", None)
        self.__java__InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression186"):
                opp_val = getattr(old_value, "java__Expression186", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression186"):
                opp_val = getattr(value, "java__Expression186", None)
                setattr(value, "java__Expression186", self)

    @property
    def java__InfixExpression188(self):
        return self.__java__InfixExpression188

    @java__InfixExpression188.setter
    def java__InfixExpression188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__InfixExpression__java__InfixExpression188", None)
        self.__java__InfixExpression188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression189"):
                opp_val = getattr(old_value, "java__Expression189", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression189"):
                opp_val = getattr(value, "java__Expression189", None)
                setattr(value, "java__Expression189", self)

    @property
    def java__InfixExpression191(self):
        return self.__java__InfixExpression191

    @java__InfixExpression191.setter
    def java__InfixExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__InfixExpression__java__InfixExpression191", None)
        self.__java__InfixExpression191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Expression192"):
                    opp_val = getattr(item, "java__Expression192", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Expression192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Expression192"):
                    opp_val = getattr(item, "java__Expression192", None)
                    
                    setattr(item, "java__Expression192", self)
                    

class java__TypeLiteral(Expression):

    pass
class java__InstanceofExpression(Expression):

    pass
class java__StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class java__SingleVariableAccess(Expression):

    pass
class java__UnresolvedItemAccess(NamespaceAccess, Expression):

    pass
class java__PostfixExpression(Expression):

    def __init__(self, operator: str, java__PostfixExpression: "java__Expression" = None):
        self.operator = operator
        self.java__PostfixExpression = java__PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java__PostfixExpression(self):
        return self.__java__PostfixExpression

    @java__PostfixExpression.setter
    def java__PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__PostfixExpression__java__PostfixExpression", None)
        self.__java__PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression284"):
                opp_val = getattr(old_value, "java__Expression284", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression284"):
                opp_val = getattr(value, "java__Expression284", None)
                setattr(value, "java__Expression284", self)

class java__ClassInstanceCreation(Expression, AbstractMethodInvocation):

    pass
class java__NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class java__FieldAccess(Expression):

    pass
class java__VariableDeclarationExpression(AbstractVariablesContainer, Expression):

    pass
class java__ArrayAccess(Expression):

    pass
class java__ParenthesizedExpression(Expression):

    pass
class java__ConditionalExpression(Expression):

    pass
class java__ArrayInitializer(Expression):

    pass
class java__MethodInvocation(Expression, AbstractMethodInvocation):

    pass
class java__BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class java__Assignment(Expression):

    def __init__(self, operator: str, java__Assignment: "java__Expression" = None, java__Assignment83: "java__Expression" = None):
        self.operator = operator
        self.java__Assignment = java__Assignment
        self.java__Assignment83 = java__Assignment83
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def java__Assignment83(self):
        return self.__java__Assignment83

    @java__Assignment83.setter
    def java__Assignment83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Assignment__java__Assignment83", None)
        self.__java__Assignment83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression84"):
                opp_val = getattr(old_value, "java__Expression84", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression84"):
                opp_val = getattr(value, "java__Expression84", None)
                setattr(value, "java__Expression84", self)

    @property
    def java__Assignment(self):
        return self.__java__Assignment

    @java__Assignment.setter
    def java__Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Assignment__java__Assignment", None)
        self.__java__Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression81"):
                opp_val = getattr(old_value, "java__Expression81", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression81"):
                opp_val = getattr(value, "java__Expression81", None)
                setattr(value, "java__Expression81", self)

class java__AbstractTypeQualifiedExpression(Expression):

    pass
class Type:

    pass
class java__ParameterizedType(Type):

    pass
class java__ArrayType(Type):

    def __init__(self, dimensions: int, java__ArrayType: "java__TypeAccess" = None):
        self.dimensions = dimensions
        self.java__ArrayType = java__ArrayType
        
    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions

    @property
    def java__ArrayType(self):
        return self.__java__ArrayType

    @java__ArrayType.setter
    def java__ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ArrayType__java__ArrayType", None)
        self.__java__ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__TypeAccess79"):
                opp_val = getattr(old_value, "java__TypeAccess79", None)
                if opp_val == self:
                    setattr(old_value, "java__TypeAccess79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__TypeAccess79"):
                opp_val = getattr(value, "java__TypeAccess79", None)
                setattr(value, "java__TypeAccess79", self)

class java__UnresolvedType(Type, UnresolvedItem):

    pass
class java__PrimitiveType(Type):

    pass
class java__WildCardType(Type):

    def __init__(self, upperBound: bool, java__WildCardType: "java__TypeAccess" = None):
        self.upperBound = upperBound
        self.java__WildCardType = java__WildCardType
        
    @property
    def upperBound(self) -> bool:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: bool):
        self.__upperBound = upperBound

    @property
    def java__WildCardType(self):
        return self.__java__WildCardType

    @java__WildCardType.setter
    def java__WildCardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__WildCardType__java__WildCardType", None)
        self.__java__WildCardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__TypeAccess364"):
                opp_val = getattr(old_value, "java__TypeAccess364", None)
                if opp_val == self:
                    setattr(old_value, "java__TypeAccess364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__TypeAccess364"):
                opp_val = getattr(value, "java__TypeAccess364", None)
                setattr(value, "java__TypeAccess364", self)

class java__Manifest:

    pass
class NamedElement:

    pass
class java__BodyDeclaration(NamedElement):

    pass
class java__Package(NamedElement):

    pass
class java__VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, VariableDeclaration: "java__SingleVariableAccess" = None, java__VariableDeclaration: "java__Expression" = None, variable: set["java__SingleVariableAccess"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclaration = VariableDeclaration
        self.java__VariableDeclaration = java__VariableDeclaration
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
        old_value = getattr(self, f"_java__VariableDeclaration__variable", None)
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
    def java__VariableDeclaration(self):
        return self.__java__VariableDeclaration

    @java__VariableDeclaration.setter
    def java__VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__VariableDeclaration__java__VariableDeclaration", None)
        self.__java__VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Expression352"):
                opp_val = getattr(old_value, "java__Expression352", None)
                if opp_val == self:
                    setattr(old_value, "java__Expression352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Expression352"):
                opp_val = getattr(value, "java__Expression352", None)
                setattr(value, "java__Expression352", self)

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__VariableDeclaration__VariableDeclaration", None)
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

class java__CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, java__CompilationUnit: "java__ASTNode" = None, java__CompilationUnit108: "java__ClassFile" = None, java__CompilationUnit129: set["java__Comment"] = None, java__CompilationUnit132: set["java__ImportDeclaration"] = None, java__CompilationUnit134: "java__Package" = None, java__CompilationUnit137: set["java__AbstractTypeDeclaration"] = None, java__CompilationUnit242: "java__Model" = None):
        self.originalFilePath = originalFilePath
        self.java__CompilationUnit = java__CompilationUnit
        self.java__CompilationUnit108 = java__CompilationUnit108
        self.java__CompilationUnit129 = java__CompilationUnit129 if java__CompilationUnit129 is not None else set()
        self.java__CompilationUnit132 = java__CompilationUnit132 if java__CompilationUnit132 is not None else set()
        self.java__CompilationUnit134 = java__CompilationUnit134
        self.java__CompilationUnit137 = java__CompilationUnit137 if java__CompilationUnit137 is not None else set()
        self.java__CompilationUnit242 = java__CompilationUnit242
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java__CompilationUnit(self):
        return self.__java__CompilationUnit

    @java__CompilationUnit.setter
    def java__CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit", None)
        self.__java__CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__ASTNode43"):
                opp_val = getattr(old_value, "java__ASTNode43", None)
                if opp_val == self:
                    setattr(old_value, "java__ASTNode43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__ASTNode43"):
                opp_val = getattr(value, "java__ASTNode43", None)
                setattr(value, "java__ASTNode43", self)

    @property
    def java__CompilationUnit108(self):
        return self.__java__CompilationUnit108

    @java__CompilationUnit108.setter
    def java__CompilationUnit108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit108", None)
        self.__java__CompilationUnit108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__ClassFile107"):
                opp_val = getattr(old_value, "java__ClassFile107", None)
                if opp_val == self:
                    setattr(old_value, "java__ClassFile107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__ClassFile107"):
                opp_val = getattr(value, "java__ClassFile107", None)
                setattr(value, "java__ClassFile107", self)

    @property
    def java__CompilationUnit242(self):
        return self.__java__CompilationUnit242

    @java__CompilationUnit242.setter
    def java__CompilationUnit242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit242", None)
        self.__java__CompilationUnit242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Model241"):
                opp_val = getattr(old_value, "java__Model241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Model241"):
                opp_val = getattr(value, "java__Model241", None)
                if opp_val is None:
                    setattr(value, "java__Model241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__CompilationUnit129(self):
        return self.__java__CompilationUnit129

    @java__CompilationUnit129.setter
    def java__CompilationUnit129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit129", None)
        self.__java__CompilationUnit129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Comment130"):
                    opp_val = getattr(item, "java__Comment130", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Comment130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Comment130"):
                    opp_val = getattr(item, "java__Comment130", None)
                    
                    setattr(item, "java__Comment130", self)
                    

    @property
    def java__CompilationUnit137(self):
        return self.__java__CompilationUnit137

    @java__CompilationUnit137.setter
    def java__CompilationUnit137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit137", None)
        self.__java__CompilationUnit137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "java__AbstractTypeDeclaration138", None)
                    
                    if opp_val == self:
                        setattr(item, "java__AbstractTypeDeclaration138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__AbstractTypeDeclaration138"):
                    opp_val = getattr(item, "java__AbstractTypeDeclaration138", None)
                    
                    setattr(item, "java__AbstractTypeDeclaration138", self)
                    

    @property
    def java__CompilationUnit134(self):
        return self.__java__CompilationUnit134

    @java__CompilationUnit134.setter
    def java__CompilationUnit134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit134", None)
        self.__java__CompilationUnit134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Package135"):
                opp_val = getattr(old_value, "java__Package135", None)
                if opp_val == self:
                    setattr(old_value, "java__Package135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Package135"):
                opp_val = getattr(value, "java__Package135", None)
                setattr(value, "java__Package135", self)

    @property
    def java__CompilationUnit132(self):
        return self.__java__CompilationUnit132

    @java__CompilationUnit132.setter
    def java__CompilationUnit132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__CompilationUnit__java__CompilationUnit132", None)
        self.__java__CompilationUnit132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__ImportDeclaration"):
                    opp_val = getattr(item, "java__ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "java__ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__ImportDeclaration"):
                    opp_val = getattr(item, "java__ImportDeclaration", None)
                    
                    setattr(item, "java__ImportDeclaration", self)
                    

class java__LabeledStatement(Statement, NamedElement):

    pass
class java__Type(NamedElement):

    pass
class java__UnresolvedItem(NamedElement):

    pass
class java__ClassFile(NamedElement):

    def __init__(self, originalFilePath: str, java__ClassFile: "java__Archive" = None, java__ClassFile46: "java__ASTNode" = None, java__ClassFile104: "java__AbstractTypeDeclaration" = None, java__ClassFile107: "java__CompilationUnit" = None, java__ClassFile110: "java__Package" = None, java__ClassFile245: "java__Model" = None):
        self.originalFilePath = originalFilePath
        self.java__ClassFile = java__ClassFile
        self.java__ClassFile46 = java__ClassFile46
        self.java__ClassFile104 = java__ClassFile104
        self.java__ClassFile107 = java__ClassFile107
        self.java__ClassFile110 = java__ClassFile110
        self.java__ClassFile245 = java__ClassFile245
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java__ClassFile110(self):
        return self.__java__ClassFile110

    @java__ClassFile110.setter
    def java__ClassFile110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile110", None)
        self.__java__ClassFile110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Package"):
                opp_val = getattr(old_value, "java__Package", None)
                if opp_val == self:
                    setattr(old_value, "java__Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Package"):
                opp_val = getattr(value, "java__Package", None)
                setattr(value, "java__Package", self)

    @property
    def java__ClassFile46(self):
        return self.__java__ClassFile46

    @java__ClassFile46.setter
    def java__ClassFile46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile46", None)
        self.__java__ClassFile46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__ASTNode45"):
                opp_val = getattr(old_value, "java__ASTNode45", None)
                if opp_val == self:
                    setattr(old_value, "java__ASTNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__ASTNode45"):
                opp_val = getattr(value, "java__ASTNode45", None)
                setattr(value, "java__ASTNode45", self)

    @property
    def java__ClassFile107(self):
        return self.__java__ClassFile107

    @java__ClassFile107.setter
    def java__ClassFile107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile107", None)
        self.__java__ClassFile107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__CompilationUnit108"):
                opp_val = getattr(old_value, "java__CompilationUnit108", None)
                if opp_val == self:
                    setattr(old_value, "java__CompilationUnit108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__CompilationUnit108"):
                opp_val = getattr(value, "java__CompilationUnit108", None)
                setattr(value, "java__CompilationUnit108", self)

    @property
    def java__ClassFile245(self):
        return self.__java__ClassFile245

    @java__ClassFile245.setter
    def java__ClassFile245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile245", None)
        self.__java__ClassFile245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Model244"):
                opp_val = getattr(old_value, "java__Model244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Model244"):
                opp_val = getattr(value, "java__Model244", None)
                if opp_val is None:
                    setattr(value, "java__Model244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__ClassFile104(self):
        return self.__java__ClassFile104

    @java__ClassFile104.setter
    def java__ClassFile104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile104", None)
        self.__java__ClassFile104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__AbstractTypeDeclaration105"):
                opp_val = getattr(old_value, "java__AbstractTypeDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "java__AbstractTypeDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__AbstractTypeDeclaration105"):
                opp_val = getattr(value, "java__AbstractTypeDeclaration105", None)
                setattr(value, "java__AbstractTypeDeclaration105", self)

    @property
    def java__ClassFile(self):
        return self.__java__ClassFile

    @java__ClassFile.setter
    def java__ClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ClassFile__java__ClassFile", None)
        self.__java__ClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Archive"):
                opp_val = getattr(old_value, "java__Archive", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Archive"):
                opp_val = getattr(value, "java__Archive", None)
                if opp_val is None:
                    setattr(value, "java__Archive", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java__Archive(NamedElement):

    def __init__(self, originalFilePath: str, java__Archive: set["java__ClassFile"] = None, java__Archive34: "java__Manifest" = None, java__Archive248: "java__Model" = None):
        self.originalFilePath = originalFilePath
        self.java__Archive = java__Archive if java__Archive is not None else set()
        self.java__Archive34 = java__Archive34
        self.java__Archive248 = java__Archive248
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def java__Archive34(self):
        return self.__java__Archive34

    @java__Archive34.setter
    def java__Archive34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Archive__java__Archive34", None)
        self.__java__Archive34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Manifest"):
                opp_val = getattr(old_value, "java__Manifest", None)
                if opp_val == self:
                    setattr(old_value, "java__Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Manifest"):
                opp_val = getattr(value, "java__Manifest", None)
                setattr(value, "java__Manifest", self)

    @property
    def java__Archive(self):
        return self.__java__Archive

    @java__Archive.setter
    def java__Archive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Archive__java__Archive", None)
        self.__java__Archive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__ClassFile"):
                    opp_val = getattr(item, "java__ClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "java__ClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__ClassFile"):
                    opp_val = getattr(item, "java__ClassFile", None)
                    
                    setattr(item, "java__ClassFile", self)
                    

    @property
    def java__Archive248(self):
        return self.__java__Archive248

    @java__Archive248.setter
    def java__Archive248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Archive__java__Archive248", None)
        self.__java__Archive248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Model247"):
                opp_val = getattr(old_value, "java__Model247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Model247"):
                opp_val = getattr(value, "java__Model247", None)
                if opp_val is None:
                    setattr(value, "java__Model247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java__AnnotationMemberValuePair(NamedElement):

    pass
class java__Annotation(Expression):

    pass
class java__VariableDeclarationFragment(VariableDeclaration):

    pass
class ASTNode:

    pass
class java__Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "java__BodyDeclaration" = None, modifier255: "java__VariableDeclarationStatement" = None, modifier257: "java__VariableDeclarationExpression" = None, modifier: "java__BodyDeclaration" = None, modifier252: "java__SingleVariableDeclaration" = None, Modifier294: "java__SingleVariableDeclaration" = None, Modifier355: "java__VariableDeclarationExpression" = None, Modifier360: "java__VariableDeclarationStatement" = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.native = native
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.Modifier = Modifier
        self.modifier255 = modifier255
        self.modifier257 = modifier257
        self.modifier = modifier
        self.modifier252 = modifier252
        self.Modifier294 = Modifier294
        self.Modifier355 = Modifier355
        self.Modifier360 = Modifier360
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def modifier257(self):
        return self.__modifier257

    @modifier257.setter
    def modifier257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Modifier__modifier257", None)
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
        old_value = getattr(self, f"_java__Modifier__modifier", None)
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
    def Modifier294(self):
        return self.__Modifier294

    @Modifier294.setter
    def Modifier294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Modifier__Modifier294", None)
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
    def Modifier(self):
        return self.__Modifier

    @Modifier.setter
    def Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Modifier__Modifier", None)
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
    def modifier255(self):
        return self.__modifier255

    @modifier255.setter
    def modifier255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Modifier__modifier255", None)
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
        old_value = getattr(self, f"_java__Modifier__modifier252", None)
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
        old_value = getattr(self, f"_java__Modifier__Modifier360", None)
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
    def Modifier355(self):
        return self.__Modifier355

    @Modifier355.setter
    def Modifier355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Modifier__Modifier355", None)
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

class java__AnonymousClassDeclaration(ASTNode):

    pass
class java__Comment(ASTNode):

    def __init__(self, prefixOfParent: bool, content: str, enclosedByParent: bool, java__Comment: "java__AbstractTypeDeclaration" = None, java__Comment18: "java__AbstractTypeDeclaration" = None, java__Comment41: "java__ASTNode" = None, java__Comment130: "java__CompilationUnit" = None):
        self.prefixOfParent = prefixOfParent
        self.content = content
        self.enclosedByParent = enclosedByParent
        self.java__Comment = java__Comment
        self.java__Comment18 = java__Comment18
        self.java__Comment41 = java__Comment41
        self.java__Comment130 = java__Comment130
        
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
    def java__Comment18(self):
        return self.__java__Comment18

    @java__Comment18.setter
    def java__Comment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Comment__java__Comment18", None)
        self.__java__Comment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__AbstractTypeDeclaration17"):
                opp_val = getattr(old_value, "java__AbstractTypeDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__AbstractTypeDeclaration17"):
                opp_val = getattr(value, "java__AbstractTypeDeclaration17", None)
                if opp_val is None:
                    setattr(value, "java__AbstractTypeDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__Comment(self):
        return self.__java__Comment

    @java__Comment.setter
    def java__Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Comment__java__Comment", None)
        self.__java__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "java__AbstractTypeDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__AbstractTypeDeclaration"):
                opp_val = getattr(value, "java__AbstractTypeDeclaration", None)
                if opp_val is None:
                    setattr(value, "java__AbstractTypeDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__Comment130(self):
        return self.__java__Comment130

    @java__Comment130.setter
    def java__Comment130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Comment__java__Comment130", None)
        self.__java__Comment130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__CompilationUnit129"):
                opp_val = getattr(old_value, "java__CompilationUnit129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__CompilationUnit129"):
                opp_val = getattr(value, "java__CompilationUnit129", None)
                if opp_val is None:
                    setattr(value, "java__CompilationUnit129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__Comment41(self):
        return self.__java__Comment41

    @java__Comment41.setter
    def java__Comment41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__Comment__java__Comment41", None)
        self.__java__Comment41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__ASTNode"):
                opp_val = getattr(old_value, "java__ASTNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__ASTNode"):
                opp_val = getattr(value, "java__ASTNode", None)
                if opp_val is None:
                    setattr(value, "java__ASTNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java__TagElement(ASTNode):

    def __init__(self, tagName: str, java__TagElement: "java__Javadoc" = None, java__TagElement321: set["java__ASTNode"] = None):
        self.tagName = tagName
        self.java__TagElement = java__TagElement
        self.java__TagElement321 = java__TagElement321 if java__TagElement321 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def java__TagElement321(self):
        return self.__java__TagElement321

    @java__TagElement321.setter
    def java__TagElement321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__TagElement__java__TagElement321", None)
        self.__java__TagElement321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__ASTNode322"):
                    opp_val = getattr(item, "java__ASTNode322", None)
                    
                    if opp_val == self:
                        setattr(item, "java__ASTNode322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__ASTNode322"):
                    opp_val = getattr(item, "java__ASTNode322", None)
                    
                    setattr(item, "java__ASTNode322", self)
                    

    @property
    def java__TagElement(self):
        return self.__java__TagElement

    @java__TagElement.setter
    def java__TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__TagElement__java__TagElement", None)
        self.__java__TagElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__Javadoc"):
                opp_val = getattr(old_value, "java__Javadoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__Javadoc"):
                opp_val = getattr(value, "java__Javadoc", None)
                if opp_val is None:
                    setattr(value, "java__Javadoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java__Statement(ASTNode):

    pass
class java__MethodRefParameter(ASTNode):

    def __init__(self, name: str, varargs: bool, java__MethodRefParameter: "java__MethodRef" = None, java__MethodRefParameter233: "java__TypeAccess" = None):
        self.name = name
        self.varargs = varargs
        self.java__MethodRefParameter = java__MethodRefParameter
        self.java__MethodRefParameter233 = java__MethodRefParameter233
        
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
    def java__MethodRefParameter(self):
        return self.__java__MethodRefParameter

    @java__MethodRefParameter.setter
    def java__MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__MethodRefParameter__java__MethodRefParameter", None)
        self.__java__MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__MethodRef231"):
                opp_val = getattr(old_value, "java__MethodRef231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__MethodRef231"):
                opp_val = getattr(value, "java__MethodRef231", None)
                if opp_val is None:
                    setattr(value, "java__MethodRef231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java__MethodRefParameter233(self):
        return self.__java__MethodRefParameter233

    @java__MethodRefParameter233.setter
    def java__MethodRefParameter233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__MethodRefParameter__java__MethodRefParameter233", None)
        self.__java__MethodRefParameter233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__TypeAccess234"):
                opp_val = getattr(old_value, "java__TypeAccess234", None)
                if opp_val == self:
                    setattr(old_value, "java__TypeAccess234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__TypeAccess234"):
                opp_val = getattr(value, "java__TypeAccess234", None)
                setattr(value, "java__TypeAccess234", self)

class java__MemberRef(ASTNode):

    pass
class java__NamespaceAccess(ASTNode):

    pass
class java__TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class java__ImportDeclaration(ASTNode):

    def __init__(self, static: bool, java__ImportDeclaration: "java__CompilationUnit" = None, usagesInImports: "java__NamedElement" = None, ImportDeclaration: "java__NamedElement" = None):
        self.static = static
        self.java__ImportDeclaration = java__ImportDeclaration
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
        old_value = getattr(self, f"_java__ImportDeclaration__usagesInImports", None)
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
    def java__ImportDeclaration(self):
        return self.__java__ImportDeclaration

    @java__ImportDeclaration.setter
    def java__ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ImportDeclaration__java__ImportDeclaration", None)
        self.__java__ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__CompilationUnit132"):
                opp_val = getattr(old_value, "java__CompilationUnit132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__CompilationUnit132"):
                opp_val = getattr(value, "java__CompilationUnit132", None)
                if opp_val is None:
                    setattr(value, "java__CompilationUnit132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ImportDeclaration(self):
        return self.__ImportDeclaration

    @ImportDeclaration.setter
    def ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__ImportDeclaration__ImportDeclaration", None)
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

class java__NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, NamedElement: "java__ImportDeclaration" = None, java__NamedElement: "java__MemberRef" = None, importedElement: set["java__ImportDeclaration"] = None):
        self.name = name
        self.proxy = proxy
        self.NamedElement = NamedElement
        self.java__NamedElement = java__NamedElement
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
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__NamedElement__NamedElement", None)
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
        old_value = getattr(self, f"_java__NamedElement__importedElement", None)
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
    def java__NamedElement(self):
        return self.__java__NamedElement

    @java__NamedElement.setter
    def java__NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__NamedElement__java__NamedElement", None)
        self.__java__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__MemberRef"):
                opp_val = getattr(old_value, "java__MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "java__MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__MemberRef"):
                opp_val = getattr(value, "java__MemberRef", None)
                setattr(value, "java__MemberRef", self)

class java__AbstractVariablesContainer(ASTNode):

    pass
class java__AbstractMethodInvocation(ASTNode):

    pass
class java__MethodRef(ASTNode):

    pass
class java__Expression(ASTNode):

    pass
class java__TypeParameter(Type):

    pass
class java__TypeAccess(NamespaceAccess, Expression):

    pass
class java__SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "java__AbstractMethodDeclaration" = None, SingleVariableDeclaration100: "java__CatchClause" = None, SingleVariableDeclaration152: "java__EnhancedForStatement" = None, SingleVariableDeclaration253: "java__Modifier" = None, parameters: "java__AbstractMethodDeclaration" = None, exception: "java__CatchClause" = None, parameter: "java__EnhancedForStatement" = None, singleVariableDeclaration: "java__Modifier" = None, java__SingleVariableDeclaration: "java__TypeAccess" = None, java__SingleVariableDeclaration298: set["java__Annotation"] = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration100 = SingleVariableDeclaration100
        self.SingleVariableDeclaration152 = SingleVariableDeclaration152
        self.SingleVariableDeclaration253 = SingleVariableDeclaration253
        self.parameters = parameters
        self.exception = exception
        self.parameter = parameter
        self.singleVariableDeclaration = singleVariableDeclaration
        self.java__SingleVariableDeclaration = java__SingleVariableDeclaration
        self.java__SingleVariableDeclaration298 = java__SingleVariableDeclaration298 if java__SingleVariableDeclaration298 is not None else set()
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def java__SingleVariableDeclaration298(self):
        return self.__java__SingleVariableDeclaration298

    @java__SingleVariableDeclaration298.setter
    def java__SingleVariableDeclaration298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__java__SingleVariableDeclaration298", None)
        self.__java__SingleVariableDeclaration298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java__Annotation299"):
                    opp_val = getattr(item, "java__Annotation299", None)
                    
                    if opp_val == self:
                        setattr(item, "java__Annotation299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java__Annotation299"):
                    opp_val = getattr(item, "java__Annotation299", None)
                    
                    setattr(item, "java__Annotation299", self)
                    

    @property
    def SingleVariableDeclaration(self):
        return self.__SingleVariableDeclaration

    @SingleVariableDeclaration.setter
    def SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__SingleVariableDeclaration", None)
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
    def java__SingleVariableDeclaration(self):
        return self.__java__SingleVariableDeclaration

    @java__SingleVariableDeclaration.setter
    def java__SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__java__SingleVariableDeclaration", None)
        self.__java__SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java__TypeAccess296"):
                opp_val = getattr(old_value, "java__TypeAccess296", None)
                if opp_val == self:
                    setattr(old_value, "java__TypeAccess296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java__TypeAccess296"):
                opp_val = getattr(value, "java__TypeAccess296", None)
                setattr(value, "java__TypeAccess296", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__parameter", None)
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
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__exception", None)
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
    def singleVariableDeclaration(self):
        return self.__singleVariableDeclaration

    @singleVariableDeclaration.setter
    def singleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__singleVariableDeclaration", None)
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
        old_value = getattr(self, f"_java__SingleVariableDeclaration__SingleVariableDeclaration100", None)
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
    def SingleVariableDeclaration152(self):
        return self.__SingleVariableDeclaration152

    @SingleVariableDeclaration152.setter
    def SingleVariableDeclaration152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__SingleVariableDeclaration152", None)
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
    def SingleVariableDeclaration253(self):
        return self.__SingleVariableDeclaration253

    @SingleVariableDeclaration253.setter
    def SingleVariableDeclaration253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__SingleVariableDeclaration253", None)
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
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java__SingleVariableDeclaration__parameters", None)
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

class java__Block(Statement):

    pass
class BodyDeclaration:

    pass
class java__AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class java__EnumConstantDeclaration(BodyDeclaration, VariableDeclaration):

    pass
class java__FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass
class java__AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class java__Initializer(BodyDeclaration):

    pass
class java__AbstractMethodDeclaration(BodyDeclaration):

    pass