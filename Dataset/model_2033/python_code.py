from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Event(Enum):
    SEND = "SEND"
    RECEIVE = "RECEIVE"
class TypeOfChannel(Enum):
    Synchronous = "Synchronous"
    Asynchronous = "Asynchronous"


############################################
# Definition of Classes
############################################

class network_ChannelBuffer:

    pass
class network_CurrentStateMapState:

    pass
class network_RunTimeNetwork:

    def __init__(self, network_RunTimeNetwork: "network_Network" = None, network_RunTimeNetwork22: set["network_CurrentStateMapState"] = None, network_RunTimeNetwork24: set["network_ChannelBuffer"] = None):
        self.network_RunTimeNetwork = network_RunTimeNetwork
        self.network_RunTimeNetwork22 = network_RunTimeNetwork22 if network_RunTimeNetwork22 is not None else set()
        self.network_RunTimeNetwork24 = network_RunTimeNetwork24 if network_RunTimeNetwork24 is not None else set()
        
    @property
    def network_RunTimeNetwork(self):
        return self.__network_RunTimeNetwork

    @network_RunTimeNetwork.setter
    def network_RunTimeNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_RunTimeNetwork__network_RunTimeNetwork", None)
        self.__network_RunTimeNetwork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_Network20"):
                opp_val = getattr(old_value, "network_Network20", None)
                if opp_val == self:
                    setattr(old_value, "network_Network20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_Network20"):
                opp_val = getattr(value, "network_Network20", None)
                setattr(value, "network_Network20", self)

    @property
    def network_RunTimeNetwork22(self):
        return self.__network_RunTimeNetwork22

    @network_RunTimeNetwork22.setter
    def network_RunTimeNetwork22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_RunTimeNetwork__network_RunTimeNetwork22", None)
        self.__network_RunTimeNetwork22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "network_CurrentStateMapState"):
                    opp_val = getattr(item, "network_CurrentStateMapState", None)
                    
                    if opp_val == self:
                        setattr(item, "network_CurrentStateMapState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "network_CurrentStateMapState"):
                    opp_val = getattr(item, "network_CurrentStateMapState", None)
                    
                    setattr(item, "network_CurrentStateMapState", self)
                    

    @property
    def network_RunTimeNetwork24(self):
        return self.__network_RunTimeNetwork24

    @network_RunTimeNetwork24.setter
    def network_RunTimeNetwork24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_RunTimeNetwork__network_RunTimeNetwork24", None)
        self.__network_RunTimeNetwork24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "network_ChannelBuffer"):
                    opp_val = getattr(item, "network_ChannelBuffer", None)
                    
                    if opp_val == self:
                        setattr(item, "network_ChannelBuffer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "network_ChannelBuffer"):
                    opp_val = getattr(item, "network_ChannelBuffer", None)
                    
                    setattr(item, "network_ChannelBuffer", self)
                    

    def makeStep(self):
        # TODO: Implement makeStep method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

class network_AbstractElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class network_Transition:

    def __init__(self, Event: str, network_Transition17: "network_Channel" = None, network_Transition: "network_Statemachine" = None, network_Transition11: "network_State" = None, network_Transition14: "network_State" = None):
        self.Event = Event
        self.network_Transition17 = network_Transition17
        self.network_Transition = network_Transition
        self.network_Transition11 = network_Transition11
        self.network_Transition14 = network_Transition14
        
    @property
    def Event(self) -> str:
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event

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

class AbstractElement:

    pass
class network_Statemachine(AbstractElement):

    pass
class network_Network(AbstractElement):

    pass
class network_State(AbstractElement):

    pass
class network_Channel(AbstractElement):

    def __init__(self, Type: str, network_Channel: "network_Network" = None, network_Channel18: "network_Transition" = None, network_Channel30: "network_ChannelBuffer" = None):
        self.Type = Type
        self.network_Channel = network_Channel
        self.network_Channel18 = network_Channel18
        self.network_Channel30 = network_Channel30
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

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

    @property
    def network_Channel30(self):
        return self.__network_Channel30

    @network_Channel30.setter
    def network_Channel30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_Channel__network_Channel30", None)
        self.__network_Channel30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "network_ChannelBuffer29"):
                opp_val = getattr(old_value, "network_ChannelBuffer29", None)
                if opp_val == self:
                    setattr(old_value, "network_ChannelBuffer29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "network_ChannelBuffer29"):
                opp_val = getattr(value, "network_ChannelBuffer29", None)
                setattr(value, "network_ChannelBuffer29", self)

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
