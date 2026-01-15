from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Component:

    pass
class adlrecur_Base(Component):

    pass
class Interface:

    pass
class adlrecur_Binding:

    pass
class adlrecur_Interface(ABC):

    def __init__(self, name: str, signature: str, adlrecur_Interface: set["adlrecur_Binding"] = None, adlrecur_Interface6: "adlrecur_Binding" = None, adlrecur_Interface9: "adlrecur_Binding" = None):
        self.name = name
        self.signature = signature
        self.adlrecur_Interface = adlrecur_Interface if adlrecur_Interface is not None else set()
        self.adlrecur_Interface6 = adlrecur_Interface6
        self.adlrecur_Interface9 = adlrecur_Interface9
        
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
    def adlrecur_Interface(self):
        return self.__adlrecur_Interface

    @adlrecur_Interface.setter
    def adlrecur_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecur_Interface__adlrecur_Interface", None)
        self.__adlrecur_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlrecur_Binding"):
                    opp_val = getattr(item, "adlrecur_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adlrecur_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlrecur_Binding"):
                    opp_val = getattr(item, "adlrecur_Binding", None)
                    
                    setattr(item, "adlrecur_Binding", self)
                    

    @property
    def adlrecur_Interface9(self):
        return self.__adlrecur_Interface9

    @adlrecur_Interface9.setter
    def adlrecur_Interface9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecur_Interface__adlrecur_Interface9", None)
        self.__adlrecur_Interface9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlrecur_Binding8"):
                opp_val = getattr(old_value, "adlrecur_Binding8", None)
                if opp_val == self:
                    setattr(old_value, "adlrecur_Binding8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlrecur_Binding8"):
                opp_val = getattr(value, "adlrecur_Binding8", None)
                setattr(value, "adlrecur_Binding8", self)

    @property
    def adlrecur_Interface6(self):
        return self.__adlrecur_Interface6

    @adlrecur_Interface6.setter
    def adlrecur_Interface6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecur_Interface__adlrecur_Interface6", None)
        self.__adlrecur_Interface6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlrecur_Binding5"):
                opp_val = getattr(old_value, "adlrecur_Binding5", None)
                if opp_val == self:
                    setattr(old_value, "adlrecur_Binding5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlrecur_Binding5"):
                opp_val = getattr(value, "adlrecur_Binding5", None)
                setattr(value, "adlrecur_Binding5", self)

class adlrecur_Provided(Interface):

    pass
class adlrecur_Component(ABC):

    def __init__(self, name: str, adlrecur_Component: set["adlrecur_Required"] = None, adlrecur_Component2: set["adlrecur_Provided"] = None):
        self.name = name
        self.adlrecur_Component = adlrecur_Component if adlrecur_Component is not None else set()
        self.adlrecur_Component2 = adlrecur_Component2 if adlrecur_Component2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adlrecur_Component2(self):
        return self.__adlrecur_Component2

    @adlrecur_Component2.setter
    def adlrecur_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecur_Component__adlrecur_Component2", None)
        self.__adlrecur_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlrecur_Provided"):
                    opp_val = getattr(item, "adlrecur_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adlrecur_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlrecur_Provided"):
                    opp_val = getattr(item, "adlrecur_Provided", None)
                    
                    setattr(item, "adlrecur_Provided", self)
                    

    @property
    def adlrecur_Component(self):
        return self.__adlrecur_Component

    @adlrecur_Component.setter
    def adlrecur_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlrecur_Component__adlrecur_Component", None)
        self.__adlrecur_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlrecur_Required"):
                    opp_val = getattr(item, "adlrecur_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adlrecur_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlrecur_Required"):
                    opp_val = getattr(item, "adlrecur_Required", None)
                    
                    setattr(item, "adlrecur_Required", self)
                    

class adlrecur_Required(Interface):

    pass