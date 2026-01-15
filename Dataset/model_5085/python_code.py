from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class fragdial_Attribute:

    def __init__(self, name: str, value: str, fragdial_Attribute: "fragdial_Attributes" = None):
        self.name = name
        self.value = value
        self.fragdial_Attribute = fragdial_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fragdial_Attribute(self):
        return self.__fragdial_Attribute

    @fragdial_Attribute.setter
    def fragdial_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Attribute__fragdial_Attribute", None)
        self.__fragdial_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Attributes26"):
                opp_val = getattr(old_value, "fragdial_Attributes26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Attributes26"):
                opp_val = getattr(value, "fragdial_Attributes26", None)
                if opp_val is None:
                    setattr(value, "fragdial_Attributes26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fragdial_Ldflag:

    def __init__(self, value: str, fragdial_Ldflag: "fragdial_Content" = None):
        self.value = value
        self.fragdial_Ldflag = fragdial_Ldflag
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fragdial_Ldflag(self):
        return self.__fragdial_Ldflag

    @fragdial_Ldflag.setter
    def fragdial_Ldflag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Ldflag__fragdial_Ldflag", None)
        self.__fragdial_Ldflag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Content24"):
                opp_val = getattr(old_value, "fragdial_Content24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Content24"):
                opp_val = getattr(value, "fragdial_Content24", None)
                if opp_val is None:
                    setattr(value, "fragdial_Content24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fragdial_Include:

    def __init__(self, file: str, fragdial_Include: "fragdial_Content" = None):
        self.file = file
        self.fragdial_Include = fragdial_Include
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def fragdial_Include(self):
        return self.__fragdial_Include

    @fragdial_Include.setter
    def fragdial_Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Include__fragdial_Include", None)
        self.__fragdial_Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Content22"):
                opp_val = getattr(old_value, "fragdial_Content22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Content22"):
                opp_val = getattr(value, "fragdial_Content22", None)
                if opp_val is None:
                    setattr(value, "fragdial_Content22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractComponent:

    pass
class fragdial_Component2(AbstractComponent):

    pass
class fragdial_Component1(AbstractComponent):

    pass
class fragdial_Component3(AbstractComponent):

    pass
class fragdial_Component(AbstractComponent):

    pass
class fragdial_Interface(ABC):

    def __init__(self, name: str, signature: str, contingency: str, cardinality: str, startProperty: str, fragdial_Interface: set["fragdial_Binding"] = None, fragdial_Interface14: "fragdial_Binding" = None, fragdial_Interface17: "fragdial_Binding" = None):
        self.name = name
        self.signature = signature
        self.contingency = contingency
        self.cardinality = cardinality
        self.startProperty = startProperty
        self.fragdial_Interface = fragdial_Interface if fragdial_Interface is not None else set()
        self.fragdial_Interface14 = fragdial_Interface14
        self.fragdial_Interface17 = fragdial_Interface17
        
    @property
    def startProperty(self) -> str:
        return self.__startProperty

    @startProperty.setter
    def startProperty(self, startProperty: str):
        self.__startProperty = startProperty

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contingency(self) -> str:
        return self.__contingency

    @contingency.setter
    def contingency(self, contingency: str):
        self.__contingency = contingency

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def fragdial_Interface14(self):
        return self.__fragdial_Interface14

    @fragdial_Interface14.setter
    def fragdial_Interface14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Interface__fragdial_Interface14", None)
        self.__fragdial_Interface14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Binding13"):
                opp_val = getattr(old_value, "fragdial_Binding13", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Binding13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Binding13"):
                opp_val = getattr(value, "fragdial_Binding13", None)
                setattr(value, "fragdial_Binding13", self)

    @property
    def fragdial_Interface17(self):
        return self.__fragdial_Interface17

    @fragdial_Interface17.setter
    def fragdial_Interface17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Interface__fragdial_Interface17", None)
        self.__fragdial_Interface17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Binding16"):
                opp_val = getattr(old_value, "fragdial_Binding16", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Binding16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Binding16"):
                opp_val = getattr(value, "fragdial_Binding16", None)
                setattr(value, "fragdial_Binding16", self)

    @property
    def fragdial_Interface(self):
        return self.__fragdial_Interface

    @fragdial_Interface.setter
    def fragdial_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Interface__fragdial_Interface", None)
        self.__fragdial_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Binding"):
                    opp_val = getattr(item, "fragdial_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Binding"):
                    opp_val = getattr(item, "fragdial_Binding", None)
                    
                    setattr(item, "fragdial_Binding", self)
                    

class fragdial_Provided(Interface):

    pass
class fragdial_Required(Interface):

    pass
class fragdial_Controller:

    def __init__(self, language: str, descriptor: str, fragdial_Controller: "fragdial_AbstractComponent" = None):
        self.language = language
        self.descriptor = descriptor
        self.fragdial_Controller = fragdial_Controller
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

    @property
    def fragdial_Controller(self):
        return self.__fragdial_Controller

    @fragdial_Controller.setter
    def fragdial_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Controller__fragdial_Controller", None)
        self.__fragdial_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_AbstractComponent6"):
                opp_val = getattr(old_value, "fragdial_AbstractComponent6", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_AbstractComponent6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_AbstractComponent6"):
                opp_val = getattr(value, "fragdial_AbstractComponent6", None)
                setattr(value, "fragdial_AbstractComponent6", self)

class fragdial_Output:

    def __init__(self, format: str, fragdial_Output: "fragdial_AbstractComponent" = None):
        self.format = format
        self.fragdial_Output = fragdial_Output
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def fragdial_Output(self):
        return self.__fragdial_Output

    @fragdial_Output.setter
    def fragdial_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Output__fragdial_Output", None)
        self.__fragdial_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_AbstractComponent4"):
                opp_val = getattr(old_value, "fragdial_AbstractComponent4", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_AbstractComponent4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_AbstractComponent4"):
                opp_val = getattr(value, "fragdial_AbstractComponent4", None)
                setattr(value, "fragdial_AbstractComponent4", self)

class fragdial_Attributes:

    def __init__(self, signature: str, fragdial_Attributes: "fragdial_AbstractComponent" = None, fragdial_Attributes26: set["fragdial_Attribute"] = None):
        self.signature = signature
        self.fragdial_Attributes = fragdial_Attributes
        self.fragdial_Attributes26 = fragdial_Attributes26 if fragdial_Attributes26 is not None else set()
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def fragdial_Attributes(self):
        return self.__fragdial_Attributes

    @fragdial_Attributes.setter
    def fragdial_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Attributes__fragdial_Attributes", None)
        self.__fragdial_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_AbstractComponent2"):
                opp_val = getattr(old_value, "fragdial_AbstractComponent2", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_AbstractComponent2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_AbstractComponent2"):
                opp_val = getattr(value, "fragdial_AbstractComponent2", None)
                setattr(value, "fragdial_AbstractComponent2", self)

    @property
    def fragdial_Attributes26(self):
        return self.__fragdial_Attributes26

    @fragdial_Attributes26.setter
    def fragdial_Attributes26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Attributes__fragdial_Attributes26", None)
        self.__fragdial_Attributes26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Attribute"):
                    opp_val = getattr(item, "fragdial_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Attribute"):
                    opp_val = getattr(item, "fragdial_Attribute", None)
                    
                    setattr(item, "fragdial_Attribute", self)
                    

class fragdial_Content:

    def __init__(self, class: str, language: str, fragdial_Content: "fragdial_AbstractComponent" = None, fragdial_Content19: "fragdial_AbstractComponent" = None, fragdial_Content22: set["fragdial_Include"] = None, fragdial_Content24: set["fragdial_Ldflag"] = None):
        self.class = class
        self.language = language
        self.fragdial_Content = fragdial_Content
        self.fragdial_Content19 = fragdial_Content19
        self.fragdial_Content22 = fragdial_Content22 if fragdial_Content22 is not None else set()
        self.fragdial_Content24 = fragdial_Content24 if fragdial_Content24 is not None else set()
        
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
    def fragdial_Content22(self):
        return self.__fragdial_Content22

    @fragdial_Content22.setter
    def fragdial_Content22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Content__fragdial_Content22", None)
        self.__fragdial_Content22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Include"):
                    opp_val = getattr(item, "fragdial_Include", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Include"):
                    opp_val = getattr(item, "fragdial_Include", None)
                    
                    setattr(item, "fragdial_Include", self)
                    

    @property
    def fragdial_Content24(self):
        return self.__fragdial_Content24

    @fragdial_Content24.setter
    def fragdial_Content24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Content__fragdial_Content24", None)
        self.__fragdial_Content24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Ldflag"):
                    opp_val = getattr(item, "fragdial_Ldflag", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Ldflag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Ldflag"):
                    opp_val = getattr(item, "fragdial_Ldflag", None)
                    
                    setattr(item, "fragdial_Ldflag", self)
                    

    @property
    def fragdial_Content(self):
        return self.__fragdial_Content

    @fragdial_Content.setter
    def fragdial_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Content__fragdial_Content", None)
        self.__fragdial_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_AbstractComponent"):
                opp_val = getattr(old_value, "fragdial_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_AbstractComponent"):
                opp_val = getattr(value, "fragdial_AbstractComponent", None)
                setattr(value, "fragdial_AbstractComponent", self)

    @property
    def fragdial_Content19(self):
        return self.__fragdial_Content19

    @fragdial_Content19.setter
    def fragdial_Content19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_Content__fragdial_Content19", None)
        self.__fragdial_Content19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_AbstractComponent20"):
                opp_val = getattr(old_value, "fragdial_AbstractComponent20", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_AbstractComponent20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_AbstractComponent20"):
                opp_val = getattr(value, "fragdial_AbstractComponent20", None)
                setattr(value, "fragdial_AbstractComponent20", self)

class fragdial_AbstractComponent(ABC):

    def __init__(self, name: str, fragdial_AbstractComponent: "fragdial_Content" = None, fragdial_AbstractComponent2: "fragdial_Attributes" = None, fragdial_AbstractComponent4: "fragdial_Output" = None, fragdial_AbstractComponent6: "fragdial_Controller" = None, fragdial_AbstractComponent8: set["fragdial_Required"] = None, fragdial_AbstractComponent10: set["fragdial_Provided"] = None, fragdial_AbstractComponent20: "fragdial_Content" = None):
        self.name = name
        self.fragdial_AbstractComponent = fragdial_AbstractComponent
        self.fragdial_AbstractComponent2 = fragdial_AbstractComponent2
        self.fragdial_AbstractComponent4 = fragdial_AbstractComponent4
        self.fragdial_AbstractComponent6 = fragdial_AbstractComponent6
        self.fragdial_AbstractComponent8 = fragdial_AbstractComponent8 if fragdial_AbstractComponent8 is not None else set()
        self.fragdial_AbstractComponent10 = fragdial_AbstractComponent10 if fragdial_AbstractComponent10 is not None else set()
        self.fragdial_AbstractComponent20 = fragdial_AbstractComponent20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fragdial_AbstractComponent10(self):
        return self.__fragdial_AbstractComponent10

    @fragdial_AbstractComponent10.setter
    def fragdial_AbstractComponent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent10", None)
        self.__fragdial_AbstractComponent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Provided"):
                    opp_val = getattr(item, "fragdial_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Provided"):
                    opp_val = getattr(item, "fragdial_Provided", None)
                    
                    setattr(item, "fragdial_Provided", self)
                    

    @property
    def fragdial_AbstractComponent2(self):
        return self.__fragdial_AbstractComponent2

    @fragdial_AbstractComponent2.setter
    def fragdial_AbstractComponent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent2", None)
        self.__fragdial_AbstractComponent2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Attributes"):
                opp_val = getattr(old_value, "fragdial_Attributes", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Attributes"):
                opp_val = getattr(value, "fragdial_Attributes", None)
                setattr(value, "fragdial_Attributes", self)

    @property
    def fragdial_AbstractComponent6(self):
        return self.__fragdial_AbstractComponent6

    @fragdial_AbstractComponent6.setter
    def fragdial_AbstractComponent6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent6", None)
        self.__fragdial_AbstractComponent6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Controller"):
                opp_val = getattr(old_value, "fragdial_Controller", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Controller"):
                opp_val = getattr(value, "fragdial_Controller", None)
                setattr(value, "fragdial_Controller", self)

    @property
    def fragdial_AbstractComponent20(self):
        return self.__fragdial_AbstractComponent20

    @fragdial_AbstractComponent20.setter
    def fragdial_AbstractComponent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent20", None)
        self.__fragdial_AbstractComponent20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Content19"):
                opp_val = getattr(old_value, "fragdial_Content19", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Content19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Content19"):
                opp_val = getattr(value, "fragdial_Content19", None)
                setattr(value, "fragdial_Content19", self)

    @property
    def fragdial_AbstractComponent4(self):
        return self.__fragdial_AbstractComponent4

    @fragdial_AbstractComponent4.setter
    def fragdial_AbstractComponent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent4", None)
        self.__fragdial_AbstractComponent4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Output"):
                opp_val = getattr(old_value, "fragdial_Output", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Output"):
                opp_val = getattr(value, "fragdial_Output", None)
                setattr(value, "fragdial_Output", self)

    @property
    def fragdial_AbstractComponent8(self):
        return self.__fragdial_AbstractComponent8

    @fragdial_AbstractComponent8.setter
    def fragdial_AbstractComponent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent8", None)
        self.__fragdial_AbstractComponent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fragdial_Required"):
                    opp_val = getattr(item, "fragdial_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "fragdial_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fragdial_Required"):
                    opp_val = getattr(item, "fragdial_Required", None)
                    
                    setattr(item, "fragdial_Required", self)
                    

    @property
    def fragdial_AbstractComponent(self):
        return self.__fragdial_AbstractComponent

    @fragdial_AbstractComponent.setter
    def fragdial_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fragdial_AbstractComponent__fragdial_AbstractComponent", None)
        self.__fragdial_AbstractComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragdial_Content"):
                opp_val = getattr(old_value, "fragdial_Content", None)
                if opp_val == self:
                    setattr(old_value, "fragdial_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragdial_Content"):
                opp_val = getattr(value, "fragdial_Content", None)
                setattr(value, "fragdial_Content", self)

class fragdial_Binding:

    pass