from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class WebApp_ActionMapping:

    pass
class WebApp_IdElement(ABC):

    def __init__(self, Id: str):
        self.Id = Id
        
    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

class WebApp_NamedElement(ABC):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class IdElement:

    pass
class NamedElement:

    pass
class WebApp_Action(NamedElement):

    pass
class WebApp_Controller(NamedElement):

    pass
class WebApp_Attribute(NamedElement):

    def __init__(self, value: str, WebApp_Attribute: "WebApp_Entities" = None, WebApp_Attribute40: "WebApp_Dummies" = None):
        self.value = value
        self.WebApp_Attribute = WebApp_Attribute
        self.WebApp_Attribute40 = WebApp_Attribute40
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def WebApp_Attribute40(self):
        return self.__WebApp_Attribute40

    @WebApp_Attribute40.setter
    def WebApp_Attribute40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Attribute__WebApp_Attribute40", None)
        self.__WebApp_Attribute40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_Dummies39"):
                opp_val = getattr(old_value, "WebApp_Dummies39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_Dummies39"):
                opp_val = getattr(value, "WebApp_Dummies39", None)
                if opp_val is None:
                    setattr(value, "WebApp_Dummies39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_Attribute(self):
        return self.__WebApp_Attribute

    @WebApp_Attribute.setter
    def WebApp_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Attribute__WebApp_Attribute", None)
        self.__WebApp_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_Entities29"):
                opp_val = getattr(old_value, "WebApp_Entities29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_Entities29"):
                opp_val = getattr(value, "WebApp_Entities29", None)
                if opp_val is None:
                    setattr(value, "WebApp_Entities29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WebApp_Entities(NamedElement):

    pass
class WebApp_FormElements(IdElement, NamedElement):

    pass
class WebApp_DynamicApplication(NamedElement):

    pass
class WebApp_Pages(NamedElement):

    pass
class WebApp_Dummies(NamedElement):

    pass
class WebApp_Views(IdElement, NamedElement):

    pass
class WebApp_styleElements(IdElement, NamedElement):

    pass
class WebApp_Forms(IdElement, NamedElement):

    pass
class WebApp_Tables(IdElement, NamedElement):

    pass