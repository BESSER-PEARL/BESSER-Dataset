from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractComponent:

    pass
class adl199_AtomicComponent(AbstractComponent):

    pass
class adl199_Component(AbstractComponent):

    pass
class adl199_Binding:

    pass
class adl199_Interface(ABC):

    def __init__(self, name: str, signature: str, adl199_Interface13: "adl199_Binding" = None, adl199_Interface: set["adl199_Binding"] = None, adl199_Interface10: "adl199_Binding" = None):
        self.name = name
        self.signature = signature
        self.adl199_Interface13 = adl199_Interface13
        self.adl199_Interface = adl199_Interface if adl199_Interface is not None else set()
        self.adl199_Interface10 = adl199_Interface10
        
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
    def adl199_Interface(self):
        return self.__adl199_Interface

    @adl199_Interface.setter
    def adl199_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_Interface__adl199_Interface", None)
        self.__adl199_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl199_Binding"):
                    opp_val = getattr(item, "adl199_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl199_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl199_Binding"):
                    opp_val = getattr(item, "adl199_Binding", None)
                    
                    setattr(item, "adl199_Binding", self)
                    

    @property
    def adl199_Interface13(self):
        return self.__adl199_Interface13

    @adl199_Interface13.setter
    def adl199_Interface13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_Interface__adl199_Interface13", None)
        self.__adl199_Interface13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_Binding12"):
                opp_val = getattr(old_value, "adl199_Binding12", None)
                if opp_val == self:
                    setattr(old_value, "adl199_Binding12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_Binding12"):
                opp_val = getattr(value, "adl199_Binding12", None)
                setattr(value, "adl199_Binding12", self)

    @property
    def adl199_Interface10(self):
        return self.__adl199_Interface10

    @adl199_Interface10.setter
    def adl199_Interface10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_Interface__adl199_Interface10", None)
        self.__adl199_Interface10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_Binding9"):
                opp_val = getattr(old_value, "adl199_Binding9", None)
                if opp_val == self:
                    setattr(old_value, "adl199_Binding9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_Binding9"):
                opp_val = getattr(value, "adl199_Binding9", None)
                setattr(value, "adl199_Binding9", self)

class adl199_Content:

    def __init__(self, expression: str, language: str, adl199_Content15: "adl199_AbstractComponent" = None, adl199_Content: "adl199_AbstractComponent" = None):
        self.expression = expression
        self.language = language
        self.adl199_Content15 = adl199_Content15
        self.adl199_Content = adl199_Content
        
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
    def adl199_Content(self):
        return self.__adl199_Content

    @adl199_Content.setter
    def adl199_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_Content__adl199_Content", None)
        self.__adl199_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_AbstractComponent"):
                opp_val = getattr(old_value, "adl199_AbstractComponent", None)
                if opp_val == self:
                    setattr(old_value, "adl199_AbstractComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_AbstractComponent"):
                opp_val = getattr(value, "adl199_AbstractComponent", None)
                setattr(value, "adl199_AbstractComponent", self)

    @property
    def adl199_Content15(self):
        return self.__adl199_Content15

    @adl199_Content15.setter
    def adl199_Content15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_Content__adl199_Content15", None)
        self.__adl199_Content15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_AbstractComponent16"):
                opp_val = getattr(old_value, "adl199_AbstractComponent16", None)
                if opp_val == self:
                    setattr(old_value, "adl199_AbstractComponent16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_AbstractComponent16"):
                opp_val = getattr(value, "adl199_AbstractComponent16", None)
                setattr(value, "adl199_AbstractComponent16", self)

class Interface:

    pass
class adl199_Required(Interface):

    pass
class adl199_Delegation(Interface):

    pass
class adl199_Provided(Interface):

    pass
