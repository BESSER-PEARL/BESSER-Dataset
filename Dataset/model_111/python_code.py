from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ModifierKind(Enum):
    static = "static"
    native = "native"
    sinchronized = "sinchronized"
    virtual = "virtual"
    override = "override"
    readonly = "readonly"
    const = "const"
    new = "new"
    none = "none"
class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    internal = "internal"
    protected = "protected"
    internal_protected = "internal_protected"
    private_protected = "private_protected"
class InheritanceKind(Enum):
    none = "none"
    abstract = "abstract"
    sealed = "sealed"
class SimpleType(Enum):
    bool = "bool"
    byte = "byte"
    char = "char"
    decimal = "decimal"
    double = "double"
    float = "float"
    int = "int"
    long = "long"
    sbyte = "sbyte"
    short = "short"
    uint = "uint"
    ulong = "ulong"
    ushort = "ushort"
    void = "void"
    object = "object"
    string = "string"


############################################
# Definition of Classes
############################################

class AbstractMethodInvocation:

    pass
class cSharpArchId_ConstructorInvocation(AbstractMethodInvocation):

    pass
class cSharpArchId_ClassInstanceCreation(AbstractMethodInvocation):

    pass
class cSharpArchId_MethodInvocation(AbstractMethodInvocation):

    pass
class AbstractMethodDeclaration:

    pass
class cSharpArchId_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class cSharpArchId_MethodDeclaration(AbstractMethodDeclaration):

    pass
class VariableDeclaration:

    pass
class cSharpArchId_SingleVariableDeclaration(VariableDeclaration):

    pass
class Statement:

    pass
class cSharpArchId_Block(Statement):

    pass
class BodyDeclaration:

    pass
class cSharpArchId_VariableDeclaration(BodyDeclaration):

    pass
class cSharpArchId_AbstractMethodDeclaration(BodyDeclaration):

    pass
class Expresion:

    pass
class cSharpArchId_Assignment(Expresion):

    pass
class cSharpArchId_Annotation(Expresion):

    pass
class cSharpArchId_TypeAcces(Expresion):

    pass
class AbstractTypeDeclaration:

    pass
class cSharpArchId_TypeDeclaration(AbstractTypeDeclaration):

    pass
class Comment:

    pass
class cSharpArchId_BlockComment(Comment):

    pass
class cSharpArchId_LineComment(Comment):

    pass
class cSharpArchId_ASTNode(ABC):

    pass
class TypeDeclaration:

    pass
class cSharpArchId_InterfaceDeclaration(TypeDeclaration):

    pass
class cSharpArchId_ClassDeclaration(TypeDeclaration):

    pass
class Type:

    pass
class cSharpArchId_TypeParameter(Type):

    pass
class cSharpArchId_PrimitiveType(Type):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class cSharpArchId_AbstractTypeDeclaration(Type):

    pass
class cSharpArchId_ElementRef(Type):

    pass
class cSharpArchId_ReturnType(Type):

    def __init__(self, returnType: str):
        self.returnType = returnType
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

class cSharpArchId_Enumeration(Type):

    pass
class ASTNode:

    pass
