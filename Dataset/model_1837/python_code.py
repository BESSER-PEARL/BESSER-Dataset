from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomType(Enum):
    Double = "Double"
    Single = "Single"
    Suite = "Suite"
    Family = "Family"
class EType(Enum):
    Receptionist = "Receptionist"
    Cleaner = "Cleaner"
    Manager = "Manager"


############################################
# Definition of Classes
############################################

class DBInterface:

    pass
class HotelManagementClassDiagram_FakeDBContext(DBInterface):

    pass
class HotelManagementClassDiagram_DBInterface(ABC):

    def __init__(self):
        
        pass
    def updateOrAddBooking(self, HotelManagementClassDiagram_booking):
        # TODO: Implement updateOrAddBooking method
        pass

    def getBooking(self, HotelManagementClassDiagram_bookingID) :
        # TODO: Implement getBooking method
        pass

    def getAllCleaners(self) :
        # TODO: Implement getAllCleaners method
        pass

    def getAvailableRooms(self, HotelManagementClassDiagram_type, HotelManagementClassDiagram_from_, HotelManagementClassDiagram_to) :
        # TODO: Implement getAvailableRooms method
        pass

    def updateOrAddExtra(self, HotelManagementClassDiagram_extra):
        # TODO: Implement updateOrAddExtra method
        pass

    def getEmployee(self, HotelManagementClassDiagram_employeeSSNumber) :
        # TODO: Implement getEmployee method
        pass

    def getAllAddons(self) :
        # TODO: Implement getAllAddons method
        pass

    def getAllManagers(self) :
        # TODO: Implement getAllManagers method
        pass

    def getAllBookings(self) :
        # TODO: Implement getAllBookings method
        pass

    def getBookings(self, HotelManagementClassDiagram_toDate, HotelManagementClassDiagram_fromDate) :
        # TODO: Implement getBookings method
        pass

    def getDiscount(self, HotelManagementClassDiagram_discountName) :
        # TODO: Implement getDiscount method
        pass

    def getAllEmployees(self) :
        # TODO: Implement getAllEmployees method
        pass

    def getAllCustomers(self) :
        # TODO: Implement getAllCustomers method
        pass

    def updateOrAddRoomType(self, HotelManagementClassDiagram_type):
        # TODO: Implement updateOrAddRoomType method
        pass

    def getCurrentBookings(self) :
        # TODO: Implement getCurrentBookings method
        pass

    def getFutureBookings(self) :
        # TODO: Implement getFutureBookings method
        pass

    def updateOrAddRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement updateOrAddRoom method
        pass

    def getAllRoomTypes(self) :
        # TODO: Implement getAllRoomTypes method
        pass

    def getRoom(self, HotelManagementClassDiagram_roomNumber) :
        # TODO: Implement getRoom method
        pass

    def getAddon(self, HotelManagementClassDiagram_addonName) :
        # TODO: Implement getAddon method
        pass

    def updateOrAddEmployeeType(self, HotelManagementClassDiagram_type):
        # TODO: Implement updateOrAddEmployeeType method
        pass

    def updateOrAddDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement updateOrAddDiscount method
        pass

    def getAvaliableRoomTypes(self, HotelManagementClassDiagram_from_, HotelManagementClassDiagram_to) :
        # TODO: Implement getAvaliableRoomTypes method
        pass

    def getAllDiscounts(self) :
        # TODO: Implement getAllDiscounts method
        pass

    def _getAllRooms(self) :
        # TODO: Implement _getAllRooms method
        pass

    def updateOrAddCustomer(self, HotelManagementClassDiagram_customer):
        # TODO: Implement updateOrAddCustomer method
        pass

    def getCustomer(self, HotelManagementClassDiagram_customerSSNumber) :
        # TODO: Implement getCustomer method
        pass

    def findCustomers(self, HotelManagementClassDiagram_partOfCustomerName) :
        # TODO: Implement findCustomers method
        pass

    def getPastBookings(self) :
        # TODO: Implement getPastBookings method
        pass

    def getAllReceptionists(self) :
        # TODO: Implement getAllReceptionists method
        pass

    def updateOrAddAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement updateOrAddAddon method
        pass

    def updateOrAddEmployee(self, HotelManagementClassDiagram_employee):
        # TODO: Implement updateOrAddEmployee method
        pass

    def findBookings(self, HotelManagementClassDiagram_customerName) :
        # TODO: Implement findBookings method
        pass

    def getRooms(self, HotelManagementClassDiagram_type) :
        # TODO: Implement getRooms method
        pass

