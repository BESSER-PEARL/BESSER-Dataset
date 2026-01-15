from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    string = "string"
    number = "number"
    boolean = "boolean"
    array = "array"
    object = "object"
    date = "date"
    any = "any"


############################################
# Definition of Classes
############################################

class Controller:

    pass
class webapp_ServiceController(Controller):

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        
    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        self.__endpoint = endpoint

class webapp_PageController(Controller):

    pass
class webapp_RouterBinding:

    def __init__(self, url: str, webapp_RouterBinding27: "webapp_Controller" = None, webapp_RouterBinding: "webapp_Router" = None):
        self.url = url
        self.webapp_RouterBinding27 = webapp_RouterBinding27
        self.webapp_RouterBinding = webapp_RouterBinding
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def webapp_RouterBinding27(self):
        return self.__webapp_RouterBinding27

    @webapp_RouterBinding27.setter
    def webapp_RouterBinding27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_RouterBinding__webapp_RouterBinding27", None)
        self.__webapp_RouterBinding27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller28"):
                opp_val = getattr(old_value, "webapp_Controller28", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Controller28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller28"):
                opp_val = getattr(value, "webapp_Controller28", None)
                setattr(value, "webapp_Controller28", self)

    @property
    def webapp_RouterBinding(self):
        return self.__webapp_RouterBinding

    @webapp_RouterBinding.setter
    def webapp_RouterBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_RouterBinding__webapp_RouterBinding", None)
        self.__webapp_RouterBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Router25"):
                opp_val = getattr(old_value, "webapp_Router25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Router25"):
                opp_val = getattr(value, "webapp_Router25", None)
                if opp_val is None:
                    setattr(value, "webapp_Router25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Router:

    pass
class Data:

    pass
class webapp_Model(Data):

    pass
class webapp_Collection(Data):

    pass
class NamedElement:

    pass
class webapp_Data(NamedElement):

    def __init__(self, endpoint: str, webapp_Data: "webapp_View" = None):
        self.endpoint = endpoint
        self.webapp_Data = webapp_Data
        
    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        self.__endpoint = endpoint

    @property
    def webapp_Data(self):
        return self.__webapp_Data

    @webapp_Data.setter
    def webapp_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Data__webapp_Data", None)
        self.__webapp_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View23"):
                opp_val = getattr(old_value, "webapp_View23", None)
                if opp_val == self:
                    setattr(old_value, "webapp_View23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View23"):
                opp_val = getattr(value, "webapp_View23", None)
                setattr(value, "webapp_View23", self)

class webapp_View(NamedElement):

    pass
class webapp_Controller(NamedElement):

    pass
class webapp_Attribute(NamedElement):

    def __init__(self, baseType: str, customType: str, webapp_Attribute: "webapp_Model" = None, webapp_Attribute31: "webapp_Controller" = None):
        self.baseType = baseType
        self.customType = customType
        self.webapp_Attribute = webapp_Attribute
        self.webapp_Attribute31 = webapp_Attribute31
        
    @property
    def customType(self) -> str:
        return self.__customType

    @customType.setter
    def customType(self, customType: str):
        self.__customType = customType

    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

    @property
    def webapp_Attribute(self):
        return self.__webapp_Attribute

    @webapp_Attribute.setter
    def webapp_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute", None)
        self.__webapp_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model12"):
                opp_val = getattr(old_value, "webapp_Model12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model12"):
                opp_val = getattr(value, "webapp_Model12", None)
                if opp_val is None:
                    setattr(value, "webapp_Model12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Attribute31(self):
        return self.__webapp_Attribute31

    @webapp_Attribute31.setter
    def webapp_Attribute31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute31", None)
        self.__webapp_Attribute31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller30"):
                opp_val = getattr(old_value, "webapp_Controller30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller30"):
                opp_val = getattr(value, "webapp_Controller30", None)
                if opp_val is None:
                    setattr(value, "webapp_Controller30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Template(NamedElement):

    def __init__(self, structure: str, style: str, webapp_Template: "webapp_WebApp" = None, webapp_Template21: "webapp_View" = None):
        self.structure = structure
        self.style = style
        self.webapp_Template = webapp_Template
        self.webapp_Template21 = webapp_Template21
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def structure(self) -> str:
        return self.__structure

    @structure.setter
    def structure(self, structure: str):
        self.__structure = structure

    @property
    def webapp_Template21(self):
        return self.__webapp_Template21

    @webapp_Template21.setter
    def webapp_Template21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Template__webapp_Template21", None)
        self.__webapp_Template21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View20"):
                opp_val = getattr(old_value, "webapp_View20", None)
                if opp_val == self:
                    setattr(old_value, "webapp_View20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View20"):
                opp_val = getattr(value, "webapp_View20", None)
                setattr(value, "webapp_View20", self)

    @property
    def webapp_Template(self):
        return self.__webapp_Template

    @webapp_Template.setter
    def webapp_Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Template__webapp_Template", None)
        self.__webapp_Template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebApp8"):
                opp_val = getattr(old_value, "webapp_WebApp8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebApp8"):
                opp_val = getattr(value, "webapp_WebApp8", None)
                if opp_val is None:
                    setattr(value, "webapp_WebApp8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_WebApp(NamedElement):

    pass
class webapp_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
