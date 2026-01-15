from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl202_BindingAttributes:

    def __init__(self, name: str, value: str, adl202_BindingAttributes: "adl202_Binding" = None):
        self.name = name
        self.value = value
        self.adl202_BindingAttributes = adl202_BindingAttributes
        
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
    def adl202_BindingAttributes(self):
        return self.__adl202_BindingAttributes

    @adl202_BindingAttributes.setter
    def adl202_BindingAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_BindingAttributes__adl202_BindingAttributes", None)
        self.__adl202_BindingAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Binding14"):
                opp_val = getattr(old_value, "adl202_Binding14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Binding14"):
                opp_val = getattr(value, "adl202_Binding14", None)
                if opp_val is None:
                    setattr(value, "adl202_Binding14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adl202_Interface(ABC):

    def __init__(self, signature: str, name: str):
        self.signature = signature
        self.name = name
        
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

class adl202_Binding:

    def __init__(self, name: str, adl202_Binding: "adl202_Component" = None, adl202_Binding11: "adl202_Required" = None, adl202_Binding14: set["adl202_BindingAttributes"] = None, adl202_Binding16: "adl202_Provided" = None, adl202_Binding23: "adl202_Provided" = None):
        self.name = name
        self.adl202_Binding = adl202_Binding
        self.adl202_Binding11 = adl202_Binding11
        self.adl202_Binding14 = adl202_Binding14 if adl202_Binding14 is not None else set()
        self.adl202_Binding16 = adl202_Binding16
        self.adl202_Binding23 = adl202_Binding23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl202_Binding(self):
        return self.__adl202_Binding

    @adl202_Binding.setter
    def adl202_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Binding__adl202_Binding", None)
        self.__adl202_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Component6"):
                opp_val = getattr(old_value, "adl202_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Component6"):
                opp_val = getattr(value, "adl202_Component6", None)
                if opp_val is None:
                    setattr(value, "adl202_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl202_Binding14(self):
        return self.__adl202_Binding14

    @adl202_Binding14.setter
    def adl202_Binding14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Binding__adl202_Binding14", None)
        self.__adl202_Binding14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl202_BindingAttributes"):
                    opp_val = getattr(item, "adl202_BindingAttributes", None)
                    
                    if opp_val == self:
                        setattr(item, "adl202_BindingAttributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl202_BindingAttributes"):
                    opp_val = getattr(item, "adl202_BindingAttributes", None)
                    
                    setattr(item, "adl202_BindingAttributes", self)
                    

    @property
    def adl202_Binding11(self):
        return self.__adl202_Binding11

    @adl202_Binding11.setter
    def adl202_Binding11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Binding__adl202_Binding11", None)
        self.__adl202_Binding11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Required12"):
                opp_val = getattr(old_value, "adl202_Required12", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Required12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Required12"):
                opp_val = getattr(value, "adl202_Required12", None)
                setattr(value, "adl202_Required12", self)

    @property
    def adl202_Binding23(self):
        return self.__adl202_Binding23

    @adl202_Binding23.setter
    def adl202_Binding23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Binding__adl202_Binding23", None)
        self.__adl202_Binding23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Provided22"):
                opp_val = getattr(old_value, "adl202_Provided22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Provided22"):
                opp_val = getattr(value, "adl202_Provided22", None)
                if opp_val is None:
                    setattr(value, "adl202_Provided22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl202_Binding16(self):
        return self.__adl202_Binding16

    @adl202_Binding16.setter
    def adl202_Binding16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Binding__adl202_Binding16", None)
        self.__adl202_Binding16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Provided17"):
                opp_val = getattr(old_value, "adl202_Provided17", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Provided17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Provided17"):
                opp_val = getattr(value, "adl202_Provided17", None)
                setattr(value, "adl202_Provided17", self)

class adl202_Provided(Interface):

    pass
class adl202_Required(Interface):

    pass
class adl202_Content:

    def __init__(self, expression: str, language: str, adl202_Content: "adl202_Component" = None, adl202_Content19: "adl202_Component" = None):
        self.expression = expression
        self.language = language
        self.adl202_Content = adl202_Content
        self.adl202_Content19 = adl202_Content19
        
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
    def adl202_Content19(self):
        return self.__adl202_Content19

    @adl202_Content19.setter
    def adl202_Content19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Content__adl202_Content19", None)
        self.__adl202_Content19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Component20"):
                opp_val = getattr(old_value, "adl202_Component20", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Component20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Component20"):
                opp_val = getattr(value, "adl202_Component20", None)
                setattr(value, "adl202_Component20", self)

    @property
    def adl202_Content(self):
        return self.__adl202_Content

    @adl202_Content.setter
    def adl202_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Content__adl202_Content", None)
        self.__adl202_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Component"):
                opp_val = getattr(old_value, "adl202_Component", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Component"):
                opp_val = getattr(value, "adl202_Component", None)
                setattr(value, "adl202_Component", self)

class adl202_Component:

    def __init__(self, name: str, adl202_Component: "adl202_Content" = None, adl202_Component2: set["adl202_Required"] = None, adl202_Component4: set["adl202_Provided"] = None, adl202_Component6: set["adl202_Binding"] = None, adl202_Component9: "adl202_Component" = None, adl202_Component7: set["adl202_Component"] = None, adl202_Component20: "adl202_Content" = None):
        self.name = name
        self.adl202_Component = adl202_Component
        self.adl202_Component2 = adl202_Component2 if adl202_Component2 is not None else set()
        self.adl202_Component4 = adl202_Component4 if adl202_Component4 is not None else set()
        self.adl202_Component6 = adl202_Component6 if adl202_Component6 is not None else set()
        self.adl202_Component9 = adl202_Component9
        self.adl202_Component7 = adl202_Component7 if adl202_Component7 is not None else set()
        self.adl202_Component20 = adl202_Component20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl202_Component(self):
        return self.__adl202_Component

    @adl202_Component.setter
    def adl202_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component", None)
        self.__adl202_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Content"):
                opp_val = getattr(old_value, "adl202_Content", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Content"):
                opp_val = getattr(value, "adl202_Content", None)
                setattr(value, "adl202_Content", self)

    @property
    def adl202_Component9(self):
        return self.__adl202_Component9

    @adl202_Component9.setter
    def adl202_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component9", None)
        self.__adl202_Component9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Component7"):
                opp_val = getattr(old_value, "adl202_Component7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Component7"):
                opp_val = getattr(value, "adl202_Component7", None)
                if opp_val is None:
                    setattr(value, "adl202_Component7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl202_Component4(self):
        return self.__adl202_Component4

    @adl202_Component4.setter
    def adl202_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component4", None)
        self.__adl202_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl202_Provided"):
                    opp_val = getattr(item, "adl202_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl202_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl202_Provided"):
                    opp_val = getattr(item, "adl202_Provided", None)
                    
                    setattr(item, "adl202_Provided", self)
                    

    @property
    def adl202_Component2(self):
        return self.__adl202_Component2

    @adl202_Component2.setter
    def adl202_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component2", None)
        self.__adl202_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl202_Required"):
                    opp_val = getattr(item, "adl202_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl202_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl202_Required"):
                    opp_val = getattr(item, "adl202_Required", None)
                    
                    setattr(item, "adl202_Required", self)
                    

    @property
    def adl202_Component7(self):
        return self.__adl202_Component7

    @adl202_Component7.setter
    def adl202_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component7", None)
        self.__adl202_Component7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl202_Component9"):
                    opp_val = getattr(item, "adl202_Component9", None)
                    
                    if opp_val == self:
                        setattr(item, "adl202_Component9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl202_Component9"):
                    opp_val = getattr(item, "adl202_Component9", None)
                    
                    setattr(item, "adl202_Component9", self)
                    

    @property
    def adl202_Component20(self):
        return self.__adl202_Component20

    @adl202_Component20.setter
    def adl202_Component20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component20", None)
        self.__adl202_Component20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl202_Content19"):
                opp_val = getattr(old_value, "adl202_Content19", None)
                if opp_val == self:
                    setattr(old_value, "adl202_Content19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl202_Content19"):
                opp_val = getattr(value, "adl202_Content19", None)
                setattr(value, "adl202_Content19", self)

    @property
    def adl202_Component6(self):
        return self.__adl202_Component6

    @adl202_Component6.setter
    def adl202_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl202_Component__adl202_Component6", None)
        self.__adl202_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl202_Binding"):
                    opp_val = getattr(item, "adl202_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl202_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl202_Binding"):
                    opp_val = getattr(item, "adl202_Binding", None)
                    
                    setattr(item, "adl202_Binding", self)
                    
