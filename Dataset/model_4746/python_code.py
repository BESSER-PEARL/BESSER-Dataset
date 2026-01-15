from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AppTypes(Enum):
    String = "String"
    Integer = "Integer"
    Float = "Float"
    Double = "Double"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class wappm_Reference:

    def __init__(self, name: str, lowBound: int, upBound: int, wappm_Reference: "wappm_WebClass" = None):
        self.name = name
        self.lowBound = lowBound
        self.upBound = upBound
        self.wappm_Reference = wappm_Reference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def upBound(self) -> int:
        return self.__upBound

    @upBound.setter
    def upBound(self, upBound: int):
        self.__upBound = upBound

    @property
    def lowBound(self) -> int:
        return self.__lowBound

    @lowBound.setter
    def lowBound(self, lowBound: int):
        self.__lowBound = lowBound

    @property
    def wappm_Reference(self):
        return self.__wappm_Reference

    @wappm_Reference.setter
    def wappm_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_Reference__wappm_Reference", None)
        self.__wappm_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_WebClass17"):
                opp_val = getattr(old_value, "wappm_WebClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_WebClass17"):
                opp_val = getattr(value, "wappm_WebClass17", None)
                if opp_val is None:
                    setattr(value, "wappm_WebClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wappm_Attribute:

    def __init__(self, name: str, type: str, wappm_Attribute: "wappm_WebClass" = None):
        self.name = name
        self.type = type
        self.wappm_Attribute = wappm_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wappm_Attribute(self):
        return self.__wappm_Attribute

    @wappm_Attribute.setter
    def wappm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_Attribute__wappm_Attribute", None)
        self.__wappm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_WebClass15"):
                opp_val = getattr(old_value, "wappm_WebClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_WebClass15"):
                opp_val = getattr(value, "wappm_WebClass15", None)
                if opp_val is None:
                    setattr(value, "wappm_WebClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DynamicPage:

    pass
class wappm_IndexPage(DynamicPage):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class wappm_DetailPage(DynamicPage):

    pass
class wappm_WebClass:

    def __init__(self, name: str, wappm_WebClass17: set["wappm_Reference"] = None, wappm_WebClass: "wappm_DynamicPage" = None, wappm_WebClass13: "wappm_ContentLayer" = None, wappm_WebClass15: set["wappm_Attribute"] = None):
        self.name = name
        self.wappm_WebClass17 = wappm_WebClass17 if wappm_WebClass17 is not None else set()
        self.wappm_WebClass = wappm_WebClass
        self.wappm_WebClass13 = wappm_WebClass13
        self.wappm_WebClass15 = wappm_WebClass15 if wappm_WebClass15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wappm_WebClass13(self):
        return self.__wappm_WebClass13

    @wappm_WebClass13.setter
    def wappm_WebClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebClass__wappm_WebClass13", None)
        self.__wappm_WebClass13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_ContentLayer12"):
                opp_val = getattr(old_value, "wappm_ContentLayer12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_ContentLayer12"):
                opp_val = getattr(value, "wappm_ContentLayer12", None)
                if opp_val is None:
                    setattr(value, "wappm_ContentLayer12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wappm_WebClass(self):
        return self.__wappm_WebClass

    @wappm_WebClass.setter
    def wappm_WebClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebClass__wappm_WebClass", None)
        self.__wappm_WebClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_DynamicPage"):
                opp_val = getattr(old_value, "wappm_DynamicPage", None)
                if opp_val == self:
                    setattr(old_value, "wappm_DynamicPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_DynamicPage"):
                opp_val = getattr(value, "wappm_DynamicPage", None)
                setattr(value, "wappm_DynamicPage", self)

    @property
    def wappm_WebClass15(self):
        return self.__wappm_WebClass15

    @wappm_WebClass15.setter
    def wappm_WebClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebClass__wappm_WebClass15", None)
        self.__wappm_WebClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wappm_Attribute"):
                    opp_val = getattr(item, "wappm_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "wappm_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wappm_Attribute"):
                    opp_val = getattr(item, "wappm_Attribute", None)
                    
                    setattr(item, "wappm_Attribute", self)
                    

    @property
    def wappm_WebClass17(self):
        return self.__wappm_WebClass17

    @wappm_WebClass17.setter
    def wappm_WebClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebClass__wappm_WebClass17", None)
        self.__wappm_WebClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wappm_Reference"):
                    opp_val = getattr(item, "wappm_Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "wappm_Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wappm_Reference"):
                    opp_val = getattr(item, "wappm_Reference", None)
                    
                    setattr(item, "wappm_Reference", self)
                    

class Page:

    pass
class wappm_DynamicPage(Page):

    pass
class wappm_StaticPage(Page):

    pass
class wappm_Link:

    pass
class wappm_Page:

    def __init__(self, name: str, path: str, wappm_Page: "wappm_HypertextLayer" = None, wappm_Page6: set["wappm_Link"] = None, wappm_Page10: "wappm_Link" = None):
        self.name = name
        self.path = path
        self.wappm_Page = wappm_Page
        self.wappm_Page6 = wappm_Page6 if wappm_Page6 is not None else set()
        self.wappm_Page10 = wappm_Page10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def wappm_Page(self):
        return self.__wappm_Page

    @wappm_Page.setter
    def wappm_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_Page__wappm_Page", None)
        self.__wappm_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_HypertextLayer4"):
                opp_val = getattr(old_value, "wappm_HypertextLayer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_HypertextLayer4"):
                opp_val = getattr(value, "wappm_HypertextLayer4", None)
                if opp_val is None:
                    setattr(value, "wappm_HypertextLayer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wappm_Page10(self):
        return self.__wappm_Page10

    @wappm_Page10.setter
    def wappm_Page10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_Page__wappm_Page10", None)
        self.__wappm_Page10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_Link9"):
                opp_val = getattr(old_value, "wappm_Link9", None)
                if opp_val == self:
                    setattr(old_value, "wappm_Link9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_Link9"):
                opp_val = getattr(value, "wappm_Link9", None)
                setattr(value, "wappm_Link9", self)

    @property
    def wappm_Page6(self):
        return self.__wappm_Page6

    @wappm_Page6.setter
    def wappm_Page6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_Page__wappm_Page6", None)
        self.__wappm_Page6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wappm_Link"):
                    opp_val = getattr(item, "wappm_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "wappm_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wappm_Link"):
                    opp_val = getattr(item, "wappm_Link", None)
                    
                    setattr(item, "wappm_Link", self)
                    

class wappm_ContentLayer:

    def __init__(self, contentName: str, wappm_ContentLayer: "wappm_WebModel" = None, wappm_ContentLayer12: set["wappm_WebClass"] = None):
        self.contentName = contentName
        self.wappm_ContentLayer = wappm_ContentLayer
        self.wappm_ContentLayer12 = wappm_ContentLayer12 if wappm_ContentLayer12 is not None else set()
        
    @property
    def contentName(self) -> str:
        return self.__contentName

    @contentName.setter
    def contentName(self, contentName: str):
        self.__contentName = contentName

    @property
    def wappm_ContentLayer(self):
        return self.__wappm_ContentLayer

    @wappm_ContentLayer.setter
    def wappm_ContentLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_ContentLayer__wappm_ContentLayer", None)
        self.__wappm_ContentLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_WebModel2"):
                opp_val = getattr(old_value, "wappm_WebModel2", None)
                if opp_val == self:
                    setattr(old_value, "wappm_WebModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_WebModel2"):
                opp_val = getattr(value, "wappm_WebModel2", None)
                setattr(value, "wappm_WebModel2", self)

    @property
    def wappm_ContentLayer12(self):
        return self.__wappm_ContentLayer12

    @wappm_ContentLayer12.setter
    def wappm_ContentLayer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_ContentLayer__wappm_ContentLayer12", None)
        self.__wappm_ContentLayer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wappm_WebClass13"):
                    opp_val = getattr(item, "wappm_WebClass13", None)
                    
                    if opp_val == self:
                        setattr(item, "wappm_WebClass13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wappm_WebClass13"):
                    opp_val = getattr(item, "wappm_WebClass13", None)
                    
                    setattr(item, "wappm_WebClass13", self)
                    

class wappm_HypertextLayer:

    def __init__(self, hyperName: str, wappm_HypertextLayer: "wappm_WebModel" = None, wappm_HypertextLayer4: set["wappm_Page"] = None):
        self.hyperName = hyperName
        self.wappm_HypertextLayer = wappm_HypertextLayer
        self.wappm_HypertextLayer4 = wappm_HypertextLayer4 if wappm_HypertextLayer4 is not None else set()
        
    @property
    def hyperName(self) -> str:
        return self.__hyperName

    @hyperName.setter
    def hyperName(self, hyperName: str):
        self.__hyperName = hyperName

    @property
    def wappm_HypertextLayer(self):
        return self.__wappm_HypertextLayer

    @wappm_HypertextLayer.setter
    def wappm_HypertextLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_HypertextLayer__wappm_HypertextLayer", None)
        self.__wappm_HypertextLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_WebModel"):
                opp_val = getattr(old_value, "wappm_WebModel", None)
                if opp_val == self:
                    setattr(old_value, "wappm_WebModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_WebModel"):
                opp_val = getattr(value, "wappm_WebModel", None)
                setattr(value, "wappm_WebModel", self)

    @property
    def wappm_HypertextLayer4(self):
        return self.__wappm_HypertextLayer4

    @wappm_HypertextLayer4.setter
    def wappm_HypertextLayer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_HypertextLayer__wappm_HypertextLayer4", None)
        self.__wappm_HypertextLayer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wappm_Page"):
                    opp_val = getattr(item, "wappm_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "wappm_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wappm_Page"):
                    opp_val = getattr(item, "wappm_Page", None)
                    
                    setattr(item, "wappm_Page", self)
                    

class wappm_WebModel:

    def __init__(self, name: str, wappm_WebModel: "wappm_HypertextLayer" = None, wappm_WebModel2: "wappm_ContentLayer" = None):
        self.name = name
        self.wappm_WebModel = wappm_WebModel
        self.wappm_WebModel2 = wappm_WebModel2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wappm_WebModel(self):
        return self.__wappm_WebModel

    @wappm_WebModel.setter
    def wappm_WebModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebModel__wappm_WebModel", None)
        self.__wappm_WebModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_HypertextLayer"):
                opp_val = getattr(old_value, "wappm_HypertextLayer", None)
                if opp_val == self:
                    setattr(old_value, "wappm_HypertextLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_HypertextLayer"):
                opp_val = getattr(value, "wappm_HypertextLayer", None)
                setattr(value, "wappm_HypertextLayer", self)

    @property
    def wappm_WebModel2(self):
        return self.__wappm_WebModel2

    @wappm_WebModel2.setter
    def wappm_WebModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wappm_WebModel__wappm_WebModel2", None)
        self.__wappm_WebModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wappm_ContentLayer"):
                opp_val = getattr(old_value, "wappm_ContentLayer", None)
                if opp_val == self:
                    setattr(old_value, "wappm_ContentLayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wappm_ContentLayer"):
                opp_val = getattr(value, "wappm_ContentLayer", None)
                setattr(value, "wappm_ContentLayer", self)
