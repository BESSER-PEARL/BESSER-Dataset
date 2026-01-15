from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fragdial101_Attribute:

    def __init__(self, name: str, value: str, fragdial101_Attribute: "fragdial101_Attributes" = None):
        self.name = name
        self.value = value
        self.fragdial101_Attribute = fragdial101_Attribute
        
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
    def fragdial101_Attribute(self):
        return self.__fragdial101_Attribute

    @fragdial101_Attribute.setter
    def fragdial101_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Attribute__fragdial101_Attribute", None)
        self.__fragdial101_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Attributes26"):
                opp_val = getattr(old_value, "fragdial101_Attributes26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Attributes26"):
                opp_val = getattr(value, "fragdial101_Attributes26", None)
                if opp_val is None:
                    setattr(value, "fragdial101_Attributes26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractComponent:

    pass
class fragdial101_Component(AbstractComponent):

    pass
class Interface:

    pass
class fragdial101_Ldflag:

    def __init__(self, value: str, fragdial101_Ldflag: "fragdial101_Content" = None):
        self.value = value
        self.fragdial101_Ldflag = fragdial101_Ldflag
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fragdial101_Ldflag(self):
        return self.__fragdial101_Ldflag

    @fragdial101_Ldflag.setter
    def fragdial101_Ldflag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Ldflag__fragdial101_Ldflag", None)
        self.__fragdial101_Ldflag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Content24"):
                opp_val = getattr(old_value, "fragdial101_Content24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Content24"):
                opp_val = getattr(value, "fragdial101_Content24", None)
                if opp_val is None:
                    setattr(value, "fragdial101_Content24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fragdial101_Include:

    def __init__(self, file: str, fragdial101_Include: "fragdial101_Content" = None):
        self.file = file
        self.fragdial101_Include = fragdial101_Include
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def fragdial101_Include(self):
        return self.__fragdial101_Include

    @fragdial101_Include.setter
    def fragdial101_Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Include__fragdial101_Include", None)
        self.__fragdial101_Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Content22"):
                opp_val = getattr(old_value, "fragdial101_Content22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Content22"):
                opp_val = getattr(value, "fragdial101_Content22", None)
                if opp_val is None:
                    setattr(value, "fragdial101_Content22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fragdial101_Binding:

    pass
class fragdial101_Interface(ABC):

    def __init__(self, name: str, signature: str, contingency: str, cardinality: str, startProperty: str, fragdial101_Interface: set["fragdial101_Binding"] = None, fragdial101_Interface14: "fragdial101_Binding" = None, fragdial101_Interface17: "fragdial101_Binding" = None):
        self.name = name
        self.signature = signature
        self.contingency = contingency
        self.cardinality = cardinality
        self.startProperty = startProperty
        self.fragdial101_Interface = fragdial101_Interface if fragdial101_Interface is not None else set()
        self.fragdial101_Interface14 = fragdial101_Interface14
        self.fragdial101_Interface17 = fragdial101_Interface17
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startProperty(self) -> str:
        return self.__startProperty

    @startProperty.setter
    def startProperty(self, startProperty: str):
        self.__startProperty = startProperty

    @property
    def contingency(self) -> str:
        return self.__contingency

    @contingency.setter
    def contingency(self, contingency: str):
        self.__contingency = contingency

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def fragdial101_Interface17(self):
        return self.__fragdial101_Interface17

    @fragdial101_Interface17.setter
    def fragdial101_Interface17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Interface__fragdial101_Interface17", None)
        self.__fragdial101_Interface17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Binding16"):
                opp_val = getattr(old_value, "fragdial101_Binding16", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Binding16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Binding16"):
                opp_val = getattr(value, "fragdial101_Binding16", None)
                setattr(value, "fragdial101_Binding16", self)

    @property
    def fragdial101_Interface(self):
        return self.__fragdial101_Interface

    @fragdial101_Interface.setter
    def fragdial101_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Interface__fragdial101_Interface", None)
        self.__fragdial101_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Binding"):
                    opp_val = getattr(item, "fragdial101_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Binding"):
                    opp_val = getattr(item, "fragdial101_Binding", None)
                    
                    setattr(item, "fragdial101_Binding", self)
                    

    @property
    def fragdial101_Interface14(self):
        return self.__fragdial101_Interface14

    @fragdial101_Interface14.setter
    def fragdial101_Interface14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Interface__fragdial101_Interface14", None)
        self.__fragdial101_Interface14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Binding13"):
                opp_val = getattr(old_value, "fragdial101_Binding13", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Binding13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Binding13"):
                opp_val = getattr(value, "fragdial101_Binding13", None)
                setattr(value, "fragdial101_Binding13", self)

class fragdial101_Provided(Interface):

    pass
class fragdial101_Required(Interface):

    pass
class fragdial101_Controller:

    def __init__(self, language: str, descriptor: str, fragdial101_Controller: "fragdial101_AbstractComponent" = None):
        self.language = language
        self.descriptor = descriptor
        self.fragdial101_Controller = fragdial101_Controller
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def fragdial101_Controller(self):
        return self.__fragdial101_Controller

    @fragdial101_Controller.setter
    def fragdial101_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Controller__fragdial101_Controller", None)
        self.__fragdial101_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_AbstractComponent6"):
                opp_val = getattr(old_value, "fragdial101_AbstractComponent6", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_AbstractComponent6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_AbstractComponent6"):
                opp_val = getattr(value, "fragdial101_AbstractComponent6", None)
                setattr(value, "fragdial101_AbstractComponent6", self)

class fragdial101_Output:

    def __init__(self, format: str, fragdial101_Output: "fragdial101_AbstractComponent" = None):
        self.format = format
        self.fragdial101_Output = fragdial101_Output
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def fragdial101_Output(self):
        return self.__fragdial101_Output

    @fragdial101_Output.setter
    def fragdial101_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Output__fragdial101_Output", None)
        self.__fragdial101_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_AbstractComponent4"):
                opp_val = getattr(old_value, "fragdial101_AbstractComponent4", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_AbstractComponent4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_AbstractComponent4"):
                opp_val = getattr(value, "fragdial101_AbstractComponent4", None)
                setattr(value, "fragdial101_AbstractComponent4", self)

class fragdial101_Attributes:

    def __init__(self, signature: str, fragdial101_Attributes: "fragdial101_AbstractComponent" = None, fragdial101_Attributes26: set["fragdial101_Attribute"] = None):
        self.signature = signature
        self.fragdial101_Attributes = fragdial101_Attributes
        self.fragdial101_Attributes26 = fragdial101_Attributes26 if fragdial101_Attributes26 is not None else set()
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def fragdial101_Attributes(self):
        return self.__fragdial101_Attributes

    @fragdial101_Attributes.setter
    def fragdial101_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Attributes__fragdial101_Attributes", None)
        self.__fragdial101_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_AbstractComponent2"):
                opp_val = getattr(old_value, "fragdial101_AbstractComponent2", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_AbstractComponent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_AbstractComponent2"):
                opp_val = getattr(value, "fragdial101_AbstractComponent2", None)
                setattr(value, "fragdial101_AbstractComponent2", self)

    @property
    def fragdial101_Attributes26(self):
        return self.__fragdial101_Attributes26

    @fragdial101_Attributes26.setter
    def fragdial101_Attributes26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Attributes__fragdial101_Attributes26", None)
        self.__fragdial101_Attributes26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Attribute"):
                    opp_val = getattr(item, "fragdial101_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Attribute"):
                    opp_val = getattr(item, "fragdial101_Attribute", None)
                    
                    setattr(item, "fragdial101_Attribute", self)
                    

class fragdial101_Content:

    def __init__(self, class: str, language: str, fragdial101_Content: "fragdial101_AbstractComponent" = None, fragdial101_Content19: "fragdial101_AbstractComponent" = None, fragdial101_Content22: set["fragdial101_Include"] = None, fragdial101_Content24: set["fragdial101_Ldflag"] = None):
        self.class = class
        self.language = language
        self.fragdial101_Content = fragdial101_Content
        self.fragdial101_Content19 = fragdial101_Content19
        self.fragdial101_Content22 = fragdial101_Content22 if fragdial101_Content22 is not None else set()
        self.fragdial101_Content24 = fragdial101_Content24 if fragdial101_Content24 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def fragdial101_Content24(self):
        return self.__fragdial101_Content24

    @fragdial101_Content24.setter
    def fragdial101_Content24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Content__fragdial101_Content24", None)
        self.__fragdial101_Content24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Ldflag"):
                    opp_val = getattr(item, "fragdial101_Ldflag", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Ldflag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Ldflag"):
                    opp_val = getattr(item, "fragdial101_Ldflag", None)
                    
                    setattr(item, "fragdial101_Ldflag", self)
                    

    @property
    def fragdial101_Content(self):
        return self.__fragdial101_Content

    @fragdial101_Content.setter
    def fragdial101_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Content__fragdial101_Content", None)
        self.__fragdial101_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_AbstractComponent"):
                opp_val = getattr(old_value, "fragdial101_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_AbstractComponent"):
                opp_val = getattr(value, "fragdial101_AbstractComponent", None)
                setattr(value, "fragdial101_AbstractComponent", self)

    @property
    def fragdial101_Content22(self):
        return self.__fragdial101_Content22

    @fragdial101_Content22.setter
    def fragdial101_Content22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Content__fragdial101_Content22", None)
        self.__fragdial101_Content22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Include"):
                    opp_val = getattr(item, "fragdial101_Include", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Include"):
                    opp_val = getattr(item, "fragdial101_Include", None)
                    
                    setattr(item, "fragdial101_Include", self)
                    

    @property
    def fragdial101_Content19(self):
        return self.__fragdial101_Content19

    @fragdial101_Content19.setter
    def fragdial101_Content19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_Content__fragdial101_Content19", None)
        self.__fragdial101_Content19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_AbstractComponent20"):
                opp_val = getattr(old_value, "fragdial101_AbstractComponent20", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_AbstractComponent20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_AbstractComponent20"):
                opp_val = getattr(value, "fragdial101_AbstractComponent20", None)
                setattr(value, "fragdial101_AbstractComponent20", self)

class fragdial101_AbstractComponent(ABC):

    def __init__(self, name: str, fragdial101_AbstractComponent2: "fragdial101_Attributes" = None, fragdial101_AbstractComponent4: "fragdial101_Output" = None, fragdial101_AbstractComponent6: "fragdial101_Controller" = None, fragdial101_AbstractComponent8: set["fragdial101_Required"] = None, fragdial101_AbstractComponent10: set["fragdial101_Provided"] = None, fragdial101_AbstractComponent20: "fragdial101_Content" = None, fragdial101_AbstractComponent: "fragdial101_Content" = None):
        self.name = name
        self.fragdial101_AbstractComponent2 = fragdial101_AbstractComponent2
        self.fragdial101_AbstractComponent4 = fragdial101_AbstractComponent4
        self.fragdial101_AbstractComponent6 = fragdial101_AbstractComponent6
        self.fragdial101_AbstractComponent8 = fragdial101_AbstractComponent8 if fragdial101_AbstractComponent8 is not None else set()
        self.fragdial101_AbstractComponent10 = fragdial101_AbstractComponent10 if fragdial101_AbstractComponent10 is not None else set()
        self.fragdial101_AbstractComponent20 = fragdial101_AbstractComponent20
        self.fragdial101_AbstractComponent = fragdial101_AbstractComponent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fragdial101_AbstractComponent(self):
        return self.__fragdial101_AbstractComponent

    @fragdial101_AbstractComponent.setter
    def fragdial101_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent", None)
        self.__fragdial101_AbstractComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Content"):
                opp_val = getattr(old_value, "fragdial101_Content", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Content"):
                opp_val = getattr(value, "fragdial101_Content", None)
                setattr(value, "fragdial101_Content", self)

    @property
    def fragdial101_AbstractComponent6(self):
        return self.__fragdial101_AbstractComponent6

    @fragdial101_AbstractComponent6.setter
    def fragdial101_AbstractComponent6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent6", None)
        self.__fragdial101_AbstractComponent6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Controller"):
                opp_val = getattr(old_value, "fragdial101_Controller", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Controller"):
                opp_val = getattr(value, "fragdial101_Controller", None)
                setattr(value, "fragdial101_Controller", self)

    @property
    def fragdial101_AbstractComponent4(self):
        return self.__fragdial101_AbstractComponent4

    @fragdial101_AbstractComponent4.setter
    def fragdial101_AbstractComponent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent4", None)
        self.__fragdial101_AbstractComponent4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Output"):
                opp_val = getattr(old_value, "fragdial101_Output", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Output"):
                opp_val = getattr(value, "fragdial101_Output", None)
                setattr(value, "fragdial101_Output", self)

    @property
    def fragdial101_AbstractComponent10(self):
        return self.__fragdial101_AbstractComponent10

    @fragdial101_AbstractComponent10.setter
    def fragdial101_AbstractComponent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent10", None)
        self.__fragdial101_AbstractComponent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Provided"):
                    opp_val = getattr(item, "fragdial101_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Provided"):
                    opp_val = getattr(item, "fragdial101_Provided", None)
                    
                    setattr(item, "fragdial101_Provided", self)
                    

    @property
    def fragdial101_AbstractComponent20(self):
        return self.__fragdial101_AbstractComponent20

    @fragdial101_AbstractComponent20.setter
    def fragdial101_AbstractComponent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent20", None)
        self.__fragdial101_AbstractComponent20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Content19"):
                opp_val = getattr(old_value, "fragdial101_Content19", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Content19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Content19"):
                opp_val = getattr(value, "fragdial101_Content19", None)
                setattr(value, "fragdial101_Content19", self)

    @property
    def fragdial101_AbstractComponent8(self):
        return self.__fragdial101_AbstractComponent8

    @fragdial101_AbstractComponent8.setter
    def fragdial101_AbstractComponent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent8", None)
        self.__fragdial101_AbstractComponent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial101_Required"):
                    opp_val = getattr(item, "fragdial101_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial101_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial101_Required"):
                    opp_val = getattr(item, "fragdial101_Required", None)
                    
                    setattr(item, "fragdial101_Required", self)
                    

    @property
    def fragdial101_AbstractComponent2(self):
        return self.__fragdial101_AbstractComponent2

    @fragdial101_AbstractComponent2.setter
    def fragdial101_AbstractComponent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial101_AbstractComponent__fragdial101_AbstractComponent2", None)
        self.__fragdial101_AbstractComponent2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial101_Attributes"):
                opp_val = getattr(old_value, "fragdial101_Attributes", None)
                if opp_val == self:
                    setattr(old_value, "fragdial101_Attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial101_Attributes"):
                opp_val = getattr(value, "fragdial101_Attributes", None)
                setattr(value, "fragdial101_Attributes", self)
