from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EA_Model_Vehicle:

    pass
class Vehicle:

    pass
class EA_Model_TravelingVehicle(Vehicle):

    pass
class EA_Model_Travel:

    pass
class Roadway:

    pass
class EA_Model_Roadway:

    pass
class RoadTrafficAccident:

    pass
class EA_Model_RearEndCollision(RoadTrafficAccident):

    pass
class EA_Model_Person:

    pass
class Traveler:

    pass
class EA_Model_Passenger(Traveler):

    pass
class EA_Model_Victim(Traveler):

    pass
class EA_Model_Driver(Traveler):

    pass
class Person:

    pass
class EA_Model_Traveler(Person):

    pass
class EA_Model_LivingPerson(Person):

    pass
class EA_Model_DeceasedPerson(Person):

    pass
class EA_Model_RoadTrafficAccident:

    def __init__(self, fatalvictims: int, RoadTrafficAccident: "EA_Model_CrashedVehicle" = None, RoadTrafficAccident8: "EA_Model_RoadwayWithAccident" = None, accident: set["EA_Model_CrashedVehicle"] = None, accident4: set["EA_Model_Victim"] = None, roadtrafficaccident: "EA_Model_RoadwayWithAccident" = None, RoadTrafficAccident19: "EA_Model_Victim" = None):
        self.fatalvictims = fatalvictims
        self.RoadTrafficAccident = RoadTrafficAccident
        self.RoadTrafficAccident8 = RoadTrafficAccident8
        self.accident = accident if accident is not None else set()
        self.accident4 = accident4 if accident4 is not None else set()
        self.roadtrafficaccident = roadtrafficaccident
        self.RoadTrafficAccident19 = RoadTrafficAccident19
        
        pass
    @property
    def fatalvictims(self):
        return self.__fatalvictims

    @fatalvictims.setter
    def fatalvictims(self, fatalvictims: int):
        self.__fatalvictims = fatalvictims


    @property
    def RoadTrafficAccident(self):
        return self.__RoadTrafficAccident

    @RoadTrafficAccident.setter
    def RoadTrafficAccident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__RoadTrafficAccident", None)
        self.__RoadTrafficAccident = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vehicles"):
                opp_val = getattr(old_value, "vehicles", None)
                if opp_val == self:
                    setattr(old_value, "vehicles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vehicles"):
                opp_val = getattr(value, "vehicles", None)
                setattr(value, "vehicles", self)

    @property
    def RoadTrafficAccident8(self):
        return self.__RoadTrafficAccident8

    @RoadTrafficAccident8.setter
    def RoadTrafficAccident8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__RoadTrafficAccident8", None)
        self.__RoadTrafficAccident8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roadwaywithaccident"):
                opp_val = getattr(old_value, "roadwaywithaccident", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roadwaywithaccident"):
                opp_val = getattr(value, "roadwaywithaccident", None)
                if opp_val is None:
                    setattr(value, "roadwaywithaccident", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roadtrafficaccident(self):
        return self.__roadtrafficaccident

    @roadtrafficaccident.setter
    def roadtrafficaccident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__roadtrafficaccident", None)
        self.__roadtrafficaccident = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoadwayWithAccident6"):
                opp_val = getattr(old_value, "RoadwayWithAccident6", None)
                if opp_val == self:
                    setattr(old_value, "RoadwayWithAccident6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoadwayWithAccident6"):
                opp_val = getattr(value, "RoadwayWithAccident6", None)
                setattr(value, "RoadwayWithAccident6", self)

    @property
    def accident4(self):
        return self.__accident4

    @accident4.setter
    def accident4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__accident4", None)
        self.__accident4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Victim"):
                    opp_val = getattr(item, "Victim", None)
                    
                    if opp_val == self:
                        setattr(item, "Victim", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Victim"):
                    opp_val = getattr(item, "Victim", None)
                    
                    setattr(item, "Victim", self)
                    

    @property
    def RoadTrafficAccident19(self):
        return self.__RoadTrafficAccident19

    @RoadTrafficAccident19.setter
    def RoadTrafficAccident19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__RoadTrafficAccident19", None)
        self.__RoadTrafficAccident19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "victims"):
                opp_val = getattr(old_value, "victims", None)
                if opp_val == self:
                    setattr(old_value, "victims", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "victims"):
                opp_val = getattr(value, "victims", None)
                setattr(value, "victims", self)

    @property
    def accident(self):
        return self.__accident

    @accident.setter
    def accident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EA_Model_RoadTrafficAccident__accident", None)
        self.__accident = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CrashedVehicle"):
                    opp_val = getattr(item, "CrashedVehicle", None)
                    
                    if opp_val == self:
                        setattr(item, "CrashedVehicle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CrashedVehicle"):
                    opp_val = getattr(item, "CrashedVehicle", None)
                    
                    setattr(item, "CrashedVehicle", self)
                    

class TravelingVehicle:

    pass
class EA_Model_CrashedVehicle(TravelingVehicle):

    pass
class EA_Model_RoadwayWithAccident(Roadway):

    pass