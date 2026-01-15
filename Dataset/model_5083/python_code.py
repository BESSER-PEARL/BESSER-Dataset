from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractComponent:

    pass
class adlold_Component(AbstractComponent):

    pass
class Interface:

    pass
class adlold_Provided(Interface):

    pass
class adlold_Binding:

    pass
class adlold_Interface(ABC):

    def __init__(self, name: str, signature: str, adlold_Interface: set["adlold_Binding"] = None, adlold_Interface8: "adlold_Binding" = None, adlold_Interface11: "adlold_Binding" = None):
        self.name = name
        self.signature = signature
        self.adlold_Interface = adlold_Interface if adlold_Interface is not None else set()
        self.adlold_Interface8 = adlold_Interface8
        self.adlold_Interface11 = adlold_Interface11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def adlold_Interface8(self):
        return self.__adlold_Interface8

    @adlold_Interface8.setter
    def adlold_Interface8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_Interface__adlold_Interface8", None)
        self.__adlold_Interface8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_Binding7"):
                opp_val = getattr(old_value, "adlold_Binding7", None)
                if opp_val == self:
                    setattr(old_value, "adlold_Binding7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_Binding7"):
                opp_val = getattr(value, "adlold_Binding7", None)
                setattr(value, "adlold_Binding7", self)

    @property
    def adlold_Interface(self):
        return self.__adlold_Interface

    @adlold_Interface.setter
    def adlold_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_Interface__adlold_Interface", None)
        self.__adlold_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlold_Binding"):
                    opp_val = getattr(item, "adlold_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adlold_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlold_Binding"):
                    opp_val = getattr(item, "adlold_Binding", None)
                    
                    setattr(item, "adlold_Binding", self)
                    

    @property
    def adlold_Interface11(self):
        return self.__adlold_Interface11

    @adlold_Interface11.setter
    def adlold_Interface11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_Interface__adlold_Interface11", None)
        self.__adlold_Interface11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_Binding10"):
                opp_val = getattr(old_value, "adlold_Binding10", None)
                if opp_val == self:
                    setattr(old_value, "adlold_Binding10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_Binding10"):
                opp_val = getattr(value, "adlold_Binding10", None)
                setattr(value, "adlold_Binding10", self)

class adlold_Required(Interface):

    pass
class adlold_Content:

    def __init__(self, expression: str, language: str, adlold_Content: "adlold_AbstractComponent" = None, adlold_Content13: "adlold_AbstractComponent" = None):
        self.expression = expression
        self.language = language
        self.adlold_Content = adlold_Content
        self.adlold_Content13 = adlold_Content13
        
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
    def adlold_Content(self):
        return self.__adlold_Content

    @adlold_Content.setter
    def adlold_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_Content__adlold_Content", None)
        self.__adlold_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_AbstractComponent"):
                opp_val = getattr(old_value, "adlold_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "adlold_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_AbstractComponent"):
                opp_val = getattr(value, "adlold_AbstractComponent", None)
                setattr(value, "adlold_AbstractComponent", self)

    @property
    def adlold_Content13(self):
        return self.__adlold_Content13

    @adlold_Content13.setter
    def adlold_Content13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_Content__adlold_Content13", None)
        self.__adlold_Content13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_AbstractComponent14"):
                opp_val = getattr(old_value, "adlold_AbstractComponent14", None)
                if opp_val == self:
                    setattr(old_value, "adlold_AbstractComponent14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_AbstractComponent14"):
                opp_val = getattr(value, "adlold_AbstractComponent14", None)
                setattr(value, "adlold_AbstractComponent14", self)

class adlold_AbstractComponent(ABC):

    def __init__(self, name: str, adlold_AbstractComponent: "adlold_Content" = None, adlold_AbstractComponent2: set["adlold_Required"] = None, adlold_AbstractComponent14: "adlold_Content" = None, adlold_AbstractComponent4: set["adlold_Provided"] = None):
        self.name = name
        self.adlold_AbstractComponent = adlold_AbstractComponent
        self.adlold_AbstractComponent2 = adlold_AbstractComponent2 if adlold_AbstractComponent2 is not None else set()
        self.adlold_AbstractComponent14 = adlold_AbstractComponent14
        self.adlold_AbstractComponent4 = adlold_AbstractComponent4 if adlold_AbstractComponent4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adlold_AbstractComponent(self):
        return self.__adlold_AbstractComponent

    @adlold_AbstractComponent.setter
    def adlold_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_AbstractComponent__adlold_AbstractComponent", None)
        self.__adlold_AbstractComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_Content"):
                opp_val = getattr(old_value, "adlold_Content", None)
                if opp_val == self:
                    setattr(old_value, "adlold_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_Content"):
                opp_val = getattr(value, "adlold_Content", None)
                setattr(value, "adlold_Content", self)

    @property
    def adlold_AbstractComponent14(self):
        return self.__adlold_AbstractComponent14

    @adlold_AbstractComponent14.setter
    def adlold_AbstractComponent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_AbstractComponent__adlold_AbstractComponent14", None)
        self.__adlold_AbstractComponent14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlold_Content13"):
                opp_val = getattr(old_value, "adlold_Content13", None)
                if opp_val == self:
                    setattr(old_value, "adlold_Content13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlold_Content13"):
                opp_val = getattr(value, "adlold_Content13", None)
                setattr(value, "adlold_Content13", self)

    @property
    def adlold_AbstractComponent2(self):
        return self.__adlold_AbstractComponent2

    @adlold_AbstractComponent2.setter
    def adlold_AbstractComponent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_AbstractComponent__adlold_AbstractComponent2", None)
        self.__adlold_AbstractComponent2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlold_Required"):
                    opp_val = getattr(item, "adlold_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adlold_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlold_Required"):
                    opp_val = getattr(item, "adlold_Required", None)
                    
                    setattr(item, "adlold_Required", self)
                    

    @property
    def adlold_AbstractComponent4(self):
        return self.__adlold_AbstractComponent4

    @adlold_AbstractComponent4.setter
    def adlold_AbstractComponent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlold_AbstractComponent__adlold_AbstractComponent4", None)
        self.__adlold_AbstractComponent4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlold_Provided"):
                    opp_val = getattr(item, "adlold_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adlold_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlold_Provided"):
                    opp_val = getattr(item, "adlold_Provided", None)
                    
                    setattr(item, "adlold_Provided", self)
                    
