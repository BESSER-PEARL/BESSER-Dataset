from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GoToStrategy(Enum):
    DIRECT = "DIRECT"
    HORIZONTAL_FIRST = "HORIZONTAL_FIRST"
    VERTICAL_FIRST = "VERTICAL_FIRST"
class TravelMode(Enum):
    SAFE = "SAFE"
    NORMAL = "NORMAL"
    AGGRESSIVE = "AGGRESSIVE"


############################################
# Definition of Classes
############################################

class behaviour_Parameter:

    def __init__(self, key: str, value: str, behaviour_Parameter39: "behaviour_Feedback" = None, behaviour_Parameter: "behaviour_DeviceAction" = None):
        self.key = key
        self.value = value
        self.behaviour_Parameter39 = behaviour_Parameter39
        self.behaviour_Parameter = behaviour_Parameter
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def behaviour_Parameter(self):
        return self.__behaviour_Parameter

    @behaviour_Parameter.setter
    def behaviour_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Parameter__behaviour_Parameter", None)
        self.__behaviour_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_DeviceAction"):
                opp_val = getattr(old_value, "behaviour_DeviceAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_DeviceAction"):
                opp_val = getattr(value, "behaviour_DeviceAction", None)
                if opp_val is None:
                    setattr(value, "behaviour_DeviceAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Parameter39(self):
        return self.__behaviour_Parameter39

    @behaviour_Parameter39.setter
    def behaviour_Parameter39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Parameter__behaviour_Parameter39", None)
        self.__behaviour_Parameter39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Feedback"):
                opp_val = getattr(old_value, "behaviour_Feedback", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Feedback"):
                opp_val = getattr(value, "behaviour_Feedback", None)
                if opp_val is None:
                    setattr(value, "behaviour_Feedback", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Notify:

    pass
class behaviour_MulticastNotify(Notify):

    pass
class behaviour_UnicastNotify(Notify):

    pass
class behaviour_BroadcastNotify(Notify):

    pass
class CommunicationAction:

    pass
class behaviour_CheckNotification(CommunicationAction):

    pass
class behaviour_Feedback(CommunicationAction):

    def __init__(self, actionName: str, behaviour_Feedback: set["behaviour_Parameter"] = None):
        self.actionName = actionName
        self.behaviour_Feedback = behaviour_Feedback if behaviour_Feedback is not None else set()
        
    @property
    def actionName(self) -> str:
        return self.__actionName

    @actionName.setter
    def actionName(self, actionName: str):
        self.__actionName = actionName

    @property
    def behaviour_Feedback(self):
        return self.__behaviour_Feedback

    @behaviour_Feedback.setter
    def behaviour_Feedback(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Feedback__behaviour_Feedback", None)
        self.__behaviour_Feedback = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Parameter39"):
                    opp_val = getattr(item, "behaviour_Parameter39", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Parameter39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Parameter39"):
                    opp_val = getattr(item, "behaviour_Parameter39", None)
                    
                    setattr(item, "behaviour_Parameter39", self)
                    

class behaviour_Notify(CommunicationAction):

    pass
class Action:

    pass
class behaviour_DeviceAction(Action):

    def __init__(self, actionName: str, behaviour_DeviceAction: set["behaviour_Parameter"] = None):
        self.actionName = actionName
        self.behaviour_DeviceAction = behaviour_DeviceAction if behaviour_DeviceAction is not None else set()
        
    @property
    def actionName(self) -> str:
        return self.__actionName

    @actionName.setter
    def actionName(self, actionName: str):
        self.__actionName = actionName

    @property
    def behaviour_DeviceAction(self):
        return self.__behaviour_DeviceAction

    @behaviour_DeviceAction.setter
    def behaviour_DeviceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DeviceAction__behaviour_DeviceAction", None)
        self.__behaviour_DeviceAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Parameter"):
                    opp_val = getattr(item, "behaviour_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Parameter"):
                    opp_val = getattr(item, "behaviour_Parameter", None)
                    
                    setattr(item, "behaviour_Parameter", self)
                    

class behaviour_CommunicationAction(Action):

    pass
class NamedElement:

    pass
class behaviour_Behaviour(NamedElement):

    def __init__(self, crs: str, behaviour_Behaviour: set["behaviour_Drone"] = None):
        self.crs = crs
        self.behaviour_Behaviour = behaviour_Behaviour if behaviour_Behaviour is not None else set()
        
    @property
    def crs(self) -> str:
        return self.__crs

    @crs.setter
    def crs(self, crs: str):
        self.__crs = crs

    @property
    def behaviour_Behaviour(self):
        return self.__behaviour_Behaviour

    @behaviour_Behaviour.setter
    def behaviour_Behaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Behaviour__behaviour_Behaviour", None)
        self.__behaviour_Behaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Drone"):
                    opp_val = getattr(item, "behaviour_Drone", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Drone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Drone"):
                    opp_val = getattr(item, "behaviour_Drone", None)
                    
                    setattr(item, "behaviour_Drone", self)
                    

class MoveTransition:

    pass
class behaviour_Choice(MoveTransition):

    def __init__(self, conditionIdentifier: str, behaviour_Choice: "behaviour_Move" = None):
        self.conditionIdentifier = conditionIdentifier
        self.behaviour_Choice = behaviour_Choice
        
    @property
    def conditionIdentifier(self) -> str:
        return self.__conditionIdentifier

    @conditionIdentifier.setter
    def conditionIdentifier(self, conditionIdentifier: str):
        self.__conditionIdentifier = conditionIdentifier

    @property
    def behaviour_Choice(self):
        return self.__behaviour_Choice

    @behaviour_Choice.setter
    def behaviour_Choice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Choice__behaviour_Choice", None)
        self.__behaviour_Choice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Move10"):
                opp_val = getattr(old_value, "behaviour_Move10", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Move10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Move10"):
                opp_val = getattr(value, "behaviour_Move10", None)
                setattr(value, "behaviour_Move10", self)

class Move:

    pass
class behaviour_Hover(Move):

    def __init__(self, duration: float):
        self.duration = duration
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

class behaviour_Stop(Move):

    pass
class behaviour_HeadTo(Move):

    def __init__(self, direction: float):
        self.direction = direction
        
    @property
    def direction(self) -> float:
        return self.__direction

    @direction.setter
    def direction(self, direction: float):
        self.__direction = direction

class behaviour_GoTo(Move):

    def __init__(self, strategy: str, behaviour_GoTo: "behaviour_Coordinate" = None):
        self.strategy = strategy
        self.behaviour_GoTo = behaviour_GoTo
        
    @property
    def strategy(self) -> str:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: str):
        self.__strategy = strategy

    @property
    def behaviour_GoTo(self):
        return self.__behaviour_GoTo

    @behaviour_GoTo.setter
    def behaviour_GoTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_GoTo__behaviour_GoTo", None)
        self.__behaviour_GoTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Coordinate17"):
                opp_val = getattr(old_value, "behaviour_Coordinate17", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Coordinate17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Coordinate17"):
                opp_val = getattr(value, "behaviour_Coordinate17", None)
                setattr(value, "behaviour_Coordinate17", self)

class behaviour_Land(Move):

    pass
class behaviour_TakeOff(Move):

    def __init__(self, altitude: float):
        self.altitude = altitude
        
    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

class behaviour_Circle(Move):

    def __init__(self, duration: float, radius: float, altitude: float, clockwise: bool, behaviour_Circle: "behaviour_Coordinate" = None):
        self.duration = duration
        self.radius = radius
        self.altitude = altitude
        self.clockwise = clockwise
        self.behaviour_Circle = behaviour_Circle
        
    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def clockwise(self) -> bool:
        return self.__clockwise

    @clockwise.setter
    def clockwise(self, clockwise: bool):
        self.__clockwise = clockwise

    @property
    def behaviour_Circle(self):
        return self.__behaviour_Circle

    @behaviour_Circle.setter
    def behaviour_Circle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Circle__behaviour_Circle", None)
        self.__behaviour_Circle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Coordinate19"):
                opp_val = getattr(old_value, "behaviour_Coordinate19", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Coordinate19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Coordinate19"):
                opp_val = getattr(value, "behaviour_Coordinate19", None)
                setattr(value, "behaviour_Coordinate19", self)

class behaviour_Start(Move):

    pass
class behaviour_Action(NamedElement):

    pass
class behaviour_Slot(NamedElement):

    pass
class behaviour_MoveTransition:

    def __init__(self, fluid: bool, behaviour_MoveTransition: "behaviour_Drone" = None, behaviour_MoveTransition30: "behaviour_Slot" = None, behaviour_MoveTransition33: "behaviour_Move" = None, behaviour_MoveTransition36: "behaviour_Move" = None):
        self.fluid = fluid
        self.behaviour_MoveTransition = behaviour_MoveTransition
        self.behaviour_MoveTransition30 = behaviour_MoveTransition30
        self.behaviour_MoveTransition33 = behaviour_MoveTransition33
        self.behaviour_MoveTransition36 = behaviour_MoveTransition36
        
    @property
    def fluid(self) -> bool:
        return self.__fluid

    @fluid.setter
    def fluid(self, fluid: bool):
        self.__fluid = fluid

    @property
    def behaviour_MoveTransition(self):
        return self.__behaviour_MoveTransition

    @behaviour_MoveTransition.setter
    def behaviour_MoveTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_MoveTransition__behaviour_MoveTransition", None)
        self.__behaviour_MoveTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Drone6"):
                opp_val = getattr(old_value, "behaviour_Drone6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Drone6"):
                opp_val = getattr(value, "behaviour_Drone6", None)
                if opp_val is None:
                    setattr(value, "behaviour_Drone6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_MoveTransition36(self):
        return self.__behaviour_MoveTransition36

    @behaviour_MoveTransition36.setter
    def behaviour_MoveTransition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_MoveTransition__behaviour_MoveTransition36", None)
        self.__behaviour_MoveTransition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Move37"):
                opp_val = getattr(old_value, "behaviour_Move37", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Move37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Move37"):
                opp_val = getattr(value, "behaviour_Move37", None)
                setattr(value, "behaviour_Move37", self)

    @property
    def behaviour_MoveTransition33(self):
        return self.__behaviour_MoveTransition33

    @behaviour_MoveTransition33.setter
    def behaviour_MoveTransition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_MoveTransition__behaviour_MoveTransition33", None)
        self.__behaviour_MoveTransition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Move34"):
                opp_val = getattr(old_value, "behaviour_Move34", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Move34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Move34"):
                opp_val = getattr(value, "behaviour_Move34", None)
                setattr(value, "behaviour_Move34", self)

    @property
    def behaviour_MoveTransition30(self):
        return self.__behaviour_MoveTransition30

    @behaviour_MoveTransition30.setter
    def behaviour_MoveTransition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_MoveTransition__behaviour_MoveTransition30", None)
        self.__behaviour_MoveTransition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Slot31"):
                opp_val = getattr(old_value, "behaviour_Slot31", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Slot31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Slot31"):
                opp_val = getattr(value, "behaviour_Slot31", None)
                setattr(value, "behaviour_Slot31", self)

class behaviour_Move(NamedElement):

    pass
class behaviour_Coordinate:

    def __init__(self, latitude: float, longitude: float, altitude: float, heading: float, behaviour_Coordinate: "behaviour_Drone" = None, behaviour_Coordinate19: "behaviour_Circle" = None, behaviour_Coordinate17: "behaviour_GoTo" = None):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.heading = heading
        self.behaviour_Coordinate = behaviour_Coordinate
        self.behaviour_Coordinate19 = behaviour_Coordinate19
        self.behaviour_Coordinate17 = behaviour_Coordinate17
        
    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def heading(self) -> float:
        return self.__heading

    @heading.setter
    def heading(self, heading: float):
        self.__heading = heading

    @property
    def behaviour_Coordinate19(self):
        return self.__behaviour_Coordinate19

    @behaviour_Coordinate19.setter
    def behaviour_Coordinate19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Coordinate__behaviour_Coordinate19", None)
        self.__behaviour_Coordinate19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Circle"):
                opp_val = getattr(old_value, "behaviour_Circle", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Circle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Circle"):
                opp_val = getattr(value, "behaviour_Circle", None)
                setattr(value, "behaviour_Circle", self)

    @property
    def behaviour_Coordinate17(self):
        return self.__behaviour_Coordinate17

    @behaviour_Coordinate17.setter
    def behaviour_Coordinate17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Coordinate__behaviour_Coordinate17", None)
        self.__behaviour_Coordinate17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_GoTo"):
                opp_val = getattr(old_value, "behaviour_GoTo", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_GoTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_GoTo"):
                opp_val = getattr(value, "behaviour_GoTo", None)
                setattr(value, "behaviour_GoTo", self)

    @property
    def behaviour_Coordinate(self):
        return self.__behaviour_Coordinate

    @behaviour_Coordinate.setter
    def behaviour_Coordinate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Coordinate__behaviour_Coordinate", None)
        self.__behaviour_Coordinate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Drone2"):
                opp_val = getattr(old_value, "behaviour_Drone2", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Drone2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Drone2"):
                opp_val = getattr(value, "behaviour_Drone2", None)
                setattr(value, "behaviour_Drone2", self)

class behaviour_Drone(NamedElement):

    def __init__(self, typeName: str, travelMode: str, behaviour_Drone: "behaviour_Behaviour" = None, behaviour_Drone2: "behaviour_Coordinate" = None, behaviour_Drone4: set["behaviour_Move"] = None, behaviour_Drone6: set["behaviour_MoveTransition"] = None, behaviour_Drone8: set["behaviour_Slot"] = None, behaviour_Drone23: "behaviour_UnicastNotify" = None, behaviour_Drone25: "behaviour_MulticastNotify" = None):
        self.typeName = typeName
        self.travelMode = travelMode
        self.behaviour_Drone = behaviour_Drone
        self.behaviour_Drone2 = behaviour_Drone2
        self.behaviour_Drone4 = behaviour_Drone4 if behaviour_Drone4 is not None else set()
        self.behaviour_Drone6 = behaviour_Drone6 if behaviour_Drone6 is not None else set()
        self.behaviour_Drone8 = behaviour_Drone8 if behaviour_Drone8 is not None else set()
        self.behaviour_Drone23 = behaviour_Drone23
        self.behaviour_Drone25 = behaviour_Drone25
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def travelMode(self) -> str:
        return self.__travelMode

    @travelMode.setter
    def travelMode(self, travelMode: str):
        self.__travelMode = travelMode

    @property
    def behaviour_Drone8(self):
        return self.__behaviour_Drone8

    @behaviour_Drone8.setter
    def behaviour_Drone8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone8", None)
        self.__behaviour_Drone8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Slot"):
                    opp_val = getattr(item, "behaviour_Slot", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Slot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Slot"):
                    opp_val = getattr(item, "behaviour_Slot", None)
                    
                    setattr(item, "behaviour_Slot", self)
                    

    @property
    def behaviour_Drone(self):
        return self.__behaviour_Drone

    @behaviour_Drone.setter
    def behaviour_Drone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone", None)
        self.__behaviour_Drone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Behaviour"):
                opp_val = getattr(old_value, "behaviour_Behaviour", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Behaviour"):
                opp_val = getattr(value, "behaviour_Behaviour", None)
                if opp_val is None:
                    setattr(value, "behaviour_Behaviour", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Drone2(self):
        return self.__behaviour_Drone2

    @behaviour_Drone2.setter
    def behaviour_Drone2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone2", None)
        self.__behaviour_Drone2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Coordinate"):
                opp_val = getattr(old_value, "behaviour_Coordinate", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Coordinate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Coordinate"):
                opp_val = getattr(value, "behaviour_Coordinate", None)
                setattr(value, "behaviour_Coordinate", self)

    @property
    def behaviour_Drone6(self):
        return self.__behaviour_Drone6

    @behaviour_Drone6.setter
    def behaviour_Drone6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone6", None)
        self.__behaviour_Drone6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_MoveTransition"):
                    opp_val = getattr(item, "behaviour_MoveTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_MoveTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_MoveTransition"):
                    opp_val = getattr(item, "behaviour_MoveTransition", None)
                    
                    setattr(item, "behaviour_MoveTransition", self)
                    

    @property
    def behaviour_Drone25(self):
        return self.__behaviour_Drone25

    @behaviour_Drone25.setter
    def behaviour_Drone25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone25", None)
        self.__behaviour_Drone25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MulticastNotify"):
                opp_val = getattr(old_value, "behaviour_MulticastNotify", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MulticastNotify"):
                opp_val = getattr(value, "behaviour_MulticastNotify", None)
                if opp_val is None:
                    setattr(value, "behaviour_MulticastNotify", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Drone23(self):
        return self.__behaviour_Drone23

    @behaviour_Drone23.setter
    def behaviour_Drone23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone23", None)
        self.__behaviour_Drone23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_UnicastNotify"):
                opp_val = getattr(old_value, "behaviour_UnicastNotify", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_UnicastNotify", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_UnicastNotify"):
                opp_val = getattr(value, "behaviour_UnicastNotify", None)
                setattr(value, "behaviour_UnicastNotify", self)

    @property
    def behaviour_Drone4(self):
        return self.__behaviour_Drone4

    @behaviour_Drone4.setter
    def behaviour_Drone4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Drone__behaviour_Drone4", None)
        self.__behaviour_Drone4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Move"):
                    opp_val = getattr(item, "behaviour_Move", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Move", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Move"):
                    opp_val = getattr(item, "behaviour_Move", None)
                    
                    setattr(item, "behaviour_Move", self)
                    

class behaviour_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
