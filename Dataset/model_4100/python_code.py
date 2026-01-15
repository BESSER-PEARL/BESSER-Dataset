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
    STRAIGHT = "STRAIGHT"
    DIVERGING = "DIVERGING"


############################################
# Definition of Classes
############################################

class railway_RailwayElement(ABC):

    def __init__(self, _id: int):
        self._id = _id
        
    @property
    def _id(self) -> int:
        return self.___id

    @_id.setter
    def _id(self, _id: int):
        self.___id = _id

class railway_RailwayContainer:

    pass
class TrackElement:

    pass
class railway_Segment(TrackElement):

    def __init__(self, length: int, railway_Segment: set["railway_Semaphore"] = None, railway_Segment2: set["railway_TrackElement"] = None):
        self.length = length
        self.railway_Segment = railway_Segment if railway_Segment is not None else set()
        self.railway_Segment2 = railway_Segment2 if railway_Segment2 is not None else set()
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def railway_Segment(self):
        return self.__railway_Segment

    @railway_Segment.setter
    def railway_Segment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Segment__railway_Segment", None)
        self.__railway_Segment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railway_Semaphore"):
                    opp_val = getattr(item, "railway_Semaphore", None)
                    
                    if opp_val == self:
                        setattr(item, "railway_Semaphore", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railway_Semaphore"):
                    opp_val = getattr(item, "railway_Semaphore", None)
                    
                    setattr(item, "railway_Semaphore", self)
                    

    @property
    def railway_Segment2(self):
        return self.__railway_Segment2

    @railway_Segment2.setter
    def railway_Segment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Segment__railway_Segment2", None)
        self.__railway_Segment2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railway_TrackElement"):
                    opp_val = getattr(item, "railway_TrackElement", None)
                    
                    if opp_val == self:
                        setattr(item, "railway_TrackElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railway_TrackElement"):
                    opp_val = getattr(item, "railway_TrackElement", None)
                    
                    setattr(item, "railway_TrackElement", self)
                    

class railway_Switch(TrackElement):

    def __init__(self, currentPosition: str, target: set["railway_SwitchPosition"] = None, railway_Switch: "railway_TrackElement" = None, railway_Switch11: "railway_TrackElement" = None, railway_Switch14: "railway_TrackElement" = None, Switch: "railway_SwitchPosition" = None):
        self.currentPosition = currentPosition
        self.target = target if target is not None else set()
        self.railway_Switch = railway_Switch
        self.railway_Switch11 = railway_Switch11
        self.railway_Switch14 = railway_Switch14
        self.Switch = Switch
        
    @property
    def currentPosition(self) -> str:
        return self.__currentPosition

    @currentPosition.setter
    def currentPosition(self, currentPosition: str):
        self.__currentPosition = currentPosition

    @property
    def railway_Switch14(self):
        return self.__railway_Switch14

    @railway_Switch14.setter
    def railway_Switch14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__railway_Switch14", None)
        self.__railway_Switch14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_TrackElement15"):
                opp_val = getattr(old_value, "railway_TrackElement15", None)
                if opp_val == self:
                    setattr(old_value, "railway_TrackElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_TrackElement15"):
                opp_val = getattr(value, "railway_TrackElement15", None)
                setattr(value, "railway_TrackElement15", self)

    @property
    def railway_Switch11(self):
        return self.__railway_Switch11

    @railway_Switch11.setter
    def railway_Switch11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__railway_Switch11", None)
        self.__railway_Switch11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_TrackElement12"):
                opp_val = getattr(old_value, "railway_TrackElement12", None)
                if opp_val == self:
                    setattr(old_value, "railway_TrackElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_TrackElement12"):
                opp_val = getattr(value, "railway_TrackElement12", None)
                setattr(value, "railway_TrackElement12", self)

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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__target", None)
        self.__target = value if value is not None else set()
        
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
                    

    @property
    def railway_Switch(self):
        return self.__railway_Switch

    @railway_Switch.setter
    def railway_Switch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Switch__railway_Switch", None)
        self.__railway_Switch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_TrackElement9"):
                opp_val = getattr(old_value, "railway_TrackElement9", None)
                if opp_val == self:
                    setattr(old_value, "railway_TrackElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_TrackElement9"):
                opp_val = getattr(value, "railway_TrackElement9", None)
                setattr(value, "railway_TrackElement9", self)

class RailwayElement:

    pass
class railway_Semaphore(RailwayElement):

    def __init__(self, signal: str, railway_Semaphore: "railway_Segment" = None, railway_Semaphore17: "railway_Route" = None, railway_Semaphore22: "railway_Route" = None):
        self.signal = signal
        self.railway_Semaphore = railway_Semaphore
        self.railway_Semaphore17 = railway_Semaphore17
        self.railway_Semaphore22 = railway_Semaphore22
        
    @property
    def signal(self) -> str:
        return self.__signal

    @signal.setter
    def signal(self, signal: str):
        self.__signal = signal

    @property
    def railway_Semaphore22(self):
        return self.__railway_Semaphore22

    @railway_Semaphore22.setter
    def railway_Semaphore22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore22", None)
        self.__railway_Semaphore22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Route21"):
                opp_val = getattr(old_value, "railway_Route21", None)
                if opp_val == self:
                    setattr(old_value, "railway_Route21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Route21"):
                opp_val = getattr(value, "railway_Route21", None)
                setattr(value, "railway_Route21", self)

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
            if hasattr(old_value, "railway_Segment"):
                opp_val = getattr(old_value, "railway_Segment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Segment"):
                opp_val = getattr(value, "railway_Segment", None)
                if opp_val is None:
                    setattr(value, "railway_Segment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railway_Semaphore17(self):
        return self.__railway_Semaphore17

    @railway_Semaphore17.setter
    def railway_Semaphore17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore17", None)
        self.__railway_Semaphore17 = value
        
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

class railway_Region(RailwayElement):

    pass
class railway_Sensor(RailwayElement):

    pass
class railway_SwitchPosition(RailwayElement):

    def __init__(self, position: str, SwitchPosition: "railway_Switch" = None, SwitchPosition19: "railway_Route" = None, positions: "railway_Switch" = None, follows: "railway_Route" = None):
        self.position = position
        self.SwitchPosition = SwitchPosition
        self.SwitchPosition19 = SwitchPosition19
        self.positions = positions
        self.follows = follows
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

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
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SwitchPosition19(self):
        return self.__SwitchPosition19

    @SwitchPosition19.setter
    def SwitchPosition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__SwitchPosition19", None)
        self.__SwitchPosition19 = value
        
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

class railway_Route(RailwayElement):

    pass
class railway_TrackElement(RailwayElement):

    pass