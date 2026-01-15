from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class z5fsm_State(AbstractState):

    pass
class z5fsm_AbstractState(ABC):

    def __init__(self, id: str, z5fsm_AbstractState: "z5fsm_Region" = None, z5fsm_AbstractState3: "z5fsm_AbstractState" = None, z5fsm_AbstractState1: set["z5fsm_AbstractState"] = None):
        self.id = id
        self.z5fsm_AbstractState = z5fsm_AbstractState
        self.z5fsm_AbstractState3 = z5fsm_AbstractState3
        self.z5fsm_AbstractState1 = z5fsm_AbstractState1 if z5fsm_AbstractState1 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def z5fsm_AbstractState(self):
        return self.__z5fsm_AbstractState

    @z5fsm_AbstractState.setter
    def z5fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z5fsm_AbstractState__z5fsm_AbstractState", None)
        self.__z5fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z5fsm_Region"):
                opp_val = getattr(old_value, "z5fsm_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z5fsm_Region"):
                opp_val = getattr(value, "z5fsm_Region", None)
                if opp_val is None:
                    setattr(value, "z5fsm_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def z5fsm_AbstractState1(self):
        return self.__z5fsm_AbstractState1

    @z5fsm_AbstractState1.setter
    def z5fsm_AbstractState1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z5fsm_AbstractState__z5fsm_AbstractState1", None)
        self.__z5fsm_AbstractState1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z5fsm_AbstractState3"):
                    opp_val = getattr(item, "z5fsm_AbstractState3", None)
                    
                    if opp_val == self:
                        setattr(item, "z5fsm_AbstractState3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z5fsm_AbstractState3"):
                    opp_val = getattr(item, "z5fsm_AbstractState3", None)
                    
                    setattr(item, "z5fsm_AbstractState3", self)
                    

    @property
    def z5fsm_AbstractState3(self):
        return self.__z5fsm_AbstractState3

    @z5fsm_AbstractState3.setter
    def z5fsm_AbstractState3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z5fsm_AbstractState__z5fsm_AbstractState3", None)
        self.__z5fsm_AbstractState3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "z5fsm_AbstractState1"):
                opp_val = getattr(old_value, "z5fsm_AbstractState1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "z5fsm_AbstractState1"):
                opp_val = getattr(value, "z5fsm_AbstractState1", None)
                if opp_val is None:
                    setattr(value, "z5fsm_AbstractState1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class z5fsm_Region:

    def __init__(self, name: str, z5fsm_Region: set["z5fsm_AbstractState"] = None):
        self.name = name
        self.z5fsm_Region = z5fsm_Region if z5fsm_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def z5fsm_Region(self):
        return self.__z5fsm_Region

    @z5fsm_Region.setter
    def z5fsm_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_z5fsm_Region__z5fsm_Region", None)
        self.__z5fsm_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "z5fsm_AbstractState"):
                    opp_val = getattr(item, "z5fsm_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "z5fsm_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "z5fsm_AbstractState"):
                    opp_val = getattr(item, "z5fsm_AbstractState", None)
                    
                    setattr(item, "z5fsm_AbstractState", self)
                    
