from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractTypeDeclaration:

    pass
class JAVA_ASTNode(ABC):

    pass
class ASTNode:

    pass
class JAVA_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool):
        self.name = name
        self.proxy = proxy
        
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

class JAVA_Expression(ASTNode):

    pass
class NamedElement:

    pass
class JAVA_BodyDeclaration(NamedElement):

    pass
class JAVA_Type(NamedElement):

    pass
class JAVA_Package(NamedElement):

    pass
class JAVA_TypeDeclaration(AbstractTypeDeclaration):

    pass
class Expression:

    pass
class Type:

    pass
class BodyDeclaration:

    pass
class JAVA_FieldDeclaration(BodyDeclaration):

    pass
class JAVA_AbstractTypeDeclaration(BodyDeclaration, Type):

    pass
class JAVA_TypeAccess(Expression):

    pass
class TypeDeclaration:

    pass
class JAVA_InterfaceDeclaration(TypeDeclaration):

    pass
class JAVA_ClassDeclaration(TypeDeclaration):

    pass