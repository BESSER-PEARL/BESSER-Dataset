from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class adl200_Interface(ABC):

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

class Interface:

    pass
class adl200_Provided(Interface):

    pass
class adl200_Required(Interface):

    pass
class adl200_Content:

    def __init__(self, expression: str, language: str, adl200_Content: "adl200_Component" = None, adl200_Content9: "adl200_Component" = None):
        self.expression = expression
        self.language = language
        self.adl200_Content = adl200_Content
        self.adl200_Content9 = adl200_Content9
        
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
    def adl200_Content9(self):
        return self.__adl200_Content9

    @adl200_Content9.setter
    def adl200_Content9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Content__adl200_Content9", None)
        self.__adl200_Content9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl200_Component10"):
                opp_val = getattr(old_value, "adl200_Component10", None)
                if opp_val == self:
                    setattr(old_value, "adl200_Component10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl200_Component10"):
                opp_val = getattr(value, "adl200_Component10", None)
                setattr(value, "adl200_Component10", self)

    @property
    def adl200_Content(self):
        return self.__adl200_Content

    @adl200_Content.setter
    def adl200_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Content__adl200_Content", None)
        self.__adl200_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl200_Component"):
                opp_val = getattr(old_value, "adl200_Component", None)
                if opp_val == self:
                    setattr(old_value, "adl200_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl200_Component"):
                opp_val = getattr(value, "adl200_Component", None)
                setattr(value, "adl200_Component", self)

class adl200_Component:

    def __init__(self, name: str, adl200_Component: "adl200_Content" = None, adl200_Component2: set["adl200_Required"] = None, adl200_Component4: set["adl200_Provided"] = None, adl200_Component7: "adl200_Component" = None, adl200_Component5: set["adl200_Component"] = None, adl200_Component10: "adl200_Content" = None):
        self.name = name
        self.adl200_Component = adl200_Component
        self.adl200_Component2 = adl200_Component2 if adl200_Component2 is not None else set()
        self.adl200_Component4 = adl200_Component4 if adl200_Component4 is not None else set()
        self.adl200_Component7 = adl200_Component7
        self.adl200_Component5 = adl200_Component5 if adl200_Component5 is not None else set()
        self.adl200_Component10 = adl200_Component10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl200_Component4(self):
        return self.__adl200_Component4

    @adl200_Component4.setter
    def adl200_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component4", None)
        self.__adl200_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl200_Provided"):
                    opp_val = getattr(item, "adl200_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl200_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl200_Provided"):
                    opp_val = getattr(item, "adl200_Provided", None)
                    
                    setattr(item, "adl200_Provided", self)
                    

    @property
    def adl200_Component5(self):
        return self.__adl200_Component5

    @adl200_Component5.setter
    def adl200_Component5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component5", None)
        self.__adl200_Component5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl200_Component7"):
                    opp_val = getattr(item, "adl200_Component7", None)
                    
                    if opp_val == self:
                        setattr(item, "adl200_Component7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl200_Component7"):
                    opp_val = getattr(item, "adl200_Component7", None)
                    
                    setattr(item, "adl200_Component7", self)
                    

    @property
    def adl200_Component(self):
        return self.__adl200_Component

    @adl200_Component.setter
    def adl200_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component", None)
        self.__adl200_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl200_Content"):
                opp_val = getattr(old_value, "adl200_Content", None)
                if opp_val == self:
                    setattr(old_value, "adl200_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl200_Content"):
                opp_val = getattr(value, "adl200_Content", None)
                setattr(value, "adl200_Content", self)

    @property
    def adl200_Component7(self):
        return self.__adl200_Component7

    @adl200_Component7.setter
    def adl200_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component7", None)
        self.__adl200_Component7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl200_Component5"):
                opp_val = getattr(old_value, "adl200_Component5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl200_Component5"):
                opp_val = getattr(value, "adl200_Component5", None)
                if opp_val is None:
                    setattr(value, "adl200_Component5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl200_Component10(self):
        return self.__adl200_Component10

    @adl200_Component10.setter
    def adl200_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component10", None)
        self.__adl200_Component10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl200_Content9"):
                opp_val = getattr(old_value, "adl200_Content9", None)
                if opp_val == self:
                    setattr(old_value, "adl200_Content9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl200_Content9"):
                opp_val = getattr(value, "adl200_Content9", None)
                setattr(value, "adl200_Content9", self)

    @property
    def adl200_Component2(self):
        return self.__adl200_Component2

    @adl200_Component2.setter
    def adl200_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl200_Component__adl200_Component2", None)
        self.__adl200_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl200_Required"):
                    opp_val = getattr(item, "adl200_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl200_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl200_Required"):
                    opp_val = getattr(item, "adl200_Required", None)
                    
                    setattr(item, "adl200_Required", self)
                    
