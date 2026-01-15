from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl301_Type(Interface):

    def __init__(self, signature: str, adl301_Type: set["adl301_Item"] = None):
        self.signature = signature
        self.adl301_Type = adl301_Type if adl301_Type is not None else set()
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def adl301_Type(self):
        return self.__adl301_Type

    @adl301_Type.setter
    def adl301_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl301_Type__adl301_Type", None)
        self.__adl301_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl301_Item"):
                    opp_val = getattr(item, "adl301_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "adl301_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl301_Item"):
                    opp_val = getattr(item, "adl301_Item", None)
                    
                    setattr(item, "adl301_Item", self)
                    

class adl301_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractComponent:

    pass
class Type:

    pass
class adl301_Attribute:

    def __init__(self, name: str, value: str, adl301_Attribute: "adl301_Attributes" = None):
        self.name = name
        self.value = value
        self.adl301_Attribute = adl301_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def adl301_Attribute(self):
        return self.__adl301_Attribute

    @adl301_Attribute.setter
    def adl301_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl301_Attribute__adl301_Attribute", None)
        self.__adl301_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl301_Attributes15"):
                opp_val = getattr(old_value, "adl301_Attributes15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl301_Attributes15"):
                opp_val = getattr(value, "adl301_Attributes15", None)
                if opp_val is None:
                    setattr(value, "adl301_Attributes15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class adl301_Binding(NamedElement):

    pass
class adl301_Component(AbstractComponent, NamedElement):

    pass
class adl301_Item(NamedElement):

    pass
class adl301_Interface(NamedElement):

    pass
class adl301_Provided(Type):

    pass
class adl301_Required(Type):

    pass
class adl301_Attributes:

    def __init__(self, signature: str, adl301_Attributes: "adl301_AbstractComponent" = None, adl301_Attributes15: set["adl301_Attribute"] = None):
        self.signature = signature
        self.adl301_Attributes = adl301_Attributes
        self.adl301_Attributes15 = adl301_Attributes15 if adl301_Attributes15 is not None else set()
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def adl301_Attributes15(self):
        return self.__adl301_Attributes15

    @adl301_Attributes15.setter
    def adl301_Attributes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl301_Attributes__adl301_Attributes15", None)
        self.__adl301_Attributes15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl301_Attribute"):
                    opp_val = getattr(item, "adl301_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "adl301_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl301_Attribute"):
                    opp_val = getattr(item, "adl301_Attribute", None)
                    
                    setattr(item, "adl301_Attribute", self)
                    

    @property
    def adl301_Attributes(self):
        return self.__adl301_Attributes

    @adl301_Attributes.setter
    def adl301_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl301_Attributes__adl301_Attributes", None)
        self.__adl301_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl301_AbstractComponent2"):
                opp_val = getattr(old_value, "adl301_AbstractComponent2", None)
                if opp_val == self:
                    setattr(old_value, "adl301_AbstractComponent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl301_AbstractComponent2"):
                opp_val = getattr(value, "adl301_AbstractComponent2", None)
                setattr(value, "adl301_AbstractComponent2", self)

class adl301_Content:

    def __init__(self, class: str, language: str, adl301_Content: "adl301_AbstractComponent" = None):
        self.class = class
        self.language = language
        self.adl301_Content = adl301_Content
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def adl301_Content(self):
        return self.__adl301_Content

    @adl301_Content.setter
    def adl301_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl301_Content__adl301_Content", None)
        self.__adl301_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl301_AbstractComponent"):
                opp_val = getattr(old_value, "adl301_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "adl301_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl301_AbstractComponent"):
                opp_val = getattr(value, "adl301_AbstractComponent", None)
                setattr(value, "adl301_AbstractComponent", self)

class adl301_AbstractComponent(ABC):

    pass