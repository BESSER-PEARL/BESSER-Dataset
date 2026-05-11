from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Type:

    pass
class Interface:

    pass
class adlrecurs_Type(Interface):

    def __init__(self, signature: str, adlrecurs_Type: set["adlrecurs_Item"] = None):
        self.signature = signature
        self.adlrecurs_Type = adlrecurs_Type if adlrecurs_Type is not None else set()
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def adlrecurs_Type(self):
        return self.__adlrecurs_Type

    @adlrecurs_Type.setter
    def adlrecurs_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecurs_Type__adlrecurs_Type", None)
        self.__adlrecurs_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlrecurs_Item"):
                    opp_val = getattr(item, "adlrecurs_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "adlrecurs_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlrecurs_Item"):
                    opp_val = getattr(item, "adlrecurs_Item", None)
                    
                    setattr(item, "adlrecurs_Item", self)
                    

class adlrecurs_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AbstractComponent:

    pass
class adlrecurs_Required(Type):

    pass
class adlrecurs_Attributes:

    def __init__(self, signature: str, adlrecurs_Attributes15: set["adlrecurs_Attribute"] = None, adlrecurs_Attributes: "adlrecurs_AbstractComponent" = None):
        self.signature = signature
        self.adlrecurs_Attributes15 = adlrecurs_Attributes15 if adlrecurs_Attributes15 is not None else set()
        self.adlrecurs_Attributes = adlrecurs_Attributes
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def adlrecurs_Attributes15(self):
        return self.__adlrecurs_Attributes15

    @adlrecurs_Attributes15.setter
    def adlrecurs_Attributes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecurs_Attributes__adlrecurs_Attributes15", None)
        self.__adlrecurs_Attributes15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlrecurs_Attribute"):
                    opp_val = getattr(item, "adlrecurs_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "adlrecurs_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlrecurs_Attribute"):
                    opp_val = getattr(item, "adlrecurs_Attribute", None)
                    
                    setattr(item, "adlrecurs_Attribute", self)
                    

    @property
    def adlrecurs_Attributes(self):
        return self.__adlrecurs_Attributes

    @adlrecurs_Attributes.setter
    def adlrecurs_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecurs_Attributes__adlrecurs_Attributes", None)
        self.__adlrecurs_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlrecurs_AbstractComponent2"):
                opp_val = getattr(old_value, "adlrecurs_AbstractComponent2", None)
                if opp_val == self:
                    setattr(old_value, "adlrecurs_AbstractComponent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlrecurs_AbstractComponent2"):
                opp_val = getattr(value, "adlrecurs_AbstractComponent2", None)
                setattr(value, "adlrecurs_AbstractComponent2", self)

class adlrecurs_Attribute:

    def __init__(self, name: str, value: str, adlrecurs_Attribute: "adlrecurs_Attributes" = None):
        self.name = name
        self.value = value
        self.adlrecurs_Attribute = adlrecurs_Attribute
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def adlrecurs_Attribute(self):
        return self.__adlrecurs_Attribute

    @adlrecurs_Attribute.setter
    def adlrecurs_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecurs_Attribute__adlrecurs_Attribute", None)
        self.__adlrecurs_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlrecurs_Attributes15"):
                opp_val = getattr(old_value, "adlrecurs_Attributes15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlrecurs_Attributes15"):
                opp_val = getattr(value, "adlrecurs_Attributes15", None)
                if opp_val is None:
                    setattr(value, "adlrecurs_Attributes15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class adlrecurs_Item(NamedElement):

    pass
class adlrecurs_Binding(NamedElement):

    pass
class adlrecurs_Component(AbstractComponent, NamedElement):

    pass
class adlrecurs_Interface(NamedElement):

    pass
class adlrecurs_Provided(Type):

    pass
class adlrecurs_Content:

    def __init__(self, class_: str, language: str, adlrecurs_Content: "adlrecurs_AbstractComponent" = None):
        self.class_ = class_
        self.language = language
        self.adlrecurs_Content = adlrecurs_Content
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def adlrecurs_Content(self):
        return self.__adlrecurs_Content

    @adlrecurs_Content.setter
    def adlrecurs_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecurs_Content__adlrecurs_Content", None)
        self.__adlrecurs_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlrecurs_AbstractComponent"):
                opp_val = getattr(old_value, "adlrecurs_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "adlrecurs_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlrecurs_AbstractComponent"):
                opp_val = getattr(value, "adlrecurs_AbstractComponent", None)
                setattr(value, "adlrecurs_AbstractComponent", self)

class adlrecurs_AbstractComponent(ABC):

    pass