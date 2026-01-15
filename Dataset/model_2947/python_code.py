from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SWMLType(Enum):
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Email = "Email"
    Boolean = "Boolean"
    Time = "Time"
    Date = "Date"


############################################
# Definition of Classes
############################################

class swml_Literal:

    def __init__(self, name: str, swml_Literal: "swml_Enumeration" = None):
        self.name = name
        self.swml_Literal = swml_Literal
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Literal(self):
        return self.__swml_Literal

    @swml_Literal.setter
    def swml_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Literal__swml_Literal", None)
        self.__swml_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Enumeration28"):
                opp_val = getattr(old_value, "swml_Enumeration28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Enumeration28"):
                opp_val = getattr(value, "swml_Enumeration28", None)
                if opp_val is None:
                    setattr(value, "swml_Enumeration28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_Parameter:

    def __init__(self, ValueSpec: str, swml_Parameter: "swml_Link" = None):
        self.ValueSpec = ValueSpec
        self.swml_Parameter = swml_Parameter
        
    @property
    def ValueSpec(self) -> str:
        return self.__ValueSpec

    @ValueSpec.setter
    def ValueSpec(self, ValueSpec: str):
        self.__ValueSpec = ValueSpec

    @property
    def swml_Parameter(self):
        return self.__swml_Parameter

    @swml_Parameter.setter
    def swml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Parameter__swml_Parameter", None)
        self.__swml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Link16"):
                opp_val = getattr(old_value, "swml_Link16", None)
                if opp_val == self:
                    setattr(old_value, "swml_Link16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Link16"):
                opp_val = getattr(value, "swml_Link16", None)
                setattr(value, "swml_Link16", self)

class Page:

    pass
class swml_StaticPage(Page):

    pass
class EntityPage:

    pass
class swml_DeletePage(EntityPage):

    pass
class swml_CreatePage(EntityPage):

    pass
class swml_UpdatePage(EntityPage):

    pass
class swml_DynamicPage(Page):

    pass
class DynamicPage:

    pass
class swml_EntityPage(DynamicPage):

    pass
class swml_IndexPage(DynamicPage):

    pass
class Link:

    pass
class swml_OKLink(Link):

    pass
class swml_KOLink(Link):

    pass
class swml_NonContextualLink(Link):

    pass
class swml_ContextualLink(Link):

    pass
class Node:

    pass
class swml_LinkJoinNode(Page, Node):

    pass
class swml_Page(Node):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class swml_Node(ABC):

    pass
class swml_Link(ABC):

    pass
class swml_Enumeration:

    def __init__(self, name: str, swml_Enumeration: "swml_Attribute" = None, swml_Enumeration28: set["swml_Literal"] = None, swml_Enumeration31: "swml_ContentModel" = None):
        self.name = name
        self.swml_Enumeration = swml_Enumeration
        self.swml_Enumeration28 = swml_Enumeration28 if swml_Enumeration28 is not None else set()
        self.swml_Enumeration31 = swml_Enumeration31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Enumeration31(self):
        return self.__swml_Enumeration31

    @swml_Enumeration31.setter
    def swml_Enumeration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration31", None)
        self.__swml_Enumeration31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentModel30"):
                opp_val = getattr(old_value, "swml_ContentModel30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentModel30"):
                opp_val = getattr(value, "swml_ContentModel30", None)
                if opp_val is None:
                    setattr(value, "swml_ContentModel30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Enumeration28(self):
        return self.__swml_Enumeration28

    @swml_Enumeration28.setter
    def swml_Enumeration28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration28", None)
        self.__swml_Enumeration28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Literal"):
                    opp_val = getattr(item, "swml_Literal", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Literal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Literal"):
                    opp_val = getattr(item, "swml_Literal", None)
                    
                    setattr(item, "swml_Literal", self)
                    

    @property
    def swml_Enumeration(self):
        return self.__swml_Enumeration

    @swml_Enumeration.setter
    def swml_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration", None)
        self.__swml_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Attribute12"):
                opp_val = getattr(old_value, "swml_Attribute12", None)
                if opp_val == self:
                    setattr(old_value, "swml_Attribute12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Attribute12"):
                opp_val = getattr(value, "swml_Attribute12", None)
                setattr(value, "swml_Attribute12", self)

class swml_Relationship:

    def __init__(self, name: str, upper: int, lower: int, Relationship: "swml_EntityType" = None, relationship: "swml_EntityType" = None, swml_Relationship: "swml_Relationship" = None, swml_Relationship22: "swml_Relationship" = None, swml_Relationship25: "swml_EntityType" = None):
        self.name = name
        self.upper = upper
        self.lower = lower
        self.Relationship = Relationship
        self.relationship = relationship
        self.swml_Relationship = swml_Relationship
        self.swml_Relationship22 = swml_Relationship22
        self.swml_Relationship25 = swml_Relationship25
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def relationship(self):
        return self.__relationship

    @relationship.setter
    def relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__relationship", None)
        self.__relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityType"):
                opp_val = getattr(old_value, "EntityType", None)
                if opp_val == self:
                    setattr(old_value, "EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityType"):
                opp_val = getattr(value, "EntityType", None)
                setattr(value, "EntityType", self)

    @property
    def swml_Relationship22(self):
        return self.__swml_Relationship22

    @swml_Relationship22.setter
    def swml_Relationship22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__swml_Relationship22", None)
        self.__swml_Relationship22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Relationship"):
                opp_val = getattr(old_value, "swml_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "swml_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Relationship"):
                opp_val = getattr(value, "swml_Relationship", None)
                setattr(value, "swml_Relationship", self)

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityType"):
                opp_val = getattr(old_value, "entityType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityType"):
                opp_val = getattr(value, "entityType", None)
                if opp_val is None:
                    setattr(value, "entityType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Relationship(self):
        return self.__swml_Relationship

    @swml_Relationship.setter
    def swml_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__swml_Relationship", None)
        self.__swml_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Relationship22"):
                opp_val = getattr(old_value, "swml_Relationship22", None)
                if opp_val == self:
                    setattr(old_value, "swml_Relationship22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Relationship22"):
                opp_val = getattr(value, "swml_Relationship22", None)
                setattr(value, "swml_Relationship22", self)

    @property
    def swml_Relationship25(self):
        return self.__swml_Relationship25

    @swml_Relationship25.setter
    def swml_Relationship25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__swml_Relationship25", None)
        self.__swml_Relationship25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EntityType26"):
                opp_val = getattr(old_value, "swml_EntityType26", None)
                if opp_val == self:
                    setattr(old_value, "swml_EntityType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EntityType26"):
                opp_val = getattr(value, "swml_EntityType26", None)
                setattr(value, "swml_EntityType26", self)

class swml_Attribute:

    def __init__(self, name: str, type: str, swml_Attribute12: "swml_Enumeration" = None, swml_Attribute: "swml_EntityType" = None, swml_Attribute6: "swml_EntityType" = None):
        self.name = name
        self.type = type
        self.swml_Attribute12 = swml_Attribute12
        self.swml_Attribute = swml_Attribute
        self.swml_Attribute6 = swml_Attribute6
        
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
    def swml_Attribute12(self):
        return self.__swml_Attribute12

    @swml_Attribute12.setter
    def swml_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute12", None)
        self.__swml_Attribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Enumeration"):
                opp_val = getattr(old_value, "swml_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "swml_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Enumeration"):
                opp_val = getattr(value, "swml_Enumeration", None)
                setattr(value, "swml_Enumeration", self)

    @property
    def swml_Attribute6(self):
        return self.__swml_Attribute6

    @swml_Attribute6.setter
    def swml_Attribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute6", None)
        self.__swml_Attribute6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EntityType5"):
                opp_val = getattr(old_value, "swml_EntityType5", None)
                if opp_val == self:
                    setattr(old_value, "swml_EntityType5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EntityType5"):
                opp_val = getattr(value, "swml_EntityType5", None)
                setattr(value, "swml_EntityType5", self)

    @property
    def swml_Attribute(self):
        return self.__swml_Attribute

    @swml_Attribute.setter
    def swml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute", None)
        self.__swml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EntityType"):
                opp_val = getattr(old_value, "swml_EntityType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EntityType"):
                opp_val = getattr(value, "swml_EntityType", None)
                if opp_val is None:
                    setattr(value, "swml_EntityType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_EntityType:

    def __init__(self, name: str, isAbstract: bool, entityType: set["swml_Relationship"] = None, swml_EntityType10: "swml_EntityType" = None, swml_EntityType8: "swml_EntityType" = None, swml_EntityType: set["swml_Attribute"] = None, swml_EntityType5: "swml_Attribute" = None, swml_EntityType20: "swml_DynamicPage" = None, EntityType: "swml_Relationship" = None, swml_EntityType26: "swml_Relationship" = None, swml_EntityType34: "swml_ContentModel" = None):
        self.name = name
        self.isAbstract = isAbstract
        self.entityType = entityType if entityType is not None else set()
        self.swml_EntityType10 = swml_EntityType10
        self.swml_EntityType8 = swml_EntityType8
        self.swml_EntityType = swml_EntityType if swml_EntityType is not None else set()
        self.swml_EntityType5 = swml_EntityType5
        self.swml_EntityType20 = swml_EntityType20
        self.EntityType = EntityType
        self.swml_EntityType26 = swml_EntityType26
        self.swml_EntityType34 = swml_EntityType34
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_EntityType8(self):
        return self.__swml_EntityType8

    @swml_EntityType8.setter
    def swml_EntityType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType8", None)
        self.__swml_EntityType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EntityType10"):
                opp_val = getattr(old_value, "swml_EntityType10", None)
                if opp_val == self:
                    setattr(old_value, "swml_EntityType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EntityType10"):
                opp_val = getattr(value, "swml_EntityType10", None)
                setattr(value, "swml_EntityType10", self)

    @property
    def entityType(self):
        return self.__entityType

    @entityType.setter
    def entityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__entityType", None)
        self.__entityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

    @property
    def swml_EntityType(self):
        return self.__swml_EntityType

    @swml_EntityType.setter
    def swml_EntityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType", None)
        self.__swml_EntityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Attribute"):
                    opp_val = getattr(item, "swml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Attribute"):
                    opp_val = getattr(item, "swml_Attribute", None)
                    
                    setattr(item, "swml_Attribute", self)
                    

    @property
    def swml_EntityType26(self):
        return self.__swml_EntityType26

    @swml_EntityType26.setter
    def swml_EntityType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType26", None)
        self.__swml_EntityType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Relationship25"):
                opp_val = getattr(old_value, "swml_Relationship25", None)
                if opp_val == self:
                    setattr(old_value, "swml_Relationship25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Relationship25"):
                opp_val = getattr(value, "swml_Relationship25", None)
                setattr(value, "swml_Relationship25", self)

    @property
    def swml_EntityType10(self):
        return self.__swml_EntityType10

    @swml_EntityType10.setter
    def swml_EntityType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType10", None)
        self.__swml_EntityType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EntityType8"):
                opp_val = getattr(old_value, "swml_EntityType8", None)
                if opp_val == self:
                    setattr(old_value, "swml_EntityType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EntityType8"):
                opp_val = getattr(value, "swml_EntityType8", None)
                setattr(value, "swml_EntityType8", self)

    @property
    def swml_EntityType34(self):
        return self.__swml_EntityType34

    @swml_EntityType34.setter
    def swml_EntityType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType34", None)
        self.__swml_EntityType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentModel33"):
                opp_val = getattr(old_value, "swml_ContentModel33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentModel33"):
                opp_val = getattr(value, "swml_ContentModel33", None)
                if opp_val is None:
                    setattr(value, "swml_ContentModel33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_EntityType20(self):
        return self.__swml_EntityType20

    @swml_EntityType20.setter
    def swml_EntityType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType20", None)
        self.__swml_EntityType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_DynamicPage19"):
                opp_val = getattr(old_value, "swml_DynamicPage19", None)
                if opp_val == self:
                    setattr(old_value, "swml_DynamicPage19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_DynamicPage19"):
                opp_val = getattr(value, "swml_DynamicPage19", None)
                setattr(value, "swml_DynamicPage19", self)

    @property
    def swml_EntityType5(self):
        return self.__swml_EntityType5

    @swml_EntityType5.setter
    def swml_EntityType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__swml_EntityType5", None)
        self.__swml_EntityType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Attribute6"):
                opp_val = getattr(old_value, "swml_Attribute6", None)
                if opp_val == self:
                    setattr(old_value, "swml_Attribute6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Attribute6"):
                opp_val = getattr(value, "swml_Attribute6", None)
                setattr(value, "swml_Attribute6", self)

    @property
    def EntityType(self):
        return self.__EntityType

    @EntityType.setter
    def EntityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EntityType__EntityType", None)
        self.__EntityType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship"):
                opp_val = getattr(old_value, "relationship", None)
                if opp_val == self:
                    setattr(old_value, "relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship"):
                opp_val = getattr(value, "relationship", None)
                setattr(value, "relationship", self)

class swml_HypertextModel:

    pass
class swml_ContentModel:

    pass
class swml_WebApplication:

    def __init__(self, name: str, swml_WebApplication: "swml_ContentModel" = None, swml_WebApplication2: "swml_HypertextModel" = None):
        self.name = name
        self.swml_WebApplication = swml_WebApplication
        self.swml_WebApplication2 = swml_WebApplication2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_WebApplication2(self):
        return self.__swml_WebApplication2

    @swml_WebApplication2.setter
    def swml_WebApplication2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebApplication__swml_WebApplication2", None)
        self.__swml_WebApplication2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_HypertextModel"):
                opp_val = getattr(old_value, "swml_HypertextModel", None)
                if opp_val == self:
                    setattr(old_value, "swml_HypertextModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_HypertextModel"):
                opp_val = getattr(value, "swml_HypertextModel", None)
                setattr(value, "swml_HypertextModel", self)

    @property
    def swml_WebApplication(self):
        return self.__swml_WebApplication

    @swml_WebApplication.setter
    def swml_WebApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebApplication__swml_WebApplication", None)
        self.__swml_WebApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentModel"):
                opp_val = getattr(old_value, "swml_ContentModel", None)
                if opp_val == self:
                    setattr(old_value, "swml_ContentModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentModel"):
                opp_val = getattr(value, "swml_ContentModel", None)
                setattr(value, "swml_ContentModel", self)
