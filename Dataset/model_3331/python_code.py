from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MPrimitiveTypes(Enum):
    boolean = "boolean"
    byte = "byte"
    short = "short"
    int = "int"
    long = "long"
    float = "float"
    double = "double"
    char = "char"
class MVisibility(Enum):
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"
    DEFAULT = "DEFAULT"
    PRIVATE = "PRIVATE"


############################################
# Definition of Classes
############################################

class AbstractCExpression:

    pass
class model_CUnparsedExpression(AbstractCExpression):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class model_CConditionalExpression(AbstractCExpression):

    pass
class AbstractCStatement:

    pass
class model_CIfStatement(AbstractCStatement):

    pass
class model_CUnparsedStatement(AbstractCStatement):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class model_CExpressionStatement(AbstractCStatement):

    pass
class model_CBlockStatement(AbstractCStatement):

    pass
class AbstractMMethodImplementation:

    pass
class model_MMethodImplementationParameter:

    def __init__(self, final: bool, name: str, MMethodImplementationParameter: "model_AbstractMMethodImplementation" = None, parameters62: "model_AbstractMMethodImplementation" = None):
        self.final = final
        self.name = name
        self.MMethodImplementationParameter = MMethodImplementationParameter
        self.parameters62 = parameters62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def parameters62(self):
        return self.__parameters62

    @parameters62.setter
    def parameters62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MMethodImplementationParameter__parameters62", None)
        self.__parameters62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMMethodImplementation63"):
                opp_val = getattr(old_value, "AbstractMMethodImplementation63", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMMethodImplementation63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMMethodImplementation63"):
                opp_val = getattr(value, "AbstractMMethodImplementation63", None)
                setattr(value, "AbstractMMethodImplementation63", self)

    @property
    def MMethodImplementationParameter(self):
        return self.__MMethodImplementationParameter

    @MMethodImplementationParameter.setter
    def MMethodImplementationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MMethodImplementationParameter__MMethodImplementationParameter", None)
        self.__MMethodImplementationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodImplementation"):
                opp_val = getattr(old_value, "methodImplementation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodImplementation"):
                opp_val = getattr(value, "methodImplementation", None)
                if opp_val is None:
                    setattr(value, "methodImplementation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractMMethodLike:

    pass
class AbstractMImplementableMethodDeclaration:

    pass
class model_MDeclaredMethodImplementation(AbstractMMethodImplementation):

    pass
class model_MDirectMethodImplementation(AbstractMMethodImplementation):

    pass
class AbstractMMethodDeclaration:

    pass
class model_MImplicitMethodDeclaration(AbstractMMethodDeclaration):

    pass
class AbstractMClassFieldDeclaration:

    pass
class model_AbstractMImplementableMethodDeclaration(AbstractMMethodDeclaration):

    pass
class AbstractMFieldDeclaration:

    pass
class model_AbstractMClassFieldDeclaration(AbstractMFieldDeclaration):

    def __init__(self, visibility: str, final: bool):
        self.visibility = visibility
        self.final = final
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class model_AbstractCExpression(ABC):

    pass
class AbstractMTypeWithNameDeclaration:

    pass
class model_AbstractMMethodDeclaration(AbstractMTypeWithNameDeclaration):

    pass
class model_MConstructorParameter(AbstractMTypeWithNameDeclaration):

    def __init__(self, final: bool, parameters68: "model_MConstructor" = None, MConstructorParameter: "model_MConstructor" = None):
        self.final = final
        self.parameters68 = parameters68
        self.MConstructorParameter = MConstructorParameter
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def MConstructorParameter(self):
        return self.__MConstructorParameter

    @MConstructorParameter.setter
    def MConstructorParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MConstructorParameter__MConstructorParameter", None)
        self.__MConstructorParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constructor"):
                opp_val = getattr(old_value, "constructor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constructor"):
                opp_val = getattr(value, "constructor", None)
                if opp_val is None:
                    setattr(value, "constructor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters68(self):
        return self.__parameters68

    @parameters68.setter
    def parameters68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MConstructorParameter__parameters68", None)
        self.__parameters68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MConstructor69"):
                opp_val = getattr(old_value, "MConstructor69", None)
                if opp_val == self:
                    setattr(old_value, "MConstructor69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MConstructor69"):
                opp_val = getattr(value, "MConstructor69", None)
                setattr(value, "MConstructor69", self)

class model_CDeclarationStatement(AbstractCStatement, AbstractMTypeWithNameDeclaration):

    def __init__(self, final: bool, model_CDeclarationStatement: "model_AbstractCExpression" = None):
        self.final = final
        self.model_CDeclarationStatement = model_CDeclarationStatement
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def model_CDeclarationStatement(self):
        return self.__model_CDeclarationStatement

    @model_CDeclarationStatement.setter
    def model_CDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CDeclarationStatement__model_CDeclarationStatement", None)
        self.__model_CDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractCExpression73"):
                opp_val = getattr(old_value, "model_AbstractCExpression73", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractCExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractCExpression73"):
                opp_val = getattr(value, "model_AbstractCExpression73", None)
                setattr(value, "model_AbstractCExpression73", self)

class model_MMethodDeclarationParameter(AbstractMTypeWithNameDeclaration):

    pass
class model_AbstractMFieldDeclaration(AbstractMTypeWithNameDeclaration):

    pass
class model_MInterfaceMethodDeclaration(AbstractMImplementableMethodDeclaration):

    pass
class model_MConstantInterfaceFieldDeclaration(AbstractMFieldDeclaration):

    pass
class AbstractMInterface:

    pass
class AbstractMExternalType:

    pass
class model_MExternalInterface(AbstractMInterface, AbstractMExternalType):

    pass
class model_MNativeMethodDeclaration(AbstractMMethodDeclaration):

    pass
class model_AbstractMMethodImplementation(AbstractMMethodLike):

    pass
class model_MConstructor(AbstractMMethodLike):

    pass
class model_MInstanceClassFieldDeclaration(AbstractMClassFieldDeclaration):

    def __init__(self, transient: bool, MInstanceClassFieldDeclaration: "model_MDeclaredClass" = None, instanceFields: "model_MDeclaredClass" = None):
        self.transient = transient
        self.MInstanceClassFieldDeclaration = MInstanceClassFieldDeclaration
        self.instanceFields = instanceFields
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def MInstanceClassFieldDeclaration(self):
        return self.__MInstanceClassFieldDeclaration

    @MInstanceClassFieldDeclaration.setter
    def MInstanceClassFieldDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MInstanceClassFieldDeclaration__MInstanceClassFieldDeclaration", None)
        self.__MInstanceClassFieldDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner25"):
                opp_val = getattr(old_value, "owner25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner25"):
                opp_val = getattr(value, "owner25", None)
                if opp_val is None:
                    setattr(value, "owner25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def instanceFields(self):
        return self.__instanceFields

    @instanceFields.setter
    def instanceFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MInstanceClassFieldDeclaration__instanceFields", None)
        self.__instanceFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDeclaredClass43"):
                opp_val = getattr(old_value, "MDeclaredClass43", None)
                if opp_val == self:
                    setattr(old_value, "MDeclaredClass43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDeclaredClass43"):
                opp_val = getattr(value, "MDeclaredClass43", None)
                setattr(value, "MDeclaredClass43", self)

class model_MStaticClassFieldDeclaration(AbstractMClassFieldDeclaration):

    pass
class AbstractMDeclaredType:

    pass
class model_MDeclaredInterface(AbstractMInterface, AbstractMDeclaredType):

    pass
class AbstractMClass:

    pass
class model_MExternalClass(AbstractMExternalType, AbstractMClass):

    pass
class model_MDeclaredClass(AbstractMDeclaredType, AbstractMClass):

    pass
class model_MAbstractClassMethodDeclaration(AbstractMImplementableMethodDeclaration):

    def __init__(self, visibility: str, MAbstractClassMethodDeclaration: "model_MAbstractDeclaredClass" = None, abstractMethods: "model_MAbstractDeclaredClass" = None):
        self.visibility = visibility
        self.MAbstractClassMethodDeclaration = MAbstractClassMethodDeclaration
        self.abstractMethods = abstractMethods
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def abstractMethods(self):
        return self.__abstractMethods

    @abstractMethods.setter
    def abstractMethods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAbstractClassMethodDeclaration__abstractMethods", None)
        self.__abstractMethods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MAbstractDeclaredClass"):
                opp_val = getattr(old_value, "MAbstractDeclaredClass", None)
                if opp_val == self:
                    setattr(old_value, "MAbstractDeclaredClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MAbstractDeclaredClass"):
                opp_val = getattr(value, "MAbstractDeclaredClass", None)
                setattr(value, "MAbstractDeclaredClass", self)

    @property
    def MAbstractClassMethodDeclaration(self):
        return self.__MAbstractClassMethodDeclaration

    @MAbstractClassMethodDeclaration.setter
    def MAbstractClassMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MAbstractClassMethodDeclaration__MAbstractClassMethodDeclaration", None)
        self.__MAbstractClassMethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner33"):
                opp_val = getattr(old_value, "owner33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner33"):
                opp_val = getattr(value, "owner33", None)
                if opp_val is None:
                    setattr(value, "owner33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MDeclaredClass:

    pass
class model_MAbstractDeclaredClass(MDeclaredClass):

    pass
class model_AbstractCStatement(ABC):

    pass
class AbstractModifiers:

    pass
class model_AbstractMMethodLike(AbstractModifiers):

    pass
class model_AbstractModifiers(ABC):

    def __init__(self, visibility: str, final: bool, synchronized: bool):
        self.visibility = visibility
        self.final = final
        self.synchronized = synchronized
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class AbstractMTypeReference:

    pass
class model_MExternalTypeReference(AbstractMTypeReference):

    pass
class model_MPrimitiveTypeReference(AbstractMTypeReference):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class model_MDeclaredTypeReference(AbstractMTypeReference):

    pass
class model_AbstractMTypeReference(ABC):

    def __init__(self, array: bool, model_AbstractMTypeReference: "model_AbstractMTypeWithNameDeclaration" = None):
        self.array = array
        self.model_AbstractMTypeReference = model_AbstractMTypeReference
        
    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def model_AbstractMTypeReference(self):
        return self.__model_AbstractMTypeReference

    @model_AbstractMTypeReference.setter
    def model_AbstractMTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMTypeReference__model_AbstractMTypeReference", None)
        self.__model_AbstractMTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractMTypeWithNameDeclaration"):
                opp_val = getattr(old_value, "model_AbstractMTypeWithNameDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractMTypeWithNameDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractMTypeWithNameDeclaration"):
                opp_val = getattr(value, "model_AbstractMTypeWithNameDeclaration", None)
                setattr(value, "model_AbstractMTypeWithNameDeclaration", self)

class AbstractMType:

    pass
class model_AbstractMInterface(AbstractMType):

    pass
class model_AbstractMClass(AbstractMType):

    pass
class model_AbstractMTypeWithNameDeclaration(ABC):

    def __init__(self, name: str, model_AbstractMTypeWithNameDeclaration: "model_AbstractMTypeReference" = None):
        self.name = name
        self.model_AbstractMTypeWithNameDeclaration = model_AbstractMTypeWithNameDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_AbstractMTypeWithNameDeclaration(self):
        return self.__model_AbstractMTypeWithNameDeclaration

    @model_AbstractMTypeWithNameDeclaration.setter
    def model_AbstractMTypeWithNameDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMTypeWithNameDeclaration__model_AbstractMTypeWithNameDeclaration", None)
        self.__model_AbstractMTypeWithNameDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractMTypeReference"):
                opp_val = getattr(old_value, "model_AbstractMTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractMTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractMTypeReference"):
                opp_val = getattr(value, "model_AbstractMTypeReference", None)
                setattr(value, "model_AbstractMTypeReference", self)

class model_AbstractMType(ABC):

    pass
class AbstractMTypeContainer:

    pass
class model_AbstractMDeclaredType(AbstractMTypeContainer):

    def __init__(self, name: str, AbstractMDeclaredType: "model_AbstractMTypeContainer" = None, types: "model_AbstractMTypeContainer" = None, model_AbstractMDeclaredType: "model_MDeclaredTypeReference" = None):
        self.name = name
        self.AbstractMDeclaredType = AbstractMDeclaredType
        self.types = types
        self.model_AbstractMDeclaredType = model_AbstractMDeclaredType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMDeclaredType__types", None)
        self.__types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMTypeContainer"):
                opp_val = getattr(old_value, "AbstractMTypeContainer", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMTypeContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMTypeContainer"):
                opp_val = getattr(value, "AbstractMTypeContainer", None)
                setattr(value, "AbstractMTypeContainer", self)

    @property
    def model_AbstractMDeclaredType(self):
        return self.__model_AbstractMDeclaredType

    @model_AbstractMDeclaredType.setter
    def model_AbstractMDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMDeclaredType__model_AbstractMDeclaredType", None)
        self.__model_AbstractMDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MDeclaredTypeReference"):
                opp_val = getattr(old_value, "model_MDeclaredTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "model_MDeclaredTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MDeclaredTypeReference"):
                opp_val = getattr(value, "model_MDeclaredTypeReference", None)
                setattr(value, "model_MDeclaredTypeReference", self)

    @property
    def AbstractMDeclaredType(self):
        return self.__AbstractMDeclaredType

    @AbstractMDeclaredType.setter
    def AbstractMDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMDeclaredType__AbstractMDeclaredType", None)
        self.__AbstractMDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeContainer"):
                opp_val = getattr(old_value, "typeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeContainer"):
                opp_val = getattr(value, "typeContainer", None)
                if opp_val is None:
                    setattr(value, "typeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_AbstractMTypeContainer(ABC):

    pass
class AbstractMResource:

    pass
class model_MCompilationUnit(AbstractMResource, AbstractMTypeContainer):

    pass
class model_MResource(AbstractMResource):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class model_AbstractMResource(ABC):

    def __init__(self, name: str, derived: bool, resources: "model_MPackage" = None, AbstractMResource8: "model_AbstractMResource" = None, superOf: set["model_AbstractMResource"] = None, AbstractMResource: "model_MPackage" = None, AbstractMResource11: "model_AbstractMResource" = None, derivedFrom: set["model_AbstractMResource"] = None):
        self.name = name
        self.derived = derived
        self.resources = resources
        self.AbstractMResource8 = AbstractMResource8
        self.superOf = superOf if superOf is not None else set()
        self.AbstractMResource = AbstractMResource
        self.AbstractMResource11 = AbstractMResource11
        self.derivedFrom = derivedFrom if derivedFrom is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def superOf(self):
        return self.__superOf

    @superOf.setter
    def superOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__superOf", None)
        self.__superOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractMResource8"):
                    opp_val = getattr(item, "AbstractMResource8", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractMResource8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractMResource8"):
                    opp_val = getattr(item, "AbstractMResource8", None)
                    
                    setattr(item, "AbstractMResource8", self)
                    

    @property
    def derivedFrom(self):
        return self.__derivedFrom

    @derivedFrom.setter
    def derivedFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__derivedFrom", None)
        self.__derivedFrom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractMResource11"):
                    opp_val = getattr(item, "AbstractMResource11", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractMResource11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractMResource11"):
                    opp_val = getattr(item, "AbstractMResource11", None)
                    
                    setattr(item, "AbstractMResource11", self)
                    

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__resources", None)
        self.__resources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MPackage5"):
                opp_val = getattr(old_value, "MPackage5", None)
                if opp_val == self:
                    setattr(old_value, "MPackage5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MPackage5"):
                opp_val = getattr(value, "MPackage5", None)
                setattr(value, "MPackage5", self)

    @property
    def AbstractMResource8(self):
        return self.__AbstractMResource8

    @AbstractMResource8.setter
    def AbstractMResource8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__AbstractMResource8", None)
        self.__AbstractMResource8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superOf"):
                opp_val = getattr(old_value, "superOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superOf"):
                opp_val = getattr(value, "superOf", None)
                if opp_val is None:
                    setattr(value, "superOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AbstractMResource(self):
        return self.__AbstractMResource

    @AbstractMResource.setter
    def AbstractMResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__AbstractMResource", None)
        self.__AbstractMResource = value
        
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
    def AbstractMResource11(self):
        return self.__AbstractMResource11

    @AbstractMResource11.setter
    def AbstractMResource11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMResource__AbstractMResource11", None)
        self.__AbstractMResource11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivedFrom"):
                opp_val = getattr(old_value, "derivedFrom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivedFrom"):
                opp_val = getattr(value, "derivedFrom", None)
                if opp_val is None:
                    setattr(value, "derivedFrom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_AbstractMExternalType(ABC):

    def __init__(self, fullQualifiedName: str, AbstractMExternalType: "model_MRoot" = None, externalTypes: "model_MRoot" = None, model_AbstractMExternalType: "model_MExternalTypeReference" = None):
        self.fullQualifiedName = fullQualifiedName
        self.AbstractMExternalType = AbstractMExternalType
        self.externalTypes = externalTypes
        self.model_AbstractMExternalType = model_AbstractMExternalType
        
    @property
    def fullQualifiedName(self) -> str:
        return self.__fullQualifiedName

    @fullQualifiedName.setter
    def fullQualifiedName(self, fullQualifiedName: str):
        self.__fullQualifiedName = fullQualifiedName

    @property
    def AbstractMExternalType(self):
        return self.__AbstractMExternalType

    @AbstractMExternalType.setter
    def AbstractMExternalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMExternalType__AbstractMExternalType", None)
        self.__AbstractMExternalType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root"):
                opp_val = getattr(old_value, "root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root"):
                opp_val = getattr(value, "root", None)
                if opp_val is None:
                    setattr(value, "root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_AbstractMExternalType(self):
        return self.__model_AbstractMExternalType

    @model_AbstractMExternalType.setter
    def model_AbstractMExternalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMExternalType__model_AbstractMExternalType", None)
        self.__model_AbstractMExternalType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MExternalTypeReference"):
                opp_val = getattr(old_value, "model_MExternalTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "model_MExternalTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MExternalTypeReference"):
                opp_val = getattr(value, "model_MExternalTypeReference", None)
                setattr(value, "model_MExternalTypeReference", self)

    @property
    def externalTypes(self):
        return self.__externalTypes

    @externalTypes.setter
    def externalTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractMExternalType__externalTypes", None)
        self.__externalTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRoot"):
                opp_val = getattr(old_value, "MRoot", None)
                if opp_val == self:
                    setattr(old_value, "MRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRoot"):
                opp_val = getattr(value, "MRoot", None)
                setattr(value, "MRoot", self)

class AbstractMPackageContainer:

    pass
class model_MRoot(AbstractMPackageContainer):

    pass
class model_MPackage(AbstractMPackageContainer):

    def __init__(self, name: str, MPackage5: "model_AbstractMResource" = None, MPackage: "model_AbstractMPackageContainer" = None, packages: "model_AbstractMPackageContainer" = None, package: set["model_AbstractMResource"] = None):
        self.name = name
        self.MPackage5 = MPackage5
        self.MPackage = MPackage
        self.packages = packages
        self.package = package if package is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPackage__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractMResource"):
                    opp_val = getattr(item, "AbstractMResource", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractMResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractMResource"):
                    opp_val = getattr(item, "AbstractMResource", None)
                    
                    setattr(item, "AbstractMResource", self)
                    

    @property
    def MPackage(self):
        return self.__MPackage

    @MPackage.setter
    def MPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPackage__MPackage", None)
        self.__MPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageContainer"):
                opp_val = getattr(old_value, "packageContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageContainer"):
                opp_val = getattr(value, "packageContainer", None)
                if opp_val is None:
                    setattr(value, "packageContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MPackage5(self):
        return self.__MPackage5

    @MPackage5.setter
    def MPackage5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPackage__MPackage5", None)
        self.__MPackage5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources"):
                opp_val = getattr(old_value, "resources", None)
                if opp_val == self:
                    setattr(old_value, "resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources"):
                opp_val = getattr(value, "resources", None)
                setattr(value, "resources", self)

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MPackage__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMPackageContainer"):
                opp_val = getattr(old_value, "AbstractMPackageContainer", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMPackageContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMPackageContainer"):
                opp_val = getattr(value, "AbstractMPackageContainer", None)
                setattr(value, "AbstractMPackageContainer", self)

class model_AbstractMPackageContainer(ABC):

    pass