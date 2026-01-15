from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterTypes(Enum):
    STRING = "STRING"
    FLOAT = "FLOAT"
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"


############################################
# Definition of Classes
############################################

class sgen_DeprecatableElement:

    def __init__(self, deprecated: bool, comment: str):
        self.deprecated = deprecated
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def deprecated(self) -> bool:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: bool):
        self.__deprecated = deprecated

class sgen_Literal(ABC):

    pass
class Literal:

    pass
class sgen_RealLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class sgen_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sgen_IntLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class sgen_BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class sgen_FeatureParameterValue:

    def __init__(self, FeatureParameterValue: "sgen_FeatureConfiguration" = None, sgen_FeatureParameterValue: "sgen_FeatureParameter" = None, parameterValues: "sgen_FeatureConfiguration" = None, sgen_FeatureParameterValue17: "sgen_Literal" = None):
        self.FeatureParameterValue = FeatureParameterValue
        self.sgen_FeatureParameterValue = sgen_FeatureParameterValue
        self.parameterValues = parameterValues
        self.sgen_FeatureParameterValue17 = sgen_FeatureParameterValue17
        
    @property
    def sgen_FeatureParameterValue17(self):
        return self.__sgen_FeatureParameterValue17

    @sgen_FeatureParameterValue17.setter
    def sgen_FeatureParameterValue17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameterValue__sgen_FeatureParameterValue17", None)
        self.__sgen_FeatureParameterValue17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_Literal"):
                opp_val = getattr(old_value, "sgen_Literal", None)
                if opp_val == self:
                    setattr(old_value, "sgen_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_Literal"):
                opp_val = getattr(value, "sgen_Literal", None)
                setattr(value, "sgen_Literal", self)

    @property
    def FeatureParameterValue(self):
        return self.__FeatureParameterValue

    @FeatureParameterValue.setter
    def FeatureParameterValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameterValue__FeatureParameterValue", None)
        self.__FeatureParameterValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureConfiguration"):
                opp_val = getattr(old_value, "featureConfiguration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureConfiguration"):
                opp_val = getattr(value, "featureConfiguration", None)
                if opp_val is None:
                    setattr(value, "featureConfiguration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameterValues(self):
        return self.__parameterValues

    @parameterValues.setter
    def parameterValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameterValue__parameterValues", None)
        self.__parameterValues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureConfiguration"):
                opp_val = getattr(old_value, "FeatureConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "FeatureConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureConfiguration"):
                opp_val = getattr(value, "FeatureConfiguration", None)
                setattr(value, "FeatureConfiguration", self)

    @property
    def sgen_FeatureParameterValue(self):
        return self.__sgen_FeatureParameterValue

    @sgen_FeatureParameterValue.setter
    def sgen_FeatureParameterValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameterValue__sgen_FeatureParameterValue", None)
        self.__sgen_FeatureParameterValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureParameter"):
                opp_val = getattr(old_value, "sgen_FeatureParameter", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureParameter"):
                opp_val = getattr(value, "sgen_FeatureParameter", None)
                setattr(value, "sgen_FeatureParameter", self)

    def getBooleanValue(self) -> bool:
        # TODO: Implement getBooleanValue method
        pass

    def setValue(self, boolean: bool):
        # TODO: Implement setValue method
        pass

    def setValue(self, string: str):
        # TODO: Implement setValue method
        pass

    def getStringValue(self) -> str:
        # TODO: Implement getStringValue method
        pass

class sgen_EObject:

    pass
class DeprecatableElement:

    pass
class NamedElement:

    pass
class sgen_FeatureParameter(NamedElement, DeprecatableElement):

    def __init__(self, optional: bool, parameterType: str, parameters: "sgen_FeatureType" = None, FeatureParameter: "sgen_FeatureType" = None, sgen_FeatureParameter: "sgen_FeatureParameterValue" = None):
        self.optional = optional
        self.parameterType = parameterType
        self.parameters = parameters
        self.FeatureParameter = FeatureParameter
        self.sgen_FeatureParameter = sgen_FeatureParameter
        
    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def sgen_FeatureParameter(self):
        return self.__sgen_FeatureParameter

    @sgen_FeatureParameter.setter
    def sgen_FeatureParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameter__sgen_FeatureParameter", None)
        self.__sgen_FeatureParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureParameterValue"):
                opp_val = getattr(old_value, "sgen_FeatureParameterValue", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureParameterValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureParameterValue"):
                opp_val = getattr(value, "sgen_FeatureParameterValue", None)
                setattr(value, "sgen_FeatureParameterValue", self)

    @property
    def FeatureParameter(self):
        return self.__FeatureParameter

    @FeatureParameter.setter
    def FeatureParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameter__FeatureParameter", None)
        self.__FeatureParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureType"):
                opp_val = getattr(old_value, "featureType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureType"):
                opp_val = getattr(value, "featureType", None)
                if opp_val is None:
                    setattr(value, "featureType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureType"):
                opp_val = getattr(old_value, "FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureType"):
                opp_val = getattr(value, "FeatureType", None)
                setattr(value, "FeatureType", self)

class sgen_FeatureType(NamedElement, DeprecatableElement):

    def __init__(self, optional: bool, sgen_FeatureType: "sgen_FeatureTypeLibrary" = None, FeatureType: "sgen_FeatureParameter" = None, featureType: set["sgen_FeatureParameter"] = None, sgen_FeatureType7: "sgen_FeatureConfiguration" = None, sgen_FeatureType20: "sgen_FeatureTypeLibrary" = None):
        self.optional = optional
        self.sgen_FeatureType = sgen_FeatureType
        self.FeatureType = FeatureType
        self.featureType = featureType if featureType is not None else set()
        self.sgen_FeatureType7 = sgen_FeatureType7
        self.sgen_FeatureType20 = sgen_FeatureType20
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def sgen_FeatureType(self):
        return self.__sgen_FeatureType

    @sgen_FeatureType.setter
    def sgen_FeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__sgen_FeatureType", None)
        self.__sgen_FeatureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureTypeLibrary"):
                opp_val = getattr(old_value, "sgen_FeatureTypeLibrary", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureTypeLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureTypeLibrary"):
                opp_val = getattr(value, "sgen_FeatureTypeLibrary", None)
                setattr(value, "sgen_FeatureTypeLibrary", self)

    @property
    def FeatureType(self):
        return self.__FeatureType

    @FeatureType.setter
    def FeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__FeatureType", None)
        self.__FeatureType = value
        
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

    @property
    def featureType(self):
        return self.__featureType

    @featureType.setter
    def featureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__featureType", None)
        self.__featureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureParameter"):
                    opp_val = getattr(item, "FeatureParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureParameter"):
                    opp_val = getattr(item, "FeatureParameter", None)
                    
                    setattr(item, "FeatureParameter", self)
                    

    @property
    def sgen_FeatureType20(self):
        return self.__sgen_FeatureType20

    @sgen_FeatureType20.setter
    def sgen_FeatureType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__sgen_FeatureType20", None)
        self.__sgen_FeatureType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureTypeLibrary19"):
                opp_val = getattr(old_value, "sgen_FeatureTypeLibrary19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureTypeLibrary19"):
                opp_val = getattr(value, "sgen_FeatureTypeLibrary19", None)
                if opp_val is None:
                    setattr(value, "sgen_FeatureTypeLibrary19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sgen_FeatureType7(self):
        return self.__sgen_FeatureType7

    @sgen_FeatureType7.setter
    def sgen_FeatureType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__sgen_FeatureType7", None)
        self.__sgen_FeatureType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureConfiguration6"):
                opp_val = getattr(old_value, "sgen_FeatureConfiguration6", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureConfiguration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureConfiguration6"):
                opp_val = getattr(value, "sgen_FeatureConfiguration6", None)
                setattr(value, "sgen_FeatureConfiguration6", self)

class sgen_FeatureConfiguration:

    def __init__(self, sgen_FeatureConfiguration: "sgen_GeneratorConfiguration" = None, sgen_FeatureConfiguration13: "sgen_GeneratorEntry" = None, sgen_FeatureConfiguration6: "sgen_FeatureType" = None, featureConfiguration: set["sgen_FeatureParameterValue"] = None, FeatureConfiguration: "sgen_FeatureParameterValue" = None):
        self.sgen_FeatureConfiguration = sgen_FeatureConfiguration
        self.sgen_FeatureConfiguration13 = sgen_FeatureConfiguration13
        self.sgen_FeatureConfiguration6 = sgen_FeatureConfiguration6
        self.featureConfiguration = featureConfiguration if featureConfiguration is not None else set()
        self.FeatureConfiguration = FeatureConfiguration
        
    @property
    def sgen_FeatureConfiguration13(self):
        return self.__sgen_FeatureConfiguration13

    @sgen_FeatureConfiguration13.setter
    def sgen_FeatureConfiguration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__sgen_FeatureConfiguration13", None)
        self.__sgen_FeatureConfiguration13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_GeneratorEntry12"):
                opp_val = getattr(old_value, "sgen_GeneratorEntry12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_GeneratorEntry12"):
                opp_val = getattr(value, "sgen_GeneratorEntry12", None)
                if opp_val is None:
                    setattr(value, "sgen_GeneratorEntry12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sgen_FeatureConfiguration(self):
        return self.__sgen_FeatureConfiguration

    @sgen_FeatureConfiguration.setter
    def sgen_FeatureConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__sgen_FeatureConfiguration", None)
        self.__sgen_FeatureConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_GeneratorConfiguration"):
                opp_val = getattr(old_value, "sgen_GeneratorConfiguration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_GeneratorConfiguration"):
                opp_val = getattr(value, "sgen_GeneratorConfiguration", None)
                if opp_val is None:
                    setattr(value, "sgen_GeneratorConfiguration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FeatureConfiguration(self):
        return self.__FeatureConfiguration

    @FeatureConfiguration.setter
    def FeatureConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__FeatureConfiguration", None)
        self.__FeatureConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterValues"):
                opp_val = getattr(old_value, "parameterValues", None)
                if opp_val == self:
                    setattr(old_value, "parameterValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterValues"):
                opp_val = getattr(value, "parameterValues", None)
                setattr(value, "parameterValues", self)

    @property
    def featureConfiguration(self):
        return self.__featureConfiguration

    @featureConfiguration.setter
    def featureConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__featureConfiguration", None)
        self.__featureConfiguration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureParameterValue"):
                    opp_val = getattr(item, "FeatureParameterValue", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureParameterValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureParameterValue"):
                    opp_val = getattr(item, "FeatureParameterValue", None)
                    
                    setattr(item, "FeatureParameterValue", self)
                    

    @property
    def sgen_FeatureConfiguration6(self):
        return self.__sgen_FeatureConfiguration6

    @sgen_FeatureConfiguration6.setter
    def sgen_FeatureConfiguration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__sgen_FeatureConfiguration6", None)
        self.__sgen_FeatureConfiguration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureType7"):
                opp_val = getattr(old_value, "sgen_FeatureType7", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureType7"):
                opp_val = getattr(value, "sgen_FeatureType7", None)
                setattr(value, "sgen_FeatureType7", self)

    def getParameterValue(self, parameterName: str) -> str:
        # TODO: Implement getParameterValue method
        pass

class sgen_GeneratorConfiguration:

    pass
class sgen_GeneratorEntry:

    def __init__(self, contentType: str, sgen_GeneratorEntry: "sgen_GeneratorModel" = None, sgen_GeneratorEntry10: "sgen_EObject" = None, sgen_GeneratorEntry12: set["sgen_FeatureConfiguration"] = None):
        self.contentType = contentType
        self.sgen_GeneratorEntry = sgen_GeneratorEntry
        self.sgen_GeneratorEntry10 = sgen_GeneratorEntry10
        self.sgen_GeneratorEntry12 = sgen_GeneratorEntry12 if sgen_GeneratorEntry12 is not None else set()
        
    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def sgen_GeneratorEntry10(self):
        return self.__sgen_GeneratorEntry10

    @sgen_GeneratorEntry10.setter
    def sgen_GeneratorEntry10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorEntry__sgen_GeneratorEntry10", None)
        self.__sgen_GeneratorEntry10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_EObject"):
                opp_val = getattr(old_value, "sgen_EObject", None)
                if opp_val == self:
                    setattr(old_value, "sgen_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_EObject"):
                opp_val = getattr(value, "sgen_EObject", None)
                setattr(value, "sgen_EObject", self)

    @property
    def sgen_GeneratorEntry(self):
        return self.__sgen_GeneratorEntry

    @sgen_GeneratorEntry.setter
    def sgen_GeneratorEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorEntry__sgen_GeneratorEntry", None)
        self.__sgen_GeneratorEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_GeneratorModel"):
                opp_val = getattr(old_value, "sgen_GeneratorModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_GeneratorModel"):
                opp_val = getattr(value, "sgen_GeneratorModel", None)
                if opp_val is None:
                    setattr(value, "sgen_GeneratorModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sgen_GeneratorEntry12(self):
        return self.__sgen_GeneratorEntry12

    @sgen_GeneratorEntry12.setter
    def sgen_GeneratorEntry12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorEntry__sgen_GeneratorEntry12", None)
        self.__sgen_GeneratorEntry12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_FeatureConfiguration13"):
                    opp_val = getattr(item, "sgen_FeatureConfiguration13", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_FeatureConfiguration13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_FeatureConfiguration13"):
                    opp_val = getattr(item, "sgen_FeatureConfiguration13", None)
                    
                    setattr(item, "sgen_FeatureConfiguration13", self)
                    

    def getFeatureConfiguration(self, featureName: str) -> str:
        # TODO: Implement getFeatureConfiguration method
        pass

    def getFeatureParameterValue(self, paramName: str, featureName: str) -> str:
        # TODO: Implement getFeatureParameterValue method
        pass

class sgen_GeneratorModel:

    def __init__(self, generatorId: str, sgen_GeneratorModel: set["sgen_GeneratorEntry"] = None):
        self.generatorId = generatorId
        self.sgen_GeneratorModel = sgen_GeneratorModel if sgen_GeneratorModel is not None else set()
        
    @property
    def generatorId(self) -> str:
        return self.__generatorId

    @generatorId.setter
    def generatorId(self, generatorId: str):
        self.__generatorId = generatorId

    @property
    def sgen_GeneratorModel(self):
        return self.__sgen_GeneratorModel

    @sgen_GeneratorModel.setter
    def sgen_GeneratorModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorModel__sgen_GeneratorModel", None)
        self.__sgen_GeneratorModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_GeneratorEntry"):
                    opp_val = getattr(item, "sgen_GeneratorEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_GeneratorEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_GeneratorEntry"):
                    opp_val = getattr(item, "sgen_GeneratorEntry", None)
                    
                    setattr(item, "sgen_GeneratorEntry", self)
                    

class sgen_FeatureTypeLibrary:

    def __init__(self, name: str, sgen_FeatureTypeLibrary: "sgen_FeatureType" = None, sgen_FeatureTypeLibrary19: set["sgen_FeatureType"] = None):
        self.name = name
        self.sgen_FeatureTypeLibrary = sgen_FeatureTypeLibrary
        self.sgen_FeatureTypeLibrary19 = sgen_FeatureTypeLibrary19 if sgen_FeatureTypeLibrary19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sgen_FeatureTypeLibrary(self):
        return self.__sgen_FeatureTypeLibrary

    @sgen_FeatureTypeLibrary.setter
    def sgen_FeatureTypeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureTypeLibrary__sgen_FeatureTypeLibrary", None)
        self.__sgen_FeatureTypeLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureType"):
                opp_val = getattr(old_value, "sgen_FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureType"):
                opp_val = getattr(value, "sgen_FeatureType", None)
                setattr(value, "sgen_FeatureType", self)

    @property
    def sgen_FeatureTypeLibrary19(self):
        return self.__sgen_FeatureTypeLibrary19

    @sgen_FeatureTypeLibrary19.setter
    def sgen_FeatureTypeLibrary19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureTypeLibrary__sgen_FeatureTypeLibrary19", None)
        self.__sgen_FeatureTypeLibrary19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_FeatureType20"):
                    opp_val = getattr(item, "sgen_FeatureType20", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_FeatureType20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_FeatureType20"):
                    opp_val = getattr(item, "sgen_FeatureType20", None)
                    
                    setattr(item, "sgen_FeatureType20", self)
                    
