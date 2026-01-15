from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Connectivity(Enum):
    DIRECTIONAL = "DIRECTIONAL"
    BIDIRECTIONAL = "BIDIRECTIONAL"
    NON_DIRECTIONAL = "NON_DIRECTIONAL"
class FileFormat(Enum):
    ZIP = "ZIP"
    HDF5 = "HDF5"
class BooleanOperator(Enum):
    AND = "AND"
    NAND = "NAND"
    OR = "OR"
class ImageFormat(Enum):
    PNG = "PNG"
    JPEG = "JPEG"
    IIP = "IIP"
    DCM = "DCM"
    NIFTI = "NIFTI"
    TIFF = "TIFF"
    DZI = "DZI"
    GOOGLE_MAP = "GOOGLE_MAP"


############################################
# Definition of Classes
############################################

class model_datasources_QueryMatchingCriteria:

    pass
class model_datasources_AQueryResult(ABC):

    pass
class model_datasources_RunnableQuery:

    def __init__(self, targetVariablePath: str, queryPath: str, booleanOperator: str):
        self.targetVariablePath = targetVariablePath
        self.queryPath = queryPath
        self.booleanOperator = booleanOperator
        
    @property
    def booleanOperator(self) -> str:
        return self.__booleanOperator

    @booleanOperator.setter
    def booleanOperator(self, booleanOperator: str):
        self.__booleanOperator = booleanOperator

    @property
    def targetVariablePath(self) -> str:
        return self.__targetVariablePath

    @targetVariablePath.setter
    def targetVariablePath(self, targetVariablePath: str):
        self.__targetVariablePath = targetVariablePath

    @property
    def queryPath(self) -> str:
        return self.__queryPath

    @queryPath.setter
    def queryPath(self, queryPath: str):
        self.__queryPath = queryPath

class AQueryResult:

    pass
