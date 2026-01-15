from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ValueType(Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    INT_RANGE = "INT_RANGE"
    FORMAT_RANGE = "FORMAT_RANGE"


############################################
# Definition of Classes
############################################

class Value:

    pass
class modelDsl_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class modelDsl_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class AnnoTypes:

    pass
class modelDsl_AnnotationType(AnnoTypes):

    pass
class modelDsl_PropertyType(AnnoTypes):

    pass
class modelDsl_DataTypeType(AnnoTypes):

    pass
class modelDsl_ReferenceListType(AnnoTypes):

    pass
class modelDsl_PackageType(AnnoTypes):

    pass
class modelDsl_ParentType(AnnoTypes):

    pass
class modelDsl_ChildType(AnnoTypes):

    pass
class modelDsl_EntityType(AnnoTypes):

    pass
class modelDsl_ReferenceType(AnnoTypes):

    pass
class modelDsl_Annotated:

    pass
class modelDsl_FormatRangeValue(Value):

    def __init__(self, from: str, to: str):
        self.from = from
        self.to = to
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

class modelDsl_RangeValue(Value):

    def __init__(self, from: int, fromInf: bool, to: int, toInf: bool):
        self.from = from
        self.fromInf = fromInf
        self.to = to
        self.toInf = toInf
        
    @property
    def fromInf(self) -> bool:
        return self.__fromInf

    @fromInf.setter
    def fromInf(self, fromInf: bool):
        self.__fromInf = fromInf

    @property
    def from(self) -> int:
        return self.__from

    @from.setter
    def from(self, from: int):
        self.__from = from

    @property
    def toInf(self) -> bool:
        return self.__toInf

    @toInf.setter
    def toInf(self, toInf: bool):
        self.__toInf = toInf

    @property
    def to(self) -> int:
        return self.__to

    @to.setter
    def to(self, to: int):
        self.__to = to

class modelDsl_DoubleValue(Value):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class modelDsl_AnnoTypes:

    def __init__(self, type: str, modelDsl_AnnoTypes: "modelDsl_Annotation" = None):
        self.type = type
        self.modelDsl_AnnoTypes = modelDsl_AnnoTypes
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def modelDsl_AnnoTypes(self):
        return self.__modelDsl_AnnoTypes

    @modelDsl_AnnoTypes.setter
    def modelDsl_AnnoTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_AnnoTypes__modelDsl_AnnoTypes", None)
        self.__modelDsl_AnnoTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Annotation"):
                opp_val = getattr(old_value, "modelDsl_Annotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Annotation"):
                opp_val = getattr(value, "modelDsl_Annotation", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Annotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Field:

    pass
class Container:

    pass
class modelDsl_AnnotationHiddenProperty:

    pass
class modelDsl_AnnotationValue:

    pass
class AnnotationValue:

    pass
class modelDsl_Value(AnnotationValue):

    pass
class modelDsl_GroupType(AnnoTypes):

    def __init__(self, name: str, modelDsl_GroupType: "modelDsl_AnnotationProperty" = None):
        self.name = name
        self.modelDsl_GroupType = modelDsl_GroupType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_GroupType(self):
        return self.__modelDsl_GroupType

    @modelDsl_GroupType.setter
    def modelDsl_GroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_GroupType__modelDsl_GroupType", None)
        self.__modelDsl_GroupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_AnnotationProperty59"):
                opp_val = getattr(old_value, "modelDsl_AnnotationProperty59", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_AnnotationProperty59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_AnnotationProperty59"):
                opp_val = getattr(value, "modelDsl_AnnotationProperty59", None)
                setattr(value, "modelDsl_AnnotationProperty59", self)

class modelDsl_AnnotationProperty:

    def __init__(self, name: str, type: str, multi: bool, modelDsl_AnnotationProperty: "modelDsl_Annotation" = None, modelDsl_AnnotationProperty57: "modelDsl_Annotation" = None, modelDsl_AnnotationProperty59: "modelDsl_GroupType" = None, modelDsl_AnnotationProperty72: "modelDsl_AnnotationHiddenProperty" = None):
        self.name = name
        self.type = type
        self.multi = multi
        self.modelDsl_AnnotationProperty = modelDsl_AnnotationProperty
        self.modelDsl_AnnotationProperty57 = modelDsl_AnnotationProperty57
        self.modelDsl_AnnotationProperty59 = modelDsl_AnnotationProperty59
        self.modelDsl_AnnotationProperty72 = modelDsl_AnnotationProperty72
        
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
    def multi(self) -> bool:
        return self.__multi

    @multi.setter
    def multi(self, multi: bool):
        self.__multi = multi

    @property
    def modelDsl_AnnotationProperty57(self):
        return self.__modelDsl_AnnotationProperty57

    @modelDsl_AnnotationProperty57.setter
    def modelDsl_AnnotationProperty57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_AnnotationProperty__modelDsl_AnnotationProperty57", None)
        self.__modelDsl_AnnotationProperty57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Annotation56"):
                opp_val = getattr(old_value, "modelDsl_Annotation56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Annotation56"):
                opp_val = getattr(value, "modelDsl_Annotation56", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Annotation56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_AnnotationProperty(self):
        return self.__modelDsl_AnnotationProperty

    @modelDsl_AnnotationProperty.setter
    def modelDsl_AnnotationProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_AnnotationProperty__modelDsl_AnnotationProperty", None)
        self.__modelDsl_AnnotationProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Annotation54"):
                opp_val = getattr(old_value, "modelDsl_Annotation54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Annotation54"):
                opp_val = getattr(value, "modelDsl_Annotation54", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Annotation54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_AnnotationProperty72(self):
        return self.__modelDsl_AnnotationProperty72

    @modelDsl_AnnotationProperty72.setter
    def modelDsl_AnnotationProperty72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_AnnotationProperty__modelDsl_AnnotationProperty72", None)
        self.__modelDsl_AnnotationProperty72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_AnnotationHiddenProperty71"):
                opp_val = getattr(old_value, "modelDsl_AnnotationHiddenProperty71", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_AnnotationHiddenProperty71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_AnnotationHiddenProperty71"):
                opp_val = getattr(value, "modelDsl_AnnotationHiddenProperty71", None)
                setattr(value, "modelDsl_AnnotationHiddenProperty71", self)

    @property
    def modelDsl_AnnotationProperty59(self):
        return self.__modelDsl_AnnotationProperty59

    @modelDsl_AnnotationProperty59.setter
    def modelDsl_AnnotationProperty59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_AnnotationProperty__modelDsl_AnnotationProperty59", None)
        self.__modelDsl_AnnotationProperty59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_GroupType"):
                opp_val = getattr(old_value, "modelDsl_GroupType", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_GroupType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_GroupType"):
                opp_val = getattr(value, "modelDsl_GroupType", None)
                setattr(value, "modelDsl_GroupType", self)

class modelDsl_PatternType:

    def __init__(self, REGEX: str, DATE: str, NUMBER: str, modelDsl_PatternType: "modelDsl_DataTypeField" = None):
        self.REGEX = REGEX
        self.DATE = DATE
        self.NUMBER = NUMBER
        self.modelDsl_PatternType = modelDsl_PatternType
        
    @property
    def DATE(self) -> str:
        return self.__DATE

    @DATE.setter
    def DATE(self, DATE: str):
        self.__DATE = DATE

    @property
    def NUMBER(self) -> str:
        return self.__NUMBER

    @NUMBER.setter
    def NUMBER(self, NUMBER: str):
        self.__NUMBER = NUMBER

    @property
    def REGEX(self) -> str:
        return self.__REGEX

    @REGEX.setter
    def REGEX(self, REGEX: str):
        self.__REGEX = REGEX

    @property
    def modelDsl_PatternType(self):
        return self.__modelDsl_PatternType

    @modelDsl_PatternType.setter
    def modelDsl_PatternType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_PatternType__modelDsl_PatternType", None)
        self.__modelDsl_PatternType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DataTypeField11"):
                opp_val = getattr(old_value, "modelDsl_DataTypeField11", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_DataTypeField11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DataTypeField11"):
                opp_val = getattr(value, "modelDsl_DataTypeField11", None)
                setattr(value, "modelDsl_DataTypeField11", self)

class modelDsl_DataTypeField:

    def __init__(self, format: str, modelDsl_DataTypeField13: "modelDsl_DataType" = None, modelDsl_DataTypeField: "modelDsl_DataType" = None, modelDsl_DataTypeField11: "modelDsl_PatternType" = None):
        self.format = format
        self.modelDsl_DataTypeField13 = modelDsl_DataTypeField13
        self.modelDsl_DataTypeField = modelDsl_DataTypeField
        self.modelDsl_DataTypeField11 = modelDsl_DataTypeField11
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def modelDsl_DataTypeField11(self):
        return self.__modelDsl_DataTypeField11

    @modelDsl_DataTypeField11.setter
    def modelDsl_DataTypeField11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DataTypeField__modelDsl_DataTypeField11", None)
        self.__modelDsl_DataTypeField11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_PatternType"):
                opp_val = getattr(old_value, "modelDsl_PatternType", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_PatternType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_PatternType"):
                opp_val = getattr(value, "modelDsl_PatternType", None)
                setattr(value, "modelDsl_PatternType", self)

    @property
    def modelDsl_DataTypeField(self):
        return self.__modelDsl_DataTypeField

    @modelDsl_DataTypeField.setter
    def modelDsl_DataTypeField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DataTypeField__modelDsl_DataTypeField", None)
        self.__modelDsl_DataTypeField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DataType"):
                opp_val = getattr(old_value, "modelDsl_DataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DataType"):
                opp_val = getattr(value, "modelDsl_DataType", None)
                if opp_val is None:
                    setattr(value, "modelDsl_DataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_DataTypeField13(self):
        return self.__modelDsl_DataTypeField13

    @modelDsl_DataTypeField13.setter
    def modelDsl_DataTypeField13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_DataTypeField__modelDsl_DataTypeField13", None)
        self.__modelDsl_DataTypeField13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_DataType14"):
                opp_val = getattr(old_value, "modelDsl_DataType14", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_DataType14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_DataType14"):
                opp_val = getattr(value, "modelDsl_DataType14", None)
                setattr(value, "modelDsl_DataType14", self)

class Type:

    pass
class modelDsl_DataType(Type):

    pass
class modelDsl_AnnotationGroup(AnnotationValue):

    pass
class Element:

    pass
class modelDsl_Annotation(Element):

    pass
class modelDsl_Package(Element):

    pass
class modelDsl_Type(Element):

    pass
class Annotated:

    pass
class modelDsl_AnnotationInstance(Annotated):

    pass
class modelDsl_Field(Annotated):

    def __init__(self, name: str, modelDsl_Field: set["modelDsl_AnnotationGroup"] = None):
        self.name = name
        self.modelDsl_Field = modelDsl_Field if modelDsl_Field is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_Field(self):
        return self.__modelDsl_Field

    @modelDsl_Field.setter
    def modelDsl_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Field__modelDsl_Field", None)
        self.__modelDsl_Field = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modelDsl_AnnotationGroup37"):
                    opp_val = getattr(item, "modelDsl_AnnotationGroup37", None)
                    
                    if opp_val == self:
                        setattr(item, "modelDsl_AnnotationGroup37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modelDsl_AnnotationGroup37"):
                    opp_val = getattr(item, "modelDsl_AnnotationGroup37", None)
                    
                    setattr(item, "modelDsl_AnnotationGroup37", self)
                    

class modelDsl_Container(Annotated):

    pass
class modelDsl_Element(Annotated):

    def __init__(self, name: str, modelDsl_Element: "modelDsl_Model" = None, modelDsl_Element8: "modelDsl_Package" = None):
        self.name = name
        self.modelDsl_Element = modelDsl_Element
        self.modelDsl_Element8 = modelDsl_Element8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_Element(self):
        return self.__modelDsl_Element

    @modelDsl_Element.setter
    def modelDsl_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Element__modelDsl_Element", None)
        self.__modelDsl_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Model2"):
                opp_val = getattr(old_value, "modelDsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Model2"):
                opp_val = getattr(value, "modelDsl_Model2", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_Element8(self):
        return self.__modelDsl_Element8

    @modelDsl_Element8.setter
    def modelDsl_Element8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Element__modelDsl_Element8", None)
        self.__modelDsl_Element8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Package7"):
                opp_val = getattr(old_value, "modelDsl_Package7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Package7"):
                opp_val = getattr(value, "modelDsl_Package7", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Package7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class modelDsl_Import:

    def __init__(self, importedNamespace: str, modelDsl_Import: "modelDsl_Model" = None):
        self.importedNamespace = importedNamespace
        self.modelDsl_Import = modelDsl_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def modelDsl_Import(self):
        return self.__modelDsl_Import

    @modelDsl_Import.setter
    def modelDsl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Import__modelDsl_Import", None)
        self.__modelDsl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Model"):
                opp_val = getattr(old_value, "modelDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Model"):
                opp_val = getattr(value, "modelDsl_Model", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class modelDsl_Model:

    pass
class modelDsl_ReferenceList(Field):

    pass
class modelDsl_Reference(Field):

    def __init__(self, optional: bool, modelDsl_Reference: "modelDsl_EntityElements" = None, modelDsl_Reference42: "modelDsl_Entity" = None, modelDsl_Reference46: "modelDsl_ReferenceList" = None):
        self.optional = optional
        self.modelDsl_Reference = modelDsl_Reference
        self.modelDsl_Reference42 = modelDsl_Reference42
        self.modelDsl_Reference46 = modelDsl_Reference46
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def modelDsl_Reference46(self):
        return self.__modelDsl_Reference46

    @modelDsl_Reference46.setter
    def modelDsl_Reference46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Reference__modelDsl_Reference46", None)
        self.__modelDsl_Reference46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_ReferenceList45"):
                opp_val = getattr(old_value, "modelDsl_ReferenceList45", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_ReferenceList45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_ReferenceList45"):
                opp_val = getattr(value, "modelDsl_ReferenceList45", None)
                setattr(value, "modelDsl_ReferenceList45", self)

    @property
    def modelDsl_Reference(self):
        return self.__modelDsl_Reference

    @modelDsl_Reference.setter
    def modelDsl_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Reference__modelDsl_Reference", None)
        self.__modelDsl_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_EntityElements28"):
                opp_val = getattr(old_value, "modelDsl_EntityElements28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_EntityElements28"):
                opp_val = getattr(value, "modelDsl_EntityElements28", None)
                if opp_val is None:
                    setattr(value, "modelDsl_EntityElements28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_Reference42(self):
        return self.__modelDsl_Reference42

    @modelDsl_Reference42.setter
    def modelDsl_Reference42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Reference__modelDsl_Reference42", None)
        self.__modelDsl_Reference42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Entity43"):
                opp_val = getattr(old_value, "modelDsl_Entity43", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_Entity43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Entity43"):
                opp_val = getattr(value, "modelDsl_Entity43", None)
                setattr(value, "modelDsl_Entity43", self)

class modelDsl_Property(Field):

    def __init__(self, optional: bool, modelDsl_Property: "modelDsl_EntityElements" = None, modelDsl_Property39: "modelDsl_Type" = None):
        self.optional = optional
        self.modelDsl_Property = modelDsl_Property
        self.modelDsl_Property39 = modelDsl_Property39
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def modelDsl_Property39(self):
        return self.__modelDsl_Property39

    @modelDsl_Property39.setter
    def modelDsl_Property39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Property__modelDsl_Property39", None)
        self.__modelDsl_Property39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Type40"):
                opp_val = getattr(old_value, "modelDsl_Type40", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_Type40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Type40"):
                opp_val = getattr(value, "modelDsl_Type40", None)
                setattr(value, "modelDsl_Type40", self)

    @property
    def modelDsl_Property(self):
        return self.__modelDsl_Property

    @modelDsl_Property.setter
    def modelDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_Property__modelDsl_Property", None)
        self.__modelDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_EntityElements26"):
                opp_val = getattr(old_value, "modelDsl_EntityElements26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_EntityElements26"):
                opp_val = getattr(value, "modelDsl_EntityElements26", None)
                if opp_val is None:
                    setattr(value, "modelDsl_EntityElements26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class modelDsl_Child(Container):

    pass
class modelDsl_EntityGroup:

    def __init__(self, name: str, modelDsl_EntityGroup: "modelDsl_Entity" = None, modelDsl_EntityGroup21: "modelDsl_EntityElements" = None):
        self.name = name
        self.modelDsl_EntityGroup = modelDsl_EntityGroup
        self.modelDsl_EntityGroup21 = modelDsl_EntityGroup21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modelDsl_EntityGroup(self):
        return self.__modelDsl_EntityGroup

    @modelDsl_EntityGroup.setter
    def modelDsl_EntityGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_EntityGroup__modelDsl_EntityGroup", None)
        self.__modelDsl_EntityGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_Entity19"):
                opp_val = getattr(old_value, "modelDsl_Entity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_Entity19"):
                opp_val = getattr(value, "modelDsl_Entity19", None)
                if opp_val is None:
                    setattr(value, "modelDsl_Entity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelDsl_EntityGroup21(self):
        return self.__modelDsl_EntityGroup21

    @modelDsl_EntityGroup21.setter
    def modelDsl_EntityGroup21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modelDsl_EntityGroup__modelDsl_EntityGroup21", None)
        self.__modelDsl_EntityGroup21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelDsl_EntityElements22"):
                opp_val = getattr(old_value, "modelDsl_EntityElements22", None)
                if opp_val == self:
                    setattr(old_value, "modelDsl_EntityElements22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelDsl_EntityElements22"):
                opp_val = getattr(value, "modelDsl_EntityElements22", None)
                setattr(value, "modelDsl_EntityElements22", self)

class modelDsl_EntityElements:

    pass
class modelDsl_Parent(Container):

    pass
class modelDsl_Entity(Type):

    pass