from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PortB:

    pass
class typeB_PortB(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class typeB_OutPortB(PortB):

    def __init__(self, name: str, OutPortB: "typeB_BlockB" = None, outputPorts: "typeB_BlockB" = None):
        self.name = name
        self.OutPortB = OutPortB
        self.outputPorts = outputPorts
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OutPortB(self):
        return self.__OutPortB

    @OutPortB.setter
    def OutPortB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_OutPortB__OutPortB", None)
        self.__OutPortB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "block"):
                opp_val = getattr(old_value, "block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "block"):
                opp_val = getattr(value, "block", None)
                if opp_val is None:
                    setattr(value, "block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputPorts(self):
        return self.__outputPorts

    @outputPorts.setter
    def outputPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_OutPortB__outputPorts", None)
        self.__outputPorts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockB"):
                opp_val = getattr(old_value, "BlockB", None)
                if opp_val == self:
                    setattr(old_value, "BlockB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockB"):
                opp_val = getattr(value, "BlockB", None)
                setattr(value, "BlockB", self)

class typeB_InPortB(PortB):

    def __init__(self, name: str, typeB_InPortB: "typeB_BlockB" = None):
        self.name = name
        self.typeB_InPortB = typeB_InPortB
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeB_InPortB(self):
        return self.__typeB_InPortB

    @typeB_InPortB.setter
    def typeB_InPortB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_InPortB__typeB_InPortB", None)
        self.__typeB_InPortB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_BlockB"):
                opp_val = getattr(old_value, "typeB_BlockB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_BlockB"):
                opp_val = getattr(value, "typeB_BlockB", None)
                if opp_val is None:
                    setattr(value, "typeB_BlockB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeB_BlockB:

    pass