class HotelManagementClassDiagram_Interaction5:

    pass
class HotelManagementClassDiagram_Interaction4:

    pass
class HotelManagementClassDiagram_Interaction3:

    pass
class HotelManagementClassDiagram_Interaction2:

    pass
class HotelManagementClassDiagram_Interaction1:

    pass
class HotelManagementClassDiagram_Hotel:

    def __init__(self, name: str, address: str, rank: float, HotelManagementClassDiagram_Hotel: "HotelManagementClassDiagram_BookingController" = None, HotelManagementClassDiagram_Hotel24: "HotelManagementClassDiagram_MaintenanceController" = None, HotelManagementClassDiagram_Hotel27: "HotelManagementClassDiagram_ManagementController" = None, HotelManagementClassDiagram_Hotel29: "HotelManagementClassDiagram_Employee" = None):
        self.name = name
        self.address = address
        self.rank = rank
        self.HotelManagementClassDiagram_Hotel = HotelManagementClassDiagram_Hotel
        self.HotelManagementClassDiagram_Hotel24 = HotelManagementClassDiagram_Hotel24
        self.HotelManagementClassDiagram_Hotel27 = HotelManagementClassDiagram_Hotel27
        self.HotelManagementClassDiagram_Hotel29 = HotelManagementClassDiagram_Hotel29
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def HotelManagementClassDiagram_Hotel(self):
        return self.__HotelManagementClassDiagram_Hotel

    @HotelManagementClassDiagram_Hotel.setter
    def HotelManagementClassDiagram_Hotel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Hotel__HotelManagementClassDiagram_Hotel", None)
        self.__HotelManagementClassDiagram_Hotel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_BookingController"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_BookingController", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_BookingController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_BookingController"):
                opp_val = getattr(value, "HotelManagementClassDiagram_BookingController", None)
                setattr(value, "HotelManagementClassDiagram_BookingController", self)

    @property
    def HotelManagementClassDiagram_Hotel29(self):
        return self.__HotelManagementClassDiagram_Hotel29

    @HotelManagementClassDiagram_Hotel29.setter
    def HotelManagementClassDiagram_Hotel29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Hotel__HotelManagementClassDiagram_Hotel29", None)
        self.__HotelManagementClassDiagram_Hotel29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Employee30"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Employee30", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Employee30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Employee30"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Employee30", None)
                setattr(value, "HotelManagementClassDiagram_Employee30", self)

    @property
    def HotelManagementClassDiagram_Hotel24(self):
        return self.__HotelManagementClassDiagram_Hotel24

    @HotelManagementClassDiagram_Hotel24.setter
    def HotelManagementClassDiagram_Hotel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Hotel__HotelManagementClassDiagram_Hotel24", None)
        self.__HotelManagementClassDiagram_Hotel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_MaintenanceController25"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_MaintenanceController25", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_MaintenanceController25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_MaintenanceController25"):
                opp_val = getattr(value, "HotelManagementClassDiagram_MaintenanceController25", None)
                setattr(value, "HotelManagementClassDiagram_MaintenanceController25", self)

    @property
    def HotelManagementClassDiagram_Hotel27(self):
        return self.__HotelManagementClassDiagram_Hotel27

    @HotelManagementClassDiagram_Hotel27.setter
    def HotelManagementClassDiagram_Hotel27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Hotel__HotelManagementClassDiagram_Hotel27", None)
        self.__HotelManagementClassDiagram_Hotel27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_ManagementController"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_ManagementController", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_ManagementController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_ManagementController"):
                opp_val = getattr(value, "HotelManagementClassDiagram_ManagementController", None)
                setattr(value, "HotelManagementClassDiagram_ManagementController", self)

    def logIn(self, HotelManagementClassDiagram_SSN, HotelManagementClassDiagram_password) :
        # TODO: Implement logIn method
        pass

