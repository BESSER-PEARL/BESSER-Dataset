from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Signal(Enum):
    FAILURE = "FAILURE"
    STOP = "STOP"
    GO = "GO"
class Position(Enum):
    FAILURE = "FAILURE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    STRAIGHT = "STRAIGHT"


############################################
# Definition of Classes
############################################

class railway_RailwayContainer:

    pass
class TrackElement:

    pass
class railway_Segment(TrackElement):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class railway_RailwayElement(ABC):

    def __init__(self, id: int, railway_RailwayElement: "railway_RailwayContainer" = None):
        self.id = id
        self.railway_RailwayElement = railway_RailwayElement
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def railway_RailwayElement(self):
        return self.__railway_RailwayElement

    @railway_RailwayElement.setter
    def railway_RailwayElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_RailwayElement__railway_RailwayElement", None)
        self.__railway_RailwayElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_RailwayContainer"):
                opp_val = getattr(old_value, "railway_RailwayContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_RailwayContainer"):
                opp_val = getattr(value, "railway_RailwayContainer", None)
                if opp_val is None:
                    setattr(value, "railway_RailwayContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class railway_Switch(TrackElement):

    def __init__(self, currentPosition: str, switch: set["railway_SwitchPosition"] = None, Switch: "railway_SwitchPosition" = None):
        self.currentPosition = currentPosition
        self.switch = switch if switch is not None else set()
        self.Switch = Switch
        
    @property
    def currentPosition(self) -> str:
        return self.__currentPosition

    @currentPosition.setter
    def currentPosition(self, currentPosition: str):
        self.__currentPosition = currentPosition

    @property
    def Switch(self):
        return self.__Switch

    @Switch.setter
    def Switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__Switch", None)
        self.__Switch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "positions"):
                opp_val = getattr(old_value, "positions", None)
                if opp_val == self:
                    setattr(old_value, "positions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "positions"):
                opp_val = getattr(value, "positions", None)
                setattr(value, "positions", self)

    @property
    def switch(self):
        return self.__switch

    @switch.setter
    def switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__switch", None)
        self.__switch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SwitchPosition"):
                    opp_val = getattr(item, "SwitchPosition", None)
                    
                    if opp_val == self:
                        setattr(item, "SwitchPosition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SwitchPosition"):
                    opp_val = getattr(item, "SwitchPosition", None)
                    
                    setattr(item, "SwitchPosition", self)
                    

class RailwayElement:

    pass
class railway_Sensor(RailwayElement):

    pass
class railway_Semaphore(RailwayElement):

    def __init__(self, signal: str, railway_Semaphore: "railway_Route" = None, railway_Semaphore9: "railway_Route" = None, railway_Semaphore18: "railway_RailwayContainer" = None):
        self.signal = signal
        self.railway_Semaphore = railway_Semaphore
        self.railway_Semaphore9 = railway_Semaphore9
        self.railway_Semaphore18 = railway_Semaphore18
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def railway_Semaphore9(self):
        return self.__railway_Semaphore9

    @railway_Semaphore9.setter
    def railway_Semaphore9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore9", None)
        self.__railway_Semaphore9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Route8"):
                opp_val = getattr(old_value, "railway_Route8", None)
                if opp_val == self:
                    setattr(old_value, "railway_Route8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Route8"):
                opp_val = getattr(value, "railway_Route8", None)
                setattr(value, "railway_Route8", self)

    @property
    def railway_Semaphore18(self):
        return self.__railway_Semaphore18

    @railway_Semaphore18.setter
    def railway_Semaphore18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore18", None)
        self.__railway_Semaphore18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_RailwayContainer17"):
                opp_val = getattr(old_value, "railway_RailwayContainer17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_RailwayContainer17"):
                opp_val = getattr(value, "railway_RailwayContainer17", None)
                if opp_val is None:
                    setattr(value, "railway_RailwayContainer17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railway_Semaphore(self):
        return self.__railway_Semaphore

    @railway_Semaphore.setter
    def railway_Semaphore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore", None)
        self.__railway_Semaphore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Route"):
                opp_val = getattr(old_value, "railway_Route", None)
                if opp_val == self:
                    setattr(old_value, "railway_Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Route"):
                opp_val = getattr(value, "railway_Route", None)
                setattr(value, "railway_Route", self)

class railway_Route(RailwayElement):

    pass
class railway_SwitchPosition(RailwayElement):

    def __init__(self, position: str, SwitchPosition: "railway_Switch" = None, SwitchPosition6: "railway_Route" = None, positions: "railway_Switch" = None, follows: "railway_Route" = None):
        self.position = position
        self.SwitchPosition = SwitchPosition
        self.SwitchPosition6 = SwitchPosition6
        self.positions = positions
        self.follows = follows
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def SwitchPosition(self):
        return self.__SwitchPosition

    @SwitchPosition.setter
    def SwitchPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__SwitchPosition", None)
        self.__SwitchPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "switch"):
                opp_val = getattr(old_value, "switch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "switch"):
                opp_val = getattr(value, "switch", None)
                if opp_val is None:
                    setattr(value, "switch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SwitchPosition6(self):
        return self.__SwitchPosition6

    @SwitchPosition6.setter
    def SwitchPosition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__SwitchPosition6", None)
        self.__SwitchPosition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "route"):
                opp_val = getattr(old_value, "route", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "route"):
                opp_val = getattr(value, "route", None)
                if opp_val is None:
                    setattr(value, "route", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__positions", None)
        self.__positions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Switch"):
                opp_val = getattr(old_value, "Switch", None)
                if opp_val == self:
                    setattr(old_value, "Switch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Switch"):
                opp_val = getattr(value, "Switch", None)
                setattr(value, "Switch", self)

    @property
    def follows(self):
        return self.__follows

    @follows.setter
    def follows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__follows", None)
        self.__follows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Route"):
                opp_val = getattr(old_value, "Route", None)
                if opp_val == self:
                    setattr(old_value, "Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Route"):
                opp_val = getattr(value, "Route", None)
                setattr(value, "Route", self)

class railway_TrackElement(RailwayElement):

    pass