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


############################################
# Definition of Classes
############################################

class JMM_ASTNode(ABC):

    pass
class NamedElement:

    pass
class JMM_Type(NamedElement):

    pass
class NamespaceAccess:

    pass
class Expression:

    pass
class ASTNode:

    pass
class JMM_NamespaceAccess(ASTNode):

    pass
class JMM_Expression(ASTNode):

    pass
class JMM_AbstractVariablesContainer(ASTNode):

    pass
class JMM_NamedElement(ASTNode):

    def __init__(self, proxy: bool, name: str):
        self.proxy = proxy
        self.name = name
        
    @property
    def proxy(self) -> bool:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class JMM_Modifier(ASTNode):

    def __init__(self, inheritance: str, JMM_Modifier: "JMM_BodyDeclaration" = None):
        self.inheritance = inheritance
        self.JMM_Modifier = JMM_Modifier
        
    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def JMM_Modifier(self):
        return self.__JMM_Modifier

    @JMM_Modifier.setter
    def JMM_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JMM_Modifier__JMM_Modifier", None)
        self.__JMM_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JMM_BodyDeclaration15"):
                opp_val = getattr(old_value, "JMM_BodyDeclaration15", None)
                if opp_val == self:
                    setattr(old_value, "JMM_BodyDeclaration15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JMM_BodyDeclaration15"):
                opp_val = getattr(value, "JMM_BodyDeclaration15", None)
                setattr(value, "JMM_BodyDeclaration15", self)

class JMM_BodyDeclaration(NamedElement):

    pass
class Type:

    pass
class JMM_Model:

    def __init__(self, name: str, JMM_Model: set["JMM_Package"] = None):
        self.name = name
        self.JMM_Model = JMM_Model if JMM_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JMM_Model(self):
        return self.__JMM_Model

    @JMM_Model.setter
    def JMM_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JMM_Model__JMM_Model", None)
        self.__JMM_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JMM_Package"):
                    opp_val = getattr(item, "JMM_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "JMM_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JMM_Package"):
                    opp_val = getattr(item, "JMM_Package", None)
                    
                    setattr(item, "JMM_Package", self)
                    

class AbstractTypeDeclaration:

    pass
class JMM_TypeDeclaration(AbstractTypeDeclaration):

    pass
class JMM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class AbstractVariablesContainer:

    pass
class JMM_TypeAccess(NamespaceAccess, Expression):

    pass
class TypeDeclaration:

    pass
class JMM_InterfaceDeclaration(TypeDeclaration):

    pass
class JMM_ClassDeclaration(TypeDeclaration):

    pass
class AbstractMethodDeclaration:

    pass
class JMM_ConstructorDeclaration(AbstractMethodDeclaration):

    pass
class JMM_MethodDeclaration(AbstractMethodDeclaration):

    pass
class JMM_Package(NamedElement):

    pass
class BodyDeclaration:

    pass
class JMM_AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class JMM_AbstractMethodDeclaration(BodyDeclaration):

    pass
class JMM_FieldDeclaration(BodyDeclaration, AbstractVariablesContainer):

    pass