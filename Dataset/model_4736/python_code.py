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
class swml_CLink(Link):

    pass
class swml_NCLink(Link):

    pass
class swml_Page(ABC):

    def __init__(self, name: str, source: set["swml_Link"] = None, swml_Page: "swml_HypertextLayer" = None, swml_Page7: "swml_HypertextLayer" = None, swml_Page19: "swml_Link" = None, Page: "swml_Link" = None):
        self.name = name
        self.source = source if source is not None else set()
        self.swml_Page = swml_Page
        self.swml_Page7 = swml_Page7
        self.swml_Page19 = swml_Page19
        self.Page = Page
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__Page", None)
        self.__Page = value
        
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
    def swml_Page19(self):
        return self.__swml_Page19

    @swml_Page19.setter
    def swml_Page19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__swml_Page19", None)
        self.__swml_Page19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Link"):
                opp_val = getattr(old_value, "swml_Link", None)
                if opp_val == self:
                    setattr(old_value, "swml_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Link"):
                opp_val = getattr(value, "swml_Link", None)
                setattr(value, "swml_Link", self)

    @property
    def swml_Page7(self):
        return self.__swml_Page7

    @swml_Page7.setter
    def swml_Page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__swml_Page7", None)
        self.__swml_Page7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_HypertextLayer6"):
                opp_val = getattr(old_value, "swml_HypertextLayer6", None)
                if opp_val == self:
                    setattr(old_value, "swml_HypertextLayer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_HypertextLayer6"):
                opp_val = getattr(value, "swml_HypertextLayer6", None)
                setattr(value, "swml_HypertextLayer6", self)

    @property
    def swml_Page(self):
        return self.__swml_Page

    @swml_Page.setter
    def swml_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__swml_Page", None)
        self.__swml_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_HypertextLayer4"):
                opp_val = getattr(old_value, "swml_HypertextLayer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_HypertextLayer4"):
                opp_val = getattr(value, "swml_HypertextLayer4", None)
                if opp_val is None:
                    setattr(value, "swml_HypertextLayer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__source", None)
        self.__source = value if value is not None else set()
        
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
                    

class Page:

    pass
class swml_StaticPage(Page):

    pass
class swml_DynamicPage(Page):

    pass
class DynamicPage:

    pass
class swml_DetailsPage(DynamicPage):

    pass
class swml_IndexPage(DynamicPage):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class swml_Link(ABC):

    pass
