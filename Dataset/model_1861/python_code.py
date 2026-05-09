from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomType(Enum):
    Handicapable = "Handicapable"
    Double = "Double"
    Single = "Single"
    Suite = "Suite"
class EType(Enum):
    Receptionist = "Receptionist"
    Cleaner = "Cleaner"
    Manager = "Manager"


############################################
# Definition of Classes
############################################

class HotelManagementClassDiagram_Interaction4:

    pass
class HotelManagementClassDiagram_Interaction3:

    pass
class HotelManagementClassDiagram_Interaction5:

    pass
class Room:

    pass
class HotelManagementClassDiagram_BookedRoom(Room):

    def __init__(self, HotelManagementClassDiagram_BookedRoom: set["HotelManagementClassDiagram_Addon"] = None):
        self.HotelManagementClassDiagram_BookedRoom = HotelManagementClassDiagram_BookedRoom if HotelManagementClassDiagram_BookedRoom is not None else set()
        
        pass
    @property
    def HotelManagementClassDiagram_BookedRoom(self):
        return self.__HotelManagementClassDiagram_BookedRoom

    @HotelManagementClassDiagram_BookedRoom.setter
    def HotelManagementClassDiagram_BookedRoom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_BookedRoom__HotelManagementClassDiagram_BookedRoom", None)
        self.__HotelManagementClassDiagram_BookedRoom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Addon23"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Addon23", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Addon23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Addon23"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Addon23", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Addon23", self)
                    

    def addAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement addAddon method
        pass

    def removeAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement removeAddon method
        pass

class HotelManagementClassDiagram_Hotel:

    def __init__(self, name: str, address: str, rank: float):
        self.name = name
        self.address = address
        self.rank = rank
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank: float):
        self.__rank = rank


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    def getBookingController(self):
        # TODO: Implement getBookingController method
        pass

    def getMaintenanceController(self):
        # TODO: Implement getMaintenanceController method
        pass

    def authenticate(self, HotelManagementClassDiagram_password, HotelManagementClassDiagram_login):
        # TODO: Implement authenticate method
        pass

    def getManagementController(self):
        # TODO: Implement getManagementController method
        pass

class HotelManagementClassDiagram_Interaction2:

    pass
class HotelManagementClassDiagram_Interaction1:

    pass
class HotelManagementClassDiagram_ManagementController:

    def __init__(self):
        
        pass
    def registerDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement registerDiscount method
        pass

    def updateRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement updateRoom method
        pass

    def updateAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement updateAddon method
        pass

    def registerRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement registerRoom method
        pass

    def registerAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement registerAddon method
        pass

    def setDateSpecificPrices(self, HotelManagementClassDiagram_priceChange, HotelManagementClassDiagram_costable, HotelManagementClassDiagram_startDate, HotelManagementClassDiagram_endDate):
        # TODO: Implement setDateSpecificPrices method
        pass

    def modifyBooking(self, HotelManagementClassDiagram_booking):
        # TODO: Implement modifyBooking method
        pass

