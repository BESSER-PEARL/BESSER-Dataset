from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Turn:

    pass
class platoon_TurnLeft(Turn):

    pass
class Step:

    pass
class platoon_Turn(Step):

    pass
class platoon_Forward(Step):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class platoon_Step(ABC):

    pass
class Vehicle:

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
            if hasattr(old_value, "platoon_FollowVehicle13"):
                opp_val = getattr(old_value, "platoon_FollowVehicle13", None)
                if opp_val == self:
                    setattr(old_value, "platoon_FollowVehicle13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_FollowVehicle13"):
                opp_val = getattr(value, "platoon_FollowVehicle13", None)
                setattr(value, "platoon_FollowVehicle13", self)

class platoon_FollowVehicle(Vehicle):

    pass
class Constraint:

    pass
class platoon_headway(Constraint):

    def __init__(self, lowbound: int, upbound: int):
        self.lowbound = lowbound
        self.upbound = upbound
        
    @property
    def upbound(self) -> int:
        return self.__upbound

    @upbound.setter
    def upbound(self, upbound: int):
        self.__upbound = upbound

    @property
    def lowbound(self) -> int:
        return self.__lowbound

    @lowbound.setter
    def lowbound(self, lowbound: int):
        self.__lowbound = lowbound

class platoon_Constraint(ABC):

    pass
class platoon_TurnRight(Turn):

    pass
class platoon_LeadVehicle(Vehicle):

    pass
class platoon_Constraints:

    pass
class platoon_Route:

    def __init__(self, name: str, platoon_Route: "platoon_World" = None, platoon_Route11: "platoon_LeadVehicle" = None, platoon_Route15: set["platoon_Step"] = None):
        self.name = name
        self.platoon_Route = platoon_Route
        self.platoon_Route11 = platoon_Route11
        self.platoon_Route15 = platoon_Route15 if platoon_Route15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def platoon_Route(self):
        return self.__platoon_Route

    @platoon_Route.setter
    def platoon_Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route", None)
        self.__platoon_Route = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_World2"):
                opp_val = getattr(old_value, "platoon_World2", None)
                if opp_val == self:
                    setattr(old_value, "platoon_World2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_World2"):
                opp_val = getattr(value, "platoon_World2", None)
                setattr(value, "platoon_World2", self)

    @property
    def platoon_Route15(self):
        return self.__platoon_Route15

    @platoon_Route15.setter
    def platoon_Route15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route15", None)
        self.__platoon_Route15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "platoon_Step"):
                    opp_val = getattr(item, "platoon_Step", None)
                    
                    if opp_val == self:
                        setattr(item, "platoon_Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "platoon_Step"):
                    opp_val = getattr(item, "platoon_Step", None)
                    
                    setattr(item, "platoon_Step", self)
                    

    @property
    def platoon_Route11(self):
        return self.__platoon_Route11

    @platoon_Route11.setter
    def platoon_Route11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route11", None)
        self.__platoon_Route11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_LeadVehicle10"):
                opp_val = getattr(old_value, "platoon_LeadVehicle10", None)
                if opp_val == self:
                    setattr(old_value, "platoon_LeadVehicle10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_LeadVehicle10"):
                opp_val = getattr(value, "platoon_LeadVehicle10", None)
                setattr(value, "platoon_LeadVehicle10", self)

class platoon_Platoon:

    pass
class platoon_World:

    pass