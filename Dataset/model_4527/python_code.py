from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Turn:

    pass
class platoon_Right(Turn):

    pass
class platoon_Left(Turn):

    pass
class Action:

    pass
class platoon_Forward(Action):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class platoon_Turn(Action):

    pass
class Vehicle:

    pass
class platoon_Action:

    pass
class platoon_Vehicle:

    def __init__(self, name: str, platoon_Vehicle: "platoon_FV" = None):
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
            if hasattr(old_value, "platoon_FV10"):
                opp_val = getattr(old_value, "platoon_FV10", None)
                if opp_val == self:
                    setattr(old_value, "platoon_FV10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_FV10"):
                opp_val = getattr(value, "platoon_FV10", None)
                setattr(value, "platoon_FV10", self)

class platoon_FV(Vehicle):

    pass
class platoon_LV(Vehicle):

    pass
class platoon_Constraints:

    def __init__(self, minHeadway: int, maxHeadway: int, platoon_Constraints: "platoon_Model" = None):
        self.minHeadway = minHeadway
        self.maxHeadway = maxHeadway
        self.platoon_Constraints = platoon_Constraints
        
    @property
    def minHeadway(self) -> int:
        return self.__minHeadway

    @minHeadway.setter
    def minHeadway(self, minHeadway: int):
        self.__minHeadway = minHeadway

    @property
    def maxHeadway(self) -> int:
        return self.__maxHeadway

    @maxHeadway.setter
    def maxHeadway(self, maxHeadway: int):
        self.__maxHeadway = maxHeadway

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
            if hasattr(old_value, "platoon_Model4"):
                opp_val = getattr(old_value, "platoon_Model4", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Model4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Model4"):
                opp_val = getattr(value, "platoon_Model4", None)
                setattr(value, "platoon_Model4", self)

class platoon_Route:

    def __init__(self, name: str, platoon_Route: "platoon_Model" = None, platoon_Route13: "platoon_LV" = None, platoon_Route15: set["platoon_Action"] = None):
        self.name = name
        self.platoon_Route = platoon_Route
        self.platoon_Route13 = platoon_Route13
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
            if hasattr(old_value, "platoon_Model2"):
                opp_val = getattr(old_value, "platoon_Model2", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Model2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Model2"):
                opp_val = getattr(value, "platoon_Model2", None)
                setattr(value, "platoon_Model2", self)

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
            if hasattr(old_value, "platoon_LV12"):
                opp_val = getattr(old_value, "platoon_LV12", None)
                if opp_val == self:
                    setattr(old_value, "platoon_LV12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_LV12"):
                opp_val = getattr(value, "platoon_LV12", None)
                setattr(value, "platoon_LV12", self)

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
                if hasattr(item, "platoon_Action"):
                    opp_val = getattr(item, "platoon_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "platoon_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "platoon_Action"):
                    opp_val = getattr(item, "platoon_Action", None)
                    
                    setattr(item, "platoon_Action", self)
                    

class platoon_Platoon:

    pass
class platoon_Model:

    pass