class HotelManagementClassDiagram_MaintenanceController:

    def __init__(self, HotelManagementClassDiagram_MaintenanceController: set["HotelManagementClassDiagram_Room"] = None, HotelManagementClassDiagram_MaintenanceController29: "HotelManagementClassDiagram_Interaction3" = None):
        self.HotelManagementClassDiagram_MaintenanceController = HotelManagementClassDiagram_MaintenanceController if HotelManagementClassDiagram_MaintenanceController is not None else set()
        self.HotelManagementClassDiagram_MaintenanceController29 = HotelManagementClassDiagram_MaintenanceController29
        
        pass
    @property
    def HotelManagementClassDiagram_MaintenanceController(self):
        return self.__HotelManagementClassDiagram_MaintenanceController

    @HotelManagementClassDiagram_MaintenanceController.setter
    def HotelManagementClassDiagram_MaintenanceController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_MaintenanceController__HotelManagementClassDiagram_MaintenanceController", None)
        self.__HotelManagementClassDiagram_MaintenanceController = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Room21"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Room21", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Room21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Room21"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Room21", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Room21", self)
                    

    @property
    def HotelManagementClassDiagram_MaintenanceController29(self):
        return self.__HotelManagementClassDiagram_MaintenanceController29

    @HotelManagementClassDiagram_MaintenanceController29.setter
    def HotelManagementClassDiagram_MaintenanceController29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_MaintenanceController__HotelManagementClassDiagram_MaintenanceController29", None)
        self.__HotelManagementClassDiagram_MaintenanceController29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Interaction3"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Interaction3", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Interaction3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Interaction3"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Interaction3", None)
                setattr(value, "HotelManagementClassDiagram_Interaction3", self)

    def setStatus(self, HotelManagementClassDiagram_status, HotelManagementClassDiagram_room):
        # TODO: Implement setStatus method
        pass

    def addToStack(self, HotelManagementClassDiagram_room):
        # TODO: Implement addToStack method
        pass

    def removeFromStack(self, HotelManagementClassDiagram_room):
        # TODO: Implement removeFromStack method
        pass

    def getNextRoomToClean(self, HotelManagementClassDiagram_room):
        # TODO: Implement getNextRoomToClean method
        pass

    def notifyWorker(self, HotelManagementClassDiagram_worker):
        # TODO: Implement notifyWorker method
        pass

class HotelManagementClassDiagram_BookingController:

    def __init__(self):
        
        pass
    def updateBooking(self, HotelManagementClassDiagram_booking) :
        # TODO: Implement updateBooking method
        pass

    def checkOut(self, HotelManagementClassDiagram_booking):
        # TODO: Implement checkOut method
        pass

    def sendConfirmation(self, HotelManagementClassDiagram_booking) :
        # TODO: Implement sendConfirmation method
        pass

    def checkIn(self, HotelManagementClassDiagram_booking):
        # TODO: Implement checkIn method
        pass

    def getBooking(self, HotelManagementClassDiagram_bookingId) :
        # TODO: Implement getBooking method
        pass

    def createKeyCard(self, HotelManagementClassDiagram_room):
        # TODO: Implement createKeyCard method
        pass

    def saveCustomer(self, HotelManagementClassDiagram_customer):
        # TODO: Implement saveCustomer method
        pass

    def searchAvailableRoomTypes(self, HotelManagementClassDiagram_toDate, HotelManagementClassDiagram_nbrOfChildren, HotelManagementClassDiagram_fromDate, HotelManagementClassDiagram_nbrOfAdults) :
        # TODO: Implement searchAvailableRoomTypes method
        pass

    def findCustomer(self, HotelManagementClassDiagram_ssNumber):
        # TODO: Implement findCustomer method
        pass

    def createBooking(self, HotelManagementClassDiagram_roomTypes) :
        # TODO: Implement createBooking method
        pass

    def assignRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement assignRoom method
        pass

    def confirm(self, HotelManagementClassDiagram_booking) :
        # TODO: Implement confirm method
        pass

class HotelManagementClassDiagram_Costable(ABC):

    def __init__(self, price: float, HotelManagementClassDiagram_Costable: "HotelManagementClassDiagram_Bill" = None, HotelManagementClassDiagram_Costable18: set["HotelManagementClassDiagram_Discount"] = None):
        self.price = price
        self.HotelManagementClassDiagram_Costable = HotelManagementClassDiagram_Costable
        self.HotelManagementClassDiagram_Costable18 = HotelManagementClassDiagram_Costable18 if HotelManagementClassDiagram_Costable18 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def HotelManagementClassDiagram_Costable(self):
        return self.__HotelManagementClassDiagram_Costable

    @HotelManagementClassDiagram_Costable.setter
    def HotelManagementClassDiagram_Costable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Costable__HotelManagementClassDiagram_Costable", None)
        self.__HotelManagementClassDiagram_Costable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Bill"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Bill", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Bill"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Bill", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Bill", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Costable18(self):
        return self.__HotelManagementClassDiagram_Costable18

    @HotelManagementClassDiagram_Costable18.setter
    def HotelManagementClassDiagram_Costable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Costable__HotelManagementClassDiagram_Costable18", None)
        self.__HotelManagementClassDiagram_Costable18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Discount19"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount19", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Discount19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Discount19"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount19", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Discount19", self)
                    

    def addDiscount(self):
        # TODO: Implement addDiscount method
        pass

    def removeDiscount(self):
        # TODO: Implement removeDiscount method
        pass

