from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sihuhu_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Rail:

    pass
class sihuhu_SwitchConnection(Rail):

    pass
class TrackElement:

    pass
class sihuhu_Switch(TrackElement):

    pass
class sihuhu_Rail(TrackElement):

    pass
class NamedElement:

    pass
class sihuhu_Track(NamedElement):

    pass
class sihuhu_TrackElement(NamedElement):

    pass
class sihuhu_Train(NamedElement):

    pass
class sihuhu_Signal(NamedElement):

    def __init__(self, enabled: bool, sihuhu_Signal: "sihuhu_Rail" = None, sihuhu_Signal12: "sihuhu_Rail" = None, sihuhu_Signal31: "sihuhu_Rail" = None):
        self.enabled = enabled
        self.sihuhu_Signal = sihuhu_Signal
        self.sihuhu_Signal12 = sihuhu_Signal12
        self.sihuhu_Signal31 = sihuhu_Signal31
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def sihuhu_Signal31(self):
        return self.__sihuhu_Signal31

    @sihuhu_Signal31.setter
    def sihuhu_Signal31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sihuhu_Signal__sihuhu_Signal31", None)
        self.__sihuhu_Signal31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sihuhu_Rail32"):
                opp_val = getattr(old_value, "sihuhu_Rail32", None)
                if opp_val == self:
                    setattr(old_value, "sihuhu_Rail32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sihuhu_Rail32"):
                opp_val = getattr(value, "sihuhu_Rail32", None)
                setattr(value, "sihuhu_Rail32", self)

    @property
    def sihuhu_Signal12(self):
        return self.__sihuhu_Signal12

    @sihuhu_Signal12.setter
    def sihuhu_Signal12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sihuhu_Signal__sihuhu_Signal12", None)
        self.__sihuhu_Signal12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sihuhu_Rail11"):
                opp_val = getattr(old_value, "sihuhu_Rail11", None)
                if opp_val == self:
                    setattr(old_value, "sihuhu_Rail11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sihuhu_Rail11"):
                opp_val = getattr(value, "sihuhu_Rail11", None)
                setattr(value, "sihuhu_Rail11", self)

    @property
    def sihuhu_Signal(self):
        return self.__sihuhu_Signal

    @sihuhu_Signal.setter
    def sihuhu_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sihuhu_Signal__sihuhu_Signal", None)
        self.__sihuhu_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sihuhu_Rail9"):
                opp_val = getattr(old_value, "sihuhu_Rail9", None)
                if opp_val == self:
                    setattr(old_value, "sihuhu_Rail9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sihuhu_Rail9"):
                opp_val = getattr(value, "sihuhu_Rail9", None)
                setattr(value, "sihuhu_Rail9", self)

class sihuhu_World(NamedElement):

    pass