class HotelManagementClassDiagram_MaintenanceController:

    def __init__(self, HotelManagementClassDiagram_MaintenanceController25: "HotelManagementClassDiagram_Hotel" = None, HotelManagementClassDiagram_MaintenanceController36: "HotelManagementClassDiagram_Interaction3" = None, HotelManagementClassDiagram_MaintenanceController: set["HotelManagementClassDiagram_Room"] = None):
        self.HotelManagementClassDiagram_MaintenanceController25 = HotelManagementClassDiagram_MaintenanceController25
        self.HotelManagementClassDiagram_MaintenanceController36 = HotelManagementClassDiagram_MaintenanceController36
        self.HotelManagementClassDiagram_MaintenanceController = HotelManagementClassDiagram_MaintenanceController if HotelManagementClassDiagram_MaintenanceController is not None else set()
        
        pass
    @property
    def HotelManagementClassDiagram_MaintenanceController36(self):
        return self.__HotelManagementClassDiagram_MaintenanceController36

    @HotelManagementClassDiagram_MaintenanceController36.setter
    def HotelManagementClassDiagram_MaintenanceController36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_MaintenanceController__HotelManagementClassDiagram_MaintenanceController36", None)
        self.__HotelManagementClassDiagram_MaintenanceController36 = value
        
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

    @property
    def HotelManagementClassDiagram_MaintenanceController25(self):
        return self.__HotelManagementClassDiagram_MaintenanceController25

    @HotelManagementClassDiagram_MaintenanceController25.setter
    def HotelManagementClassDiagram_MaintenanceController25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_MaintenanceController__HotelManagementClassDiagram_MaintenanceController25", None)
        self.__HotelManagementClassDiagram_MaintenanceController25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Hotel24"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Hotel24", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Hotel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Hotel24"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Hotel24", None)
                setattr(value, "HotelManagementClassDiagram_Hotel24", self)

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
                    

    def getNextRoomToClean(self) :
        # TODO: Implement getNextRoomToClean method
        pass

    def removeFromQueue(self, HotelManagementClassDiagram_room):
        # TODO: Implement removeFromQueue method
        pass

    def addToQueue(self, HotelManagementClassDiagram_room):
        # TODO: Implement addToQueue method
        pass

    def setCleanedStatus(self, HotelManagementClassDiagram_room, HotelManagementClassDiagram_status):
        # TODO: Implement setCleanedStatus method
        pass

    def setRepairedStatus(self, HotelManagementClassDiagram_repaired, HotelManagementClassDiagram_room):
        # TODO: Implement setRepairedStatus method
        pass

class HotelManagementClassDiagram_ManagementController:

    def __init__(self, HotelManagementClassDiagram_ManagementController: "HotelManagementClassDiagram_Hotel" = None):
        self.HotelManagementClassDiagram_ManagementController = HotelManagementClassDiagram_ManagementController
        
        pass
    @property
    def HotelManagementClassDiagram_ManagementController(self):
        return self.__HotelManagementClassDiagram_ManagementController

    @HotelManagementClassDiagram_ManagementController.setter
    def HotelManagementClassDiagram_ManagementController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_ManagementController__HotelManagementClassDiagram_ManagementController", None)
        self.__HotelManagementClassDiagram_ManagementController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Hotel27"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Hotel27", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Hotel27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Hotel27"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Hotel27", None)
                setattr(value, "HotelManagementClassDiagram_Hotel27", self)

    def updateOrAddDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement updateOrAddDiscount method
        pass

    def getAllEmployees(self) :
        # TODO: Implement getAllEmployees method
        pass

    def updateOrAddRoomType(self, HotelManagementClassDiagram_roomType):
        # TODO: Implement updateOrAddRoomType method
        pass

    def getAllExtras(self) :
        # TODO: Implement getAllExtras method
        pass

    def updateOrAddAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement updateOrAddAddon method
        pass

    def updateOrAddEmployeeType(self, HotelManagementClassDiagram_employeeType):
        # TODO: Implement updateOrAddEmployeeType method
        pass

    def updateOrAddEmployee(self, HotelManagementClassDiagram_employee):
        # TODO: Implement updateOrAddEmployee method
        pass

    def getAllAddons(self) :
        # TODO: Implement getAllAddons method
        pass

    def updateOrAddRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement updateOrAddRoom method
        pass

    def updateOrAddExtra(self, HotelManagementClassDiagram_extra):
        # TODO: Implement updateOrAddExtra method
        pass

    def getEmployee(self, HotelManagementClassDiagram_SSN) :
        # TODO: Implement getEmployee method
        pass

    def getAllDiscounts(self) :
        # TODO: Implement getAllDiscounts method
        pass