class HotelManagementClassDiagram_Bill:

    def __init__(self, totalPrice: float, valueAddedTax: float, final: bool, paid: bool, HotelManagementClassDiagram_Bill: set["HotelManagementClassDiagram_Costable"] = None, HotelManagementClassDiagram_Bill15: "HotelManagementClassDiagram_Customer" = None):
        self.totalPrice = totalPrice
        self.valueAddedTax = valueAddedTax
        self.final = final
        self.paid = paid
        self.HotelManagementClassDiagram_Bill = HotelManagementClassDiagram_Bill if HotelManagementClassDiagram_Bill is not None else set()
        self.HotelManagementClassDiagram_Bill15 = HotelManagementClassDiagram_Bill15
        
        pass
    @property
    def paid(self):
        return self.__paid

    @paid.setter
    def paid(self, paid: bool):
        self.__paid = paid


    @property
    def valueAddedTax(self):
        return self.__valueAddedTax

    @valueAddedTax.setter
    def valueAddedTax(self, valueAddedTax: float):
        self.__valueAddedTax = valueAddedTax


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def totalPrice(self):
        return self.__totalPrice

    @totalPrice.setter
    def totalPrice(self, totalPrice: float):
        self.__totalPrice = totalPrice


    @property
    def HotelManagementClassDiagram_Bill15(self):
        return self.__HotelManagementClassDiagram_Bill15

    @HotelManagementClassDiagram_Bill15.setter
    def HotelManagementClassDiagram_Bill15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Bill__HotelManagementClassDiagram_Bill15", None)
        self.__HotelManagementClassDiagram_Bill15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Customer16"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Customer16", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Customer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Customer16"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Customer16", None)
                setattr(value, "HotelManagementClassDiagram_Customer16", self)

    @property
    def HotelManagementClassDiagram_Bill(self):
        return self.__HotelManagementClassDiagram_Bill

    @HotelManagementClassDiagram_Bill.setter
    def HotelManagementClassDiagram_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Bill__HotelManagementClassDiagram_Bill", None)
        self.__HotelManagementClassDiagram_Bill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Costable"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Costable", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Costable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Costable"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Costable", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Costable", self)
                    

    def addCostable(self, HotelManagementClassDiagram_costable):
        # TODO: Implement addCostable method
        pass

