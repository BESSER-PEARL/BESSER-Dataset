from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trip_model_TripModel:

    pass
class trip_model_Trip:

    def __init__(self, End: date, name: str, Start: date, trip_model_Trip: set["trip_model_Service"] = None, trip_model_Trip8: "trip_model_location" = None, trip_model_Trip11: "trip_model_location" = None, trip_model_Trip14: "trip_model_TripModel" = None):
        self.End = End
        self.name = name
        self.Start = Start
        self.trip_model_Trip = trip_model_Trip if trip_model_Trip is not None else set()
        self.trip_model_Trip8 = trip_model_Trip8
        self.trip_model_Trip11 = trip_model_Trip11
        self.trip_model_Trip14 = trip_model_Trip14
        
    @property
    def End(self) -> date:
        return self.__End

    @End.setter
    def End(self, End: date):
        self.__End = End

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Start(self) -> date:
        return self.__Start

    @Start.setter
    def Start(self, Start: date):
        self.__Start = Start

    @property
    def trip_model_Trip11(self):
        return self.__trip_model_Trip11

    @trip_model_Trip11.setter
    def trip_model_Trip11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_Trip__trip_model_Trip11", None)
        self.__trip_model_Trip11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_location12"):
                opp_val = getattr(old_value, "trip_model_location12", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_location12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_location12"):
                opp_val = getattr(value, "trip_model_location12", None)
                setattr(value, "trip_model_location12", self)

    @property
    def trip_model_Trip(self):
        return self.__trip_model_Trip

    @trip_model_Trip.setter
    def trip_model_Trip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_Trip__trip_model_Trip", None)
        self.__trip_model_Trip = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trip_model_Service"):
                    opp_val = getattr(item, "trip_model_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "trip_model_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trip_model_Service"):
                    opp_val = getattr(item, "trip_model_Service", None)
                    
                    setattr(item, "trip_model_Service", self)
                    

    @property
    def trip_model_Trip8(self):
        return self.__trip_model_Trip8

    @trip_model_Trip8.setter
    def trip_model_Trip8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_Trip__trip_model_Trip8", None)
        self.__trip_model_Trip8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_location9"):
                opp_val = getattr(old_value, "trip_model_location9", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_location9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_location9"):
                opp_val = getattr(value, "trip_model_location9", None)
                setattr(value, "trip_model_location9", self)

    @property
    def trip_model_Trip14(self):
        return self.__trip_model_Trip14

    @trip_model_Trip14.setter
    def trip_model_Trip14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_Trip__trip_model_Trip14", None)
        self.__trip_model_Trip14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_TripModel"):
                opp_val = getattr(old_value, "trip_model_TripModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_TripModel"):
                opp_val = getattr(value, "trip_model_TripModel", None)
                if opp_val is None:
                    setattr(value, "trip_model_TripModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trip_model_location:

    def __init__(self, name: str, trip_model_location: "trip_model_OtherService" = None, trip_model_location2: "trip_model_TravelService" = None, trip_model_location5: "trip_model_TravelService" = None, trip_model_location9: "trip_model_Trip" = None, trip_model_location12: "trip_model_Trip" = None, trip_model_location17: "trip_model_TripModel" = None):
        self.name = name
        self.trip_model_location = trip_model_location
        self.trip_model_location2 = trip_model_location2
        self.trip_model_location5 = trip_model_location5
        self.trip_model_location9 = trip_model_location9
        self.trip_model_location12 = trip_model_location12
        self.trip_model_location17 = trip_model_location17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trip_model_location(self):
        return self.__trip_model_location

    @trip_model_location.setter
    def trip_model_location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location", None)
        self.__trip_model_location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_OtherService"):
                opp_val = getattr(old_value, "trip_model_OtherService", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_OtherService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_OtherService"):
                opp_val = getattr(value, "trip_model_OtherService", None)
                setattr(value, "trip_model_OtherService", self)

    @property
    def trip_model_location12(self):
        return self.__trip_model_location12

    @trip_model_location12.setter
    def trip_model_location12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location12", None)
        self.__trip_model_location12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_Trip11"):
                opp_val = getattr(old_value, "trip_model_Trip11", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_Trip11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_Trip11"):
                opp_val = getattr(value, "trip_model_Trip11", None)
                setattr(value, "trip_model_Trip11", self)

    @property
    def trip_model_location9(self):
        return self.__trip_model_location9

    @trip_model_location9.setter
    def trip_model_location9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location9", None)
        self.__trip_model_location9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_Trip8"):
                opp_val = getattr(old_value, "trip_model_Trip8", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_Trip8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_Trip8"):
                opp_val = getattr(value, "trip_model_Trip8", None)
                setattr(value, "trip_model_Trip8", self)

    @property
    def trip_model_location5(self):
        return self.__trip_model_location5

    @trip_model_location5.setter
    def trip_model_location5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location5", None)
        self.__trip_model_location5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_TravelService4"):
                opp_val = getattr(old_value, "trip_model_TravelService4", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_TravelService4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_TravelService4"):
                opp_val = getattr(value, "trip_model_TravelService4", None)
                setattr(value, "trip_model_TravelService4", self)

    @property
    def trip_model_location17(self):
        return self.__trip_model_location17

    @trip_model_location17.setter
    def trip_model_location17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location17", None)
        self.__trip_model_location17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_TripModel16"):
                opp_val = getattr(old_value, "trip_model_TripModel16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_TripModel16"):
                opp_val = getattr(value, "trip_model_TripModel16", None)
                if opp_val is None:
                    setattr(value, "trip_model_TripModel16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trip_model_location2(self):
        return self.__trip_model_location2

    @trip_model_location2.setter
    def trip_model_location2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_location__trip_model_location2", None)
        self.__trip_model_location2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_TravelService"):
                opp_val = getattr(old_value, "trip_model_TravelService", None)
                if opp_val == self:
                    setattr(old_value, "trip_model_TravelService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_TravelService"):
                opp_val = getattr(value, "trip_model_TravelService", None)
                setattr(value, "trip_model_TravelService", self)

class Service:

    pass
class trip_model_TravelService(Service):

    pass
class trip_model_OtherService(Service):

    pass
class trip_model_Service:

    def __init__(self, Cost: float, Duration: int, Rating: int, name: str, Type: str, trip_model_Service: "trip_model_Trip" = None):
        self.Cost = Cost
        self.Duration = Duration
        self.Rating = Rating
        self.name = name
        self.Type = Type
        self.trip_model_Service = trip_model_Service
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Rating(self) -> int:
        return self.__Rating

    @Rating.setter
    def Rating(self, Rating: int):
        self.__Rating = Rating

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Cost(self) -> float:
        return self.__Cost

    @Cost.setter
    def Cost(self, Cost: float):
        self.__Cost = Cost

    @property
    def Duration(self) -> int:
        return self.__Duration

    @Duration.setter
    def Duration(self, Duration: int):
        self.__Duration = Duration

    @property
    def trip_model_Service(self):
        return self.__trip_model_Service

    @trip_model_Service.setter
    def trip_model_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_model_Service__trip_model_Service", None)
        self.__trip_model_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_model_Trip"):
                opp_val = getattr(old_value, "trip_model_Trip", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_model_Trip"):
                opp_val = getattr(value, "trip_model_Trip", None)
                if opp_val is None:
                    setattr(value, "trip_model_Trip", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
