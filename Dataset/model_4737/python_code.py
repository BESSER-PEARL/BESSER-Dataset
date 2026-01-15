from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SWMLTypes(Enum):
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Email = "Email"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class Link:

    pass
class swml_CLink(Link):

    pass
class swml_NCLink(Link):

    pass
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

class swml_Page(ABC):

    def __init__(self, name: str, swml_Page16: set["swml_Link"] = None, swml_Page: "swml_HypertextLayer" = None, swml_Page7: "swml_HypertextLayer" = None, swml_Page21: "swml_Link" = None):
        self.name = name
        self.swml_Page16 = swml_Page16 if swml_Page16 is not None else set()
        self.swml_Page = swml_Page
        self.swml_Page7 = swml_Page7
        self.swml_Page21 = swml_Page21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def swml_Page21(self):
        return self.__swml_Page21

    @swml_Page21.setter
    def swml_Page21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__swml_Page21", None)
        self.__swml_Page21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Link20"):
                opp_val = getattr(old_value, "swml_Link20", None)
                if opp_val == self:
                    setattr(old_value, "swml_Link20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Link20"):
                opp_val = getattr(value, "swml_Link20", None)
                setattr(value, "swml_Link20", self)

    @property
    def swml_Page16(self):
        return self.__swml_Page16

    @swml_Page16.setter
    def swml_Page16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Page__swml_Page16", None)
        self.__swml_Page16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Link"):
                    opp_val = getattr(item, "swml_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Link"):
                    opp_val = getattr(item, "swml_Link", None)
                    
                    setattr(item, "swml_Link", self)
                    

class swml_ContentLayer:

    pass
class swml_HypertextLayer:

    pass
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

class swml_Class:

    def __init__(self, name: str, swml_Class: "swml_ContentLayer" = None, swml_Class11: set["swml_Attribute"] = None, swml_Class13: "swml_Attribute" = None, swml_Class18: "swml_DynamicPage" = None):
        self.name = name
        self.swml_Class = swml_Class
        self.swml_Class11 = swml_Class11 if swml_Class11 is not None else set()
        self.swml_Class13 = swml_Class13
        self.swml_Class18 = swml_Class18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Class18(self):
        return self.__swml_Class18

    @swml_Class18.setter
    def swml_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Class__swml_Class18", None)
        self.__swml_Class18 = value
        
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