class HotelManagementClassDiagram_Room:

    def __init__(self, roomNumber: int, size: float, internalComment: str, booked: bool, maxNbrPeople: int, underCleaning: bool, underRepair: bool, types: str, roomName: str, HotelManagementClassDiagram_Room: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Room21: "HotelManagementClassDiagram_MaintenanceController" = None):
        self.roomNumber = roomNumber
        self.size = size
        self.internalComment = internalComment
        self.booked = booked
        self.maxNbrPeople = maxNbrPeople
        self.underCleaning = underCleaning
        self.underRepair = underRepair
        self.types = types
        self.roomName = roomName
        self.HotelManagementClassDiagram_Room = HotelManagementClassDiagram_Room
        self.HotelManagementClassDiagram_Room21 = HotelManagementClassDiagram_Room21
        
        pass
    @property
    def underRepair(self):
        return self.__underRepair

    @underRepair.setter
    def underRepair(self, underRepair: bool):
        self.__underRepair = underRepair


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size


    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber


    @property
    def booked(self):
        return self.__booked

    @booked.setter
    def booked(self, booked: bool):
        self.__booked = booked


    @property
    def roomName(self):
        return self.__roomName

    @roomName.setter
    def roomName(self, roomName: str):
        self.__roomName = roomName


    @property
    def internalComment(self):
        return self.__internalComment

    @internalComment.setter
    def internalComment(self, internalComment: str):
        self.__internalComment = internalComment


    @property
    def underCleaning(self):
        return self.__underCleaning

    @underCleaning.setter
    def underCleaning(self, underCleaning: bool):
        self.__underCleaning = underCleaning


    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types


    @property
    def maxNbrPeople(self):
        return self.__maxNbrPeople

    @maxNbrPeople.setter
    def maxNbrPeople(self, maxNbrPeople: int):
        self.__maxNbrPeople = maxNbrPeople


    @property
    def HotelManagementClassDiagram_Room(self):
        return self.__HotelManagementClassDiagram_Room

    @HotelManagementClassDiagram_Room.setter
    def HotelManagementClassDiagram_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Room__HotelManagementClassDiagram_Room", None)
        self.__HotelManagementClassDiagram_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking7"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking7"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking7", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Booking7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Room21(self):
        return self.__HotelManagementClassDiagram_Room21

    @HotelManagementClassDiagram_Room21.setter
    def HotelManagementClassDiagram_Room21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Room__HotelManagementClassDiagram_Room21", None)
        self.__HotelManagementClassDiagram_Room21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_MaintenanceController"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_MaintenanceController", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_MaintenanceController"):
                opp_val = getattr(value, "HotelManagementClassDiagram_MaintenanceController", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_MaintenanceController", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HotelManagementClassDiagram_Addon:

    def __init__(self, name: str, description: str, HotelManagementClassDiagram_Addon: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Addon23: "HotelManagementClassDiagram_BookedRoom" = None):
        self.name = name
        self.description = description
        self.HotelManagementClassDiagram_Addon = HotelManagementClassDiagram_Addon
        self.HotelManagementClassDiagram_Addon23 = HotelManagementClassDiagram_Addon23
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def HotelManagementClassDiagram_Addon(self):
        return self.__HotelManagementClassDiagram_Addon

    @HotelManagementClassDiagram_Addon.setter
    def HotelManagementClassDiagram_Addon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Addon__HotelManagementClassDiagram_Addon", None)
        self.__HotelManagementClassDiagram_Addon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking5"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking5"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking5", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Booking5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Addon23(self):
        return self.__HotelManagementClassDiagram_Addon23

    @HotelManagementClassDiagram_Addon23.setter
    def HotelManagementClassDiagram_Addon23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Addon__HotelManagementClassDiagram_Addon23", None)
        self.__HotelManagementClassDiagram_Addon23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_BookedRoom"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_BookedRoom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_BookedRoom"):
                opp_val = getattr(value, "HotelManagementClassDiagram_BookedRoom", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_BookedRoom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HotelManagementClassDiagram_Creditcard:

    def __init__(self, number: str, cvc: int, owner: str, expirationMonth: int, expirationDay: int, HotelManagementClassDiagram_Creditcard: "HotelManagementClassDiagram_Booking" = None):
        self.number = number
        self.cvc = cvc
        self.owner = owner
        self.expirationMonth = expirationMonth
        self.expirationDay = expirationDay
        self.HotelManagementClassDiagram_Creditcard = HotelManagementClassDiagram_Creditcard
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner


    @property
    def cvc(self):
        return self.__cvc

    @cvc.setter
    def cvc(self, cvc: int):
        self.__cvc = cvc


    @property
    def expirationMonth(self):
        return self.__expirationMonth

    @expirationMonth.setter
    def expirationMonth(self, expirationMonth: int):
        self.__expirationMonth = expirationMonth


    @property
    def expirationDay(self):
        return self.__expirationDay

    @expirationDay.setter
    def expirationDay(self, expirationDay: int):
        self.__expirationDay = expirationDay


    @property
    def HotelManagementClassDiagram_Creditcard(self):
        return self.__HotelManagementClassDiagram_Creditcard

    @HotelManagementClassDiagram_Creditcard.setter
    def HotelManagementClassDiagram_Creditcard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Creditcard__HotelManagementClassDiagram_Creditcard", None)
        self.__HotelManagementClassDiagram_Creditcard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking", None)
                setattr(value, "HotelManagementClassDiagram_Booking", self)

class HotelManagementClassDiagram_Discount:

    def __init__(self, isPercentage: str, amount: float, HotelManagementClassDiagram_Discount19: "HotelManagementClassDiagram_Costable" = None, HotelManagementClassDiagram_Discount: "HotelManagementClassDiagram_Booking" = None):
        self.isPercentage = isPercentage
        self.amount = amount
        self.HotelManagementClassDiagram_Discount19 = HotelManagementClassDiagram_Discount19
        self.HotelManagementClassDiagram_Discount = HotelManagementClassDiagram_Discount
        
        pass
    @property
    def isPercentage(self):
        return self.__isPercentage

    @isPercentage.setter
    def isPercentage(self, isPercentage: str):
        self.__isPercentage = isPercentage


    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount


    @property
    def HotelManagementClassDiagram_Discount(self):
        return self.__HotelManagementClassDiagram_Discount

    @HotelManagementClassDiagram_Discount.setter
    def HotelManagementClassDiagram_Discount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Discount__HotelManagementClassDiagram_Discount", None)
        self.__HotelManagementClassDiagram_Discount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking12"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking12"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking12", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Booking12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Discount19(self):
        return self.__HotelManagementClassDiagram_Discount19

    @HotelManagementClassDiagram_Discount19.setter
    def HotelManagementClassDiagram_Discount19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Discount__HotelManagementClassDiagram_Discount19", None)
        self.__HotelManagementClassDiagram_Discount19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Costable18"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Costable18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Costable18"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Costable18", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Costable18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HotelManagementClassDiagram_Booking:

    def __init__(self, startDate: date, endDate: date, created: date, internalComments: str, externalComments: str, checkedIn: bool, checkedOut: bool, bookingId: int, HotelManagementClassDiagram_Booking7: set["HotelManagementClassDiagram_Room"] = None, HotelManagementClassDiagram_Booking3: "HotelManagementClassDiagram_Customer" = None, HotelManagementClassDiagram_Booking5: set["HotelManagementClassDiagram_Addon"] = None, HotelManagementClassDiagram_Booking33: "HotelManagementClassDiagram_Interaction5" = None, HotelManagementClassDiagram_Booking9: "HotelManagementClassDiagram_Customer" = None, HotelManagementClassDiagram_Booking12: set["HotelManagementClassDiagram_Discount"] = None, HotelManagementClassDiagram_Booking: "HotelManagementClassDiagram_Creditcard" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.created = created
        self.internalComments = internalComments
        self.externalComments = externalComments
        self.checkedIn = checkedIn
        self.checkedOut = checkedOut
        self.bookingId = bookingId
        self.HotelManagementClassDiagram_Booking7 = HotelManagementClassDiagram_Booking7 if HotelManagementClassDiagram_Booking7 is not None else set()
        self.HotelManagementClassDiagram_Booking3 = HotelManagementClassDiagram_Booking3
        self.HotelManagementClassDiagram_Booking5 = HotelManagementClassDiagram_Booking5 if HotelManagementClassDiagram_Booking5 is not None else set()
        self.HotelManagementClassDiagram_Booking33 = HotelManagementClassDiagram_Booking33
        self.HotelManagementClassDiagram_Booking9 = HotelManagementClassDiagram_Booking9
        self.HotelManagementClassDiagram_Booking12 = HotelManagementClassDiagram_Booking12 if HotelManagementClassDiagram_Booking12 is not None else set()
        self.HotelManagementClassDiagram_Booking = HotelManagementClassDiagram_Booking
        
        pass
    @property
    def checkedIn(self):
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate


    @property
    def bookingId(self):
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId


    @property
    def externalComments(self):
        return self.__externalComments

    @externalComments.setter
    def externalComments(self, externalComments: str):
        self.__externalComments = externalComments


    @property
    def internalComments(self):
        return self.__internalComments

    @internalComments.setter
    def internalComments(self, internalComments: str):
        self.__internalComments = internalComments


    @property
    def checkedOut(self):
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: bool):
        self.__checkedOut = checkedOut


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created


    @property
    def HotelManagementClassDiagram_Booking5(self):
        return self.__HotelManagementClassDiagram_Booking5

    @HotelManagementClassDiagram_Booking5.setter
    def HotelManagementClassDiagram_Booking5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking5", None)
        self.__HotelManagementClassDiagram_Booking5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Addon"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Addon", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Addon", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Addon"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Addon", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Addon", self)
                    

    @property
    def HotelManagementClassDiagram_Booking7(self):
        return self.__HotelManagementClassDiagram_Booking7

    @HotelManagementClassDiagram_Booking7.setter
    def HotelManagementClassDiagram_Booking7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking7", None)
        self.__HotelManagementClassDiagram_Booking7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Room"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Room"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Room", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Room", self)
                    

    @property
    def HotelManagementClassDiagram_Booking33(self):
        return self.__HotelManagementClassDiagram_Booking33

    @HotelManagementClassDiagram_Booking33.setter
    def HotelManagementClassDiagram_Booking33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking33", None)
        self.__HotelManagementClassDiagram_Booking33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Interaction5"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Interaction5", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Interaction5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Interaction5"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Interaction5", None)
                setattr(value, "HotelManagementClassDiagram_Interaction5", self)

    @property
    def HotelManagementClassDiagram_Booking12(self):
        return self.__HotelManagementClassDiagram_Booking12

    @HotelManagementClassDiagram_Booking12.setter
    def HotelManagementClassDiagram_Booking12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking12", None)
        self.__HotelManagementClassDiagram_Booking12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Discount"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Discount", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Discount"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Discount", self)
                    

    @property
    def HotelManagementClassDiagram_Booking(self):
        return self.__HotelManagementClassDiagram_Booking

    @HotelManagementClassDiagram_Booking.setter
    def HotelManagementClassDiagram_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking", None)
        self.__HotelManagementClassDiagram_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Creditcard"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Creditcard", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Creditcard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Creditcard"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Creditcard", None)
                setattr(value, "HotelManagementClassDiagram_Creditcard", self)

    @property
    def HotelManagementClassDiagram_Booking9(self):
        return self.__HotelManagementClassDiagram_Booking9

    @HotelManagementClassDiagram_Booking9.setter
    def HotelManagementClassDiagram_Booking9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking9", None)
        self.__HotelManagementClassDiagram_Booking9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Customer10"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Customer10", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Customer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Customer10"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Customer10", None)
                setattr(value, "HotelManagementClassDiagram_Customer10", self)

    @property
    def HotelManagementClassDiagram_Booking3(self):
        return self.__HotelManagementClassDiagram_Booking3

    @HotelManagementClassDiagram_Booking3.setter
    def HotelManagementClassDiagram_Booking3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking3", None)
        self.__HotelManagementClassDiagram_Booking3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Customer"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Customer", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Customer"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Customer", None)
                setattr(value, "HotelManagementClassDiagram_Customer", self)

    def pay(self, HotelManagementClassDiagram_bill) :
        # TODO: Implement pay method
        pass

    def checkOut(self) :
        # TODO: Implement checkOut method
        pass

    def removeAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement removeAddon method
        pass

    def checkIn(self):
        # TODO: Implement checkIn method
        pass

    def addRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement addRoom method
        pass

    def addDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement addDiscount method
        pass

    def addAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement addAddon method
        pass

    def removeRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement removeRoom method
        pass

    def removeDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement removeDiscount method
        pass

    def generateBill(self) :
        # TODO: Implement generateBill method
        pass

