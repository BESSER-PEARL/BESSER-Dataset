from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class z8fsm_State(AbstractState):

    pass
class z8fsm_Region(AbstractState):

    def __init__(self, name: str, z8fsm_Region: set["z8fsm_AbstractState"] = None):
        self.name = name
        self.z8fsm_Region = z8fsm_Region if z8fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z8fsm_Region(self):
        return self.__z8fsm_Region

    @z8fsm_Region.setter
    def z8fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z8fsm_Region__z8fsm_Region", None)
        self.__z8fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z8fsm_AbstractState"):
                    opp_val = getattr(item, "z8fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z8fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z8fsm_AbstractState"):
                    opp_val = getattr(item, "z8fsm_AbstractState", None)
                    
                    setattr(item, "z8fsm_AbstractState", self)
                    

class z8fsm_AbstractState(ABC):

    def __init__(self, id: str, z8fsm_AbstractState: "z8fsm_Region" = None, z8fsm_AbstractState3: "z8fsm_AbstractState" = None, z8fsm_AbstractState1: set["z8fsm_AbstractState"] = None):
        self.id = id
        self.z8fsm_AbstractState = z8fsm_AbstractState
        self.z8fsm_AbstractState3 = z8fsm_AbstractState3
        self.z8fsm_AbstractState1 = z8fsm_AbstractState1 if z8fsm_AbstractState1 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z8fsm_AbstractState(self):
        return self.__z8fsm_AbstractState

    @z8fsm_AbstractState.setter
    def z8fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z8fsm_AbstractState__z8fsm_AbstractState", None)
        self.__z8fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z8fsm_Region"):
                opp_val = getattr(old_value, "z8fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z8fsm_Region"):
                opp_val = getattr(value, "z8fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z8fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def z8fsm_AbstractState1(self):
        return self.__z8fsm_AbstractState1

    @z8fsm_AbstractState1.setter
    def z8fsm_AbstractState1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z8fsm_AbstractState__z8fsm_AbstractState1", None)
        self.__z8fsm_AbstractState1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z8fsm_AbstractState3"):
                    opp_val = getattr(item, "z8fsm_AbstractState3", None)
                    
                    if opp_val == self:
                        setattr(item, "z8fsm_AbstractState3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z8fsm_AbstractState3"):
                    opp_val = getattr(item, "z8fsm_AbstractState3", None)
                    
                    setattr(item, "z8fsm_AbstractState3", self)
                    

    @property
    def z8fsm_AbstractState3(self):
        return self.__z8fsm_AbstractState3

    @z8fsm_AbstractState3.setter
    def z8fsm_AbstractState3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z8fsm_AbstractState__z8fsm_AbstractState3", None)
        self.__z8fsm_AbstractState3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z8fsm_AbstractState1"):
                opp_val = getattr(old_value, "z8fsm_AbstractState1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z8fsm_AbstractState1"):
                opp_val = getattr(value, "z8fsm_AbstractState1", None)
                if opp_val is None:
                    setattr(value, "z8fsm_AbstractState1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
