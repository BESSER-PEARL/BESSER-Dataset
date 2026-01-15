from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UIElementType(Enum):
    input = "input"
    output = "output"


############################################
# Definition of Classes
############################################

class UIElement:

    pass
class webapp_ImageViewer(UIElement):

    pass
class webapp_Table(UIElement):

    pass
class webapp_TextArea(UIElement):

    pass
class webapp_Form(UIElement):

    pass
class Named:

    pass
class webapp_Attribute(Named):

    def __init__(self, type: str, Attribute: "webapp_DataStructure" = None, Attribute13: "webapp_DataStructure" = None, parentOf: "webapp_DataStructure" = None, linkedTo: set["webapp_DataStructure"] = None):
        self.type = type
        self.Attribute = Attribute
        self.Attribute13 = Attribute13
        self.parentOf = parentOf
        self.linkedTo = linkedTo if linkedTo is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def parentOf(self):
        return self.__parentOf

    @parentOf.setter
    def parentOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__parentOf", None)
        self.__parentOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataStructure17"):
                opp_val = getattr(old_value, "DataStructure17", None)
                if opp_val == self:
                    setattr(old_value, "DataStructure17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataStructure17"):
                opp_val = getattr(value, "DataStructure17", None)
                setattr(value, "DataStructure17", self)

    @property
    def Attribute13(self):
        return self.__Attribute13

    @Attribute13.setter
    def Attribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__Attribute13", None)
        self.__Attribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkedBy"):
                opp_val = getattr(old_value, "linkedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkedBy"):
                opp_val = getattr(value, "linkedBy", None)
                if opp_val is None:
                    setattr(value, "linkedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linkedTo(self):
        return self.__linkedTo

    @linkedTo.setter
    def linkedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__linkedTo", None)
        self.__linkedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataStructure19"):
                    opp_val = getattr(item, "DataStructure19", None)
                    
                    if opp_val == self:
                        setattr(item, "DataStructure19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataStructure19"):
                    opp_val = getattr(item, "DataStructure19", None)
                    
                    setattr(item, "DataStructure19", self)
                    

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributeOf"):
                opp_val = getattr(old_value, "attributeOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributeOf"):
                opp_val = getattr(value, "attributeOf", None)
                if opp_val is None:
                    setattr(value, "attributeOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_DataSourceManager(Named):

    pass
class webapp_UIElement(Named):

    def __init__(self, type: str, webapp_UIElement: "webapp_ClientPage" = None, webapp_UIElement25: "webapp_DataStructure" = None):
        self.type = type
        self.webapp_UIElement = webapp_UIElement
        self.webapp_UIElement25 = webapp_UIElement25
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def webapp_UIElement25(self):
        return self.__webapp_UIElement25

    @webapp_UIElement25.setter
    def webapp_UIElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_UIElement__webapp_UIElement25", None)
        self.__webapp_UIElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_DataStructure26"):
                opp_val = getattr(old_value, "webapp_DataStructure26", None)
                if opp_val == self:
                    setattr(old_value, "webapp_DataStructure26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_DataStructure26"):
                opp_val = getattr(value, "webapp_DataStructure26", None)
                setattr(value, "webapp_DataStructure26", self)

    @property
    def webapp_UIElement(self):
        return self.__webapp_UIElement

    @webapp_UIElement.setter
    def webapp_UIElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_UIElement__webapp_UIElement", None)
        self.__webapp_UIElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ClientPage21"):
                opp_val = getattr(old_value, "webapp_ClientPage21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ClientPage21"):
                opp_val = getattr(value, "webapp_ClientPage21", None)
                if opp_val is None:
                    setattr(value, "webapp_ClientPage21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_ServerPage(Named):

    def __init__(self, connectsTo: "webapp_ClientPage" = None, providesContent: set["webapp_DataSourceManager"] = None, managedBy: set["webapp_DataStructure"] = None, ServerPage: "webapp_DataStructure" = None, ServerPage15: "webapp_DataSourceManager" = None, webapp_ServerPage: "webapp_WebApp" = None, ServerPage23: "webapp_ClientPage" = None):
        self.connectsTo = connectsTo
        self.providesContent = providesContent if providesContent is not None else set()
        self.managedBy = managedBy if managedBy is not None else set()
        self.ServerPage = ServerPage
        self.ServerPage15 = ServerPage15
        self.webapp_ServerPage = webapp_ServerPage
        self.ServerPage23 = ServerPage23
        
    @property
    def providesContent(self):
        return self.__providesContent

    @providesContent.setter
    def providesContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__providesContent", None)
        self.__providesContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataSourceManager"):
                    opp_val = getattr(item, "DataSourceManager", None)
                    
                    if opp_val == self:
                        setattr(item, "DataSourceManager", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataSourceManager"):
                    opp_val = getattr(item, "DataSourceManager", None)
                    
                    setattr(item, "DataSourceManager", self)
                    

    @property
    def ServerPage15(self):
        return self.__ServerPage15

    @ServerPage15.setter
    def ServerPage15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__ServerPage15", None)
        self.__ServerPage15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "getContents"):
                opp_val = getattr(old_value, "getContents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "getContents"):
                opp_val = getattr(value, "getContents", None)
                if opp_val is None:
                    setattr(value, "getContents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_ServerPage(self):
        return self.__webapp_ServerPage

    @webapp_ServerPage.setter
    def webapp_ServerPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__webapp_ServerPage", None)
        self.__webapp_ServerPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebApp2"):
                opp_val = getattr(old_value, "webapp_WebApp2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebApp2"):
                opp_val = getattr(value, "webapp_WebApp2", None)
                if opp_val is None:
                    setattr(value, "webapp_WebApp2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ServerPage(self):
        return self.__ServerPage

    @ServerPage.setter
    def ServerPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__ServerPage", None)
        self.__ServerPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manages"):
                opp_val = getattr(old_value, "manages", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manages"):
                opp_val = getattr(value, "manages", None)
                if opp_val is None:
                    setattr(value, "manages", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ServerPage23(self):
        return self.__ServerPage23

    @ServerPage23.setter
    def ServerPage23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__ServerPage23", None)
        self.__ServerPage23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generates"):
                opp_val = getattr(old_value, "generates", None)
                if opp_val == self:
                    setattr(old_value, "generates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generates"):
                opp_val = getattr(value, "generates", None)
                setattr(value, "generates", self)

    @property
    def connectsTo(self):
        return self.__connectsTo

    @connectsTo.setter
    def connectsTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__connectsTo", None)
        self.__connectsTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClientPage"):
                opp_val = getattr(old_value, "ClientPage", None)
                if opp_val == self:
                    setattr(old_value, "ClientPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClientPage"):
                opp_val = getattr(value, "ClientPage", None)
                setattr(value, "ClientPage", self)

    @property
    def managedBy(self):
        return self.__managedBy

    @managedBy.setter
    def managedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ServerPage__managedBy", None)
        self.__managedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataStructure"):
                    opp_val = getattr(item, "DataStructure", None)
                    
                    if opp_val == self:
                        setattr(item, "DataStructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataStructure"):
                    opp_val = getattr(item, "DataStructure", None)
                    
                    setattr(item, "DataStructure", self)
                    

    def response(self):
        # TODO: Implement response method
        pass

    def request(self):
        # TODO: Implement request method
        pass

class webapp_DataStructure(Named):

    pass
class webapp_ClientPage(Named):

    pass
class webapp_WebApp(Named):

    pass
class webapp_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