class swml_Attribute:

    def __init__(self, name: str, type: str, swml_Attribute: "swml_Class" = None, swml_Attribute14: "swml_Class" = None):
        self.name = name
        self.type = type
        self.swml_Attribute = swml_Attribute
        self.swml_Attribute14 = swml_Attribute14
        
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
    def swml_Attribute(self):
        return self.__swml_Attribute

    @swml_Attribute.setter
    def swml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute", None)
        self.__swml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Class11"):
                opp_val = getattr(old_value, "swml_Class11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Class11"):
                opp_val = getattr(value, "swml_Class11", None)
                if opp_val is None:
                    setattr(value, "swml_Class11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Attribute14(self):
        return self.__swml_Attribute14

    @swml_Attribute14.setter
    def swml_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute14", None)
        self.__swml_Attribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Class13"):
                opp_val = getattr(old_value, "swml_Class13", None)
                if opp_val == self:
                    setattr(old_value, "swml_Class13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Class13"):
                opp_val = getattr(value, "swml_Class13", None)
                setattr(value, "swml_Class13", self)

class swml_Class:

    def __init__(self, name: str, swml_Class: "swml_ContentLayer" = None, swml_Class11: set["swml_Attribute"] = None, swml_Class13: "swml_Attribute" = None, swml_Class17: "swml_DynamicPage" = None):
        self.name = name
        self.swml_Class = swml_Class
        self.swml_Class11 = swml_Class11 if swml_Class11 is not None else set()
        self.swml_Class13 = swml_Class13
        self.swml_Class17 = swml_Class17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Class13(self):
        return self.__swml_Class13

    @swml_Class13.setter
    def swml_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Class__swml_Class13", None)
        self.__swml_Class13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Attribute14"):
                opp_val = getattr(old_value, "swml_Attribute14", None)
                if opp_val == self:
                    setattr(old_value, "swml_Attribute14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Attribute14"):
                opp_val = getattr(value, "swml_Attribute14", None)
                setattr(value, "swml_Attribute14", self)

    @property
    def swml_Class(self):
        return self.__swml_Class

    @swml_Class.setter
    def swml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Class__swml_Class", None)
        self.__swml_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentLayer9"):
                opp_val = getattr(old_value, "swml_ContentLayer9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentLayer9"):
                opp_val = getattr(value, "swml_ContentLayer9", None)
                if opp_val is None:
                    setattr(value, "swml_ContentLayer9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Class11(self):
        return self.__swml_Class11

    @swml_Class11.setter
    def swml_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Class__swml_Class11", None)
        self.__swml_Class11 = value if value is not None else set()
        
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
    def swml_Class17(self):
        return self.__swml_Class17

    @swml_Class17.setter
    def swml_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Class__swml_Class17", None)
        self.__swml_Class17 = value
        
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

class swml_ContentLayer:

    def __init__(self, name: str, swml_ContentLayer: "swml_WebModel" = None, swml_ContentLayer9: set["swml_Class"] = None):
        self.name = name
        self.swml_ContentLayer = swml_ContentLayer
        self.swml_ContentLayer9 = swml_ContentLayer9 if swml_ContentLayer9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_ContentLayer9(self):
        return self.__swml_ContentLayer9

    @swml_ContentLayer9.setter
    def swml_ContentLayer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_ContentLayer__swml_ContentLayer9", None)
        self.__swml_ContentLayer9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Class"):
                    opp_val = getattr(item, "swml_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Class"):
                    opp_val = getattr(item, "swml_Class", None)
                    
                    setattr(item, "swml_Class", self)
                    

    @property
    def swml_ContentLayer(self):
        return self.__swml_ContentLayer

    @swml_ContentLayer.setter
    def swml_ContentLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_ContentLayer__swml_ContentLayer", None)
        self.__swml_ContentLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_WebModel2"):
                opp_val = getattr(old_value, "swml_WebModel2", None)
                if opp_val == self:
                    setattr(old_value, "swml_WebModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_WebModel2"):
                opp_val = getattr(value, "swml_WebModel2", None)
                setattr(value, "swml_WebModel2", self)

class swml_HypertextLayer:

    def __init__(self, name: str, swml_HypertextLayer: "swml_WebModel" = None, swml_HypertextLayer4: set["swml_Page"] = None, swml_HypertextLayer6: "swml_Page" = None):
        self.name = name
        self.swml_HypertextLayer = swml_HypertextLayer
        self.swml_HypertextLayer4 = swml_HypertextLayer4 if swml_HypertextLayer4 is not None else set()
        self.swml_HypertextLayer6 = swml_HypertextLayer6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_HypertextLayer4(self):
        return self.__swml_HypertextLayer4

    @swml_HypertextLayer4.setter
    def swml_HypertextLayer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_HypertextLayer__swml_HypertextLayer4", None)
        self.__swml_HypertextLayer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Page"):
                    opp_val = getattr(item, "swml_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Page"):
                    opp_val = getattr(item, "swml_Page", None)
                    
                    setattr(item, "swml_Page", self)
                    

    @property
    def swml_HypertextLayer(self):
        return self.__swml_HypertextLayer

    @swml_HypertextLayer.setter
    def swml_HypertextLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_HypertextLayer__swml_HypertextLayer", None)
        self.__swml_HypertextLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_WebModel"):
                opp_val = getattr(old_value, "swml_WebModel", None)
                if opp_val == self:
                    setattr(old_value, "swml_WebModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_WebModel"):
                opp_val = getattr(value, "swml_WebModel", None)
                setattr(value, "swml_WebModel", self)

    @property
    def swml_HypertextLayer6(self):
        return self.__swml_HypertextLayer6

    @swml_HypertextLayer6.setter
    def swml_HypertextLayer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_HypertextLayer__swml_HypertextLayer6", None)
        self.__swml_HypertextLayer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Page7"):
                opp_val = getattr(old_value, "swml_Page7", None)
                if opp_val == self:
                    setattr(old_value, "swml_Page7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Page7"):
                opp_val = getattr(value, "swml_Page7", None)
                setattr(value, "swml_Page7", self)

class swml_WebModel:

    def __init__(self, name: str, swml_WebModel: "swml_HypertextLayer" = None, swml_WebModel2: "swml_ContentLayer" = None):
        self.name = name
        self.swml_WebModel = swml_WebModel
        self.swml_WebModel2 = swml_WebModel2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_WebModel2(self):
        return self.__swml_WebModel2

    @swml_WebModel2.setter
    def swml_WebModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebModel__swml_WebModel2", None)
        self.__swml_WebModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentLayer"):
                opp_val = getattr(old_value, "swml_ContentLayer", None)
                if opp_val == self:
                    setattr(old_value, "swml_ContentLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentLayer"):
                opp_val = getattr(value, "swml_ContentLayer", None)
                setattr(value, "swml_ContentLayer", self)

    @property
    def swml_WebModel(self):
        return self.__swml_WebModel

    @swml_WebModel.setter
    def swml_WebModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebModel__swml_WebModel", None)
        self.__swml_WebModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_HypertextLayer"):
                opp_val = getattr(old_value, "swml_HypertextLayer", None)
                if opp_val == self:
                    setattr(old_value, "swml_HypertextLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_HypertextLayer"):
                opp_val = getattr(value, "swml_HypertextLayer", None)
                setattr(value, "swml_HypertextLayer", self)