class HotelManagementClassDiagram_BookingController:

    def __init__(self, HotelManagementClassDiagram_BookingController: "HotelManagementClassDiagram_Hotel" = None):
        self.HotelManagementClassDiagram_BookingController = HotelManagementClassDiagram_BookingController
        
        pass
    @property
    def HotelManagementClassDiagram_BookingController(self):
        return self.__HotelManagementClassDiagram_BookingController

    @HotelManagementClassDiagram_BookingController.setter
    def HotelManagementClassDiagram_BookingController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_BookingController__HotelManagementClassDiagram_BookingController", None)
        self.__HotelManagementClassDiagram_BookingController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Hotel"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Hotel", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Hotel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Hotel"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Hotel", None)
                setattr(value, "HotelManagementClassDiagram_Hotel", self)

    def checkIn(self, HotelManagementClassDiagram_booking):
        # TODO: Implement checkIn method
        pass

    def sendConfirmation(self, HotelManagementClassDiagram_booking) :
        # TODO: Implement sendConfirmation method
        pass

    def saveCustomer(self, HotelManagementClassDiagram_customer):
        # TODO: Implement saveCustomer method
        pass

    def getAllCustomers(self) :
        # TODO: Implement getAllCustomers method
        pass

    def getCustomer(self, HotelManagementClassDiagram_SSN) :
        # TODO: Implement getCustomer method
        pass

    def getAllBookings(self) :
        # TODO: Implement getAllBookings method
        pass

    def updateOrAddCustomer(self, HotelManagementClassDiagram_customer):
        # TODO: Implement updateOrAddCustomer method
        pass

    def checkOut(self, HotelManagementClassDiagram_booking):
        # TODO: Implement checkOut method
        pass

    def searchAvailableRoomTypes(self, HotelManagementClassDiagram_nbrOfAdults, HotelManagementClassDiagram_toDate, HotelManagementClassDiagram_nbrOfChildren, HotelManagementClassDiagram_fromDate) :
        # TODO: Implement searchAvailableRoomTypes method
        pass

    def updateOrAddBooking(self, HotelManagementClassDiagram_booking):
        # TODO: Implement updateOrAddBooking method
        pass

    def assignRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement assignRoom method
        pass

    def findCustomer(self, HotelManagementClassDiagram_ssNumber):
        # TODO: Implement findCustomer method
        pass

    def getBooking(self, HotelManagementClassDiagram_bookingId) :
        # TODO: Implement getBooking method
        pass

class HotelManagementClassDiagram_Costable(ABC):

    def __init__(self, price: float, HotelManagementClassDiagram_Costable16: "HotelManagementClassDiagram_Bill" = None, HotelManagementClassDiagram_Costable: set["HotelManagementClassDiagram_Discount"] = None):
        self.price = price
        self.HotelManagementClassDiagram_Costable16 = HotelManagementClassDiagram_Costable16
        self.HotelManagementClassDiagram_Costable = HotelManagementClassDiagram_Costable if HotelManagementClassDiagram_Costable is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def HotelManagementClassDiagram_Costable16(self):
        return self.__HotelManagementClassDiagram_Costable16

    @HotelManagementClassDiagram_Costable16.setter
    def HotelManagementClassDiagram_Costable16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Costable__HotelManagementClassDiagram_Costable16", None)
        self.__HotelManagementClassDiagram_Costable16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Bill15"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Bill15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Bill15"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Bill15", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Bill15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Costable(self):
        return self.__HotelManagementClassDiagram_Costable

    @HotelManagementClassDiagram_Costable.setter
    def HotelManagementClassDiagram_Costable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Costable__HotelManagementClassDiagram_Costable", None)
        self.__HotelManagementClassDiagram_Costable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Discount13"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount13", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Discount13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Discount13"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Discount13", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Discount13", self)
                    

    def removeDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement removeDiscount method
        pass

    def addDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement addDiscount method
        pass

class HotelManagementClassDiagram_Extra:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
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


class Costable:

    pass
class Extra:

    pass
