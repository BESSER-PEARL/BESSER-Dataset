from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SWMLTypes(Enum):
    Boolean = "Boolean"
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Email = "Email"


############################################
# Definition of Classes
############################################

class Link:

    pass
class swml_v2_CLink(Link):

    pass
class swml_v2_NCLink(Link):

    pass
class Page:

    pass
class swml_v2_StaticPage(Page):

    pass
class swml_v2_DynamicPage(Page):

    pass
class DynamicPage:

    pass
class swml_v2_DetailsPage(DynamicPage):

    pass
class swml_v2_IndexPage(DynamicPage):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class swml_v2_Attribute:

    def __init__(self, name: str, type: str, swml_v2_Attribute: "swml_v2_Class" = None, swml_v2_Attribute14: "swml_v2_Class" = None):
        self.name = name
        self.type = type
        self.swml_v2_Attribute = swml_v2_Attribute
        self.swml_v2_Attribute14 = swml_v2_Attribute14
        
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
    def swml_v2_Attribute(self):
        return self.__swml_v2_Attribute

    @swml_v2_Attribute.setter
    def swml_v2_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Attribute__swml_v2_Attribute", None)
        self.__swml_v2_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_Class11"):
                opp_val = getattr(old_value, "swml_v2_Class11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_Class11"):
                opp_val = getattr(value, "swml_v2_Class11", None)
                if opp_val is None:
                    setattr(value, "swml_v2_Class11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_v2_Attribute14(self):
        return self.__swml_v2_Attribute14

    @swml_v2_Attribute14.setter
    def swml_v2_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Attribute__swml_v2_Attribute14", None)
        self.__swml_v2_Attribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_Class13"):
                opp_val = getattr(old_value, "swml_v2_Class13", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_Class13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_Class13"):
                opp_val = getattr(value, "swml_v2_Class13", None)
                setattr(value, "swml_v2_Class13", self)

class swml_v2_Class:

    def __init__(self, name: str, swml_v2_Class: "swml_v2_ContentLayer" = None, swml_v2_Class11: set["swml_v2_Attribute"] = None, swml_v2_Class13: "swml_v2_Attribute" = None, swml_v2_Class18: "swml_v2_DynamicPage" = None):
        self.name = name
        self.swml_v2_Class = swml_v2_Class
        self.swml_v2_Class11 = swml_v2_Class11 if swml_v2_Class11 is not None else set()
        self.swml_v2_Class13 = swml_v2_Class13
        self.swml_v2_Class18 = swml_v2_Class18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_v2_Class(self):
        return self.__swml_v2_Class

    @swml_v2_Class.setter
    def swml_v2_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Class__swml_v2_Class", None)
        self.__swml_v2_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_ContentLayer9"):
                opp_val = getattr(old_value, "swml_v2_ContentLayer9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_ContentLayer9"):
                opp_val = getattr(value, "swml_v2_ContentLayer9", None)
                if opp_val is None:
                    setattr(value, "swml_v2_ContentLayer9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_v2_Class11(self):
        return self.__swml_v2_Class11

    @swml_v2_Class11.setter
    def swml_v2_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Class__swml_v2_Class11", None)
        self.__swml_v2_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_v2_Attribute"):
                    opp_val = getattr(item, "swml_v2_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_v2_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_v2_Attribute"):
                    opp_val = getattr(item, "swml_v2_Attribute", None)
                    
                    setattr(item, "swml_v2_Attribute", self)
                    

    @property
    def swml_v2_Class18(self):
        return self.__swml_v2_Class18

    @swml_v2_Class18.setter
    def swml_v2_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Class__swml_v2_Class18", None)
        self.__swml_v2_Class18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_DynamicPage"):
                opp_val = getattr(old_value, "swml_v2_DynamicPage", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_DynamicPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_DynamicPage"):
                opp_val = getattr(value, "swml_v2_DynamicPage", None)
                setattr(value, "swml_v2_DynamicPage", self)

    @property
    def swml_v2_Class13(self):
        return self.__swml_v2_Class13

    @swml_v2_Class13.setter
    def swml_v2_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Class__swml_v2_Class13", None)
        self.__swml_v2_Class13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_Attribute14"):
                opp_val = getattr(old_value, "swml_v2_Attribute14", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_Attribute14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_Attribute14"):
                opp_val = getattr(value, "swml_v2_Attribute14", None)
                setattr(value, "swml_v2_Attribute14", self)

class swml_v2_Page(ABC):

    def __init__(self, name: str, swml_v2_Page16: set["swml_v2_Link"] = None, swml_v2_Page: "swml_v2_NavigationLayer" = None, swml_v2_Page7: "swml_v2_NavigationLayer" = None, swml_v2_Page21: "swml_v2_Link" = None):
        self.name = name
        self.swml_v2_Page16 = swml_v2_Page16 if swml_v2_Page16 is not None else set()
        self.swml_v2_Page = swml_v2_Page
        self.swml_v2_Page7 = swml_v2_Page7
        self.swml_v2_Page21 = swml_v2_Page21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_v2_Page(self):
        return self.__swml_v2_Page

    @swml_v2_Page.setter
    def swml_v2_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Page__swml_v2_Page", None)
        self.__swml_v2_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_NavigationLayer4"):
                opp_val = getattr(old_value, "swml_v2_NavigationLayer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_NavigationLayer4"):
                opp_val = getattr(value, "swml_v2_NavigationLayer4", None)
                if opp_val is None:
                    setattr(value, "swml_v2_NavigationLayer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_v2_Page21(self):
        return self.__swml_v2_Page21

    @swml_v2_Page21.setter
    def swml_v2_Page21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Page__swml_v2_Page21", None)
        self.__swml_v2_Page21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_Link20"):
                opp_val = getattr(old_value, "swml_v2_Link20", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_Link20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_Link20"):
                opp_val = getattr(value, "swml_v2_Link20", None)
                setattr(value, "swml_v2_Link20", self)

    @property
    def swml_v2_Page7(self):
        return self.__swml_v2_Page7

    @swml_v2_Page7.setter
    def swml_v2_Page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Page__swml_v2_Page7", None)
        self.__swml_v2_Page7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_NavigationLayer6"):
                opp_val = getattr(old_value, "swml_v2_NavigationLayer6", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_NavigationLayer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_NavigationLayer6"):
                opp_val = getattr(value, "swml_v2_NavigationLayer6", None)
                setattr(value, "swml_v2_NavigationLayer6", self)

    @property
    def swml_v2_Page16(self):
        return self.__swml_v2_Page16

    @swml_v2_Page16.setter
    def swml_v2_Page16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_Page__swml_v2_Page16", None)
        self.__swml_v2_Page16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_v2_Link"):
                    opp_val = getattr(item, "swml_v2_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_v2_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_v2_Link"):
                    opp_val = getattr(item, "swml_v2_Link", None)
                    
                    setattr(item, "swml_v2_Link", self)
                    

class swml_v2_ContentLayer:

    pass
class swml_v2_NavigationLayer:

    pass
class swml_v2_WebModel:

    def __init__(self, name: str, swml_v2_WebModel: "swml_v2_NavigationLayer" = None, swml_v2_WebModel2: "swml_v2_ContentLayer" = None):
        self.name = name
        self.swml_v2_WebModel = swml_v2_WebModel
        self.swml_v2_WebModel2 = swml_v2_WebModel2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_v2_WebModel2(self):
        return self.__swml_v2_WebModel2

    @swml_v2_WebModel2.setter
    def swml_v2_WebModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_WebModel__swml_v2_WebModel2", None)
        self.__swml_v2_WebModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_ContentLayer"):
                opp_val = getattr(old_value, "swml_v2_ContentLayer", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_ContentLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_ContentLayer"):
                opp_val = getattr(value, "swml_v2_ContentLayer", None)
                setattr(value, "swml_v2_ContentLayer", self)

    @property
    def swml_v2_WebModel(self):
        return self.__swml_v2_WebModel

    @swml_v2_WebModel.setter
    def swml_v2_WebModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_v2_WebModel__swml_v2_WebModel", None)
        self.__swml_v2_WebModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_v2_NavigationLayer"):
                opp_val = getattr(old_value, "swml_v2_NavigationLayer", None)
                if opp_val == self:
                    setattr(old_value, "swml_v2_NavigationLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_v2_NavigationLayer"):
                opp_val = getattr(value, "swml_v2_NavigationLayer", None)
                setattr(value, "swml_v2_NavigationLayer", self)

class swml_v2_Link:

    pass