class HotelManagementClassDiagram_Person(ABC):

    def __init__(self, name: str, SSNumber: str, phoneNumber: str, street: str, city: str, postalCode: str, country: str, gender: str, title: str):
        self.name = name
        self.SSNumber = SSNumber
        self.phoneNumber = phoneNumber
        self.street = street
        self.city = city
        self.postalCode = postalCode
        self.country = country
        self.gender = gender
        self.title = title
        
        pass
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def postalCode(self):
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode


    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city


    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def SSNumber(self):
        return self.__SSNumber

    @SSNumber.setter
    def SSNumber(self, SSNumber: str):
        self.__SSNumber = SSNumber


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


class HotelManagementClassDiagram_EmployeeType:

    def __init__(self, type: str, acessLevel: int, HotelManagementClassDiagram_EmployeeType: "HotelManagementClassDiagram_Employee" = None):
        self.type = type
        self.acessLevel = acessLevel
        self.HotelManagementClassDiagram_EmployeeType = HotelManagementClassDiagram_EmployeeType
        
        pass
    @property
    def acessLevel(self):
        return self.__acessLevel

    @acessLevel.setter
    def acessLevel(self, acessLevel: int):
        self.__acessLevel = acessLevel


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def HotelManagementClassDiagram_EmployeeType(self):
        return self.__HotelManagementClassDiagram_EmployeeType

    @HotelManagementClassDiagram_EmployeeType.setter
    def HotelManagementClassDiagram_EmployeeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_EmployeeType__HotelManagementClassDiagram_EmployeeType", None)
        self.__HotelManagementClassDiagram_EmployeeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Employee"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Employee", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Employee"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Employee", None)
                setattr(value, "HotelManagementClassDiagram_Employee", self)

