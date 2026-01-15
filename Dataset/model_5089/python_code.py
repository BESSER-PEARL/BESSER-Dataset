from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Binding:

    pass
class adl402_EClass2(Binding):

    pass
class adl402_EClass1(Binding):

    pass
class Interface:

    pass
class adl402_Provided(Interface):

    pass
class adl402_Required(Interface):

    pass
class adl402_EClass0:

    def __init__(self, EAttribute0: str, adl402_EClass0: "adl402_Content" = None, adl402_EClass018: "adl402_EClass0" = None, adl402_EClass016: set["adl402_EClass0"] = None):
        self.EAttribute0 = EAttribute0
        self.adl402_EClass0 = adl402_EClass0
        self.adl402_EClass018 = adl402_EClass018
        self.adl402_EClass016 = adl402_EClass016 if adl402_EClass016 is not None else set()
        
    @property
    def EAttribute0(self) -> str:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: str):
        self.__EAttribute0 = EAttribute0

    @property
    def adl402_EClass018(self):
        return self.__adl402_EClass018

    @adl402_EClass018.setter
    def adl402_EClass018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_EClass0__adl402_EClass018", None)
        self.__adl402_EClass018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl402_EClass016"):
                opp_val = getattr(old_value, "adl402_EClass016", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl402_EClass016"):
                opp_val = getattr(value, "adl402_EClass016", None)
                if opp_val is None:
                    setattr(value, "adl402_EClass016", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl402_EClass0(self):
        return self.__adl402_EClass0

    @adl402_EClass0.setter
    def adl402_EClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_EClass0__adl402_EClass0", None)
        self.__adl402_EClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl402_Content"):
                opp_val = getattr(old_value, "adl402_Content", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl402_Content"):
                opp_val = getattr(value, "adl402_Content", None)
                if opp_val is None:
                    setattr(value, "adl402_Content", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adl402_EClass016(self):
        return self.__adl402_EClass016

    @adl402_EClass016.setter
    def adl402_EClass016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_EClass0__adl402_EClass016", None)
        self.__adl402_EClass016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_EClass018"):
                    opp_val = getattr(item, "adl402_EClass018", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_EClass018", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_EClass018"):
                    opp_val = getattr(item, "adl402_EClass018", None)
                    
                    setattr(item, "adl402_EClass018", self)
                    

class adl402_Component:

    def __init__(self, name: str, adl402_Component: "adl402_Component" = None, adl402_Component9: set["adl402_Component"] = None, adl402_Component12: set["adl402_Required"] = None, adl402_Component14: set["adl402_Provided"] = None, Component: "adl402_Content" = None, contentParent: "adl402_Content" = None):
        self.name = name
        self.adl402_Component = adl402_Component
        self.adl402_Component9 = adl402_Component9 if adl402_Component9 is not None else set()
        self.adl402_Component12 = adl402_Component12 if adl402_Component12 is not None else set()
        self.adl402_Component14 = adl402_Component14 if adl402_Component14 is not None else set()
        self.Component = Component
        self.contentParent = contentParent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adl402_Component12(self):
        return self.__adl402_Component12

    @adl402_Component12.setter
    def adl402_Component12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__adl402_Component12", None)
        self.__adl402_Component12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_Required"):
                    opp_val = getattr(item, "adl402_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_Required"):
                    opp_val = getattr(item, "adl402_Required", None)
                    
                    setattr(item, "adl402_Required", self)
                    

    @property
    def adl402_Component(self):
        return self.__adl402_Component

    @adl402_Component.setter
    def adl402_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__adl402_Component", None)
        self.__adl402_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl402_Component9"):
                opp_val = getattr(old_value, "adl402_Component9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl402_Component9"):
                opp_val = getattr(value, "adl402_Component9", None)
                if opp_val is None:
                    setattr(value, "adl402_Component9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contentParent(self):
        return self.__contentParent

    @contentParent.setter
    def contentParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__contentParent", None)
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
    def adl402_Component14(self):
        return self.__adl402_Component14

    @adl402_Component14.setter
    def adl402_Component14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__adl402_Component14", None)
        self.__adl402_Component14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_Provided"):
                    opp_val = getattr(item, "adl402_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_Provided"):
                    opp_val = getattr(item, "adl402_Provided", None)
                    
                    setattr(item, "adl402_Provided", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__Component", None)
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
    def adl402_Component9(self):
        return self.__adl402_Component9

    @adl402_Component9.setter
    def adl402_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Component__adl402_Component9", None)
        self.__adl402_Component9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_Component"):
                    opp_val = getattr(item, "adl402_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_Component"):
                    opp_val = getattr(item, "adl402_Component", None)
                    
                    setattr(item, "adl402_Component", self)
                    

class adl402_Content:

    def __init__(self, expression: str, language: str, content: "adl402_Component" = None, adl402_Content: set["adl402_EClass0"] = None, Content: "adl402_Component" = None):
        self.expression = expression
        self.language = language
        self.content = content
        self.adl402_Content = adl402_Content if adl402_Content is not None else set()
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
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Content__Content", None)
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

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Content__content", None)
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
    def adl402_Content(self):
        return self.__adl402_Content

    @adl402_Content.setter
    def adl402_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Content__adl402_Content", None)
        self.__adl402_Content = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_EClass0"):
                    opp_val = getattr(item, "adl402_EClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_EClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_EClass0"):
                    opp_val = getattr(item, "adl402_EClass0", None)
                    
                    setattr(item, "adl402_EClass0", self)
                    

class adl402_Binding(ABC):

    pass
class adl402_Interface(ABC):

    def __init__(self, name: str, signature: str, adl402_Interface: set["adl402_Binding"] = None, adl402_Interface3: "adl402_Binding" = None, adl402_Interface6: "adl402_Binding" = None):
        self.name = name
        self.signature = signature
        self.adl402_Interface = adl402_Interface if adl402_Interface is not None else set()
        self.adl402_Interface3 = adl402_Interface3
        self.adl402_Interface6 = adl402_Interface6
        
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
    def adl402_Interface3(self):
        return self.__adl402_Interface3

    @adl402_Interface3.setter
    def adl402_Interface3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Interface__adl402_Interface3", None)
        self.__adl402_Interface3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl402_Binding2"):
                opp_val = getattr(old_value, "adl402_Binding2", None)
                if opp_val == self:
                    setattr(old_value, "adl402_Binding2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl402_Binding2"):
                opp_val = getattr(value, "adl402_Binding2", None)
                setattr(value, "adl402_Binding2", self)

    @property
    def adl402_Interface6(self):
        return self.__adl402_Interface6

    @adl402_Interface6.setter
    def adl402_Interface6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Interface__adl402_Interface6", None)
        self.__adl402_Interface6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adl402_Binding5"):
                opp_val = getattr(old_value, "adl402_Binding5", None)
                if opp_val == self:
                    setattr(old_value, "adl402_Binding5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adl402_Binding5"):
                opp_val = getattr(value, "adl402_Binding5", None)
                setattr(value, "adl402_Binding5", self)

    @property
    def adl402_Interface(self):
        return self.__adl402_Interface

    @adl402_Interface.setter
    def adl402_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adl402_Interface__adl402_Interface", None)
        self.__adl402_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adl402_Binding"):
                    opp_val = getattr(item, "adl402_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adl402_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adl402_Binding"):
                    opp_val = getattr(item, "adl402_Binding", None)
                    
                    setattr(item, "adl402_Binding", self)
                    
