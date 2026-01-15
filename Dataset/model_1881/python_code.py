from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CodeGenLanguage(Enum):
    ACCELEO = "ACCELEO"
class PointcutType(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    BEFORE_BODY = "BEFORE_BODY"
    AFTER_BODY = "AFTER_BODY"
class InjectionMode(Enum):
    GOOGLE_JUICE = "GOOGLE_JUICE"
    PLAIN_JAVA = "PLAIN_JAVA"


############################################
# Definition of Classes
############################################

class serviceInterfaces_modelingenv_Operation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Operation:

    pass
class serviceInterfaces_modelingenv_JavaTypeDeclaration(ABC):

    def __init__(self, qualifiedName: str):
        self.qualifiedName = qualifiedName
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class serviceInterfaces_modelingenv_ExtensionPoint:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class ExtensionPoint:

    pass
class serviceInterfaces_codegen_Pointcut(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Pointcut:

    pass
class serviceInterfaces_codegen_StatementPoincut(Pointcut):

    pass
class serviceInterfaces_codegen_ClassPointcut(Pointcut):

    pass
class serviceInterfaces_codegen_ImportElementPointcut(Pointcut):

    pass
class serviceInterfaces_codegen_MethodPoincut(Pointcut):

    pass
class JavaTypeDeclaration:

    pass
class serviceInterfaces_modelingenv_JavaInterface(JavaTypeDeclaration):

    pass
class serviceInterfaces_modelingenv_JavaClass(JavaTypeDeclaration):

    pass
class serviceInterfaces_codegen_TransformationLibrary:

    def __init__(self, name: str, language: str):
        self.name = name
        self.language = language
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

class TransformationLibrary:

    pass
class Interface:

    pass
class serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0(Interface):

    def __init__(self, mode: str, serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0: set["JavaTypeDeclaration"] = None):
        self.mode = mode
        self.serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 = serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 if serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0(self):
        return self.__serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0

    @serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0.setter
    def serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0__serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0", None)
        self.__serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaTypeDeclaration"):
                    opp_val = getattr(item, "JavaTypeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaTypeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaTypeDeclaration"):
                    opp_val = getattr(item, "JavaTypeDeclaration", None)
                    
                    setattr(item, "JavaTypeDeclaration", self)
                    

class serviceInterfaces_modelingenv_SlotPlugInterfaceL0(Interface):

    pass
class serviceInterfaces_codegen_SlotPlugInterfaceL1(Interface):

    pass
class serviceInterfaces_codegen_InjectorAcceptorInterfaceL1(Interface):

    pass
class Packageable:

    pass
class serviceInterfaces_Interface(Packageable):

    def __init__(self, qName: str, description: str):
        self.qName = qName
        self.description = description
        
    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class serviceInterfaces_Package(Packageable):

    def __init__(self, name: str, serviceInterfaces_Package: set["serviceInterfaces_Packageable"] = None):
        self.name = name
        self.serviceInterfaces_Package = serviceInterfaces_Package if serviceInterfaces_Package is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def serviceInterfaces_Package(self):
        return self.__serviceInterfaces_Package

    @serviceInterfaces_Package.setter
    def serviceInterfaces_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_serviceInterfaces_Package__serviceInterfaces_Package", None)
        self.__serviceInterfaces_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "serviceInterfaces_Packageable2"):
                    opp_val = getattr(item, "serviceInterfaces_Packageable2", None)
                    
                    if opp_val == self:
                        setattr(item, "serviceInterfaces_Packageable2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "serviceInterfaces_Packageable2"):
                    opp_val = getattr(item, "serviceInterfaces_Packageable2", None)
                    
                    setattr(item, "serviceInterfaces_Packageable2", self)
                    

class serviceInterfaces_Packageable(ABC):

    pass
class serviceInterfaces_InterfaceRepository:

    pass