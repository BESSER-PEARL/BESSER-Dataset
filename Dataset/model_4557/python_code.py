from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Vehicle:

    pass
class platoon_Vehicle(ABC):

    def __init__(self, name: str, platoon_Vehicle: "platoon_FollowingVehicle" = None):
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
            if hasattr(old_value, "platoon_FollowingVehicle12"):
                opp_val = getattr(old_value, "platoon_FollowingVehicle12", None)
                if opp_val == self:
                    setattr(old_value, "platoon_FollowingVehicle12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_FollowingVehicle12"):
                opp_val = getattr(value, "platoon_FollowingVehicle12", None)
                setattr(value, "platoon_FollowingVehicle12", self)

class routeCommand:

    pass
class platoon_TurnRight(routeCommand):

    pass
class platoon_TurnLeft(routeCommand):

    pass
class platoon_Forward(routeCommand):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class platoon_FollowingVehicle(Vehicle):

    pass
class platoon_LeaderVehicle(Vehicle):

    pass
class platoon_routeCommand(ABC):

    pass
class platoon_Constraints:

    def __init__(self, lbound: int, ubound: int, platoon_Constraints: "platoon_Root" = None):
        self.lbound = lbound
        self.ubound = ubound
        self.platoon_Constraints = platoon_Constraints
        
    @property
    def lbound(self) -> int:
        return self.__lbound

    @lbound.setter
    def lbound(self, lbound: int):
        self.__lbound = lbound

    @property
    def ubound(self) -> int:
        return self.__ubound

    @ubound.setter
    def ubound(self, ubound: int):
        self.__ubound = ubound

    @property
    def platoon_Constraints(self):
        return self.__platoon_Constraints

    @platoon_Constraints.setter
    def platoon_Constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Constraints__platoon_Constraints", None)
        self.__platoon_Constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Root4"):
                opp_val = getattr(old_value, "platoon_Root4", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Root4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Root4"):
                opp_val = getattr(value, "platoon_Root4", None)
                setattr(value, "platoon_Root4", self)

class platoon_Route:

    def __init__(self, name: str, platoon_Route: "platoon_Root" = None, platoon_Route6: set["platoon_routeCommand"] = None, platoon_Route15: "platoon_LeaderVehicle" = None):
        self.name = name
        self.platoon_Route = platoon_Route
        self.platoon_Route6 = platoon_Route6 if platoon_Route6 is not None else set()
        self.platoon_Route15 = platoon_Route15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def platoon_Route15(self):
        return self.__platoon_Route15

    @platoon_Route15.setter
    def platoon_Route15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route15", None)
        self.__platoon_Route15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_LeaderVehicle14"):
                opp_val = getattr(old_value, "platoon_LeaderVehicle14", None)
                if opp_val == self:
                    setattr(old_value, "platoon_LeaderVehicle14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_LeaderVehicle14"):
                opp_val = getattr(value, "platoon_LeaderVehicle14", None)
                setattr(value, "platoon_LeaderVehicle14", self)

    @property
    def platoon_Route6(self):
        return self.__platoon_Route6

    @platoon_Route6.setter
    def platoon_Route6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Route__platoon_Route6", None)
        self.__platoon_Route6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "platoon_routeCommand"):
                    opp_val = getattr(item, "platoon_routeCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "platoon_routeCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "platoon_routeCommand"):
                    opp_val = getattr(item, "platoon_routeCommand", None)
                    
                    setattr(item, "platoon_routeCommand", self)
                    

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
            if hasattr(old_value, "platoon_Root2"):
                opp_val = getattr(old_value, "platoon_Root2", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Root2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Root2"):
                opp_val = getattr(value, "platoon_Root2", None)
                setattr(value, "platoon_Root2", self)

class platoon_Platoon:

    pass
class platoon_Root:

    pass