class HotelManagementClassDiagram_Bill:

    def __init__(self, totalPrice: float, final: bool, paid: bool, HotelManagementClassDiagram_Bill: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Bill15: set["HotelManagementClassDiagram_Costable"] = None, HotelManagementClassDiagram_Bill18: "HotelManagementClassDiagram_Customer" = None):
        self.totalPrice = totalPrice
        self.final = final
        self.paid = paid
        self.HotelManagementClassDiagram_Bill = HotelManagementClassDiagram_Bill
        self.HotelManagementClassDiagram_Bill15 = HotelManagementClassDiagram_Bill15 if HotelManagementClassDiagram_Bill15 is not None else set()
        self.HotelManagementClassDiagram_Bill18 = HotelManagementClassDiagram_Bill18
        
        pass
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
    def paid(self):
        return self.__paid

    @paid.setter
    def paid(self, paid: bool):
        self.__paid = paid


    @property
    def HotelManagementClassDiagram_Bill(self):
        return self.__HotelManagementClassDiagram_Bill

    @HotelManagementClassDiagram_Bill.setter
    def HotelManagementClassDiagram_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Bill__HotelManagementClassDiagram_Bill", None)
        self.__HotelManagementClassDiagram_Bill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Booking11"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking11", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Booking11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking11"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking11", None)
                setattr(value, "HotelManagementClassDiagram_Booking11", self)

    @property
    def HotelManagementClassDiagram_Bill15(self):
        return self.__HotelManagementClassDiagram_Bill15

    @HotelManagementClassDiagram_Bill15.setter
    def HotelManagementClassDiagram_Bill15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Bill__HotelManagementClassDiagram_Bill15", None)
        self.__HotelManagementClassDiagram_Bill15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelManagementClassDiagram_Costable16"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Costable16", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelManagementClassDiagram_Costable16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelManagementClassDiagram_Costable16"):
                    opp_val = getattr(item, "HotelManagementClassDiagram_Costable16", None)
                    
                    setattr(item, "HotelManagementClassDiagram_Costable16", self)
                    

    @property
    def HotelManagementClassDiagram_Bill18(self):
        return self.__HotelManagementClassDiagram_Bill18

    @HotelManagementClassDiagram_Bill18.setter
    def HotelManagementClassDiagram_Bill18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Bill__HotelManagementClassDiagram_Bill18", None)
        self.__HotelManagementClassDiagram_Bill18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Customer19"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Customer19", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Customer19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Customer19"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Customer19", None)
                setattr(value, "HotelManagementClassDiagram_Customer19", self)

    def addCostable(self, HotelManagementClassDiagram_costable):
        # TODO: Implement addCostable method
        pass

