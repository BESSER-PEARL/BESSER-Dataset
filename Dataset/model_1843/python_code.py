from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HTTPMethods(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    HEAD = "HEAD"
    PATCH = "PATCH"
    TRACE = "TRACE"
    OPTIONS = "OPTIONS"
    CONNECT = "CONNECT"
class CollectionRealizationEnum(Enum):
    EMBEDDED_OBJECT_LIST = "EMBEDDED_OBJECT_LIST"
    REFERENCE_LINK_LIST = "REFERENCE_LINK_LIST"
class AuthenticationTypes(Enum):
    BASIC = "BASIC"
    OAUTH2 = "OAUTH2"
    CUSTOM = "CUSTOM"
class CollectionRealizationLevelEnum(Enum):
    ITEM_LEVEL = "ITEM_LEVEL"
    COLLECTION_LEVEL = "COLLECTION_LEVEL"
class ReferenceRealizationEnum(Enum):
    EMBED = "EMBED"
    LINK = "LINK"
class AuthenticationFlows(Enum):
    IMPLICIT = "IMPLICIT"
    PASSWORD = "PASSWORD"
    APPLICATION = "APPLICATION"
    ACCESS_CODE = "ACCESS_CODE"
class HttpMessageParameterLocation(Enum):
    NONE = "NONE"
    QUERY = "QUERY"
    HEADER = "HEADER"


############################################
# Definition of Classes
############################################

class Constraint:

    pass
class rapidml_ValueRangeConstraint(Constraint):

    def __init__(self, minValue: str, minValueExclusive: bool, maxValue: str, maxValueExclusive: bool):
        self.minValue = minValue
        self.minValueExclusive = minValueExclusive
        self.maxValue = maxValue
        self.maxValueExclusive = maxValueExclusive
        
    @property
    def maxValueExclusive(self) -> bool:
        return self.__maxValueExclusive

    @maxValueExclusive.setter
    def maxValueExclusive(self, maxValueExclusive: bool):
        self.__maxValueExclusive = maxValueExclusive

    @property
    def minValueExclusive(self) -> bool:
        return self.__minValueExclusive

    @minValueExclusive.setter
    def minValueExclusive(self, minValueExclusive: bool):
        self.__minValueExclusive = minValueExclusive

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

class rapidml_RegExConstraint(Constraint):

    def __init__(self, pattern: str):
        self.pattern = pattern
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class rapidml_LengthConstraint(Constraint):

    def __init__(self, minLength: int, maxLength: int, length: int):
        self.minLength = minLength
        self.maxLength = maxLength
        self.length = length
        
    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def minLength(self) -> int:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: int):
        self.__minLength = minLength

class rapidml_Element(ABC):

    def __init__(self, cardinality: str):
        self.cardinality = cardinality
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    def getDataType(self) -> str:
        # TODO: Implement getDataType method
        pass

    def isMultiValued(self) -> bool:
        # TODO: Implement isMultiValued method
        pass

    def getMaxOccurs(self) -> int:
        # TODO: Implement getMaxOccurs method
        pass

    def getMinOccurs(self) -> int:
        # TODO: Implement getMinOccurs method
        pass

class SimpleType:

    pass
class SingleValueType:

    pass
