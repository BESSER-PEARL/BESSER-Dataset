from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class spotType(Enum):
    pass
class spotStatus(Enum):
    pass
class vehicleStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Parking_Record:

    def __init__(self, spot: Spot, vehicleLicensePlate: str, vehicleModel: str, vehicleColor: str, ownerName: str, ownerPhone: str, parkTime: str, releaseTime: str, hourlyRate: int, totalCost: int, parkingLot3: "ParkingLot" = None, spot25: "Spot" = None):
        self.spot = spot
        self.vehicleLicensePlate = vehicleLicensePlate
        self.vehicleModel = vehicleModel
        self.vehicleColor = vehicleColor
        self.ownerName = ownerName
        self.ownerPhone = ownerPhone
        self.parkTime = parkTime
        self.releaseTime = releaseTime
        self.hourlyRate = hourlyRate
        self.totalCost = totalCost
        self.parkingLot3 = parkingLot3
        self.spot25 = spot25
        
        pass
    @property
    def releaseTime(self):
        return self.__releaseTime
    @releaseTime.setter
    def releaseTime(self, releaseTime: str):
        self.__releaseTime = releaseTime

    @property
    def totalCost(self):
        return self.__totalCost
    @totalCost.setter
    def totalCost(self, totalCost: int):
        self.__totalCost = totalCost

    @property
    def hourlyRate(self):
        return self.__hourlyRate
    @hourlyRate.setter
    def hourlyRate(self, hourlyRate: int):
        self.__hourlyRate = hourlyRate

    @property
    def parkTime(self):
        return self.__parkTime
    @parkTime.setter
    def parkTime(self, parkTime: str):
        self.__parkTime = parkTime

    @property
    def ownerPhone(self):
        return self.__ownerPhone
    @ownerPhone.setter
    def ownerPhone(self, ownerPhone: str):
        self.__ownerPhone = ownerPhone

    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def vehicleLicensePlate(self):
        return self.__vehicleLicensePlate
    @vehicleLicensePlate.setter
    def vehicleLicensePlate(self, vehicleLicensePlate: str):
        self.__vehicleLicensePlate = vehicleLicensePlate

    @property
    def vehicleModel(self):
        return self.__vehicleModel
    @vehicleModel.setter
    def vehicleModel(self, vehicleModel: str):
        self.__vehicleModel = vehicleModel

    @property
    def spot(self):
        return self.__spot
    @spot.setter
    def spot(self, spot: Spot):
        self.__spot = spot

    @property
    def vehicleColor(self):
        return self.__vehicleColor
    @vehicleColor.setter
    def vehicleColor(self, vehicleColor: str):
        self.__vehicleColor = vehicleColor

    @property
    def spot25(self):
        return self.__spot25
    @spot25.setter
    def spot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Record__spot25", None)
        self.__spot25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parking_Record4"):
                opp_val = getattr(old_value, "parking_Record4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parking_Record4"):
                opp_val = getattr(value, "parking_Record4", None)
                if opp_val is None:
                    setattr(value, "parking_Record4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parkingLot3(self):
        return self.__parkingLot3
    @parkingLot3.setter
    def parkingLot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Parking_Record__parkingLot3", None)
        self.__parkingLot3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parking_Record2"):
                opp_val = getattr(old_value, "parking_Record2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parking_Record2"):
                opp_val = getattr(value, "parking_Record2", None)
                if opp_val is None:
                    setattr(value, "parking_Record2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Spot:

    def __init__(self, spotType: spotType, level: int, section: str, spotNumber: int, status: spotStatus, covered: bool, isDisabledSpot: bool, isValet: bool, parkingLot0: "ParkingLot" = None, parking_Record4: set["Parking_Record"] = None):
        self.spotType = spotType
        self.level = level
        self.section = section
        self.spotNumber = spotNumber
        self.status = status
        self.covered = covered
        self.isDisabledSpot = isDisabledSpot
        self.isValet = isValet
        self.parkingLot0 = parkingLot0
        self.parking_Record4 = parking_Record4 if parking_Record4 is not None else set()
        
        pass
    @property
    def spotNumber(self):
        return self.__spotNumber
    @spotNumber.setter
    def spotNumber(self, spotNumber: int):
        self.__spotNumber = spotNumber

    @property
    def isValet(self):
        return self.__isValet
    @isValet.setter
    def isValet(self, isValet: bool):
        self.__isValet = isValet

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: spotStatus):
        self.__status = status

    @property
    def isDisabledSpot(self):
        return self.__isDisabledSpot
    @isDisabledSpot.setter
    def isDisabledSpot(self, isDisabledSpot: bool):
        self.__isDisabledSpot = isDisabledSpot

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def covered(self):
        return self.__covered
    @covered.setter
    def covered(self, covered: bool):
        self.__covered = covered

    @property
    def spotType(self):
        return self.__spotType
    @spotType.setter
    def spotType(self, spotType: spotType):
        self.__spotType = spotType

    @property
    def parkingLot0(self):
        return self.__parkingLot0
    @parkingLot0.setter
    def parkingLot0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Spot__parkingLot0", None)
        self.__parkingLot0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spot1"):
                opp_val = getattr(old_value, "spot1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spot1"):
                opp_val = getattr(value, "spot1", None)
                if opp_val is None:
                    setattr(value, "spot1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parking_Record4(self):
        return self.__parking_Record4
    @parking_Record4.setter
    def parking_Record4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Spot__parking_Record4", None)
        self.__parking_Record4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spot25"):
                    opp_val = getattr(item, "spot25", None)
                    
                    if opp_val == self:
                        setattr(item, "spot25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spot25"):
                    opp_val = getattr(item, "spot25", None)
                    
                    setattr(item, "spot25", self)
                    



class ParkingLot:

    def __init__(self, maxSize: int, hourlyPrice: int, spot1: set["Spot"] = None, parking_Record2: set["Parking_Record"] = None):
        self.maxSize = maxSize
        self.hourlyPrice = hourlyPrice
        self.spot1 = spot1 if spot1 is not None else set()
        self.parking_Record2 = parking_Record2 if parking_Record2 is not None else set()
        
        pass
    @property
    def maxSize(self):
        return self.__maxSize
    @maxSize.setter
    def maxSize(self, maxSize: int):
        self.__maxSize = maxSize

    @property
    def hourlyPrice(self):
        return self.__hourlyPrice
    @hourlyPrice.setter
    def hourlyPrice(self, hourlyPrice: int):
        self.__hourlyPrice = hourlyPrice

    @property
    def spot1(self):
        return self.__spot1
    @spot1.setter
    def spot1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ParkingLot__spot1", None)
        self.__spot1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parkingLot0"):
                    opp_val = getattr(item, "parkingLot0", None)
                    
                    if opp_val == self:
                        setattr(item, "parkingLot0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parkingLot0"):
                    opp_val = getattr(item, "parkingLot0", None)
                    
                    setattr(item, "parkingLot0", self)
                    

    @property
    def parking_Record2(self):
        return self.__parking_Record2
    @parking_Record2.setter
    def parking_Record2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ParkingLot__parking_Record2", None)
        self.__parking_Record2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parkingLot3"):
                    opp_val = getattr(item, "parkingLot3", None)
                    
                    if opp_val == self:
                        setattr(item, "parkingLot3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parkingLot3"):
                    opp_val = getattr(item, "parkingLot3", None)
                    
                    setattr(item, "parkingLot3", self)
                    



class VehicleInterface_Interface:

    pass


class MotorCycle:

    pass


class Car:

    pass


class Bus:

    pass


class AbstractVehicle(ABC):

    def __init__(self, type: str, licensePlate: str, restrictions: spotRestriction):
        self.type = type
        self.licensePlate = licensePlate
        self.restrictions = restrictions
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def restrictions(self):
        return self.__restrictions
    @restrictions.setter
    def restrictions(self, restrictions: spotRestriction):
        self.__restrictions = restrictions

    @property
    def licensePlate(self):
        return self.__licensePlate
    @licensePlate.setter
    def licensePlate(self, licensePlate: str):
        self.__licensePlate = licensePlate



class spotRestriction:

    def __init__(self, spotType: spotType, size: int):
        self.spotType = spotType
        self.size = size
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def spotType(self):
        return self.__spotType
    @spotType.setter
    def spotType(self, spotType: spotType):
        self.__spotType = spotType