class adl199_AbstractComponent(ABC):

    def __init__(self, name: str, adl199_AbstractComponent16: "adl199_Content" = None, adl199_AbstractComponent: "adl199_Content" = None, adl199_AbstractComponent2: set["adl199_Required"] = None, adl199_AbstractComponent4: set["adl199_Provided"] = None, adl199_AbstractComponent6: set["adl199_Delegation"] = None, adl199_AbstractComponent18: "adl199_Component" = None):
        self.name = name
        self.adl199_AbstractComponent16 = adl199_AbstractComponent16
        self.adl199_AbstractComponent = adl199_AbstractComponent
        self.adl199_AbstractComponent2 = adl199_AbstractComponent2 if adl199_AbstractComponent2 is not None else set()
        self.adl199_AbstractComponent4 = adl199_AbstractComponent4 if adl199_AbstractComponent4 is not None else set()
        self.adl199_AbstractComponent6 = adl199_AbstractComponent6 if adl199_AbstractComponent6 is not None else set()
        self.adl199_AbstractComponent18 = adl199_AbstractComponent18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl199_AbstractComponent(self):
        return self.__adl199_AbstractComponent

    @adl199_AbstractComponent.setter
    def adl199_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent", None)
        self.__adl199_AbstractComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_Content"):
                opp_val = getattr(old_value, "adl199_Content", None)
                if opp_val == self:
                    setattr(old_value, "adl199_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_Content"):
                opp_val = getattr(value, "adl199_Content", None)
                setattr(value, "adl199_Content", self)

    @property
    def adl199_AbstractComponent18(self):
        return self.__adl199_AbstractComponent18

    @adl199_AbstractComponent18.setter
    def adl199_AbstractComponent18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent18", None)
        self.__adl199_AbstractComponent18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_Component"):
                opp_val = getattr(old_value, "adl199_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_Component"):
                opp_val = getattr(value, "adl199_Component", None)
                if opp_val is None:
                    setattr(value, "adl199_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl199_AbstractComponent4(self):
        return self.__adl199_AbstractComponent4

    @adl199_AbstractComponent4.setter
    def adl199_AbstractComponent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent4", None)
        self.__adl199_AbstractComponent4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl199_Provided"):
                    opp_val = getattr(item, "adl199_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl199_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl199_Provided"):
                    opp_val = getattr(item, "adl199_Provided", None)
                    
                    setattr(item, "adl199_Provided", self)
                    

    @property
    def adl199_AbstractComponent6(self):
        return self.__adl199_AbstractComponent6

    @adl199_AbstractComponent6.setter
    def adl199_AbstractComponent6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent6", None)
        self.__adl199_AbstractComponent6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl199_Delegation"):
                    opp_val = getattr(item, "adl199_Delegation", None)
                    
                    if opp_val == self:
                        setattr(item, "adl199_Delegation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl199_Delegation"):
                    opp_val = getattr(item, "adl199_Delegation", None)
                    
                    setattr(item, "adl199_Delegation", self)
                    

    @property
    def adl199_AbstractComponent2(self):
        return self.__adl199_AbstractComponent2

    @adl199_AbstractComponent2.setter
    def adl199_AbstractComponent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent2", None)
        self.__adl199_AbstractComponent2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl199_Required"):
                    opp_val = getattr(item, "adl199_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl199_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl199_Required"):
                    opp_val = getattr(item, "adl199_Required", None)
                    
                    setattr(item, "adl199_Required", self)
                    

    @property
    def adl199_AbstractComponent16(self):
        return self.__adl199_AbstractComponent16

    @adl199_AbstractComponent16.setter
    def adl199_AbstractComponent16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl199_AbstractComponent__adl199_AbstractComponent16", None)
        self.__adl199_AbstractComponent16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl199_Content15"):
                opp_val = getattr(old_value, "adl199_Content15", None)
                if opp_val == self:
                    setattr(old_value, "adl199_Content15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl199_Content15"):
                opp_val = getattr(value, "adl199_Content15", None)
                setattr(value, "adl199_Content15", self)