class rapidml_Enumeration(SingleValueType):

    def __init__(self, enumeration: set["rapidml_EnumConstant"] = None, rapidml_Enumeration: "rapidml_PrimitiveType" = None, Enumeration: "rapidml_EnumConstant" = None):
        self.enumeration = enumeration if enumeration is not None else set()
        self.rapidml_Enumeration = rapidml_Enumeration
        self.Enumeration = Enumeration
        
    @property
    def Enumeration(self):
        return self.__Enumeration

    @Enumeration.setter
    def Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Enumeration__Enumeration", None)
        self.__Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumConstants"):
                opp_val = getattr(old_value, "enumConstants", None)
                if opp_val == self:
                    setattr(old_value, "enumConstants", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumConstants"):
                opp_val = getattr(value, "enumConstants", None)
                setattr(value, "enumConstants", self)

    @property
    def enumeration(self):
        return self.__enumeration

    @enumeration.setter
    def enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Enumeration__enumeration", None)
        self.__enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumConstant"):
                    opp_val = getattr(item, "EnumConstant", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumConstant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumConstant"):
                    opp_val = getattr(item, "EnumConstant", None)
                    
                    setattr(item, "EnumConstant", self)
                    

    @property
    def rapidml_Enumeration(self):
        return self.__rapidml_Enumeration

    @rapidml_Enumeration.setter
    def rapidml_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Enumeration__rapidml_Enumeration", None)
        self.__rapidml_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveType158"):
                opp_val = getattr(old_value, "rapidml_PrimitiveType158", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveType158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveType158"):
                opp_val = getattr(value, "rapidml_PrimitiveType158", None)
                setattr(value, "rapidml_PrimitiveType158", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

class DataExample:

    pass
class rapidml_InlineDataExample(DataExample):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class rapidml_DataExample(ABC):

    pass
class rapidml_WithDataExamples(ABC):

    pass
class rapidml_SimpleType(SingleValueType):

    pass
class rapidml_Inheritable(ABC):

    pass
class Inheritable:

    pass
class WithDataExamples:

    pass
class DataType:

    pass
class rapidml_SingleValueType(DataType):

    def __init__(self, rapidml_SingleValueType: "rapidml_PrimitiveProperty" = None):
        self.rapidml_SingleValueType = rapidml_SingleValueType
        
    @property
    def rapidml_SingleValueType(self):
        return self.__rapidml_SingleValueType

    @rapidml_SingleValueType.setter
    def rapidml_SingleValueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SingleValueType__rapidml_SingleValueType", None)
        self.__rapidml_SingleValueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveProperty141"):
                opp_val = getattr(old_value, "rapidml_PrimitiveProperty141", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveProperty141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveProperty141"):
                opp_val = getattr(value, "rapidml_PrimitiveProperty141", None)
                setattr(value, "rapidml_PrimitiveProperty141", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

class Feature:

    pass
class Element:

    pass
class rapidml_HasTitle(ABC):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class rapidml_Extension:

    def __init__(self, name: str, value: str, rapidml_Extension: "rapidml_Extensible" = None):
        self.name = name
        self.value = value
        self.rapidml_Extension = rapidml_Extension
        
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
    def rapidml_Extension(self):
        return self.__rapidml_Extension

    @rapidml_Extension.setter
    def rapidml_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Extension__rapidml_Extension", None)
        self.__rapidml_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Extensible"):
                opp_val = getattr(old_value, "rapidml_Extensible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Extensible"):
                opp_val = getattr(value, "rapidml_Extensible", None)
                if opp_val is None:
                    setattr(value, "rapidml_Extensible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_Extensible(ABC):

    pass
class rapidml_Structure(WithDataExamples, DataType, Inheritable):

    def __init__(self, rapidml_Structure: "rapidml_RealizationContainer" = None, Structure: "rapidml_Feature" = None, rapidml_Structure136: "rapidml_ReferenceProperty" = None, rapidml_Structure151: set["rapidml_Inheritable"] = None, containingDataType: set["rapidml_Feature"] = None, rapidml_Structure145: "rapidml_Structure" = None, rapidml_Structure143: set["rapidml_Structure"] = None, rapidml_Structure147: set["rapidml_Operation"] = None, rapidml_Structure149: set["rapidml_Inheritable"] = None, rapidml_Structure163: "rapidml_ReferenceElement" = None):
        self.rapidml_Structure = rapidml_Structure
        self.Structure = Structure
        self.rapidml_Structure136 = rapidml_Structure136
        self.rapidml_Structure151 = rapidml_Structure151 if rapidml_Structure151 is not None else set()
        self.containingDataType = containingDataType if containingDataType is not None else set()
        self.rapidml_Structure145 = rapidml_Structure145
        self.rapidml_Structure143 = rapidml_Structure143 if rapidml_Structure143 is not None else set()
        self.rapidml_Structure147 = rapidml_Structure147 if rapidml_Structure147 is not None else set()
        self.rapidml_Structure149 = rapidml_Structure149 if rapidml_Structure149 is not None else set()
        self.rapidml_Structure163 = rapidml_Structure163
        
    @property
    def rapidml_Structure149(self):
        return self.__rapidml_Structure149

    @rapidml_Structure149.setter
    def rapidml_Structure149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure149", None)
        self.__rapidml_Structure149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Inheritable"):
                    opp_val = getattr(item, "rapidml_Inheritable", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Inheritable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Inheritable"):
                    opp_val = getattr(item, "rapidml_Inheritable", None)
                    
                    setattr(item, "rapidml_Inheritable", self)
                    

    @property
    def rapidml_Structure147(self):
        return self.__rapidml_Structure147

    @rapidml_Structure147.setter
    def rapidml_Structure147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure147", None)
        self.__rapidml_Structure147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Operation"):
                    opp_val = getattr(item, "rapidml_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Operation"):
                    opp_val = getattr(item, "rapidml_Operation", None)
                    
                    setattr(item, "rapidml_Operation", self)
                    

    @property
    def rapidml_Structure145(self):
        return self.__rapidml_Structure145

    @rapidml_Structure145.setter
    def rapidml_Structure145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure145", None)
        self.__rapidml_Structure145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Structure143"):
                opp_val = getattr(old_value, "rapidml_Structure143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Structure143"):
                opp_val = getattr(value, "rapidml_Structure143", None)
                if opp_val is None:
                    setattr(value, "rapidml_Structure143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containingDataType(self):
        return self.__containingDataType

    @containingDataType.setter
    def containingDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__containingDataType", None)
        self.__containingDataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def rapidml_Structure143(self):
        return self.__rapidml_Structure143

    @rapidml_Structure143.setter
    def rapidml_Structure143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure143", None)
        self.__rapidml_Structure143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Structure145"):
                    opp_val = getattr(item, "rapidml_Structure145", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Structure145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Structure145"):
                    opp_val = getattr(item, "rapidml_Structure145", None)
                    
                    setattr(item, "rapidml_Structure145", self)
                    

    @property
    def rapidml_Structure163(self):
        return self.__rapidml_Structure163

    @rapidml_Structure163.setter
    def rapidml_Structure163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure163", None)
        self.__rapidml_Structure163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceElement162"):
                opp_val = getattr(old_value, "rapidml_ReferenceElement162", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceElement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceElement162"):
                opp_val = getattr(value, "rapidml_ReferenceElement162", None)
                setattr(value, "rapidml_ReferenceElement162", self)

    @property
    def rapidml_Structure(self):
        return self.__rapidml_Structure

    @rapidml_Structure.setter
    def rapidml_Structure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure", None)
        self.__rapidml_Structure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_RealizationContainer123"):
                opp_val = getattr(old_value, "rapidml_RealizationContainer123", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_RealizationContainer123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_RealizationContainer123"):
                opp_val = getattr(value, "rapidml_RealizationContainer123", None)
                setattr(value, "rapidml_RealizationContainer123", self)

    @property
    def rapidml_Structure151(self):
        return self.__rapidml_Structure151

    @rapidml_Structure151.setter
    def rapidml_Structure151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure151", None)
        self.__rapidml_Structure151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Inheritable152"):
                    opp_val = getattr(item, "rapidml_Inheritable152", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Inheritable152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Inheritable152"):
                    opp_val = getattr(item, "rapidml_Inheritable152", None)
                    
                    setattr(item, "rapidml_Inheritable152", self)
                    

    @property
    def rapidml_Structure136(self):
        return self.__rapidml_Structure136

    @rapidml_Structure136.setter
    def rapidml_Structure136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__rapidml_Structure136", None)
        self.__rapidml_Structure136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceProperty"):
                opp_val = getattr(old_value, "rapidml_ReferenceProperty", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceProperty"):
                opp_val = getattr(value, "rapidml_ReferenceProperty", None)
                setattr(value, "rapidml_ReferenceProperty", self)

    @property
    def Structure(self):
        return self.__Structure

    @Structure.setter
    def Structure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Structure__Structure", None)
        self.__Structure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedFeatures"):
                opp_val = getattr(old_value, "ownedFeatures", None)
                if opp_val == self:
                    setattr(old_value, "ownedFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedFeatures"):
                opp_val = getattr(value, "ownedFeatures", None)
                setattr(value, "ownedFeatures", self)

    def getAllPrimitiveProperties(self) -> str:
        # TODO: Implement getAllPrimitiveProperties method
        pass

    def getPrimitiveProperties(self) -> str:
        # TODO: Implement getPrimitiveProperties method
        pass

    def getReferenceProperties(self) -> str:
        # TODO: Implement getReferenceProperties method
        pass

class rapidml_AuthenticationMethod:

    pass
class rapidml_HasSecurityValue(ABC):

    pass
class ReferenceElement:

    pass
class rapidml_ReferenceProperty(Feature, ReferenceElement):

    def __init__(self, containment: bool, container: bool, rapidml_ReferenceProperty139: "rapidml_ReferenceProperty" = None, rapidml_ReferenceProperty137: "rapidml_ReferenceProperty" = None, rapidml_ReferenceProperty: "rapidml_Structure" = None):
        self.containment = containment
        self.container = container
        self.rapidml_ReferenceProperty139 = rapidml_ReferenceProperty139
        self.rapidml_ReferenceProperty137 = rapidml_ReferenceProperty137
        self.rapidml_ReferenceProperty = rapidml_ReferenceProperty
        
    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def rapidml_ReferenceProperty139(self):
        return self.__rapidml_ReferenceProperty139

    @rapidml_ReferenceProperty139.setter
    def rapidml_ReferenceProperty139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceProperty__rapidml_ReferenceProperty139", None)
        self.__rapidml_ReferenceProperty139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceProperty137"):
                opp_val = getattr(old_value, "rapidml_ReferenceProperty137", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceProperty137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceProperty137"):
                opp_val = getattr(value, "rapidml_ReferenceProperty137", None)
                setattr(value, "rapidml_ReferenceProperty137", self)

    @property
    def rapidml_ReferenceProperty(self):
        return self.__rapidml_ReferenceProperty

    @rapidml_ReferenceProperty.setter
    def rapidml_ReferenceProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceProperty__rapidml_ReferenceProperty", None)
        self.__rapidml_ReferenceProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Structure136"):
                opp_val = getattr(old_value, "rapidml_Structure136", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Structure136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Structure136"):
                opp_val = getattr(value, "rapidml_Structure136", None)
                setattr(value, "rapidml_Structure136", self)

    @property
    def rapidml_ReferenceProperty137(self):
        return self.__rapidml_ReferenceProperty137

    @rapidml_ReferenceProperty137.setter
    def rapidml_ReferenceProperty137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceProperty__rapidml_ReferenceProperty137", None)
        self.__rapidml_ReferenceProperty137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceProperty139"):
                opp_val = getattr(old_value, "rapidml_ReferenceProperty139", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceProperty139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceProperty139"):
                opp_val = getattr(value, "rapidml_ReferenceProperty139", None)
                setattr(value, "rapidml_ReferenceProperty139", self)

class rapidml_HasStringValue(ABC):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class rapidml_Example(ABC):

    def __init__(self, rapidml_Example: "rapidml_WithExamples" = None):
        self.rapidml_Example = rapidml_Example
        
    @property
    def rapidml_Example(self):
        return self.__rapidml_Example

    @rapidml_Example.setter
    def rapidml_Example(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Example__rapidml_Example", None)
        self.__rapidml_Example = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_WithExamples"):
                opp_val = getattr(old_value, "rapidml_WithExamples", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_WithExamples"):
                opp_val = getattr(value, "rapidml_WithExamples", None)
                if opp_val is None:
                    setattr(value, "rapidml_WithExamples", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getBody(self) -> str:
        # TODO: Implement getBody method
        pass

class rapidml_WithExamples(ABC):

    pass
class Example:

    pass
class rapidml_ExternalExample(Example):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    def getBody(self) -> str:
        # TODO: Implement getBody method
        pass

class rapidml_InlineExample(Example):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class ConstrainableType:

    pass
class rapidml_UserDefinedType(SimpleType, ConstrainableType):

    def __init__(self, rapidml_UserDefinedType: "rapidml_SimpleType" = None):
        self.rapidml_UserDefinedType = rapidml_UserDefinedType
        
    @property
    def rapidml_UserDefinedType(self):
        return self.__rapidml_UserDefinedType

    @rapidml_UserDefinedType.setter
    def rapidml_UserDefinedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_UserDefinedType__rapidml_UserDefinedType", None)
        self.__rapidml_UserDefinedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SimpleType"):
                opp_val = getattr(old_value, "rapidml_SimpleType", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_SimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SimpleType"):
                opp_val = getattr(value, "rapidml_SimpleType", None)
                setattr(value, "rapidml_SimpleType", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

class rapidml_PropertyRealization(ConstrainableType):

    def __init__(self, cardinality: str, rapidml_PropertyRealization: "rapidml_Feature" = None, rapidml_PropertyRealization91: "rapidml_ObjectRealization" = None, rapidml_PropertyRealization94: "rapidml_ObjectRealization" = None):
        self.cardinality = cardinality
        self.rapidml_PropertyRealization = rapidml_PropertyRealization
        self.rapidml_PropertyRealization91 = rapidml_PropertyRealization91
        self.rapidml_PropertyRealization94 = rapidml_PropertyRealization94
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def rapidml_PropertyRealization(self):
        return self.__rapidml_PropertyRealization

    @rapidml_PropertyRealization.setter
    def rapidml_PropertyRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PropertyRealization__rapidml_PropertyRealization", None)
        self.__rapidml_PropertyRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Feature"):
                opp_val = getattr(old_value, "rapidml_Feature", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Feature"):
                opp_val = getattr(value, "rapidml_Feature", None)
                setattr(value, "rapidml_Feature", self)

    @property
    def rapidml_PropertyRealization91(self):
        return self.__rapidml_PropertyRealization91

    @rapidml_PropertyRealization91.setter
    def rapidml_PropertyRealization91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PropertyRealization__rapidml_PropertyRealization91", None)
        self.__rapidml_PropertyRealization91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ObjectRealization"):
                opp_val = getattr(old_value, "rapidml_ObjectRealization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ObjectRealization"):
                opp_val = getattr(value, "rapidml_ObjectRealization", None)
                if opp_val is None:
                    setattr(value, "rapidml_ObjectRealization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_PropertyRealization94(self):
        return self.__rapidml_PropertyRealization94

    @rapidml_PropertyRealization94.setter
    def rapidml_PropertyRealization94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PropertyRealization__rapidml_PropertyRealization94", None)
        self.__rapidml_PropertyRealization94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ObjectRealization93"):
                opp_val = getattr(old_value, "rapidml_ObjectRealization93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ObjectRealization93"):
                opp_val = getattr(value, "rapidml_ObjectRealization93", None)
                if opp_val is None:
                    setattr(value, "rapidml_ObjectRealization93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getMaxOccurs(self) -> int:
        # TODO: Implement getMaxOccurs method
        pass

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

    def getMinOccurs(self) -> int:
        # TODO: Implement getMinOccurs method
        pass

class URISegment:

    pass
class HasStringValue:

    pass
class rapidml_URISegment(HasStringValue):

    def __init__(self, name: str, rapidml_URISegment: "rapidml_URI" = None):
        self.name = name
        self.rapidml_URISegment = rapidml_URISegment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_URISegment(self):
        return self.__rapidml_URISegment

    @rapidml_URISegment.setter
    def rapidml_URISegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_URISegment__rapidml_URISegment", None)
        self.__rapidml_URISegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_URI83"):
                opp_val = getattr(old_value, "rapidml_URI83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_URI83"):
                opp_val = getattr(value, "rapidml_URI83", None)
                if opp_val is None:
                    setattr(value, "rapidml_URI83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_PrimitiveType(SimpleType):

    def __init__(self, rapidml_PrimitiveType: "rapidml_PrimitiveTypeSourceReference" = None, rapidml_PrimitiveType133: "rapidml_PrimitiveTypesLibrary" = None, rapidml_PrimitiveType158: "rapidml_Enumeration" = None):
        self.rapidml_PrimitiveType = rapidml_PrimitiveType
        self.rapidml_PrimitiveType133 = rapidml_PrimitiveType133
        self.rapidml_PrimitiveType158 = rapidml_PrimitiveType158
        
    @property
    def rapidml_PrimitiveType158(self):
        return self.__rapidml_PrimitiveType158

    @rapidml_PrimitiveType158.setter
    def rapidml_PrimitiveType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveType__rapidml_PrimitiveType158", None)
        self.__rapidml_PrimitiveType158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Enumeration"):
                opp_val = getattr(old_value, "rapidml_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Enumeration"):
                opp_val = getattr(value, "rapidml_Enumeration", None)
                setattr(value, "rapidml_Enumeration", self)

    @property
    def rapidml_PrimitiveType133(self):
        return self.__rapidml_PrimitiveType133

    @rapidml_PrimitiveType133.setter
    def rapidml_PrimitiveType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveType__rapidml_PrimitiveType133", None)
        self.__rapidml_PrimitiveType133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveTypesLibrary132"):
                opp_val = getattr(old_value, "rapidml_PrimitiveTypesLibrary132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveTypesLibrary132"):
                opp_val = getattr(value, "rapidml_PrimitiveTypesLibrary132", None)
                if opp_val is None:
                    setattr(value, "rapidml_PrimitiveTypesLibrary132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_PrimitiveType(self):
        return self.__rapidml_PrimitiveType

    @rapidml_PrimitiveType.setter
    def rapidml_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveType__rapidml_PrimitiveType", None)
        self.__rapidml_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveTypeSourceReference"):
                opp_val = getattr(old_value, "rapidml_PrimitiveTypeSourceReference", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveTypeSourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveTypeSourceReference"):
                opp_val = getattr(value, "rapidml_PrimitiveTypeSourceReference", None)
                setattr(value, "rapidml_PrimitiveTypeSourceReference", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

class ObjectRealization:

    pass
class ReferenceTreatment:

    pass
class rapidml_ReferenceEmbed(ReferenceTreatment):

    def __init__(self):
        
    def getNestedReferenceTreatments(self) -> ReferenceTreatment:
        # TODO: Implement getNestedReferenceTreatments method
        pass

    def getAllNestedReferenceTreatments(self) -> ReferenceTreatment:
        # TODO: Implement getAllNestedReferenceTreatments method
        pass

class rapidml_ReferenceLink(ReferenceTreatment):

    def __init__(self, name: str, collectionRealizationLevel: str, rapidml_ReferenceLink: "rapidml_LinkRelation" = None):
        self.name = name
        self.collectionRealizationLevel = collectionRealizationLevel
        self.rapidml_ReferenceLink = rapidml_ReferenceLink
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def collectionRealizationLevel(self) -> str:
        return self.__collectionRealizationLevel

    @collectionRealizationLevel.setter
    def collectionRealizationLevel(self, collectionRealizationLevel: str):
        self.__collectionRealizationLevel = collectionRealizationLevel

    @property
    def rapidml_ReferenceLink(self):
        return self.__rapidml_ReferenceLink

    @rapidml_ReferenceLink.setter
    def rapidml_ReferenceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceLink__rapidml_ReferenceLink", None)
        self.__rapidml_ReferenceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_LinkRelation78"):
                opp_val = getattr(old_value, "rapidml_LinkRelation78", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_LinkRelation78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_LinkRelation78"):
                opp_val = getattr(value, "rapidml_LinkRelation78", None)
                setattr(value, "rapidml_LinkRelation78", self)

    def getTargetResource(self) -> ResourceDefinition:
        # TODO: Implement getTargetResource method
        pass

class rapidml_PathSegment(ABC):

    pass
class rapidml_ReferenceElement(Element):

    def __init__(self, rapidml_ReferenceElement: "rapidml_ReferenceTreatment" = None, rapidml_ReferenceElement80: "rapidml_PathSegment" = None, rapidml_ReferenceElement162: "rapidml_Structure" = None):
        self.rapidml_ReferenceElement = rapidml_ReferenceElement
        self.rapidml_ReferenceElement80 = rapidml_ReferenceElement80
        self.rapidml_ReferenceElement162 = rapidml_ReferenceElement162
        
    @property
    def rapidml_ReferenceElement(self):
        return self.__rapidml_ReferenceElement

    @rapidml_ReferenceElement.setter
    def rapidml_ReferenceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceElement__rapidml_ReferenceElement", None)
        self.__rapidml_ReferenceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceTreatment"):
                opp_val = getattr(old_value, "rapidml_ReferenceTreatment", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceTreatment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceTreatment"):
                opp_val = getattr(value, "rapidml_ReferenceTreatment", None)
                setattr(value, "rapidml_ReferenceTreatment", self)

    @property
    def rapidml_ReferenceElement80(self):
        return self.__rapidml_ReferenceElement80

    @rapidml_ReferenceElement80.setter
    def rapidml_ReferenceElement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceElement__rapidml_ReferenceElement80", None)
        self.__rapidml_ReferenceElement80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PathSegment"):
                opp_val = getattr(old_value, "rapidml_PathSegment", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PathSegment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PathSegment"):
                opp_val = getattr(value, "rapidml_PathSegment", None)
                setattr(value, "rapidml_PathSegment", self)

    @property
    def rapidml_ReferenceElement162(self):
        return self.__rapidml_ReferenceElement162

    @rapidml_ReferenceElement162.setter
    def rapidml_ReferenceElement162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceElement__rapidml_ReferenceElement162", None)
        self.__rapidml_ReferenceElement162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Structure163"):
                opp_val = getattr(old_value, "rapidml_Structure163", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Structure163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Structure163"):
                opp_val = getattr(value, "rapidml_Structure163", None)
                setattr(value, "rapidml_Structure163", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class rapidml_NamedLinkDescriptor(ObjectRealization):

    def __init__(self, default: bool, name: str, rapidml_NamedLinkDescriptor: "rapidml_ServiceDataResource" = None):
        self.default = default
        self.name = name
        self.rapidml_NamedLinkDescriptor = rapidml_NamedLinkDescriptor
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_NamedLinkDescriptor(self):
        return self.__rapidml_NamedLinkDescriptor

    @rapidml_NamedLinkDescriptor.setter
    def rapidml_NamedLinkDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_NamedLinkDescriptor__rapidml_NamedLinkDescriptor", None)
        self.__rapidml_NamedLinkDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ServiceDataResource"):
                opp_val = getattr(old_value, "rapidml_ServiceDataResource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ServiceDataResource"):
                opp_val = getattr(value, "rapidml_ServiceDataResource", None)
                if opp_val is None:
                    setattr(value, "rapidml_ServiceDataResource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ResourceDefinition:

    pass
class rapidml_RealizationModelLocation:

    def __init__(self, uri: str, rapidml_RealizationModelLocation: "rapidml_ResourceAPI" = None):
        self.uri = uri
        self.rapidml_RealizationModelLocation = rapidml_RealizationModelLocation
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def rapidml_RealizationModelLocation(self):
        return self.__rapidml_RealizationModelLocation

    @rapidml_RealizationModelLocation.setter
    def rapidml_RealizationModelLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationModelLocation__rapidml_RealizationModelLocation", None)
        self.__rapidml_RealizationModelLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI65"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI65"):
                opp_val = getattr(value, "rapidml_ResourceAPI65", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getRealizationModel(self) -> str:
        # TODO: Implement getRealizationModel method
        pass

class rapidml_ImportDeclaration:

    def __init__(self, importURI: str, importedNamespace: str, alias: str, rapidml_ImportDeclaration: "rapidml_ZenModel" = None, rapidml_ImportDeclaration88: "rapidml_ZenModel" = None):
        self.importURI = importURI
        self.importedNamespace = importedNamespace
        self.alias = alias
        self.rapidml_ImportDeclaration = rapidml_ImportDeclaration
        self.rapidml_ImportDeclaration88 = rapidml_ImportDeclaration88
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def rapidml_ImportDeclaration88(self):
        return self.__rapidml_ImportDeclaration88

    @rapidml_ImportDeclaration88.setter
    def rapidml_ImportDeclaration88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ImportDeclaration__rapidml_ImportDeclaration88", None)
        self.__rapidml_ImportDeclaration88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel89"):
                opp_val = getattr(old_value, "rapidml_ZenModel89", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ZenModel89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel89"):
                opp_val = getattr(value, "rapidml_ZenModel89", None)
                setattr(value, "rapidml_ZenModel89", self)

    @property
    def rapidml_ImportDeclaration(self):
        return self.__rapidml_ImportDeclaration

    @rapidml_ImportDeclaration.setter
    def rapidml_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ImportDeclaration__rapidml_ImportDeclaration", None)
        self.__rapidml_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel45"):
                opp_val = getattr(old_value, "rapidml_ZenModel45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel45"):
                opp_val = getattr(value, "rapidml_ZenModel45", None)
                if opp_val is None:
                    setattr(value, "rapidml_ZenModel45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_PrimitiveTypesLibrary:

    def __init__(self, name: str, rapidml_PrimitiveTypesLibrary: "rapidml_ZenModel" = None, rapidml_PrimitiveTypesLibrary132: set["rapidml_PrimitiveType"] = None):
        self.name = name
        self.rapidml_PrimitiveTypesLibrary = rapidml_PrimitiveTypesLibrary
        self.rapidml_PrimitiveTypesLibrary132 = rapidml_PrimitiveTypesLibrary132 if rapidml_PrimitiveTypesLibrary132 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_PrimitiveTypesLibrary(self):
        return self.__rapidml_PrimitiveTypesLibrary

    @rapidml_PrimitiveTypesLibrary.setter
    def rapidml_PrimitiveTypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveTypesLibrary__rapidml_PrimitiveTypesLibrary", None)
        self.__rapidml_PrimitiveTypesLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel43"):
                opp_val = getattr(old_value, "rapidml_ZenModel43", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ZenModel43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel43"):
                opp_val = getattr(value, "rapidml_ZenModel43", None)
                setattr(value, "rapidml_ZenModel43", self)

    @property
    def rapidml_PrimitiveTypesLibrary132(self):
        return self.__rapidml_PrimitiveTypesLibrary132

    @rapidml_PrimitiveTypesLibrary132.setter
    def rapidml_PrimitiveTypesLibrary132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveTypesLibrary__rapidml_PrimitiveTypesLibrary132", None)
        self.__rapidml_PrimitiveTypesLibrary132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_PrimitiveType133"):
                    opp_val = getattr(item, "rapidml_PrimitiveType133", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_PrimitiveType133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_PrimitiveType133"):
                    opp_val = getattr(item, "rapidml_PrimitiveType133", None)
                    
                    setattr(item, "rapidml_PrimitiveType133", self)
                    

class rapidml_LinkRelationsLibrary:

    def __init__(self, name: str, rapidml_LinkRelationsLibrary: "rapidml_ZenModel" = None, rapidml_LinkRelationsLibrary129: set["rapidml_LinkRelation"] = None):
        self.name = name
        self.rapidml_LinkRelationsLibrary = rapidml_LinkRelationsLibrary
        self.rapidml_LinkRelationsLibrary129 = rapidml_LinkRelationsLibrary129 if rapidml_LinkRelationsLibrary129 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_LinkRelationsLibrary129(self):
        return self.__rapidml_LinkRelationsLibrary129

    @rapidml_LinkRelationsLibrary129.setter
    def rapidml_LinkRelationsLibrary129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_LinkRelationsLibrary__rapidml_LinkRelationsLibrary129", None)
        self.__rapidml_LinkRelationsLibrary129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_LinkRelation130"):
                    opp_val = getattr(item, "rapidml_LinkRelation130", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_LinkRelation130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_LinkRelation130"):
                    opp_val = getattr(item, "rapidml_LinkRelation130", None)
                    
                    setattr(item, "rapidml_LinkRelation130", self)
                    

    @property
    def rapidml_LinkRelationsLibrary(self):
        return self.__rapidml_LinkRelationsLibrary

    @rapidml_LinkRelationsLibrary.setter
    def rapidml_LinkRelationsLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_LinkRelationsLibrary__rapidml_LinkRelationsLibrary", None)
        self.__rapidml_LinkRelationsLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel41"):
                opp_val = getattr(old_value, "rapidml_ZenModel41", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ZenModel41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel41"):
                opp_val = getattr(value, "rapidml_ZenModel41", None)
                setattr(value, "rapidml_ZenModel41", self)

class rapidml_MediaTypesLibrary:

    pass
class HasTitle:

    pass
class rapidml_PrimitiveProperty(HasStringValue, Feature, ConstrainableType):

    def __init__(self, rapidml_PrimitiveProperty: "rapidml_PropertyReference" = None, rapidml_PrimitiveProperty141: "rapidml_SingleValueType" = None):
        self.rapidml_PrimitiveProperty = rapidml_PrimitiveProperty
        self.rapidml_PrimitiveProperty141 = rapidml_PrimitiveProperty141
        
    @property
    def rapidml_PrimitiveProperty(self):
        return self.__rapidml_PrimitiveProperty

    @rapidml_PrimitiveProperty.setter
    def rapidml_PrimitiveProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveProperty__rapidml_PrimitiveProperty", None)
        self.__rapidml_PrimitiveProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PropertyReference"):
                opp_val = getattr(old_value, "rapidml_PropertyReference", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PropertyReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PropertyReference"):
                opp_val = getattr(value, "rapidml_PropertyReference", None)
                setattr(value, "rapidml_PropertyReference", self)

    @property
    def rapidml_PrimitiveProperty141(self):
        return self.__rapidml_PrimitiveProperty141

    @rapidml_PrimitiveProperty141.setter
    def rapidml_PrimitiveProperty141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveProperty__rapidml_PrimitiveProperty141", None)
        self.__rapidml_PrimitiveProperty141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SingleValueType"):
                opp_val = getattr(old_value, "rapidml_SingleValueType", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_SingleValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SingleValueType"):
                opp_val = getattr(value, "rapidml_SingleValueType", None)
                setattr(value, "rapidml_SingleValueType", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

class SourceReference:

    pass
class rapidml_PrimitiveTypeSourceReference(SourceReference):

    def __init__(self, rapidml_PrimitiveTypeSourceReference: "rapidml_PrimitiveType" = None):
        self.rapidml_PrimitiveTypeSourceReference = rapidml_PrimitiveTypeSourceReference
        
    @property
    def rapidml_PrimitiveTypeSourceReference(self):
        return self.__rapidml_PrimitiveTypeSourceReference

    @rapidml_PrimitiveTypeSourceReference.setter
    def rapidml_PrimitiveTypeSourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PrimitiveTypeSourceReference__rapidml_PrimitiveTypeSourceReference", None)
        self.__rapidml_PrimitiveTypeSourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveType"):
                opp_val = getattr(old_value, "rapidml_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveType"):
                opp_val = getattr(value, "rapidml_PrimitiveType", None)
                setattr(value, "rapidml_PrimitiveType", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getConstraints(self) -> str:
        # TODO: Implement getConstraints method
        pass

class rapidml_PropertyReference(SourceReference):

    def __init__(self, rapidml_PropertyReference: "rapidml_PrimitiveProperty" = None):
        self.rapidml_PropertyReference = rapidml_PropertyReference
        
    @property
    def rapidml_PropertyReference(self):
        return self.__rapidml_PropertyReference

    @rapidml_PropertyReference.setter
    def rapidml_PropertyReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_PropertyReference__rapidml_PropertyReference", None)
        self.__rapidml_PropertyReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveProperty"):
                opp_val = getattr(old_value, "rapidml_PrimitiveProperty", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveProperty"):
                opp_val = getattr(value, "rapidml_PrimitiveProperty", None)
                setattr(value, "rapidml_PrimitiveProperty", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getConstraints(self) -> str:
        # TODO: Implement getConstraints method
        pass

class URIParameter:

    pass
class rapidml_TemplateParameter(URIParameter):

    pass
class rapidml_MatrixParameter(URIParameter):

    pass
class rapidml_URISegmentWithParameter(URISegment):

    pass
class Parameter:

    pass
class rapidml_URIParameter(Parameter):

    def __init__(self, rapidml_URIParameter: "rapidml_URISegmentWithParameter" = None, uriParameters: "rapidml_URI" = None, URIParameter: "rapidml_URI" = None):
        self.rapidml_URIParameter = rapidml_URIParameter
        self.uriParameters = uriParameters
        self.URIParameter = URIParameter
        
    @property
    def URIParameter(self):
        return self.__URIParameter

    @URIParameter.setter
    def URIParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_URIParameter__URIParameter", None)
        self.__URIParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingURI"):
                opp_val = getattr(old_value, "containingURI", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingURI"):
                opp_val = getattr(value, "containingURI", None)
                if opp_val is None:
                    setattr(value, "containingURI", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uriParameters(self):
        return self.__uriParameters

    @uriParameters.setter
    def uriParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_URIParameter__uriParameters", None)
        self.__uriParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI"):
                opp_val = getattr(old_value, "URI", None)
                if opp_val == self:
                    setattr(old_value, "URI", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI"):
                opp_val = getattr(value, "URI", None)
                setattr(value, "URI", self)

    @property
    def rapidml_URIParameter(self):
        return self.__rapidml_URIParameter

    @rapidml_URIParameter.setter
    def rapidml_URIParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_URIParameter__rapidml_URIParameter", None)
        self.__rapidml_URIParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_URISegmentWithParameter"):
                opp_val = getattr(old_value, "rapidml_URISegmentWithParameter", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_URISegmentWithParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_URISegmentWithParameter"):
                opp_val = getattr(value, "rapidml_URISegmentWithParameter", None)
                setattr(value, "rapidml_URISegmentWithParameter", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class TypedMessage:

    pass
class rapidml_CollectionReferenceElement(ReferenceElement):

    def __init__(self, rapidml_CollectionReferenceElement: "rapidml_CollectionResource" = None):
        self.rapidml_CollectionReferenceElement = rapidml_CollectionReferenceElement
        
    @property
    def rapidml_CollectionReferenceElement(self):
        return self.__rapidml_CollectionReferenceElement

    @rapidml_CollectionReferenceElement.setter
    def rapidml_CollectionReferenceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_CollectionReferenceElement__rapidml_CollectionReferenceElement", None)
        self.__rapidml_CollectionReferenceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_CollectionResource"):
                opp_val = getattr(old_value, "rapidml_CollectionResource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_CollectionResource"):
                opp_val = getattr(value, "rapidml_CollectionResource", None)
                if opp_val is None:
                    setattr(value, "rapidml_CollectionResource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class rapidml_CollectionParameter(Parameter):

    pass
class ServiceDataResource:

    pass
class rapidml_ObjectResource(ServiceDataResource):

    pass
class rapidml_CollectionResource(ServiceDataResource):

    def __init__(self, resourceRealizationKind: str, containingResourceDefinition29: set["rapidml_CollectionParameter"] = None, rapidml_CollectionResource: set["rapidml_CollectionReferenceElement"] = None, CollectionResource: "rapidml_CollectionParameter" = None):
        self.resourceRealizationKind = resourceRealizationKind
        self.containingResourceDefinition29 = containingResourceDefinition29 if containingResourceDefinition29 is not None else set()
        self.rapidml_CollectionResource = rapidml_CollectionResource if rapidml_CollectionResource is not None else set()
        self.CollectionResource = CollectionResource
        
    @property
    def resourceRealizationKind(self) -> str:
        return self.__resourceRealizationKind

    @resourceRealizationKind.setter
    def resourceRealizationKind(self, resourceRealizationKind: str):
        self.__resourceRealizationKind = resourceRealizationKind

    @property
    def CollectionResource(self):
        return self.__CollectionResource

    @CollectionResource.setter
    def CollectionResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_CollectionResource__CollectionResource", None)
        self.__CollectionResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "collectionParameters"):
                opp_val = getattr(old_value, "collectionParameters", None)
                if opp_val == self:
                    setattr(old_value, "collectionParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "collectionParameters"):
                opp_val = getattr(value, "collectionParameters", None)
                setattr(value, "collectionParameters", self)

    @property
    def rapidml_CollectionResource(self):
        return self.__rapidml_CollectionResource

    @rapidml_CollectionResource.setter
    def rapidml_CollectionResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_CollectionResource__rapidml_CollectionResource", None)
        self.__rapidml_CollectionResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_CollectionReferenceElement"):
                    opp_val = getattr(item, "rapidml_CollectionReferenceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_CollectionReferenceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_CollectionReferenceElement"):
                    opp_val = getattr(item, "rapidml_CollectionReferenceElement", None)
                    
                    setattr(item, "rapidml_CollectionReferenceElement", self)
                    

    @property
    def containingResourceDefinition29(self):
        return self.__containingResourceDefinition29

    @containingResourceDefinition29.setter
    def containingResourceDefinition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_CollectionResource__containingResourceDefinition29", None)
        self.__containingResourceDefinition29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionParameter"):
                    opp_val = getattr(item, "CollectionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionParameter"):
                    opp_val = getattr(item, "CollectionParameter", None)
                    
                    setattr(item, "CollectionParameter", self)
                    

class rapidml_Documentable:

    pass
class rapidml_Documentation:

    def __init__(self, text: str, rapidml_Documentation: "rapidml_Documentable" = None):
        self.text = text
        self.rapidml_Documentation = rapidml_Documentation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def rapidml_Documentation(self):
        return self.__rapidml_Documentation

    @rapidml_Documentation.setter
    def rapidml_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Documentation__rapidml_Documentation", None)
        self.__rapidml_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Documentable"):
                opp_val = getattr(old_value, "rapidml_Documentable", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Documentable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Documentable"):
                opp_val = getattr(value, "rapidml_Documentable", None)
                setattr(value, "rapidml_Documentable", self)

class Documentable:

    pass
class rapidml_LinkRelation(Documentable):

    def __init__(self, name: str, specURL: str, rapidml_LinkRelation: "rapidml_ResourceAPI" = None, rapidml_LinkRelation78: "rapidml_ReferenceLink" = None, rapidml_LinkRelation130: "rapidml_LinkRelationsLibrary" = None):
        self.name = name
        self.specURL = specURL
        self.rapidml_LinkRelation = rapidml_LinkRelation
        self.rapidml_LinkRelation78 = rapidml_LinkRelation78
        self.rapidml_LinkRelation130 = rapidml_LinkRelation130
        
    @property
    def specURL(self) -> str:
        return self.__specURL

    @specURL.setter
    def specURL(self, specURL: str):
        self.__specURL = specURL

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_LinkRelation(self):
        return self.__rapidml_LinkRelation

    @rapidml_LinkRelation.setter
    def rapidml_LinkRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_LinkRelation__rapidml_LinkRelation", None)
        self.__rapidml_LinkRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI61"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI61"):
                opp_val = getattr(value, "rapidml_ResourceAPI61", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_LinkRelation130(self):
        return self.__rapidml_LinkRelation130

    @rapidml_LinkRelation130.setter
    def rapidml_LinkRelation130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_LinkRelation__rapidml_LinkRelation130", None)
        self.__rapidml_LinkRelation130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_LinkRelationsLibrary129"):
                opp_val = getattr(old_value, "rapidml_LinkRelationsLibrary129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_LinkRelationsLibrary129"):
                opp_val = getattr(value, "rapidml_LinkRelationsLibrary129", None)
                if opp_val is None:
                    setattr(value, "rapidml_LinkRelationsLibrary129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_LinkRelation78(self):
        return self.__rapidml_LinkRelation78

    @rapidml_LinkRelation78.setter
    def rapidml_LinkRelation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_LinkRelation__rapidml_LinkRelation78", None)
        self.__rapidml_LinkRelation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceLink"):
                opp_val = getattr(old_value, "rapidml_ReferenceLink", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceLink"):
                opp_val = getattr(value, "rapidml_ReferenceLink", None)
                setattr(value, "rapidml_ReferenceLink", self)

class rapidml_SecuritySchemeParameter(Documentable):

    def __init__(self, name: str, value: str, rapidml_SecuritySchemeParameter: "rapidml_SecurityScheme" = None):
        self.name = name
        self.value = value
        self.rapidml_SecuritySchemeParameter = rapidml_SecuritySchemeParameter
        
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
    def rapidml_SecuritySchemeParameter(self):
        return self.__rapidml_SecuritySchemeParameter

    @rapidml_SecuritySchemeParameter.setter
    def rapidml_SecuritySchemeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecuritySchemeParameter__rapidml_SecuritySchemeParameter", None)
        self.__rapidml_SecuritySchemeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecurityScheme102"):
                opp_val = getattr(old_value, "rapidml_SecurityScheme102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecurityScheme102"):
                opp_val = getattr(value, "rapidml_SecurityScheme102", None)
                if opp_val is None:
                    setattr(value, "rapidml_SecurityScheme102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_SecurityScope(Documentable):

    def __init__(self, name: str, rapidml_SecurityScope: "rapidml_SecurityScheme" = None, rapidml_SecurityScope112: "rapidml_AuthenticationMethod" = None):
        self.name = name
        self.rapidml_SecurityScope = rapidml_SecurityScope
        self.rapidml_SecurityScope112 = rapidml_SecurityScope112
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_SecurityScope112(self):
        return self.__rapidml_SecurityScope112

    @rapidml_SecurityScope112.setter
    def rapidml_SecurityScope112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScope__rapidml_SecurityScope112", None)
        self.__rapidml_SecurityScope112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_AuthenticationMethod111"):
                opp_val = getattr(old_value, "rapidml_AuthenticationMethod111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_AuthenticationMethod111"):
                opp_val = getattr(value, "rapidml_AuthenticationMethod111", None)
                if opp_val is None:
                    setattr(value, "rapidml_AuthenticationMethod111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_SecurityScope(self):
        return self.__rapidml_SecurityScope

    @rapidml_SecurityScope.setter
    def rapidml_SecurityScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScope__rapidml_SecurityScope", None)
        self.__rapidml_SecurityScope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecurityScheme"):
                opp_val = getattr(old_value, "rapidml_SecurityScheme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecurityScheme"):
                opp_val = getattr(value, "rapidml_SecurityScheme", None)
                if opp_val is None:
                    setattr(value, "rapidml_SecurityScheme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_EnumConstant(Documentable):

    def __init__(self, name: str, integerValue: int, literalValue: str, EnumConstant: "rapidml_Enumeration" = None, enumConstants: "rapidml_Enumeration" = None):
        self.name = name
        self.integerValue = integerValue
        self.literalValue = literalValue
        self.EnumConstant = EnumConstant
        self.enumConstants = enumConstants
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def integerValue(self) -> int:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue

    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

    @property
    def EnumConstant(self):
        return self.__EnumConstant

    @EnumConstant.setter
    def EnumConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_EnumConstant__EnumConstant", None)
        self.__EnumConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumeration"):
                opp_val = getattr(old_value, "enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumeration"):
                opp_val = getattr(value, "enumeration", None)
                if opp_val is None:
                    setattr(value, "enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def enumConstants(self):
        return self.__enumConstants

    @enumConstants.setter
    def enumConstants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_EnumConstant__enumConstants", None)
        self.__enumConstants = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumeration"):
                opp_val = getattr(old_value, "Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumeration"):
                opp_val = getattr(value, "Enumeration", None)
                setattr(value, "Enumeration", self)

    def getImplicitIntegerValue(self) -> int:
        # TODO: Implement getImplicitIntegerValue method
        pass

class rapidml_DataModel(HasTitle, Documentable):

    def __init__(self, name: str, rapidml_DataModel: "rapidml_ZenModel" = None, rapidml_DataModel53: "rapidml_ResourceAPI" = None, rapidml_DataModel154: set["rapidml_DataType"] = None):
        self.name = name
        self.rapidml_DataModel = rapidml_DataModel
        self.rapidml_DataModel53 = rapidml_DataModel53
        self.rapidml_DataModel154 = rapidml_DataModel154 if rapidml_DataModel154 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_DataModel53(self):
        return self.__rapidml_DataModel53

    @rapidml_DataModel53.setter
    def rapidml_DataModel53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_DataModel__rapidml_DataModel53", None)
        self.__rapidml_DataModel53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI52"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI52"):
                opp_val = getattr(value, "rapidml_ResourceAPI52", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_DataModel154(self):
        return self.__rapidml_DataModel154

    @rapidml_DataModel154.setter
    def rapidml_DataModel154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_DataModel__rapidml_DataModel154", None)
        self.__rapidml_DataModel154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_DataType"):
                    opp_val = getattr(item, "rapidml_DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_DataType"):
                    opp_val = getattr(item, "rapidml_DataType", None)
                    
                    setattr(item, "rapidml_DataType", self)
                    

    @property
    def rapidml_DataModel(self):
        return self.__rapidml_DataModel

    @rapidml_DataModel.setter
    def rapidml_DataModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_DataModel__rapidml_DataModel", None)
        self.__rapidml_DataModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel37"):
                opp_val = getattr(old_value, "rapidml_ZenModel37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel37"):
                opp_val = getattr(value, "rapidml_ZenModel37", None)
                if opp_val is None:
                    setattr(value, "rapidml_ZenModel37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_Operation(Documentable):

    def __init__(self, name: str, rapidml_Operation: "rapidml_Structure" = None):
        self.name = name
        self.rapidml_Operation = rapidml_Operation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_Operation(self):
        return self.__rapidml_Operation

    @rapidml_Operation.setter
    def rapidml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Operation__rapidml_Operation", None)
        self.__rapidml_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Structure147"):
                opp_val = getattr(old_value, "rapidml_Structure147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Structure147"):
                opp_val = getattr(value, "rapidml_Structure147", None)
                if opp_val is None:
                    setattr(value, "rapidml_Structure147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_SecuritySchemeLibrary(Documentable):

    def __init__(self, name: str, rapidml_SecuritySchemeLibrary: "rapidml_ZenModel" = None, rapidml_SecuritySchemeLibrary114: set["rapidml_SecurityScheme"] = None):
        self.name = name
        self.rapidml_SecuritySchemeLibrary = rapidml_SecuritySchemeLibrary
        self.rapidml_SecuritySchemeLibrary114 = rapidml_SecuritySchemeLibrary114 if rapidml_SecuritySchemeLibrary114 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_SecuritySchemeLibrary(self):
        return self.__rapidml_SecuritySchemeLibrary

    @rapidml_SecuritySchemeLibrary.setter
    def rapidml_SecuritySchemeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecuritySchemeLibrary__rapidml_SecuritySchemeLibrary", None)
        self.__rapidml_SecuritySchemeLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel47"):
                opp_val = getattr(old_value, "rapidml_ZenModel47", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ZenModel47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel47"):
                opp_val = getattr(value, "rapidml_ZenModel47", None)
                setattr(value, "rapidml_ZenModel47", self)

    @property
    def rapidml_SecuritySchemeLibrary114(self):
        return self.__rapidml_SecuritySchemeLibrary114

    @rapidml_SecuritySchemeLibrary114.setter
    def rapidml_SecuritySchemeLibrary114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecuritySchemeLibrary__rapidml_SecuritySchemeLibrary114", None)
        self.__rapidml_SecuritySchemeLibrary114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_SecurityScheme115"):
                    opp_val = getattr(item, "rapidml_SecurityScheme115", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_SecurityScheme115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_SecurityScheme115"):
                    opp_val = getattr(item, "rapidml_SecurityScheme115", None)
                    
                    setattr(item, "rapidml_SecurityScheme115", self)
                    

class rapidml_SourceReference(ABC):

    def __init__(self, SourceReference: "rapidml_Parameter" = None, sourceReference: "rapidml_Parameter" = None):
        self.SourceReference = SourceReference
        self.sourceReference = sourceReference
        
    @property
    def SourceReference(self):
        return self.__SourceReference

    @SourceReference.setter
    def SourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SourceReference__SourceReference", None)
        self.__SourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingParameter"):
                opp_val = getattr(old_value, "containingParameter", None)
                if opp_val == self:
                    setattr(old_value, "containingParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingParameter"):
                opp_val = getattr(value, "containingParameter", None)
                setattr(value, "containingParameter", self)

    @property
    def sourceReference(self):
        return self.__sourceReference

    @sourceReference.setter
    def sourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SourceReference__sourceReference", None)
        self.__sourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter"):
                opp_val = getattr(old_value, "Parameter", None)
                if opp_val == self:
                    setattr(old_value, "Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter"):
                opp_val = getattr(value, "Parameter", None)
                setattr(value, "Parameter", self)

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getConstraints(self) -> str:
        # TODO: Implement getConstraints method
        pass

class rapidml_TypedResponse(TypedMessage):

    def __init__(self, statusCode: int, TypedResponse: "rapidml_Method" = None, responses: "rapidml_Method" = None, rapidml_TypedResponse: "rapidml_SecurityScheme" = None):
        self.statusCode = statusCode
        self.TypedResponse = TypedResponse
        self.responses = responses
        self.rapidml_TypedResponse = rapidml_TypedResponse
        
    @property
    def statusCode(self) -> int:
        return self.__statusCode

    @statusCode.setter
    def statusCode(self, statusCode: int):
        self.__statusCode = statusCode

    @property
    def rapidml_TypedResponse(self):
        return self.__rapidml_TypedResponse

    @rapidml_TypedResponse.setter
    def rapidml_TypedResponse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedResponse__rapidml_TypedResponse", None)
        self.__rapidml_TypedResponse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecurityScheme106"):
                opp_val = getattr(old_value, "rapidml_SecurityScheme106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecurityScheme106"):
                opp_val = getattr(value, "rapidml_SecurityScheme106", None)
                if opp_val is None:
                    setattr(value, "rapidml_SecurityScheme106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def responses(self):
        return self.__responses

    @responses.setter
    def responses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedResponse__responses", None)
        self.__responses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method25"):
                opp_val = getattr(old_value, "Method25", None)
                if opp_val == self:
                    setattr(old_value, "Method25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method25"):
                opp_val = getattr(value, "Method25", None)
                setattr(value, "Method25", self)

    @property
    def TypedResponse(self):
        return self.__TypedResponse

    @TypedResponse.setter
    def TypedResponse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedResponse__TypedResponse", None)
        self.__TypedResponse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingMethod15"):
                opp_val = getattr(old_value, "containingMethod15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingMethod15"):
                opp_val = getattr(value, "containingMethod15", None)
                if opp_val is None:
                    setattr(value, "containingMethod15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_TypedRequest(TypedMessage):

    pass
class Extensible:

    pass
class rapidml_Constraint(Extensible):

    def __init__(self, rapidml_Constraint: "rapidml_ConstrainableType" = None):
        self.rapidml_Constraint = rapidml_Constraint
        
    @property
    def rapidml_Constraint(self):
        return self.__rapidml_Constraint

    @rapidml_Constraint.setter
    def rapidml_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Constraint__rapidml_Constraint", None)
        self.__rapidml_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ConstrainableType"):
                opp_val = getattr(old_value, "rapidml_ConstrainableType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ConstrainableType"):
                opp_val = getattr(value, "rapidml_ConstrainableType", None)
                if opp_val is None:
                    setattr(value, "rapidml_ConstrainableType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def supports(self, type: str) -> bool:
        # TODO: Implement supports method
        pass

class rapidml_RealizationContainer(Extensible):

    def __init__(self, withDefaultRealization: bool, realizationName: str, effectiveRealization: str, RealizationContainer: "rapidml_ObjectRealization" = None, realizationContainer: "rapidml_ObjectRealization" = None, rapidml_RealizationContainer: "rapidml_ObjectRealization" = None, rapidml_RealizationContainer120: set["rapidml_ReferenceTreatment"] = None, rapidml_RealizationContainer123: "rapidml_Structure" = None):
        self.withDefaultRealization = withDefaultRealization
        self.realizationName = realizationName
        self.effectiveRealization = effectiveRealization
        self.RealizationContainer = RealizationContainer
        self.realizationContainer = realizationContainer
        self.rapidml_RealizationContainer = rapidml_RealizationContainer
        self.rapidml_RealizationContainer120 = rapidml_RealizationContainer120 if rapidml_RealizationContainer120 is not None else set()
        self.rapidml_RealizationContainer123 = rapidml_RealizationContainer123
        
    @property
    def withDefaultRealization(self) -> bool:
        return self.__withDefaultRealization

    @withDefaultRealization.setter
    def withDefaultRealization(self, withDefaultRealization: bool):
        self.__withDefaultRealization = withDefaultRealization

    @property
    def realizationName(self) -> str:
        return self.__realizationName

    @realizationName.setter
    def realizationName(self, realizationName: str):
        self.__realizationName = realizationName

    @property
    def effectiveRealization(self) -> str:
        return self.__effectiveRealization

    @effectiveRealization.setter
    def effectiveRealization(self, effectiveRealization: str):
        self.__effectiveRealization = effectiveRealization

    @property
    def rapidml_RealizationContainer120(self):
        return self.__rapidml_RealizationContainer120

    @rapidml_RealizationContainer120.setter
    def rapidml_RealizationContainer120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationContainer__rapidml_RealizationContainer120", None)
        self.__rapidml_RealizationContainer120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_ReferenceTreatment121"):
                    opp_val = getattr(item, "rapidml_ReferenceTreatment121", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_ReferenceTreatment121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_ReferenceTreatment121"):
                    opp_val = getattr(item, "rapidml_ReferenceTreatment121", None)
                    
                    setattr(item, "rapidml_ReferenceTreatment121", self)
                    

    @property
    def rapidml_RealizationContainer123(self):
        return self.__rapidml_RealizationContainer123

    @rapidml_RealizationContainer123.setter
    def rapidml_RealizationContainer123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationContainer__rapidml_RealizationContainer123", None)
        self.__rapidml_RealizationContainer123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_Structure"):
                opp_val = getattr(old_value, "rapidml_Structure", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_Structure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_Structure"):
                opp_val = getattr(value, "rapidml_Structure", None)
                setattr(value, "rapidml_Structure", self)

    @property
    def realizationContainer(self):
        return self.__realizationContainer

    @realizationContainer.setter
    def realizationContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationContainer__realizationContainer", None)
        self.__realizationContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjectRealization"):
                opp_val = getattr(old_value, "ObjectRealization", None)
                if opp_val == self:
                    setattr(old_value, "ObjectRealization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjectRealization"):
                opp_val = getattr(value, "ObjectRealization", None)
                setattr(value, "ObjectRealization", self)

    @property
    def rapidml_RealizationContainer(self):
        return self.__rapidml_RealizationContainer

    @rapidml_RealizationContainer.setter
    def rapidml_RealizationContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationContainer__rapidml_RealizationContainer", None)
        self.__rapidml_RealizationContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ObjectRealization118"):
                opp_val = getattr(old_value, "rapidml_ObjectRealization118", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ObjectRealization118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ObjectRealization118"):
                opp_val = getattr(value, "rapidml_ObjectRealization118", None)
                setattr(value, "rapidml_ObjectRealization118", self)

    @property
    def RealizationContainer(self):
        return self.__RealizationContainer

    @RealizationContainer.setter
    def RealizationContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_RealizationContainer__RealizationContainer", None)
        self.__RealizationContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inlineObjectRealization"):
                opp_val = getattr(old_value, "inlineObjectRealization", None)
                if opp_val == self:
                    setattr(old_value, "inlineObjectRealization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inlineObjectRealization"):
                opp_val = getattr(value, "inlineObjectRealization", None)
                setattr(value, "inlineObjectRealization", self)

    def getActualType(self) -> str:
        # TODO: Implement getActualType method
        pass

class rapidml_Feature(Extensible, Documentable, Element):

    def __init__(self, name: str, restriction: bool, readOnly: bool, key: bool, rapidml_Feature: "rapidml_PropertyRealization" = None, rapidml_Feature97: "rapidml_ObjectRealization" = None, ownedFeatures: "rapidml_Structure" = None, Feature: "rapidml_Structure" = None):
        self.name = name
        self.restriction = restriction
        self.readOnly = readOnly
        self.key = key
        self.rapidml_Feature = rapidml_Feature
        self.rapidml_Feature97 = rapidml_Feature97
        self.ownedFeatures = ownedFeatures
        self.Feature = Feature
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def restriction(self) -> bool:
        return self.__restriction

    @restriction.setter
    def restriction(self, restriction: bool):
        self.__restriction = restriction

    @property
    def key(self) -> bool:
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingDataType"):
                opp_val = getattr(old_value, "containingDataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingDataType"):
                opp_val = getattr(value, "containingDataType", None)
                if opp_val is None:
                    setattr(value, "containingDataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_Feature97(self):
        return self.__rapidml_Feature97

    @rapidml_Feature97.setter
    def rapidml_Feature97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Feature__rapidml_Feature97", None)
        self.__rapidml_Feature97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ObjectRealization96"):
                opp_val = getattr(old_value, "rapidml_ObjectRealization96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ObjectRealization96"):
                opp_val = getattr(value, "rapidml_ObjectRealization96", None)
                if opp_val is None:
                    setattr(value, "rapidml_ObjectRealization96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_Feature(self):
        return self.__rapidml_Feature

    @rapidml_Feature.setter
    def rapidml_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Feature__rapidml_Feature", None)
        self.__rapidml_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PropertyRealization"):
                opp_val = getattr(old_value, "rapidml_PropertyRealization", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PropertyRealization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PropertyRealization"):
                opp_val = getattr(value, "rapidml_PropertyRealization", None)
                setattr(value, "rapidml_PropertyRealization", self)

    @property
    def ownedFeatures(self):
        return self.__ownedFeatures

    @ownedFeatures.setter
    def ownedFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Feature__ownedFeatures", None)
        self.__ownedFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Structure"):
                opp_val = getattr(old_value, "Structure", None)
                if opp_val == self:
                    setattr(old_value, "Structure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Structure"):
                opp_val = getattr(value, "Structure", None)
                setattr(value, "Structure", self)

    def getMaxOccurs(self) -> int:
        # TODO: Implement getMaxOccurs method
        pass

    def getMinOccurs(self) -> int:
        # TODO: Implement getMinOccurs method
        pass

class rapidml_ZenModel(HasTitle, Extensible, Documentable):

    def __init__(self, name: str, namespace: str, rapidml_ZenModel: set["rapidml_ResourceAPI"] = None, rapidml_ZenModel37: set["rapidml_DataModel"] = None, rapidml_ZenModel39: "rapidml_MediaTypesLibrary" = None, rapidml_ZenModel41: "rapidml_LinkRelationsLibrary" = None, rapidml_ZenModel43: "rapidml_PrimitiveTypesLibrary" = None, rapidml_ZenModel45: set["rapidml_ImportDeclaration"] = None, rapidml_ZenModel47: "rapidml_SecuritySchemeLibrary" = None, rapidml_ZenModel89: "rapidml_ImportDeclaration" = None):
        self.name = name
        self.namespace = namespace
        self.rapidml_ZenModel = rapidml_ZenModel if rapidml_ZenModel is not None else set()
        self.rapidml_ZenModel37 = rapidml_ZenModel37 if rapidml_ZenModel37 is not None else set()
        self.rapidml_ZenModel39 = rapidml_ZenModel39
        self.rapidml_ZenModel41 = rapidml_ZenModel41
        self.rapidml_ZenModel43 = rapidml_ZenModel43
        self.rapidml_ZenModel45 = rapidml_ZenModel45 if rapidml_ZenModel45 is not None else set()
        self.rapidml_ZenModel47 = rapidml_ZenModel47
        self.rapidml_ZenModel89 = rapidml_ZenModel89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def rapidml_ZenModel89(self):
        return self.__rapidml_ZenModel89

    @rapidml_ZenModel89.setter
    def rapidml_ZenModel89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel89", None)
        self.__rapidml_ZenModel89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ImportDeclaration88"):
                opp_val = getattr(old_value, "rapidml_ImportDeclaration88", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ImportDeclaration88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ImportDeclaration88"):
                opp_val = getattr(value, "rapidml_ImportDeclaration88", None)
                setattr(value, "rapidml_ImportDeclaration88", self)

    @property
    def rapidml_ZenModel41(self):
        return self.__rapidml_ZenModel41

    @rapidml_ZenModel41.setter
    def rapidml_ZenModel41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel41", None)
        self.__rapidml_ZenModel41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_LinkRelationsLibrary"):
                opp_val = getattr(old_value, "rapidml_LinkRelationsLibrary", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_LinkRelationsLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_LinkRelationsLibrary"):
                opp_val = getattr(value, "rapidml_LinkRelationsLibrary", None)
                setattr(value, "rapidml_LinkRelationsLibrary", self)

    @property
    def rapidml_ZenModel45(self):
        return self.__rapidml_ZenModel45

    @rapidml_ZenModel45.setter
    def rapidml_ZenModel45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel45", None)
        self.__rapidml_ZenModel45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_ImportDeclaration"):
                    opp_val = getattr(item, "rapidml_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_ImportDeclaration"):
                    opp_val = getattr(item, "rapidml_ImportDeclaration", None)
                    
                    setattr(item, "rapidml_ImportDeclaration", self)
                    

    @property
    def rapidml_ZenModel43(self):
        return self.__rapidml_ZenModel43

    @rapidml_ZenModel43.setter
    def rapidml_ZenModel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel43", None)
        self.__rapidml_ZenModel43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_PrimitiveTypesLibrary"):
                opp_val = getattr(old_value, "rapidml_PrimitiveTypesLibrary", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_PrimitiveTypesLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_PrimitiveTypesLibrary"):
                opp_val = getattr(value, "rapidml_PrimitiveTypesLibrary", None)
                setattr(value, "rapidml_PrimitiveTypesLibrary", self)

    @property
    def rapidml_ZenModel47(self):
        return self.__rapidml_ZenModel47

    @rapidml_ZenModel47.setter
    def rapidml_ZenModel47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel47", None)
        self.__rapidml_ZenModel47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecuritySchemeLibrary"):
                opp_val = getattr(old_value, "rapidml_SecuritySchemeLibrary", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_SecuritySchemeLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecuritySchemeLibrary"):
                opp_val = getattr(value, "rapidml_SecuritySchemeLibrary", None)
                setattr(value, "rapidml_SecuritySchemeLibrary", self)

    @property
    def rapidml_ZenModel39(self):
        return self.__rapidml_ZenModel39

    @rapidml_ZenModel39.setter
    def rapidml_ZenModel39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel39", None)
        self.__rapidml_ZenModel39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_MediaTypesLibrary"):
                opp_val = getattr(old_value, "rapidml_MediaTypesLibrary", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_MediaTypesLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_MediaTypesLibrary"):
                opp_val = getattr(value, "rapidml_MediaTypesLibrary", None)
                setattr(value, "rapidml_MediaTypesLibrary", self)

    @property
    def rapidml_ZenModel37(self):
        return self.__rapidml_ZenModel37

    @rapidml_ZenModel37.setter
    def rapidml_ZenModel37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel37", None)
        self.__rapidml_ZenModel37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_DataModel"):
                    opp_val = getattr(item, "rapidml_DataModel", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_DataModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_DataModel"):
                    opp_val = getattr(item, "rapidml_DataModel", None)
                    
                    setattr(item, "rapidml_DataModel", self)
                    

    @property
    def rapidml_ZenModel(self):
        return self.__rapidml_ZenModel

    @rapidml_ZenModel.setter
    def rapidml_ZenModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ZenModel__rapidml_ZenModel", None)
        self.__rapidml_ZenModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_ResourceAPI"):
                    opp_val = getattr(item, "rapidml_ResourceAPI", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_ResourceAPI", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_ResourceAPI"):
                    opp_val = getattr(item, "rapidml_ResourceAPI", None)
                    
                    setattr(item, "rapidml_ResourceAPI", self)
                    

class rapidml_ReferenceTreatment(Extensible):

    def __init__(self, rapidml_ReferenceTreatment: "rapidml_ReferenceElement" = None, rapidml_ReferenceTreatment69: "rapidml_ReferenceRealization" = None, rapidml_ReferenceTreatment72: "rapidml_ReferenceRealization" = None, rapidml_ReferenceTreatment121: "rapidml_RealizationContainer" = None):
        self.rapidml_ReferenceTreatment = rapidml_ReferenceTreatment
        self.rapidml_ReferenceTreatment69 = rapidml_ReferenceTreatment69
        self.rapidml_ReferenceTreatment72 = rapidml_ReferenceTreatment72
        self.rapidml_ReferenceTreatment121 = rapidml_ReferenceTreatment121
        
    @property
    def rapidml_ReferenceTreatment121(self):
        return self.__rapidml_ReferenceTreatment121

    @rapidml_ReferenceTreatment121.setter
    def rapidml_ReferenceTreatment121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceTreatment__rapidml_ReferenceTreatment121", None)
        self.__rapidml_ReferenceTreatment121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_RealizationContainer120"):
                opp_val = getattr(old_value, "rapidml_RealizationContainer120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_RealizationContainer120"):
                opp_val = getattr(value, "rapidml_RealizationContainer120", None)
                if opp_val is None:
                    setattr(value, "rapidml_RealizationContainer120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_ReferenceTreatment72(self):
        return self.__rapidml_ReferenceTreatment72

    @rapidml_ReferenceTreatment72.setter
    def rapidml_ReferenceTreatment72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceTreatment__rapidml_ReferenceTreatment72", None)
        self.__rapidml_ReferenceTreatment72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceRealization73"):
                opp_val = getattr(old_value, "rapidml_ReferenceRealization73", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceRealization73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceRealization73"):
                opp_val = getattr(value, "rapidml_ReferenceRealization73", None)
                setattr(value, "rapidml_ReferenceRealization73", self)

    @property
    def rapidml_ReferenceTreatment(self):
        return self.__rapidml_ReferenceTreatment

    @rapidml_ReferenceTreatment.setter
    def rapidml_ReferenceTreatment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceTreatment__rapidml_ReferenceTreatment", None)
        self.__rapidml_ReferenceTreatment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceElement"):
                opp_val = getattr(old_value, "rapidml_ReferenceElement", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceElement"):
                opp_val = getattr(value, "rapidml_ReferenceElement", None)
                setattr(value, "rapidml_ReferenceElement", self)

    @property
    def rapidml_ReferenceTreatment69(self):
        return self.__rapidml_ReferenceTreatment69

    @rapidml_ReferenceTreatment69.setter
    def rapidml_ReferenceTreatment69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceTreatment__rapidml_ReferenceTreatment69", None)
        self.__rapidml_ReferenceTreatment69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceRealization70"):
                opp_val = getattr(old_value, "rapidml_ReferenceRealization70", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceRealization70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceRealization70"):
                opp_val = getattr(value, "rapidml_ReferenceRealization70", None)
                setattr(value, "rapidml_ReferenceRealization70", self)

    def getEmbedHierarchy(self) -> str:
        # TODO: Implement getEmbedHierarchy method
        pass

    def getLinkDescriptor(self) -> str:
        # TODO: Implement getLinkDescriptor method
        pass

class rapidml_ConstrainableType(Extensible):

    def __init__(self, rapidml_ConstrainableType: set["rapidml_Constraint"] = None):
        self.rapidml_ConstrainableType = rapidml_ConstrainableType if rapidml_ConstrainableType is not None else set()
        
    @property
    def rapidml_ConstrainableType(self):
        return self.__rapidml_ConstrainableType

    @rapidml_ConstrainableType.setter
    def rapidml_ConstrainableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ConstrainableType__rapidml_ConstrainableType", None)
        self.__rapidml_ConstrainableType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Constraint"):
                    opp_val = getattr(item, "rapidml_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Constraint"):
                    opp_val = getattr(item, "rapidml_Constraint", None)
                    
                    setattr(item, "rapidml_Constraint", self)
                    

    def getAllConstraints(self) -> Constraint:
        # TODO: Implement getAllConstraints method
        pass

    def getConstrainableParent(self) -> ConstrainableType:
        # TODO: Implement getConstrainableParent method
        pass

class rapidml_DataType(Extensible, Documentable):

    def __init__(self, name: str, rapidml_DataType: "rapidml_DataModel" = None):
        self.name = name
        self.rapidml_DataType = rapidml_DataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_DataType(self):
        return self.__rapidml_DataType

    @rapidml_DataType.setter
    def rapidml_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_DataType__rapidml_DataType", None)
        self.__rapidml_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_DataModel154"):
                opp_val = getattr(old_value, "rapidml_DataModel154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_DataModel154"):
                opp_val = getattr(value, "rapidml_DataModel154", None)
                if opp_val is None:
                    setattr(value, "rapidml_DataModel154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rapidml_ObjectRealization(Extensible):

    def __init__(self, rapidml_ObjectRealization: set["rapidml_PropertyRealization"] = None, rapidml_ObjectRealization93: set["rapidml_PropertyRealization"] = None, rapidml_ObjectRealization96: set["rapidml_Feature"] = None, inlineObjectRealization: "rapidml_RealizationContainer" = None, ObjectRealization: "rapidml_RealizationContainer" = None, rapidml_ObjectRealization118: "rapidml_RealizationContainer" = None):
        self.rapidml_ObjectRealization = rapidml_ObjectRealization if rapidml_ObjectRealization is not None else set()
        self.rapidml_ObjectRealization93 = rapidml_ObjectRealization93 if rapidml_ObjectRealization93 is not None else set()
        self.rapidml_ObjectRealization96 = rapidml_ObjectRealization96 if rapidml_ObjectRealization96 is not None else set()
        self.inlineObjectRealization = inlineObjectRealization
        self.ObjectRealization = ObjectRealization
        self.rapidml_ObjectRealization118 = rapidml_ObjectRealization118
        
    @property
    def inlineObjectRealization(self):
        return self.__inlineObjectRealization

    @inlineObjectRealization.setter
    def inlineObjectRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__inlineObjectRealization", None)
        self.__inlineObjectRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealizationContainer"):
                opp_val = getattr(old_value, "RealizationContainer", None)
                if opp_val == self:
                    setattr(old_value, "RealizationContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealizationContainer"):
                opp_val = getattr(value, "RealizationContainer", None)
                setattr(value, "RealizationContainer", self)

    @property
    def rapidml_ObjectRealization96(self):
        return self.__rapidml_ObjectRealization96

    @rapidml_ObjectRealization96.setter
    def rapidml_ObjectRealization96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__rapidml_ObjectRealization96", None)
        self.__rapidml_ObjectRealization96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_Feature97"):
                    opp_val = getattr(item, "rapidml_Feature97", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_Feature97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_Feature97"):
                    opp_val = getattr(item, "rapidml_Feature97", None)
                    
                    setattr(item, "rapidml_Feature97", self)
                    

    @property
    def rapidml_ObjectRealization118(self):
        return self.__rapidml_ObjectRealization118

    @rapidml_ObjectRealization118.setter
    def rapidml_ObjectRealization118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__rapidml_ObjectRealization118", None)
        self.__rapidml_ObjectRealization118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_RealizationContainer"):
                opp_val = getattr(old_value, "rapidml_RealizationContainer", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_RealizationContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_RealizationContainer"):
                opp_val = getattr(value, "rapidml_RealizationContainer", None)
                setattr(value, "rapidml_RealizationContainer", self)

    @property
    def rapidml_ObjectRealization(self):
        return self.__rapidml_ObjectRealization

    @rapidml_ObjectRealization.setter
    def rapidml_ObjectRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__rapidml_ObjectRealization", None)
        self.__rapidml_ObjectRealization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_PropertyRealization91"):
                    opp_val = getattr(item, "rapidml_PropertyRealization91", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_PropertyRealization91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_PropertyRealization91"):
                    opp_val = getattr(item, "rapidml_PropertyRealization91", None)
                    
                    setattr(item, "rapidml_PropertyRealization91", self)
                    

    @property
    def ObjectRealization(self):
        return self.__ObjectRealization

    @ObjectRealization.setter
    def ObjectRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__ObjectRealization", None)
        self.__ObjectRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realizationContainer"):
                opp_val = getattr(old_value, "realizationContainer", None)
                if opp_val == self:
                    setattr(old_value, "realizationContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realizationContainer"):
                opp_val = getattr(value, "realizationContainer", None)
                setattr(value, "realizationContainer", self)

    @property
    def rapidml_ObjectRealization93(self):
        return self.__rapidml_ObjectRealization93

    @rapidml_ObjectRealization93.setter
    def rapidml_ObjectRealization93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ObjectRealization__rapidml_ObjectRealization93", None)
        self.__rapidml_ObjectRealization93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_PropertyRealization94"):
                    opp_val = getattr(item, "rapidml_PropertyRealization94", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_PropertyRealization94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_PropertyRealization94"):
                    opp_val = getattr(item, "rapidml_PropertyRealization94", None)
                    
                    setattr(item, "rapidml_PropertyRealization94", self)
                    

    def getDataType(self) -> str:
        # TODO: Implement getDataType method
        pass

    def getAllIncludedProperties(self) -> str:
        # TODO: Implement getAllIncludedProperties method
        pass

class rapidml_RESTElement(Extensible, Documentable):

    pass
class rapidml_MessageParameter(Parameter):

    def __init__(self, httpLocation: str, MessageParameter: "rapidml_TypedMessage" = None, parameters: "rapidml_TypedMessage" = None, rapidml_MessageParameter: "rapidml_SecurityScheme" = None):
        self.httpLocation = httpLocation
        self.MessageParameter = MessageParameter
        self.parameters = parameters
        self.rapidml_MessageParameter = rapidml_MessageParameter
        
    @property
    def httpLocation(self) -> str:
        return self.__httpLocation

    @httpLocation.setter
    def httpLocation(self, httpLocation: str):
        self.__httpLocation = httpLocation

    @property
    def rapidml_MessageParameter(self):
        return self.__rapidml_MessageParameter

    @rapidml_MessageParameter.setter
    def rapidml_MessageParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MessageParameter__rapidml_MessageParameter", None)
        self.__rapidml_MessageParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecurityScheme104"):
                opp_val = getattr(old_value, "rapidml_SecurityScheme104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecurityScheme104"):
                opp_val = getattr(value, "rapidml_SecurityScheme104", None)
                if opp_val is None:
                    setattr(value, "rapidml_SecurityScheme104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageParameter(self):
        return self.__MessageParameter

    @MessageParameter.setter
    def MessageParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MessageParameter__MessageParameter", None)
        self.__MessageParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingMessage"):
                opp_val = getattr(old_value, "containingMessage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingMessage"):
                opp_val = getattr(value, "containingMessage", None)
                if opp_val is None:
                    setattr(value, "containingMessage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MessageParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedMessage"):
                opp_val = getattr(old_value, "TypedMessage", None)
                if opp_val == self:
                    setattr(old_value, "TypedMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedMessage"):
                opp_val = getattr(value, "TypedMessage", None)
                setattr(value, "TypedMessage", self)

class rapidml_URI(HasStringValue):

    pass
class HasSecurityValue:

    pass
class WithExamples:

    pass
class RESTElement:

    pass
class rapidml_Method(HasSecurityValue, RESTElement, Extensible):

    def __init__(self, id: str, httpMethod: str, Method: "rapidml_ResourceDefinition" = None, containingMethod: "rapidml_TypedRequest" = None, containingMethod15: set["rapidml_TypedResponse"] = None, methods: "rapidml_ResourceDefinition" = None, Method23: "rapidml_TypedRequest" = None, Method25: "rapidml_TypedResponse" = None):
        self.id = id
        self.httpMethod = httpMethod
        self.Method = Method
        self.containingMethod = containingMethod
        self.containingMethod15 = containingMethod15 if containingMethod15 is not None else set()
        self.methods = methods
        self.Method23 = Method23
        self.Method25 = Method25
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def httpMethod(self) -> str:
        return self.__httpMethod

    @httpMethod.setter
    def httpMethod(self, httpMethod: str):
        self.__httpMethod = httpMethod

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceDefinition"):
                opp_val = getattr(old_value, "ResourceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ResourceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceDefinition"):
                opp_val = getattr(value, "ResourceDefinition", None)
                setattr(value, "ResourceDefinition", self)

    @property
    def Method25(self):
        return self.__Method25

    @Method25.setter
    def Method25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__Method25", None)
        self.__Method25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responses"):
                opp_val = getattr(old_value, "responses", None)
                if opp_val == self:
                    setattr(old_value, "responses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responses"):
                opp_val = getattr(value, "responses", None)
                setattr(value, "responses", self)

    @property
    def Method23(self):
        return self.__Method23

    @Method23.setter
    def Method23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__Method23", None)
        self.__Method23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request"):
                opp_val = getattr(old_value, "request", None)
                if opp_val == self:
                    setattr(old_value, "request", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request"):
                opp_val = getattr(value, "request", None)
                setattr(value, "request", self)

    @property
    def containingMethod(self):
        return self.__containingMethod

    @containingMethod.setter
    def containingMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__containingMethod", None)
        self.__containingMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedRequest"):
                opp_val = getattr(old_value, "TypedRequest", None)
                if opp_val == self:
                    setattr(old_value, "TypedRequest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedRequest"):
                opp_val = getattr(value, "TypedRequest", None)
                setattr(value, "TypedRequest", self)

    @property
    def containingMethod15(self):
        return self.__containingMethod15

    @containingMethod15.setter
    def containingMethod15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__containingMethod15", None)
        self.__containingMethod15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypedResponse"):
                    opp_val = getattr(item, "TypedResponse", None)
                    
                    if opp_val == self:
                        setattr(item, "TypedResponse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypedResponse"):
                    opp_val = getattr(item, "TypedResponse", None)
                    
                    setattr(item, "TypedResponse", self)
                    

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingResourceDefinition"):
                opp_val = getattr(old_value, "containingResourceDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingResourceDefinition"):
                opp_val = getattr(value, "containingResourceDefinition", None)
                if opp_val is None:
                    setattr(value, "containingResourceDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class rapidml_MediaType(RESTElement):

    def __init__(self, name: str, specURL: str, rapidml_MediaType: "rapidml_ResourceDefinition" = None, rapidml_MediaType4: "rapidml_ResourceDefinition" = None, rapidml_MediaType12: "rapidml_TypedMessage" = None, rapidml_MediaType21: "rapidml_MediaType" = None, rapidml_MediaType19: set["rapidml_MediaType"] = None, rapidml_MediaType56: "rapidml_ResourceAPI" = None, rapidml_MediaType59: "rapidml_ResourceAPI" = None, rapidml_MediaType127: "rapidml_MediaTypesLibrary" = None):
        self.name = name
        self.specURL = specURL
        self.rapidml_MediaType = rapidml_MediaType
        self.rapidml_MediaType4 = rapidml_MediaType4
        self.rapidml_MediaType12 = rapidml_MediaType12
        self.rapidml_MediaType21 = rapidml_MediaType21
        self.rapidml_MediaType19 = rapidml_MediaType19 if rapidml_MediaType19 is not None else set()
        self.rapidml_MediaType56 = rapidml_MediaType56
        self.rapidml_MediaType59 = rapidml_MediaType59
        self.rapidml_MediaType127 = rapidml_MediaType127
        
    @property
    def specURL(self) -> str:
        return self.__specURL

    @specURL.setter
    def specURL(self, specURL: str):
        self.__specURL = specURL

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_MediaType4(self):
        return self.__rapidml_MediaType4

    @rapidml_MediaType4.setter
    def rapidml_MediaType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType4", None)
        self.__rapidml_MediaType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceDefinition3"):
                opp_val = getattr(old_value, "rapidml_ResourceDefinition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceDefinition3"):
                opp_val = getattr(value, "rapidml_ResourceDefinition3", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceDefinition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType21(self):
        return self.__rapidml_MediaType21

    @rapidml_MediaType21.setter
    def rapidml_MediaType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType21", None)
        self.__rapidml_MediaType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_MediaType19"):
                opp_val = getattr(old_value, "rapidml_MediaType19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_MediaType19"):
                opp_val = getattr(value, "rapidml_MediaType19", None)
                if opp_val is None:
                    setattr(value, "rapidml_MediaType19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType12(self):
        return self.__rapidml_MediaType12

    @rapidml_MediaType12.setter
    def rapidml_MediaType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType12", None)
        self.__rapidml_MediaType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_TypedMessage11"):
                opp_val = getattr(old_value, "rapidml_TypedMessage11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_TypedMessage11"):
                opp_val = getattr(value, "rapidml_TypedMessage11", None)
                if opp_val is None:
                    setattr(value, "rapidml_TypedMessage11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType127(self):
        return self.__rapidml_MediaType127

    @rapidml_MediaType127.setter
    def rapidml_MediaType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType127", None)
        self.__rapidml_MediaType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_MediaTypesLibrary126"):
                opp_val = getattr(old_value, "rapidml_MediaTypesLibrary126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_MediaTypesLibrary126"):
                opp_val = getattr(value, "rapidml_MediaTypesLibrary126", None)
                if opp_val is None:
                    setattr(value, "rapidml_MediaTypesLibrary126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType56(self):
        return self.__rapidml_MediaType56

    @rapidml_MediaType56.setter
    def rapidml_MediaType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType56", None)
        self.__rapidml_MediaType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI55"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI55"):
                opp_val = getattr(value, "rapidml_ResourceAPI55", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType59(self):
        return self.__rapidml_MediaType59

    @rapidml_MediaType59.setter
    def rapidml_MediaType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType59", None)
        self.__rapidml_MediaType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI58"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI58"):
                opp_val = getattr(value, "rapidml_ResourceAPI58", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_MediaType19(self):
        return self.__rapidml_MediaType19

    @rapidml_MediaType19.setter
    def rapidml_MediaType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType19", None)
        self.__rapidml_MediaType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType21"):
                    opp_val = getattr(item, "rapidml_MediaType21", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType21"):
                    opp_val = getattr(item, "rapidml_MediaType21", None)
                    
                    setattr(item, "rapidml_MediaType21", self)
                    

    @property
    def rapidml_MediaType(self):
        return self.__rapidml_MediaType

    @rapidml_MediaType.setter
    def rapidml_MediaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_MediaType__rapidml_MediaType", None)
        self.__rapidml_MediaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceDefinition"):
                opp_val = getattr(old_value, "rapidml_ResourceDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceDefinition"):
                opp_val = getattr(value, "rapidml_ResourceDefinition", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hashCode(self) -> int:
        # TODO: Implement hashCode method
        pass

    def equals(self, other: str) -> bool:
        # TODO: Implement equals method
        pass

class rapidml_SecurityScheme(RESTElement, Documentable):

    def __init__(self, name: str, type: str, flow: str, rapidml_SecurityScheme: set["rapidml_SecurityScope"] = None, rapidml_SecurityScheme102: set["rapidml_SecuritySchemeParameter"] = None, rapidml_SecurityScheme104: set["rapidml_MessageParameter"] = None, rapidml_SecurityScheme106: set["rapidml_TypedResponse"] = None, rapidml_SecurityScheme109: "rapidml_AuthenticationMethod" = None, rapidml_SecurityScheme115: "rapidml_SecuritySchemeLibrary" = None):
        self.name = name
        self.type = type
        self.flow = flow
        self.rapidml_SecurityScheme = rapidml_SecurityScheme if rapidml_SecurityScheme is not None else set()
        self.rapidml_SecurityScheme102 = rapidml_SecurityScheme102 if rapidml_SecurityScheme102 is not None else set()
        self.rapidml_SecurityScheme104 = rapidml_SecurityScheme104 if rapidml_SecurityScheme104 is not None else set()
        self.rapidml_SecurityScheme106 = rapidml_SecurityScheme106 if rapidml_SecurityScheme106 is not None else set()
        self.rapidml_SecurityScheme109 = rapidml_SecurityScheme109
        self.rapidml_SecurityScheme115 = rapidml_SecurityScheme115
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def flow(self) -> str:
        return self.__flow

    @flow.setter
    def flow(self, flow: str):
        self.__flow = flow

    @property
    def rapidml_SecurityScheme102(self):
        return self.__rapidml_SecurityScheme102

    @rapidml_SecurityScheme102.setter
    def rapidml_SecurityScheme102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme102", None)
        self.__rapidml_SecurityScheme102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_SecuritySchemeParameter"):
                    opp_val = getattr(item, "rapidml_SecuritySchemeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_SecuritySchemeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_SecuritySchemeParameter"):
                    opp_val = getattr(item, "rapidml_SecuritySchemeParameter", None)
                    
                    setattr(item, "rapidml_SecuritySchemeParameter", self)
                    

    @property
    def rapidml_SecurityScheme(self):
        return self.__rapidml_SecurityScheme

    @rapidml_SecurityScheme.setter
    def rapidml_SecurityScheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme", None)
        self.__rapidml_SecurityScheme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_SecurityScope"):
                    opp_val = getattr(item, "rapidml_SecurityScope", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_SecurityScope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_SecurityScope"):
                    opp_val = getattr(item, "rapidml_SecurityScope", None)
                    
                    setattr(item, "rapidml_SecurityScope", self)
                    

    @property
    def rapidml_SecurityScheme115(self):
        return self.__rapidml_SecurityScheme115

    @rapidml_SecurityScheme115.setter
    def rapidml_SecurityScheme115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme115", None)
        self.__rapidml_SecurityScheme115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_SecuritySchemeLibrary114"):
                opp_val = getattr(old_value, "rapidml_SecuritySchemeLibrary114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_SecuritySchemeLibrary114"):
                opp_val = getattr(value, "rapidml_SecuritySchemeLibrary114", None)
                if opp_val is None:
                    setattr(value, "rapidml_SecuritySchemeLibrary114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_SecurityScheme109(self):
        return self.__rapidml_SecurityScheme109

    @rapidml_SecurityScheme109.setter
    def rapidml_SecurityScheme109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme109", None)
        self.__rapidml_SecurityScheme109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_AuthenticationMethod108"):
                opp_val = getattr(old_value, "rapidml_AuthenticationMethod108", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_AuthenticationMethod108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_AuthenticationMethod108"):
                opp_val = getattr(value, "rapidml_AuthenticationMethod108", None)
                setattr(value, "rapidml_AuthenticationMethod108", self)

    @property
    def rapidml_SecurityScheme104(self):
        return self.__rapidml_SecurityScheme104

    @rapidml_SecurityScheme104.setter
    def rapidml_SecurityScheme104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme104", None)
        self.__rapidml_SecurityScheme104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MessageParameter"):
                    opp_val = getattr(item, "rapidml_MessageParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MessageParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MessageParameter"):
                    opp_val = getattr(item, "rapidml_MessageParameter", None)
                    
                    setattr(item, "rapidml_MessageParameter", self)
                    

    @property
    def rapidml_SecurityScheme106(self):
        return self.__rapidml_SecurityScheme106

    @rapidml_SecurityScheme106.setter
    def rapidml_SecurityScheme106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_SecurityScheme__rapidml_SecurityScheme106", None)
        self.__rapidml_SecurityScheme106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_TypedResponse"):
                    opp_val = getattr(item, "rapidml_TypedResponse", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_TypedResponse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_TypedResponse"):
                    opp_val = getattr(item, "rapidml_TypedResponse", None)
                    
                    setattr(item, "rapidml_TypedResponse", self)
                    

class rapidml_ResourceAPI(HasSecurityValue, RESTElement, HasTitle):

    def __init__(self, name: str, version: str, baseURI: str, rapidml_ResourceAPI: "rapidml_ZenModel" = None, rapidml_ResourceAPI58: set["rapidml_MediaType"] = None, rapidml_ResourceAPI61: set["rapidml_LinkRelation"] = None, rapidml_ResourceAPI63: set["rapidml_ReferenceRealization"] = None, rapidml_ResourceAPI49: set["rapidml_ResourceDefinition"] = None, rapidml_ResourceAPI52: set["rapidml_DataModel"] = None, rapidml_ResourceAPI55: set["rapidml_MediaType"] = None, rapidml_ResourceAPI65: set["rapidml_RealizationModelLocation"] = None):
        self.name = name
        self.version = version
        self.baseURI = baseURI
        self.rapidml_ResourceAPI = rapidml_ResourceAPI
        self.rapidml_ResourceAPI58 = rapidml_ResourceAPI58 if rapidml_ResourceAPI58 is not None else set()
        self.rapidml_ResourceAPI61 = rapidml_ResourceAPI61 if rapidml_ResourceAPI61 is not None else set()
        self.rapidml_ResourceAPI63 = rapidml_ResourceAPI63 if rapidml_ResourceAPI63 is not None else set()
        self.rapidml_ResourceAPI49 = rapidml_ResourceAPI49 if rapidml_ResourceAPI49 is not None else set()
        self.rapidml_ResourceAPI52 = rapidml_ResourceAPI52 if rapidml_ResourceAPI52 is not None else set()
        self.rapidml_ResourceAPI55 = rapidml_ResourceAPI55 if rapidml_ResourceAPI55 is not None else set()
        self.rapidml_ResourceAPI65 = rapidml_ResourceAPI65 if rapidml_ResourceAPI65 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def baseURI(self) -> str:
        return self.__baseURI

    @baseURI.setter
    def baseURI(self, baseURI: str):
        self.__baseURI = baseURI

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def rapidml_ResourceAPI(self):
        return self.__rapidml_ResourceAPI

    @rapidml_ResourceAPI.setter
    def rapidml_ResourceAPI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI", None)
        self.__rapidml_ResourceAPI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ZenModel"):
                opp_val = getattr(old_value, "rapidml_ZenModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ZenModel"):
                opp_val = getattr(value, "rapidml_ZenModel", None)
                if opp_val is None:
                    setattr(value, "rapidml_ZenModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_ResourceAPI49(self):
        return self.__rapidml_ResourceAPI49

    @rapidml_ResourceAPI49.setter
    def rapidml_ResourceAPI49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI49", None)
        self.__rapidml_ResourceAPI49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_ResourceDefinition50"):
                    opp_val = getattr(item, "rapidml_ResourceDefinition50", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_ResourceDefinition50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_ResourceDefinition50"):
                    opp_val = getattr(item, "rapidml_ResourceDefinition50", None)
                    
                    setattr(item, "rapidml_ResourceDefinition50", self)
                    

    @property
    def rapidml_ResourceAPI61(self):
        return self.__rapidml_ResourceAPI61

    @rapidml_ResourceAPI61.setter
    def rapidml_ResourceAPI61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI61", None)
        self.__rapidml_ResourceAPI61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_LinkRelation"):
                    opp_val = getattr(item, "rapidml_LinkRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_LinkRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_LinkRelation"):
                    opp_val = getattr(item, "rapidml_LinkRelation", None)
                    
                    setattr(item, "rapidml_LinkRelation", self)
                    

    @property
    def rapidml_ResourceAPI63(self):
        return self.__rapidml_ResourceAPI63

    @rapidml_ResourceAPI63.setter
    def rapidml_ResourceAPI63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI63", None)
        self.__rapidml_ResourceAPI63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_ReferenceRealization"):
                    opp_val = getattr(item, "rapidml_ReferenceRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_ReferenceRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_ReferenceRealization"):
                    opp_val = getattr(item, "rapidml_ReferenceRealization", None)
                    
                    setattr(item, "rapidml_ReferenceRealization", self)
                    

    @property
    def rapidml_ResourceAPI52(self):
        return self.__rapidml_ResourceAPI52

    @rapidml_ResourceAPI52.setter
    def rapidml_ResourceAPI52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI52", None)
        self.__rapidml_ResourceAPI52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_DataModel53"):
                    opp_val = getattr(item, "rapidml_DataModel53", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_DataModel53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_DataModel53"):
                    opp_val = getattr(item, "rapidml_DataModel53", None)
                    
                    setattr(item, "rapidml_DataModel53", self)
                    

    @property
    def rapidml_ResourceAPI58(self):
        return self.__rapidml_ResourceAPI58

    @rapidml_ResourceAPI58.setter
    def rapidml_ResourceAPI58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI58", None)
        self.__rapidml_ResourceAPI58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType59"):
                    opp_val = getattr(item, "rapidml_MediaType59", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType59"):
                    opp_val = getattr(item, "rapidml_MediaType59", None)
                    
                    setattr(item, "rapidml_MediaType59", self)
                    

    @property
    def rapidml_ResourceAPI65(self):
        return self.__rapidml_ResourceAPI65

    @rapidml_ResourceAPI65.setter
    def rapidml_ResourceAPI65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI65", None)
        self.__rapidml_ResourceAPI65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_RealizationModelLocation"):
                    opp_val = getattr(item, "rapidml_RealizationModelLocation", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_RealizationModelLocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_RealizationModelLocation"):
                    opp_val = getattr(item, "rapidml_RealizationModelLocation", None)
                    
                    setattr(item, "rapidml_RealizationModelLocation", self)
                    

    @property
    def rapidml_ResourceAPI55(self):
        return self.__rapidml_ResourceAPI55

    @rapidml_ResourceAPI55.setter
    def rapidml_ResourceAPI55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceAPI__rapidml_ResourceAPI55", None)
        self.__rapidml_ResourceAPI55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType56"):
                    opp_val = getattr(item, "rapidml_MediaType56", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType56"):
                    opp_val = getattr(item, "rapidml_MediaType56", None)
                    
                    setattr(item, "rapidml_MediaType56", self)
                    

class rapidml_Parameter(RESTElement, Extensible):

    def __init__(self, name: str, required: bool, default: str, fixed: str, containingParameter: "rapidml_SourceReference" = None, Parameter: "rapidml_SourceReference" = None):
        self.name = name
        self.required = required
        self.default = default
        self.fixed = fixed
        self.containingParameter = containingParameter
        self.Parameter = Parameter
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fixed(self) -> str:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: str):
        self.__fixed = fixed

    @property
    def containingParameter(self):
        return self.__containingParameter

    @containingParameter.setter
    def containingParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Parameter__containingParameter", None)
        self.__containingParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceReference"):
                opp_val = getattr(old_value, "SourceReference", None)
                if opp_val == self:
                    setattr(old_value, "SourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceReference"):
                opp_val = getattr(value, "SourceReference", None)
                setattr(value, "SourceReference", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceReference"):
                opp_val = getattr(old_value, "sourceReference", None)
                if opp_val == self:
                    setattr(old_value, "sourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceReference"):
                opp_val = getattr(value, "sourceReference", None)
                setattr(value, "sourceReference", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getPrimitiveType(self) -> str:
        # TODO: Implement getPrimitiveType method
        pass

    def getConstraints(self) -> str:
        # TODO: Implement getConstraints method
        pass

class rapidml_ResourceDefinition(HasSecurityValue, WithExamples, RESTElement):

    def __init__(self, name: str, containingResourceDefinition: set["rapidml_Method"] = None, rapidml_ResourceDefinition: set["rapidml_MediaType"] = None, rapidml_ResourceDefinition3: set["rapidml_MediaType"] = None, rapidml_ResourceDefinition6: "rapidml_URI" = None, rapidml_ResourceDefinition9: "rapidml_TypedMessage" = None, ResourceDefinition: "rapidml_Method" = None, rapidml_ResourceDefinition50: "rapidml_ResourceAPI" = None, rapidml_ResourceDefinition76: "rapidml_ReferenceRealization" = None):
        self.name = name
        self.containingResourceDefinition = containingResourceDefinition if containingResourceDefinition is not None else set()
        self.rapidml_ResourceDefinition = rapidml_ResourceDefinition if rapidml_ResourceDefinition is not None else set()
        self.rapidml_ResourceDefinition3 = rapidml_ResourceDefinition3 if rapidml_ResourceDefinition3 is not None else set()
        self.rapidml_ResourceDefinition6 = rapidml_ResourceDefinition6
        self.rapidml_ResourceDefinition9 = rapidml_ResourceDefinition9
        self.ResourceDefinition = ResourceDefinition
        self.rapidml_ResourceDefinition50 = rapidml_ResourceDefinition50
        self.rapidml_ResourceDefinition76 = rapidml_ResourceDefinition76
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rapidml_ResourceDefinition(self):
        return self.__rapidml_ResourceDefinition

    @rapidml_ResourceDefinition.setter
    def rapidml_ResourceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition", None)
        self.__rapidml_ResourceDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType"):
                    opp_val = getattr(item, "rapidml_MediaType", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType"):
                    opp_val = getattr(item, "rapidml_MediaType", None)
                    
                    setattr(item, "rapidml_MediaType", self)
                    

    @property
    def ResourceDefinition(self):
        return self.__ResourceDefinition

    @ResourceDefinition.setter
    def ResourceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__ResourceDefinition", None)
        self.__ResourceDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def rapidml_ResourceDefinition50(self):
        return self.__rapidml_ResourceDefinition50

    @rapidml_ResourceDefinition50.setter
    def rapidml_ResourceDefinition50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition50", None)
        self.__rapidml_ResourceDefinition50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI49"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI49"):
                opp_val = getattr(value, "rapidml_ResourceAPI49", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_ResourceDefinition3(self):
        return self.__rapidml_ResourceDefinition3

    @rapidml_ResourceDefinition3.setter
    def rapidml_ResourceDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition3", None)
        self.__rapidml_ResourceDefinition3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType4"):
                    opp_val = getattr(item, "rapidml_MediaType4", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType4"):
                    opp_val = getattr(item, "rapidml_MediaType4", None)
                    
                    setattr(item, "rapidml_MediaType4", self)
                    

    @property
    def rapidml_ResourceDefinition9(self):
        return self.__rapidml_ResourceDefinition9

    @rapidml_ResourceDefinition9.setter
    def rapidml_ResourceDefinition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition9", None)
        self.__rapidml_ResourceDefinition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_TypedMessage"):
                opp_val = getattr(old_value, "rapidml_TypedMessage", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_TypedMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_TypedMessage"):
                opp_val = getattr(value, "rapidml_TypedMessage", None)
                setattr(value, "rapidml_TypedMessage", self)

    @property
    def rapidml_ResourceDefinition6(self):
        return self.__rapidml_ResourceDefinition6

    @rapidml_ResourceDefinition6.setter
    def rapidml_ResourceDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition6", None)
        self.__rapidml_ResourceDefinition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_URI"):
                opp_val = getattr(old_value, "rapidml_URI", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_URI", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_URI"):
                opp_val = getattr(value, "rapidml_URI", None)
                setattr(value, "rapidml_URI", self)

    @property
    def rapidml_ResourceDefinition76(self):
        return self.__rapidml_ResourceDefinition76

    @rapidml_ResourceDefinition76.setter
    def rapidml_ResourceDefinition76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__rapidml_ResourceDefinition76", None)
        self.__rapidml_ResourceDefinition76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceRealization75"):
                opp_val = getattr(old_value, "rapidml_ReferenceRealization75", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceRealization75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceRealization75"):
                opp_val = getattr(value, "rapidml_ReferenceRealization75", None)
                setattr(value, "rapidml_ReferenceRealization75", self)

    @property
    def containingResourceDefinition(self):
        return self.__containingResourceDefinition

    @containingResourceDefinition.setter
    def containingResourceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ResourceDefinition__containingResourceDefinition", None)
        self.__containingResourceDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

class RealizationContainer:

    pass
class rapidml_ReferenceRealization(RealizationContainer):

    def __init__(self, realizationType: str, multiValued: bool, rapidml_ReferenceRealization: "rapidml_ResourceAPI" = None, rapidml_ReferenceRealization70: "rapidml_ReferenceTreatment" = None, rapidml_ReferenceRealization73: "rapidml_ReferenceTreatment" = None, rapidml_ReferenceRealization75: "rapidml_ResourceDefinition" = None):
        self.realizationType = realizationType
        self.multiValued = multiValued
        self.rapidml_ReferenceRealization = rapidml_ReferenceRealization
        self.rapidml_ReferenceRealization70 = rapidml_ReferenceRealization70
        self.rapidml_ReferenceRealization73 = rapidml_ReferenceRealization73
        self.rapidml_ReferenceRealization75 = rapidml_ReferenceRealization75
        
    @property
    def realizationType(self) -> str:
        return self.__realizationType

    @realizationType.setter
    def realizationType(self, realizationType: str):
        self.__realizationType = realizationType

    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def rapidml_ReferenceRealization75(self):
        return self.__rapidml_ReferenceRealization75

    @rapidml_ReferenceRealization75.setter
    def rapidml_ReferenceRealization75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceRealization__rapidml_ReferenceRealization75", None)
        self.__rapidml_ReferenceRealization75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceDefinition76"):
                opp_val = getattr(old_value, "rapidml_ResourceDefinition76", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ResourceDefinition76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceDefinition76"):
                opp_val = getattr(value, "rapidml_ResourceDefinition76", None)
                setattr(value, "rapidml_ResourceDefinition76", self)

    @property
    def rapidml_ReferenceRealization70(self):
        return self.__rapidml_ReferenceRealization70

    @rapidml_ReferenceRealization70.setter
    def rapidml_ReferenceRealization70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceRealization__rapidml_ReferenceRealization70", None)
        self.__rapidml_ReferenceRealization70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceTreatment69"):
                opp_val = getattr(old_value, "rapidml_ReferenceTreatment69", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceTreatment69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceTreatment69"):
                opp_val = getattr(value, "rapidml_ReferenceTreatment69", None)
                setattr(value, "rapidml_ReferenceTreatment69", self)

    @property
    def rapidml_ReferenceRealization(self):
        return self.__rapidml_ReferenceRealization

    @rapidml_ReferenceRealization.setter
    def rapidml_ReferenceRealization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceRealization__rapidml_ReferenceRealization", None)
        self.__rapidml_ReferenceRealization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceAPI63"):
                opp_val = getattr(old_value, "rapidml_ResourceAPI63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceAPI63"):
                opp_val = getattr(value, "rapidml_ResourceAPI63", None)
                if opp_val is None:
                    setattr(value, "rapidml_ResourceAPI63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rapidml_ReferenceRealization73(self):
        return self.__rapidml_ReferenceRealization73

    @rapidml_ReferenceRealization73.setter
    def rapidml_ReferenceRealization73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ReferenceRealization__rapidml_ReferenceRealization73", None)
        self.__rapidml_ReferenceRealization73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ReferenceTreatment72"):
                opp_val = getattr(old_value, "rapidml_ReferenceTreatment72", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ReferenceTreatment72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ReferenceTreatment72"):
                opp_val = getattr(value, "rapidml_ReferenceTreatment72", None)
                setattr(value, "rapidml_ReferenceTreatment72", self)

    def getLinkDescriptor(self) -> str:
        # TODO: Implement getLinkDescriptor method
        pass

class rapidml_ServiceDataResource(RealizationContainer, ResourceDefinition):

    def __init__(self, default: bool, rapidml_ServiceDataResource: set["rapidml_NamedLinkDescriptor"] = None):
        self.default = default
        self.rapidml_ServiceDataResource = rapidml_ServiceDataResource if rapidml_ServiceDataResource is not None else set()
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def rapidml_ServiceDataResource(self):
        return self.__rapidml_ServiceDataResource

    @rapidml_ServiceDataResource.setter
    def rapidml_ServiceDataResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_ServiceDataResource__rapidml_ServiceDataResource", None)
        self.__rapidml_ServiceDataResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_NamedLinkDescriptor"):
                    opp_val = getattr(item, "rapidml_NamedLinkDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_NamedLinkDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_NamedLinkDescriptor"):
                    opp_val = getattr(item, "rapidml_NamedLinkDescriptor", None)
                    
                    setattr(item, "rapidml_NamedLinkDescriptor", self)
                    

    def isIncluded(self, feature: str) -> bool:
        # TODO: Implement isIncluded method
        pass

    def getReferenceLinks(self) -> str:
        # TODO: Implement getReferenceLinks method
        pass

    def getIncludedProperties(self) -> str:
        # TODO: Implement getIncludedProperties method
        pass

    def getAllReferenceTreatments(self) -> str:
        # TODO: Implement getAllReferenceTreatments method
        pass

    def getDefaultLinkDescriptor(self) -> str:
        # TODO: Implement getDefaultLinkDescriptor method
        pass

class rapidml_TypedMessage(RealizationContainer, RESTElement, WithExamples):

    def __init__(self, useParentTypeReference: bool, containingMessage: set["rapidml_MessageParameter"] = None, rapidml_TypedMessage: "rapidml_ResourceDefinition" = None, rapidml_TypedMessage11: set["rapidml_MediaType"] = None, TypedMessage: "rapidml_MessageParameter" = None):
        self.useParentTypeReference = useParentTypeReference
        self.containingMessage = containingMessage if containingMessage is not None else set()
        self.rapidml_TypedMessage = rapidml_TypedMessage
        self.rapidml_TypedMessage11 = rapidml_TypedMessage11 if rapidml_TypedMessage11 is not None else set()
        self.TypedMessage = TypedMessage
        
    @property
    def useParentTypeReference(self) -> bool:
        return self.__useParentTypeReference

    @useParentTypeReference.setter
    def useParentTypeReference(self, useParentTypeReference: bool):
        self.__useParentTypeReference = useParentTypeReference

    @property
    def rapidml_TypedMessage11(self):
        return self.__rapidml_TypedMessage11

    @rapidml_TypedMessage11.setter
    def rapidml_TypedMessage11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedMessage__rapidml_TypedMessage11", None)
        self.__rapidml_TypedMessage11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rapidml_MediaType12"):
                    opp_val = getattr(item, "rapidml_MediaType12", None)
                    
                    if opp_val == self:
                        setattr(item, "rapidml_MediaType12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rapidml_MediaType12"):
                    opp_val = getattr(item, "rapidml_MediaType12", None)
                    
                    setattr(item, "rapidml_MediaType12", self)
                    

    @property
    def TypedMessage(self):
        return self.__TypedMessage

    @TypedMessage.setter
    def TypedMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedMessage__TypedMessage", None)
        self.__TypedMessage = value
        
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
    def containingMessage(self):
        return self.__containingMessage

    @containingMessage.setter
    def containingMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedMessage__containingMessage", None)
        self.__containingMessage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageParameter"):
                    opp_val = getattr(item, "MessageParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageParameter"):
                    opp_val = getattr(item, "MessageParameter", None)
                    
                    setattr(item, "MessageParameter", self)
                    

    @property
    def rapidml_TypedMessage(self):
        return self.__rapidml_TypedMessage

    @rapidml_TypedMessage.setter
    def rapidml_TypedMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rapidml_TypedMessage__rapidml_TypedMessage", None)
        self.__rapidml_TypedMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rapidml_ResourceDefinition9"):
                opp_val = getattr(old_value, "rapidml_ResourceDefinition9", None)
                if opp_val == self:
                    setattr(old_value, "rapidml_ResourceDefinition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rapidml_ResourceDefinition9"):
                opp_val = getattr(value, "rapidml_ResourceDefinition9", None)
                setattr(value, "rapidml_ResourceDefinition9", self)

    def isIncluded(self, feature: str) -> bool:
        # TODO: Implement isIncluded method
        pass

    def getReferenceLinks(self) -> str:
        # TODO: Implement getReferenceLinks method
        pass

    def getIncludedProperties(self) -> str:
        # TODO: Implement getIncludedProperties method
        pass

    def getActualType(self) -> str:
        # TODO: Implement getActualType method
        pass

    def getAllExamples(self) -> str:
        # TODO: Implement getAllExamples method
        pass
