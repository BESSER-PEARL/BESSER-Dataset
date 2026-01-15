from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class z2fsm_Foo(AbstractState):

    pass
class z2fsm_State(AbstractState):

    pass
class z2fsm_Region:

    def __init__(self, name: str, z2fsm_Region: set["z2fsm_AbstractState"] = None):
        self.name = name
        self.z2fsm_Region = z2fsm_Region if z2fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z2fsm_Region(self):
        return self.__z2fsm_Region

    @z2fsm_Region.setter
    def z2fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z2fsm_Region__z2fsm_Region", None)
        self.__z2fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z2fsm_AbstractState"):
                    opp_val = getattr(item, "z2fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z2fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z2fsm_AbstractState"):
                    opp_val = getattr(item, "z2fsm_AbstractState", None)
                    
                    setattr(item, "z2fsm_AbstractState", self)
                    

class z2fsm_AbstractState(ABC):

    def __init__(self, id: str, z2fsm_AbstractState: "z2fsm_Region" = None):
        self.id = id
        self.z2fsm_AbstractState = z2fsm_AbstractState
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z2fsm_AbstractState(self):
        return self.__z2fsm_AbstractState

    @z2fsm_AbstractState.setter
    def z2fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z2fsm_AbstractState__z2fsm_AbstractState", None)
        self.__z2fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z2fsm_Region"):
                opp_val = getattr(old_value, "z2fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z2fsm_Region"):
                opp_val = getattr(value, "z2fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z2fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
