from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class z4fsm_State(AbstractState):

    pass
class z4fsm_AbstractState(ABC):

    def __init__(self, id: str, z4fsm_AbstractState: "z4fsm_Region" = None, z4fsm_AbstractState2: set["z4fsm_State"] = None):
        self.id = id
        self.z4fsm_AbstractState = z4fsm_AbstractState
        self.z4fsm_AbstractState2 = z4fsm_AbstractState2 if z4fsm_AbstractState2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z4fsm_AbstractState(self):
        return self.__z4fsm_AbstractState

    @z4fsm_AbstractState.setter
    def z4fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z4fsm_AbstractState__z4fsm_AbstractState", None)
        self.__z4fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z4fsm_Region"):
                opp_val = getattr(old_value, "z4fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z4fsm_Region"):
                opp_val = getattr(value, "z4fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z4fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def z4fsm_AbstractState2(self):
        return self.__z4fsm_AbstractState2

    @z4fsm_AbstractState2.setter
    def z4fsm_AbstractState2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z4fsm_AbstractState__z4fsm_AbstractState2", None)
        self.__z4fsm_AbstractState2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z4fsm_State"):
                    opp_val = getattr(item, "z4fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "z4fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z4fsm_State"):
                    opp_val = getattr(item, "z4fsm_State", None)
                    
                    setattr(item, "z4fsm_State", self)
                    

class z4fsm_Region:

    def __init__(self, name: str, z4fsm_Region: set["z4fsm_AbstractState"] = None):
        self.name = name
        self.z4fsm_Region = z4fsm_Region if z4fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z4fsm_Region(self):
        return self.__z4fsm_Region

    @z4fsm_Region.setter
    def z4fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z4fsm_Region__z4fsm_Region", None)
        self.__z4fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z4fsm_AbstractState"):
                    opp_val = getattr(item, "z4fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z4fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z4fsm_AbstractState"):
                    opp_val = getattr(item, "z4fsm_AbstractState", None)
                    
                    setattr(item, "z4fsm_AbstractState", self)
                    
