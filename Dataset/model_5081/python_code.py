from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adlsimple_Base:

    pass
class adlsimple_Binding:

    pass
class adlsimple_Interface(ABC):

    def __init__(self, name: str, signature: str, adlsimple_Interface: set["adlsimple_Binding"] = None, adlsimple_Interface6: "adlsimple_Binding" = None, adlsimple_Interface9: "adlsimple_Binding" = None):
        self.name = name
        self.signature = signature
        self.adlsimple_Interface = adlsimple_Interface if adlsimple_Interface is not None else set()
        self.adlsimple_Interface6 = adlsimple_Interface6
        self.adlsimple_Interface9 = adlsimple_Interface9
        
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
    def adlsimple_Interface6(self):
        return self.__adlsimple_Interface6

    @adlsimple_Interface6.setter
    def adlsimple_Interface6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Interface__adlsimple_Interface6", None)
        self.__adlsimple_Interface6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlsimple_Binding5"):
                opp_val = getattr(old_value, "adlsimple_Binding5", None)
                if opp_val == self:
                    setattr(old_value, "adlsimple_Binding5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlsimple_Binding5"):
                opp_val = getattr(value, "adlsimple_Binding5", None)
                setattr(value, "adlsimple_Binding5", self)

    @property
    def adlsimple_Interface(self):
        return self.__adlsimple_Interface

    @adlsimple_Interface.setter
    def adlsimple_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Interface__adlsimple_Interface", None)
        self.__adlsimple_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlsimple_Binding"):
                    opp_val = getattr(item, "adlsimple_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "adlsimple_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlsimple_Binding"):
                    opp_val = getattr(item, "adlsimple_Binding", None)
                    
                    setattr(item, "adlsimple_Binding", self)
                    

    @property
    def adlsimple_Interface9(self):
        return self.__adlsimple_Interface9

    @adlsimple_Interface9.setter
    def adlsimple_Interface9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Interface__adlsimple_Interface9", None)
        self.__adlsimple_Interface9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlsimple_Binding8"):
                opp_val = getattr(old_value, "adlsimple_Binding8", None)
                if opp_val == self:
                    setattr(old_value, "adlsimple_Binding8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlsimple_Binding8"):
                opp_val = getattr(value, "adlsimple_Binding8", None)
                setattr(value, "adlsimple_Binding8", self)

class adlsimple_Provided(Interface):

    pass
class adlsimple_Required(Interface):

    pass
class adlsimple_Component:

    def __init__(self, name: str, adlsimple_Component: set["adlsimple_Required"] = None, adlsimple_Component2: set["adlsimple_Provided"] = None, adlsimple_Component11: "adlsimple_Base" = None):
        self.name = name
        self.adlsimple_Component = adlsimple_Component if adlsimple_Component is not None else set()
        self.adlsimple_Component2 = adlsimple_Component2 if adlsimple_Component2 is not None else set()
        self.adlsimple_Component11 = adlsimple_Component11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adlsimple_Component(self):
        return self.__adlsimple_Component

    @adlsimple_Component.setter
    def adlsimple_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Component__adlsimple_Component", None)
        self.__adlsimple_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlsimple_Required"):
                    opp_val = getattr(item, "adlsimple_Required", None)
                    
                    if opp_val == self:
                        setattr(item, "adlsimple_Required", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlsimple_Required"):
                    opp_val = getattr(item, "adlsimple_Required", None)
                    
                    setattr(item, "adlsimple_Required", self)
                    

    @property
    def adlsimple_Component2(self):
        return self.__adlsimple_Component2

    @adlsimple_Component2.setter
    def adlsimple_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Component__adlsimple_Component2", None)
        self.__adlsimple_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adlsimple_Provided"):
                    opp_val = getattr(item, "adlsimple_Provided", None)
                    
                    if opp_val == self:
                        setattr(item, "adlsimple_Provided", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adlsimple_Provided"):
                    opp_val = getattr(item, "adlsimple_Provided", None)
                    
                    setattr(item, "adlsimple_Provided", self)
                    

    @property
    def adlsimple_Component11(self):
        return self.__adlsimple_Component11

    @adlsimple_Component11.setter
    def adlsimple_Component11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adlsimple_Component__adlsimple_Component11", None)
        self.__adlsimple_Component11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adlsimple_Base"):
                opp_val = getattr(old_value, "adlsimple_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adlsimple_Base"):
                opp_val = getattr(value, "adlsimple_Base", None)
                if opp_val is None:
                    setattr(value, "adlsimple_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
