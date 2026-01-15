from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl201_BindingAttributes:

    def __init__(self, name: str, value: str, adl201_BindingAttributes: "adl201_Binding" = None):
        self.name = name
        self.value = value
        self.adl201_BindingAttributes = adl201_BindingAttributes
        
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
    def adl201_BindingAttributes(self):
        return self.__adl201_BindingAttributes

    @adl201_BindingAttributes.setter
    def adl201_BindingAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_BindingAttributes__adl201_BindingAttributes", None)
        self.__adl201_BindingAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Binding14"):
                opp_val = getattr(old_value, "adl201_Binding14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Binding14"):
                opp_val = getattr(value, "adl201_Binding14", None)
                if opp_val is None:
                    setattr(value, "adl201_Binding14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adl201_Component:

    def __init__(self, name: str, adl201_Component: "adl201_Content" = None, adl201_Component2: set["adl201_Required"] = None, adl201_Component4: set["adl201_Provided"] = None, adl201_Component6: set["adl201_Binding"] = None, adl201_Component9: "adl201_Component" = None, adl201_Component7: set["adl201_Component"] = None, adl201_Component20: "adl201_Content" = None):
        self.name = name
        self.adl201_Component = adl201_Component
        self.adl201_Component2 = adl201_Component2 if adl201_Component2 is not None else set()
        self.adl201_Component4 = adl201_Component4 if adl201_Component4 is not None else set()
        self.adl201_Component6 = adl201_Component6 if adl201_Component6 is not None else set()
        self.adl201_Component9 = adl201_Component9
        self.adl201_Component7 = adl201_Component7 if adl201_Component7 is not None else set()
        self.adl201_Component20 = adl201_Component20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl201_Component6(self):
        return self.__adl201_Component6

    @adl201_Component6.setter
    def adl201_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component6", None)
        self.__adl201_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl201_Binding"):
                    opp_val = getattr(item, "adl201_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl201_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl201_Binding"):
                    opp_val = getattr(item, "adl201_Binding", None)
                    
                    setattr(item, "adl201_Binding", self)
                    

    @property
    def adl201_Component7(self):
        return self.__adl201_Component7

    @adl201_Component7.setter
    def adl201_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component7", None)
        self.__adl201_Component7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl201_Component9"):
                    opp_val = getattr(item, "adl201_Component9", None)
                    
                    if opp_val == self:
                        setattr(item, "adl201_Component9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl201_Component9"):
                    opp_val = getattr(item, "adl201_Component9", None)
                    
                    setattr(item, "adl201_Component9", self)
                    

    @property
    def adl201_Component(self):
        return self.__adl201_Component

    @adl201_Component.setter
    def adl201_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component", None)
        self.__adl201_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Content"):
                opp_val = getattr(old_value, "adl201_Content", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Content"):
                opp_val = getattr(value, "adl201_Content", None)
                setattr(value, "adl201_Content", self)

    @property
    def adl201_Component9(self):
        return self.__adl201_Component9

    @adl201_Component9.setter
    def adl201_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component9", None)
        self.__adl201_Component9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Component7"):
                opp_val = getattr(old_value, "adl201_Component7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Component7"):
                opp_val = getattr(value, "adl201_Component7", None)
                if opp_val is None:
                    setattr(value, "adl201_Component7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl201_Component4(self):
        return self.__adl201_Component4

    @adl201_Component4.setter
    def adl201_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component4", None)
        self.__adl201_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl201_Provided"):
                    opp_val = getattr(item, "adl201_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl201_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl201_Provided"):
                    opp_val = getattr(item, "adl201_Provided", None)
                    
                    setattr(item, "adl201_Provided", self)
                    

    @property
    def adl201_Component20(self):
        return self.__adl201_Component20

    @adl201_Component20.setter
    def adl201_Component20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component20", None)
        self.__adl201_Component20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Content19"):
                opp_val = getattr(old_value, "adl201_Content19", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Content19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Content19"):
                opp_val = getattr(value, "adl201_Content19", None)
                setattr(value, "adl201_Content19", self)

    @property
    def adl201_Component2(self):
        return self.__adl201_Component2

    @adl201_Component2.setter
    def adl201_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Component__adl201_Component2", None)
        self.__adl201_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl201_Required"):
                    opp_val = getattr(item, "adl201_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl201_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl201_Required"):
                    opp_val = getattr(item, "adl201_Required", None)
                    
                    setattr(item, "adl201_Required", self)
                    

class adl201_Interface(ABC):

    def __init__(self, name: str, signature: str):
        self.name = name
        self.signature = signature
        
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

class adl201_Binding:

    def __init__(self, name: str, adl201_Binding: "adl201_Component" = None, adl201_Binding23: "adl201_Provided" = None, adl201_Binding11: "adl201_Required" = None, adl201_Binding14: set["adl201_BindingAttributes"] = None, adl201_Binding16: "adl201_Provided" = None):
        self.name = name
        self.adl201_Binding = adl201_Binding
        self.adl201_Binding23 = adl201_Binding23
        self.adl201_Binding11 = adl201_Binding11
        self.adl201_Binding14 = adl201_Binding14 if adl201_Binding14 is not None else set()
        self.adl201_Binding16 = adl201_Binding16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl201_Binding(self):
        return self.__adl201_Binding

    @adl201_Binding.setter
    def adl201_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Binding__adl201_Binding", None)
        self.__adl201_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Component6"):
                opp_val = getattr(old_value, "adl201_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Component6"):
                opp_val = getattr(value, "adl201_Component6", None)
                if opp_val is None:
                    setattr(value, "adl201_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl201_Binding16(self):
        return self.__adl201_Binding16

    @adl201_Binding16.setter
    def adl201_Binding16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Binding__adl201_Binding16", None)
        self.__adl201_Binding16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Provided17"):
                opp_val = getattr(old_value, "adl201_Provided17", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Provided17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Provided17"):
                opp_val = getattr(value, "adl201_Provided17", None)
                setattr(value, "adl201_Provided17", self)

    @property
    def adl201_Binding14(self):
        return self.__adl201_Binding14

    @adl201_Binding14.setter
    def adl201_Binding14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Binding__adl201_Binding14", None)
        self.__adl201_Binding14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl201_BindingAttributes"):
                    opp_val = getattr(item, "adl201_BindingAttributes", None)
                    
                    if opp_val == self:
                        setattr(item, "adl201_BindingAttributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl201_BindingAttributes"):
                    opp_val = getattr(item, "adl201_BindingAttributes", None)
                    
                    setattr(item, "adl201_BindingAttributes", self)
                    

    @property
    def adl201_Binding11(self):
        return self.__adl201_Binding11

    @adl201_Binding11.setter
    def adl201_Binding11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Binding__adl201_Binding11", None)
        self.__adl201_Binding11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Required12"):
                opp_val = getattr(old_value, "adl201_Required12", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Required12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Required12"):
                opp_val = getattr(value, "adl201_Required12", None)
                setattr(value, "adl201_Required12", self)

    @property
    def adl201_Binding23(self):
        return self.__adl201_Binding23

    @adl201_Binding23.setter
    def adl201_Binding23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Binding__adl201_Binding23", None)
        self.__adl201_Binding23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Provided22"):
                opp_val = getattr(old_value, "adl201_Provided22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Provided22"):
                opp_val = getattr(value, "adl201_Provided22", None)
                if opp_val is None:
                    setattr(value, "adl201_Provided22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adl201_Provided(Interface):

    pass
class adl201_Required(Interface):

    pass
class adl201_Content:

    def __init__(self, expression: str, language: str, adl201_Content: "adl201_Component" = None, adl201_Content19: "adl201_Component" = None):
        self.expression = expression
        self.language = language
        self.adl201_Content = adl201_Content
        self.adl201_Content19 = adl201_Content19
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def adl201_Content19(self):
        return self.__adl201_Content19

    @adl201_Content19.setter
    def adl201_Content19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Content__adl201_Content19", None)
        self.__adl201_Content19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Component20"):
                opp_val = getattr(old_value, "adl201_Component20", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Component20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Component20"):
                opp_val = getattr(value, "adl201_Component20", None)
                setattr(value, "adl201_Component20", self)

    @property
    def adl201_Content(self):
        return self.__adl201_Content

    @adl201_Content.setter
    def adl201_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl201_Content__adl201_Content", None)
        self.__adl201_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl201_Component"):
                opp_val = getattr(old_value, "adl201_Component", None)
                if opp_val == self:
                    setattr(old_value, "adl201_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl201_Component"):
                opp_val = getattr(value, "adl201_Component", None)
                setattr(value, "adl201_Component", self)
