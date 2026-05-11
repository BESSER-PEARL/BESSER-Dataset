from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractComponent:

    pass
class Type:

    pass
class Interface:

    pass
class ktest301_Type(Interface):

    def __init__(self, signature: str, ktest301_Type: set["ktest301_Item"] = None):
        self.signature = signature
        self.ktest301_Type = ktest301_Type if ktest301_Type is not None else set()
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def ktest301_Type(self):
        return self.__ktest301_Type

    @ktest301_Type.setter
    def ktest301_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest301_Type__ktest301_Type", None)
        self.__ktest301_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest301_Item"):
                    opp_val = getattr(item, "ktest301_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest301_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest301_Item"):
                    opp_val = getattr(item, "ktest301_Item", None)
                    
                    setattr(item, "ktest301_Item", self)
                    

class ktest301_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class ktest301_Item(NamedElement):

    pass
class ktest301_Component(AbstractComponent, NamedElement):

    pass
class ktest301_Binding(NamedElement):

    pass
class ktest301_Interface(NamedElement):

    pass
class ktest301_Provided(Type):

    pass
class ktest301_Required(Type):

    pass
class ktest301_Attribute:

    def __init__(self, name: str, value: str, ktest301_Attribute: "ktest301_Attributes" = None):
        self.name = name
        self.value = value
        self.ktest301_Attribute = ktest301_Attribute
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def ktest301_Attribute(self):
        return self.__ktest301_Attribute

    @ktest301_Attribute.setter
    def ktest301_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest301_Attribute__ktest301_Attribute", None)
        self.__ktest301_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest301_Attributes15"):
                opp_val = getattr(old_value, "ktest301_Attributes15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest301_Attributes15"):
                opp_val = getattr(value, "ktest301_Attributes15", None)
                if opp_val is None:
                    setattr(value, "ktest301_Attributes15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ktest301_Attributes:

    def __init__(self, signature: str, ktest301_Attributes: "ktest301_AbstractComponent" = None, ktest301_Attributes15: set["ktest301_Attribute"] = None):
        self.signature = signature
        self.ktest301_Attributes = ktest301_Attributes
        self.ktest301_Attributes15 = ktest301_Attributes15 if ktest301_Attributes15 is not None else set()
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def ktest301_Attributes15(self):
        return self.__ktest301_Attributes15

    @ktest301_Attributes15.setter
    def ktest301_Attributes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest301_Attributes__ktest301_Attributes15", None)
        self.__ktest301_Attributes15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ktest301_Attribute"):
                    opp_val = getattr(item, "ktest301_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ktest301_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ktest301_Attribute"):
                    opp_val = getattr(item, "ktest301_Attribute", None)
                    
                    setattr(item, "ktest301_Attribute", self)
                    

    @property
    def ktest301_Attributes(self):
        return self.__ktest301_Attributes

    @ktest301_Attributes.setter
    def ktest301_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest301_Attributes__ktest301_Attributes", None)
        self.__ktest301_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest301_AbstractComponent2"):
                opp_val = getattr(old_value, "ktest301_AbstractComponent2", None)
                if opp_val == self:
                    setattr(old_value, "ktest301_AbstractComponent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest301_AbstractComponent2"):
                opp_val = getattr(value, "ktest301_AbstractComponent2", None)
                setattr(value, "ktest301_AbstractComponent2", self)

class ktest301_Content:

    def __init__(self, class_: str, language: str, ktest301_Content: "ktest301_AbstractComponent" = None):
        self.class_ = class_
        self.language = language
        self.ktest301_Content = ktest301_Content
        
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
    def ktest301_Content(self):
        return self.__ktest301_Content

    @ktest301_Content.setter
    def ktest301_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest301_Content__ktest301_Content", None)
        self.__ktest301_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest301_AbstractComponent"):
                opp_val = getattr(old_value, "ktest301_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "ktest301_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest301_AbstractComponent"):
                opp_val = getattr(value, "ktest301_AbstractComponent", None)
                setattr(value, "ktest301_AbstractComponent", self)

class ktest301_AbstractComponent(ABC):

    pass