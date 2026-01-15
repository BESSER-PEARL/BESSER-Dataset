from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OutPortB:

    pass
class typeB_OutType1(OutPortB):

    pass
class typeB_NonReferencedClass2:

    pass
class typeB_NonReferencedClass:

    pass
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

    def __init__(self, name: str, typeB_OutPortB: "typeB_BlockB" = None, typeB_OutPortB4: "typeB_BlockB" = None):
        self.name = name
        self.typeB_OutPortB = typeB_OutPortB
        self.typeB_OutPortB4 = typeB_OutPortB4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeB_OutPortB(self):
        return self.__typeB_OutPortB

    @typeB_OutPortB.setter
    def typeB_OutPortB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_OutPortB__typeB_OutPortB", None)
        self.__typeB_OutPortB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_BlockB2"):
                opp_val = getattr(old_value, "typeB_BlockB2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_BlockB2"):
                opp_val = getattr(value, "typeB_BlockB2", None)
                if opp_val is None:
                    setattr(value, "typeB_BlockB2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typeB_OutPortB4(self):
        return self.__typeB_OutPortB4

    @typeB_OutPortB4.setter
    def typeB_OutPortB4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_OutPortB__typeB_OutPortB4", None)
        self.__typeB_OutPortB4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_BlockB5"):
                opp_val = getattr(old_value, "typeB_BlockB5", None)
                if opp_val == self:
                    setattr(old_value, "typeB_BlockB5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_BlockB5"):
                opp_val = getattr(value, "typeB_BlockB5", None)
                setattr(value, "typeB_BlockB5", self)

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