class model_datasources_QueryResult(AQueryResult):

    def __init__(self, values: str, AQueryResult: "model_datasources_QueryResults"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_datasources_SerializableQueryResult(AQueryResult):

    def __init__(self, values: str, AQueryResult: "model_datasources_QueryResults"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_datasources_QueryResults:

    def __init__(self, id: str, header: str, model_datasources_QueryResults: set["AQueryResult"] = None):
        self.id = id
        self.header = header
        self.model_datasources_QueryResults = model_datasources_QueryResults if model_datasources_QueryResults is not None else set()
        
    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def model_datasources_QueryResults(self):
        return self.__model_datasources_QueryResults

    @model_datasources_QueryResults.setter
    def model_datasources_QueryResults(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_QueryResults__model_datasources_QueryResults", None)
        self.__model_datasources_QueryResults = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AQueryResult"):
                    opp_val = getattr(item, "AQueryResult", None)
                    
                    if opp_val == self:
                        setattr(item, "AQueryResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AQueryResult"):
                    opp_val = getattr(item, "AQueryResult", None)
                    
                    setattr(item, "AQueryResult", self)
                    

    def getValue(self, field: str, row: str) -> str:
        # TODO: Implement getValue method
        pass

class DataSourceLibraryConfiguration:

    pass
class datasources_model_StringToStringMap:

    pass
class QueryMatchingCriteria:

    pass
class model_datasources_DataSourceLibraryConfiguration:

    def __init__(self, modelInterpreterId: str, format: str, model_datasources_DataSourceLibraryConfiguration: "datasources_model_GeppettoLibrary" = None):
        self.modelInterpreterId = modelInterpreterId
        self.format = format
        self.model_datasources_DataSourceLibraryConfiguration = model_datasources_DataSourceLibraryConfiguration
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def modelInterpreterId(self) -> str:
        return self.__modelInterpreterId

    @modelInterpreterId.setter
    def modelInterpreterId(self, modelInterpreterId: str):
        self.__modelInterpreterId = modelInterpreterId

    @property
    def model_datasources_DataSourceLibraryConfiguration(self):
        return self.__model_datasources_DataSourceLibraryConfiguration

    @model_datasources_DataSourceLibraryConfiguration.setter
    def model_datasources_DataSourceLibraryConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSourceLibraryConfiguration__model_datasources_DataSourceLibraryConfiguration", None)
        self.__model_datasources_DataSourceLibraryConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasources_model_GeppettoLibrary155"):
                opp_val = getattr(old_value, "datasources_model_GeppettoLibrary155", None)
                if opp_val == self:
                    setattr(old_value, "datasources_model_GeppettoLibrary155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasources_model_GeppettoLibrary155"):
                opp_val = getattr(value, "datasources_model_GeppettoLibrary155", None)
                setattr(value, "datasources_model_GeppettoLibrary155", self)

class datasources_model_GeppettoLibrary:

    pass
class model_variables_TypeToValueMap:

    pass
class TypeToValueMap:

    pass
class model_values_SkeletonTransformation:

    def __init__(self, skeletonTransformation: str):
        self.skeletonTransformation = skeletonTransformation
        
    @property
    def skeletonTransformation(self) -> str:
        return self.__skeletonTransformation

    @skeletonTransformation.setter
    def skeletonTransformation(self, skeletonTransformation: str):
        self.__skeletonTransformation = skeletonTransformation

class SkeletonTransformation:

    pass
class ArrayElement:

    pass
class FunctionPlot:

    pass
class VisualGroupElement:

    pass
class PointerElement:

    pass
class MetadataValue:

    pass
class model_values_HTML(MetadataValue):

    def __init__(self, html: str):
        self.html = html
        
    @property
    def html(self) -> str:
        return self.__html

    @html.setter
    def html(self, html: str):
        self.__html = html

class model_values_Metadata(MetadataValue):

    pass
class model_values_URL(MetadataValue):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class model_values_JSON(MetadataValue):

    def __init__(self, json: str):
        self.json = json
        
    @property
    def json(self) -> str:
        return self.__json

    @json.setter
    def json(self, json: str):
        self.__json = json

class model_values_Text(MetadataValue):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class model_values_FunctionPlot:

    def __init__(self, title: str, xAxisLabel: str, yAxisLabel: str, initialValue: str, finalValue: str, stepValue: str):
        self.title = title
        self.xAxisLabel = xAxisLabel
        self.yAxisLabel = yAxisLabel
        self.initialValue = initialValue
        self.finalValue = finalValue
        self.stepValue = stepValue
        
    @property
    def xAxisLabel(self) -> str:
        return self.__xAxisLabel

    @xAxisLabel.setter
    def xAxisLabel(self, xAxisLabel: str):
        self.__xAxisLabel = xAxisLabel

    @property
    def stepValue(self) -> str:
        return self.__stepValue

    @stepValue.setter
    def stepValue(self, stepValue: str):
        self.__stepValue = stepValue

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def yAxisLabel(self) -> str:
        return self.__yAxisLabel

    @yAxisLabel.setter
    def yAxisLabel(self, yAxisLabel: str):
        self.__yAxisLabel = yAxisLabel

    @property
    def finalValue(self) -> str:
        return self.__finalValue

    @finalValue.setter
    def finalValue(self, finalValue: str):
        self.__finalValue = finalValue

class Function:

    pass
class PhysicalQuantity:

    pass
class model_values_PointerElement:

    def __init__(self, index: str, model_values_PointerElement: "Variable" = None, model_values_PointerElement88: "Type" = None):
        self.index = index
        self.model_values_PointerElement = model_values_PointerElement
        self.model_values_PointerElement88 = model_values_PointerElement88
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def model_values_PointerElement(self):
        return self.__model_values_PointerElement

    @model_values_PointerElement.setter
    def model_values_PointerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_PointerElement__model_values_PointerElement", None)
        self.__model_values_PointerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable86"):
                opp_val = getattr(old_value, "Variable86", None)
                if opp_val == self:
                    setattr(old_value, "Variable86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable86"):
                opp_val = getattr(value, "Variable86", None)
                setattr(value, "Variable86", self)

    @property
    def model_values_PointerElement88(self):
        return self.__model_values_PointerElement88

    @model_values_PointerElement88.setter
    def model_values_PointerElement88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_PointerElement__model_values_PointerElement88", None)
        self.__model_values_PointerElement88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type89"):
                opp_val = getattr(old_value, "Type89", None)
                if opp_val == self:
                    setattr(old_value, "Type89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type89"):
                opp_val = getattr(value, "Type89", None)
                setattr(value, "Type89", self)

class AArrayValue:

    pass
class model_values_GenericArray(AArrayValue):

    pass
class model_values_StringArray(AArrayValue):

    def __init__(self, elements: str, AArrayValue: "model_types_SimpleArrayType"):
        self.elements = elements
        
    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

class model_values_IntArray(AArrayValue):

    def __init__(self, elements: str, AArrayValue: "model_types_SimpleArrayType"):
        self.elements = elements
        
    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

class model_values_DoubleArray(AArrayValue):

    def __init__(self, elements: str, AArrayValue: "model_types_SimpleArrayType"):
        self.elements = elements
        
    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

class Image:

    pass
class Unit:

    pass
class model_values_StringToValueMap:

    def __init__(self, key: str, model_values_StringToValueMap: "Value" = None):
        self.key = key
        self.model_values_StringToValueMap = model_values_StringToValueMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_values_StringToValueMap(self):
        return self.__model_values_StringToValueMap

    @model_values_StringToValueMap.setter
    def model_values_StringToValueMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_StringToValueMap__model_values_StringToValueMap", None)
        self.__model_values_StringToValueMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Value75"):
                opp_val = getattr(old_value, "Value75", None)
                if opp_val == self:
                    setattr(old_value, "Value75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Value75"):
                opp_val = getattr(value, "Value75", None)
                setattr(value, "Value75", self)

class StringToValueMap:

    pass
class HTML:

    pass
class Expression:

    pass
class Argument:

    pass
class Dynamics:

    pass
class VisualGroup:

    pass
class ArrayValue:

    pass
class Point:

    pass
class URL:

    pass
class Text:

    pass
class JSON:

    pass
class types_model_DomainModel:

    pass
class VisualType:

    pass
class model_types_CompositeVisualType(VisualType):

    pass
class Quantity:

    pass
class model_values_PhysicalQuantity(Quantity):

    pass
class Composite:

    pass
class VisualValue:

    pass
class model_values_OBJ(VisualValue):

    def __init__(self, obj: str, VisualValue: "model_types_VisualType"):
        self.obj = obj
        
    @property
    def obj(self) -> str:
        return self.__obj

    @obj.setter
    def obj(self, obj: str):
        self.__obj = obj

class model_values_Cylinder(VisualValue):

    def __init__(self, bottomRadius: str, topRadius: str, height: str, model_values_Cylinder: "Point" = None, VisualValue: "model_types_VisualType"):
        self.bottomRadius = bottomRadius
        self.topRadius = topRadius
        self.height = height
        self.model_values_Cylinder = model_values_Cylinder
        
    @property
    def bottomRadius(self) -> str:
        return self.__bottomRadius

    @bottomRadius.setter
    def bottomRadius(self, bottomRadius: str):
        self.__bottomRadius = bottomRadius

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def topRadius(self) -> str:
        return self.__topRadius

    @topRadius.setter
    def topRadius(self, topRadius: str):
        self.__topRadius = topRadius

    @property
    def model_values_Cylinder(self):
        return self.__model_values_Cylinder

    @model_values_Cylinder.setter
    def model_values_Cylinder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_Cylinder__model_values_Cylinder", None)
        self.__model_values_Cylinder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Point105"):
                opp_val = getattr(old_value, "Point105", None)
                if opp_val == self:
                    setattr(old_value, "Point105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Point105"):
                opp_val = getattr(value, "Point105", None)
                setattr(value, "Point105", self)

class model_values_Sphere(VisualValue):

    def __init__(self, radius: str, VisualValue: "model_types_VisualType"):
        self.radius = radius
        
    @property
    def radius(self) -> str:
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius

class model_values_Collada(VisualValue):

    def __init__(self, collada: str, VisualValue: "model_types_VisualType"):
        self.collada = collada
        
    @property
    def collada(self) -> str:
        return self.__collada

    @collada.setter
    def collada(self, collada: str):
        self.__collada = collada

class model_values_SkeletonAnimation(VisualValue):

    pass
class model_VariableValue:

    pass
class model_ExperimentState:

    def __init__(self, experimentId: str, projectId: str, model_ExperimentState: set["model_VariableValue"] = None, model_ExperimentState20: set["model_VariableValue"] = None):
        self.experimentId = experimentId
        self.projectId = projectId
        self.model_ExperimentState = model_ExperimentState if model_ExperimentState is not None else set()
        self.model_ExperimentState20 = model_ExperimentState20 if model_ExperimentState20 is not None else set()
        
    @property
    def experimentId(self) -> str:
        return self.__experimentId

    @experimentId.setter
    def experimentId(self, experimentId: str):
        self.__experimentId = experimentId

    @property
    def projectId(self) -> str:
        return self.__projectId

    @projectId.setter
    def projectId(self, projectId: str):
        self.__projectId = projectId

    @property
    def model_ExperimentState20(self):
        return self.__model_ExperimentState20

    @model_ExperimentState20.setter
    def model_ExperimentState20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExperimentState__model_ExperimentState20", None)
        self.__model_ExperimentState20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_VariableValue21"):
                    opp_val = getattr(item, "model_VariableValue21", None)
                    
                    if opp_val == self:
                        setattr(item, "model_VariableValue21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_VariableValue21"):
                    opp_val = getattr(item, "model_VariableValue21", None)
                    
                    setattr(item, "model_VariableValue21", self)
                    

    @property
    def model_ExperimentState(self):
        return self.__model_ExperimentState

    @model_ExperimentState.setter
    def model_ExperimentState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExperimentState__model_ExperimentState", None)
        self.__model_ExperimentState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_VariableValue"):
                    opp_val = getattr(item, "model_VariableValue", None)
                    
                    if opp_val == self:
                        setattr(item, "model_VariableValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_VariableValue"):
                    opp_val = getattr(item, "model_VariableValue", None)
                    
                    setattr(item, "model_VariableValue", self)
                    

class model_LibraryManager:

    pass
class Type:

    pass
class model_types_StateVariableType(Type):

    pass
class model_types_JSONType(Type):

    pass
class model_types_CompositeType(Type):

    pass
class model_types_ExpressionType(Type):

    pass
class model_types_PointerType(Type):

    pass
class model_types_ArrayType(Type):

    def __init__(self, size: str, model_types_ArrayType: "Type" = None, model_types_ArrayType61: "ArrayValue" = None, Type159: "model_datasources_Query", Type167: "model_datasources_QueryMatchingCriteria", Type: "model_GeppettoLibrary", Type129: "model_variables_Variable", Type31: "model_types_Type", types: "model_variables_Variable", Type59: "model_types_ArrayType", Type138: "model_variables_TypeToValueMap", Type15: "model_GeppettoLibrary", Type89: "model_values_PointerElement"):
        self.size = size
        self.model_types_ArrayType = model_types_ArrayType
        self.model_types_ArrayType61 = model_types_ArrayType61
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def model_types_ArrayType61(self):
        return self.__model_types_ArrayType61

    @model_types_ArrayType61.setter
    def model_types_ArrayType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_ArrayType__model_types_ArrayType61", None)
        self.__model_types_ArrayType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayValue"):
                opp_val = getattr(old_value, "ArrayValue", None)
                if opp_val == self:
                    setattr(old_value, "ArrayValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayValue"):
                opp_val = getattr(value, "ArrayValue", None)
                setattr(value, "ArrayValue", self)

    @property
    def model_types_ArrayType(self):
        return self.__model_types_ArrayType

    @model_types_ArrayType.setter
    def model_types_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_ArrayType__model_types_ArrayType", None)
        self.__model_types_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type59"):
                opp_val = getattr(old_value, "Type59", None)
                if opp_val == self:
                    setattr(old_value, "Type59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type59"):
                opp_val = getattr(value, "Type59", None)
                setattr(value, "Type59", self)

class model_types_PointType(Type):

    pass
class model_types_ParameterType(Type):

    pass
class model_types_SimpleType(Type):

    pass
class model_types_ArgumentType(Type):

    pass
class model_types_ConnectionType(Type):

    pass
class model_types_TextType(Type):

    pass
class model_types_QuantityType(Type):

    pass
class model_types_SimpleArrayType(Type):

    pass
class model_types_ImportType(Type):

    def __init__(self, url: str, referenceURL: str, modelInterpreterId: str, autoresolve: str, Type159: "model_datasources_Query", Type167: "model_datasources_QueryMatchingCriteria", Type: "model_GeppettoLibrary", Type129: "model_variables_Variable", Type31: "model_types_Type", types: "model_variables_Variable", Type59: "model_types_ArrayType", Type138: "model_variables_TypeToValueMap", Type15: "model_GeppettoLibrary", Type89: "model_values_PointerElement"):
        self.url = url
        self.referenceURL = referenceURL
        self.modelInterpreterId = modelInterpreterId
        self.autoresolve = autoresolve
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def referenceURL(self) -> str:
        return self.__referenceURL

    @referenceURL.setter
    def referenceURL(self, referenceURL: str):
        self.__referenceURL = referenceURL

    @property
    def autoresolve(self) -> str:
        return self.__autoresolve

    @autoresolve.setter
    def autoresolve(self, autoresolve: str):
        self.__autoresolve = autoresolve

    @property
    def modelInterpreterId(self) -> str:
        return self.__modelInterpreterId

    @modelInterpreterId.setter
    def modelInterpreterId(self, modelInterpreterId: str):
        self.__modelInterpreterId = modelInterpreterId

class model_types_ImageType(Type):

    pass
class model_types_DynamicsType(Type):

    pass
class model_types_URLType(Type):

    pass
class model_types_VisualType(Type):

    pass
class model_types_HTMLType(Type):

    pass
class model_types_MetadataType(Type):

    pass
class model_ISynchable(ABC):

    def __init__(self, synched: str):
        self.synched = synched
        
    @property
    def synched(self) -> str:
        return self.__synched

    @synched.setter
    def synched(self, synched: str):
        self.__synched = synched

class model_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DomainModel:

    pass
class model_ExternalDomainModel(DomainModel):

    def __init__(self, fileFormat: str):
        self.fileFormat = fileFormat
        
    @property
    def fileFormat(self) -> str:
        return self.__fileFormat

    @fileFormat.setter
    def fileFormat(self, fileFormat: str):
        self.__fileFormat = fileFormat

class model_ModelFormat:

    def __init__(self, modelFormat: str, model_ModelFormat: "model_DomainModel" = None):
        self.modelFormat = modelFormat
        self.model_ModelFormat = model_ModelFormat
        
    @property
    def modelFormat(self) -> str:
        return self.__modelFormat

    @modelFormat.setter
    def modelFormat(self, modelFormat: str):
        self.__modelFormat = modelFormat

    @property
    def model_ModelFormat(self):
        return self.__model_ModelFormat

    @model_ModelFormat.setter
    def model_ModelFormat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelFormat__model_ModelFormat", None)
        self.__model_ModelFormat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DomainModel"):
                opp_val = getattr(old_value, "model_DomainModel", None)
                if opp_val == self:
                    setattr(old_value, "model_DomainModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DomainModel"):
                opp_val = getattr(value, "model_DomainModel", None)
                setattr(value, "model_DomainModel", self)

class model_DomainModel:

    def __init__(self, domainModel: str, model_DomainModel: "model_ModelFormat" = None):
        self.domainModel = domainModel
        self.model_DomainModel = model_DomainModel
        
    @property
    def domainModel(self) -> str:
        return self.__domainModel

    @domainModel.setter
    def domainModel(self, domainModel: str):
        self.__domainModel = domainModel

    @property
    def model_DomainModel(self):
        return self.__model_DomainModel

    @model_DomainModel.setter
    def model_DomainModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DomainModel__model_DomainModel", None)
        self.__model_DomainModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelFormat"):
                opp_val = getattr(old_value, "model_ModelFormat", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelFormat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelFormat"):
                opp_val = getattr(value, "model_ModelFormat", None)
                setattr(value, "model_ModelFormat", self)

class Value:

    pass
class model_values_Function(Value):

    pass
class model_values_ArrayElement(Value):

    def __init__(self, index: str, model_values_ArrayElement: "Point" = None, model_values_ArrayElement121: "Value" = None, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.index = index
        self.model_values_ArrayElement = model_values_ArrayElement
        self.model_values_ArrayElement121 = model_values_ArrayElement121
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def model_values_ArrayElement(self):
        return self.__model_values_ArrayElement

    @model_values_ArrayElement.setter
    def model_values_ArrayElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_ArrayElement__model_values_ArrayElement", None)
        self.__model_values_ArrayElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Point119"):
                opp_val = getattr(old_value, "Point119", None)
                if opp_val == self:
                    setattr(old_value, "Point119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Point119"):
                opp_val = getattr(value, "Point119", None)
                setattr(value, "Point119", self)

    @property
    def model_values_ArrayElement121(self):
        return self.__model_values_ArrayElement121

    @model_values_ArrayElement121.setter
    def model_values_ArrayElement121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_ArrayElement__model_values_ArrayElement121", None)
        self.__model_values_ArrayElement121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Value122"):
                opp_val = getattr(old_value, "Value122", None)
                if opp_val == self:
                    setattr(old_value, "Value122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Value122"):
                opp_val = getattr(value, "Value122", None)
                setattr(value, "Value122", self)

class model_values_Image(Value):

    def __init__(self, data: str, name: str, reference: str, format: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.data = data
        self.name = name
        self.reference = reference
        self.format = format
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class model_values_Point(Value):

    def __init__(self, x: str, y: str, z: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def z(self) -> str:
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

class model_values_Composite(Value):

    pass
class model_values_Unit(Value):

    def __init__(self, unit: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class model_values_Particles(Value):

    pass
class model_values_VisualValue(Value):

    pass
class model_values_Connection(Value):

    def __init__(self, connectivity: str, model_values_Connection: "Pointer" = None, model_values_Connection116: "Pointer" = None, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.connectivity = connectivity
        self.model_values_Connection = model_values_Connection
        self.model_values_Connection116 = model_values_Connection116
        
    @property
    def connectivity(self) -> str:
        return self.__connectivity

    @connectivity.setter
    def connectivity(self, connectivity: str):
        self.__connectivity = connectivity

    @property
    def model_values_Connection(self):
        return self.__model_values_Connection

    @model_values_Connection.setter
    def model_values_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_Connection__model_values_Connection", None)
        self.__model_values_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pointer114"):
                opp_val = getattr(old_value, "Pointer114", None)
                if opp_val == self:
                    setattr(old_value, "Pointer114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pointer114"):
                opp_val = getattr(value, "Pointer114", None)
                setattr(value, "Pointer114", self)

    @property
    def model_values_Connection116(self):
        return self.__model_values_Connection116

    @model_values_Connection116.setter
    def model_values_Connection116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_Connection__model_values_Connection116", None)
        self.__model_values_Connection116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pointer117"):
                opp_val = getattr(old_value, "Pointer117", None)
                if opp_val == self:
                    setattr(old_value, "Pointer117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pointer117"):
                opp_val = getattr(value, "Pointer117", None)
                setattr(value, "Pointer117", self)

class model_values_Argument(Value):

    def __init__(self, argument: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.argument = argument
        
    @property
    def argument(self) -> str:
        return self.__argument

    @argument.setter
    def argument(self, argument: str):
        self.__argument = argument

class model_values_MDTimeSeries(Value):

    pass
class model_values_ImportValue(Value):

    def __init__(self, modelInterpreterId: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.modelInterpreterId = modelInterpreterId
        
    @property
    def modelInterpreterId(self) -> str:
        return self.__modelInterpreterId

    @modelInterpreterId.setter
    def modelInterpreterId(self, modelInterpreterId: str):
        self.__modelInterpreterId = modelInterpreterId

class model_values_MetadataValue(Value):

    pass
class model_values_ArrayValue(Value):

    pass
class model_values_Dynamics(Value):

    pass
class model_values_Pointer(Value):

    def __init__(self, path: str, model_values_Pointer83: "Point" = None, model_values_Pointer: set["PointerElement"] = None, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.path = path
        self.model_values_Pointer83 = model_values_Pointer83
        self.model_values_Pointer = model_values_Pointer if model_values_Pointer is not None else set()
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def model_values_Pointer83(self):
        return self.__model_values_Pointer83

    @model_values_Pointer83.setter
    def model_values_Pointer83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_Pointer__model_values_Pointer83", None)
        self.__model_values_Pointer83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Point84"):
                opp_val = getattr(old_value, "Point84", None)
                if opp_val == self:
                    setattr(old_value, "Point84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Point84"):
                opp_val = getattr(value, "Point84", None)
                setattr(value, "Point84", self)

    @property
    def model_values_Pointer(self):
        return self.__model_values_Pointer

    @model_values_Pointer.setter
    def model_values_Pointer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_Pointer__model_values_Pointer", None)
        self.__model_values_Pointer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PointerElement"):
                    opp_val = getattr(item, "PointerElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PointerElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PointerElement"):
                    opp_val = getattr(item, "PointerElement", None)
                    
                    setattr(item, "PointerElement", self)
                    

    def getInstancePath(self) -> str:
        # TODO: Implement getInstancePath method
        pass

class model_values_Expression(Value):

    def __init__(self, expression: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class model_values_AArrayValue(Value):

    pass
class model_values_TimeSeries(Value):

    def __init__(self, scalingFactor: str, value: str, model_values_TimeSeries: "Unit" = None, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.scalingFactor = scalingFactor
        self.value = value
        self.model_values_TimeSeries = model_values_TimeSeries
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def scalingFactor(self) -> str:
        return self.__scalingFactor

    @scalingFactor.setter
    def scalingFactor(self, scalingFactor: str):
        self.__scalingFactor = scalingFactor

    @property
    def model_values_TimeSeries(self):
        return self.__model_values_TimeSeries

    @model_values_TimeSeries.setter
    def model_values_TimeSeries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_TimeSeries__model_values_TimeSeries", None)
        self.__model_values_TimeSeries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit78"):
                opp_val = getattr(old_value, "Unit78", None)
                if opp_val == self:
                    setattr(old_value, "Unit78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit78"):
                opp_val = getattr(value, "Unit78", None)
                setattr(value, "Unit78", self)

class model_values_Quantity(Value):

    def __init__(self, scalingFactor: str, value: str, Value127: "model_values_GenericArray", Value75: "model_values_StringToValueMap", Value: "model_VariableValue", Value122: "model_values_ArrayElement", Value141: "model_variables_TypeToValueMap", Value80: "model_values_MDTimeSeries"):
        self.scalingFactor = scalingFactor
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def scalingFactor(self) -> str:
        return self.__scalingFactor

    @scalingFactor.setter
    def scalingFactor(self, scalingFactor: str):
        self.__scalingFactor = scalingFactor

class Pointer:

    pass
class Variable:

    pass
class model_GeppettoModel:

    def __init__(self, id: str, name: str, model_GeppettoModel2: set["model_GeppettoLibrary"] = None, model_GeppettoModel4: set["model_Tag"] = None, model_GeppettoModel6: set["DataSource"] = None, model_GeppettoModel8: set["Query"] = None, model_GeppettoModel: set["Variable"] = None):
        self.id = id
        self.name = name
        self.model_GeppettoModel2 = model_GeppettoModel2 if model_GeppettoModel2 is not None else set()
        self.model_GeppettoModel4 = model_GeppettoModel4 if model_GeppettoModel4 is not None else set()
        self.model_GeppettoModel6 = model_GeppettoModel6 if model_GeppettoModel6 is not None else set()
        self.model_GeppettoModel8 = model_GeppettoModel8 if model_GeppettoModel8 is not None else set()
        self.model_GeppettoModel = model_GeppettoModel if model_GeppettoModel is not None else set()
        
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
    def model_GeppettoModel8(self):
        return self.__model_GeppettoModel8

    @model_GeppettoModel8.setter
    def model_GeppettoModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoModel__model_GeppettoModel8", None)
        self.__model_GeppettoModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    if opp_val == self:
                        setattr(item, "Query", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    setattr(item, "Query", self)
                    

    @property
    def model_GeppettoModel4(self):
        return self.__model_GeppettoModel4

    @model_GeppettoModel4.setter
    def model_GeppettoModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoModel__model_GeppettoModel4", None)
        self.__model_GeppettoModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Tag"):
                    opp_val = getattr(item, "model_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Tag"):
                    opp_val = getattr(item, "model_Tag", None)
                    
                    setattr(item, "model_Tag", self)
                    

    @property
    def model_GeppettoModel2(self):
        return self.__model_GeppettoModel2

    @model_GeppettoModel2.setter
    def model_GeppettoModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoModel__model_GeppettoModel2", None)
        self.__model_GeppettoModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_GeppettoLibrary"):
                    opp_val = getattr(item, "model_GeppettoLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "model_GeppettoLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_GeppettoLibrary"):
                    opp_val = getattr(item, "model_GeppettoLibrary", None)
                    
                    setattr(item, "model_GeppettoLibrary", self)
                    

    @property
    def model_GeppettoModel(self):
        return self.__model_GeppettoModel

    @model_GeppettoModel.setter
    def model_GeppettoModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoModel__model_GeppettoModel", None)
        self.__model_GeppettoModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def model_GeppettoModel6(self):
        return self.__model_GeppettoModel6

    @model_GeppettoModel6.setter
    def model_GeppettoModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoModel__model_GeppettoModel6", None)
        self.__model_GeppettoModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataSource"):
                    opp_val = getattr(item, "DataSource", None)
                    
                    if opp_val == self:
                        setattr(item, "DataSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataSource"):
                    opp_val = getattr(item, "DataSource", None)
                    
                    setattr(item, "DataSource", self)
                    

class Node:

    pass
class model_types_Type(Node):

    def __init__(self, abstract: str, model_types_Type: set["Type"] = None, model_types_Type33: "VisualType" = None, Variable35: set["Variable"] = None, model_types_Type37: "types_model_DomainModel" = None):
        self.abstract = abstract
        self.model_types_Type = model_types_Type if model_types_Type is not None else set()
        self.model_types_Type33 = model_types_Type33
        self.Variable35 = Variable35 if Variable35 is not None else set()
        self.model_types_Type37 = model_types_Type37
        
    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def model_types_Type(self):
        return self.__model_types_Type

    @model_types_Type.setter
    def model_types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_Type__model_types_Type", None)
        self.__model_types_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type31"):
                    opp_val = getattr(item, "Type31", None)
                    
                    if opp_val == self:
                        setattr(item, "Type31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type31"):
                    opp_val = getattr(item, "Type31", None)
                    
                    setattr(item, "Type31", self)
                    

    @property
    def model_types_Type37(self):
        return self.__model_types_Type37

    @model_types_Type37.setter
    def model_types_Type37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_Type__model_types_Type37", None)
        self.__model_types_Type37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_model_DomainModel"):
                opp_val = getattr(old_value, "types_model_DomainModel", None)
                if opp_val == self:
                    setattr(old_value, "types_model_DomainModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_model_DomainModel"):
                opp_val = getattr(value, "types_model_DomainModel", None)
                setattr(value, "types_model_DomainModel", self)

    @property
    def Variable35(self):
        return self.__Variable35

    @Variable35.setter
    def Variable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_Type__Variable35", None)
        self.__Variable35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variables"):
                    opp_val = getattr(item, "variables", None)
                    
                    if opp_val == self:
                        setattr(item, "variables", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables"):
                    opp_val = getattr(item, "variables", None)
                    
                    setattr(item, "variables", self)
                    

    @property
    def model_types_Type33(self):
        return self.__model_types_Type33

    @model_types_Type33.setter
    def model_types_Type33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_Type__model_types_Type33", None)
        self.__model_types_Type33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualType"):
                opp_val = getattr(old_value, "VisualType", None)
                if opp_val == self:
                    setattr(old_value, "VisualType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualType"):
                opp_val = getattr(value, "VisualType", None)
                setattr(value, "VisualType", self)

    def extendsType(self, type: str) -> str:
        # TODO: Implement extendsType method
        pass

    def getDefaultValue(self) -> str:
        # TODO: Implement getDefaultValue method
        pass

class model_datasources_DataSource(Node):

    def __init__(self, url: str, dataSourceService: str, model_datasources_DataSource144: set["Query"] = None, model_datasources_DataSource147: set["datasources_model_GeppettoLibrary"] = None, model_datasources_DataSource149: "datasources_model_GeppettoLibrary" = None, model_datasources_DataSource152: "Query" = None, model_datasources_DataSource: set["DataSourceLibraryConfiguration"] = None):
        self.url = url
        self.dataSourceService = dataSourceService
        self.model_datasources_DataSource144 = model_datasources_DataSource144 if model_datasources_DataSource144 is not None else set()
        self.model_datasources_DataSource147 = model_datasources_DataSource147 if model_datasources_DataSource147 is not None else set()
        self.model_datasources_DataSource149 = model_datasources_DataSource149
        self.model_datasources_DataSource152 = model_datasources_DataSource152
        self.model_datasources_DataSource = model_datasources_DataSource if model_datasources_DataSource is not None else set()
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def dataSourceService(self) -> str:
        return self.__dataSourceService

    @dataSourceService.setter
    def dataSourceService(self, dataSourceService: str):
        self.__dataSourceService = dataSourceService

    @property
    def model_datasources_DataSource152(self):
        return self.__model_datasources_DataSource152

    @model_datasources_DataSource152.setter
    def model_datasources_DataSource152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSource__model_datasources_DataSource152", None)
        self.__model_datasources_DataSource152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Query153"):
                opp_val = getattr(old_value, "Query153", None)
                if opp_val == self:
                    setattr(old_value, "Query153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Query153"):
                opp_val = getattr(value, "Query153", None)
                setattr(value, "Query153", self)

    @property
    def model_datasources_DataSource(self):
        return self.__model_datasources_DataSource

    @model_datasources_DataSource.setter
    def model_datasources_DataSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSource__model_datasources_DataSource", None)
        self.__model_datasources_DataSource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataSourceLibraryConfiguration"):
                    opp_val = getattr(item, "DataSourceLibraryConfiguration", None)
                    
                    if opp_val == self:
                        setattr(item, "DataSourceLibraryConfiguration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataSourceLibraryConfiguration"):
                    opp_val = getattr(item, "DataSourceLibraryConfiguration", None)
                    
                    setattr(item, "DataSourceLibraryConfiguration", self)
                    

    @property
    def model_datasources_DataSource149(self):
        return self.__model_datasources_DataSource149

    @model_datasources_DataSource149.setter
    def model_datasources_DataSource149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSource__model_datasources_DataSource149", None)
        self.__model_datasources_DataSource149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasources_model_GeppettoLibrary150"):
                opp_val = getattr(old_value, "datasources_model_GeppettoLibrary150", None)
                if opp_val == self:
                    setattr(old_value, "datasources_model_GeppettoLibrary150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasources_model_GeppettoLibrary150"):
                opp_val = getattr(value, "datasources_model_GeppettoLibrary150", None)
                setattr(value, "datasources_model_GeppettoLibrary150", self)

    @property
    def model_datasources_DataSource144(self):
        return self.__model_datasources_DataSource144

    @model_datasources_DataSource144.setter
    def model_datasources_DataSource144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSource__model_datasources_DataSource144", None)
        self.__model_datasources_DataSource144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Query145"):
                    opp_val = getattr(item, "Query145", None)
                    
                    if opp_val == self:
                        setattr(item, "Query145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Query145"):
                    opp_val = getattr(item, "Query145", None)
                    
                    setattr(item, "Query145", self)
                    

    @property
    def model_datasources_DataSource147(self):
        return self.__model_datasources_DataSource147

    @model_datasources_DataSource147.setter
    def model_datasources_DataSource147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_DataSource__model_datasources_DataSource147", None)
        self.__model_datasources_DataSource147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datasources_model_GeppettoLibrary"):
                    opp_val = getattr(item, "datasources_model_GeppettoLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "datasources_model_GeppettoLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datasources_model_GeppettoLibrary"):
                    opp_val = getattr(item, "datasources_model_GeppettoLibrary", None)
                    
                    setattr(item, "datasources_model_GeppettoLibrary", self)
                    

class model_values_VisualGroupElement(Node):

    def __init__(self, defaultColor: str, model_values_VisualGroupElement: "Quantity" = None):
        self.defaultColor = defaultColor
        self.model_values_VisualGroupElement = model_values_VisualGroupElement
        
    @property
    def defaultColor(self) -> str:
        return self.__defaultColor

    @defaultColor.setter
    def defaultColor(self, defaultColor: str):
        self.__defaultColor = defaultColor

    @property
    def model_values_VisualGroupElement(self):
        return self.__model_values_VisualGroupElement

    @model_values_VisualGroupElement.setter
    def model_values_VisualGroupElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_VisualGroupElement__model_values_VisualGroupElement", None)
        self.__model_values_VisualGroupElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Quantity110"):
                opp_val = getattr(old_value, "Quantity110", None)
                if opp_val == self:
                    setattr(old_value, "Quantity110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Quantity110"):
                opp_val = getattr(value, "Quantity110", None)
                setattr(value, "Quantity110", self)

class model_datasources_Query(Node):

    def __init__(self, description: str, runForCount: str, model_datasources_Query: set["QueryMatchingCriteria"] = None, model_datasources_Query158: "Type" = None):
        self.description = description
        self.runForCount = runForCount
        self.model_datasources_Query = model_datasources_Query if model_datasources_Query is not None else set()
        self.model_datasources_Query158 = model_datasources_Query158
        
    @property
    def runForCount(self) -> str:
        return self.__runForCount

    @runForCount.setter
    def runForCount(self, runForCount: str):
        self.__runForCount = runForCount

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def model_datasources_Query158(self):
        return self.__model_datasources_Query158

    @model_datasources_Query158.setter
    def model_datasources_Query158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_Query__model_datasources_Query158", None)
        self.__model_datasources_Query158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type159"):
                opp_val = getattr(old_value, "Type159", None)
                if opp_val == self:
                    setattr(old_value, "Type159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type159"):
                opp_val = getattr(value, "Type159", None)
                setattr(value, "Type159", self)

    @property
    def model_datasources_Query(self):
        return self.__model_datasources_Query

    @model_datasources_Query.setter
    def model_datasources_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_Query__model_datasources_Query", None)
        self.__model_datasources_Query = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryMatchingCriteria"):
                    opp_val = getattr(item, "QueryMatchingCriteria", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryMatchingCriteria", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryMatchingCriteria"):
                    opp_val = getattr(item, "QueryMatchingCriteria", None)
                    
                    setattr(item, "QueryMatchingCriteria", self)
                    

class model_values_VisualGroup(Node):

    def __init__(self, lowSpectrumColor: str, highSpectrumColor: str, type: str, model_values_VisualGroup: set["VisualGroupElement"] = None):
        self.lowSpectrumColor = lowSpectrumColor
        self.highSpectrumColor = highSpectrumColor
        self.type = type
        self.model_values_VisualGroup = model_values_VisualGroup if model_values_VisualGroup is not None else set()
        
    @property
    def highSpectrumColor(self) -> str:
        return self.__highSpectrumColor

    @highSpectrumColor.setter
    def highSpectrumColor(self, highSpectrumColor: str):
        self.__highSpectrumColor = highSpectrumColor

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lowSpectrumColor(self) -> str:
        return self.__lowSpectrumColor

    @lowSpectrumColor.setter
    def lowSpectrumColor(self, lowSpectrumColor: str):
        self.__lowSpectrumColor = lowSpectrumColor

    @property
    def model_values_VisualGroup(self):
        return self.__model_values_VisualGroup

    @model_values_VisualGroup.setter
    def model_values_VisualGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_values_VisualGroup__model_values_VisualGroup", None)
        self.__model_values_VisualGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualGroupElement112"):
                    opp_val = getattr(item, "VisualGroupElement112", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualGroupElement112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualGroupElement112"):
                    opp_val = getattr(item, "VisualGroupElement112", None)
                    
                    setattr(item, "VisualGroupElement112", self)
                    

class model_variables_Variable(Node):

    def __init__(self, static: str, model_variables_Variable: set["Type"] = None, Type131: set["Type"] = None, model_variables_Variable133: set["TypeToValueMap"] = None, model_variables_Variable135: "Point" = None):
        self.static = static
        self.model_variables_Variable = model_variables_Variable if model_variables_Variable is not None else set()
        self.Type131 = Type131 if Type131 is not None else set()
        self.model_variables_Variable133 = model_variables_Variable133 if model_variables_Variable133 is not None else set()
        self.model_variables_Variable135 = model_variables_Variable135
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def model_variables_Variable135(self):
        return self.__model_variables_Variable135

    @model_variables_Variable135.setter
    def model_variables_Variable135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_variables_Variable__model_variables_Variable135", None)
        self.__model_variables_Variable135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Point136"):
                opp_val = getattr(old_value, "Point136", None)
                if opp_val == self:
                    setattr(old_value, "Point136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Point136"):
                opp_val = getattr(value, "Point136", None)
                setattr(value, "Point136", self)

    @property
    def Type131(self):
        return self.__Type131

    @Type131.setter
    def Type131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_variables_Variable__Type131", None)
        self.__Type131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types"):
                    opp_val = getattr(item, "types", None)
                    
                    if opp_val == self:
                        setattr(item, "types", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types"):
                    opp_val = getattr(item, "types", None)
                    
                    setattr(item, "types", self)
                    

    @property
    def model_variables_Variable133(self):
        return self.__model_variables_Variable133

    @model_variables_Variable133.setter
    def model_variables_Variable133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_variables_Variable__model_variables_Variable133", None)
        self.__model_variables_Variable133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeToValueMap"):
                    opp_val = getattr(item, "TypeToValueMap", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeToValueMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeToValueMap"):
                    opp_val = getattr(item, "TypeToValueMap", None)
                    
                    setattr(item, "TypeToValueMap", self)
                    

    @property
    def model_variables_Variable(self):
        return self.__model_variables_Variable

    @model_variables_Variable.setter
    def model_variables_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_variables_Variable__model_variables_Variable", None)
        self.__model_variables_Variable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type129"):
                    opp_val = getattr(item, "Type129", None)
                    
                    if opp_val == self:
                        setattr(item, "Type129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type129"):
                    opp_val = getattr(item, "Type129", None)
                    
                    setattr(item, "Type129", self)
                    

class ISynchable:

    pass
class model_values_Value(ISynchable):

    pass
class model_Node(ISynchable):

    def __init__(self, id: str, name: str, model_Node: set["model_Tag"] = None):
        self.id = id
        self.name = name
        self.model_Node = model_Node if model_Node is not None else set()
        
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
    def model_Node(self):
        return self.__model_Node

    @model_Node.setter
    def model_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node", None)
        self.__model_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Tag10"):
                    opp_val = getattr(item, "model_Tag10", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Tag10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Tag10"):
                    opp_val = getattr(item, "model_Tag10", None)
                    
                    setattr(item, "model_Tag10", self)
                    

    def getPath(self) -> str:
        # TODO: Implement getPath method
        pass

class Query:

    pass
class model_datasources_CompoundQuery(Query):

    pass
class model_datasources_SimpleQuery(Query):

    def __init__(self, query: str, countQuery: str, Query162: "model_datasources_CompoundQuery", Query145: "model_datasources_DataSource", Query164: "model_datasources_CompoundRefQuery", Query: "model_GeppettoModel", Query153: "model_datasources_DataSource"):
        self.query = query
        self.countQuery = countQuery
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def countQuery(self) -> str:
        return self.__countQuery

    @countQuery.setter
    def countQuery(self, countQuery: str):
        self.__countQuery = countQuery

class model_datasources_ProcessQuery(Query):

    def __init__(self, queryProcessorId: str, model_datasources_ProcessQuery: set["datasources_model_StringToStringMap"] = None, Query162: "model_datasources_CompoundQuery", Query145: "model_datasources_DataSource", Query164: "model_datasources_CompoundRefQuery", Query: "model_GeppettoModel", Query153: "model_datasources_DataSource"):
        self.queryProcessorId = queryProcessorId
        self.model_datasources_ProcessQuery = model_datasources_ProcessQuery if model_datasources_ProcessQuery is not None else set()
        
    @property
    def queryProcessorId(self) -> str:
        return self.__queryProcessorId

    @queryProcessorId.setter
    def queryProcessorId(self, queryProcessorId: str):
        self.__queryProcessorId = queryProcessorId

    @property
    def model_datasources_ProcessQuery(self):
        return self.__model_datasources_ProcessQuery

    @model_datasources_ProcessQuery.setter
    def model_datasources_ProcessQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_datasources_ProcessQuery__model_datasources_ProcessQuery", None)
        self.__model_datasources_ProcessQuery = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datasources_model_StringToStringMap"):
                    opp_val = getattr(item, "datasources_model_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "datasources_model_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datasources_model_StringToStringMap"):
                    opp_val = getattr(item, "datasources_model_StringToStringMap", None)
                    
                    setattr(item, "datasources_model_StringToStringMap", self)
                    

class model_datasources_CompoundRefQuery(Query):

    pass
class DataSource:

    pass
class model_Tag(ISynchable):

    def __init__(self, name: str, model_Tag: "model_GeppettoModel" = None, model_Tag10: "model_Node" = None, model_Tag28: "model_Tag" = None, model_Tag26: set["model_Tag"] = None):
        self.name = name
        self.model_Tag = model_Tag
        self.model_Tag10 = model_Tag10
        self.model_Tag28 = model_Tag28
        self.model_Tag26 = model_Tag26 if model_Tag26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Tag10(self):
        return self.__model_Tag10

    @model_Tag10.setter
    def model_Tag10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Tag__model_Tag10", None)
        self.__model_Tag10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node"):
                opp_val = getattr(old_value, "model_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node"):
                opp_val = getattr(value, "model_Node", None)
                if opp_val is None:
                    setattr(value, "model_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Tag26(self):
        return self.__model_Tag26

    @model_Tag26.setter
    def model_Tag26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Tag__model_Tag26", None)
        self.__model_Tag26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Tag28"):
                    opp_val = getattr(item, "model_Tag28", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Tag28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Tag28"):
                    opp_val = getattr(item, "model_Tag28", None)
                    
                    setattr(item, "model_Tag28", self)
                    

    @property
    def model_Tag28(self):
        return self.__model_Tag28

    @model_Tag28.setter
    def model_Tag28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Tag__model_Tag28", None)
        self.__model_Tag28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Tag26"):
                opp_val = getattr(old_value, "model_Tag26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Tag26"):
                opp_val = getattr(value, "model_Tag26", None)
                if opp_val is None:
                    setattr(value, "model_Tag26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Tag(self):
        return self.__model_Tag

    @model_Tag.setter
    def model_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Tag__model_Tag", None)
        self.__model_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_GeppettoModel4"):
                opp_val = getattr(old_value, "model_GeppettoModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_GeppettoModel4"):
                opp_val = getattr(value, "model_GeppettoModel4", None)
                if opp_val is None:
                    setattr(value, "model_GeppettoModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_GeppettoLibrary(Node):

    def __init__(self, model_GeppettoLibrary: "model_GeppettoModel" = None, model_GeppettoLibrary12: set["Type"] = None, model_GeppettoLibrary14: set["Type"] = None, model_GeppettoLibrary17: "model_LibraryManager" = None):
        self.model_GeppettoLibrary = model_GeppettoLibrary
        self.model_GeppettoLibrary12 = model_GeppettoLibrary12 if model_GeppettoLibrary12 is not None else set()
        self.model_GeppettoLibrary14 = model_GeppettoLibrary14 if model_GeppettoLibrary14 is not None else set()
        self.model_GeppettoLibrary17 = model_GeppettoLibrary17
        
    @property
    def model_GeppettoLibrary(self):
        return self.__model_GeppettoLibrary

    @model_GeppettoLibrary.setter
    def model_GeppettoLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoLibrary__model_GeppettoLibrary", None)
        self.__model_GeppettoLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_GeppettoModel2"):
                opp_val = getattr(old_value, "model_GeppettoModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_GeppettoModel2"):
                opp_val = getattr(value, "model_GeppettoModel2", None)
                if opp_val is None:
                    setattr(value, "model_GeppettoModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_GeppettoLibrary14(self):
        return self.__model_GeppettoLibrary14

    @model_GeppettoLibrary14.setter
    def model_GeppettoLibrary14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoLibrary__model_GeppettoLibrary14", None)
        self.__model_GeppettoLibrary14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type15"):
                    opp_val = getattr(item, "Type15", None)
                    
                    if opp_val == self:
                        setattr(item, "Type15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type15"):
                    opp_val = getattr(item, "Type15", None)
                    
                    setattr(item, "Type15", self)
                    

    @property
    def model_GeppettoLibrary17(self):
        return self.__model_GeppettoLibrary17

    @model_GeppettoLibrary17.setter
    def model_GeppettoLibrary17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoLibrary__model_GeppettoLibrary17", None)
        self.__model_GeppettoLibrary17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_LibraryManager"):
                opp_val = getattr(old_value, "model_LibraryManager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_LibraryManager"):
                opp_val = getattr(value, "model_LibraryManager", None)
                if opp_val is None:
                    setattr(value, "model_LibraryManager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_GeppettoLibrary12(self):
        return self.__model_GeppettoLibrary12

    @model_GeppettoLibrary12.setter
    def model_GeppettoLibrary12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GeppettoLibrary__model_GeppettoLibrary12", None)
        self.__model_GeppettoLibrary12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    def getTypeById(self) -> str:
        # TODO: Implement getTypeById method
        pass
