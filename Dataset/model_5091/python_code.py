from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl203_BindingAttributes:

    def __init__(self, name: str, value: str, adl203_BindingAttributes: "adl203_Binding" = None):
        self.name = name
        self.value = value
        self.adl203_BindingAttributes = adl203_BindingAttributes
        
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
    def adl203_BindingAttributes(self):
        return self.__adl203_BindingAttributes

    @adl203_BindingAttributes.setter
    def adl203_BindingAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_BindingAttributes__adl203_BindingAttributes", None)
        self.__adl203_BindingAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Binding14"):
                opp_val = getattr(old_value, "adl203_Binding14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Binding14"):
                opp_val = getattr(value, "adl203_Binding14", None)
                if opp_val is None:
                    setattr(value, "adl203_Binding14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adl203_Interface(ABC):

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

class adl203_Binding:

    def __init__(self, name: str, adl203_Binding: "adl203_Component" = None, adl203_Binding11: "adl203_Required" = None, adl203_Binding14: set["adl203_BindingAttributes"] = None, adl203_Binding16: "adl203_Provided" = None, adl203_Binding23: "adl203_Provided" = None):
        self.name = name
        self.adl203_Binding = adl203_Binding
        self.adl203_Binding11 = adl203_Binding11
        self.adl203_Binding14 = adl203_Binding14 if adl203_Binding14 is not None else set()
        self.adl203_Binding16 = adl203_Binding16
        self.adl203_Binding23 = adl203_Binding23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl203_Binding11(self):
        return self.__adl203_Binding11

    @adl203_Binding11.setter
    def adl203_Binding11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Binding__adl203_Binding11", None)
        self.__adl203_Binding11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Required12"):
                opp_val = getattr(old_value, "adl203_Required12", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Required12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Required12"):
                opp_val = getattr(value, "adl203_Required12", None)
                setattr(value, "adl203_Required12", self)

    @property
    def adl203_Binding23(self):
        return self.__adl203_Binding23

    @adl203_Binding23.setter
    def adl203_Binding23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Binding__adl203_Binding23", None)
        self.__adl203_Binding23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Provided22"):
                opp_val = getattr(old_value, "adl203_Provided22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Provided22"):
                opp_val = getattr(value, "adl203_Provided22", None)
                if opp_val is None:
                    setattr(value, "adl203_Provided22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl203_Binding14(self):
        return self.__adl203_Binding14

    @adl203_Binding14.setter
    def adl203_Binding14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Binding__adl203_Binding14", None)
        self.__adl203_Binding14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl203_BindingAttributes"):
                    opp_val = getattr(item, "adl203_BindingAttributes", None)
                    
                    if opp_val == self:
                        setattr(item, "adl203_BindingAttributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl203_BindingAttributes"):
                    opp_val = getattr(item, "adl203_BindingAttributes", None)
                    
                    setattr(item, "adl203_BindingAttributes", self)
                    

    @property
    def adl203_Binding(self):
        return self.__adl203_Binding

    @adl203_Binding.setter
    def adl203_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Binding__adl203_Binding", None)
        self.__adl203_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Component6"):
                opp_val = getattr(old_value, "adl203_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Component6"):
                opp_val = getattr(value, "adl203_Component6", None)
                if opp_val is None:
                    setattr(value, "adl203_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl203_Binding16(self):
        return self.__adl203_Binding16

    @adl203_Binding16.setter
    def adl203_Binding16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Binding__adl203_Binding16", None)
        self.__adl203_Binding16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Provided17"):
                opp_val = getattr(old_value, "adl203_Provided17", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Provided17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Provided17"):
                opp_val = getattr(value, "adl203_Provided17", None)
                setattr(value, "adl203_Provided17", self)

class adl203_Provided(Interface):

    pass
class adl203_Required(Interface):

    pass
class adl203_Content:

    def __init__(self, expression: str, language: str, adl203_Content: "adl203_Component" = None, adl203_Content19: "adl203_Component" = None):
        self.expression = expression
        self.language = language
        self.adl203_Content = adl203_Content
        self.adl203_Content19 = adl203_Content19
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def adl203_Content(self):
        return self.__adl203_Content

    @adl203_Content.setter
    def adl203_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Content__adl203_Content", None)
        self.__adl203_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Component"):
                opp_val = getattr(old_value, "adl203_Component", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Component"):
                opp_val = getattr(value, "adl203_Component", None)
                setattr(value, "adl203_Component", self)

    @property
    def adl203_Content19(self):
        return self.__adl203_Content19

    @adl203_Content19.setter
    def adl203_Content19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Content__adl203_Content19", None)
        self.__adl203_Content19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Component20"):
                opp_val = getattr(old_value, "adl203_Component20", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Component20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Component20"):
                opp_val = getattr(value, "adl203_Component20", None)
                setattr(value, "adl203_Component20", self)

class adl203_Component:

    def __init__(self, name: str, adl203_Component: "adl203_Content" = None, adl203_Component2: set["adl203_Required"] = None, adl203_Component4: set["adl203_Provided"] = None, adl203_Component6: set["adl203_Binding"] = None, adl203_Component9: "adl203_Component" = None, adl203_Component20: "adl203_Content" = None, adl203_Component7: set["adl203_Component"] = None):
        self.name = name
        self.adl203_Component = adl203_Component
        self.adl203_Component2 = adl203_Component2 if adl203_Component2 is not None else set()
        self.adl203_Component4 = adl203_Component4 if adl203_Component4 is not None else set()
        self.adl203_Component6 = adl203_Component6 if adl203_Component6 is not None else set()
        self.adl203_Component9 = adl203_Component9
        self.adl203_Component20 = adl203_Component20
        self.adl203_Component7 = adl203_Component7 if adl203_Component7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl203_Component4(self):
        return self.__adl203_Component4

    @adl203_Component4.setter
    def adl203_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component4", None)
        self.__adl203_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl203_Provided"):
                    opp_val = getattr(item, "adl203_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl203_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl203_Provided"):
                    opp_val = getattr(item, "adl203_Provided", None)
                    
                    setattr(item, "adl203_Provided", self)
                    

    @property
    def adl203_Component2(self):
        return self.__adl203_Component2

    @adl203_Component2.setter
    def adl203_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component2", None)
        self.__adl203_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl203_Required"):
                    opp_val = getattr(item, "adl203_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl203_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl203_Required"):
                    opp_val = getattr(item, "adl203_Required", None)
                    
                    setattr(item, "adl203_Required", self)
                    

    @property
    def adl203_Component20(self):
        return self.__adl203_Component20

    @adl203_Component20.setter
    def adl203_Component20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component20", None)
        self.__adl203_Component20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Content19"):
                opp_val = getattr(old_value, "adl203_Content19", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Content19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Content19"):
                opp_val = getattr(value, "adl203_Content19", None)
                setattr(value, "adl203_Content19", self)

    @property
    def adl203_Component(self):
        return self.__adl203_Component

    @adl203_Component.setter
    def adl203_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component", None)
        self.__adl203_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Content"):
                opp_val = getattr(old_value, "adl203_Content", None)
                if opp_val == self:
                    setattr(old_value, "adl203_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Content"):
                opp_val = getattr(value, "adl203_Content", None)
                setattr(value, "adl203_Content", self)

    @property
    def adl203_Component7(self):
        return self.__adl203_Component7

    @adl203_Component7.setter
    def adl203_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component7", None)
        self.__adl203_Component7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl203_Component9"):
                    opp_val = getattr(item, "adl203_Component9", None)
                    
                    if opp_val == self:
                        setattr(item, "adl203_Component9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl203_Component9"):
                    opp_val = getattr(item, "adl203_Component9", None)
                    
                    setattr(item, "adl203_Component9", self)
                    

    @property
    def adl203_Component9(self):
        return self.__adl203_Component9

    @adl203_Component9.setter
    def adl203_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component9", None)
        self.__adl203_Component9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl203_Component7"):
                opp_val = getattr(old_value, "adl203_Component7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl203_Component7"):
                opp_val = getattr(value, "adl203_Component7", None)
                if opp_val is None:
                    setattr(value, "adl203_Component7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl203_Component6(self):
        return self.__adl203_Component6

    @adl203_Component6.setter
    def adl203_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl203_Component__adl203_Component6", None)
        self.__adl203_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl203_Binding"):
                    opp_val = getattr(item, "adl203_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl203_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl203_Binding"):
                    opp_val = getattr(item, "adl203_Binding", None)
                    
                    setattr(item, "adl203_Binding", self)
                    
