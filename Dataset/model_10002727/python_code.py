from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Arterial_Access_Site:

    def __init__(self, CathPCI_Arterial_Access_Site: str, AAA_Arterial_Access_Site: str, Lower_Extremity_Arterial_Access_Site: str, Renal_Arterial_Access_Site: str, Carotid_Intervention_Arterial_Access_Site: str):
        self.CathPCI_Arterial_Access_Site = CathPCI_Arterial_Access_Site
        self.AAA_Arterial_Access_Site = AAA_Arterial_Access_Site
        self.Lower_Extremity_Arterial_Access_Site = Lower_Extremity_Arterial_Access_Site
        self.Renal_Arterial_Access_Site = Renal_Arterial_Access_Site
        self.Carotid_Intervention_Arterial_Access_Site = Carotid_Intervention_Arterial_Access_Site
        
        pass
    @property
    def Lower_Extremity_Arterial_Access_Site(self):
        return self.__Lower_Extremity_Arterial_Access_Site
    @Lower_Extremity_Arterial_Access_Site.setter
    def Lower_Extremity_Arterial_Access_Site(self, Lower_Extremity_Arterial_Access_Site: str):
        self.__Lower_Extremity_Arterial_Access_Site = Lower_Extremity_Arterial_Access_Site

    @property
    def Carotid_Intervention_Arterial_Access_Site(self):
        return self.__Carotid_Intervention_Arterial_Access_Site
    @Carotid_Intervention_Arterial_Access_Site.setter
    def Carotid_Intervention_Arterial_Access_Site(self, Carotid_Intervention_Arterial_Access_Site: str):
        self.__Carotid_Intervention_Arterial_Access_Site = Carotid_Intervention_Arterial_Access_Site

    @property
    def CathPCI_Arterial_Access_Site(self):
        return self.__CathPCI_Arterial_Access_Site
    @CathPCI_Arterial_Access_Site.setter
    def CathPCI_Arterial_Access_Site(self, CathPCI_Arterial_Access_Site: str):
        self.__CathPCI_Arterial_Access_Site = CathPCI_Arterial_Access_Site

    @property
    def Renal_Arterial_Access_Site(self):
        return self.__Renal_Arterial_Access_Site
    @Renal_Arterial_Access_Site.setter
    def Renal_Arterial_Access_Site(self, Renal_Arterial_Access_Site: str):
        self.__Renal_Arterial_Access_Site = Renal_Arterial_Access_Site

    @property
    def AAA_Arterial_Access_Site(self):
        return self.__AAA_Arterial_Access_Site
    @AAA_Arterial_Access_Site.setter
    def AAA_Arterial_Access_Site(self, AAA_Arterial_Access_Site: str):
        self.__AAA_Arterial_Access_Site = AAA_Arterial_Access_Site



class FastCard:

    pass


class ExtensionBoard:

    pass


class Vendor2Sound:

    pass


class Vendor1Sound:

    pass


class Vendor2Adapter:

    pass


class Vendor1Adapter:

    pass


class GenericSound:

    pass


class Sound(ABC):

    pass


class Card(ABC):

    pass


class DeviceCard(ABC):

    pass


class Memory_Interface:

    pass


class Instruction:

    pass


class Program:

    def __init__(self, name: str, instructions5: set["Instruction"] = None, processor8: set["Processor"] = None):
        self.name = name
        self.instructions5 = instructions5 if instructions5 is not None else set()
        self.processor8 = processor8 if processor8 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def instructions5(self):
        return self.__instructions5
    @instructions5.setter
    def instructions5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__instructions5", None)
        self.__instructions5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program4"):
                    opp_val = getattr(item, "program4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program4"):
                    opp_val = getattr(item, "program4", None)
                    
                    if opp_val is None:
                        setattr(item, "program4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def processor8(self):
        return self.__processor8
    @processor8.setter
    def processor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__processor8", None)
        self.__processor8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program9"):
                    opp_val = getattr(item, "program9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program9"):
                    opp_val = getattr(item, "program9", None)
                    
                    if opp_val is None:
                        setattr(item, "program9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Machine:

    pass


class RAM:

    pass


class Cache:

    def __init__(self, chunck: str, ramProxy10: "RAM" = None):
        self.chunck = chunck
        self.ramProxy10 = ramProxy10
        
        pass
    @property
    def chunck(self):
        return self.__chunck
    @chunck.setter
    def chunck(self, chunck: str):
        self.__chunck = chunck

    @property
    def ramProxy10(self):
        return self.__ramProxy10
    @ramProxy10.setter
    def ramProxy10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cache__ramProxy10", None)
        self.__ramProxy10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cache11"):
                opp_val = getattr(old_value, "cache11", None)
                if opp_val == self:
                    setattr(old_value, "cache11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cache11"):
                opp_val = getattr(value, "cache11", None)
                setattr(value, "cache11", self)



class AcceleratorCard(ABC):

    pass


class Processor(ABC):

    pass


class CPU:

    pass
