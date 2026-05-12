from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Class2:

    pass


class Class:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



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

    def __init__(self, name: str, instructions3: set["Instruction"] = None, processor4: set["Processor"] = None):
        self.name = name
        self.instructions3 = instructions3 if instructions3 is not None else set()
        self.processor4 = processor4 if processor4 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def instructions3(self):
        return self.__instructions3
    @instructions3.setter
    def instructions3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__instructions3", None)
        self.__instructions3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program2"):
                    opp_val = getattr(item, "program2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program2"):
                    opp_val = getattr(item, "program2", None)
                    
                    if opp_val is None:
                        setattr(item, "program2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def processor4(self):
        return self.__processor4
    @processor4.setter
    def processor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__processor4", None)
        self.__processor4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program5"):
                    opp_val = getattr(item, "program5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program5"):
                    opp_val = getattr(item, "program5", None)
                    
                    if opp_val is None:
                        setattr(item, "program5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class RAM:

    pass


class Cache:

    def __init__(self, chunck: str, ramProxy6: "RAM" = None):
        self.chunck = chunck
        self.ramProxy6 = ramProxy6
        
        pass
    @property
    def chunck(self):
        return self.__chunck
    @chunck.setter
    def chunck(self, chunck: str):
        self.__chunck = chunck

    @property
    def ramProxy6(self):
        return self.__ramProxy6
    @ramProxy6.setter
    def ramProxy6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cache__ramProxy6", None)
        self.__ramProxy6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cache7"):
                opp_val = getattr(old_value, "cache7", None)
                if opp_val == self:
                    setattr(old_value, "cache7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cache7"):
                opp_val = getattr(value, "cache7", None)
                setattr(value, "cache7", self)



class AcceleratorCard(ABC):

    pass


class Processor(ABC):

    pass


class CPU:

    pass
