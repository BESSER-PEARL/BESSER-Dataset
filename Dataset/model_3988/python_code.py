from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MIFlowConditionType(Enum):
    None = "None"
    One = "One"
    All = "All"
    Complex = "Complex"
class ModeType(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class TypeType(Enum):
    STRING = "STRING"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    REFERENCE = "REFERENCE"
    DATETIME = "DATETIME"
    BOOLEAN = "BOOLEAN"
    PERFORMER = "PERFORMER"
class LoopTypeType(Enum):
    Standard = "Standard"
    MultiInstance = "MultiInstance"
class MIOrderingType(Enum):
    Sequential = "Sequential"
    Parallel = "Parallel"
class TestTimeType(Enum):
    Before = "Before"
    After = "After"


############################################
# Definition of Classes
############################################

class xpdl2_extensions_LoopDataRefType:

    def __init__(self, inputItemRef: str, outputItemRef: str, loopCounterRef: str):
        self.inputItemRef = inputItemRef
        self.outputItemRef = outputItemRef
        self.loopCounterRef = loopCounterRef
        
    @property
    def outputItemRef(self) -> str:
        return self.__outputItemRef

    @outputItemRef.setter
    def outputItemRef(self, outputItemRef: str):
        self.__outputItemRef = outputItemRef

    @property
    def loopCounterRef(self) -> str:
        return self.__loopCounterRef

    @loopCounterRef.setter
    def loopCounterRef(self, loopCounterRef: str):
        self.__loopCounterRef = loopCounterRef

    @property
    def inputItemRef(self) -> str:
        return self.__inputItemRef

    @inputItemRef.setter
    def inputItemRef(self, inputItemRef: str):
        self.__inputItemRef = inputItemRef

class XSDAnnotation:

    pass
class xpdl2_extensions_ExtendedAnnotationType(XSDAnnotation):

    pass
class xpdl2_XpdlTypeType(ABC):

    pass
class xpdl2_ScriptType:

    def __init__(self, type: str, version: str, grammar: str):
        self.type = type
        self.version = version
        self.grammar = grammar
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def grammar(self) -> str:
        return self.__grammar

    @grammar.setter
    def grammar(self, grammar: str):
        self.__grammar = grammar

class xpdl2_XSDSchema:

    pass
class xpdl2_TypeDeclarationsType:

    def __init__(self, xpdl2_TypeDeclarationsType: set["xpdl2_TypeDeclarationType"] = None):
        self.xpdl2_TypeDeclarationsType = xpdl2_TypeDeclarationsType if xpdl2_TypeDeclarationsType is not None else set()
        
    @property
    def xpdl2_TypeDeclarationsType(self):
        return self.__xpdl2_TypeDeclarationsType

    @xpdl2_TypeDeclarationsType.setter
    def xpdl2_TypeDeclarationsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationsType__xpdl2_TypeDeclarationsType", None)
        self.__xpdl2_TypeDeclarationsType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl2_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl2_TypeDeclarationType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl2_TypeDeclarationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl2_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl2_TypeDeclarationType", None)
                    
                    setattr(item, "xpdl2_TypeDeclarationType", self)
                    

    def getTypeDeclaration(self, typeId: str) -> str:
        # TODO: Implement getTypeDeclaration method
        pass

class xpdl2_LoopMultiInstanceType:

    def __init__(self, mIFlowCondition: str, mIOrdering: str, xpdl2_LoopMultiInstanceType: "xpdl2_ExpressionType" = None, xpdl2_LoopMultiInstanceType19: "xpdl2_ExpressionType" = None, xpdl2_LoopMultiInstanceType22: "LoopDataRefType" = None, xpdl2_LoopMultiInstanceType29: "xpdl2_LoopType" = None):
        self.mIFlowCondition = mIFlowCondition
        self.mIOrdering = mIOrdering
        self.xpdl2_LoopMultiInstanceType = xpdl2_LoopMultiInstanceType
        self.xpdl2_LoopMultiInstanceType19 = xpdl2_LoopMultiInstanceType19
        self.xpdl2_LoopMultiInstanceType22 = xpdl2_LoopMultiInstanceType22
        self.xpdl2_LoopMultiInstanceType29 = xpdl2_LoopMultiInstanceType29
        
    @property
    def mIFlowCondition(self) -> str:
        return self.__mIFlowCondition

    @mIFlowCondition.setter
    def mIFlowCondition(self, mIFlowCondition: str):
        self.__mIFlowCondition = mIFlowCondition

    @property
    def mIOrdering(self) -> str:
        return self.__mIOrdering

    @mIOrdering.setter
    def mIOrdering(self, mIOrdering: str):
        self.__mIOrdering = mIOrdering

    @property
    def xpdl2_LoopMultiInstanceType(self):
        return self.__xpdl2_LoopMultiInstanceType

    @xpdl2_LoopMultiInstanceType.setter
    def xpdl2_LoopMultiInstanceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopMultiInstanceType__xpdl2_LoopMultiInstanceType", None)
        self.__xpdl2_LoopMultiInstanceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExpressionType"):
                opp_val = getattr(old_value, "xpdl2_ExpressionType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_ExpressionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExpressionType"):
                opp_val = getattr(value, "xpdl2_ExpressionType", None)
                setattr(value, "xpdl2_ExpressionType", self)

    @property
    def xpdl2_LoopMultiInstanceType29(self):
        return self.__xpdl2_LoopMultiInstanceType29

    @xpdl2_LoopMultiInstanceType29.setter
    def xpdl2_LoopMultiInstanceType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopMultiInstanceType__xpdl2_LoopMultiInstanceType29", None)
        self.__xpdl2_LoopMultiInstanceType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopType28"):
                opp_val = getattr(old_value, "xpdl2_LoopType28", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopType28"):
                opp_val = getattr(value, "xpdl2_LoopType28", None)
                setattr(value, "xpdl2_LoopType28", self)

    @property
    def xpdl2_LoopMultiInstanceType22(self):
        return self.__xpdl2_LoopMultiInstanceType22

    @xpdl2_LoopMultiInstanceType22.setter
    def xpdl2_LoopMultiInstanceType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopMultiInstanceType__xpdl2_LoopMultiInstanceType22", None)
        self.__xpdl2_LoopMultiInstanceType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoopDataRefType"):
                opp_val = getattr(old_value, "LoopDataRefType", None)
                if opp_val == self:
                    setattr(old_value, "LoopDataRefType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoopDataRefType"):
                opp_val = getattr(value, "LoopDataRefType", None)
                setattr(value, "LoopDataRefType", self)

    @property
    def xpdl2_LoopMultiInstanceType19(self):
        return self.__xpdl2_LoopMultiInstanceType19

    @xpdl2_LoopMultiInstanceType19.setter
    def xpdl2_LoopMultiInstanceType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopMultiInstanceType__xpdl2_LoopMultiInstanceType19", None)
        self.__xpdl2_LoopMultiInstanceType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExpressionType20"):
                opp_val = getattr(old_value, "xpdl2_ExpressionType20", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_ExpressionType20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExpressionType20"):
                opp_val = getattr(value, "xpdl2_ExpressionType20", None)
                setattr(value, "xpdl2_ExpressionType20", self)

class xpdl2_LoopType:

    def __init__(self, loopType: str, xpdl2_LoopType: "xpdl2_LoopStandardType" = None, xpdl2_LoopType28: "xpdl2_LoopMultiInstanceType" = None):
        self.loopType = loopType
        self.xpdl2_LoopType = xpdl2_LoopType
        self.xpdl2_LoopType28 = xpdl2_LoopType28
        
    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

    @property
    def xpdl2_LoopType(self):
        return self.__xpdl2_LoopType

    @xpdl2_LoopType.setter
    def xpdl2_LoopType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopType__xpdl2_LoopType", None)
        self.__xpdl2_LoopType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopStandardType26"):
                opp_val = getattr(old_value, "xpdl2_LoopStandardType26", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopStandardType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopStandardType26"):
                opp_val = getattr(value, "xpdl2_LoopStandardType26", None)
                setattr(value, "xpdl2_LoopStandardType26", self)

    @property
    def xpdl2_LoopType28(self):
        return self.__xpdl2_LoopType28

    @xpdl2_LoopType28.setter
    def xpdl2_LoopType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopType__xpdl2_LoopType28", None)
        self.__xpdl2_LoopType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopMultiInstanceType29"):
                opp_val = getattr(old_value, "xpdl2_LoopMultiInstanceType29", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopMultiInstanceType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopMultiInstanceType29"):
                opp_val = getattr(value, "xpdl2_LoopMultiInstanceType29", None)
                setattr(value, "xpdl2_LoopMultiInstanceType29", self)

class xpdl2_LoopStandardType:

    def __init__(self, loopMaximum: str, testTime: str, xpdl2_LoopStandardType: "xpdl2_ExpressionType" = None, xpdl2_LoopStandardType26: "xpdl2_LoopType" = None):
        self.loopMaximum = loopMaximum
        self.testTime = testTime
        self.xpdl2_LoopStandardType = xpdl2_LoopStandardType
        self.xpdl2_LoopStandardType26 = xpdl2_LoopStandardType26
        
    @property
    def testTime(self) -> str:
        return self.__testTime

    @testTime.setter
    def testTime(self, testTime: str):
        self.__testTime = testTime

    @property
    def loopMaximum(self) -> str:
        return self.__loopMaximum

    @loopMaximum.setter
    def loopMaximum(self, loopMaximum: str):
        self.__loopMaximum = loopMaximum

    @property
    def xpdl2_LoopStandardType(self):
        return self.__xpdl2_LoopStandardType

    @xpdl2_LoopStandardType.setter
    def xpdl2_LoopStandardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopStandardType__xpdl2_LoopStandardType", None)
        self.__xpdl2_LoopStandardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExpressionType24"):
                opp_val = getattr(old_value, "xpdl2_ExpressionType24", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_ExpressionType24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExpressionType24"):
                opp_val = getattr(value, "xpdl2_ExpressionType24", None)
                setattr(value, "xpdl2_ExpressionType24", self)

    @property
    def xpdl2_LoopStandardType26(self):
        return self.__xpdl2_LoopStandardType26

    @xpdl2_LoopStandardType26.setter
    def xpdl2_LoopStandardType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_LoopStandardType__xpdl2_LoopStandardType26", None)
        self.__xpdl2_LoopStandardType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopType"):
                opp_val = getattr(old_value, "xpdl2_LoopType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopType"):
                opp_val = getattr(value, "xpdl2_LoopType", None)
                setattr(value, "xpdl2_LoopType", self)

class LoopDataRefType:

    pass
class Extensible:

    pass
class xpdl2_TypeDeclarationType(Extensible):

    def __init__(self, description: str, id: str, name: str, xpdl2_TypeDeclarationType: "xpdl2_TypeDeclarationsType" = None, xpdl2_TypeDeclarationType34: "xpdl2_BasicTypeType" = None, xpdl2_TypeDeclarationType37: "xpdl2_DeclaredTypeType" = None, xpdl2_TypeDeclarationType40: "xpdl2_SchemaTypeType" = None, xpdl2_TypeDeclarationType43: "xpdl2_ExternalReferenceType" = None):
        self.description = description
        self.id = id
        self.name = name
        self.xpdl2_TypeDeclarationType = xpdl2_TypeDeclarationType
        self.xpdl2_TypeDeclarationType34 = xpdl2_TypeDeclarationType34
        self.xpdl2_TypeDeclarationType37 = xpdl2_TypeDeclarationType37
        self.xpdl2_TypeDeclarationType40 = xpdl2_TypeDeclarationType40
        self.xpdl2_TypeDeclarationType43 = xpdl2_TypeDeclarationType43
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xpdl2_TypeDeclarationType43(self):
        return self.__xpdl2_TypeDeclarationType43

    @xpdl2_TypeDeclarationType43.setter
    def xpdl2_TypeDeclarationType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationType__xpdl2_TypeDeclarationType43", None)
        self.__xpdl2_TypeDeclarationType43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExternalReferenceType44"):
                opp_val = getattr(old_value, "xpdl2_ExternalReferenceType44", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_ExternalReferenceType44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExternalReferenceType44"):
                opp_val = getattr(value, "xpdl2_ExternalReferenceType44", None)
                setattr(value, "xpdl2_ExternalReferenceType44", self)

    @property
    def xpdl2_TypeDeclarationType(self):
        return self.__xpdl2_TypeDeclarationType

    @xpdl2_TypeDeclarationType.setter
    def xpdl2_TypeDeclarationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationType__xpdl2_TypeDeclarationType", None)
        self.__xpdl2_TypeDeclarationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_TypeDeclarationsType"):
                opp_val = getattr(old_value, "xpdl2_TypeDeclarationsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_TypeDeclarationsType"):
                opp_val = getattr(value, "xpdl2_TypeDeclarationsType", None)
                if opp_val is None:
                    setattr(value, "xpdl2_TypeDeclarationsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl2_TypeDeclarationType37(self):
        return self.__xpdl2_TypeDeclarationType37

    @xpdl2_TypeDeclarationType37.setter
    def xpdl2_TypeDeclarationType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationType__xpdl2_TypeDeclarationType37", None)
        self.__xpdl2_TypeDeclarationType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DeclaredTypeType38"):
                opp_val = getattr(old_value, "xpdl2_DeclaredTypeType38", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DeclaredTypeType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DeclaredTypeType38"):
                opp_val = getattr(value, "xpdl2_DeclaredTypeType38", None)
                setattr(value, "xpdl2_DeclaredTypeType38", self)

    @property
    def xpdl2_TypeDeclarationType40(self):
        return self.__xpdl2_TypeDeclarationType40

    @xpdl2_TypeDeclarationType40.setter
    def xpdl2_TypeDeclarationType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationType__xpdl2_TypeDeclarationType40", None)
        self.__xpdl2_TypeDeclarationType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_SchemaTypeType41"):
                opp_val = getattr(old_value, "xpdl2_SchemaTypeType41", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_SchemaTypeType41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_SchemaTypeType41"):
                opp_val = getattr(value, "xpdl2_SchemaTypeType41", None)
                setattr(value, "xpdl2_SchemaTypeType41", self)

    @property
    def xpdl2_TypeDeclarationType34(self):
        return self.__xpdl2_TypeDeclarationType34

    @xpdl2_TypeDeclarationType34.setter
    def xpdl2_TypeDeclarationType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_TypeDeclarationType__xpdl2_TypeDeclarationType34", None)
        self.__xpdl2_TypeDeclarationType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_BasicTypeType35"):
                opp_val = getattr(old_value, "xpdl2_BasicTypeType35", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_BasicTypeType35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_BasicTypeType35"):
                opp_val = getattr(value, "xpdl2_BasicTypeType35", None)
                setattr(value, "xpdl2_BasicTypeType35", self)

    def getSchema(self) -> str:
        # TODO: Implement getSchema method
        pass

    def getDataType(self) -> XpdlTypeType:
        # TODO: Implement getDataType method
        pass

class xpdl2_ExternalPackage(Extensible):

    def __init__(self, href: str, id: str, name: str, xpdl2_ExternalPackage: "xpdl2_ExternalPackages" = None):
        self.href = href
        self.id = id
        self.name = name
        self.xpdl2_ExternalPackage = xpdl2_ExternalPackage
        
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
    def xpdl2_ExternalPackage(self):
        return self.__xpdl2_ExternalPackage

    @xpdl2_ExternalPackage.setter
    def xpdl2_ExternalPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExternalPackage__xpdl2_ExternalPackage", None)
        self.__xpdl2_ExternalPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExternalPackages"):
                opp_val = getattr(old_value, "xpdl2_ExternalPackages", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExternalPackages"):
                opp_val = getattr(value, "xpdl2_ExternalPackages", None)
                if opp_val is None:
                    setattr(value, "xpdl2_ExternalPackages", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl2_ExternalPackages:

    def __init__(self, xpdl2_ExternalPackages: set["xpdl2_ExternalPackage"] = None):
        self.xpdl2_ExternalPackages = xpdl2_ExternalPackages if xpdl2_ExternalPackages is not None else set()
        
    @property
    def xpdl2_ExternalPackages(self):
        return self.__xpdl2_ExternalPackages

    @xpdl2_ExternalPackages.setter
    def xpdl2_ExternalPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExternalPackages__xpdl2_ExternalPackages", None)
        self.__xpdl2_ExternalPackages = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl2_ExternalPackage"):
                    opp_val = getattr(item, "xpdl2_ExternalPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl2_ExternalPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl2_ExternalPackage"):
                    opp_val = getattr(item, "xpdl2_ExternalPackage", None)
                    
                    setattr(item, "xpdl2_ExternalPackage", self)
                    

    def getExternalPackage(self, packageId: str) -> str:
        # TODO: Implement getExternalPackage method
        pass

class xpdl2_Extensible(ABC):

    pass
class xpdl2_FormalParameterType:

    def __init__(self, description: str, id: str, mode: str, name: str, xpdl2_FormalParameterType: "xpdl2_FormalParametersType" = None, xpdl2_FormalParameterType15: "xpdl2_DataTypeType" = None):
        self.description = description
        self.id = id
        self.mode = mode
        self.name = name
        self.xpdl2_FormalParameterType = xpdl2_FormalParameterType
        self.xpdl2_FormalParameterType15 = xpdl2_FormalParameterType15
        
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
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def xpdl2_FormalParameterType15(self):
        return self.__xpdl2_FormalParameterType15

    @xpdl2_FormalParameterType15.setter
    def xpdl2_FormalParameterType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_FormalParameterType__xpdl2_FormalParameterType15", None)
        self.__xpdl2_FormalParameterType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DataTypeType16"):
                opp_val = getattr(old_value, "xpdl2_DataTypeType16", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DataTypeType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DataTypeType16"):
                opp_val = getattr(value, "xpdl2_DataTypeType16", None)
                setattr(value, "xpdl2_DataTypeType16", self)

    @property
    def xpdl2_FormalParameterType(self):
        return self.__xpdl2_FormalParameterType

    @xpdl2_FormalParameterType.setter
    def xpdl2_FormalParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_FormalParameterType__xpdl2_FormalParameterType", None)
        self.__xpdl2_FormalParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_FormalParametersType"):
                opp_val = getattr(old_value, "xpdl2_FormalParametersType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_FormalParametersType"):
                opp_val = getattr(value, "xpdl2_FormalParametersType", None)
                if opp_val is None:
                    setattr(value, "xpdl2_FormalParametersType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl2_FormalParametersType:

    def __init__(self, xpdl2_FormalParametersType: set["xpdl2_FormalParameterType"] = None):
        self.xpdl2_FormalParametersType = xpdl2_FormalParametersType if xpdl2_FormalParametersType is not None else set()
        
    @property
    def xpdl2_FormalParametersType(self):
        return self.__xpdl2_FormalParametersType

    @xpdl2_FormalParametersType.setter
    def xpdl2_FormalParametersType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_FormalParametersType__xpdl2_FormalParametersType", None)
        self.__xpdl2_FormalParametersType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl2_FormalParameterType"):
                    opp_val = getattr(item, "xpdl2_FormalParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl2_FormalParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl2_FormalParameterType"):
                    opp_val = getattr(item, "xpdl2_FormalParameterType", None)
                    
                    setattr(item, "xpdl2_FormalParameterType", self)
                    

    def addFormalParameter(self, parameter: str):
        # TODO: Implement addFormalParameter method
        pass

    def getFormalParameter(self, parameterId: str) -> str:
        # TODO: Implement getFormalParameter method
        pass

class xpdl2_ExpressionType:

    def __init__(self, scriptGrammar: str, scriptType: str, scriptVersion: str, mixed: str, group: str, any: str, xpdl2_ExpressionType: "xpdl2_LoopMultiInstanceType" = None, xpdl2_ExpressionType20: "xpdl2_LoopMultiInstanceType" = None, xpdl2_ExpressionType24: "xpdl2_LoopStandardType" = None):
        self.scriptGrammar = scriptGrammar
        self.scriptType = scriptType
        self.scriptVersion = scriptVersion
        self.mixed = mixed
        self.group = group
        self.any = any
        self.xpdl2_ExpressionType = xpdl2_ExpressionType
        self.xpdl2_ExpressionType20 = xpdl2_ExpressionType20
        self.xpdl2_ExpressionType24 = xpdl2_ExpressionType24
        
    @property
    def scriptType(self) -> str:
        return self.__scriptType

    @scriptType.setter
    def scriptType(self, scriptType: str):
        self.__scriptType = scriptType

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
    def scriptVersion(self) -> str:
        return self.__scriptVersion

    @scriptVersion.setter
    def scriptVersion(self, scriptVersion: str):
        self.__scriptVersion = scriptVersion

    @property
    def scriptGrammar(self) -> str:
        return self.__scriptGrammar

    @scriptGrammar.setter
    def scriptGrammar(self, scriptGrammar: str):
        self.__scriptGrammar = scriptGrammar

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xpdl2_ExpressionType20(self):
        return self.__xpdl2_ExpressionType20

    @xpdl2_ExpressionType20.setter
    def xpdl2_ExpressionType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExpressionType__xpdl2_ExpressionType20", None)
        self.__xpdl2_ExpressionType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopMultiInstanceType19"):
                opp_val = getattr(old_value, "xpdl2_LoopMultiInstanceType19", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopMultiInstanceType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopMultiInstanceType19"):
                opp_val = getattr(value, "xpdl2_LoopMultiInstanceType19", None)
                setattr(value, "xpdl2_LoopMultiInstanceType19", self)

    @property
    def xpdl2_ExpressionType(self):
        return self.__xpdl2_ExpressionType

    @xpdl2_ExpressionType.setter
    def xpdl2_ExpressionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExpressionType__xpdl2_ExpressionType", None)
        self.__xpdl2_ExpressionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopMultiInstanceType"):
                opp_val = getattr(old_value, "xpdl2_LoopMultiInstanceType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopMultiInstanceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopMultiInstanceType"):
                opp_val = getattr(value, "xpdl2_LoopMultiInstanceType", None)
                setattr(value, "xpdl2_LoopMultiInstanceType", self)

    @property
    def xpdl2_ExpressionType24(self):
        return self.__xpdl2_ExpressionType24

    @xpdl2_ExpressionType24.setter
    def xpdl2_ExpressionType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExpressionType__xpdl2_ExpressionType24", None)
        self.__xpdl2_ExpressionType24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_LoopStandardType"):
                opp_val = getattr(old_value, "xpdl2_LoopStandardType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_LoopStandardType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_LoopStandardType"):
                opp_val = getattr(value, "xpdl2_LoopStandardType", None)
                setattr(value, "xpdl2_LoopStandardType", self)

class ExtendedAnnotationType:

    pass
class xpdl2_ExtendedAttributeType:

    def __init__(self, mixed: str, group: str, any: str, name: str, value: str, xpdl2_ExtendedAttributeType: "xpdl2_ExtendedAttributesType" = None, xpdl2_ExtendedAttributeType9: "ExtendedAnnotationType" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.name = name
        self.value = value
        self.xpdl2_ExtendedAttributeType = xpdl2_ExtendedAttributeType
        self.xpdl2_ExtendedAttributeType9 = xpdl2_ExtendedAttributeType9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xpdl2_ExtendedAttributeType(self):
        return self.__xpdl2_ExtendedAttributeType

    @xpdl2_ExtendedAttributeType.setter
    def xpdl2_ExtendedAttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExtendedAttributeType__xpdl2_ExtendedAttributeType", None)
        self.__xpdl2_ExtendedAttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExtendedAttributesType"):
                opp_val = getattr(old_value, "xpdl2_ExtendedAttributesType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExtendedAttributesType"):
                opp_val = getattr(value, "xpdl2_ExtendedAttributesType", None)
                if opp_val is None:
                    setattr(value, "xpdl2_ExtendedAttributesType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl2_ExtendedAttributeType9(self):
        return self.__xpdl2_ExtendedAttributeType9

    @xpdl2_ExtendedAttributeType9.setter
    def xpdl2_ExtendedAttributeType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExtendedAttributeType__xpdl2_ExtendedAttributeType9", None)
        self.__xpdl2_ExtendedAttributeType9 = value
        
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

class xpdl2_ExtendedAttributesType:

    pass
class xpdl2_DataTypeType:

    def __init__(self, carnotType: str, xpdl2_DataTypeType: "xpdl2_BasicTypeType" = None, xpdl2_DataTypeType2: "xpdl2_DeclaredTypeType" = None, xpdl2_DataTypeType4: "xpdl2_SchemaTypeType" = None, xpdl2_DataTypeType6: "xpdl2_ExternalReferenceType" = None, xpdl2_DataTypeType16: "xpdl2_FormalParameterType" = None):
        self.carnotType = carnotType
        self.xpdl2_DataTypeType = xpdl2_DataTypeType
        self.xpdl2_DataTypeType2 = xpdl2_DataTypeType2
        self.xpdl2_DataTypeType4 = xpdl2_DataTypeType4
        self.xpdl2_DataTypeType6 = xpdl2_DataTypeType6
        self.xpdl2_DataTypeType16 = xpdl2_DataTypeType16
        
    @property
    def carnotType(self) -> str:
        return self.__carnotType

    @carnotType.setter
    def carnotType(self, carnotType: str):
        self.__carnotType = carnotType

    @property
    def xpdl2_DataTypeType(self):
        return self.__xpdl2_DataTypeType

    @xpdl2_DataTypeType.setter
    def xpdl2_DataTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DataTypeType__xpdl2_DataTypeType", None)
        self.__xpdl2_DataTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_BasicTypeType"):
                opp_val = getattr(old_value, "xpdl2_BasicTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_BasicTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_BasicTypeType"):
                opp_val = getattr(value, "xpdl2_BasicTypeType", None)
                setattr(value, "xpdl2_BasicTypeType", self)

    @property
    def xpdl2_DataTypeType6(self):
        return self.__xpdl2_DataTypeType6

    @xpdl2_DataTypeType6.setter
    def xpdl2_DataTypeType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DataTypeType__xpdl2_DataTypeType6", None)
        self.__xpdl2_DataTypeType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_ExternalReferenceType"):
                opp_val = getattr(old_value, "xpdl2_ExternalReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_ExternalReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_ExternalReferenceType"):
                opp_val = getattr(value, "xpdl2_ExternalReferenceType", None)
                setattr(value, "xpdl2_ExternalReferenceType", self)

    @property
    def xpdl2_DataTypeType16(self):
        return self.__xpdl2_DataTypeType16

    @xpdl2_DataTypeType16.setter
    def xpdl2_DataTypeType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DataTypeType__xpdl2_DataTypeType16", None)
        self.__xpdl2_DataTypeType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_FormalParameterType15"):
                opp_val = getattr(old_value, "xpdl2_FormalParameterType15", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_FormalParameterType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_FormalParameterType15"):
                opp_val = getattr(value, "xpdl2_FormalParameterType15", None)
                setattr(value, "xpdl2_FormalParameterType15", self)

    @property
    def xpdl2_DataTypeType4(self):
        return self.__xpdl2_DataTypeType4

    @xpdl2_DataTypeType4.setter
    def xpdl2_DataTypeType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DataTypeType__xpdl2_DataTypeType4", None)
        self.__xpdl2_DataTypeType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_SchemaTypeType"):
                opp_val = getattr(old_value, "xpdl2_SchemaTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_SchemaTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_SchemaTypeType"):
                opp_val = getattr(value, "xpdl2_SchemaTypeType", None)
                setattr(value, "xpdl2_SchemaTypeType", self)

    @property
    def xpdl2_DataTypeType2(self):
        return self.__xpdl2_DataTypeType2

    @xpdl2_DataTypeType2.setter
    def xpdl2_DataTypeType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DataTypeType__xpdl2_DataTypeType2", None)
        self.__xpdl2_DataTypeType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DeclaredTypeType"):
                opp_val = getattr(old_value, "xpdl2_DeclaredTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DeclaredTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DeclaredTypeType"):
                opp_val = getattr(value, "xpdl2_DeclaredTypeType", None)
                setattr(value, "xpdl2_DeclaredTypeType", self)

    def getDataType(self) -> XpdlTypeType:
        # TODO: Implement getDataType method
        pass

class XpdlTypeType:

    pass
class xpdl2_ExternalReferenceType(XpdlTypeType):

    def __init__(self, location: str, namespace: str, xref: str, uuid: str, xpdl2_ExternalReferenceType: "xpdl2_DataTypeType" = None, xpdl2_ExternalReferenceType44: "xpdl2_TypeDeclarationType" = None):
        self.location = location
        self.namespace = namespace
        self.xref = xref
        self.uuid = uuid
        self.xpdl2_ExternalReferenceType = xpdl2_ExternalReferenceType
        self.xpdl2_ExternalReferenceType44 = xpdl2_ExternalReferenceType44
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

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
    def xpdl2_ExternalReferenceType44(self):
        return self.__xpdl2_ExternalReferenceType44

    @xpdl2_ExternalReferenceType44.setter
    def xpdl2_ExternalReferenceType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExternalReferenceType__xpdl2_ExternalReferenceType44", None)
        self.__xpdl2_ExternalReferenceType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_TypeDeclarationType43"):
                opp_val = getattr(old_value, "xpdl2_TypeDeclarationType43", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_TypeDeclarationType43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_TypeDeclarationType43"):
                opp_val = getattr(value, "xpdl2_TypeDeclarationType43", None)
                setattr(value, "xpdl2_TypeDeclarationType43", self)

    @property
    def xpdl2_ExternalReferenceType(self):
        return self.__xpdl2_ExternalReferenceType

    @xpdl2_ExternalReferenceType.setter
    def xpdl2_ExternalReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_ExternalReferenceType__xpdl2_ExternalReferenceType", None)
        self.__xpdl2_ExternalReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DataTypeType6"):
                opp_val = getattr(old_value, "xpdl2_DataTypeType6", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DataTypeType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DataTypeType6"):
                opp_val = getattr(value, "xpdl2_DataTypeType6", None)
                setattr(value, "xpdl2_DataTypeType6", self)

    def getSchema(self) -> str:
        # TODO: Implement getSchema method
        pass

class xpdl2_DeclaredTypeType(XpdlTypeType):

    def __init__(self, id: str, xpdl2_DeclaredTypeType: "xpdl2_DataTypeType" = None, xpdl2_DeclaredTypeType38: "xpdl2_TypeDeclarationType" = None):
        self.id = id
        self.xpdl2_DeclaredTypeType = xpdl2_DeclaredTypeType
        self.xpdl2_DeclaredTypeType38 = xpdl2_DeclaredTypeType38
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl2_DeclaredTypeType38(self):
        return self.__xpdl2_DeclaredTypeType38

    @xpdl2_DeclaredTypeType38.setter
    def xpdl2_DeclaredTypeType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DeclaredTypeType__xpdl2_DeclaredTypeType38", None)
        self.__xpdl2_DeclaredTypeType38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_TypeDeclarationType37"):
                opp_val = getattr(old_value, "xpdl2_TypeDeclarationType37", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_TypeDeclarationType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_TypeDeclarationType37"):
                opp_val = getattr(value, "xpdl2_TypeDeclarationType37", None)
                setattr(value, "xpdl2_TypeDeclarationType37", self)

    @property
    def xpdl2_DeclaredTypeType(self):
        return self.__xpdl2_DeclaredTypeType

    @xpdl2_DeclaredTypeType.setter
    def xpdl2_DeclaredTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_DeclaredTypeType__xpdl2_DeclaredTypeType", None)
        self.__xpdl2_DeclaredTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DataTypeType2"):
                opp_val = getattr(old_value, "xpdl2_DataTypeType2", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DataTypeType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DataTypeType2"):
                opp_val = getattr(value, "xpdl2_DataTypeType2", None)
                setattr(value, "xpdl2_DataTypeType2", self)

class xpdl2_SchemaTypeType(XpdlTypeType):

    pass
class xpdl2_BasicTypeType(XpdlTypeType):

    def __init__(self, type: str, xpdl2_BasicTypeType: "xpdl2_DataTypeType" = None, xpdl2_BasicTypeType35: "xpdl2_TypeDeclarationType" = None):
        self.type = type
        self.xpdl2_BasicTypeType = xpdl2_BasicTypeType
        self.xpdl2_BasicTypeType35 = xpdl2_BasicTypeType35
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl2_BasicTypeType35(self):
        return self.__xpdl2_BasicTypeType35

    @xpdl2_BasicTypeType35.setter
    def xpdl2_BasicTypeType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_BasicTypeType__xpdl2_BasicTypeType35", None)
        self.__xpdl2_BasicTypeType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_TypeDeclarationType34"):
                opp_val = getattr(old_value, "xpdl2_TypeDeclarationType34", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_TypeDeclarationType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_TypeDeclarationType34"):
                opp_val = getattr(value, "xpdl2_TypeDeclarationType34", None)
                setattr(value, "xpdl2_TypeDeclarationType34", self)

    @property
    def xpdl2_BasicTypeType(self):
        return self.__xpdl2_BasicTypeType

    @xpdl2_BasicTypeType.setter
    def xpdl2_BasicTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl2_BasicTypeType__xpdl2_BasicTypeType", None)
        self.__xpdl2_BasicTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl2_DataTypeType"):
                opp_val = getattr(old_value, "xpdl2_DataTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl2_DataTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl2_DataTypeType"):
                opp_val = getattr(value, "xpdl2_DataTypeType", None)
                setattr(value, "xpdl2_DataTypeType", self)