class cSharpArchId_Comment(ASTNode):

    def __init__(self, content: str, cSharpArchId_Comment: "cSharpArchId_CompileUnit" = None, cSharpArchId_Comment30: "cSharpArchId_AbstractTypeDeclaration" = None, cSharpArchId_Comment33: "cSharpArchId_AbstractTypeDeclaration" = None):
        self.content = content
        self.cSharpArchId_Comment = cSharpArchId_Comment
        self.cSharpArchId_Comment30 = cSharpArchId_Comment30
        self.cSharpArchId_Comment33 = cSharpArchId_Comment33
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def cSharpArchId_Comment(self):
        return self.__cSharpArchId_Comment

    @cSharpArchId_Comment.setter
    def cSharpArchId_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Comment__cSharpArchId_Comment", None)
        self.__cSharpArchId_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_CompileUnit15"):
                opp_val = getattr(old_value, "cSharpArchId_CompileUnit15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_CompileUnit15"):
                opp_val = getattr(value, "cSharpArchId_CompileUnit15", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_CompileUnit15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharpArchId_Comment30(self):
        return self.__cSharpArchId_Comment30

    @cSharpArchId_Comment30.setter
    def cSharpArchId_Comment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Comment__cSharpArchId_Comment30", None)
        self.__cSharpArchId_Comment30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_AbstractTypeDeclaration29"):
                opp_val = getattr(old_value, "cSharpArchId_AbstractTypeDeclaration29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_AbstractTypeDeclaration29"):
                opp_val = getattr(value, "cSharpArchId_AbstractTypeDeclaration29", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_AbstractTypeDeclaration29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharpArchId_Comment33(self):
        return self.__cSharpArchId_Comment33

    @cSharpArchId_Comment33.setter
    def cSharpArchId_Comment33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Comment__cSharpArchId_Comment33", None)
        self.__cSharpArchId_Comment33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_AbstractTypeDeclaration32"):
                opp_val = getattr(old_value, "cSharpArchId_AbstractTypeDeclaration32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_AbstractTypeDeclaration32"):
                opp_val = getattr(value, "cSharpArchId_AbstractTypeDeclaration32", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_AbstractTypeDeclaration32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cSharpArchId_Statement(ASTNode):

    pass
class cSharpArchId_Expresion(ASTNode):

    pass
class cSharpArchId_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, modifier: str, cSharpArchId_Modifier: "cSharpArchId_AbstractTypeDeclaration" = None, Modifier: "cSharpArchId_BodyDeclaration" = None, modifier: "cSharpArchId_BodyDeclaration" = None, cSharpArchId_Modifier41: set["cSharpArchId_Annotation"] = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.modifier = modifier
        self.cSharpArchId_Modifier = cSharpArchId_Modifier
        self.Modifier = Modifier
        self.modifier = modifier
        self.cSharpArchId_Modifier41 = cSharpArchId_Modifier41 if cSharpArchId_Modifier41 is not None else set()
        
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
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Modifier__modifier", None)
        self.__modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyDeclaration"):
                opp_val = getattr(old_value, "BodyDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "BodyDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyDeclaration"):
                opp_val = getattr(value, "BodyDeclaration", None)
                setattr(value, "BodyDeclaration", self)

    @property
    def cSharpArchId_Modifier(self):
        return self.__cSharpArchId_Modifier

    @cSharpArchId_Modifier.setter
    def cSharpArchId_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Modifier__cSharpArchId_Modifier", None)
        self.__cSharpArchId_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_AbstractTypeDeclaration37"):
                opp_val = getattr(old_value, "cSharpArchId_AbstractTypeDeclaration37", None)
                if opp_val == self:
                    setattr(old_value, "cSharpArchId_AbstractTypeDeclaration37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_AbstractTypeDeclaration37"):
                opp_val = getattr(value, "cSharpArchId_AbstractTypeDeclaration37", None)
                setattr(value, "cSharpArchId_AbstractTypeDeclaration37", self)

    @property
    def cSharpArchId_Modifier41(self):
        return self.__cSharpArchId_Modifier41

    @cSharpArchId_Modifier41.setter
    def cSharpArchId_Modifier41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Modifier__cSharpArchId_Modifier41", None)
        self.__cSharpArchId_Modifier41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_Annotation"):
                    opp_val = getattr(item, "cSharpArchId_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_Annotation"):
                    opp_val = getattr(item, "cSharpArchId_Annotation", None)
                    
                    setattr(item, "cSharpArchId_Annotation", self)
                    

    @property
    def Modifier(self):
        return self.__Modifier

    @Modifier.setter
    def Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Modifier__Modifier", None)
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

class cSharpArchId_AbstractMethodInvocation(ASTNode):

    pass
class cSharpArchId_NamedElement(ASTNode):

    def __init__(self, name: str, cSharpArchId_NamedElement: "cSharpArchId_CompileUnit" = None):
        self.name = name
        self.cSharpArchId_NamedElement = cSharpArchId_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cSharpArchId_NamedElement(self):
        return self.__cSharpArchId_NamedElement

    @cSharpArchId_NamedElement.setter
    def cSharpArchId_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_NamedElement__cSharpArchId_NamedElement", None)
        self.__cSharpArchId_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_CompileUnit13"):
                opp_val = getattr(old_value, "cSharpArchId_CompileUnit13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_CompileUnit13"):
                opp_val = getattr(value, "cSharpArchId_CompileUnit13", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_CompileUnit13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class cSharpArchId_MethodParameter(NamedElement):

    pass
class cSharpArchId_UsingDeclaration(NamedElement):

    pass
class cSharpArchId_BodyDeclaration(NamedElement):

    pass
class cSharpArchId_Type(NamedElement):

    pass
class cSharpArchId_Namespace(NamedElement):

    pass
class cSharpArchId_EnumerationLiteral(NamedElement):

    pass
class cSharpArchId_CompileUnit(NamedElement):

    def __init__(self, originalFilePath: str, cSharpArchId_CompileUnit: "cSharpArchId_Model" = None, cSharpArchId_CompileUnit15: set["cSharpArchId_Comment"] = None, cSharpArchId_CompileUnit17: "cSharpArchId_AbstractTypeDeclaration" = None, cSharpArchId_CompileUnit19: set["cSharpArchId_UsingDeclaration"] = None, cSharpArchId_CompileUnit21: "cSharpArchId_Namespace" = None, cSharpArchId_CompileUnit24: "cSharpArchId_ASTNode" = None, cSharpArchId_CompileUnit13: set["cSharpArchId_NamedElement"] = None, cSharpArchId_CompileUnit27: "cSharpArchId_Archive" = None):
        self.originalFilePath = originalFilePath
        self.cSharpArchId_CompileUnit = cSharpArchId_CompileUnit
        self.cSharpArchId_CompileUnit15 = cSharpArchId_CompileUnit15 if cSharpArchId_CompileUnit15 is not None else set()
        self.cSharpArchId_CompileUnit17 = cSharpArchId_CompileUnit17
        self.cSharpArchId_CompileUnit19 = cSharpArchId_CompileUnit19 if cSharpArchId_CompileUnit19 is not None else set()
        self.cSharpArchId_CompileUnit21 = cSharpArchId_CompileUnit21
        self.cSharpArchId_CompileUnit24 = cSharpArchId_CompileUnit24
        self.cSharpArchId_CompileUnit13 = cSharpArchId_CompileUnit13 if cSharpArchId_CompileUnit13 is not None else set()
        self.cSharpArchId_CompileUnit27 = cSharpArchId_CompileUnit27
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def cSharpArchId_CompileUnit27(self):
        return self.__cSharpArchId_CompileUnit27

    @cSharpArchId_CompileUnit27.setter
    def cSharpArchId_CompileUnit27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit27", None)
        self.__cSharpArchId_CompileUnit27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_Archive26"):
                opp_val = getattr(old_value, "cSharpArchId_Archive26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_Archive26"):
                opp_val = getattr(value, "cSharpArchId_Archive26", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_Archive26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharpArchId_CompileUnit24(self):
        return self.__cSharpArchId_CompileUnit24

    @cSharpArchId_CompileUnit24.setter
    def cSharpArchId_CompileUnit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit24", None)
        self.__cSharpArchId_CompileUnit24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_ASTNode"):
                opp_val = getattr(old_value, "cSharpArchId_ASTNode", None)
                if opp_val == self:
                    setattr(old_value, "cSharpArchId_ASTNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_ASTNode"):
                opp_val = getattr(value, "cSharpArchId_ASTNode", None)
                setattr(value, "cSharpArchId_ASTNode", self)

    @property
    def cSharpArchId_CompileUnit15(self):
        return self.__cSharpArchId_CompileUnit15

    @cSharpArchId_CompileUnit15.setter
    def cSharpArchId_CompileUnit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit15", None)
        self.__cSharpArchId_CompileUnit15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_Comment"):
                    opp_val = getattr(item, "cSharpArchId_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_Comment"):
                    opp_val = getattr(item, "cSharpArchId_Comment", None)
                    
                    setattr(item, "cSharpArchId_Comment", self)
                    

    @property
    def cSharpArchId_CompileUnit21(self):
        return self.__cSharpArchId_CompileUnit21

    @cSharpArchId_CompileUnit21.setter
    def cSharpArchId_CompileUnit21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit21", None)
        self.__cSharpArchId_CompileUnit21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_Namespace22"):
                opp_val = getattr(old_value, "cSharpArchId_Namespace22", None)
                if opp_val == self:
                    setattr(old_value, "cSharpArchId_Namespace22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_Namespace22"):
                opp_val = getattr(value, "cSharpArchId_Namespace22", None)
                setattr(value, "cSharpArchId_Namespace22", self)

    @property
    def cSharpArchId_CompileUnit19(self):
        return self.__cSharpArchId_CompileUnit19

    @cSharpArchId_CompileUnit19.setter
    def cSharpArchId_CompileUnit19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit19", None)
        self.__cSharpArchId_CompileUnit19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_UsingDeclaration"):
                    opp_val = getattr(item, "cSharpArchId_UsingDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_UsingDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_UsingDeclaration"):
                    opp_val = getattr(item, "cSharpArchId_UsingDeclaration", None)
                    
                    setattr(item, "cSharpArchId_UsingDeclaration", self)
                    

    @property
    def cSharpArchId_CompileUnit(self):
        return self.__cSharpArchId_CompileUnit

    @cSharpArchId_CompileUnit.setter
    def cSharpArchId_CompileUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit", None)
        self.__cSharpArchId_CompileUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_Model2"):
                opp_val = getattr(old_value, "cSharpArchId_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_Model2"):
                opp_val = getattr(value, "cSharpArchId_Model2", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharpArchId_CompileUnit17(self):
        return self.__cSharpArchId_CompileUnit17

    @cSharpArchId_CompileUnit17.setter
    def cSharpArchId_CompileUnit17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit17", None)
        self.__cSharpArchId_CompileUnit17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "cSharpArchId_AbstractTypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "cSharpArchId_AbstractTypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_AbstractTypeDeclaration"):
                opp_val = getattr(value, "cSharpArchId_AbstractTypeDeclaration", None)
                setattr(value, "cSharpArchId_AbstractTypeDeclaration", self)

    @property
    def cSharpArchId_CompileUnit13(self):
        return self.__cSharpArchId_CompileUnit13

    @cSharpArchId_CompileUnit13.setter
    def cSharpArchId_CompileUnit13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_CompileUnit__cSharpArchId_CompileUnit13", None)
        self.__cSharpArchId_CompileUnit13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_NamedElement"):
                    opp_val = getattr(item, "cSharpArchId_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_NamedElement"):
                    opp_val = getattr(item, "cSharpArchId_NamedElement", None)
                    
                    setattr(item, "cSharpArchId_NamedElement", self)
                    

class cSharpArchId_Archive(NamedElement):

    def __init__(self, originalFilePath: str, cSharpArchId_Archive: "cSharpArchId_Model" = None, cSharpArchId_Archive26: set["cSharpArchId_CompileUnit"] = None):
        self.originalFilePath = originalFilePath
        self.cSharpArchId_Archive = cSharpArchId_Archive
        self.cSharpArchId_Archive26 = cSharpArchId_Archive26 if cSharpArchId_Archive26 is not None else set()
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def cSharpArchId_Archive(self):
        return self.__cSharpArchId_Archive

    @cSharpArchId_Archive.setter
    def cSharpArchId_Archive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Archive__cSharpArchId_Archive", None)
        self.__cSharpArchId_Archive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cSharpArchId_Model"):
                opp_val = getattr(old_value, "cSharpArchId_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cSharpArchId_Model"):
                opp_val = getattr(value, "cSharpArchId_Model", None)
                if opp_val is None:
                    setattr(value, "cSharpArchId_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cSharpArchId_Archive26(self):
        return self.__cSharpArchId_Archive26

    @cSharpArchId_Archive26.setter
    def cSharpArchId_Archive26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Archive__cSharpArchId_Archive26", None)
        self.__cSharpArchId_Archive26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_CompileUnit27"):
                    opp_val = getattr(item, "cSharpArchId_CompileUnit27", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_CompileUnit27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_CompileUnit27"):
                    opp_val = getattr(item, "cSharpArchId_CompileUnit27", None)
                    
                    setattr(item, "cSharpArchId_CompileUnit27", self)
                    

class cSharpArchId_Model:

    def __init__(self, name: str, cSharpArchId_Model: set["cSharpArchId_Archive"] = None, cSharpArchId_Model2: set["cSharpArchId_CompileUnit"] = None):
        self.name = name
        self.cSharpArchId_Model = cSharpArchId_Model if cSharpArchId_Model is not None else set()
        self.cSharpArchId_Model2 = cSharpArchId_Model2 if cSharpArchId_Model2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cSharpArchId_Model2(self):
        return self.__cSharpArchId_Model2

    @cSharpArchId_Model2.setter
    def cSharpArchId_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Model__cSharpArchId_Model2", None)
        self.__cSharpArchId_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_CompileUnit"):
                    opp_val = getattr(item, "cSharpArchId_CompileUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_CompileUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_CompileUnit"):
                    opp_val = getattr(item, "cSharpArchId_CompileUnit", None)
                    
                    setattr(item, "cSharpArchId_CompileUnit", self)
                    

    @property
    def cSharpArchId_Model(self):
        return self.__cSharpArchId_Model

    @cSharpArchId_Model.setter
    def cSharpArchId_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cSharpArchId_Model__cSharpArchId_Model", None)
        self.__cSharpArchId_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cSharpArchId_Archive"):
                    opp_val = getattr(item, "cSharpArchId_Archive", None)
                    
                    if opp_val == self:
                        setattr(item, "cSharpArchId_Archive", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cSharpArchId_Archive"):
                    opp_val = getattr(item, "cSharpArchId_Archive", None)
                    
                    setattr(item, "cSharpArchId_Archive", self)
                    
