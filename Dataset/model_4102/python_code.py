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

class TrackElement:

    pass
class railway_Switch(TrackElement):

    def __init__(self, currentPosition: str, target: set["railway_SwitchPosition"] = None, Switch: "railway_SwitchPosition" = None):
        self.currentPosition = currentPosition
        self.target = target if target is not None else set()
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
                if hasattr(item, "SwitchPosition24"):
                    opp_val = getattr(item, "SwitchPosition24", None)
                    
                    if opp_val == self:
                        setattr(item, "SwitchPosition24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SwitchPosition24"):
                    opp_val = getattr(item, "SwitchPosition24", None)
                    
                    setattr(item, "SwitchPosition24", self)
                    

class railway_Segment(TrackElement):

    def __init__(self, length: int, railway_Segment: set["railway_Semaphore"] = None):
        self.length = length
        self.railway_Segment = railway_Segment if railway_Segment is not None else set()
        
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
                if hasattr(item, "railway_Semaphore22"):
                    opp_val = getattr(item, "railway_Semaphore22", None)
                    
                    if opp_val == self:
                        setattr(item, "railway_Semaphore22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railway_Semaphore22"):
                    opp_val = getattr(item, "railway_Semaphore22", None)
                    
                    setattr(item, "railway_Semaphore22", self)
                    

class RailwayElement:

    pass
class railway_SwitchPosition(RailwayElement):

    def __init__(self, position: str, SwitchPosition: "railway_Route" = None, SwitchPosition24: "railway_Switch" = None, follows: "railway_Route" = None, positions: "railway_Switch" = None):
        self.position = position
        self.SwitchPosition = SwitchPosition
        self.SwitchPosition24 = SwitchPosition24
        self.follows = follows
        self.positions = positions
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

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
    def SwitchPosition24(self):
        return self.__SwitchPosition24

    @SwitchPosition24.setter
    def SwitchPosition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_SwitchPosition__SwitchPosition24", None)
        self.__SwitchPosition24 = value
        
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

class railway_TrackElement(RailwayElement):

    pass
class railway_Sensor(RailwayElement):

    pass
class railway_Region(RailwayElement):

    pass
class railway_Route(RailwayElement):

    def __init__(self, active: bool, railway_Route9: set["railway_Sensor"] = None, railway_Route12: "railway_Semaphore" = None, railway_Route14: "railway_Semaphore" = None, railway_Route: "railway_RailwayContainer" = None, route: set["railway_SwitchPosition"] = None, Route: "railway_SwitchPosition" = None):
        self.active = active
        self.railway_Route9 = railway_Route9 if railway_Route9 is not None else set()
        self.railway_Route12 = railway_Route12
        self.railway_Route14 = railway_Route14
        self.railway_Route = railway_Route
        self.route = route if route is not None else set()
        self.Route = Route
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def railway_Route(self):
        return self.__railway_Route

    @railway_Route.setter
    def railway_Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__railway_Route", None)
        self.__railway_Route = value
        
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

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__route", None)
        self.__route = value if value is not None else set()
        
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
    def railway_Route9(self):
        return self.__railway_Route9

    @railway_Route9.setter
    def railway_Route9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__railway_Route9", None)
        self.__railway_Route9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railway_Sensor10"):
                    opp_val = getattr(item, "railway_Sensor10", None)
                    
                    if opp_val == self:
                        setattr(item, "railway_Sensor10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railway_Sensor10"):
                    opp_val = getattr(item, "railway_Sensor10", None)
                    
                    setattr(item, "railway_Sensor10", self)
                    

    @property
    def Route(self):
        return self.__Route

    @Route.setter
    def Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__Route", None)
        self.__Route = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "follows"):
                opp_val = getattr(old_value, "follows", None)
                if opp_val == self:
                    setattr(old_value, "follows", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "follows"):
                opp_val = getattr(value, "follows", None)
                setattr(value, "follows", self)

    @property
    def railway_Route12(self):
        return self.__railway_Route12

    @railway_Route12.setter
    def railway_Route12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__railway_Route12", None)
        self.__railway_Route12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Semaphore"):
                opp_val = getattr(old_value, "railway_Semaphore", None)
                if opp_val == self:
                    setattr(old_value, "railway_Semaphore", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Semaphore"):
                opp_val = getattr(value, "railway_Semaphore", None)
                setattr(value, "railway_Semaphore", self)

    @property
    def railway_Route14(self):
        return self.__railway_Route14

    @railway_Route14.setter
    def railway_Route14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Route__railway_Route14", None)
        self.__railway_Route14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Semaphore15"):
                opp_val = getattr(old_value, "railway_Semaphore15", None)
                if opp_val == self:
                    setattr(old_value, "railway_Semaphore15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Semaphore15"):
                opp_val = getattr(value, "railway_Semaphore15", None)
                setattr(value, "railway_Semaphore15", self)

class railway_RailwayContainer:

    pass
class railway_RailwayElement(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class railway_Semaphore(RailwayElement):

    def __init__(self, signal: str, railway_Semaphore: "railway_Route" = None, railway_Semaphore15: "railway_Route" = None, railway_Semaphore22: "railway_Segment" = None):
        self.signal = signal
        self.railway_Semaphore = railway_Semaphore
        self.railway_Semaphore15 = railway_Semaphore15
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
    def railway_Semaphore(self):
        return self.__railway_Semaphore

    @railway_Semaphore.setter
    def railway_Semaphore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore", None)
        self.__railway_Semaphore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Route12"):
                opp_val = getattr(old_value, "railway_Route12", None)
                if opp_val == self:
                    setattr(old_value, "railway_Route12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Route12"):
                opp_val = getattr(value, "railway_Route12", None)
                setattr(value, "railway_Route12", self)

    @property
    def railway_Semaphore15(self):
        return self.__railway_Semaphore15

    @railway_Semaphore15.setter
    def railway_Semaphore15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railway_Semaphore__railway_Semaphore15", None)
        self.__railway_Semaphore15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railway_Route14"):
                opp_val = getattr(old_value, "railway_Route14", None)
                if opp_val == self:
                    setattr(old_value, "railway_Route14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railway_Route14"):
                opp_val = getattr(value, "railway_Route14", None)
                setattr(value, "railway_Route14", self)
