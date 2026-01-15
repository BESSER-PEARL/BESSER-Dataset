from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeType(Enum):
    STRING = "STRING"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    REFERENCE = "REFERENCE"
    DATETIME = "DATETIME"
    BOOLEAN = "BOOLEAN"
    PERFORMER = "PERFORMER"
class ModeType(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"


############################################
# Definition of Classes
############################################

class XSDAnnotation:

    pass
class xpdl_extensions_ExtendedAnnotationType(XSDAnnotation):

    pass
class xpdl_XpdlTypeType(ABC):

    pass
class xpdl_ScriptType:

    def __init__(self, version: str, grammar: str, type: str):
        self.version = version
        self.grammar = grammar
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def grammar(self) -> str:
        return self.__grammar

    @grammar.setter
    def grammar(self, grammar: str):
        self.__grammar = grammar

class xpdl_XSDSchema:

    pass
class xpdl_TypeDeclarationsType:

    def __init__(self, xpdl_TypeDeclarationsType: set["xpdl_TypeDeclarationType"] = None):
        self.xpdl_TypeDeclarationsType = xpdl_TypeDeclarationsType if xpdl_TypeDeclarationsType is not None else set()
        
    @property
    def xpdl_TypeDeclarationsType(self):
        return self.__xpdl_TypeDeclarationsType

    @xpdl_TypeDeclarationsType.setter
    def xpdl_TypeDeclarationsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationsType__xpdl_TypeDeclarationsType", None)
        self.__xpdl_TypeDeclarationsType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl_TypeDeclarationType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl_TypeDeclarationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl_TypeDeclarationType", None)
                    
                    setattr(item, "xpdl_TypeDeclarationType", self)
                    

    def getTypeDeclaration(self, typeId: str) -> str:
        # TODO: Implement getTypeDeclaration method
        pass

class xpdl_FormalParameterType:

    def __init__(self, description: str, id: str, mode: str, name: str, xpdl_FormalParameterType15: "xpdl_DataTypeType" = None, xpdl_FormalParameterType: "xpdl_FormalParametersType" = None):
        self.description = description
        self.id = id
        self.mode = mode
        self.name = name
        self.xpdl_FormalParameterType15 = xpdl_FormalParameterType15
        self.xpdl_FormalParameterType = xpdl_FormalParameterType
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xpdl_FormalParameterType(self):
        return self.__xpdl_FormalParameterType

    @xpdl_FormalParameterType.setter
    def xpdl_FormalParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_FormalParameterType__xpdl_FormalParameterType", None)
        self.__xpdl_FormalParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_FormalParametersType"):
                opp_val = getattr(old_value, "xpdl_FormalParametersType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_FormalParametersType"):
                opp_val = getattr(value, "xpdl_FormalParametersType", None)
                if opp_val is None:
                    setattr(value, "xpdl_FormalParametersType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl_FormalParameterType15(self):
        return self.__xpdl_FormalParameterType15

    @xpdl_FormalParameterType15.setter
    def xpdl_FormalParameterType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_FormalParameterType__xpdl_FormalParameterType15", None)
        self.__xpdl_FormalParameterType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DataTypeType16"):
                opp_val = getattr(old_value, "xpdl_DataTypeType16", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DataTypeType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DataTypeType16"):
                opp_val = getattr(value, "xpdl_DataTypeType16", None)
                setattr(value, "xpdl_DataTypeType16", self)

class xpdl_FormalParametersType:

    def __init__(self, xpdl_FormalParametersType: set["xpdl_FormalParameterType"] = None):
        self.xpdl_FormalParametersType = xpdl_FormalParametersType if xpdl_FormalParametersType is not None else set()
        
    @property
    def xpdl_FormalParametersType(self):
        return self.__xpdl_FormalParametersType

    @xpdl_FormalParametersType.setter
    def xpdl_FormalParametersType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_FormalParametersType__xpdl_FormalParametersType", None)
        self.__xpdl_FormalParametersType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl_FormalParameterType"):
                    opp_val = getattr(item, "xpdl_FormalParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl_FormalParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl_FormalParameterType"):
                    opp_val = getattr(item, "xpdl_FormalParameterType", None)
                    
                    setattr(item, "xpdl_FormalParameterType", self)
                    

    def addFormalParameter(self, parameter: str):
        # TODO: Implement addFormalParameter method
        pass

    def getFormalParameter(self, parameterId: str) -> str:
        # TODO: Implement getFormalParameter method
        pass

class xpdl_ExternalPackages:

    def __init__(self, xpdl_ExternalPackages: set["xpdl_ExternalPackage"] = None):
        self.xpdl_ExternalPackages = xpdl_ExternalPackages if xpdl_ExternalPackages is not None else set()
        
    @property
    def xpdl_ExternalPackages(self):
        return self.__xpdl_ExternalPackages

    @xpdl_ExternalPackages.setter
    def xpdl_ExternalPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExternalPackages__xpdl_ExternalPackages", None)
        self.__xpdl_ExternalPackages = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl_ExternalPackage"):
                    opp_val = getattr(item, "xpdl_ExternalPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl_ExternalPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl_ExternalPackage"):
                    opp_val = getattr(item, "xpdl_ExternalPackage", None)
                    
                    setattr(item, "xpdl_ExternalPackage", self)
                    

    def getExternalPackage(self, packageId: str) -> str:
        # TODO: Implement getExternalPackage method
        pass

class xpdl_Extensible(ABC):

    pass
class Extensible:

    pass
class xpdl_TypeDeclarationType(Extensible):

    def __init__(self, id: str, name: str, description: str, xpdl_TypeDeclarationType: "xpdl_TypeDeclarationsType" = None, xpdl_TypeDeclarationType21: "xpdl_BasicTypeType" = None, xpdl_TypeDeclarationType24: "xpdl_DeclaredTypeType" = None, xpdl_TypeDeclarationType27: "xpdl_SchemaTypeType" = None, xpdl_TypeDeclarationType30: "xpdl_ExternalReferenceType" = None):
        self.id = id
        self.name = name
        self.description = description
        self.xpdl_TypeDeclarationType = xpdl_TypeDeclarationType
        self.xpdl_TypeDeclarationType21 = xpdl_TypeDeclarationType21
        self.xpdl_TypeDeclarationType24 = xpdl_TypeDeclarationType24
        self.xpdl_TypeDeclarationType27 = xpdl_TypeDeclarationType27
        self.xpdl_TypeDeclarationType30 = xpdl_TypeDeclarationType30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl_TypeDeclarationType(self):
        return self.__xpdl_TypeDeclarationType

    @xpdl_TypeDeclarationType.setter
    def xpdl_TypeDeclarationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationType__xpdl_TypeDeclarationType", None)
        self.__xpdl_TypeDeclarationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_TypeDeclarationsType"):
                opp_val = getattr(old_value, "xpdl_TypeDeclarationsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_TypeDeclarationsType"):
                opp_val = getattr(value, "xpdl_TypeDeclarationsType", None)
                if opp_val is None:
                    setattr(value, "xpdl_TypeDeclarationsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl_TypeDeclarationType30(self):
        return self.__xpdl_TypeDeclarationType30

    @xpdl_TypeDeclarationType30.setter
    def xpdl_TypeDeclarationType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationType__xpdl_TypeDeclarationType30", None)
        self.__xpdl_TypeDeclarationType30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_ExternalReferenceType31"):
                opp_val = getattr(old_value, "xpdl_ExternalReferenceType31", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_ExternalReferenceType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_ExternalReferenceType31"):
                opp_val = getattr(value, "xpdl_ExternalReferenceType31", None)
                setattr(value, "xpdl_ExternalReferenceType31", self)

    @property
    def xpdl_TypeDeclarationType21(self):
        return self.__xpdl_TypeDeclarationType21

    @xpdl_TypeDeclarationType21.setter
    def xpdl_TypeDeclarationType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationType__xpdl_TypeDeclarationType21", None)
        self.__xpdl_TypeDeclarationType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_BasicTypeType22"):
                opp_val = getattr(old_value, "xpdl_BasicTypeType22", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_BasicTypeType22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_BasicTypeType22"):
                opp_val = getattr(value, "xpdl_BasicTypeType22", None)
                setattr(value, "xpdl_BasicTypeType22", self)

    @property
    def xpdl_TypeDeclarationType27(self):
        return self.__xpdl_TypeDeclarationType27

    @xpdl_TypeDeclarationType27.setter
    def xpdl_TypeDeclarationType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationType__xpdl_TypeDeclarationType27", None)
        self.__xpdl_TypeDeclarationType27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_SchemaTypeType28"):
                opp_val = getattr(old_value, "xpdl_SchemaTypeType28", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_SchemaTypeType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_SchemaTypeType28"):
                opp_val = getattr(value, "xpdl_SchemaTypeType28", None)
                setattr(value, "xpdl_SchemaTypeType28", self)

    @property
    def xpdl_TypeDeclarationType24(self):
        return self.__xpdl_TypeDeclarationType24

    @xpdl_TypeDeclarationType24.setter
    def xpdl_TypeDeclarationType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_TypeDeclarationType__xpdl_TypeDeclarationType24", None)
        self.__xpdl_TypeDeclarationType24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DeclaredTypeType25"):
                opp_val = getattr(old_value, "xpdl_DeclaredTypeType25", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DeclaredTypeType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DeclaredTypeType25"):
                opp_val = getattr(value, "xpdl_DeclaredTypeType25", None)
                setattr(value, "xpdl_DeclaredTypeType25", self)

    def getSchema(self) -> str:
        # TODO: Implement getSchema method
        pass

    def getDataType(self) -> XpdlTypeType:
        # TODO: Implement getDataType method
        pass

class xpdl_ExternalPackage(Extensible):

    def __init__(self, href: str, id: str, name: str, xpdl_ExternalPackage: "xpdl_ExternalPackages" = None):
        self.href = href
        self.id = id
        self.name = name
        self.xpdl_ExternalPackage = xpdl_ExternalPackage
        
    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xpdl_ExternalPackage(self):
        return self.__xpdl_ExternalPackage

    @xpdl_ExternalPackage.setter
    def xpdl_ExternalPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExternalPackage__xpdl_ExternalPackage", None)
        self.__xpdl_ExternalPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_ExternalPackages"):
                opp_val = getattr(old_value, "xpdl_ExternalPackages", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_ExternalPackages"):
                opp_val = getattr(value, "xpdl_ExternalPackages", None)
                if opp_val is None:
                    setattr(value, "xpdl_ExternalPackages", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl_ExtendedAttributeType:

    def __init__(self, mixed: str, group: str, any: str, name: str, value: str, xpdl_ExtendedAttributeType9: "ExtendedAnnotationType" = None, xpdl_ExtendedAttributeType: "xpdl_ExtendedAttributesType" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.name = name
        self.value = value
        self.xpdl_ExtendedAttributeType9 = xpdl_ExtendedAttributeType9
        self.xpdl_ExtendedAttributeType = xpdl_ExtendedAttributeType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xpdl_ExtendedAttributeType(self):
        return self.__xpdl_ExtendedAttributeType

    @xpdl_ExtendedAttributeType.setter
    def xpdl_ExtendedAttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExtendedAttributeType__xpdl_ExtendedAttributeType", None)
        self.__xpdl_ExtendedAttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_ExtendedAttributesType"):
                opp_val = getattr(old_value, "xpdl_ExtendedAttributesType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_ExtendedAttributesType"):
                opp_val = getattr(value, "xpdl_ExtendedAttributesType", None)
                if opp_val is None:
                    setattr(value, "xpdl_ExtendedAttributesType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl_ExtendedAttributeType9(self):
        return self.__xpdl_ExtendedAttributeType9

    @xpdl_ExtendedAttributeType9.setter
    def xpdl_ExtendedAttributeType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExtendedAttributeType__xpdl_ExtendedAttributeType9", None)
        self.__xpdl_ExtendedAttributeType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExtendedAnnotationType"):
                opp_val = getattr(old_value, "ExtendedAnnotationType", None)
                if opp_val == self:
                    setattr(old_value, "ExtendedAnnotationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExtendedAnnotationType"):
                opp_val = getattr(value, "ExtendedAnnotationType", None)
                setattr(value, "ExtendedAnnotationType", self)

class xpdl_ExtendedAttributesType:

    pass
class ExtendedAnnotationType:

    pass
class xpdl_DataTypeType:

    def __init__(self, carnotType: str, xpdl_DataTypeType2: "xpdl_DeclaredTypeType" = None, xpdl_DataTypeType4: "xpdl_SchemaTypeType" = None, xpdl_DataTypeType6: "xpdl_ExternalReferenceType" = None, xpdl_DataTypeType: "xpdl_BasicTypeType" = None, xpdl_DataTypeType16: "xpdl_FormalParameterType" = None):
        self.carnotType = carnotType
        self.xpdl_DataTypeType2 = xpdl_DataTypeType2
        self.xpdl_DataTypeType4 = xpdl_DataTypeType4
        self.xpdl_DataTypeType6 = xpdl_DataTypeType6
        self.xpdl_DataTypeType = xpdl_DataTypeType
        self.xpdl_DataTypeType16 = xpdl_DataTypeType16
        
    @property
    def carnotType(self) -> str:
        return self.__carnotType

    @carnotType.setter
    def carnotType(self, carnotType: str):
        self.__carnotType = carnotType

    @property
    def xpdl_DataTypeType2(self):
        return self.__xpdl_DataTypeType2

    @xpdl_DataTypeType2.setter
    def xpdl_DataTypeType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DataTypeType__xpdl_DataTypeType2", None)
        self.__xpdl_DataTypeType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DeclaredTypeType"):
                opp_val = getattr(old_value, "xpdl_DeclaredTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DeclaredTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DeclaredTypeType"):
                opp_val = getattr(value, "xpdl_DeclaredTypeType", None)
                setattr(value, "xpdl_DeclaredTypeType", self)

    @property
    def xpdl_DataTypeType(self):
        return self.__xpdl_DataTypeType

    @xpdl_DataTypeType.setter
    def xpdl_DataTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DataTypeType__xpdl_DataTypeType", None)
        self.__xpdl_DataTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_BasicTypeType"):
                opp_val = getattr(old_value, "xpdl_BasicTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_BasicTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_BasicTypeType"):
                opp_val = getattr(value, "xpdl_BasicTypeType", None)
                setattr(value, "xpdl_BasicTypeType", self)

    @property
    def xpdl_DataTypeType16(self):
        return self.__xpdl_DataTypeType16

    @xpdl_DataTypeType16.setter
    def xpdl_DataTypeType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DataTypeType__xpdl_DataTypeType16", None)
        self.__xpdl_DataTypeType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_FormalParameterType15"):
                opp_val = getattr(old_value, "xpdl_FormalParameterType15", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_FormalParameterType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_FormalParameterType15"):
                opp_val = getattr(value, "xpdl_FormalParameterType15", None)
                setattr(value, "xpdl_FormalParameterType15", self)

    @property
    def xpdl_DataTypeType6(self):
        return self.__xpdl_DataTypeType6

    @xpdl_DataTypeType6.setter
    def xpdl_DataTypeType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DataTypeType__xpdl_DataTypeType6", None)
        self.__xpdl_DataTypeType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_ExternalReferenceType"):
                opp_val = getattr(old_value, "xpdl_ExternalReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_ExternalReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_ExternalReferenceType"):
                opp_val = getattr(value, "xpdl_ExternalReferenceType", None)
                setattr(value, "xpdl_ExternalReferenceType", self)

    @property
    def xpdl_DataTypeType4(self):
        return self.__xpdl_DataTypeType4

    @xpdl_DataTypeType4.setter
    def xpdl_DataTypeType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DataTypeType__xpdl_DataTypeType4", None)
        self.__xpdl_DataTypeType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_SchemaTypeType"):
                opp_val = getattr(old_value, "xpdl_SchemaTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_SchemaTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_SchemaTypeType"):
                opp_val = getattr(value, "xpdl_SchemaTypeType", None)
                setattr(value, "xpdl_SchemaTypeType", self)

    def getDataType(self) -> XpdlTypeType:
        # TODO: Implement getDataType method
        pass

class XpdlTypeType:

    pass
class xpdl_ExternalReferenceType(XpdlTypeType):

    def __init__(self, location: str, namespace: str, xref: str, xpdl_ExternalReferenceType: "xpdl_DataTypeType" = None, xpdl_ExternalReferenceType31: "xpdl_TypeDeclarationType" = None):
        self.location = location
        self.namespace = namespace
        self.xref = xref
        self.xpdl_ExternalReferenceType = xpdl_ExternalReferenceType
        self.xpdl_ExternalReferenceType31 = xpdl_ExternalReferenceType31
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def xref(self) -> str:
        return self.__xref

    @xref.setter
    def xref(self, xref: str):
        self.__xref = xref

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def xpdl_ExternalReferenceType(self):
        return self.__xpdl_ExternalReferenceType

    @xpdl_ExternalReferenceType.setter
    def xpdl_ExternalReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExternalReferenceType__xpdl_ExternalReferenceType", None)
        self.__xpdl_ExternalReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DataTypeType6"):
                opp_val = getattr(old_value, "xpdl_DataTypeType6", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DataTypeType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DataTypeType6"):
                opp_val = getattr(value, "xpdl_DataTypeType6", None)
                setattr(value, "xpdl_DataTypeType6", self)

    @property
    def xpdl_ExternalReferenceType31(self):
        return self.__xpdl_ExternalReferenceType31

    @xpdl_ExternalReferenceType31.setter
    def xpdl_ExternalReferenceType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_ExternalReferenceType__xpdl_ExternalReferenceType31", None)
        self.__xpdl_ExternalReferenceType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_TypeDeclarationType30"):
                opp_val = getattr(old_value, "xpdl_TypeDeclarationType30", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_TypeDeclarationType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_TypeDeclarationType30"):
                opp_val = getattr(value, "xpdl_TypeDeclarationType30", None)
                setattr(value, "xpdl_TypeDeclarationType30", self)

    def getSchema(self) -> str:
        # TODO: Implement getSchema method
        pass

class xpdl_DeclaredTypeType(XpdlTypeType):

    def __init__(self, id: str, xpdl_DeclaredTypeType: "xpdl_DataTypeType" = None, xpdl_DeclaredTypeType25: "xpdl_TypeDeclarationType" = None):
        self.id = id
        self.xpdl_DeclaredTypeType = xpdl_DeclaredTypeType
        self.xpdl_DeclaredTypeType25 = xpdl_DeclaredTypeType25
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl_DeclaredTypeType25(self):
        return self.__xpdl_DeclaredTypeType25

    @xpdl_DeclaredTypeType25.setter
    def xpdl_DeclaredTypeType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DeclaredTypeType__xpdl_DeclaredTypeType25", None)
        self.__xpdl_DeclaredTypeType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_TypeDeclarationType24"):
                opp_val = getattr(old_value, "xpdl_TypeDeclarationType24", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_TypeDeclarationType24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_TypeDeclarationType24"):
                opp_val = getattr(value, "xpdl_TypeDeclarationType24", None)
                setattr(value, "xpdl_TypeDeclarationType24", self)

    @property
    def xpdl_DeclaredTypeType(self):
        return self.__xpdl_DeclaredTypeType

    @xpdl_DeclaredTypeType.setter
    def xpdl_DeclaredTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_DeclaredTypeType__xpdl_DeclaredTypeType", None)
        self.__xpdl_DeclaredTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DataTypeType2"):
                opp_val = getattr(old_value, "xpdl_DataTypeType2", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DataTypeType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DataTypeType2"):
                opp_val = getattr(value, "xpdl_DataTypeType2", None)
                setattr(value, "xpdl_DataTypeType2", self)

class xpdl_SchemaTypeType(XpdlTypeType):

    pass
class xpdl_BasicTypeType(XpdlTypeType):

    def __init__(self, type: str, xpdl_BasicTypeType: "xpdl_DataTypeType" = None, xpdl_BasicTypeType22: "xpdl_TypeDeclarationType" = None):
        self.type = type
        self.xpdl_BasicTypeType = xpdl_BasicTypeType
        self.xpdl_BasicTypeType22 = xpdl_BasicTypeType22
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl_BasicTypeType(self):
        return self.__xpdl_BasicTypeType

    @xpdl_BasicTypeType.setter
    def xpdl_BasicTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_BasicTypeType__xpdl_BasicTypeType", None)
        self.__xpdl_BasicTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_DataTypeType"):
                opp_val = getattr(old_value, "xpdl_DataTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_DataTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_DataTypeType"):
                opp_val = getattr(value, "xpdl_DataTypeType", None)
                setattr(value, "xpdl_DataTypeType", self)

    @property
    def xpdl_BasicTypeType22(self):
        return self.__xpdl_BasicTypeType22

    @xpdl_BasicTypeType22.setter
    def xpdl_BasicTypeType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl_BasicTypeType__xpdl_BasicTypeType22", None)
        self.__xpdl_BasicTypeType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl_TypeDeclarationType21"):
                opp_val = getattr(old_value, "xpdl_TypeDeclarationType21", None)
                if opp_val == self:
                    setattr(old_value, "xpdl_TypeDeclarationType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl_TypeDeclarationType21"):
                opp_val = getattr(value, "xpdl_TypeDeclarationType21", None)
                setattr(value, "xpdl_TypeDeclarationType21", self)
