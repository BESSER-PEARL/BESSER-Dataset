from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ulmDsl2_LookupStringValue:

    def __init__(self, value: str, description: str, ulmDsl2_LookupStringValue: "ulmDsl2_LookupString" = None):
        self.value = value
        self.description = description
        self.ulmDsl2_LookupStringValue = ulmDsl2_LookupStringValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ulmDsl2_LookupStringValue(self):
        return self.__ulmDsl2_LookupStringValue

    @ulmDsl2_LookupStringValue.setter
    def ulmDsl2_LookupStringValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_LookupStringValue__ulmDsl2_LookupStringValue", None)
        self.__ulmDsl2_LookupStringValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_LookupString"):
                opp_val = getattr(old_value, "ulmDsl2_LookupString", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_LookupString"):
                opp_val = getattr(value, "ulmDsl2_LookupString", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_LookupString", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ulmDsl2_LookupString:

    def __init__(self, description: str, ulmDsl2_LookupString: set["ulmDsl2_LookupStringValue"] = None):
        self.description = description
        self.ulmDsl2_LookupString = ulmDsl2_LookupString if ulmDsl2_LookupString is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ulmDsl2_LookupString(self):
        return self.__ulmDsl2_LookupString

    @ulmDsl2_LookupString.setter
    def ulmDsl2_LookupString(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_LookupString__ulmDsl2_LookupString", None)
        self.__ulmDsl2_LookupString = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_LookupStringValue"):
                    opp_val = getattr(item, "ulmDsl2_LookupStringValue", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_LookupStringValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_LookupStringValue"):
                    opp_val = getattr(item, "ulmDsl2_LookupStringValue", None)
                    
                    setattr(item, "ulmDsl2_LookupStringValue", self)
                    

class ulmDsl2_LookupIntValue:

    def __init__(self, value: int, description: str, ulmDsl2_LookupIntValue: "ulmDsl2_LookupInt" = None):
        self.value = value
        self.description = description
        self.ulmDsl2_LookupIntValue = ulmDsl2_LookupIntValue
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ulmDsl2_LookupIntValue(self):
        return self.__ulmDsl2_LookupIntValue

    @ulmDsl2_LookupIntValue.setter
    def ulmDsl2_LookupIntValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_LookupIntValue__ulmDsl2_LookupIntValue", None)
        self.__ulmDsl2_LookupIntValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_LookupInt"):
                opp_val = getattr(old_value, "ulmDsl2_LookupInt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_LookupInt"):
                opp_val = getattr(value, "ulmDsl2_LookupInt", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_LookupInt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ulmDsl2_LookupInt:

    def __init__(self, description: str, ulmDsl2_LookupInt: set["ulmDsl2_LookupIntValue"] = None):
        self.description = description
        self.ulmDsl2_LookupInt = ulmDsl2_LookupInt if ulmDsl2_LookupInt is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ulmDsl2_LookupInt(self):
        return self.__ulmDsl2_LookupInt

    @ulmDsl2_LookupInt.setter
    def ulmDsl2_LookupInt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_LookupInt__ulmDsl2_LookupInt", None)
        self.__ulmDsl2_LookupInt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_LookupIntValue"):
                    opp_val = getattr(item, "ulmDsl2_LookupIntValue", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_LookupIntValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_LookupIntValue"):
                    opp_val = getattr(item, "ulmDsl2_LookupIntValue", None)
                    
                    setattr(item, "ulmDsl2_LookupIntValue", self)
                    

class ulmDsl2_EntityFeatureType:

    def __init__(self, array: bool, length: int, ulmDsl2_EntityFeatureType: "ulmDsl2_Entity" = None):
        self.array = array
        self.length = length
        self.ulmDsl2_EntityFeatureType = ulmDsl2_EntityFeatureType
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def ulmDsl2_EntityFeatureType(self):
        return self.__ulmDsl2_EntityFeatureType

    @ulmDsl2_EntityFeatureType.setter
    def ulmDsl2_EntityFeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_EntityFeatureType__ulmDsl2_EntityFeatureType", None)
        self.__ulmDsl2_EntityFeatureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Entity25"):
                opp_val = getattr(old_value, "ulmDsl2_Entity25", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_Entity25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Entity25"):
                opp_val = getattr(value, "ulmDsl2_Entity25", None)
                setattr(value, "ulmDsl2_Entity25", self)

class ulmDsl2_AttributeFeatureType:

    pass
class ulmDsl2_AttributeType:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ulmDsl2_EObject:

    pass
class ulmDsl2_FeatureType:

    pass
class ulmDsl2_Feature:

    def __init__(self, mandatory: bool, identifier: bool, name: str, ulmDsl2_Feature: "ulmDsl2_Entity" = None, ulmDsl2_Feature15: "ulmDsl2_FeatureType" = None):
        self.mandatory = mandatory
        self.identifier = identifier
        self.name = name
        self.ulmDsl2_Feature = ulmDsl2_Feature
        self.ulmDsl2_Feature15 = ulmDsl2_Feature15
        
    @property
    def identifier(self) -> bool:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: bool):
        self.__identifier = identifier

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ulmDsl2_Feature(self):
        return self.__ulmDsl2_Feature

    @ulmDsl2_Feature.setter
    def ulmDsl2_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Feature__ulmDsl2_Feature", None)
        self.__ulmDsl2_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Entity13"):
                opp_val = getattr(old_value, "ulmDsl2_Entity13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Entity13"):
                opp_val = getattr(value, "ulmDsl2_Entity13", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_Entity13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ulmDsl2_Feature15(self):
        return self.__ulmDsl2_Feature15

    @ulmDsl2_Feature15.setter
    def ulmDsl2_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Feature__ulmDsl2_Feature15", None)
        self.__ulmDsl2_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_FeatureType"):
                opp_val = getattr(old_value, "ulmDsl2_FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_FeatureType"):
                opp_val = getattr(value, "ulmDsl2_FeatureType", None)
                setattr(value, "ulmDsl2_FeatureType", self)

class ulmDsl2_AttributeDecimalType:

    def __init__(self, name: str, array: bool, scale: int, precision: int):
        self.name = name
        self.array = array
        self.scale = scale
        self.precision = precision
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

class ulmDsl2_AttributeStringType:

    def __init__(self, name: str, array: bool, length: int):
        self.name = name
        self.array = array
        self.length = length
        
    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class ulmDsl2_Entity:

    def __init__(self, type: str, name: str, desc: str, ulmDsl2_Entity: "ulmDsl2_Context" = None, ulmDsl2_Entity11: "ulmDsl2_Entity" = None, ulmDsl2_Entity9: "ulmDsl2_Entity" = None, ulmDsl2_Entity13: set["ulmDsl2_Feature"] = None, ulmDsl2_Entity25: "ulmDsl2_EntityFeatureType" = None):
        self.type = type
        self.name = name
        self.desc = desc
        self.ulmDsl2_Entity = ulmDsl2_Entity
        self.ulmDsl2_Entity11 = ulmDsl2_Entity11
        self.ulmDsl2_Entity9 = ulmDsl2_Entity9
        self.ulmDsl2_Entity13 = ulmDsl2_Entity13 if ulmDsl2_Entity13 is not None else set()
        self.ulmDsl2_Entity25 = ulmDsl2_Entity25
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

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
    def ulmDsl2_Entity11(self):
        return self.__ulmDsl2_Entity11

    @ulmDsl2_Entity11.setter
    def ulmDsl2_Entity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Entity__ulmDsl2_Entity11", None)
        self.__ulmDsl2_Entity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Entity9"):
                opp_val = getattr(old_value, "ulmDsl2_Entity9", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_Entity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Entity9"):
                opp_val = getattr(value, "ulmDsl2_Entity9", None)
                setattr(value, "ulmDsl2_Entity9", self)

    @property
    def ulmDsl2_Entity25(self):
        return self.__ulmDsl2_Entity25

    @ulmDsl2_Entity25.setter
    def ulmDsl2_Entity25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Entity__ulmDsl2_Entity25", None)
        self.__ulmDsl2_Entity25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_EntityFeatureType"):
                opp_val = getattr(old_value, "ulmDsl2_EntityFeatureType", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_EntityFeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_EntityFeatureType"):
                opp_val = getattr(value, "ulmDsl2_EntityFeatureType", None)
                setattr(value, "ulmDsl2_EntityFeatureType", self)

    @property
    def ulmDsl2_Entity(self):
        return self.__ulmDsl2_Entity

    @ulmDsl2_Entity.setter
    def ulmDsl2_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Entity__ulmDsl2_Entity", None)
        self.__ulmDsl2_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Context6"):
                opp_val = getattr(old_value, "ulmDsl2_Context6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Context6"):
                opp_val = getattr(value, "ulmDsl2_Context6", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_Context6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ulmDsl2_Entity9(self):
        return self.__ulmDsl2_Entity9

    @ulmDsl2_Entity9.setter
    def ulmDsl2_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Entity__ulmDsl2_Entity9", None)
        self.__ulmDsl2_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Entity11"):
                opp_val = getattr(old_value, "ulmDsl2_Entity11", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_Entity11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Entity11"):
                opp_val = getattr(value, "ulmDsl2_Entity11", None)
                setattr(value, "ulmDsl2_Entity11", self)

    @property
    def ulmDsl2_Entity13(self):
        return self.__ulmDsl2_Entity13

    @ulmDsl2_Entity13.setter
    def ulmDsl2_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Entity__ulmDsl2_Entity13", None)
        self.__ulmDsl2_Entity13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_Feature"):
                    opp_val = getattr(item, "ulmDsl2_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_Feature"):
                    opp_val = getattr(item, "ulmDsl2_Feature", None)
                    
                    setattr(item, "ulmDsl2_Feature", self)
                    

class ulmDsl2_Lookup:

    def __init__(self, name: str, ulmDsl2_Lookup: "ulmDsl2_Context" = None, ulmDsl2_Lookup23: "ulmDsl2_AttributeFeatureType" = None, ulmDsl2_Lookup27: "ulmDsl2_EObject" = None):
        self.name = name
        self.ulmDsl2_Lookup = ulmDsl2_Lookup
        self.ulmDsl2_Lookup23 = ulmDsl2_Lookup23
        self.ulmDsl2_Lookup27 = ulmDsl2_Lookup27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ulmDsl2_Lookup23(self):
        return self.__ulmDsl2_Lookup23

    @ulmDsl2_Lookup23.setter
    def ulmDsl2_Lookup23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Lookup__ulmDsl2_Lookup23", None)
        self.__ulmDsl2_Lookup23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_AttributeFeatureType22"):
                opp_val = getattr(old_value, "ulmDsl2_AttributeFeatureType22", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_AttributeFeatureType22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_AttributeFeatureType22"):
                opp_val = getattr(value, "ulmDsl2_AttributeFeatureType22", None)
                setattr(value, "ulmDsl2_AttributeFeatureType22", self)

    @property
    def ulmDsl2_Lookup27(self):
        return self.__ulmDsl2_Lookup27

    @ulmDsl2_Lookup27.setter
    def ulmDsl2_Lookup27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Lookup__ulmDsl2_Lookup27", None)
        self.__ulmDsl2_Lookup27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_EObject28"):
                opp_val = getattr(old_value, "ulmDsl2_EObject28", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_EObject28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_EObject28"):
                opp_val = getattr(value, "ulmDsl2_EObject28", None)
                setattr(value, "ulmDsl2_EObject28", self)

    @property
    def ulmDsl2_Lookup(self):
        return self.__ulmDsl2_Lookup

    @ulmDsl2_Lookup.setter
    def ulmDsl2_Lookup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Lookup__ulmDsl2_Lookup", None)
        self.__ulmDsl2_Lookup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Context4"):
                opp_val = getattr(old_value, "ulmDsl2_Context4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Context4"):
                opp_val = getattr(value, "ulmDsl2_Context4", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_Context4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ulmDsl2_Attribute:

    def __init__(self, name: str, desc: str, ulmDsl2_Attribute: "ulmDsl2_Context" = None, ulmDsl2_Attribute8: "ulmDsl2_EObject" = None, ulmDsl2_Attribute20: "ulmDsl2_AttributeFeatureType" = None):
        self.name = name
        self.desc = desc
        self.ulmDsl2_Attribute = ulmDsl2_Attribute
        self.ulmDsl2_Attribute8 = ulmDsl2_Attribute8
        self.ulmDsl2_Attribute20 = ulmDsl2_Attribute20
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ulmDsl2_Attribute20(self):
        return self.__ulmDsl2_Attribute20

    @ulmDsl2_Attribute20.setter
    def ulmDsl2_Attribute20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Attribute__ulmDsl2_Attribute20", None)
        self.__ulmDsl2_Attribute20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_AttributeFeatureType"):
                opp_val = getattr(old_value, "ulmDsl2_AttributeFeatureType", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_AttributeFeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_AttributeFeatureType"):
                opp_val = getattr(value, "ulmDsl2_AttributeFeatureType", None)
                setattr(value, "ulmDsl2_AttributeFeatureType", self)

    @property
    def ulmDsl2_Attribute8(self):
        return self.__ulmDsl2_Attribute8

    @ulmDsl2_Attribute8.setter
    def ulmDsl2_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Attribute__ulmDsl2_Attribute8", None)
        self.__ulmDsl2_Attribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_EObject"):
                opp_val = getattr(old_value, "ulmDsl2_EObject", None)
                if opp_val == self:
                    setattr(old_value, "ulmDsl2_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_EObject"):
                opp_val = getattr(value, "ulmDsl2_EObject", None)
                setattr(value, "ulmDsl2_EObject", self)

    @property
    def ulmDsl2_Attribute(self):
        return self.__ulmDsl2_Attribute

    @ulmDsl2_Attribute.setter
    def ulmDsl2_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Attribute__ulmDsl2_Attribute", None)
        self.__ulmDsl2_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Context2"):
                opp_val = getattr(old_value, "ulmDsl2_Context2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Context2"):
                opp_val = getattr(value, "ulmDsl2_Context2", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_Context2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ulmDsl2_Context:

    def __init__(self, name: str, version: str, ulmDsl2_Context: "ulmDsl2_Model" = None, ulmDsl2_Context2: set["ulmDsl2_Attribute"] = None, ulmDsl2_Context4: set["ulmDsl2_Lookup"] = None, ulmDsl2_Context6: set["ulmDsl2_Entity"] = None):
        self.name = name
        self.version = version
        self.ulmDsl2_Context = ulmDsl2_Context
        self.ulmDsl2_Context2 = ulmDsl2_Context2 if ulmDsl2_Context2 is not None else set()
        self.ulmDsl2_Context4 = ulmDsl2_Context4 if ulmDsl2_Context4 is not None else set()
        self.ulmDsl2_Context6 = ulmDsl2_Context6 if ulmDsl2_Context6 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ulmDsl2_Context2(self):
        return self.__ulmDsl2_Context2

    @ulmDsl2_Context2.setter
    def ulmDsl2_Context2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Context__ulmDsl2_Context2", None)
        self.__ulmDsl2_Context2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_Attribute"):
                    opp_val = getattr(item, "ulmDsl2_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_Attribute"):
                    opp_val = getattr(item, "ulmDsl2_Attribute", None)
                    
                    setattr(item, "ulmDsl2_Attribute", self)
                    

    @property
    def ulmDsl2_Context4(self):
        return self.__ulmDsl2_Context4

    @ulmDsl2_Context4.setter
    def ulmDsl2_Context4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Context__ulmDsl2_Context4", None)
        self.__ulmDsl2_Context4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_Lookup"):
                    opp_val = getattr(item, "ulmDsl2_Lookup", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_Lookup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_Lookup"):
                    opp_val = getattr(item, "ulmDsl2_Lookup", None)
                    
                    setattr(item, "ulmDsl2_Lookup", self)
                    

    @property
    def ulmDsl2_Context6(self):
        return self.__ulmDsl2_Context6

    @ulmDsl2_Context6.setter
    def ulmDsl2_Context6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Context__ulmDsl2_Context6", None)
        self.__ulmDsl2_Context6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_Entity"):
                    opp_val = getattr(item, "ulmDsl2_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_Entity"):
                    opp_val = getattr(item, "ulmDsl2_Entity", None)
                    
                    setattr(item, "ulmDsl2_Entity", self)
                    

    @property
    def ulmDsl2_Context(self):
        return self.__ulmDsl2_Context

    @ulmDsl2_Context.setter
    def ulmDsl2_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Context__ulmDsl2_Context", None)
        self.__ulmDsl2_Context = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ulmDsl2_Model"):
                opp_val = getattr(old_value, "ulmDsl2_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ulmDsl2_Model"):
                opp_val = getattr(value, "ulmDsl2_Model", None)
                if opp_val is None:
                    setattr(value, "ulmDsl2_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ulmDsl2_Model:

    def __init__(self, name: str, ulmDsl2_Model: set["ulmDsl2_Context"] = None):
        self.name = name
        self.ulmDsl2_Model = ulmDsl2_Model if ulmDsl2_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ulmDsl2_Model(self):
        return self.__ulmDsl2_Model

    @ulmDsl2_Model.setter
    def ulmDsl2_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ulmDsl2_Model__ulmDsl2_Model", None)
        self.__ulmDsl2_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ulmDsl2_Context"):
                    opp_val = getattr(item, "ulmDsl2_Context", None)
                    
                    if opp_val == self:
                        setattr(item, "ulmDsl2_Context", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ulmDsl2_Context"):
                    opp_val = getattr(item, "ulmDsl2_Context", None)
                    
                    setattr(item, "ulmDsl2_Context", self)
                    
