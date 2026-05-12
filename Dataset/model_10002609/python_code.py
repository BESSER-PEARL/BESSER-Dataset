from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class ExtensionBoard:

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

    def __init__(self, chunck: str, machine0: set["Machine"] = None, processor2: set["Processor"] = None, ramProxy10: "RAM" = None):
        self.chunck = chunck
        self.machine0 = machine0 if machine0 is not None else set()
        self.processor2 = processor2 if processor2 is not None else set()
        self.ramProxy10 = ramProxy10
        
        pass
    @property
    def chunck(self):
        return self.__chunck
    @chunck.setter
    def chunck(self, chunck: str):
        self.__chunck = chunck

    @property
    def processor2(self):
        return self.__processor2
    @processor2.setter
    def processor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cache__processor2", None)
        self.__processor2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "memory3"):
                    opp_val = getattr(item, "memory3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "memory3"):
                    opp_val = getattr(item, "memory3", None)
                    
                    if opp_val is None:
                        setattr(item, "memory3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

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

    @property
    def machine0(self):
        return self.__machine0
    @machine0.setter
    def machine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cache__machine0", None)
        self.__machine0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "memory1"):
                    opp_val = getattr(item, "memory1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "memory1"):
                    opp_val = getattr(item, "memory1", None)
                    
                    if opp_val is None:
                        setattr(item, "memory1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class AcceleratorCard(ABC):

    pass


class Processor(ABC):

    pass


class CPU:

    pass
