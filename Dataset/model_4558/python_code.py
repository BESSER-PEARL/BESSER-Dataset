from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class platoon_Constraints:

    pass
class platoon_World:

    pass
class platoon_Constraint:

    pass
class Constraint:

    pass
class platoon_HeadwayConstraint(Constraint):

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

class Command:

    pass
class platoon_TurnCommand(Command):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class platoon_ForwardCommand(Command):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class platoon_Command:

    pass
class platoon_Route:

    def __init__(self, name: str, platoon_Route: set["platoon_Command"] = None, platoon_Route8: "platoon_LeadingVehicle" = None, platoon_Route13: "platoon_World" = None):
        self.name = name
        self.platoon_Route = platoon_Route if platoon_Route is not None else set()
        self.platoon_Route8 = platoon_Route8
        self.platoon_Route13 = platoon_Route13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def platoon_Route13(self):
        return self.__platoon_Route13

    @platoon_Route13.setter
    def platoon_Route13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route13", None)
        self.__platoon_Route13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_World12"):
                opp_val = getattr(old_value, "platoon_World12", None)
                if opp_val == self:
                    setattr(old_value, "platoon_World12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_World12"):
                opp_val = getattr(value, "platoon_World12", None)
                setattr(value, "platoon_World12", self)

    @property
    def platoon_Route(self):
        return self.__platoon_Route

    @platoon_Route.setter
    def platoon_Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route", None)
        self.__platoon_Route = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "platoon_Command"):
                    opp_val = getattr(item, "platoon_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "platoon_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "platoon_Command"):
                    opp_val = getattr(item, "platoon_Command", None)
                    
                    setattr(item, "platoon_Command", self)
                    

    @property
    def platoon_Route8(self):
        return self.__platoon_Route8

    @platoon_Route8.setter
    def platoon_Route8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route8", None)
        self.__platoon_Route8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_LeadingVehicle7"):
                opp_val = getattr(old_value, "platoon_LeadingVehicle7", None)
                if opp_val == self:
                    setattr(old_value, "platoon_LeadingVehicle7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_LeadingVehicle7"):
                opp_val = getattr(value, "platoon_LeadingVehicle7", None)
                setattr(value, "platoon_LeadingVehicle7", self)

class platoon_Platoon:

    pass
class Vehicle:

    pass
class platoon_LeadingVehicle(Vehicle):

    pass
class platoon_FollowVehicle(Vehicle):

    pass
class platoon_Vehicle(ABC):

    def __init__(self, name: str, platoon_Vehicle: "platoon_FollowVehicle" = None):
        self.name = name
        self.platoon_Vehicle = platoon_Vehicle
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def platoon_Vehicle(self):
        return self.__platoon_Vehicle

    @platoon_Vehicle.setter
    def platoon_Vehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle", None)
        self.__platoon_Vehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_FollowVehicle5"):
                opp_val = getattr(old_value, "platoon_FollowVehicle5", None)
                if opp_val == self:
                    setattr(old_value, "platoon_FollowVehicle5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_FollowVehicle5"):
                opp_val = getattr(value, "platoon_FollowVehicle5", None)
                setattr(value, "platoon_FollowVehicle5", self)
