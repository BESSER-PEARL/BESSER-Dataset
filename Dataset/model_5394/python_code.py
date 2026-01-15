from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Identified:

    pass
class multicontainment_b_ChildB1(Identified):

    def __init__(self, name: str, multicontainment_b_ChildB1: "multicontainment_b_RootB" = None, multicontainment_b_ChildB13: "multicontainment_b_RootB" = None):
        self.name = name
        self.multicontainment_b_ChildB1 = multicontainment_b_ChildB1
        self.multicontainment_b_ChildB13 = multicontainment_b_ChildB13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multicontainment_b_ChildB1(self):
        return self.__multicontainment_b_ChildB1

    @multicontainment_b_ChildB1.setter
    def multicontainment_b_ChildB1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multicontainment_b_ChildB1__multicontainment_b_ChildB1", None)
        self.__multicontainment_b_ChildB1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multicontainment_b_RootB"):
                opp_val = getattr(old_value, "multicontainment_b_RootB", None)
                if opp_val == self:
                    setattr(old_value, "multicontainment_b_RootB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multicontainment_b_RootB"):
                opp_val = getattr(value, "multicontainment_b_RootB", None)
                setattr(value, "multicontainment_b_RootB", self)

    @property
    def multicontainment_b_ChildB13(self):
        return self.__multicontainment_b_ChildB13

    @multicontainment_b_ChildB13.setter
    def multicontainment_b_ChildB13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multicontainment_b_ChildB1__multicontainment_b_ChildB13", None)
        self.__multicontainment_b_ChildB13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multicontainment_b_RootB2"):
                opp_val = getattr(old_value, "multicontainment_b_RootB2", None)
                if opp_val == self:
                    setattr(old_value, "multicontainment_b_RootB2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multicontainment_b_RootB2"):
                opp_val = getattr(value, "multicontainment_b_RootB2", None)
                setattr(value, "multicontainment_b_RootB2", self)

class multicontainment_b_RootB(Identified):

    pass
class multicontainment_b_Identified(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class multicontainment_b_ChildB2(Identified):

    def __init__(self, name: str, multicontainment_b_ChildB2: "multicontainment_b_RootB" = None):
        self.name = name
        self.multicontainment_b_ChildB2 = multicontainment_b_ChildB2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multicontainment_b_ChildB2(self):
        return self.__multicontainment_b_ChildB2

    @multicontainment_b_ChildB2.setter
    def multicontainment_b_ChildB2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multicontainment_b_ChildB2__multicontainment_b_ChildB2", None)
        self.__multicontainment_b_ChildB2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multicontainment_b_RootB5"):
                opp_val = getattr(old_value, "multicontainment_b_RootB5", None)
                if opp_val == self:
                    setattr(old_value, "multicontainment_b_RootB5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multicontainment_b_RootB5"):
                opp_val = getattr(value, "multicontainment_b_RootB5", None)
                setattr(value, "multicontainment_b_RootB5", self)
