from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class z7fsm_AbstractState(ABC):

    def __init__(self, id: str, z7fsm_AbstractState: "z7fsm_Region" = None, z7fsm_AbstractState3: "z7fsm_AbstractState" = None, z7fsm_AbstractState1: set["z7fsm_AbstractState"] = None):
        self.id = id
        self.z7fsm_AbstractState = z7fsm_AbstractState
        self.z7fsm_AbstractState3 = z7fsm_AbstractState3
        self.z7fsm_AbstractState1 = z7fsm_AbstractState1 if z7fsm_AbstractState1 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z7fsm_AbstractState1(self):
        return self.__z7fsm_AbstractState1

    @z7fsm_AbstractState1.setter
    def z7fsm_AbstractState1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z7fsm_AbstractState__z7fsm_AbstractState1", None)
        self.__z7fsm_AbstractState1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z7fsm_AbstractState3"):
                    opp_val = getattr(item, "z7fsm_AbstractState3", None)
                    
                    if opp_val == self:
                        setattr(item, "z7fsm_AbstractState3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z7fsm_AbstractState3"):
                    opp_val = getattr(item, "z7fsm_AbstractState3", None)
                    
                    setattr(item, "z7fsm_AbstractState3", self)
                    

    @property
    def z7fsm_AbstractState(self):
        return self.__z7fsm_AbstractState

    @z7fsm_AbstractState.setter
    def z7fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z7fsm_AbstractState__z7fsm_AbstractState", None)
        self.__z7fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z7fsm_Region"):
                opp_val = getattr(old_value, "z7fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z7fsm_Region"):
                opp_val = getattr(value, "z7fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z7fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def z7fsm_AbstractState3(self):
        return self.__z7fsm_AbstractState3

    @z7fsm_AbstractState3.setter
    def z7fsm_AbstractState3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z7fsm_AbstractState__z7fsm_AbstractState3", None)
        self.__z7fsm_AbstractState3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z7fsm_AbstractState1"):
                opp_val = getattr(old_value, "z7fsm_AbstractState1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z7fsm_AbstractState1"):
                opp_val = getattr(value, "z7fsm_AbstractState1", None)
                if opp_val is None:
                    setattr(value, "z7fsm_AbstractState1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractState:

    pass
class z7fsm_State(AbstractState):

    pass
class z7fsm_Region(AbstractState):

    def __init__(self, name: str, z7fsm_Region: set["z7fsm_AbstractState"] = None):
        self.name = name
        self.z7fsm_Region = z7fsm_Region if z7fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z7fsm_Region(self):
        return self.__z7fsm_Region

    @z7fsm_Region.setter
    def z7fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z7fsm_Region__z7fsm_Region", None)
        self.__z7fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z7fsm_AbstractState"):
                    opp_val = getattr(item, "z7fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z7fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z7fsm_AbstractState"):
                    opp_val = getattr(item, "z7fsm_AbstractState", None)
                    
                    setattr(item, "z7fsm_AbstractState", self)
                    