class Person:

    pass
class HotelManagementClassDiagram_Customer(Person):

    def __init__(self, customerID: int, bonusPoints: int, miscInfo: str, rank: float, HotelManagementClassDiagram_Customer10: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Customer: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Customer16: "HotelManagementClassDiagram_Bill" = None):
        self.customerID = customerID
        self.bonusPoints = bonusPoints
        self.miscInfo = miscInfo
        self.rank = rank
        self.HotelManagementClassDiagram_Customer10 = HotelManagementClassDiagram_Customer10
        self.HotelManagementClassDiagram_Customer = HotelManagementClassDiagram_Customer
        self.HotelManagementClassDiagram_Customer16 = HotelManagementClassDiagram_Customer16
        
        pass
    @property
    def customerID(self):
        return self.__customerID

    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID


    @property
    def bonusPoints(self):
        return self.__bonusPoints

    @bonusPoints.setter
    def bonusPoints(self, bonusPoints: int):
        self.__bonusPoints = bonusPoints


    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank: float):
        self.__rank = rank


    @property
    def miscInfo(self):
        return self.__miscInfo

    @miscInfo.setter
    def miscInfo(self, miscInfo: str):
        self.__miscInfo = miscInfo


    @property
    def HotelManagementClassDiagram_Customer(self):
        return self.__HotelManagementClassDiagram_Customer

    @HotelManagementClassDiagram_Customer.setter
    def HotelManagementClassDiagram_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Customer__HotelManagementClassDiagram_Customer", None)
        self.__HotelManagementClassDiagram_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking3"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking3", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Booking3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking3"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking3", None)
                setattr(value, "HotelManagementClassDiagram_Booking3", self)

    @property
    def HotelManagementClassDiagram_Customer10(self):
        return self.__HotelManagementClassDiagram_Customer10

    @HotelManagementClassDiagram_Customer10.setter
    def HotelManagementClassDiagram_Customer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Customer__HotelManagementClassDiagram_Customer10", None)
        self.__HotelManagementClassDiagram_Customer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking9"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking9", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Booking9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking9"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking9", None)
                setattr(value, "HotelManagementClassDiagram_Booking9", self)

    @property
    def HotelManagementClassDiagram_Customer16(self):
        return self.__HotelManagementClassDiagram_Customer16

    @HotelManagementClassDiagram_Customer16.setter
    def HotelManagementClassDiagram_Customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Customer__HotelManagementClassDiagram_Customer16", None)
        self.__HotelManagementClassDiagram_Customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Bill15"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Bill15", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Bill15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Bill15"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Bill15", None)
                setattr(value, "HotelManagementClassDiagram_Bill15", self)

    def addBonusPoints(self, HotelManagementClassDiagram_bonusPoints):
        # TODO: Implement addBonusPoints method
        pass

