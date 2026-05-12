from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass
class VehicleType(Enum):
    pass
class Parking_Space_Type(Enum):
    pass
class Enumeration2(Enum):
    pass

############################################
# Definition of Classes
############################################










class Boolean_external:

    pass


class Regular_Space:

    pass


class Class:

    pass


class Parking_Level:

    def __init__(self, Fl_Number: int, Composed_Of0: set["Boolean_external"] = None):
        self.Fl_Number = Fl_Number
        self.Composed_Of0 = Composed_Of0 if Composed_Of0 is not None else set()
        
        pass
    @property
    def Fl_Number(self):
        return self.__Fl_Number
    @Fl_Number.setter
    def Fl_Number(self, Fl_Number: int):
        self.__Fl_Number = Fl_Number

    @property
    def Composed_Of0(self):
        return self.__Composed_Of0
    @Composed_Of0.setter
    def Composed_Of0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Level__Composed_Of0", None)
        self.__Composed_Of0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor1"):
                    opp_val = getattr(item, "floor1", None)
                    
                    if opp_val == self:
                        setattr(item, "floor1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor1"):
                    opp_val = getattr(item, "floor1", None)
                    
                    setattr(item, "floor1", self)
                    



class Motorbike:

    pass


class Truck:

    pass


class Car:

    pass


class Vehicle_Interface:

    pass


class Parking_Space(ABC):

    def __init__(self, Space_Number: int, Floor_Number: Parking_Level, Space_Type: Parking_Space_Type, Occupied: bool, vehicle2: "Vehicle_Interface" = None):
        self.Space_Number = Space_Number
        self.Floor_Number = Floor_Number
        self.Space_Type = Space_Type
        self.Occupied = Occupied
        self.vehicle2 = vehicle2
        
        pass
    @property
    def Floor_Number(self):
        return self.__Floor_Number
    @Floor_Number.setter
    def Floor_Number(self, Floor_Number: Parking_Level):
        self.__Floor_Number = Floor_Number

    @property
    def Occupied(self):
        return self.__Occupied
    @Occupied.setter
    def Occupied(self, Occupied: bool):
        self.__Occupied = Occupied

    @property
    def Space_Number(self):
        return self.__Space_Number
    @Space_Number.setter
    def Space_Number(self, Space_Number: int):
        self.__Space_Number = Space_Number

    @property
    def Space_Type(self):
        return self.__Space_Type
    @Space_Type.setter
    def Space_Type(self, Space_Type: Parking_Space_Type):
        self.__Space_Type = Space_Type

    @property
    def vehicle2(self):
        return self.__vehicle2
    @vehicle2.setter
    def vehicle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Space__vehicle2", None)
        self.__vehicle2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has3"):
                opp_val = getattr(old_value, "has3", None)
                if opp_val == self:
                    setattr(old_value, "has3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has3"):
                opp_val = getattr(value, "has3", None)
                setattr(value, "has3", self)

