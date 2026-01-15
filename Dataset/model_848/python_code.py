from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NumericTypeEnum(Enum):
    Byte = "Byte"
    Double = "Double"
    Float = "Float"
    Integer = "Integer"
    Long = "Long"
    Short = "Short"
    BigDecimal = "BigDecimal"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class occi_RecordField(Attribute):

    pass
class DataType:

    pass
class occi_ArrayType(DataType):

    pass
class occi_EnumerationType(DataType):

    pass
class occi_RecordType(DataType):

    pass
class occi_BasicType(DataType):

    pass
class occi_Extension:

    def __init__(self, name: str, scheme: str, description: str, specification: str, occi_Extension: "occi_Extension" = None, occi_Extension63: set["occi_Extension"] = None, occi_Extension66: set["occi_Kind"] = None, occi_Extension69: set["occi_Mixin"] = None, occi_Extension72: set["occi_DataType"] = None, occi_Extension75: "occi_Configuration" = None):
        self.name = name
        self.scheme = scheme
        self.description = description
        self.specification = specification
        self.occi_Extension = occi_Extension
        self.occi_Extension63 = occi_Extension63 if occi_Extension63 is not None else set()
        self.occi_Extension66 = occi_Extension66 if occi_Extension66 is not None else set()
        self.occi_Extension69 = occi_Extension69 if occi_Extension69 is not None else set()
        self.occi_Extension72 = occi_Extension72 if occi_Extension72 is not None else set()
        self.occi_Extension75 = occi_Extension75
        
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
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def occi_Extension66(self):
        return self.__occi_Extension66

    @occi_Extension66.setter
    def occi_Extension66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension66", None)
        self.__occi_Extension66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Kind67"):
                    opp_val = getattr(item, "occi_Kind67", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Kind67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Kind67"):
                    opp_val = getattr(item, "occi_Kind67", None)
                    
                    setattr(item, "occi_Kind67", self)
                    

    @property
    def occi_Extension(self):
        return self.__occi_Extension

    @occi_Extension.setter
    def occi_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension", None)
        self.__occi_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Extension63"):
                opp_val = getattr(old_value, "occi_Extension63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Extension63"):
                opp_val = getattr(value, "occi_Extension63", None)
                if opp_val is None:
                    setattr(value, "occi_Extension63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Extension72(self):
        return self.__occi_Extension72

    @occi_Extension72.setter
    def occi_Extension72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension72", None)
        self.__occi_Extension72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_DataType73"):
                    opp_val = getattr(item, "occi_DataType73", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_DataType73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_DataType73"):
                    opp_val = getattr(item, "occi_DataType73", None)
                    
                    setattr(item, "occi_DataType73", self)
                    

    @property
    def occi_Extension69(self):
        return self.__occi_Extension69

    @occi_Extension69.setter
    def occi_Extension69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension69", None)
        self.__occi_Extension69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Mixin70"):
                    opp_val = getattr(item, "occi_Mixin70", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Mixin70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Mixin70"):
                    opp_val = getattr(item, "occi_Mixin70", None)
                    
                    setattr(item, "occi_Mixin70", self)
                    

    @property
    def occi_Extension75(self):
        return self.__occi_Extension75

    @occi_Extension75.setter
    def occi_Extension75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension75", None)
        self.__occi_Extension75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Configuration"):
                opp_val = getattr(old_value, "occi_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Configuration"):
                opp_val = getattr(value, "occi_Configuration", None)
                if opp_val is None:
                    setattr(value, "occi_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Extension63(self):
        return self.__occi_Extension63

    @occi_Extension63.setter
    def occi_Extension63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Extension__occi_Extension63", None)
        self.__occi_Extension63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Extension"):
                    opp_val = getattr(item, "occi_Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Extension"):
                    opp_val = getattr(item, "occi_Extension", None)
                    
                    setattr(item, "occi_Extension", self)
                    

class occi_Configuration:

    def __init__(self, description: str, location: str, occi_Configuration: set["occi_Extension"] = None, occi_Configuration77: set["occi_Resource"] = None, occi_Configuration79: set["occi_Mixin"] = None):
        self.description = description
        self.location = location
        self.occi_Configuration = occi_Configuration if occi_Configuration is not None else set()
        self.occi_Configuration77 = occi_Configuration77 if occi_Configuration77 is not None else set()
        self.occi_Configuration79 = occi_Configuration79 if occi_Configuration79 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def occi_Configuration79(self):
        return self.__occi_Configuration79

    @occi_Configuration79.setter
    def occi_Configuration79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Configuration__occi_Configuration79", None)
        self.__occi_Configuration79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Mixin80"):
                    opp_val = getattr(item, "occi_Mixin80", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Mixin80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Mixin80"):
                    opp_val = getattr(item, "occi_Mixin80", None)
                    
                    setattr(item, "occi_Mixin80", self)
                    

    @property
    def occi_Configuration77(self):
        return self.__occi_Configuration77

    @occi_Configuration77.setter
    def occi_Configuration77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Configuration__occi_Configuration77", None)
        self.__occi_Configuration77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Resource"):
                    opp_val = getattr(item, "occi_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Resource"):
                    opp_val = getattr(item, "occi_Resource", None)
                    
                    setattr(item, "occi_Resource", self)
                    

    @property
    def occi_Configuration(self):
        return self.__occi_Configuration

    @occi_Configuration.setter
    def occi_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Configuration__occi_Configuration", None)
        self.__occi_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Extension75"):
                    opp_val = getattr(item, "occi_Extension75", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Extension75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Extension75"):
                    opp_val = getattr(item, "occi_Extension75", None)
                    
                    setattr(item, "occi_Extension75", self)
                    

class BasicType:

    pass
class occi_EObjectType(BasicType):

    def __init__(self, instanceClassName: str):
        self.instanceClassName = instanceClassName
        
    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

class occi_BooleanType(BasicType):

    pass
class occi_NumericType(BasicType):

    def __init__(self, type: str, totalDigits: str, minExclusive: str, maxExclusive: str, minInclusive: str, maxInclusive: str):
        self.type = type
        self.totalDigits = totalDigits
        self.minExclusive = minExclusive
        self.maxExclusive = maxExclusive
        self.minInclusive = minInclusive
        self.maxInclusive = maxInclusive
        
    @property
    def maxExclusive(self) -> str:
        return self.__maxExclusive

    @maxExclusive.setter
    def maxExclusive(self, maxExclusive: str):
        self.__maxExclusive = maxExclusive

    @property
    def minExclusive(self) -> str:
        return self.__minExclusive

    @minExclusive.setter
    def minExclusive(self, minExclusive: str):
        self.__minExclusive = minExclusive

    @property
    def maxInclusive(self) -> str:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: str):
        self.__maxInclusive = maxInclusive

    @property
    def totalDigits(self) -> str:
        return self.__totalDigits

    @totalDigits.setter
    def totalDigits(self, totalDigits: str):
        self.__totalDigits = totalDigits

    @property
    def minInclusive(self) -> str:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: str):
        self.__minInclusive = minInclusive

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class occi_StringType(BasicType):

    def __init__(self, pattern: str, length: str, minLength: str, maxLength: str):
        self.pattern = pattern
        self.length = length
        self.minLength = minLength
        self.maxLength = maxLength
        
    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

    @property
    def minLength(self) -> str:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: str):
        self.__minLength = minLength

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class occi_MixinBase:

    pass
class occi_AttributeState:

    def __init__(self, name: str, value: str, occi_AttributeState55: "occi_MixinBase" = None, occi_AttributeState: "occi_Entity" = None):
        self.name = name
        self.value = value
        self.occi_AttributeState55 = occi_AttributeState55
        self.occi_AttributeState = occi_AttributeState
        
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
    def occi_AttributeState55(self):
        return self.__occi_AttributeState55

    @occi_AttributeState55.setter
    def occi_AttributeState55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_AttributeState__occi_AttributeState55", None)
        self.__occi_AttributeState55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_MixinBase54"):
                opp_val = getattr(old_value, "occi_MixinBase54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_MixinBase54"):
                opp_val = getattr(value, "occi_MixinBase54", None)
                if opp_val is None:
                    setattr(value, "occi_MixinBase54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_AttributeState(self):
        return self.__occi_AttributeState

    @occi_AttributeState.setter
    def occi_AttributeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_AttributeState__occi_AttributeState", None)
        self.__occi_AttributeState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Entity45"):
                opp_val = getattr(old_value, "occi_Entity45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Entity45"):
                opp_val = getattr(value, "occi_Entity45", None)
                if opp_val is None:
                    setattr(value, "occi_Entity45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entity:

    pass
class occi_Link(Entity):

    def __init__(self, Link: "occi_Resource" = None, Link59: "occi_Resource" = None, links: "occi_Resource" = None, rlinks: "occi_Resource" = None):
        self.Link = Link
        self.Link59 = Link59
        self.links = links
        self.rlinks = rlinks
        
    @property
    def rlinks(self):
        return self.__rlinks

    @rlinks.setter
    def rlinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Link__rlinks", None)
        self.__rlinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Resource62"):
                opp_val = getattr(old_value, "Resource62", None)
                if opp_val == self:
                    setattr(old_value, "Resource62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Resource62"):
                opp_val = getattr(value, "Resource62", None)
                setattr(value, "Resource62", self)

    @property
    def Link59(self):
        return self.__Link59

    @Link59.setter
    def Link59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Link__Link59", None)
        self.__Link59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Link(self):
        return self.__Link

    @Link.setter
    def Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Link__Link", None)
        self.__Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source57"):
                opp_val = getattr(old_value, "source57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source57"):
                opp_val = getattr(value, "source57", None)
                if opp_val is None:
                    setattr(value, "source57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def links(self):
        return self.__links

    @links.setter
    def links(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Link__links", None)
        self.__links = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Resource"):
                opp_val = getattr(old_value, "Resource", None)
                if opp_val == self:
                    setattr(old_value, "Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Resource"):
                opp_val = getattr(value, "Resource", None)
                setattr(value, "Resource", self)

    def LinkSourceInvariant(self, linkInstanceKind: str, resourcekind: str) -> str:
        # TODO: Implement LinkSourceInvariant method
        pass

    def LinkTargetInvariant(self, resourcekind: str, linkInstanceKind: str) -> str:
        # TODO: Implement LinkTargetInvariant method
        pass

class occi_Resource(Entity):

    def __init__(self, summary: str, source57: set["occi_Link"] = None, target: set["occi_Link"] = None, Resource: "occi_Link" = None, Resource62: "occi_Link" = None, occi_Resource: "occi_Configuration" = None):
        self.summary = summary
        self.source57 = source57 if source57 is not None else set()
        self.target = target if target is not None else set()
        self.Resource = Resource
        self.Resource62 = Resource62
        self.occi_Resource = occi_Resource
        
    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Resource__Resource", None)
        self.__Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links"):
                opp_val = getattr(old_value, "links", None)
                if opp_val == self:
                    setattr(old_value, "links", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links"):
                opp_val = getattr(value, "links", None)
                setattr(value, "links", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Resource__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link59"):
                    opp_val = getattr(item, "Link59", None)
                    
                    if opp_val == self:
                        setattr(item, "Link59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link59"):
                    opp_val = getattr(item, "Link59", None)
                    
                    setattr(item, "Link59", self)
                    

    @property
    def Resource62(self):
        return self.__Resource62

    @Resource62.setter
    def Resource62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Resource__Resource62", None)
        self.__Resource62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rlinks"):
                opp_val = getattr(old_value, "rlinks", None)
                if opp_val == self:
                    setattr(old_value, "rlinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rlinks"):
                opp_val = getattr(value, "rlinks", None)
                setattr(value, "rlinks", self)

    @property
    def occi_Resource(self):
        return self.__occi_Resource

    @occi_Resource.setter
    def occi_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Resource__occi_Resource", None)
        self.__occi_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Configuration77"):
                opp_val = getattr(old_value, "occi_Configuration77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Configuration77"):
                opp_val = getattr(value, "occi_Configuration77", None)
                if opp_val is None:
                    setattr(value, "occi_Configuration77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source57(self):
        return self.__source57

    @source57.setter
    def source57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Resource__source57", None)
        self.__source57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

class occi_Entity(ABC):

    def __init__(self, id: str, title: str, location: str, occi_Entity: "occi_Kind" = None, Entity: "occi_MixinBase" = None, occi_Entity40: "occi_Mixin" = None, occi_Entity42: "occi_Kind" = None, occi_Entity45: set["occi_AttributeState"] = None, occi_Entity47: set["occi_Mixin"] = None, entity: set["occi_MixinBase"] = None):
        self.id = id
        self.title = title
        self.location = location
        self.occi_Entity = occi_Entity
        self.Entity = Entity
        self.occi_Entity40 = occi_Entity40
        self.occi_Entity42 = occi_Entity42
        self.occi_Entity45 = occi_Entity45 if occi_Entity45 is not None else set()
        self.occi_Entity47 = occi_Entity47 if occi_Entity47 is not None else set()
        self.entity = entity if entity is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def occi_Entity40(self):
        return self.__occi_Entity40

    @occi_Entity40.setter
    def occi_Entity40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__occi_Entity40", None)
        self.__occi_Entity40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Mixin39"):
                opp_val = getattr(old_value, "occi_Mixin39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Mixin39"):
                opp_val = getattr(value, "occi_Mixin39", None)
                if opp_val is None:
                    setattr(value, "occi_Mixin39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Entity47(self):
        return self.__occi_Entity47

    @occi_Entity47.setter
    def occi_Entity47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__occi_Entity47", None)
        self.__occi_Entity47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Mixin48"):
                    opp_val = getattr(item, "occi_Mixin48", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Mixin48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Mixin48"):
                    opp_val = getattr(item, "occi_Mixin48", None)
                    
                    setattr(item, "occi_Mixin48", self)
                    

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__entity", None)
        self.__entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MixinBase"):
                    opp_val = getattr(item, "MixinBase", None)
                    
                    if opp_val == self:
                        setattr(item, "MixinBase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MixinBase"):
                    opp_val = getattr(item, "MixinBase", None)
                    
                    setattr(item, "MixinBase", self)
                    

    @property
    def occi_Entity42(self):
        return self.__occi_Entity42

    @occi_Entity42.setter
    def occi_Entity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__occi_Entity42", None)
        self.__occi_Entity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind43"):
                opp_val = getattr(old_value, "occi_Kind43", None)
                if opp_val == self:
                    setattr(old_value, "occi_Kind43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind43"):
                opp_val = getattr(value, "occi_Kind43", None)
                setattr(value, "occi_Kind43", self)

    @property
    def occi_Entity45(self):
        return self.__occi_Entity45

    @occi_Entity45.setter
    def occi_Entity45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__occi_Entity45", None)
        self.__occi_Entity45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_AttributeState"):
                    opp_val = getattr(item, "occi_AttributeState", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_AttributeState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_AttributeState"):
                    opp_val = getattr(item, "occi_AttributeState", None)
                    
                    setattr(item, "occi_AttributeState", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parts"):
                opp_val = getattr(old_value, "parts", None)
                if opp_val == self:
                    setattr(old_value, "parts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parts"):
                opp_val = getattr(value, "parts", None)
                setattr(value, "parts", self)

    @property
    def occi_Entity(self):
        return self.__occi_Entity

    @occi_Entity.setter
    def occi_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Entity__occi_Entity", None)
        self.__occi_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind26"):
                opp_val = getattr(old_value, "occi_Kind26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind26"):
                opp_val = getattr(value, "occi_Kind26", None)
                if opp_val is None:
                    setattr(value, "occi_Kind26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def occiUpdate(self):
        # TODO: Implement occiUpdate method
        pass

    def occiCreate(self):
        # TODO: Implement occiCreate method
        pass

    def occiDelete(self):
        # TODO: Implement occiDelete method
        pass

    def occiRetrieve(self):
        # TODO: Implement occiRetrieve method
        pass

class Type:

    pass
class occi_Kind(Type):

    def __init__(self, occi_Kind32: "occi_Kind" = None, occi_Kind30: set["occi_Kind"] = None, occi_Kind: "occi_Kind" = None, occi_Kind23: "occi_Kind" = None, occi_Kind26: set["occi_Entity"] = None, occi_Kind29: "occi_Kind" = None, occi_Kind27: set["occi_Kind"] = None, occi_Kind37: "occi_Mixin" = None, occi_Kind43: "occi_Entity" = None, occi_Kind67: "occi_Extension" = None):
        self.occi_Kind32 = occi_Kind32
        self.occi_Kind30 = occi_Kind30 if occi_Kind30 is not None else set()
        self.occi_Kind = occi_Kind
        self.occi_Kind23 = occi_Kind23
        self.occi_Kind26 = occi_Kind26 if occi_Kind26 is not None else set()
        self.occi_Kind29 = occi_Kind29
        self.occi_Kind27 = occi_Kind27 if occi_Kind27 is not None else set()
        self.occi_Kind37 = occi_Kind37
        self.occi_Kind43 = occi_Kind43
        self.occi_Kind67 = occi_Kind67
        
    @property
    def occi_Kind23(self):
        return self.__occi_Kind23

    @occi_Kind23.setter
    def occi_Kind23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind23", None)
        self.__occi_Kind23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind"):
                opp_val = getattr(old_value, "occi_Kind", None)
                if opp_val == self:
                    setattr(old_value, "occi_Kind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind"):
                opp_val = getattr(value, "occi_Kind", None)
                setattr(value, "occi_Kind", self)

    @property
    def occi_Kind29(self):
        return self.__occi_Kind29

    @occi_Kind29.setter
    def occi_Kind29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind29", None)
        self.__occi_Kind29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind27"):
                opp_val = getattr(old_value, "occi_Kind27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind27"):
                opp_val = getattr(value, "occi_Kind27", None)
                if opp_val is None:
                    setattr(value, "occi_Kind27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Kind26(self):
        return self.__occi_Kind26

    @occi_Kind26.setter
    def occi_Kind26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind26", None)
        self.__occi_Kind26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Entity"):
                    opp_val = getattr(item, "occi_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Entity"):
                    opp_val = getattr(item, "occi_Entity", None)
                    
                    setattr(item, "occi_Entity", self)
                    

    @property
    def occi_Kind43(self):
        return self.__occi_Kind43

    @occi_Kind43.setter
    def occi_Kind43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind43", None)
        self.__occi_Kind43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Entity42"):
                opp_val = getattr(old_value, "occi_Entity42", None)
                if opp_val == self:
                    setattr(old_value, "occi_Entity42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Entity42"):
                opp_val = getattr(value, "occi_Entity42", None)
                setattr(value, "occi_Entity42", self)

    @property
    def occi_Kind67(self):
        return self.__occi_Kind67

    @occi_Kind67.setter
    def occi_Kind67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind67", None)
        self.__occi_Kind67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Extension66"):
                opp_val = getattr(old_value, "occi_Extension66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Extension66"):
                opp_val = getattr(value, "occi_Extension66", None)
                if opp_val is None:
                    setattr(value, "occi_Extension66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Kind37(self):
        return self.__occi_Kind37

    @occi_Kind37.setter
    def occi_Kind37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind37", None)
        self.__occi_Kind37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Mixin36"):
                opp_val = getattr(old_value, "occi_Mixin36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Mixin36"):
                opp_val = getattr(value, "occi_Mixin36", None)
                if opp_val is None:
                    setattr(value, "occi_Mixin36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Kind27(self):
        return self.__occi_Kind27

    @occi_Kind27.setter
    def occi_Kind27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind27", None)
        self.__occi_Kind27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Kind29"):
                    opp_val = getattr(item, "occi_Kind29", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Kind29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Kind29"):
                    opp_val = getattr(item, "occi_Kind29", None)
                    
                    setattr(item, "occi_Kind29", self)
                    

    @property
    def occi_Kind32(self):
        return self.__occi_Kind32

    @occi_Kind32.setter
    def occi_Kind32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind32", None)
        self.__occi_Kind32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind30"):
                opp_val = getattr(old_value, "occi_Kind30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind30"):
                opp_val = getattr(value, "occi_Kind30", None)
                if opp_val is None:
                    setattr(value, "occi_Kind30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Kind30(self):
        return self.__occi_Kind30

    @occi_Kind30.setter
    def occi_Kind30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind30", None)
        self.__occi_Kind30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Kind32"):
                    opp_val = getattr(item, "occi_Kind32", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Kind32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Kind32"):
                    opp_val = getattr(item, "occi_Kind32", None)
                    
                    setattr(item, "occi_Kind32", self)
                    

    @property
    def occi_Kind(self):
        return self.__occi_Kind

    @occi_Kind.setter
    def occi_Kind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Kind__occi_Kind", None)
        self.__occi_Kind = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Kind23"):
                opp_val = getattr(old_value, "occi_Kind23", None)
                if opp_val == self:
                    setattr(old_value, "occi_Kind23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Kind23"):
                opp_val = getattr(value, "occi_Kind23", None)
                setattr(value, "occi_Kind23", self)

    def occiIsKindOf(self, kind: str) -> str:
        # TODO: Implement occiIsKindOf method
        pass

class occi_DataType(ABC):

    def __init__(self, name: str, documentation: str, occi_DataType: "occi_Attribute" = None, occi_DataType73: "occi_Extension" = None, occi_DataType85: "occi_ArrayType" = None):
        self.name = name
        self.documentation = documentation
        self.occi_DataType = occi_DataType
        self.occi_DataType73 = occi_DataType73
        self.occi_DataType85 = occi_DataType85
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def occi_DataType73(self):
        return self.__occi_DataType73

    @occi_DataType73.setter
    def occi_DataType73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_DataType__occi_DataType73", None)
        self.__occi_DataType73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Extension72"):
                opp_val = getattr(old_value, "occi_Extension72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Extension72"):
                opp_val = getattr(value, "occi_Extension72", None)
                if opp_val is None:
                    setattr(value, "occi_Extension72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_DataType(self):
        return self.__occi_DataType

    @occi_DataType.setter
    def occi_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_DataType__occi_DataType", None)
        self.__occi_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Attribute22"):
                opp_val = getattr(old_value, "occi_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "occi_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Attribute22"):
                opp_val = getattr(value, "occi_Attribute22", None)
                setattr(value, "occi_Attribute22", self)

    @property
    def occi_DataType85(self):
        return self.__occi_DataType85

    @occi_DataType85.setter
    def occi_DataType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_DataType__occi_DataType85", None)
        self.__occi_DataType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_ArrayType"):
                opp_val = getattr(old_value, "occi_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "occi_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_ArrayType"):
                opp_val = getattr(value, "occi_ArrayType", None)
                setattr(value, "occi_ArrayType", self)

class occi_Mixin(Type):

    pass
class occi_Transition:

    pass
class occi_EnumerationLiteral:

    def __init__(self, name: str, documentation: str, occi_EnumerationLiteral: "occi_State" = None, EnumerationLiteral: "occi_EnumerationType" = None, literals: "occi_EnumerationType" = None):
        self.name = name
        self.documentation = documentation
        self.occi_EnumerationLiteral = occi_EnumerationLiteral
        self.EnumerationLiteral = EnumerationLiteral
        self.literals = literals
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def occi_EnumerationLiteral(self):
        return self.__occi_EnumerationLiteral

    @occi_EnumerationLiteral.setter
    def occi_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_EnumerationLiteral__occi_EnumerationLiteral", None)
        self.__occi_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_State"):
                opp_val = getattr(old_value, "occi_State", None)
                if opp_val == self:
                    setattr(old_value, "occi_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_State"):
                opp_val = getattr(value, "occi_State", None)
                setattr(value, "occi_State", self)

    @property
    def literals(self):
        return self.__literals

    @literals.setter
    def literals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_EnumerationLiteral__literals", None)
        self.__literals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationType"):
                opp_val = getattr(old_value, "EnumerationType", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationType"):
                opp_val = getattr(value, "EnumerationType", None)
                setattr(value, "EnumerationType", self)

    @property
    def EnumerationLiteral(self):
        return self.__EnumerationLiteral

    @EnumerationLiteral.setter
    def EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_EnumerationLiteral__EnumerationLiteral", None)
        self.__EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enumerationType"):
                opp_val = getattr(old_value, "enumerationType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enumerationType"):
                opp_val = getattr(value, "enumerationType", None)
                if opp_val is None:
                    setattr(value, "enumerationType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class occi_State:

    def __init__(self, initial: str, final: str, State15: "occi_Transition" = None, occi_State17: "occi_Transition" = None, State: "occi_FSM" = None, occi_State: "occi_EnumerationLiteral" = None, ownedState: "occi_FSM" = None, source: set["occi_Transition"] = None):
        self.initial = initial
        self.final = final
        self.State15 = State15
        self.occi_State17 = occi_State17
        self.State = State
        self.occi_State = occi_State
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        
    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def occi_State17(self):
        return self.__occi_State17

    @occi_State17.setter
    def occi_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__occi_State17", None)
        self.__occi_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Transition"):
                opp_val = getattr(old_value, "occi_Transition", None)
                if opp_val == self:
                    setattr(old_value, "occi_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Transition"):
                opp_val = getattr(value, "occi_Transition", None)
                setattr(value, "occi_Transition", self)

    @property
    def occi_State(self):
        return self.__occi_State

    @occi_State.setter
    def occi_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__occi_State", None)
        self.__occi_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_EnumerationLiteral"):
                opp_val = getattr(old_value, "occi_EnumerationLiteral", None)
                if opp_val == self:
                    setattr(old_value, "occi_EnumerationLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_EnumerationLiteral"):
                opp_val = getattr(value, "occi_EnumerationLiteral", None)
                setattr(value, "occi_EnumerationLiteral", self)

    @property
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__State15", None)
        self.__State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransition"):
                opp_val = getattr(old_value, "outgoingTransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransition"):
                opp_val = getattr(value, "outgoingTransition", None)
                setattr(value, "outgoingTransition", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

class occi_FSM:

    pass
class occi_Constraint:

    def __init__(self, name: str, description: str, body: str, occi_Constraint: "occi_Type" = None):
        self.name = name
        self.description = description
        self.body = body
        self.occi_Constraint = occi_Constraint
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def occi_Constraint(self):
        return self.__occi_Constraint

    @occi_Constraint.setter
    def occi_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Constraint__occi_Constraint", None)
        self.__occi_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Type4"):
                opp_val = getattr(old_value, "occi_Type4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Type4"):
                opp_val = getattr(value, "occi_Type4", None)
                if opp_val is None:
                    setattr(value, "occi_Type4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AnnotatedElement:

    pass
class occi_Attribute(AnnotatedElement):

    def __init__(self, name: str, mutable: str, required: str, default: str, description: str, occi_Attribute: "occi_Category" = None, occi_Attribute10: "occi_FSM" = None, occi_Attribute22: "occi_DataType" = None):
        self.name = name
        self.mutable = mutable
        self.required = required
        self.default = default
        self.description = description
        self.occi_Attribute = occi_Attribute
        self.occi_Attribute10 = occi_Attribute10
        self.occi_Attribute22 = occi_Attribute22
        
    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def mutable(self) -> str:
        return self.__mutable

    @mutable.setter
    def mutable(self, mutable: str):
        self.__mutable = mutable

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def occi_Attribute(self):
        return self.__occi_Attribute

    @occi_Attribute.setter
    def occi_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Attribute__occi_Attribute", None)
        self.__occi_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_Category"):
                opp_val = getattr(old_value, "occi_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_Category"):
                opp_val = getattr(value, "occi_Category", None)
                if opp_val is None:
                    setattr(value, "occi_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def occi_Attribute22(self):
        return self.__occi_Attribute22

    @occi_Attribute22.setter
    def occi_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Attribute__occi_Attribute22", None)
        self.__occi_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_DataType"):
                opp_val = getattr(old_value, "occi_DataType", None)
                if opp_val == self:
                    setattr(old_value, "occi_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_DataType"):
                opp_val = getattr(value, "occi_DataType", None)
                setattr(value, "occi_DataType", self)

    @property
    def occi_Attribute10(self):
        return self.__occi_Attribute10

    @occi_Attribute10.setter
    def occi_Attribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Attribute__occi_Attribute10", None)
        self.__occi_Attribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_FSM9"):
                opp_val = getattr(old_value, "occi_FSM9", None)
                if opp_val == self:
                    setattr(old_value, "occi_FSM9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_FSM9"):
                opp_val = getattr(value, "occi_FSM9", None)
                setattr(value, "occi_FSM9", self)

class occi_Category(AnnotatedElement):

    def __init__(self, name: str, term: str, scheme: str, title: str, description: str, occi_Category: set["occi_Attribute"] = None):
        self.name = name
        self.term = term
        self.scheme = scheme
        self.title = title
        self.description = description
        self.occi_Category = occi_Category if occi_Category is not None else set()
        
    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def occi_Category(self):
        return self.__occi_Category

    @occi_Category.setter
    def occi_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Category__occi_Category", None)
        self.__occi_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "occi_Attribute"):
                    opp_val = getattr(item, "occi_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "occi_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "occi_Attribute"):
                    opp_val = getattr(item, "occi_Attribute", None)
                    
                    setattr(item, "occi_Attribute", self)
                    

class occi_Annotation:

    def __init__(self, key: str, value: str, occi_Annotation: "occi_AnnotatedElement" = None):
        self.key = key
        self.value = value
        self.occi_Annotation = occi_Annotation
        
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

    @property
    def occi_Annotation(self):
        return self.__occi_Annotation

    @occi_Annotation.setter
    def occi_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_occi_Annotation__occi_Annotation", None)
        self.__occi_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "occi_AnnotatedElement"):
                opp_val = getattr(old_value, "occi_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "occi_AnnotatedElement"):
                opp_val = getattr(value, "occi_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "occi_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class occi_AnnotatedElement(ABC):

    pass
class Category:

    pass
class occi_Action(Category):

    pass
class occi_Type(Category):

    pass