from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class trip_Vehicle(NamedElement):

    def __init__(self, nrOfSeats: int, trip_Vehicle: "trip_Trip" = None):
        self.nrOfSeats = nrOfSeats
        self.trip_Vehicle = trip_Vehicle
        
    @property
    def nrOfSeats(self) -> int:
        return self.__nrOfSeats

    @nrOfSeats.setter
    def nrOfSeats(self, nrOfSeats: int):
        self.__nrOfSeats = nrOfSeats

    @property
    def trip_Vehicle(self):
        return self.__trip_Vehicle

    @trip_Vehicle.setter
    def trip_Vehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_Vehicle__trip_Vehicle", None)
        self.__trip_Vehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_Trip"):
                opp_val = getattr(old_value, "trip_Trip", None)
                if opp_val == self:
                    setattr(old_value, "trip_Trip", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_Trip"):
                opp_val = getattr(value, "trip_Trip", None)
                setattr(value, "trip_Trip", self)

class trip_Trip(NamedElement):

    pass
class trip_NamedElement(ABC):

    def __init__(self, name: str, trip_NamedElement: "trip_TripModel" = None):
        self.name = name
        self.trip_NamedElement = trip_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trip_NamedElement(self):
        return self.__trip_NamedElement

    @trip_NamedElement.setter
    def trip_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trip_NamedElement__trip_NamedElement", None)
        self.__trip_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trip_TripModel"):
                opp_val = getattr(old_value, "trip_TripModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trip_TripModel"):
                opp_val = getattr(value, "trip_TripModel", None)
                if opp_val is None:
                    setattr(value, "trip_TripModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trip_TripModel(NamedElement):

    pass
class Vehicle:

    pass
class trip_Van(Vehicle):

    pass
class trip_Car(Vehicle):

    pass
class trip_Person(NamedElement):

    pass