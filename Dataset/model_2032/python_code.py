from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeOfChannel(Enum):
    Synchronous = "Synchronous"
    Asynchronous = "Asynchronous"
class Event(Enum):
    RECEIVE = "RECEIVE"
    SEND = "SEND"


############################################
# Definition of Classes
############################################

class network_AbstractElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractElement:

    pass
class network_Channel(AbstractElement):

    def __init__(self, Type: str, network_Channel: "network_Network" = None, network_Channel18: "network_Transition" = None):
        self.Type = Type
        self.network_Channel = network_Channel
        self.network_Channel18 = network_Channel18
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def network_Channel(self):
        return self.__network_Channel

    @network_Channel.setter
    def network_Channel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Channel__network_Channel", None)
        self.__network_Channel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_Network2"):
                opp_val = getattr(old_value, "network_Network2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_Network2"):
                opp_val = getattr(value, "network_Network2", None)
                if opp_val is None:
                    setattr(value, "network_Network2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def network_Channel18(self):
        return self.__network_Channel18

    @network_Channel18.setter
    def network_Channel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Channel__network_Channel18", None)
        self.__network_Channel18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_Transition17"):
                opp_val = getattr(old_value, "network_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "network_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_Transition17"):
                opp_val = getattr(value, "network_Transition17", None)
                setattr(value, "network_Transition17", self)

class network_Statemachine(AbstractElement):

    pass
class network_State(AbstractElement):

    pass
class network_Network(AbstractElement):

    pass
class network_Transition:

    def __init__(self, Event: str, network_Transition: "network_Statemachine" = None, network_Transition11: "network_State" = None, network_Transition14: "network_State" = None, network_Transition17: "network_Channel" = None):
        self.Event = Event
        self.network_Transition = network_Transition
        self.network_Transition11 = network_Transition11
        self.network_Transition14 = network_Transition14
        self.network_Transition17 = network_Transition17
        
    @property
    def Event(self) -> str:
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event

    @property
    def network_Transition11(self):
        return self.__network_Transition11

    @network_Transition11.setter
    def network_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Transition__network_Transition11", None)
        self.__network_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_State12"):
                opp_val = getattr(old_value, "network_State12", None)
                if opp_val == self:
                    setattr(old_value, "network_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_State12"):
                opp_val = getattr(value, "network_State12", None)
                setattr(value, "network_State12", self)

    @property
    def network_Transition17(self):
        return self.__network_Transition17

    @network_Transition17.setter
    def network_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Transition__network_Transition17", None)
        self.__network_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_Channel18"):
                opp_val = getattr(old_value, "network_Channel18", None)
                if opp_val == self:
                    setattr(old_value, "network_Channel18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_Channel18"):
                opp_val = getattr(value, "network_Channel18", None)
                setattr(value, "network_Channel18", self)

    @property
    def network_Transition14(self):
        return self.__network_Transition14

    @network_Transition14.setter
    def network_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Transition__network_Transition14", None)
        self.__network_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_State15"):
                opp_val = getattr(old_value, "network_State15", None)
                if opp_val == self:
                    setattr(old_value, "network_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_State15"):
                opp_val = getattr(value, "network_State15", None)
                setattr(value, "network_State15", self)

    @property
    def network_Transition(self):
        return self.__network_Transition

    @network_Transition.setter
    def network_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Transition__network_Transition", None)
        self.__network_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_Statemachine9"):
                opp_val = getattr(old_value, "network_Statemachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_Statemachine9"):
                opp_val = getattr(value, "network_Statemachine9", None)
                if opp_val is None:
                    setattr(value, "network_Statemachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