class HotelManagementClassDiagram_Discount:

    def __init__(self, name: str, isPercentage: str, amount: float, HotelManagementClassDiagram_Discount: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Discount13: "HotelManagementClassDiagram_Costable" = None):
        self.name = name
        self.isPercentage = isPercentage
        self.amount = amount
        self.HotelManagementClassDiagram_Discount = HotelManagementClassDiagram_Discount
        self.HotelManagementClassDiagram_Discount13 = HotelManagementClassDiagram_Discount13
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount


    @property
    def isPercentage(self):
        return self.__isPercentage

    @isPercentage.setter
    def isPercentage(self, isPercentage: str):
        self.__isPercentage = isPercentage


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
            if hasattr(old_value, "HotelManagementClassDiagram_Booking9"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking9"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking9", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Booking9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HotelManagementClassDiagram_Discount13(self):
        return self.__HotelManagementClassDiagram_Discount13

    @HotelManagementClassDiagram_Discount13.setter
    def HotelManagementClassDiagram_Discount13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Discount__HotelManagementClassDiagram_Discount13", None)
        self.__HotelManagementClassDiagram_Discount13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Costable"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Costable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Costable"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Costable", None)
                if opp_val is None:
                    setattr(value, "HotelManagementClassDiagram_Costable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HotelManagementClassDiagram_Room(Costable):

    def __init__(self, roomNumber: int, size: float, internalComment: str, maxNbrPeople: int, underCleaning: bool, underRepair: bool, type: str, HotelManagementClassDiagram_Room: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Room21: "HotelManagementClassDiagram_MaintenanceController" = None):
        self.roomNumber = roomNumber
        self.size = size
        self.internalComment = internalComment
        self.maxNbrPeople = maxNbrPeople
        self.underCleaning = underCleaning
        self.underRepair = underRepair
        self.type = type
        self.HotelManagementClassDiagram_Room = HotelManagementClassDiagram_Room
        self.HotelManagementClassDiagram_Room21 = HotelManagementClassDiagram_Room21
        
        pass
    @property
    def underCleaning(self):
        return self.__underCleaning

    @underCleaning.setter
    def underCleaning(self, underCleaning: bool):
        self.__underCleaning = underCleaning


    @property
    def underRepair(self):
        return self.__underRepair

    @underRepair.setter
    def underRepair(self, underRepair: bool):
        self.__underRepair = underRepair


    @property
    def maxNbrPeople(self):
        return self.__maxNbrPeople

    @maxNbrPeople.setter
    def maxNbrPeople(self, maxNbrPeople: int):
        self.__maxNbrPeople = maxNbrPeople


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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def internalComment(self):
        return self.__internalComment

    @internalComment.setter
    def internalComment(self, internalComment: str):
        self.__internalComment = internalComment


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

class HotelManagementClassDiagram_Addon(Costable, Extra):

    pass
class HotelManagementClassDiagram_Creditcard:

    def __init__(self, number: str, cvc: int, owner: str, expirationMonth: int, expirationYear: int, HotelManagementClassDiagram_Creditcard: "HotelManagementClassDiagram_Booking" = None):
        self.number = number
        self.cvc = cvc
        self.owner = owner
        self.expirationMonth = expirationMonth
        self.expirationYear = expirationYear
        self.HotelManagementClassDiagram_Creditcard = HotelManagementClassDiagram_Creditcard
        
        pass
    @property
    def expirationMonth(self):
        return self.__expirationMonth

    @expirationMonth.setter
    def expirationMonth(self, expirationMonth: int):
        self.__expirationMonth = expirationMonth


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def cvc(self):
        return self.__cvc

    @cvc.setter
    def cvc(self, cvc: int):
        self.__cvc = cvc


    @property
    def expirationYear(self):
        return self.__expirationYear

    @expirationYear.setter
    def expirationYear(self, expirationYear: int):
        self.__expirationYear = expirationYear


    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner


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

    def __init__(self, customerID: int, bonusPoints: int, miscInfo: str, HotelManagementClassDiagram_Customer: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Customer19: "HotelManagementClassDiagram_Bill" = None):
        self.customerID = customerID
        self.bonusPoints = bonusPoints
        self.miscInfo = miscInfo
        self.HotelManagementClassDiagram_Customer = HotelManagementClassDiagram_Customer
        self.HotelManagementClassDiagram_Customer19 = HotelManagementClassDiagram_Customer19
        
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
            if hasattr(old_value, "HotelManagementClassDiagram_Booking7"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Booking7", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Booking7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Booking7"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Booking7", None)
                setattr(value, "HotelManagementClassDiagram_Booking7", self)

    @property
    def HotelManagementClassDiagram_Customer19(self):
        return self.__HotelManagementClassDiagram_Customer19

    @HotelManagementClassDiagram_Customer19.setter
    def HotelManagementClassDiagram_Customer19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Customer__HotelManagementClassDiagram_Customer19", None)
        self.__HotelManagementClassDiagram_Customer19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Bill18"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Bill18", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Bill18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Bill18"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Bill18", None)
                setattr(value, "HotelManagementClassDiagram_Bill18", self)

    def addBonusPoints(self, HotelManagementClassDiagram_bonusPoints):
        # TODO: Implement addBonusPoints method
        pass

class HotelManagementClassDiagram_Employee(Person):

    def __init__(self, salary: float, password: str, employeeID: int, workRate: float, HotelManagementClassDiagram_Employee: "HotelManagementClassDiagram_EmployeeType" = None, HotelManagementClassDiagram_Employee30: "HotelManagementClassDiagram_Hotel" = None, HotelManagementClassDiagram_Employee32: "HotelManagementClassDiagram_Interaction1" = None, HotelManagementClassDiagram_Employee34: "HotelManagementClassDiagram_Interaction2" = None, HotelManagementClassDiagram_Employee38: "HotelManagementClassDiagram_Interaction4" = None):
        self.salary = salary
        self.password = password
        self.employeeID = employeeID
        self.workRate = workRate
        self.HotelManagementClassDiagram_Employee = HotelManagementClassDiagram_Employee
        self.HotelManagementClassDiagram_Employee30 = HotelManagementClassDiagram_Employee30
        self.HotelManagementClassDiagram_Employee32 = HotelManagementClassDiagram_Employee32
        self.HotelManagementClassDiagram_Employee34 = HotelManagementClassDiagram_Employee34
        self.HotelManagementClassDiagram_Employee38 = HotelManagementClassDiagram_Employee38
        
        pass
    @property
    def workRate(self):
        return self.__workRate

    @workRate.setter
    def workRate(self, workRate: float):
        self.__workRate = workRate


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def employeeID(self):
        return self.__employeeID

    @employeeID.setter
    def employeeID(self, employeeID: int):
        self.__employeeID = employeeID


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary


    @property
    def HotelManagementClassDiagram_Employee38(self):
        return self.__HotelManagementClassDiagram_Employee38

    @HotelManagementClassDiagram_Employee38.setter
    def HotelManagementClassDiagram_Employee38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee38", None)
        self.__HotelManagementClassDiagram_Employee38 = value
        
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

    @property
    def HotelManagementClassDiagram_Employee30(self):
        return self.__HotelManagementClassDiagram_Employee30

    @HotelManagementClassDiagram_Employee30.setter
    def HotelManagementClassDiagram_Employee30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee30", None)
        self.__HotelManagementClassDiagram_Employee30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Hotel29"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Hotel29", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Hotel29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Hotel29"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Hotel29", None)
                setattr(value, "HotelManagementClassDiagram_Hotel29", self)

    @property
    def HotelManagementClassDiagram_Employee32(self):
        return self.__HotelManagementClassDiagram_Employee32

    @HotelManagementClassDiagram_Employee32.setter
    def HotelManagementClassDiagram_Employee32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee32", None)
        self.__HotelManagementClassDiagram_Employee32 = value
        
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
    def HotelManagementClassDiagram_Employee34(self):
        return self.__HotelManagementClassDiagram_Employee34

    @HotelManagementClassDiagram_Employee34.setter
    def HotelManagementClassDiagram_Employee34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Employee__HotelManagementClassDiagram_Employee34", None)
        self.__HotelManagementClassDiagram_Employee34 = value
        
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

    def Boolean(self):
        # TODO: Implement Boolean method
        pass

    def roomTypes(self):
        # TODO: Implement roomTypes method
        pass

    def Booking(self):
        # TODO: Implement Booking method
        pass

class HotelManagementClassDiagram_Booking:

    def __init__(self, internalComments: str, externalComments: str, checkedIn: bool, checkedOut: bool, roomTypes: str, bookingId: int, startDate: date, endDate: date, created: date, HotelManagementClassDiagram_Booking: "HotelManagementClassDiagram_Creditcard" = None, HotelManagementClassDiagram_Booking3: set["HotelManagementClassDiagram_Addon"] = None, HotelManagementClassDiagram_Booking5: set["HotelManagementClassDiagram_Room"] = None, HotelManagementClassDiagram_Booking7: "HotelManagementClassDiagram_Customer" = None, HotelManagementClassDiagram_Booking9: set["HotelManagementClassDiagram_Discount"] = None, HotelManagementClassDiagram_Booking11: "HotelManagementClassDiagram_Bill" = None, HotelManagementClassDiagram_Booking40: "HotelManagementClassDiagram_Interaction5" = None):
        self.internalComments = internalComments
        self.externalComments = externalComments
        self.checkedIn = checkedIn
        self.checkedOut = checkedOut
        self.roomTypes = roomTypes
        self.bookingId = bookingId
        self.startDate = startDate
        self.endDate = endDate
        self.created = created
        self.HotelManagementClassDiagram_Booking = HotelManagementClassDiagram_Booking
        self.HotelManagementClassDiagram_Booking3 = HotelManagementClassDiagram_Booking3 if HotelManagementClassDiagram_Booking3 is not None else set()
        self.HotelManagementClassDiagram_Booking5 = HotelManagementClassDiagram_Booking5 if HotelManagementClassDiagram_Booking5 is not None else set()
        self.HotelManagementClassDiagram_Booking7 = HotelManagementClassDiagram_Booking7
        self.HotelManagementClassDiagram_Booking9 = HotelManagementClassDiagram_Booking9 if HotelManagementClassDiagram_Booking9 is not None else set()
        self.HotelManagementClassDiagram_Booking11 = HotelManagementClassDiagram_Booking11
        self.HotelManagementClassDiagram_Booking40 = HotelManagementClassDiagram_Booking40
        
        pass
    @property
    def roomTypes(self):
        return self.__roomTypes

    @roomTypes.setter
    def roomTypes(self, roomTypes: str):
        self.__roomTypes = roomTypes


    @property
    def externalComments(self):
        return self.__externalComments

    @externalComments.setter
    def externalComments(self, externalComments: str):
        self.__externalComments = externalComments


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate


    @property
    def checkedIn(self):
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn


    @property
    def bookingId(self):
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId


    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created


    @property
    def internalComments(self):
        return self.__internalComments

    @internalComments.setter
    def internalComments(self, internalComments: str):
        self.__internalComments = internalComments


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


    @property
    def checkedOut(self):
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: bool):
        self.__checkedOut = checkedOut


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
    def HotelManagementClassDiagram_Booking7(self):
        return self.__HotelManagementClassDiagram_Booking7

    @HotelManagementClassDiagram_Booking7.setter
    def HotelManagementClassDiagram_Booking7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking7", None)
        self.__HotelManagementClassDiagram_Booking7 = value
        
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
    def HotelManagementClassDiagram_Booking40(self):
        return self.__HotelManagementClassDiagram_Booking40

    @HotelManagementClassDiagram_Booking40.setter
    def HotelManagementClassDiagram_Booking40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking40", None)
        self.__HotelManagementClassDiagram_Booking40 = value
        
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
    def HotelManagementClassDiagram_Booking9(self):
        return self.__HotelManagementClassDiagram_Booking9

    @HotelManagementClassDiagram_Booking9.setter
    def HotelManagementClassDiagram_Booking9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking9", None)
        self.__HotelManagementClassDiagram_Booking9 = value if value is not None else set()
        
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
    def HotelManagementClassDiagram_Booking11(self):
        return self.__HotelManagementClassDiagram_Booking11

    @HotelManagementClassDiagram_Booking11.setter
    def HotelManagementClassDiagram_Booking11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking11", None)
        self.__HotelManagementClassDiagram_Booking11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HotelManagementClassDiagram_Bill"):
                opp_val = getattr(old_value, "HotelManagementClassDiagram_Bill", None)
                if opp_val == self:
                    setattr(old_value, "HotelManagementClassDiagram_Bill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HotelManagementClassDiagram_Bill"):
                opp_val = getattr(value, "HotelManagementClassDiagram_Bill", None)
                setattr(value, "HotelManagementClassDiagram_Bill", self)

    @property
    def HotelManagementClassDiagram_Booking3(self):
        return self.__HotelManagementClassDiagram_Booking3

    @HotelManagementClassDiagram_Booking3.setter
    def HotelManagementClassDiagram_Booking3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HotelManagementClassDiagram_Booking__HotelManagementClassDiagram_Booking3", None)
        self.__HotelManagementClassDiagram_Booking3 = value if value is not None else set()
        
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
                    

    def removeRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement removeRoom method
        pass

    def pay(self, HotelManagementClassDiagram_bill) :
        # TODO: Implement pay method
        pass

    def addDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement addDiscount method
        pass

    def addRoom(self, HotelManagementClassDiagram_room):
        # TODO: Implement addRoom method
        pass

    def removeAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement removeAddon method
        pass

    def checkIn(self):
        # TODO: Implement checkIn method
        pass

    def generateBill(self) :
        # TODO: Implement generateBill method
        pass

    def addAddon(self, HotelManagementClassDiagram_addon):
        # TODO: Implement addAddon method
        pass

    def removeDiscount(self, HotelManagementClassDiagram_discount):
        # TODO: Implement removeDiscount method
        pass

    def checkOut(self) :
        # TODO: Implement checkOut method
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
    def SSNumber(self):
        return self.__SSNumber

    @SSNumber.setter
    def SSNumber(self, SSNumber: str):
        self.__SSNumber = SSNumber


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street


    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def postalCode(self):
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