class HotelManagementClassDiagram_Employee(Person):

    def __init__(self, employeeID: int, workRate: int, salary: float, HotelManagementClassDiagram_Employee: "HotelManagementClassDiagram_EmployeeType" = None, HotelManagementClassDiagram_Employee25: "HotelManagementClassDiagram_Interaction1" = None, HotelManagementClassDiagram_Employee27: "HotelManagementClassDiagram_Interaction2" = None, HotelManagementClassDiagram_Employee31: "HotelManagementClassDiagram_Interaction4" = None):
        self.employeeID = employeeID
        self.workRate = workRate
        self.salary = salary
        self.HotelManagementClassDiagram_Employee = HotelManagementClassDiagram_Employee
        self.HotelManagementClassDiagram_Employee25 = HotelManagementClassDiagram_Employee25
        self.HotelManagementClassDiagram_Employee27 = HotelManagementClassDiagram_Employee27
        self.HotelManagementClassDiagram_Employee31 = HotelManagementClassDiagram_Employee31
        
        pass
    @property
    def employeeID(self):
        return self.__employeeID

    @employeeID.setter
    def employeeID(self, employeeID: int):
        self.__employeeID = employeeID


    @property
    def workRate(self):
        return self.__workRate

    @workRate.setter
    def workRate(self, workRate: int):
        self.__workRate = workRate


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary


    @property
    def HotelManagementClassDiagram_Employee(self):
        return self.__HotelManagementClassDiagram_Employee

    @HotelManagementClassDiagram_Employee.setter
    def HotelManagementClassDiagram_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee", None)
        self.__HotelManagementClassDiagram_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_EmployeeType"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_EmployeeType", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_EmployeeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_EmployeeType"):
                opp_val = getattr(value, "HotelManagementClassDiagram_EmployeeType", None)
                setattr(value, "HotelManagementClassDiagram_EmployeeType", self)

    @property
    def HotelManagementClassDiagram_Employee27(self):
        return self.__HotelManagementClassDiagram_Employee27

    @HotelManagementClassDiagram_Employee27.setter
    def HotelManagementClassDiagram_Employee27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee27", None)
        self.__HotelManagementClassDiagram_Employee27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Interaction2"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Interaction2", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Interaction2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Interaction2"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Interaction2", None)
                setattr(value, "HotelManagementClassDiagram_Interaction2", self)

    @property
    def HotelManagementClassDiagram_Employee25(self):
        return self.__HotelManagementClassDiagram_Employee25

    @HotelManagementClassDiagram_Employee25.setter
    def HotelManagementClassDiagram_Employee25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee25", None)
        self.__HotelManagementClassDiagram_Employee25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Interaction1"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Interaction1", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Interaction1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Interaction1"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Interaction1", None)
                setattr(value, "HotelManagementClassDiagram_Interaction1", self)

    @property
    def HotelManagementClassDiagram_Employee31(self):
        return self.__HotelManagementClassDiagram_Employee31

    @HotelManagementClassDiagram_Employee31.setter
    def HotelManagementClassDiagram_Employee31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee31", None)
        self.__HotelManagementClassDiagram_Employee31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Interaction4"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Interaction4", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Interaction4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Interaction4"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Interaction4", None)
                setattr(value, "HotelManagementClassDiagram_Interaction4", self)

    def Booking(self):
        # TODO: Implement Booking method
        pass

    def Boolean(self):
        # TODO: Implement Boolean method
        pass

    def roomTypes(self):
        # TODO: Implement roomTypes method
        pass
