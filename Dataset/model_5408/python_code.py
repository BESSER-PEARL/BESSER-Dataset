from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GateType(Enum):
    ORGate = "ORGate"
    ANDGate = "ANDGate"


############################################
# Definition of Classes
############################################

class Diagram:

    pass
class fta_Event(Diagram):

    def __init__(self, BaseEvent: bool, fta_Event: "fta_Condition" = None, fta_Event6: "fta_Condition" = None):
        self.BaseEvent = BaseEvent
        self.fta_Event = fta_Event
        self.fta_Event6 = fta_Event6
        
    @property
    def BaseEvent(self) -> bool:
        return self.__BaseEvent

    @BaseEvent.setter
    def BaseEvent(self, BaseEvent: bool):
        self.__BaseEvent = BaseEvent

    @property
    def fta_Event6(self):
        return self.__fta_Event6

    @fta_Event6.setter
    def fta_Event6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Event__fta_Event6", None)
        self.__fta_Event6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fta_Condition5"):
                opp_val = getattr(old_value, "fta_Condition5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fta_Condition5"):
                opp_val = getattr(value, "fta_Condition5", None)
                if opp_val is None:
                    setattr(value, "fta_Condition5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fta_Event(self):
        return self.__fta_Event

    @fta_Event.setter
    def fta_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Event__fta_Event", None)
        self.__fta_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fta_Condition3"):
                opp_val = getattr(old_value, "fta_Condition3", None)
                if opp_val == self:
                    setattr(old_value, "fta_Condition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fta_Condition3"):
                opp_val = getattr(value, "fta_Condition3", None)
                setattr(value, "fta_Condition3", self)

class fta_Condition(Diagram):

    def __init__(self, GateKind: str, fta_Condition: "fta_Hazard" = None, fta_Condition3: "fta_Event" = None, fta_Condition5: set["fta_Event"] = None):
        self.GateKind = GateKind
        self.fta_Condition = fta_Condition
        self.fta_Condition3 = fta_Condition3
        self.fta_Condition5 = fta_Condition5 if fta_Condition5 is not None else set()
        
    @property
    def GateKind(self) -> str:
        return self.__GateKind

    @GateKind.setter
    def GateKind(self, GateKind: str):
        self.__GateKind = GateKind

    @property
    def fta_Condition3(self):
        return self.__fta_Condition3

    @fta_Condition3.setter
    def fta_Condition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Condition__fta_Condition3", None)
        self.__fta_Condition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fta_Event"):
                opp_val = getattr(old_value, "fta_Event", None)
                if opp_val == self:
                    setattr(old_value, "fta_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fta_Event"):
                opp_val = getattr(value, "fta_Event", None)
                setattr(value, "fta_Event", self)

    @property
    def fta_Condition(self):
        return self.__fta_Condition

    @fta_Condition.setter
    def fta_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Condition__fta_Condition", None)
        self.__fta_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fta_Hazard"):
                opp_val = getattr(old_value, "fta_Hazard", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fta_Hazard"):
                opp_val = getattr(value, "fta_Hazard", None)
                if opp_val is None:
                    setattr(value, "fta_Hazard", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fta_Condition5(self):
        return self.__fta_Condition5

    @fta_Condition5.setter
    def fta_Condition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Condition__fta_Condition5", None)
        self.__fta_Condition5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fta_Event6"):
                    opp_val = getattr(item, "fta_Event6", None)
                    
                    if opp_val == self:
                        setattr(item, "fta_Event6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fta_Event6"):
                    opp_val = getattr(item, "fta_Event6", None)
                    
                    setattr(item, "fta_Event6", self)
                    

class fta_Hazard(Diagram):

    pass
class fta_Diagram(ABC):

    def __init__(self, name: str, detail: str, id: str, fta_Diagram: "fta_FTA" = None):
        self.name = name
        self.detail = detail
        self.id = id
        self.fta_Diagram = fta_Diagram
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def detail(self) -> str:
        return self.__detail

    @detail.setter
    def detail(self, detail: str):
        self.__detail = detail

    @property
    def fta_Diagram(self):
        return self.__fta_Diagram

    @fta_Diagram.setter
    def fta_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fta_Diagram__fta_Diagram", None)
        self.__fta_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fta_FTA"):
                opp_val = getattr(old_value, "fta_FTA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fta_FTA"):
                opp_val = getattr(value, "fta_FTA", None)
                if opp_val is None:
                    setattr(value, "fta_FTA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fta_FTA:

    pass