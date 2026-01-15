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

    def __init__(self, requestURL: str, requestCookies: str, webapp_RouterBinding: "webapp_Router" = None, webapp_RouterBinding33: "webapp_Controller" = None):
        self.requestURL = requestURL
        self.requestCookies = requestCookies
        self.webapp_RouterBinding = webapp_RouterBinding
        self.webapp_RouterBinding33 = webapp_RouterBinding33
        
    @property
    def requestURL(self) -> str:
        return self.__requestURL

    @requestURL.setter
    def requestURL(self, requestURL: str):
        self.__requestURL = requestURL

    @property
    def requestCookies(self) -> str:
        return self.__requestCookies

    @requestCookies.setter
    def requestCookies(self, requestCookies: str):
        self.__requestCookies = requestCookies

    @property
    def webapp_RouterBinding33(self):
        return self.__webapp_RouterBinding33

    @webapp_RouterBinding33.setter
    def webapp_RouterBinding33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_RouterBinding__webapp_RouterBinding33", None)
        self.__webapp_RouterBinding33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller34"):
                opp_val = getattr(old_value, "webapp_Controller34", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Controller34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller34"):
                opp_val = getattr(value, "webapp_Controller34", None)
                setattr(value, "webapp_Controller34", self)

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
            if hasattr(old_value, "webapp_Router28"):
                opp_val = getattr(old_value, "webapp_Router28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Router28"):
                opp_val = getattr(value, "webapp_Router28", None)
                if opp_val is None:
                    setattr(value, "webapp_Router28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data:

    pass
class webapp_Model(Data):

    pass
class webapp_Router:

    pass
class webapp_Collection(Data):

    pass
class NamedElement:

    pass
class webapp_Style(NamedElement):

    def __init__(self, src: str, href: str, webapp_Style: "webapp_WebApp" = None, webapp_Style31: "webapp_Template" = None):
        self.src = src
        self.href = href
        self.webapp_Style = webapp_Style
        self.webapp_Style31 = webapp_Style31
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def webapp_Style(self):
        return self.__webapp_Style

    @webapp_Style.setter
    def webapp_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Style__webapp_Style", None)
        self.__webapp_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebApp12"):
                opp_val = getattr(old_value, "webapp_WebApp12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebApp12"):
                opp_val = getattr(value, "webapp_WebApp12", None)
                if opp_val is None:
                    setattr(value, "webapp_WebApp12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Style31(self):
        return self.__webapp_Style31

    @webapp_Style31.setter
    def webapp_Style31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Style__webapp_Style31", None)
        self.__webapp_Style31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Template30"):
                opp_val = getattr(old_value, "webapp_Template30", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Template30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Template30"):
                opp_val = getattr(value, "webapp_Template30", None)
                setattr(value, "webapp_Template30", self)

class webapp_Data(NamedElement):

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        
    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        self.__endpoint = endpoint

class webapp_Controller(NamedElement):

    pass
class webapp_View(NamedElement):

    pass
class webapp_Attribute(NamedElement):

    def __init__(self, baseType: str, customType: str, webapp_Attribute: "webapp_Model" = None, webapp_Attribute37: "webapp_Controller" = None, webapp_Attribute26: "webapp_View" = None):
        self.baseType = baseType
        self.customType = customType
        self.webapp_Attribute = webapp_Attribute
        self.webapp_Attribute37 = webapp_Attribute37
        self.webapp_Attribute26 = webapp_Attribute26
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

    @property
    def customType(self) -> str:
        return self.__customType

    @customType.setter
    def customType(self, customType: str):
        self.__customType = customType

    @property
    def webapp_Attribute26(self):
        return self.__webapp_Attribute26

    @webapp_Attribute26.setter
    def webapp_Attribute26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute26", None)
        self.__webapp_Attribute26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View25"):
                opp_val = getattr(old_value, "webapp_View25", None)
                if opp_val == self:
                    setattr(old_value, "webapp_View25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View25"):
                opp_val = getattr(value, "webapp_View25", None)
                setattr(value, "webapp_View25", self)

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
            if hasattr(old_value, "webapp_Model14"):
                opp_val = getattr(old_value, "webapp_Model14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model14"):
                opp_val = getattr(value, "webapp_Model14", None)
                if opp_val is None:
                    setattr(value, "webapp_Model14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Attribute37(self):
        return self.__webapp_Attribute37

    @webapp_Attribute37.setter
    def webapp_Attribute37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute37", None)
        self.__webapp_Attribute37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller36"):
                opp_val = getattr(old_value, "webapp_Controller36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller36"):
                opp_val = getattr(value, "webapp_Controller36", None)
                if opp_val is None:
                    setattr(value, "webapp_Controller36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Template(NamedElement):

    def __init__(self, structure: str, webapp_Template: "webapp_WebApp" = None, webapp_Template30: "webapp_Style" = None, webapp_Template23: "webapp_View" = None):
        self.structure = structure
        self.webapp_Template = webapp_Template
        self.webapp_Template30 = webapp_Template30
        self.webapp_Template23 = webapp_Template23
        
    @property
    def structure(self) -> str:
        return self.__structure

    @structure.setter
    def structure(self, structure: str):
        self.__structure = structure

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

    @property
    def webapp_Template23(self):
        return self.__webapp_Template23

    @webapp_Template23.setter
    def webapp_Template23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Template__webapp_Template23", None)
        self.__webapp_Template23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View22"):
                opp_val = getattr(old_value, "webapp_View22", None)
                if opp_val == self:
                    setattr(old_value, "webapp_View22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View22"):
                opp_val = getattr(value, "webapp_View22", None)
                setattr(value, "webapp_View22", self)

    @property
    def webapp_Template30(self):
        return self.__webapp_Template30

    @webapp_Template30.setter
    def webapp_Template30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Template__webapp_Template30", None)
        self.__webapp_Template30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Style31"):
                opp_val = getattr(old_value, "webapp_Style31", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Style31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Style31"):
                opp_val = getattr(value, "webapp_Style31", None)
                setattr(value, "webapp_Style31", self)

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
