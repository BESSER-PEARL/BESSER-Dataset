from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VertexKind(Enum):
    InnerVertex = "InnerVertex"
    TrackEnd = "TrackEnd"
    StationBorder = "StationBorder"
class PointKind(Enum):
    FixedCrossing = "FixedCrossing"
    SimplePoint = "SimplePoint"
    DoublePoint = "DoublePoint"
    SingleSlipPoint = "SingleSlipPoint"
    DoubleSlipPoint = "DoubleSlipPoint"
class Side(Enum):
    Both = "Both"
    Right = "Right"
    Left = "Left"
class TrainRouteKind(Enum):
    Main = "Main"
    Shunting = "Shunting"
class SpeedLimit(Enum):
    Stop = "Stop"
    Speed40 = "Speed40"
    Speed80 = "Speed80"
    Speed120 = "Speed120"
    Max = "Max"
class Orientation(Enum):
    Forwards = "Forwards"
    Backwards = "Backwards"


############################################
# Definition of Classes
############################################

class TrainRouteObject:

    pass
class railDsl_TrainRouteSegment(TrainRouteObject):

    pass
class railDsl_TrainRoutePoint(TrainRouteObject):

    def __init__(self, selectedInput: int, selectedOutput: int, railDsl_TrainRoutePoint: "railDsl_Point" = None):
        self.selectedInput = selectedInput
        self.selectedOutput = selectedOutput
        self.railDsl_TrainRoutePoint = railDsl_TrainRoutePoint
        
    @property
    def selectedInput(self) -> int:
        return self.__selectedInput

    @selectedInput.setter
    def selectedInput(self, selectedInput: int):
        self.__selectedInput = selectedInput

    @property
    def selectedOutput(self) -> int:
        return self.__selectedOutput

    @selectedOutput.setter
    def selectedOutput(self, selectedOutput: int):
        self.__selectedOutput = selectedOutput

    @property
    def railDsl_TrainRoutePoint(self):
        return self.__railDsl_TrainRoutePoint

    @railDsl_TrainRoutePoint.setter
    def railDsl_TrainRoutePoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoutePoint__railDsl_TrainRoutePoint", None)
        self.__railDsl_TrainRoutePoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Point41"):
                opp_val = getattr(old_value, "railDsl_Point41", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Point41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Point41"):
                opp_val = getattr(value, "railDsl_Point41", None)
                setattr(value, "railDsl_Point41", self)

class railDsl_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class railDsl_TrainRouteObject:

    def __init__(self, speedLimit: str, railDsl_TrainRouteObject: "railDsl_TrainRoute" = None, railDsl_TrainRouteObject36: "railDsl_TrainRoute" = None):
        self.speedLimit = speedLimit
        self.railDsl_TrainRouteObject = railDsl_TrainRouteObject
        self.railDsl_TrainRouteObject36 = railDsl_TrainRouteObject36
        
    @property
    def speedLimit(self) -> str:
        return self.__speedLimit

    @speedLimit.setter
    def speedLimit(self, speedLimit: str):
        self.__speedLimit = speedLimit

    @property
    def railDsl_TrainRouteObject36(self):
        return self.__railDsl_TrainRouteObject36

    @railDsl_TrainRouteObject36.setter
    def railDsl_TrainRouteObject36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRouteObject__railDsl_TrainRouteObject36", None)
        self.__railDsl_TrainRouteObject36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoute35"):
                opp_val = getattr(old_value, "railDsl_TrainRoute35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoute35"):
                opp_val = getattr(value, "railDsl_TrainRoute35", None)
                if opp_val is None:
                    setattr(value, "railDsl_TrainRoute35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railDsl_TrainRouteObject(self):
        return self.__railDsl_TrainRouteObject

    @railDsl_TrainRouteObject.setter
    def railDsl_TrainRouteObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRouteObject__railDsl_TrainRouteObject", None)
        self.__railDsl_TrainRouteObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoute"):
                opp_val = getattr(old_value, "railDsl_TrainRoute", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoute"):
                opp_val = getattr(value, "railDsl_TrainRoute", None)
                if opp_val is None:
                    setattr(value, "railDsl_TrainRoute", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class railDsl_RouteObject(ABC):

    def __init__(self, speedLimit: str, error: bool):
        self.speedLimit = speedLimit
        self.error = error
        
    @property
    def error(self) -> bool:
        return self.__error

    @error.setter
    def error(self, error: bool):
        self.__error = error

    @property
    def speedLimit(self) -> str:
        return self.__speedLimit

    @speedLimit.setter
    def speedLimit(self, speedLimit: str):
        self.__speedLimit = speedLimit

class railDsl_TrainSegment:

    def __init__(self, length: float, railDsl_TrainSegment: "railDsl_Train" = None, railDsl_TrainSegment25: "railDsl_SegmentPosition" = None):
        self.length = length
        self.railDsl_TrainSegment = railDsl_TrainSegment
        self.railDsl_TrainSegment25 = railDsl_TrainSegment25
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def railDsl_TrainSegment25(self):
        return self.__railDsl_TrainSegment25

    @railDsl_TrainSegment25.setter
    def railDsl_TrainSegment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainSegment__railDsl_TrainSegment25", None)
        self.__railDsl_TrainSegment25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_SegmentPosition26"):
                opp_val = getattr(old_value, "railDsl_SegmentPosition26", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_SegmentPosition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_SegmentPosition26"):
                opp_val = getattr(value, "railDsl_SegmentPosition26", None)
                setattr(value, "railDsl_SegmentPosition26", self)

    @property
    def railDsl_TrainSegment(self):
        return self.__railDsl_TrainSegment

    @railDsl_TrainSegment.setter
    def railDsl_TrainSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainSegment__railDsl_TrainSegment", None)
        self.__railDsl_TrainSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Train"):
                opp_val = getattr(old_value, "railDsl_Train", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Train"):
                opp_val = getattr(value, "railDsl_Train", None)
                if opp_val is None:
                    setattr(value, "railDsl_Train", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SegmentObject:

    pass
class railDsl_Derailer(SegmentObject):

    def __init__(self, active: bool):
        self.active = active
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

class railDsl_SegmentPosition:

    def __init__(self, atStart: bool, atEnd: bool, position: float, side: str, orientation: str, railDsl_SegmentPosition12: "railDsl_Segment" = None, railDsl_SegmentPosition: "railDsl_SegmentObject" = None, railDsl_SegmentPosition23: "railDsl_Train" = None, railDsl_SegmentPosition26: "railDsl_TrainSegment" = None):
        self.atStart = atStart
        self.atEnd = atEnd
        self.position = position
        self.side = side
        self.orientation = orientation
        self.railDsl_SegmentPosition12 = railDsl_SegmentPosition12
        self.railDsl_SegmentPosition = railDsl_SegmentPosition
        self.railDsl_SegmentPosition23 = railDsl_SegmentPosition23
        self.railDsl_SegmentPosition26 = railDsl_SegmentPosition26
        
    @property
    def position(self) -> float:
        return self.__position

    @position.setter
    def position(self, position: float):
        self.__position = position

    @property
    def atEnd(self) -> bool:
        return self.__atEnd

    @atEnd.setter
    def atEnd(self, atEnd: bool):
        self.__atEnd = atEnd

    @property
    def side(self) -> str:
        return self.__side

    @side.setter
    def side(self, side: str):
        self.__side = side

    @property
    def atStart(self) -> bool:
        return self.__atStart

    @atStart.setter
    def atStart(self, atStart: bool):
        self.__atStart = atStart

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def railDsl_SegmentPosition26(self):
        return self.__railDsl_SegmentPosition26

    @railDsl_SegmentPosition26.setter
    def railDsl_SegmentPosition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_SegmentPosition__railDsl_SegmentPosition26", None)
        self.__railDsl_SegmentPosition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainSegment25"):
                opp_val = getattr(old_value, "railDsl_TrainSegment25", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_TrainSegment25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainSegment25"):
                opp_val = getattr(value, "railDsl_TrainSegment25", None)
                setattr(value, "railDsl_TrainSegment25", self)

    @property
    def railDsl_SegmentPosition(self):
        return self.__railDsl_SegmentPosition

    @railDsl_SegmentPosition.setter
    def railDsl_SegmentPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_SegmentPosition__railDsl_SegmentPosition", None)
        self.__railDsl_SegmentPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_SegmentObject8"):
                opp_val = getattr(old_value, "railDsl_SegmentObject8", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_SegmentObject8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_SegmentObject8"):
                opp_val = getattr(value, "railDsl_SegmentObject8", None)
                setattr(value, "railDsl_SegmentObject8", self)

    @property
    def railDsl_SegmentPosition23(self):
        return self.__railDsl_SegmentPosition23

    @railDsl_SegmentPosition23.setter
    def railDsl_SegmentPosition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_SegmentPosition__railDsl_SegmentPosition23", None)
        self.__railDsl_SegmentPosition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Train22"):
                opp_val = getattr(old_value, "railDsl_Train22", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Train22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Train22"):
                opp_val = getattr(value, "railDsl_Train22", None)
                setattr(value, "railDsl_Train22", self)

    @property
    def railDsl_SegmentPosition12(self):
        return self.__railDsl_SegmentPosition12

    @railDsl_SegmentPosition12.setter
    def railDsl_SegmentPosition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_SegmentPosition__railDsl_SegmentPosition12", None)
        self.__railDsl_SegmentPosition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Segment13"):
                opp_val = getattr(old_value, "railDsl_Segment13", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Segment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Segment13"):
                opp_val = getattr(value, "railDsl_Segment13", None)
                setattr(value, "railDsl_Segment13", self)

class TrackObject:

    pass
class railDsl_Segment(TrackObject):

    pass
class RouteObject:

    pass
class Declaration:

    pass
class railDsl_Train(Declaration):

    def __init__(self, length: float, speed: float, acceleration: float, railDsl_Train: set["railDsl_TrainSegment"] = None, railDsl_Train22: "railDsl_SegmentPosition" = None):
        self.length = length
        self.speed = speed
        self.acceleration = acceleration
        self.railDsl_Train = railDsl_Train if railDsl_Train is not None else set()
        self.railDsl_Train22 = railDsl_Train22
        
    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        self.__speed = speed

    @property
    def acceleration(self) -> float:
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, acceleration: float):
        self.__acceleration = acceleration

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def railDsl_Train(self):
        return self.__railDsl_Train

    @railDsl_Train.setter
    def railDsl_Train(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Train__railDsl_Train", None)
        self.__railDsl_Train = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_TrainSegment"):
                    opp_val = getattr(item, "railDsl_TrainSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_TrainSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_TrainSegment"):
                    opp_val = getattr(item, "railDsl_TrainSegment", None)
                    
                    setattr(item, "railDsl_TrainSegment", self)
                    

    @property
    def railDsl_Train22(self):
        return self.__railDsl_Train22

    @railDsl_Train22.setter
    def railDsl_Train22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Train__railDsl_Train22", None)
        self.__railDsl_Train22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_SegmentPosition23"):
                opp_val = getattr(old_value, "railDsl_SegmentPosition23", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_SegmentPosition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_SegmentPosition23"):
                opp_val = getattr(value, "railDsl_SegmentPosition23", None)
                setattr(value, "railDsl_SegmentPosition23", self)

class railDsl_Track(Declaration):

    pass
class railDsl_Vertex(Declaration):

    def __init__(self, kind: str, railDsl_Vertex15: "railDsl_Point" = None, railDsl_Vertex18: "railDsl_Point" = None, railDsl_Vertex: "railDsl_Segment" = None, railDsl_Vertex4: "railDsl_Segment" = None):
        self.kind = kind
        self.railDsl_Vertex15 = railDsl_Vertex15
        self.railDsl_Vertex18 = railDsl_Vertex18
        self.railDsl_Vertex = railDsl_Vertex
        self.railDsl_Vertex4 = railDsl_Vertex4
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def railDsl_Vertex18(self):
        return self.__railDsl_Vertex18

    @railDsl_Vertex18.setter
    def railDsl_Vertex18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Vertex__railDsl_Vertex18", None)
        self.__railDsl_Vertex18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Point17"):
                opp_val = getattr(old_value, "railDsl_Point17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Point17"):
                opp_val = getattr(value, "railDsl_Point17", None)
                if opp_val is None:
                    setattr(value, "railDsl_Point17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railDsl_Vertex(self):
        return self.__railDsl_Vertex

    @railDsl_Vertex.setter
    def railDsl_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Vertex__railDsl_Vertex", None)
        self.__railDsl_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Segment"):
                opp_val = getattr(old_value, "railDsl_Segment", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Segment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Segment"):
                opp_val = getattr(value, "railDsl_Segment", None)
                setattr(value, "railDsl_Segment", self)

    @property
    def railDsl_Vertex15(self):
        return self.__railDsl_Vertex15

    @railDsl_Vertex15.setter
    def railDsl_Vertex15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Vertex__railDsl_Vertex15", None)
        self.__railDsl_Vertex15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Point"):
                opp_val = getattr(old_value, "railDsl_Point", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Point"):
                opp_val = getattr(value, "railDsl_Point", None)
                if opp_val is None:
                    setattr(value, "railDsl_Point", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railDsl_Vertex4(self):
        return self.__railDsl_Vertex4

    @railDsl_Vertex4.setter
    def railDsl_Vertex4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Vertex__railDsl_Vertex4", None)
        self.__railDsl_Vertex4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Segment3"):
                opp_val = getattr(old_value, "railDsl_Segment3", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Segment3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Segment3"):
                opp_val = getattr(value, "railDsl_Segment3", None)
                setattr(value, "railDsl_Segment3", self)

class railDsl_TrainRoute(Declaration):

    def __init__(self, kind: str, locked: bool, railDsl_TrainRoute: set["railDsl_TrainRouteObject"] = None, railDsl_TrainRoute29: "railDsl_Signal" = None, railDsl_TrainRoute32: "railDsl_Signal" = None, railDsl_TrainRoute35: set["railDsl_TrainRouteObject"] = None, railDsl_TrainRoute39: "railDsl_TrainRoute" = None, railDsl_TrainRoute37: set["railDsl_TrainRoute"] = None):
        self.kind = kind
        self.locked = locked
        self.railDsl_TrainRoute = railDsl_TrainRoute if railDsl_TrainRoute is not None else set()
        self.railDsl_TrainRoute29 = railDsl_TrainRoute29
        self.railDsl_TrainRoute32 = railDsl_TrainRoute32
        self.railDsl_TrainRoute35 = railDsl_TrainRoute35 if railDsl_TrainRoute35 is not None else set()
        self.railDsl_TrainRoute39 = railDsl_TrainRoute39
        self.railDsl_TrainRoute37 = railDsl_TrainRoute37 if railDsl_TrainRoute37 is not None else set()
        
    @property
    def locked(self) -> bool:
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def railDsl_TrainRoute39(self):
        return self.__railDsl_TrainRoute39

    @railDsl_TrainRoute39.setter
    def railDsl_TrainRoute39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute39", None)
        self.__railDsl_TrainRoute39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoute37"):
                opp_val = getattr(old_value, "railDsl_TrainRoute37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoute37"):
                opp_val = getattr(value, "railDsl_TrainRoute37", None)
                if opp_val is None:
                    setattr(value, "railDsl_TrainRoute37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def railDsl_TrainRoute35(self):
        return self.__railDsl_TrainRoute35

    @railDsl_TrainRoute35.setter
    def railDsl_TrainRoute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute35", None)
        self.__railDsl_TrainRoute35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_TrainRouteObject36"):
                    opp_val = getattr(item, "railDsl_TrainRouteObject36", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_TrainRouteObject36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_TrainRouteObject36"):
                    opp_val = getattr(item, "railDsl_TrainRouteObject36", None)
                    
                    setattr(item, "railDsl_TrainRouteObject36", self)
                    

    @property
    def railDsl_TrainRoute29(self):
        return self.__railDsl_TrainRoute29

    @railDsl_TrainRoute29.setter
    def railDsl_TrainRoute29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute29", None)
        self.__railDsl_TrainRoute29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Signal30"):
                opp_val = getattr(old_value, "railDsl_Signal30", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Signal30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Signal30"):
                opp_val = getattr(value, "railDsl_Signal30", None)
                setattr(value, "railDsl_Signal30", self)

    @property
    def railDsl_TrainRoute32(self):
        return self.__railDsl_TrainRoute32

    @railDsl_TrainRoute32.setter
    def railDsl_TrainRoute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute32", None)
        self.__railDsl_TrainRoute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Signal33"):
                opp_val = getattr(old_value, "railDsl_Signal33", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Signal33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Signal33"):
                opp_val = getattr(value, "railDsl_Signal33", None)
                setattr(value, "railDsl_Signal33", self)

    @property
    def railDsl_TrainRoute37(self):
        return self.__railDsl_TrainRoute37

    @railDsl_TrainRoute37.setter
    def railDsl_TrainRoute37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute37", None)
        self.__railDsl_TrainRoute37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_TrainRoute39"):
                    opp_val = getattr(item, "railDsl_TrainRoute39", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_TrainRoute39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_TrainRoute39"):
                    opp_val = getattr(item, "railDsl_TrainRoute39", None)
                    
                    setattr(item, "railDsl_TrainRoute39", self)
                    

    @property
    def railDsl_TrainRoute(self):
        return self.__railDsl_TrainRoute

    @railDsl_TrainRoute.setter
    def railDsl_TrainRoute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrainRoute__railDsl_TrainRoute", None)
        self.__railDsl_TrainRoute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_TrainRouteObject"):
                    opp_val = getattr(item, "railDsl_TrainRouteObject", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_TrainRouteObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_TrainRouteObject"):
                    opp_val = getattr(item, "railDsl_TrainRouteObject", None)
                    
                    setattr(item, "railDsl_TrainRouteObject", self)
                    

class railDsl_TrackObject(Declaration, RouteObject):

    def __init__(self, length: float, railDsl_TrackObject: "railDsl_Track" = None):
        self.length = length
        self.railDsl_TrackObject = railDsl_TrackObject
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def railDsl_TrackObject(self):
        return self.__railDsl_TrackObject

    @railDsl_TrackObject.setter
    def railDsl_TrackObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_TrackObject__railDsl_TrackObject", None)
        self.__railDsl_TrackObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Track"):
                opp_val = getattr(old_value, "railDsl_Track", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Track"):
                opp_val = getattr(value, "railDsl_Track", None)
                if opp_val is None:
                    setattr(value, "railDsl_Track", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class railDsl_Point(TrackObject):

    def __init__(self, kind: str, selectedInput: int, selectedOutput: int, locked: bool, railDsl_Point: set["railDsl_Vertex"] = None, railDsl_Point17: set["railDsl_Vertex"] = None, railDsl_Point41: "railDsl_TrainRoutePoint" = None):
        self.kind = kind
        self.selectedInput = selectedInput
        self.selectedOutput = selectedOutput
        self.locked = locked
        self.railDsl_Point = railDsl_Point if railDsl_Point is not None else set()
        self.railDsl_Point17 = railDsl_Point17 if railDsl_Point17 is not None else set()
        self.railDsl_Point41 = railDsl_Point41
        
    @property
    def selectedOutput(self) -> int:
        return self.__selectedOutput

    @selectedOutput.setter
    def selectedOutput(self, selectedOutput: int):
        self.__selectedOutput = selectedOutput

    @property
    def locked(self) -> bool:
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked

    @property
    def selectedInput(self) -> int:
        return self.__selectedInput

    @selectedInput.setter
    def selectedInput(self, selectedInput: int):
        self.__selectedInput = selectedInput

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def railDsl_Point17(self):
        return self.__railDsl_Point17

    @railDsl_Point17.setter
    def railDsl_Point17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Point__railDsl_Point17", None)
        self.__railDsl_Point17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_Vertex18"):
                    opp_val = getattr(item, "railDsl_Vertex18", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_Vertex18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_Vertex18"):
                    opp_val = getattr(item, "railDsl_Vertex18", None)
                    
                    setattr(item, "railDsl_Vertex18", self)
                    

    @property
    def railDsl_Point(self):
        return self.__railDsl_Point

    @railDsl_Point.setter
    def railDsl_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Point__railDsl_Point", None)
        self.__railDsl_Point = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "railDsl_Vertex15"):
                    opp_val = getattr(item, "railDsl_Vertex15", None)
                    
                    if opp_val == self:
                        setattr(item, "railDsl_Vertex15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "railDsl_Vertex15"):
                    opp_val = getattr(item, "railDsl_Vertex15", None)
                    
                    setattr(item, "railDsl_Vertex15", self)
                    

    @property
    def railDsl_Point41(self):
        return self.__railDsl_Point41

    @railDsl_Point41.setter
    def railDsl_Point41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Point__railDsl_Point41", None)
        self.__railDsl_Point41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoutePoint"):
                opp_val = getattr(old_value, "railDsl_TrainRoutePoint", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_TrainRoutePoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoutePoint"):
                opp_val = getattr(value, "railDsl_TrainRoutePoint", None)
                setattr(value, "railDsl_TrainRoutePoint", self)

class railDsl_Platform(SegmentObject):

    def __init__(self, length: float):
        self.length = length
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

class railDsl_Signal(SegmentObject):

    def __init__(self, main: bool, shunting: bool, railDsl_Signal: "railDsl_Signal" = None, railDsl_Signal9: "railDsl_Signal" = None, railDsl_Signal30: "railDsl_TrainRoute" = None, railDsl_Signal33: "railDsl_TrainRoute" = None):
        self.main = main
        self.shunting = shunting
        self.railDsl_Signal = railDsl_Signal
        self.railDsl_Signal9 = railDsl_Signal9
        self.railDsl_Signal30 = railDsl_Signal30
        self.railDsl_Signal33 = railDsl_Signal33
        
    @property
    def shunting(self) -> bool:
        return self.__shunting

    @shunting.setter
    def shunting(self, shunting: bool):
        self.__shunting = shunting

    @property
    def main(self) -> bool:
        return self.__main

    @main.setter
    def main(self, main: bool):
        self.__main = main

    @property
    def railDsl_Signal(self):
        return self.__railDsl_Signal

    @railDsl_Signal.setter
    def railDsl_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Signal__railDsl_Signal", None)
        self.__railDsl_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Signal9"):
                opp_val = getattr(old_value, "railDsl_Signal9", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Signal9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Signal9"):
                opp_val = getattr(value, "railDsl_Signal9", None)
                setattr(value, "railDsl_Signal9", self)

    @property
    def railDsl_Signal30(self):
        return self.__railDsl_Signal30

    @railDsl_Signal30.setter
    def railDsl_Signal30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Signal__railDsl_Signal30", None)
        self.__railDsl_Signal30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoute29"):
                opp_val = getattr(old_value, "railDsl_TrainRoute29", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_TrainRoute29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoute29"):
                opp_val = getattr(value, "railDsl_TrainRoute29", None)
                setattr(value, "railDsl_TrainRoute29", self)

    @property
    def railDsl_Signal33(self):
        return self.__railDsl_Signal33

    @railDsl_Signal33.setter
    def railDsl_Signal33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Signal__railDsl_Signal33", None)
        self.__railDsl_Signal33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_TrainRoute32"):
                opp_val = getattr(old_value, "railDsl_TrainRoute32", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_TrainRoute32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_TrainRoute32"):
                opp_val = getattr(value, "railDsl_TrainRoute32", None)
                setattr(value, "railDsl_TrainRoute32", self)

    @property
    def railDsl_Signal9(self):
        return self.__railDsl_Signal9

    @railDsl_Signal9.setter
    def railDsl_Signal9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_railDsl_Signal__railDsl_Signal9", None)
        self.__railDsl_Signal9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "railDsl_Signal"):
                opp_val = getattr(old_value, "railDsl_Signal", None)
                if opp_val == self:
                    setattr(old_value, "railDsl_Signal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "railDsl_Signal"):
                opp_val = getattr(value, "railDsl_Signal", None)
                setattr(value, "railDsl_Signal", self)

class railDsl_LevelCrossing(SegmentObject):

    def __init__(self, closed: bool, length: float):
        self.closed = closed
        self.length = length
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def closed(self) -> bool:
        return self.__closed

    @closed.setter
    def closed(self, closed: bool):
        self.__closed = closed

class NamedElement:

    pass
class railDsl_Declaration(NamedElement):

    pass
class railDsl_SegmentObject(NamedElement, RouteObject):

    pass
class railDsl_Station(NamedElement):

    pass