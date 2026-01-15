from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Speed(Enum):
    ZERO = "ZERO"
    TWENTY = "TWENTY"
    FOURTY = "FOURTY"
    SIXTY = "SIXTY"
class TurnoutDirection(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    STRAIGHT = "STRAIGHT"
class ConnectionDirection(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    STRAIGHT = "STRAIGHT"
    TOP = "TOP"


############################################
# Definition of Classes
############################################

class Signal:

    pass
class RDM_TurnoutSignal(Signal):

    pass
class Section:

    pass
class TrackElement:

    pass
class RDM_RDMElement(ABC):

    def __init__(self, name: str, length: int):
        self.name = name
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RDM_Station(Section):

    pass
class RDMElement:

    pass
class RDM_RouteElement(RDMElement):

    pass
class RDM_Route(RDMElement):

    pass
class RDM_TurnoutDesiredDirection(RDMElement):

    def __init__(self, desiredDirection: str, RDM_TurnoutDesiredDirection: "RDM_RailwayDomainModel" = None, RDM_TurnoutDesiredDirection33: "RDM_Turnout" = None, desiredDirection: "RDM_RouteElement" = None, TurnoutDesiredDirection: "RDM_RouteElement" = None):
        self.desiredDirection = desiredDirection
        self.RDM_TurnoutDesiredDirection = RDM_TurnoutDesiredDirection
        self.RDM_TurnoutDesiredDirection33 = RDM_TurnoutDesiredDirection33
        self.desiredDirection = desiredDirection
        self.TurnoutDesiredDirection = TurnoutDesiredDirection
        
    @property
    def desiredDirection(self) -> str:
        return self.__desiredDirection

    @desiredDirection.setter
    def desiredDirection(self, desiredDirection: str):
        self.__desiredDirection = desiredDirection

    @property
    def TurnoutDesiredDirection(self):
        return self.__TurnoutDesiredDirection

    @TurnoutDesiredDirection.setter
    def TurnoutDesiredDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_TurnoutDesiredDirection__TurnoutDesiredDirection", None)
        self.__TurnoutDesiredDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "routeElement"):
                opp_val = getattr(old_value, "routeElement", None)
                if opp_val == self:
                    setattr(old_value, "routeElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "routeElement"):
                opp_val = getattr(value, "routeElement", None)
                setattr(value, "routeElement", self)

    @property
    def RDM_TurnoutDesiredDirection(self):
        return self.__RDM_TurnoutDesiredDirection

    @RDM_TurnoutDesiredDirection.setter
    def RDM_TurnoutDesiredDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_TurnoutDesiredDirection__RDM_TurnoutDesiredDirection", None)
        self.__RDM_TurnoutDesiredDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_RailwayDomainModel10"):
                opp_val = getattr(old_value, "RDM_RailwayDomainModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_RailwayDomainModel10"):
                opp_val = getattr(value, "RDM_RailwayDomainModel10", None)
                if opp_val is None:
                    setattr(value, "RDM_RailwayDomainModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDM_TurnoutDesiredDirection33(self):
        return self.__RDM_TurnoutDesiredDirection33

    @RDM_TurnoutDesiredDirection33.setter
    def RDM_TurnoutDesiredDirection33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_TurnoutDesiredDirection__RDM_TurnoutDesiredDirection33", None)
        self.__RDM_TurnoutDesiredDirection33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_Turnout34"):
                opp_val = getattr(old_value, "RDM_Turnout34", None)
                if opp_val == self:
                    setattr(old_value, "RDM_Turnout34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_Turnout34"):
                opp_val = getattr(value, "RDM_Turnout34", None)
                setattr(value, "RDM_Turnout34", self)

    @property
    def desiredDirection(self):
        return self.__desiredDirection

    @desiredDirection.setter
    def desiredDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_TurnoutDesiredDirection__desiredDirection", None)
        self.__desiredDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RouteElement36"):
                opp_val = getattr(old_value, "RouteElement36", None)
                if opp_val == self:
                    setattr(old_value, "RouteElement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RouteElement36"):
                opp_val = getattr(value, "RouteElement36", None)
                setattr(value, "RouteElement36", self)

class RDM_Signal(RDMElement):

    def __init__(self, allowedSpeed: str, holds: "RDM_ConnectionPoint" = None, RDM_Signal26: "RDM_TrackElement" = None, RDM_Signal: "RDM_RailwayDomainModel" = None, RDM_Signal39: "RDM_Station" = None, Signal: "RDM_ConnectionPoint" = None):
        self.allowedSpeed = allowedSpeed
        self.holds = holds
        self.RDM_Signal26 = RDM_Signal26
        self.RDM_Signal = RDM_Signal
        self.RDM_Signal39 = RDM_Signal39
        self.Signal = Signal
        
    @property
    def allowedSpeed(self) -> str:
        return self.__allowedSpeed

    @allowedSpeed.setter
    def allowedSpeed(self, allowedSpeed: str):
        self.__allowedSpeed = allowedSpeed

    @property
    def RDM_Signal26(self):
        return self.__RDM_Signal26

    @RDM_Signal26.setter
    def RDM_Signal26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Signal__RDM_Signal26", None)
        self.__RDM_Signal26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_TrackElement"):
                opp_val = getattr(old_value, "RDM_TrackElement", None)
                if opp_val == self:
                    setattr(old_value, "RDM_TrackElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_TrackElement"):
                opp_val = getattr(value, "RDM_TrackElement", None)
                setattr(value, "RDM_TrackElement", self)

    @property
    def holds(self):
        return self.__holds

    @holds.setter
    def holds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Signal__holds", None)
        self.__holds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConnectionPoint"):
                opp_val = getattr(old_value, "ConnectionPoint", None)
                if opp_val == self:
                    setattr(old_value, "ConnectionPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConnectionPoint"):
                opp_val = getattr(value, "ConnectionPoint", None)
                setattr(value, "ConnectionPoint", self)

    @property
    def Signal(self):
        return self.__Signal

    @Signal.setter
    def Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Signal__Signal", None)
        self.__Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standsOn41"):
                opp_val = getattr(old_value, "standsOn41", None)
                if opp_val == self:
                    setattr(old_value, "standsOn41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standsOn41"):
                opp_val = getattr(value, "standsOn41", None)
                setattr(value, "standsOn41", self)

    @property
    def RDM_Signal39(self):
        return self.__RDM_Signal39

    @RDM_Signal39.setter
    def RDM_Signal39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Signal__RDM_Signal39", None)
        self.__RDM_Signal39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_Station38"):
                opp_val = getattr(old_value, "RDM_Station38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_Station38"):
                opp_val = getattr(value, "RDM_Station38", None)
                if opp_val is None:
                    setattr(value, "RDM_Station38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDM_Signal(self):
        return self.__RDM_Signal

    @RDM_Signal.setter
    def RDM_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Signal__RDM_Signal", None)
        self.__RDM_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_RailwayDomainModel8"):
                opp_val = getattr(old_value, "RDM_RailwayDomainModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_RailwayDomainModel8"):
                opp_val = getattr(value, "RDM_RailwayDomainModel8", None)
                if opp_val is None:
                    setattr(value, "RDM_RailwayDomainModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RDM_ConnectionPoint(RDMElement):

    def __init__(self, direction: str, ConnectionPoint: "RDM_Signal" = None, RDM_ConnectionPoint29: "RDM_TrackElement" = None, RDM_ConnectionPoint: "RDM_RailwayDomainModel" = None, standsOn41: "RDM_Signal" = None, RDM_ConnectionPoint43: "RDM_TrackElement" = None):
        self.direction = direction
        self.ConnectionPoint = ConnectionPoint
        self.RDM_ConnectionPoint29 = RDM_ConnectionPoint29
        self.RDM_ConnectionPoint = RDM_ConnectionPoint
        self.standsOn41 = standsOn41
        self.RDM_ConnectionPoint43 = RDM_ConnectionPoint43
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def RDM_ConnectionPoint29(self):
        return self.__RDM_ConnectionPoint29

    @RDM_ConnectionPoint29.setter
    def RDM_ConnectionPoint29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_ConnectionPoint__RDM_ConnectionPoint29", None)
        self.__RDM_ConnectionPoint29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_TrackElement28"):
                opp_val = getattr(old_value, "RDM_TrackElement28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_TrackElement28"):
                opp_val = getattr(value, "RDM_TrackElement28", None)
                if opp_val is None:
                    setattr(value, "RDM_TrackElement28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def standsOn41(self):
        return self.__standsOn41

    @standsOn41.setter
    def standsOn41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_ConnectionPoint__standsOn41", None)
        self.__standsOn41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signal"):
                opp_val = getattr(old_value, "Signal", None)
                if opp_val == self:
                    setattr(old_value, "Signal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signal"):
                opp_val = getattr(value, "Signal", None)
                setattr(value, "Signal", self)

    @property
    def RDM_ConnectionPoint(self):
        return self.__RDM_ConnectionPoint

    @RDM_ConnectionPoint.setter
    def RDM_ConnectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_ConnectionPoint__RDM_ConnectionPoint", None)
        self.__RDM_ConnectionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_RailwayDomainModel6"):
                opp_val = getattr(old_value, "RDM_RailwayDomainModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_RailwayDomainModel6"):
                opp_val = getattr(value, "RDM_RailwayDomainModel6", None)
                if opp_val is None:
                    setattr(value, "RDM_RailwayDomainModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDM_ConnectionPoint43(self):
        return self.__RDM_ConnectionPoint43

    @RDM_ConnectionPoint43.setter
    def RDM_ConnectionPoint43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_ConnectionPoint__RDM_ConnectionPoint43", None)
        self.__RDM_ConnectionPoint43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_TrackElement44"):
                opp_val = getattr(old_value, "RDM_TrackElement44", None)
                if opp_val == self:
                    setattr(old_value, "RDM_TrackElement44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_TrackElement44"):
                opp_val = getattr(value, "RDM_TrackElement44", None)
                setattr(value, "RDM_TrackElement44", self)

    @property
    def ConnectionPoint(self):
        return self.__ConnectionPoint

    @ConnectionPoint.setter
    def ConnectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_ConnectionPoint__ConnectionPoint", None)
        self.__ConnectionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "holds"):
                opp_val = getattr(old_value, "holds", None)
                if opp_val == self:
                    setattr(old_value, "holds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "holds"):
                opp_val = getattr(value, "holds", None)
                setattr(value, "holds", self)

class RDM_Turnout(TrackElement):

    def __init__(self, currentDirection: str, switchingDirection: str, RDM_Turnout: "RDM_RailwayDomainModel" = None, RDM_Turnout34: "RDM_TurnoutDesiredDirection" = None, RDM_Turnout54: "RDM_TurnoutSignal" = None):
        self.currentDirection = currentDirection
        self.switchingDirection = switchingDirection
        self.RDM_Turnout = RDM_Turnout
        self.RDM_Turnout34 = RDM_Turnout34
        self.RDM_Turnout54 = RDM_Turnout54
        
    @property
    def currentDirection(self) -> str:
        return self.__currentDirection

    @currentDirection.setter
    def currentDirection(self, currentDirection: str):
        self.__currentDirection = currentDirection

    @property
    def switchingDirection(self) -> str:
        return self.__switchingDirection

    @switchingDirection.setter
    def switchingDirection(self, switchingDirection: str):
        self.__switchingDirection = switchingDirection

    @property
    def RDM_Turnout(self):
        return self.__RDM_Turnout

    @RDM_Turnout.setter
    def RDM_Turnout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Turnout__RDM_Turnout", None)
        self.__RDM_Turnout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_RailwayDomainModel4"):
                opp_val = getattr(old_value, "RDM_RailwayDomainModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_RailwayDomainModel4"):
                opp_val = getattr(value, "RDM_RailwayDomainModel4", None)
                if opp_val is None:
                    setattr(value, "RDM_RailwayDomainModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDM_Turnout34(self):
        return self.__RDM_Turnout34

    @RDM_Turnout34.setter
    def RDM_Turnout34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Turnout__RDM_Turnout34", None)
        self.__RDM_Turnout34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_TurnoutDesiredDirection33"):
                opp_val = getattr(old_value, "RDM_TurnoutDesiredDirection33", None)
                if opp_val == self:
                    setattr(old_value, "RDM_TurnoutDesiredDirection33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_TurnoutDesiredDirection33"):
                opp_val = getattr(value, "RDM_TurnoutDesiredDirection33", None)
                setattr(value, "RDM_TurnoutDesiredDirection33", self)

    @property
    def RDM_Turnout54(self):
        return self.__RDM_Turnout54

    @RDM_Turnout54.setter
    def RDM_Turnout54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Turnout__RDM_Turnout54", None)
        self.__RDM_Turnout54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_TurnoutSignal"):
                opp_val = getattr(old_value, "RDM_TurnoutSignal", None)
                if opp_val == self:
                    setattr(old_value, "RDM_TurnoutSignal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_TurnoutSignal"):
                opp_val = getattr(value, "RDM_TurnoutSignal", None)
                setattr(value, "RDM_TurnoutSignal", self)

class RDM_Section(TrackElement):

    pass
class RDM_TrackElement(RDMElement):

    pass
class RDM_Train(RDMElement):

    def __init__(self, headingSpeed: str, maxSpeed: str, RDM_Train: "RDM_RailwayDomainModel" = None, RDM_Train18: "RDM_Station" = None, RDM_Train21: "RDM_Route" = None, occupiedBy: set["RDM_TrackElement"] = None, RDM_Train16: "RDM_Station" = None, Train: "RDM_TrackElement" = None):
        self.headingSpeed = headingSpeed
        self.maxSpeed = maxSpeed
        self.RDM_Train = RDM_Train
        self.RDM_Train18 = RDM_Train18
        self.RDM_Train21 = RDM_Train21
        self.occupiedBy = occupiedBy if occupiedBy is not None else set()
        self.RDM_Train16 = RDM_Train16
        self.Train = Train
        
    @property
    def maxSpeed(self) -> str:
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed: str):
        self.__maxSpeed = maxSpeed

    @property
    def headingSpeed(self) -> str:
        return self.__headingSpeed

    @headingSpeed.setter
    def headingSpeed(self, headingSpeed: str):
        self.__headingSpeed = headingSpeed

    @property
    def Train(self):
        return self.__Train

    @Train.setter
    def Train(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__Train", None)
        self.__Train = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standsOn"):
                opp_val = getattr(old_value, "standsOn", None)
                if opp_val == self:
                    setattr(old_value, "standsOn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standsOn"):
                opp_val = getattr(value, "standsOn", None)
                setattr(value, "standsOn", self)

    @property
    def RDM_Train18(self):
        return self.__RDM_Train18

    @RDM_Train18.setter
    def RDM_Train18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__RDM_Train18", None)
        self.__RDM_Train18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_Station19"):
                opp_val = getattr(old_value, "RDM_Station19", None)
                if opp_val == self:
                    setattr(old_value, "RDM_Station19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_Station19"):
                opp_val = getattr(value, "RDM_Station19", None)
                setattr(value, "RDM_Station19", self)

    @property
    def RDM_Train21(self):
        return self.__RDM_Train21

    @RDM_Train21.setter
    def RDM_Train21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__RDM_Train21", None)
        self.__RDM_Train21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_Route22"):
                opp_val = getattr(old_value, "RDM_Route22", None)
                if opp_val == self:
                    setattr(old_value, "RDM_Route22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_Route22"):
                opp_val = getattr(value, "RDM_Route22", None)
                setattr(value, "RDM_Route22", self)

    @property
    def occupiedBy(self):
        return self.__occupiedBy

    @occupiedBy.setter
    def occupiedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__occupiedBy", None)
        self.__occupiedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrackElement"):
                    opp_val = getattr(item, "TrackElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TrackElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrackElement"):
                    opp_val = getattr(item, "TrackElement", None)
                    
                    setattr(item, "TrackElement", self)
                    

    @property
    def RDM_Train16(self):
        return self.__RDM_Train16

    @RDM_Train16.setter
    def RDM_Train16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__RDM_Train16", None)
        self.__RDM_Train16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_Station"):
                opp_val = getattr(old_value, "RDM_Station", None)
                if opp_val == self:
                    setattr(old_value, "RDM_Station", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_Station"):
                opp_val = getattr(value, "RDM_Station", None)
                setattr(value, "RDM_Station", self)

    @property
    def RDM_Train(self):
        return self.__RDM_Train

    @RDM_Train.setter
    def RDM_Train(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDM_Train__RDM_Train", None)
        self.__RDM_Train = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDM_RailwayDomainModel"):
                opp_val = getattr(old_value, "RDM_RailwayDomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDM_RailwayDomainModel"):
                opp_val = getattr(value, "RDM_RailwayDomainModel", None)
                if opp_val is None:
                    setattr(value, "RDM_RailwayDomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RDM_RailwayDomainModel:

    pass