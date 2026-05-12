from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Sex(Enum):
    male = "male"
    female = "female"


############################################
# Definition of Classes
############################################

class CoachBusWithEDataType_Passenger:

    def __init__(self, age: int, sex: str, CoachBusWithEDataType_Passenger: "CoachBusWithEDataType_Trip" = None):
        self.age = age
        self.sex = sex
        self.CoachBusWithEDataType_Passenger = CoachBusWithEDataType_Passenger
        
        pass
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex


    @property
    def CoachBusWithEDataType_Passenger(self):
        return self.__CoachBusWithEDataType_Passenger

    @CoachBusWithEDataType_Passenger.setter
    def CoachBusWithEDataType_Passenger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBusWithEDataType_Passenger__CoachBusWithEDataType_Passenger", None)
        self.__CoachBusWithEDataType_Passenger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoachBusWithEDataType_Trip2"):
                opp_val = getattr(old_value, "CoachBusWithEDataType_Trip2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoachBusWithEDataType_Trip2"):
                opp_val = getattr(value, "CoachBusWithEDataType_Trip2", None)
                if opp_val is None:
                    setattr(value, "CoachBusWithEDataType_Trip2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CoachBusWithEDataType_Ticket:

    def __init__(self, number: int):
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


class Trip:

    pass
class CoachBusWithEDataType_PrivateTrip(Trip):

    pass
class CoachBusWithEDataType_RegularTrip(Trip):

    pass
class CoachBusWithEDataType_Trip:

    def __init__(self, type: str, CoachBusWithEDataType_Trip: "CoachBusWithEDataType_Coach" = None, CoachBusWithEDataType_Trip2: set["CoachBusWithEDataType_Passenger"] = None):
        self.type = type
        self.CoachBusWithEDataType_Trip = CoachBusWithEDataType_Trip
        self.CoachBusWithEDataType_Trip2 = CoachBusWithEDataType_Trip2 if CoachBusWithEDataType_Trip2 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def CoachBusWithEDataType_Trip2(self):
        return self.__CoachBusWithEDataType_Trip2

    @CoachBusWithEDataType_Trip2.setter
    def CoachBusWithEDataType_Trip2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBusWithEDataType_Trip__CoachBusWithEDataType_Trip2", None)
        self.__CoachBusWithEDataType_Trip2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CoachBusWithEDataType_Passenger"):
                    opp_val = getattr(item, "CoachBusWithEDataType_Passenger", None)
                    
                    if opp_val == self:
                        setattr(item, "CoachBusWithEDataType_Passenger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CoachBusWithEDataType_Passenger"):
                    opp_val = getattr(item, "CoachBusWithEDataType_Passenger", None)
                    
                    setattr(item, "CoachBusWithEDataType_Passenger", self)
                    

    @property
    def CoachBusWithEDataType_Trip(self):
        return self.__CoachBusWithEDataType_Trip

    @CoachBusWithEDataType_Trip.setter
    def CoachBusWithEDataType_Trip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBusWithEDataType_Trip__CoachBusWithEDataType_Trip", None)
        self.__CoachBusWithEDataType_Trip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoachBusWithEDataType_Coach"):
                opp_val = getattr(old_value, "CoachBusWithEDataType_Coach", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoachBusWithEDataType_Coach"):
                opp_val = getattr(value, "CoachBusWithEDataType_Coach", None)
                if opp_val is None:
                    setattr(value, "CoachBusWithEDataType_Coach", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Ticket:

    pass
class CoachBusWithEDataType_AdultTicket(Ticket):

    pass
class CoachBusWithEDataType_ChildTicket(Ticket):

    pass
class CoachBusWithEDataType_Coach:

    def __init__(self, noOfSeats: int, CoachBusWithEDataType_Coach: set["CoachBusWithEDataType_Trip"] = None):
        self.noOfSeats = noOfSeats
        self.CoachBusWithEDataType_Coach = CoachBusWithEDataType_Coach if CoachBusWithEDataType_Coach is not None else set()
        
        pass
    @property
    def noOfSeats(self):
        return self.__noOfSeats

    @noOfSeats.setter
    def noOfSeats(self, noOfSeats: int):
        self.__noOfSeats = noOfSeats


    @property
    def CoachBusWithEDataType_Coach(self):
        return self.__CoachBusWithEDataType_Coach

    @CoachBusWithEDataType_Coach.setter
    def CoachBusWithEDataType_Coach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBusWithEDataType_Coach__CoachBusWithEDataType_Coach", None)
        self.__CoachBusWithEDataType_Coach = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CoachBusWithEDataType_Trip"):
                    opp_val = getattr(item, "CoachBusWithEDataType_Trip", None)
                    
                    if opp_val == self:
                        setattr(item, "CoachBusWithEDataType_Trip", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CoachBusWithEDataType_Trip"):
                    opp_val = getattr(item, "CoachBusWithEDataType_Trip", None)
                    
                    setattr(item, "CoachBusWithEDataType_Trip", self)
                    
