from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class surveillance_Clock:

    def __init__(self, now: int):
        self.now = now
        
    @property
    def now(self) -> int:
        return self.__now

    @now.setter
    def now(self, now: int):
        self.__now = now

class surveillance_ProbableElement(ABC):

    def __init__(self, confidence: float):
        self.confidence = confidence
        
    @property
    def confidence(self) -> float:
        return self.__confidence

    @confidence.setter
    def confidence(self, confidence: float):
        self.__confidence = confidence

class surveillance_Coordinate:

    def __init__(self, x: float, y: float, shootingPosition: "surveillance_GunShot" = None, currentPosition: "surveillance_MovingObject" = None, Coordinate: "surveillance_MovingObject" = None, Coordinate8: "surveillance_GunShot" = None):
        self.x = x
        self.y = y
        self.shootingPosition = shootingPosition
        self.currentPosition = currentPosition
        self.Coordinate = Coordinate
        self.Coordinate8 = Coordinate8
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def Coordinate8(self):
        return self.__Coordinate8

    @Coordinate8.setter
    def Coordinate8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_Coordinate__Coordinate8", None)
        self.__Coordinate8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shot"):
                opp_val = getattr(old_value, "shot", None)
                if opp_val == self:
                    setattr(old_value, "shot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shot"):
                opp_val = getattr(value, "shot", None)
                setattr(value, "shot", self)

    @property
    def shootingPosition(self):
        return self.__shootingPosition

    @shootingPosition.setter
    def shootingPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_Coordinate__shootingPosition", None)
        self.__shootingPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GunShot"):
                opp_val = getattr(old_value, "GunShot", None)
                if opp_val == self:
                    setattr(old_value, "GunShot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GunShot"):
                opp_val = getattr(value, "GunShot", None)
                setattr(value, "GunShot", self)

    @property
    def Coordinate(self):
        return self.__Coordinate

    @Coordinate.setter
    def Coordinate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_Coordinate__Coordinate", None)
        self.__Coordinate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "object"):
                opp_val = getattr(old_value, "object", None)
                if opp_val == self:
                    setattr(old_value, "object", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "object"):
                opp_val = getattr(value, "object", None)
                setattr(value, "object", self)

    @property
    def currentPosition(self):
        return self.__currentPosition

    @currentPosition.setter
    def currentPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_Coordinate__currentPosition", None)
        self.__currentPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MovingObject"):
                opp_val = getattr(old_value, "MovingObject", None)
                if opp_val == self:
                    setattr(old_value, "MovingObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MovingObject"):
                opp_val = getattr(value, "MovingObject", None)
                setattr(value, "MovingObject", self)

    def distance(self, other: str) -> float:
        # TODO: Implement distance method
        pass

class ProbableElement:

    pass
class MovingObject:

    pass
class surveillance_UnidentifiedObject(ProbableElement, MovingObject):

    pass
class surveillance_Drone(MovingObject):

    pass
class surveillance_MovingObject(ABC):

    def __init__(self, width: float, angle: float, speed: float, MovingObject: "surveillance_Coordinate" = None, object: "surveillance_Coordinate" = None):
        self.width = width
        self.angle = angle
        self.speed = speed
        self.MovingObject = MovingObject
        self.object = object
        
    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        self.__speed = speed

    @property
    def MovingObject(self):
        return self.__MovingObject

    @MovingObject.setter
    def MovingObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_MovingObject__MovingObject", None)
        self.__MovingObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "currentPosition"):
                opp_val = getattr(old_value, "currentPosition", None)
                if opp_val == self:
                    setattr(old_value, "currentPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "currentPosition"):
                opp_val = getattr(value, "currentPosition", None)
                setattr(value, "currentPosition", self)

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_MovingObject__object", None)
        self.__object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coordinate"):
                opp_val = getattr(old_value, "Coordinate", None)
                if opp_val == self:
                    setattr(old_value, "Coordinate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coordinate"):
                opp_val = getattr(value, "Coordinate", None)
                setattr(value, "Coordinate", self)

    def move(self, seconds: int):
        # TODO: Implement move method
        pass

class surveillance_GunShot(ProbableElement):

    def __init__(self, angle: float, hitsTarget: bool, GunShot: "surveillance_Coordinate" = None, GunShot4: "surveillance_Drone" = None, GunShot6: "surveillance_UnidentifiedObject" = None, shot: "surveillance_Coordinate" = None, shot10: "surveillance_Drone" = None, shot12: "surveillance_UnidentifiedObject" = None):
        self.angle = angle
        self.hitsTarget = hitsTarget
        self.GunShot = GunShot
        self.GunShot4 = GunShot4
        self.GunShot6 = GunShot6
        self.shot = shot
        self.shot10 = shot10
        self.shot12 = shot12
        
    @property
    def hitsTarget(self) -> bool:
        return self.__hitsTarget

    @hitsTarget.setter
    def hitsTarget(self, hitsTarget: bool):
        self.__hitsTarget = hitsTarget

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle

    @property
    def GunShot(self):
        return self.__GunShot

    @GunShot.setter
    def GunShot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__GunShot", None)
        self.__GunShot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shootingPosition"):
                opp_val = getattr(old_value, "shootingPosition", None)
                if opp_val == self:
                    setattr(old_value, "shootingPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shootingPosition"):
                opp_val = getattr(value, "shootingPosition", None)
                setattr(value, "shootingPosition", self)

    @property
    def shot12(self):
        return self.__shot12

    @shot12.setter
    def shot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__shot12", None)
        self.__shot12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnidentifiedObject"):
                opp_val = getattr(old_value, "UnidentifiedObject", None)
                if opp_val == self:
                    setattr(old_value, "UnidentifiedObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnidentifiedObject"):
                opp_val = getattr(value, "UnidentifiedObject", None)
                setattr(value, "UnidentifiedObject", self)

    @property
    def shot10(self):
        return self.__shot10

    @shot10.setter
    def shot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__shot10", None)
        self.__shot10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Drone"):
                opp_val = getattr(old_value, "Drone", None)
                if opp_val == self:
                    setattr(old_value, "Drone", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Drone"):
                opp_val = getattr(value, "Drone", None)
                setattr(value, "Drone", self)

    @property
    def shot(self):
        return self.__shot

    @shot.setter
    def shot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__shot", None)
        self.__shot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coordinate8"):
                opp_val = getattr(old_value, "Coordinate8", None)
                if opp_val == self:
                    setattr(old_value, "Coordinate8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coordinate8"):
                opp_val = getattr(value, "Coordinate8", None)
                setattr(value, "Coordinate8", self)

    @property
    def GunShot6(self):
        return self.__GunShot6

    @GunShot6.setter
    def GunShot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__GunShot6", None)
        self.__GunShot6 = value
        
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
    def GunShot4(self):
        return self.__GunShot4

    @GunShot4.setter
    def GunShot4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_surveillance_GunShot__GunShot4", None)
        self.__GunShot4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone"):
                opp_val = getattr(old_value, "drone", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone"):
                opp_val = getattr(value, "drone", None)
                if opp_val is None:
                    setattr(value, "drone", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
