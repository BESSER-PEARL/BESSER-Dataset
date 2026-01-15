from datetime import datetime, date, time
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

class sgen_Expression:

    pass
class sgen_DeprecatableElement:

    def __init__(self, deprecated: bool, comment: str):
        self.deprecated = deprecated
        self.comment = comment
        
    @property
    def deprecated(self) -> bool:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: bool):
        self.__deprecated = deprecated

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class sgen_EObject:

    pass
class sgen_FeatureTypeLibrary:

    def __init__(self, name: str, sgen_FeatureTypeLibrary: "sgen_FeatureType" = None, sgen_FeatureTypeLibrary21: set["sgen_FeatureType"] = None):
        self.name = name
        self.sgen_FeatureTypeLibrary = sgen_FeatureTypeLibrary
        self.sgen_FeatureTypeLibrary21 = sgen_FeatureTypeLibrary21 if sgen_FeatureTypeLibrary21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sgen_FeatureTypeLibrary21(self):
        return self.__sgen_FeatureTypeLibrary21

    @sgen_FeatureTypeLibrary21.setter
    def sgen_FeatureTypeLibrary21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureTypeLibrary__sgen_FeatureTypeLibrary21", None)
        self.__sgen_FeatureTypeLibrary21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_FeatureType22"):
                    opp_val = getattr(item, "sgen_FeatureType22", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_FeatureType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_FeatureType22"):
                    opp_val = getattr(item, "sgen_FeatureType22", None)
                    
                    setattr(item, "sgen_FeatureType22", self)
                    

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
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

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

class sgen_FeatureType(NamedElement, DeprecatableElement):

    def __init__(self, optional: bool, FeatureType: "sgen_FeatureParameter" = None, sgen_FeatureType9: "sgen_FeatureConfiguration" = None, featureType: set["sgen_FeatureParameter"] = None, sgen_FeatureType: "sgen_FeatureTypeLibrary" = None, sgen_FeatureType22: "sgen_FeatureTypeLibrary" = None):
        self.optional = optional
        self.FeatureType = FeatureType
        self.sgen_FeatureType9 = sgen_FeatureType9
        self.featureType = featureType if featureType is not None else set()
        self.sgen_FeatureType = sgen_FeatureType
        self.sgen_FeatureType22 = sgen_FeatureType22
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

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
    def sgen_FeatureType22(self):
        return self.__sgen_FeatureType22

    @sgen_FeatureType22.setter
    def sgen_FeatureType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__sgen_FeatureType22", None)
        self.__sgen_FeatureType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureTypeLibrary21"):
                opp_val = getattr(old_value, "sgen_FeatureTypeLibrary21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureTypeLibrary21"):
                opp_val = getattr(value, "sgen_FeatureTypeLibrary21", None)
                if opp_val is None:
                    setattr(value, "sgen_FeatureTypeLibrary21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def sgen_FeatureType9(self):
        return self.__sgen_FeatureType9

    @sgen_FeatureType9.setter
    def sgen_FeatureType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureType__sgen_FeatureType9", None)
        self.__sgen_FeatureType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureConfiguration8"):
                opp_val = getattr(old_value, "sgen_FeatureConfiguration8", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureConfiguration8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureConfiguration8"):
                opp_val = getattr(value, "sgen_FeatureConfiguration8", None)
                setattr(value, "sgen_FeatureConfiguration8", self)

class sgen_FeatureParameterValue:

    def __init__(self, FeatureParameterValue: "sgen_FeatureConfiguration" = None, sgen_FeatureParameterValue: "sgen_FeatureParameter" = None, parameterValues: "sgen_FeatureConfiguration" = None, sgen_FeatureParameterValue19: "sgen_Expression" = None):
        self.FeatureParameterValue = FeatureParameterValue
        self.sgen_FeatureParameterValue = sgen_FeatureParameterValue
        self.parameterValues = parameterValues
        self.sgen_FeatureParameterValue19 = sgen_FeatureParameterValue19
        
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
    def sgen_FeatureParameterValue19(self):
        return self.__sgen_FeatureParameterValue19

    @sgen_FeatureParameterValue19.setter
    def sgen_FeatureParameterValue19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureParameterValue__sgen_FeatureParameterValue19", None)
        self.__sgen_FeatureParameterValue19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_Expression"):
                opp_val = getattr(old_value, "sgen_Expression", None)
                if opp_val == self:
                    setattr(old_value, "sgen_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_Expression"):
                opp_val = getattr(value, "sgen_Expression", None)
                setattr(value, "sgen_Expression", self)

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

    def getIntegerValue(self) -> int:
        # TODO: Implement getIntegerValue method
        pass

    def setValue(self, value: int):
        # TODO: Implement setValue method
        pass

    def setValue(self, boolean: bool):
        # TODO: Implement setValue method
        pass

    def getStringValue(self) -> str:
        # TODO: Implement getStringValue method
        pass

    def setValue(self, string: str):
        # TODO: Implement setValue method
        pass

    def getBooleanValue(self) -> bool:
        # TODO: Implement getBooleanValue method
        pass

class sgen_FeatureConfiguration:

    def __init__(self, sgen_FeatureConfiguration: "sgen_GeneratorConfiguration" = None, sgen_FeatureConfiguration8: "sgen_FeatureType" = None, featureConfiguration: set["sgen_FeatureParameterValue"] = None, sgen_FeatureConfiguration15: "sgen_GeneratorEntry" = None, FeatureConfiguration: "sgen_FeatureParameterValue" = None):
        self.sgen_FeatureConfiguration = sgen_FeatureConfiguration
        self.sgen_FeatureConfiguration8 = sgen_FeatureConfiguration8
        self.featureConfiguration = featureConfiguration if featureConfiguration is not None else set()
        self.sgen_FeatureConfiguration15 = sgen_FeatureConfiguration15
        self.FeatureConfiguration = FeatureConfiguration
        
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
    def sgen_FeatureConfiguration15(self):
        return self.__sgen_FeatureConfiguration15

    @sgen_FeatureConfiguration15.setter
    def sgen_FeatureConfiguration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__sgen_FeatureConfiguration15", None)
        self.__sgen_FeatureConfiguration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_GeneratorEntry14"):
                opp_val = getattr(old_value, "sgen_GeneratorEntry14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_GeneratorEntry14"):
                opp_val = getattr(value, "sgen_GeneratorEntry14", None)
                if opp_val is None:
                    setattr(value, "sgen_GeneratorEntry14", set([self]))
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
    def sgen_FeatureConfiguration8(self):
        return self.__sgen_FeatureConfiguration8

    @sgen_FeatureConfiguration8.setter
    def sgen_FeatureConfiguration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_FeatureConfiguration__sgen_FeatureConfiguration8", None)
        self.__sgen_FeatureConfiguration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgen_FeatureType9"):
                opp_val = getattr(old_value, "sgen_FeatureType9", None)
                if opp_val == self:
                    setattr(old_value, "sgen_FeatureType9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgen_FeatureType9"):
                opp_val = getattr(value, "sgen_FeatureType9", None)
                setattr(value, "sgen_FeatureType9", self)

    def getParameterValue(self, parameterName: str) -> str:
        # TODO: Implement getParameterValue method
        pass

class sgen_GeneratorConfiguration:

    pass
class sgen_Property:

    pass
class sgen_GeneratorEntry:

    def __init__(self, contentType: str, sgen_GeneratorEntry: "sgen_GeneratorModel" = None, sgen_GeneratorEntry14: set["sgen_FeatureConfiguration"] = None, sgen_GeneratorEntry12: "sgen_EObject" = None):
        self.contentType = contentType
        self.sgen_GeneratorEntry = sgen_GeneratorEntry
        self.sgen_GeneratorEntry14 = sgen_GeneratorEntry14 if sgen_GeneratorEntry14 is not None else set()
        self.sgen_GeneratorEntry12 = sgen_GeneratorEntry12
        
    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def sgen_GeneratorEntry12(self):
        return self.__sgen_GeneratorEntry12

    @sgen_GeneratorEntry12.setter
    def sgen_GeneratorEntry12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorEntry__sgen_GeneratorEntry12", None)
        self.__sgen_GeneratorEntry12 = value
        
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
    def sgen_GeneratorEntry14(self):
        return self.__sgen_GeneratorEntry14

    @sgen_GeneratorEntry14.setter
    def sgen_GeneratorEntry14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorEntry__sgen_GeneratorEntry14", None)
        self.__sgen_GeneratorEntry14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_FeatureConfiguration15"):
                    opp_val = getattr(item, "sgen_FeatureConfiguration15", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_FeatureConfiguration15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_FeatureConfiguration15"):
                    opp_val = getattr(item, "sgen_FeatureConfiguration15", None)
                    
                    setattr(item, "sgen_FeatureConfiguration15", self)
                    

    def getFeatureParameterValue(self, featureName: str, paramName: str) -> str:
        # TODO: Implement getFeatureParameterValue method
        pass

    def getFeatureConfiguration(self, featureName: str) -> str:
        # TODO: Implement getFeatureConfiguration method
        pass

class sgen_GeneratorModel:

    def __init__(self, generatorId: str, sgen_GeneratorModel: set["sgen_GeneratorEntry"] = None, sgen_GeneratorModel2: set["sgen_Property"] = None):
        self.generatorId = generatorId
        self.sgen_GeneratorModel = sgen_GeneratorModel if sgen_GeneratorModel is not None else set()
        self.sgen_GeneratorModel2 = sgen_GeneratorModel2 if sgen_GeneratorModel2 is not None else set()
        
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
                    

    @property
    def sgen_GeneratorModel2(self):
        return self.__sgen_GeneratorModel2

    @sgen_GeneratorModel2.setter
    def sgen_GeneratorModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgen_GeneratorModel__sgen_GeneratorModel2", None)
        self.__sgen_GeneratorModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgen_Property"):
                    opp_val = getattr(item, "sgen_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "sgen_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgen_Property"):
                    opp_val = getattr(item, "sgen_Property", None)
                    
                    setattr(item, "sgen_Property", self)
                    
