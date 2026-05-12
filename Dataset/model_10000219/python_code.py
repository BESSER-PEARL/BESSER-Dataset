from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Parking_Space_Type(Enum):
    pass
class Enumeration(Enum):
    pass
class Structure_Type(Enum):
    pass
class Enumeration2(Enum):
    pass

############################################
# Definition of Classes
############################################










class Boolean_external:

    pass


class Handicapped_Space:

    pass


class Regular_Space:

    pass


class Class:

    pass


class Parking_Level:

    def __init__(self, Fl_Number: int, Composed_Of0: set["Boolean_external"] = None, has5: "Parking_Structure" = None):
        self.Fl_Number = Fl_Number
        self.Composed_Of0 = Composed_Of0 if Composed_Of0 is not None else set()
        self.has5 = has5
        
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
                    

    @property
    def has5(self):
        return self.__has5
    @has5.setter
    def has5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Level__has5", None)
        self.__has5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parking_Level4"):
                opp_val = getattr(old_value, "parking_Level4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parking_Level4"):
                opp_val = getattr(value, "parking_Level4", None)
                if opp_val is None:
                    setattr(value, "parking_Level4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Convertible:

    pass


class Electric:

    pass


class Motorbike:

    pass


class Truck:

    pass


class Car:

    pass


class Vehicle_Interface:

    pass


class Parking_Space(ABC):

    def __init__(self, Space_Number: int, Floor_Number: Parking_Level, Space_Type: Parking_Space_Type, vehicle2: "Vehicle_Interface" = None):
        self.Space_Number = Space_Number
        self.Floor_Number = Floor_Number
        self.Space_Type = Space_Type
        self.vehicle2 = vehicle2
        
        pass
    @property
    def Space_Type(self):
        return self.__Space_Type
    @Space_Type.setter
    def Space_Type(self, Space_Type: Parking_Space_Type):
        self.__Space_Type = Space_Type

    @property
    def Floor_Number(self):
        return self.__Floor_Number
    @Floor_Number.setter
    def Floor_Number(self, Floor_Number: Parking_Level):
        self.__Floor_Number = Floor_Number

    @property
    def Space_Number(self):
        return self.__Space_Number
    @Space_Number.setter
    def Space_Number(self, Space_Number: int):
        self.__Space_Number = Space_Number

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



class Parking_Structure:

    def __init__(self, City: str, Address: str, Type: Structure_Type, parking_Level4: set["Parking_Level"] = None):
        self.City = City
        self.Address = Address
        self.Type = Type
        self.parking_Level4 = parking_Level4 if parking_Level4 is not None else set()
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: Structure_Type):
        self.__Type = Type

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def parking_Level4(self):
        return self.__parking_Level4
    @parking_Level4.setter
    def parking_Level4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Structure__parking_Level4", None)
        self.__parking_Level4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has5"):
                    opp_val = getattr(item, "has5", None)
                    
                    if opp_val == self:
                        setattr(item, "has5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has5"):
                    opp_val = getattr(item, "has5", None)
                    
                    setattr(item, "has5", self)
                    

