from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class z3fsm_AbstractState(ABC):

    def __init__(self, id: str, z3fsm_AbstractState: "z3fsm_Region" = None):
        self.id = id
        self.z3fsm_AbstractState = z3fsm_AbstractState
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z3fsm_AbstractState(self):
        return self.__z3fsm_AbstractState

    @z3fsm_AbstractState.setter
    def z3fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z3fsm_AbstractState__z3fsm_AbstractState", None)
        self.__z3fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z3fsm_Region"):
                opp_val = getattr(old_value, "z3fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z3fsm_Region"):
                opp_val = getattr(value, "z3fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z3fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractState:

    pass
class z3fsm_State(AbstractState):

    pass
class z3fsm_Region(AbstractState):

    def __init__(self, name: str, z3fsm_Region: set["z3fsm_AbstractState"] = None):
        self.name = name
        self.z3fsm_Region = z3fsm_Region if z3fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z3fsm_Region(self):
        return self.__z3fsm_Region

    @z3fsm_Region.setter
    def z3fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z3fsm_Region__z3fsm_Region", None)
        self.__z3fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z3fsm_AbstractState"):
                    opp_val = getattr(item, "z3fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z3fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z3fsm_AbstractState"):
                    opp_val = getattr(item, "z3fsm_AbstractState", None)
                    
                    setattr(item, "z3fsm_AbstractState", self)
                    
