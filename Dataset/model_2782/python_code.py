from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AnEnumeration(Enum):
    LITERAL0 = "LITERAL0"
    LITERAL1 = "LITERAL1"
    LITERAL2 = "LITERAL2"


############################################
# Definition of Classes
############################################

class BoemTest_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class B:

    pass
class BoemTest_C(B):

    pass
class BoemTest_BNode:

    pass
class A:

    pass
class BoemTest_B(A):

    def __init__(self, enumAttr: str, BoemTest_B: set["BoemTest_Node"] = None, BoemTest_B19: "BoemTest_Node" = None, BoemTest_B22: "BoemTest_BNode" = None):
        self.enumAttr = enumAttr
        self.BoemTest_B = BoemTest_B if BoemTest_B is not None else set()
        self.BoemTest_B19 = BoemTest_B19
        self.BoemTest_B22 = BoemTest_B22
        
    @property
    def enumAttr(self) -> str:
        return self.__enumAttr

    @enumAttr.setter
    def enumAttr(self, enumAttr: str):
        self.__enumAttr = enumAttr

    @property
    def BoemTest_B22(self):
        return self.__BoemTest_B22

    @BoemTest_B22.setter
    def BoemTest_B22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoemTest_B__BoemTest_B22", None)
        self.__BoemTest_B22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoemTest_BNode"):
                opp_val = getattr(old_value, "BoemTest_BNode", None)
                if opp_val == self:
                    setattr(old_value, "BoemTest_BNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoemTest_BNode"):
                opp_val = getattr(value, "BoemTest_BNode", None)
                setattr(value, "BoemTest_BNode", self)

    @property
    def BoemTest_B19(self):
        return self.__BoemTest_B19

    @BoemTest_B19.setter
    def BoemTest_B19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoemTest_B__BoemTest_B19", None)
        self.__BoemTest_B19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoemTest_Node20"):
                opp_val = getattr(old_value, "BoemTest_Node20", None)
                if opp_val == self:
                    setattr(old_value, "BoemTest_Node20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoemTest_Node20"):
                opp_val = getattr(value, "BoemTest_Node20", None)
                setattr(value, "BoemTest_Node20", self)

    @property
    def BoemTest_B(self):
        return self.__BoemTest_B

    @BoemTest_B.setter
    def BoemTest_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoemTest_B__BoemTest_B", None)
        self.__BoemTest_B = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoemTest_Node17"):
                    opp_val = getattr(item, "BoemTest_Node17", None)
                    
                    if opp_val == self:
                        setattr(item, "BoemTest_Node17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoemTest_Node17"):
                    opp_val = getattr(item, "BoemTest_Node17", None)
                    
                    setattr(item, "BoemTest_Node17", self)
                    

class NamedElement:

    pass
class BoemTest_Node(NamedElement):

    pass
class BoemTest_A(NamedElement):

    pass