from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl401_Provided(Interface):

    pass
class adl401_Required(Interface):

    pass
class adl401_EClass0:

    def __init__(self, EAttribute0: str, adl401_EClass018: "adl401_EClass0" = None, adl401_EClass016: set["adl401_EClass0"] = None, adl401_EClass0: "adl401_Content" = None):
        self.EAttribute0 = EAttribute0
        self.adl401_EClass018 = adl401_EClass018
        self.adl401_EClass016 = adl401_EClass016 if adl401_EClass016 is not None else set()
        self.adl401_EClass0 = adl401_EClass0
        
    @property
    def EAttribute0(self) -> str:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: str):
        self.__EAttribute0 = EAttribute0

    @property
    def adl401_EClass016(self):
        return self.__adl401_EClass016

    @adl401_EClass016.setter
    def adl401_EClass016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_EClass0__adl401_EClass016", None)
        self.__adl401_EClass016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_EClass018"):
                    opp_val = getattr(item, "adl401_EClass018", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_EClass018", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_EClass018"):
                    opp_val = getattr(item, "adl401_EClass018", None)
                    
                    setattr(item, "adl401_EClass018", self)
                    

    @property
    def adl401_EClass0(self):
        return self.__adl401_EClass0

    @adl401_EClass0.setter
    def adl401_EClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_EClass0__adl401_EClass0", None)
        self.__adl401_EClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl401_Content"):
                opp_val = getattr(old_value, "adl401_Content", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl401_Content"):
                opp_val = getattr(value, "adl401_Content", None)
                if opp_val is None:
                    setattr(value, "adl401_Content", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl401_EClass018(self):
        return self.__adl401_EClass018

    @adl401_EClass018.setter
    def adl401_EClass018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_EClass0__adl401_EClass018", None)
        self.__adl401_EClass018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl401_EClass016"):
                opp_val = getattr(old_value, "adl401_EClass016", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl401_EClass016"):
                opp_val = getattr(value, "adl401_EClass016", None)
                if opp_val is None:
                    setattr(value, "adl401_EClass016", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adl401_Binding:

    pass
class adl401_Interface(ABC):

    def __init__(self, name: str, signature: str, adl401_Interface3: "adl401_Binding" = None, adl401_Interface6: "adl401_Binding" = None, adl401_Interface: set["adl401_Binding"] = None):
        self.name = name
        self.signature = signature
        self.adl401_Interface3 = adl401_Interface3
        self.adl401_Interface6 = adl401_Interface6
        self.adl401_Interface = adl401_Interface if adl401_Interface is not None else set()
        
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
    def adl401_Interface6(self):
        return self.__adl401_Interface6

    @adl401_Interface6.setter
    def adl401_Interface6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Interface__adl401_Interface6", None)
        self.__adl401_Interface6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl401_Binding5"):
                opp_val = getattr(old_value, "adl401_Binding5", None)
                if opp_val == self:
                    setattr(old_value, "adl401_Binding5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl401_Binding5"):
                opp_val = getattr(value, "adl401_Binding5", None)
                setattr(value, "adl401_Binding5", self)

    @property
    def adl401_Interface3(self):
        return self.__adl401_Interface3

    @adl401_Interface3.setter
    def adl401_Interface3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Interface__adl401_Interface3", None)
        self.__adl401_Interface3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl401_Binding2"):
                opp_val = getattr(old_value, "adl401_Binding2", None)
                if opp_val == self:
                    setattr(old_value, "adl401_Binding2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl401_Binding2"):
                opp_val = getattr(value, "adl401_Binding2", None)
                setattr(value, "adl401_Binding2", self)

    @property
    def adl401_Interface(self):
        return self.__adl401_Interface

    @adl401_Interface.setter
    def adl401_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Interface__adl401_Interface", None)
        self.__adl401_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_Binding"):
                    opp_val = getattr(item, "adl401_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_Binding"):
                    opp_val = getattr(item, "adl401_Binding", None)
                    
                    setattr(item, "adl401_Binding", self)
                    

class adl401_Component:

    def __init__(self, name: str, Component: "adl401_Content" = None, adl401_Component: "adl401_Component" = None, adl401_Component9: set["adl401_Component"] = None, adl401_Component12: set["adl401_Required"] = None, adl401_Component14: set["adl401_Provided"] = None, contentParent: "adl401_Content" = None):
        self.name = name
        self.Component = Component
        self.adl401_Component = adl401_Component
        self.adl401_Component9 = adl401_Component9 if adl401_Component9 is not None else set()
        self.adl401_Component12 = adl401_Component12 if adl401_Component12 is not None else set()
        self.adl401_Component14 = adl401_Component14 if adl401_Component14 is not None else set()
        self.contentParent = contentParent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl401_Component9(self):
        return self.__adl401_Component9

    @adl401_Component9.setter
    def adl401_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__adl401_Component9", None)
        self.__adl401_Component9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_Component"):
                    opp_val = getattr(item, "adl401_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_Component"):
                    opp_val = getattr(item, "adl401_Component", None)
                    
                    setattr(item, "adl401_Component", self)
                    

    @property
    def contentParent(self):
        return self.__contentParent

    @contentParent.setter
    def contentParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__contentParent", None)
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
    def adl401_Component(self):
        return self.__adl401_Component

    @adl401_Component.setter
    def adl401_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__adl401_Component", None)
        self.__adl401_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl401_Component9"):
                opp_val = getattr(old_value, "adl401_Component9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl401_Component9"):
                opp_val = getattr(value, "adl401_Component9", None)
                if opp_val is None:
                    setattr(value, "adl401_Component9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl401_Component14(self):
        return self.__adl401_Component14

    @adl401_Component14.setter
    def adl401_Component14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__adl401_Component14", None)
        self.__adl401_Component14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_Provided"):
                    opp_val = getattr(item, "adl401_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_Provided"):
                    opp_val = getattr(item, "adl401_Provided", None)
                    
                    setattr(item, "adl401_Provided", self)
                    

    @property
    def adl401_Component12(self):
        return self.__adl401_Component12

    @adl401_Component12.setter
    def adl401_Component12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__adl401_Component12", None)
        self.__adl401_Component12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_Required"):
                    opp_val = getattr(item, "adl401_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_Required"):
                    opp_val = getattr(item, "adl401_Required", None)
                    
                    setattr(item, "adl401_Required", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Component__Component", None)
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

class adl401_Content:

    def __init__(self, expression: str, language: str, content: "adl401_Component" = None, adl401_Content: set["adl401_EClass0"] = None, Content: "adl401_Component" = None):
        self.expression = expression
        self.language = language
        self.content = content
        self.adl401_Content = adl401_Content if adl401_Content is not None else set()
        self.Content = Content
        
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
    def adl401_Content(self):
        return self.__adl401_Content

    @adl401_Content.setter
    def adl401_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Content__adl401_Content", None)
        self.__adl401_Content = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl401_EClass0"):
                    opp_val = getattr(item, "adl401_EClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "adl401_EClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl401_EClass0"):
                    opp_val = getattr(item, "adl401_EClass0", None)
                    
                    setattr(item, "adl401_EClass0", self)
                    

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl401_Content__content", None)
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
        old_value = getattr(self, f"_adl401_Content__Content", None)
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
