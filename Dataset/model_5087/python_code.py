from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl101_Provided(Interface):

    pass
class adl101_Required(Interface):

    pass
class adl101_Component:

    def __init__(self, name: str, Component: "adl101_Content" = None, adl101_Component: "adl101_Component" = None, adl101_Component8: set["adl101_Component"] = None, adl101_Component11: set["adl101_Required"] = None, adl101_Component13: set["adl101_Provided"] = None, contentParent: "adl101_Content" = None):
        self.name = name
        self.Component = Component
        self.adl101_Component = adl101_Component
        self.adl101_Component8 = adl101_Component8 if adl101_Component8 is not None else set()
        self.adl101_Component11 = adl101_Component11 if adl101_Component11 is not None else set()
        self.adl101_Component13 = adl101_Component13 if adl101_Component13 is not None else set()
        self.contentParent = contentParent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "content"):
                opp_val = getattr(old_value, "content", None)
                if opp_val == self:
                    setattr(old_value, "content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "content"):
                opp_val = getattr(value, "content", None)
                setattr(value, "content", self)

    @property
    def adl101_Component13(self):
        return self.__adl101_Component13

    @adl101_Component13.setter
    def adl101_Component13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__adl101_Component13", None)
        self.__adl101_Component13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl101_Provided"):
                    opp_val = getattr(item, "adl101_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl101_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl101_Provided"):
                    opp_val = getattr(item, "adl101_Provided", None)
                    
                    setattr(item, "adl101_Provided", self)
                    

    @property
    def adl101_Component(self):
        return self.__adl101_Component

    @adl101_Component.setter
    def adl101_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__adl101_Component", None)
        self.__adl101_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl101_Component8"):
                opp_val = getattr(old_value, "adl101_Component8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl101_Component8"):
                opp_val = getattr(value, "adl101_Component8", None)
                if opp_val is None:
                    setattr(value, "adl101_Component8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentParent(self):
        return self.__contentParent

    @contentParent.setter
    def contentParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__contentParent", None)
        self.__contentParent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Content"):
                opp_val = getattr(old_value, "Content", None)
                if opp_val == self:
                    setattr(old_value, "Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Content"):
                opp_val = getattr(value, "Content", None)
                setattr(value, "Content", self)

    @property
    def adl101_Component11(self):
        return self.__adl101_Component11

    @adl101_Component11.setter
    def adl101_Component11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__adl101_Component11", None)
        self.__adl101_Component11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl101_Required"):
                    opp_val = getattr(item, "adl101_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl101_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl101_Required"):
                    opp_val = getattr(item, "adl101_Required", None)
                    
                    setattr(item, "adl101_Required", self)
                    

    @property
    def adl101_Component8(self):
        return self.__adl101_Component8

    @adl101_Component8.setter
    def adl101_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Component__adl101_Component8", None)
        self.__adl101_Component8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl101_Component"):
                    opp_val = getattr(item, "adl101_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "adl101_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl101_Component"):
                    opp_val = getattr(item, "adl101_Component", None)
                    
                    setattr(item, "adl101_Component", self)
                    

class adl101_Content:

    def __init__(self, expression: str, language: str, content: "adl101_Component" = None, Content: "adl101_Component" = None):
        self.expression = expression
        self.language = language
        self.content = content
        self.Content = Content
        
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
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Content__content", None)
        self.__content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component"):
                opp_val = getattr(old_value, "Component", None)
                if opp_val == self:
                    setattr(old_value, "Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component"):
                opp_val = getattr(value, "Component", None)
                setattr(value, "Component", self)

    @property
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Content__Content", None)
        self.__Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentParent"):
                opp_val = getattr(old_value, "contentParent", None)
                if opp_val == self:
                    setattr(old_value, "contentParent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentParent"):
                opp_val = getattr(value, "contentParent", None)
                setattr(value, "contentParent", self)

class adl101_Binding:

    pass
class adl101_Interface(ABC):

    def __init__(self, name: str, signature: str, adl101_Interface: set["adl101_Binding"] = None, adl101_Interface3: "adl101_Binding" = None, adl101_Interface6: "adl101_Binding" = None):
        self.name = name
        self.signature = signature
        self.adl101_Interface = adl101_Interface if adl101_Interface is not None else set()
        self.adl101_Interface3 = adl101_Interface3
        self.adl101_Interface6 = adl101_Interface6
        
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
    def adl101_Interface3(self):
        return self.__adl101_Interface3

    @adl101_Interface3.setter
    def adl101_Interface3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Interface__adl101_Interface3", None)
        self.__adl101_Interface3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl101_Binding2"):
                opp_val = getattr(old_value, "adl101_Binding2", None)
                if opp_val == self:
                    setattr(old_value, "adl101_Binding2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl101_Binding2"):
                opp_val = getattr(value, "adl101_Binding2", None)
                setattr(value, "adl101_Binding2", self)

    @property
    def adl101_Interface(self):
        return self.__adl101_Interface

    @adl101_Interface.setter
    def adl101_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Interface__adl101_Interface", None)
        self.__adl101_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl101_Binding"):
                    opp_val = getattr(item, "adl101_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl101_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl101_Binding"):
                    opp_val = getattr(item, "adl101_Binding", None)
                    
                    setattr(item, "adl101_Binding", self)
                    

    @property
    def adl101_Interface6(self):
        return self.__adl101_Interface6

    @adl101_Interface6.setter
    def adl101_Interface6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl101_Interface__adl101_Interface6", None)
        self.__adl101_Interface6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl101_Binding5"):
                opp_val = getattr(old_value, "adl101_Binding5", None)
                if opp_val == self:
                    setattr(old_value, "adl101_Binding5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl101_Binding5"):
                opp_val = getattr(value, "adl101_Binding5", None)
                setattr(value, "adl101_Binding5", self)
