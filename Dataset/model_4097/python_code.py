from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Signal(Enum):
    Failure = "Failure"
    STOP = "STOP"
    Go = "Go"


############################################
# Definition of Classes
############################################

class TrackElement:

    pass
class Train5_Segment(TrackElement):

    pass
class Train5_Station(TrackElement):

    pass
class Train5_Switch(TrackElement):

    pass
class NamedElement:

    pass
class Train5_Route(NamedElement):

    def __init__(self, currentIndex: str, speed: str, leftOver: str, Train5_Route: "Train5_TrackElement" = None, Train5_Route2: set["Train5_RoutePart"] = None, Train5_Route13: "Train5_RailwayDiagram" = None):
        self.currentIndex = currentIndex
        self.speed = speed
        self.leftOver = leftOver
        self.Train5_Route = Train5_Route
        self.Train5_Route2 = Train5_Route2 if Train5_Route2 is not None else set()
        self.Train5_Route13 = Train5_Route13
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def currentIndex(self) -> str:
        return self.__currentIndex

    @currentIndex.setter
    def currentIndex(self, currentIndex: str):
        self.__currentIndex = currentIndex

    @property
    def leftOver(self) -> str:
        return self.__leftOver

    @leftOver.setter
    def leftOver(self, leftOver: str):
        self.__leftOver = leftOver

    @property
    def Train5_Route13(self):
        return self.__Train5_Route13

    @Train5_Route13.setter
    def Train5_Route13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_Route__Train5_Route13", None)
        self.__Train5_Route13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Train5_RailwayDiagram12"):
                opp_val = getattr(old_value, "Train5_RailwayDiagram12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Train5_RailwayDiagram12"):
                opp_val = getattr(value, "Train5_RailwayDiagram12", None)
                if opp_val is None:
                    setattr(value, "Train5_RailwayDiagram12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Train5_Route(self):
        return self.__Train5_Route

    @Train5_Route.setter
    def Train5_Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_Route__Train5_Route", None)
        self.__Train5_Route = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Train5_TrackElement"):
                opp_val = getattr(old_value, "Train5_TrackElement", None)
                if opp_val == self:
                    setattr(old_value, "Train5_TrackElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Train5_TrackElement"):
                opp_val = getattr(value, "Train5_TrackElement", None)
                setattr(value, "Train5_TrackElement", self)

    @property
    def Train5_Route2(self):
        return self.__Train5_Route2

    @Train5_Route2.setter
    def Train5_Route2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_Route__Train5_Route2", None)
        self.__Train5_Route2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Train5_RoutePart"):
                    opp_val = getattr(item, "Train5_RoutePart", None)
                    
                    if opp_val == self:
                        setattr(item, "Train5_RoutePart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Train5_RoutePart"):
                    opp_val = getattr(item, "Train5_RoutePart", None)
                    
                    setattr(item, "Train5_RoutePart", self)
                    

class Train5_SensorNetwork(NamedElement):

    pass
class Train5_RoutePart(NamedElement):

    pass
class Train5_TrackElement(NamedElement):

    def __init__(self, State: str, length: str, Train5_TrackElement: "Train5_Route" = None, Train5_TrackElement7: "Train5_RailwayDiagram" = None, Train5_TrackElement19: "Train5_RoutePart" = None):
        self.State = State
        self.length = length
        self.Train5_TrackElement = Train5_TrackElement
        self.Train5_TrackElement7 = Train5_TrackElement7
        self.Train5_TrackElement19 = Train5_TrackElement19
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def State(self) -> str:
        return self.__State

    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Train5_TrackElement(self):
        return self.__Train5_TrackElement

    @Train5_TrackElement.setter
    def Train5_TrackElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_TrackElement__Train5_TrackElement", None)
        self.__Train5_TrackElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Train5_Route"):
                opp_val = getattr(old_value, "Train5_Route", None)
                if opp_val == self:
                    setattr(old_value, "Train5_Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Train5_Route"):
                opp_val = getattr(value, "Train5_Route", None)
                setattr(value, "Train5_Route", self)

    @property
    def Train5_TrackElement7(self):
        return self.__Train5_TrackElement7

    @Train5_TrackElement7.setter
    def Train5_TrackElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_TrackElement__Train5_TrackElement7", None)
        self.__Train5_TrackElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Train5_RailwayDiagram"):
                opp_val = getattr(old_value, "Train5_RailwayDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Train5_RailwayDiagram"):
                opp_val = getattr(value, "Train5_RailwayDiagram", None)
                if opp_val is None:
                    setattr(value, "Train5_RailwayDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Train5_TrackElement19(self):
        return self.__Train5_TrackElement19

    @Train5_TrackElement19.setter
    def Train5_TrackElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train5_TrackElement__Train5_TrackElement19", None)
        self.__Train5_TrackElement19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Train5_RoutePart18"):
                opp_val = getattr(old_value, "Train5_RoutePart18", None)
                if opp_val == self:
                    setattr(old_value, "Train5_RoutePart18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Train5_RoutePart18"):
                opp_val = getattr(value, "Train5_RoutePart18", None)
                setattr(value, "Train5_RoutePart18", self)

class Train5_NamedElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Train5_RailwayDiagram:

    pass