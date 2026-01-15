from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    String = "String"
    Float = "Float"
    Integer = "Integer"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class DynamicPage:

    pass
class swml_IndexPage(DynamicPage):

    pass
class swml_EntityPage(DynamicPage):

    pass
class swml_Icon:

    def __init__(self, image: str, swml_Icon: "swml_DynamicPage" = None):
        self.image = image
        self.swml_Icon = swml_Icon
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def swml_Icon(self):
        return self.__swml_Icon

    @swml_Icon.setter
    def swml_Icon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Icon__swml_Icon", None)
        self.__swml_Icon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_DynamicPage"):
                opp_val = getattr(old_value, "swml_DynamicPage", None)
                if opp_val == self:
                    setattr(old_value, "swml_DynamicPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_DynamicPage"):
                opp_val = getattr(value, "swml_DynamicPage", None)
                setattr(value, "swml_DynamicPage", self)

class swml_Link:

    def __init__(self, href: str, swml_Link: "swml_StaticPage" = None):
        self.href = href
        self.swml_Link = swml_Link
        
    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def swml_Link(self):
        return self.__swml_Link

    @swml_Link.setter
    def swml_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Link__swml_Link", None)
        self.__swml_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_StaticPage14"):
                opp_val = getattr(old_value, "swml_StaticPage14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_StaticPage14"):
                opp_val = getattr(value, "swml_StaticPage14", None)
                if opp_val is None:
                    setattr(value, "swml_StaticPage14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WebPage:

    pass
class swml_DynamicPage(WebPage):

    pass
class swml_WebPage:

    def __init__(self, title: str, relativeUrl: str):
        self.title = title
        self.relativeUrl = relativeUrl
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def relativeUrl(self) -> str:
        return self.__relativeUrl

    @relativeUrl.setter
    def relativeUrl(self, relativeUrl: str):
        self.__relativeUrl = relativeUrl

class swml_Relationship:

    def __init__(self, role: str, lowerBound: int, upperBound: int, swml_Relationship: "swml_Entity" = None, swml_Relationship11: "swml_Entity" = None):
        self.role = role
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.swml_Relationship = swml_Relationship
        self.swml_Relationship11 = swml_Relationship11
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

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
            if hasattr(old_value, "swml_Entity9"):
                opp_val = getattr(old_value, "swml_Entity9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity9"):
                opp_val = getattr(value, "swml_Entity9", None)
                if opp_val is None:
                    setattr(value, "swml_Entity9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Relationship11(self):
        return self.__swml_Relationship11

    @swml_Relationship11.setter
    def swml_Relationship11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Relationship__swml_Relationship11", None)
        self.__swml_Relationship11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity12"):
                opp_val = getattr(old_value, "swml_Entity12", None)
                if opp_val == self:
                    setattr(old_value, "swml_Entity12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity12"):
                opp_val = getattr(value, "swml_Entity12", None)
                setattr(value, "swml_Entity12", self)

class swml_Attribute:

    def __init__(self, name: str, dataType: str, swml_Attribute: "swml_Entity" = None, swml_Attribute7: "swml_Entity" = None):
        self.name = name
        self.dataType = dataType
        self.swml_Attribute = swml_Attribute
        self.swml_Attribute7 = swml_Attribute7
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Attribute7(self):
        return self.__swml_Attribute7

    @swml_Attribute7.setter
    def swml_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute7", None)
        self.__swml_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity6"):
                opp_val = getattr(old_value, "swml_Entity6", None)
                if opp_val == self:
                    setattr(old_value, "swml_Entity6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity6"):
                opp_val = getattr(value, "swml_Entity6", None)
                setattr(value, "swml_Entity6", self)

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
            if hasattr(old_value, "swml_Entity4"):
                opp_val = getattr(old_value, "swml_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity4"):
                opp_val = getattr(value, "swml_Entity4", None)
                if opp_val is None:
                    setattr(value, "swml_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_StaticPage(WebPage):

    pass
class swml_Entity:

    def __init__(self, name: str, swml_Entity: "swml_WebApplication" = None, swml_Entity4: set["swml_Attribute"] = None, swml_Entity6: "swml_Attribute" = None, swml_Entity9: set["swml_Relationship"] = None, swml_Entity18: "swml_DynamicPage" = None, swml_Entity12: "swml_Relationship" = None):
        self.name = name
        self.swml_Entity = swml_Entity
        self.swml_Entity4 = swml_Entity4 if swml_Entity4 is not None else set()
        self.swml_Entity6 = swml_Entity6
        self.swml_Entity9 = swml_Entity9 if swml_Entity9 is not None else set()
        self.swml_Entity18 = swml_Entity18
        self.swml_Entity12 = swml_Entity12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Entity18(self):
        return self.__swml_Entity18

    @swml_Entity18.setter
    def swml_Entity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity18", None)
        self.__swml_Entity18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_DynamicPage17"):
                opp_val = getattr(old_value, "swml_DynamicPage17", None)
                if opp_val == self:
                    setattr(old_value, "swml_DynamicPage17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_DynamicPage17"):
                opp_val = getattr(value, "swml_DynamicPage17", None)
                setattr(value, "swml_DynamicPage17", self)

    @property
    def swml_Entity4(self):
        return self.__swml_Entity4

    @swml_Entity4.setter
    def swml_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity4", None)
        self.__swml_Entity4 = value if value is not None else set()
        
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
    def swml_Entity(self):
        return self.__swml_Entity

    @swml_Entity.setter
    def swml_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity", None)
        self.__swml_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_WebApplication"):
                opp_val = getattr(old_value, "swml_WebApplication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_WebApplication"):
                opp_val = getattr(value, "swml_WebApplication", None)
                if opp_val is None:
                    setattr(value, "swml_WebApplication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Entity12(self):
        return self.__swml_Entity12

    @swml_Entity12.setter
    def swml_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity12", None)
        self.__swml_Entity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Relationship11"):
                opp_val = getattr(old_value, "swml_Relationship11", None)
                if opp_val == self:
                    setattr(old_value, "swml_Relationship11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Relationship11"):
                opp_val = getattr(value, "swml_Relationship11", None)
                setattr(value, "swml_Relationship11", self)

    @property
    def swml_Entity9(self):
        return self.__swml_Entity9

    @swml_Entity9.setter
    def swml_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity9", None)
        self.__swml_Entity9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Relationship"):
                    opp_val = getattr(item, "swml_Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Relationship"):
                    opp_val = getattr(item, "swml_Relationship", None)
                    
                    setattr(item, "swml_Relationship", self)
                    

    @property
    def swml_Entity6(self):
        return self.__swml_Entity6

    @swml_Entity6.setter
    def swml_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity6", None)
        self.__swml_Entity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Attribute7"):
                opp_val = getattr(old_value, "swml_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "swml_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Attribute7"):
                opp_val = getattr(value, "swml_Attribute7", None)
                setattr(value, "swml_Attribute7", self)

class swml_WebApplication:

    def __init__(self, name: str, swml_WebApplication: set["swml_Entity"] = None, swml_WebApplication2: "swml_StaticPage" = None):
        self.name = name
        self.swml_WebApplication = swml_WebApplication if swml_WebApplication is not None else set()
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
            if hasattr(old_value, "swml_StaticPage"):
                opp_val = getattr(old_value, "swml_StaticPage", None)
                if opp_val == self:
                    setattr(old_value, "swml_StaticPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_StaticPage"):
                opp_val = getattr(value, "swml_StaticPage", None)
                setattr(value, "swml_StaticPage", self)

    @property
    def swml_WebApplication(self):
        return self.__swml_WebApplication

    @swml_WebApplication.setter
    def swml_WebApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebApplication__swml_WebApplication", None)
        self.__swml_WebApplication = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Entity"):
                    opp_val = getattr(item, "swml_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Entity"):
                    opp_val = getattr(item, "swml_Entity", None)
                    
                    setattr(item, "swml_Entity", self)
                    
