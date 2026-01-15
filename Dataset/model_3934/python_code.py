from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnumLiteralPropertyAttributeType(Enum):
    measurementUnit = "measurementUnit"
class BooleanPropertyAttributeType(Enum):
    readable = "readable"
    writable = "writable"
    eventable = "eventable"
class PrimitiveType(Enum):
    string = "string"
    int = "int"
    float = "float"
    boolean = "boolean"
    datetime = "datetime"
    double = "double"
    long = "long"
    short = "short"
    base64Binary = "base64Binary"
    byte = "byte"
class ConstraintIntervalType(Enum):
    min = "min"
    max = "max"
    strlen = "strlen"
    regex = "regex"
    mimetype = "mimetype"
    scaling = "scaling"


############################################
# Definition of Classes
############################################

class PropertyAttribute:

    pass
class datatype_BooleanPropertyAttribute(PropertyAttribute):

    def __init__(self, type: str, value: bool):
        self.type = type
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Model:

    pass
class datatype_EnumLiteral:

    def __init__(self, name: str, description: str, datatype_EnumLiteral15: "datatype_EnumLiteralPropertyAttribute" = None, datatype_EnumLiteral: "datatype_Enum" = None):
        self.name = name
        self.description = description
        self.datatype_EnumLiteral15 = datatype_EnumLiteral15
        self.datatype_EnumLiteral = datatype_EnumLiteral
        
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
    def datatype_EnumLiteral15(self):
        return self.__datatype_EnumLiteral15

    @datatype_EnumLiteral15.setter
    def datatype_EnumLiteral15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_EnumLiteral__datatype_EnumLiteral15", None)
        self.__datatype_EnumLiteral15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_EnumLiteralPropertyAttribute"):
                opp_val = getattr(old_value, "datatype_EnumLiteralPropertyAttribute", None)
                if opp_val == self:
                    setattr(old_value, "datatype_EnumLiteralPropertyAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_EnumLiteralPropertyAttribute"):
                opp_val = getattr(value, "datatype_EnumLiteralPropertyAttribute", None)
                setattr(value, "datatype_EnumLiteralPropertyAttribute", self)

    @property
    def datatype_EnumLiteral(self):
        return self.__datatype_EnumLiteral

    @datatype_EnumLiteral.setter
    def datatype_EnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_EnumLiteral__datatype_EnumLiteral", None)
        self.__datatype_EnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_Enum"):
                opp_val = getattr(old_value, "datatype_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_Enum"):
                opp_val = getattr(value, "datatype_Enum", None)
                if opp_val is None:
                    setattr(value, "datatype_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComplexPrimitivePropertyType:

    pass
class datatype_DictionaryPropertyType(ComplexPrimitivePropertyType):

    pass
class datatype_EnumLiteralPropertyAttribute(PropertyAttribute):

    def __init__(self, type: str, datatype_EnumLiteralPropertyAttribute: "datatype_EnumLiteral" = None):
        self.type = type
        self.datatype_EnumLiteralPropertyAttribute = datatype_EnumLiteralPropertyAttribute
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def datatype_EnumLiteralPropertyAttribute(self):
        return self.__datatype_EnumLiteralPropertyAttribute

    @datatype_EnumLiteralPropertyAttribute.setter
    def datatype_EnumLiteralPropertyAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_EnumLiteralPropertyAttribute__datatype_EnumLiteralPropertyAttribute", None)
        self.__datatype_EnumLiteralPropertyAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_EnumLiteral15"):
                opp_val = getattr(old_value, "datatype_EnumLiteral15", None)
                if opp_val == self:
                    setattr(old_value, "datatype_EnumLiteral15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_EnumLiteral15"):
                opp_val = getattr(value, "datatype_EnumLiteral15", None)
                setattr(value, "datatype_EnumLiteral15", self)

class PropertyType:

    pass
class datatype_ComplexPrimitivePropertyType(PropertyType):

    pass
class datatype_PrimitivePropertyType(PropertyType):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class datatype_PropertyAttribute(ABC):

    pass
class datatype_PropertyType:

    pass
class datatype_ConstraintRule:

    pass
class datatype_Presence:

    def __init__(self, mandatory: bool, datatype_Presence: "datatype_Property" = None):
        self.mandatory = mandatory
        self.datatype_Presence = datatype_Presence
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def datatype_Presence(self):
        return self.__datatype_Presence

    @datatype_Presence.setter
    def datatype_Presence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Presence__datatype_Presence", None)
        self.__datatype_Presence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_Property5"):
                opp_val = getattr(old_value, "datatype_Property5", None)
                if opp_val == self:
                    setattr(old_value, "datatype_Property5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_Property5"):
                opp_val = getattr(value, "datatype_Property5", None)
                setattr(value, "datatype_Property5", self)

class datatype_Property:

    def __init__(self, multiplicity: bool, name: str, description: str, datatype_Property: "datatype_Entity" = None, datatype_Property5: "datatype_Presence" = None, datatype_Property7: "datatype_ConstraintRule" = None, datatype_Property9: "datatype_PropertyType" = None, datatype_Property11: set["datatype_PropertyAttribute"] = None):
        self.multiplicity = multiplicity
        self.name = name
        self.description = description
        self.datatype_Property = datatype_Property
        self.datatype_Property5 = datatype_Property5
        self.datatype_Property7 = datatype_Property7
        self.datatype_Property9 = datatype_Property9
        self.datatype_Property11 = datatype_Property11 if datatype_Property11 is not None else set()
        
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
    def multiplicity(self) -> bool:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: bool):
        self.__multiplicity = multiplicity

    @property
    def datatype_Property(self):
        return self.__datatype_Property

    @datatype_Property.setter
    def datatype_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Property__datatype_Property", None)
        self.__datatype_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_Entity3"):
                opp_val = getattr(old_value, "datatype_Entity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_Entity3"):
                opp_val = getattr(value, "datatype_Entity3", None)
                if opp_val is None:
                    setattr(value, "datatype_Entity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datatype_Property5(self):
        return self.__datatype_Property5

    @datatype_Property5.setter
    def datatype_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Property__datatype_Property5", None)
        self.__datatype_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_Presence"):
                opp_val = getattr(old_value, "datatype_Presence", None)
                if opp_val == self:
                    setattr(old_value, "datatype_Presence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_Presence"):
                opp_val = getattr(value, "datatype_Presence", None)
                setattr(value, "datatype_Presence", self)

    @property
    def datatype_Property11(self):
        return self.__datatype_Property11

    @datatype_Property11.setter
    def datatype_Property11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Property__datatype_Property11", None)
        self.__datatype_Property11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datatype_PropertyAttribute"):
                    opp_val = getattr(item, "datatype_PropertyAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "datatype_PropertyAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datatype_PropertyAttribute"):
                    opp_val = getattr(item, "datatype_PropertyAttribute", None)
                    
                    setattr(item, "datatype_PropertyAttribute", self)
                    

    @property
    def datatype_Property9(self):
        return self.__datatype_Property9

    @datatype_Property9.setter
    def datatype_Property9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Property__datatype_Property9", None)
        self.__datatype_Property9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_PropertyType"):
                opp_val = getattr(old_value, "datatype_PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "datatype_PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_PropertyType"):
                opp_val = getattr(value, "datatype_PropertyType", None)
                setattr(value, "datatype_PropertyType", self)

    @property
    def datatype_Property7(self):
        return self.__datatype_Property7

    @datatype_Property7.setter
    def datatype_Property7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Property__datatype_Property7", None)
        self.__datatype_Property7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_ConstraintRule"):
                opp_val = getattr(old_value, "datatype_ConstraintRule", None)
                if opp_val == self:
                    setattr(old_value, "datatype_ConstraintRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_ConstraintRule"):
                opp_val = getattr(value, "datatype_ConstraintRule", None)
                setattr(value, "datatype_ConstraintRule", self)

class datatype_Constraint:

    def __init__(self, type: str, constraintValues: str, datatype_Constraint: "datatype_ConstraintRule" = None):
        self.type = type
        self.constraintValues = constraintValues
        self.datatype_Constraint = datatype_Constraint
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def constraintValues(self) -> str:
        return self.__constraintValues

    @constraintValues.setter
    def constraintValues(self, constraintValues: str):
        self.__constraintValues = constraintValues

    @property
    def datatype_Constraint(self):
        return self.__datatype_Constraint

    @datatype_Constraint.setter
    def datatype_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatype_Constraint__datatype_Constraint", None)
        self.__datatype_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype_ConstraintRule17"):
                opp_val = getattr(old_value, "datatype_ConstraintRule17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype_ConstraintRule17"):
                opp_val = getattr(value, "datatype_ConstraintRule17", None)
                if opp_val is None:
                    setattr(value, "datatype_ConstraintRule17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datatype_Type(Model):

    pass
class datatype_ObjectPropertyType(PropertyType):

    pass
class Type:

    pass
class datatype_Enum(Type):

    pass
class datatype_Entity(Type):

    pass