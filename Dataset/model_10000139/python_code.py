from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Chess:

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field
    @field.setter
    def field(self, field: str):
        self.__field = field



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


class Instruction:

    pass


class Program:

    def __init__(self, name: str, instructions1: set["Instruction"] = None, processor2: set["Processor"] = None):
        self.name = name
        self.instructions1 = instructions1 if instructions1 is not None else set()
        self.processor2 = processor2 if processor2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def instructions1(self):
        return self.__instructions1
    @instructions1.setter
    def instructions1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__instructions1", None)
        self.__instructions1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program0"):
                    opp_val = getattr(item, "program0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program0"):
                    opp_val = getattr(item, "program0", None)
                    
                    if opp_val is None:
                        setattr(item, "program0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def processor2(self):
        return self.__processor2
    @processor2.setter
    def processor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program__processor2", None)
        self.__processor2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "program3"):
                    opp_val = getattr(item, "program3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "program3"):
                    opp_val = getattr(item, "program3", None)
                    
                    if opp_val is None:
                        setattr(item, "program3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class RAM:

    pass


class Cache:

    def __init__(self, chunck: str, ramProxy4: "RAM" = None):
        self.chunck = chunck
        self.ramProxy4 = ramProxy4
        
        pass
    @property
    def chunck(self):
        return self.__chunck
    @chunck.setter
    def chunck(self, chunck: str):
        self.__chunck = chunck

    @property
    def ramProxy4(self):
        return self.__ramProxy4
    @ramProxy4.setter
    def ramProxy4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cache__ramProxy4", None)
        self.__ramProxy4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cache5"):
                opp_val = getattr(old_value, "cache5", None)
                if opp_val == self:
                    setattr(old_value, "cache5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cache5"):
                opp_val = getattr(value, "cache5", None)
                setattr(value, "cache5", self)



class AcceleratorCard(ABC):

    pass


class Processor(ABC):

    pass


class CPU:

    pass
