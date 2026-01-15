from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomType(Enum):
    Family = "Family"
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

class DBInterface:

    pass
class HotelManagementClassDiagram_FakeDBContext(DBInterface):

    pass
class HotelManagementClassDiagram_DBInterface(ABC):

    def __init__(self):
        
    def getAllDiscounts(self) -> str:
        # TODO: Implement getAllDiscounts method
        pass

    def getDiscount(self, discountName: str) -> str:
        # TODO: Implement getDiscount method
        pass

    def getAvailableRooms(self, type: str, to: date, from: date) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def getAllCustomers(self) -> str:
        # TODO: Implement getAllCustomers method
        pass

    def updateOrAddEmployee(self, employee: str):
        # TODO: Implement updateOrAddEmployee method
        pass

    def getFutureBookings(self) -> str:
        # TODO: Implement getFutureBookings method
        pass

    def updateOrAddRoom(self, room: str):
        # TODO: Implement updateOrAddRoom method
        pass

    def getAllBookings(self) -> str:
        # TODO: Implement getAllBookings method
        pass

    def getAddon(self, addonName: str) -> str:
        # TODO: Implement getAddon method
        pass

    def getAllAddons(self) -> str:
        # TODO: Implement getAllAddons method
        pass

    def updateOrAddDiscount(self, discount: str):
        # TODO: Implement updateOrAddDiscount method
        pass

    def updateOrAddEmployeeType(self, type: str):
        # TODO: Implement updateOrAddEmployeeType method
        pass

    def updateOrAddAddon(self, addon: str):
        # TODO: Implement updateOrAddAddon method
        pass

    def getCustomer(self, customerSSNumber: str) -> str:
        # TODO: Implement getCustomer method
        pass

    def getBooking(self, bookingID: int) -> str:
        # TODO: Implement getBooking method
        pass

    def getRoom(self, roomNumber: int) -> str:
        # TODO: Implement getRoom method
        pass

    def _getAllRooms(self) -> str:
        # TODO: Implement _getAllRooms method
        pass

    def findCustomers(self, partOfCustomerName: str) -> str:
        # TODO: Implement findCustomers method
        pass

    def getAllCleaners(self) -> str:
        # TODO: Implement getAllCleaners method
        pass

    def getRooms(self, type: str) -> str:
        # TODO: Implement getRooms method
        pass

    def getAllEmployees(self) -> str:
        # TODO: Implement getAllEmployees method
        pass

    def getBookings(self, fromDate: date, toDate: date) -> str:
        # TODO: Implement getBookings method
        pass

    def getCurrentBookings(self) -> str:
        # TODO: Implement getCurrentBookings method
        pass

    def getAllManagers(self) -> str:
        # TODO: Implement getAllManagers method
        pass

    def getPastBookings(self) -> str:
        # TODO: Implement getPastBookings method
        pass

    def getAllReceptionists(self) -> str:
        # TODO: Implement getAllReceptionists method
        pass

    def updateOrAddExtra(self, extra: Extra):
        # TODO: Implement updateOrAddExtra method
        pass

    def updateOrAddCustomer(self, customer: str):
        # TODO: Implement updateOrAddCustomer method
        pass

    def findBookings(self, customerName: str) -> str:
        # TODO: Implement findBookings method
        pass

    def getAllRoomTypes(self) -> str:
        # TODO: Implement getAllRoomTypes method
        pass

    def getEmployee(self, employeeSSNumber: str) -> str:
        # TODO: Implement getEmployee method
        pass

    def updateOrAddBooking(self, booking: str):
        # TODO: Implement updateOrAddBooking method
        pass

    def updateOrAddRoomType(self, type: str):
        # TODO: Implement updateOrAddRoomType method
        pass

    def getAvaliableRoomTypes(self, from: date, to: date) -> str:
        # TODO: Implement getAvaliableRoomTypes method
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

    def __init__(self, name: str, address: str, rank: float, HotelManagementClassDiagram_Hotel29: "HotelManagementClassDiagram_Employee" = None, HotelManagementClassDiagram_Hotel: "HotelManagementClassDiagram_BookingController" = None, HotelManagementClassDiagram_Hotel24: "HotelManagementClassDiagram_MaintenanceController" = None, HotelManagementClassDiagram_Hotel27: "HotelManagementClassDiagram_ManagementController" = None):
        self.name = name
        self.address = address
        self.rank = rank
        self.HotelManagementClassDiagram_Hotel29 = HotelManagementClassDiagram_Hotel29
        self.HotelManagementClassDiagram_Hotel = HotelManagementClassDiagram_Hotel
        self.HotelManagementClassDiagram_Hotel24 = HotelManagementClassDiagram_Hotel24
        self.HotelManagementClassDiagram_Hotel27 = HotelManagementClassDiagram_Hotel27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def rank(self) -> float:
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

    def logIn(self, password: str, SSN: str) -> str:
        # TODO: Implement logIn method
        pass

class HotelManagementClassDiagram_MaintenanceController:

    def __init__(self, HotelManagementClassDiagram_MaintenanceController: set["HotelManagementClassDiagram_Room"] = None, HotelManagementClassDiagram_MaintenanceController25: "HotelManagementClassDiagram_Hotel" = None, HotelManagementClassDiagram_MaintenanceController36: "HotelManagementClassDiagram_Interaction3" = None):
        self.HotelManagementClassDiagram_MaintenanceController = HotelManagementClassDiagram_MaintenanceController if HotelManagementClassDiagram_MaintenanceController is not None else set()
        self.HotelManagementClassDiagram_MaintenanceController25 = HotelManagementClassDiagram_MaintenanceController25
        self.HotelManagementClassDiagram_MaintenanceController36 = HotelManagementClassDiagram_MaintenanceController36
        
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
                    

    def addToQueue(self, room: str):
        # TODO: Implement addToQueue method
        pass

    def getNextRoomToClean(self, room: str):
        # TODO: Implement getNextRoomToClean method
        pass

    def removeFromQueue(self, room: str):
        # TODO: Implement removeFromQueue method
        pass

    def setRepairedStatus(self, repaired: bool, room: str):
        # TODO: Implement setRepairedStatus method
        pass

    def setCleanedStatus(self, room: str, status: bool):
        # TODO: Implement setCleanedStatus method
        pass

    def getNextRoomToClean(self) -> str:
        # TODO: Implement getNextRoomToClean method
        pass

class HotelManagementClassDiagram_ManagementController:

    def __init__(self, HotelManagementClassDiagram_ManagementController: "HotelManagementClassDiagram_Hotel" = None):
        self.HotelManagementClassDiagram_ManagementController = HotelManagementClassDiagram_ManagementController
        
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

    def getAllDiscounts(self) -> str:
        # TODO: Implement getAllDiscounts method
        pass

    def updateOrAddRoomType(self, roomType: str):
        # TODO: Implement updateOrAddRoomType method
        pass

    def updateOrAddAddon(self, addon: str):
        # TODO: Implement updateOrAddAddon method
        pass

    def updateOrAddEmployee(self, employee: str):
        # TODO: Implement updateOrAddEmployee method
        pass

    def getEmployee(self, SSN: str) -> str:
        # TODO: Implement getEmployee method
        pass

    def getAllAddons(self) -> str:
        # TODO: Implement getAllAddons method
        pass

    def updateOrAddEmployeeType(self, employeeType: str):
        # TODO: Implement updateOrAddEmployeeType method
        pass

    def updateOrAddRoom(self, room: str):
        # TODO: Implement updateOrAddRoom method
        pass

    def updateOrAddDiscount(self, discount: str):
        # TODO: Implement updateOrAddDiscount method
        pass

    def updateOrAddExtra(self, extra: Extra):
        # TODO: Implement updateOrAddExtra method
        pass

    def getAllExtras(self) -> Extra:
        # TODO: Implement getAllExtras method
        pass

    def getAllEmployees(self) -> str:
        # TODO: Implement getAllEmployees method
        pass

class HotelManagementClassDiagram_BookingController:

    def __init__(self, HotelManagementClassDiagram_BookingController: "HotelManagementClassDiagram_Hotel" = None):
        self.HotelManagementClassDiagram_BookingController = HotelManagementClassDiagram_BookingController
        
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

    def checkOut(self, booking: str):
        # TODO: Implement checkOut method
        pass

    def updateOrAddCustomer(self, customer: str):
        # TODO: Implement updateOrAddCustomer method
        pass

    def assignRoom(self, room: str):
        # TODO: Implement assignRoom method
        pass

    def getCustomer(self, SSN: str) -> str:
        # TODO: Implement getCustomer method
        pass

    def findCustomer(self, ssNumber: str):
        # TODO: Implement findCustomer method
        pass

    def getAllBookings(self) -> str:
        # TODO: Implement getAllBookings method
        pass

    def sendConfirmation(self, booking: str) -> bool:
        # TODO: Implement sendConfirmation method
        pass

    def searchAvailableRoomTypes(self, fromDate: date, nbrOfChildren: int, nbrOfAdults: int, toDate: date) -> str:
        # TODO: Implement searchAvailableRoomTypes method
        pass

    def getAllCustomers(self) -> str:
        # TODO: Implement getAllCustomers method
        pass

    def updateOrAddBooking(self, booking: str):
        # TODO: Implement updateOrAddBooking method
        pass

    def saveCustomer(self, customer: str):
        # TODO: Implement saveCustomer method
        pass

    def checkIn(self, booking: str):
        # TODO: Implement checkIn method
        pass

    def getBooking(self, bookingId: int) -> str:
        # TODO: Implement getBooking method
        pass

class HotelManagementClassDiagram_Costable(ABC):

    def __init__(self, price: float, HotelManagementClassDiagram_Costable: set["HotelManagementClassDiagram_Discount"] = None, HotelManagementClassDiagram_Costable16: "HotelManagementClassDiagram_Bill" = None):
        self.price = price
        self.HotelManagementClassDiagram_Costable = HotelManagementClassDiagram_Costable if HotelManagementClassDiagram_Costable is not None else set()
        self.HotelManagementClassDiagram_Costable16 = HotelManagementClassDiagram_Costable16
        
    @property
    def price(self) -> float:
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
                    

    def removeDiscount(self, discount: str):
        # TODO: Implement removeDiscount method
        pass

    def addDiscount(self, discount: str):
        # TODO: Implement addDiscount method
        pass

class HotelManagementClassDiagram_Extra:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
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
        
    @property
    def paid(self) -> bool:
        return self.__paid

    @paid.setter
    def paid(self, paid: bool):
        self.__paid = paid

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def totalPrice(self) -> float:
        return self.__totalPrice

    @totalPrice.setter
    def totalPrice(self, totalPrice: float):
        self.__totalPrice = totalPrice

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
                    

    def addCostable(self, costable: Costable):
        # TODO: Implement addCostable method
        pass

class HotelManagementClassDiagram_Discount:

    def __init__(self, isPercentage: str, amount: float, name: str, HotelManagementClassDiagram_Discount: "HotelManagementClassDiagram_Booking" = None, HotelManagementClassDiagram_Discount13: "HotelManagementClassDiagram_Costable" = None):
        self.isPercentage = isPercentage
        self.amount = amount
        self.name = name
        self.HotelManagementClassDiagram_Discount = HotelManagementClassDiagram_Discount
        self.HotelManagementClassDiagram_Discount13 = HotelManagementClassDiagram_Discount13
        
    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def isPercentage(self) -> str:
        return self.__isPercentage

    @isPercentage.setter
    def isPercentage(self, isPercentage: str):
        self.__isPercentage = isPercentage

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
        
    @property
    def internalComment(self) -> str:
        return self.__internalComment

    @internalComment.setter
    def internalComment(self, internalComment: str):
        self.__internalComment = internalComment

    @property
    def underCleaning(self) -> bool:
        return self.__underCleaning

    @underCleaning.setter
    def underCleaning(self, underCleaning: bool):
        self.__underCleaning = underCleaning

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def maxNbrPeople(self) -> int:
        return self.__maxNbrPeople

    @maxNbrPeople.setter
    def maxNbrPeople(self, maxNbrPeople: int):
        self.__maxNbrPeople = maxNbrPeople

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def roomNumber(self) -> int:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber

    @property
    def underRepair(self) -> bool:
        return self.__underRepair

    @underRepair.setter
    def underRepair(self, underRepair: bool):
        self.__underRepair = underRepair

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
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def expirationYear(self) -> int:
        return self.__expirationYear

    @expirationYear.setter
    def expirationYear(self, expirationYear: int):
        self.__expirationYear = expirationYear

    @property
    def cvc(self) -> int:
        return self.__cvc

    @cvc.setter
    def cvc(self, cvc: int):
        self.__cvc = cvc

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def expirationMonth(self) -> int:
        return self.__expirationMonth

    @expirationMonth.setter
    def expirationMonth(self, expirationMonth: int):
        self.__expirationMonth = expirationMonth

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

class HotelManagementClassDiagram_Booking:

    def __init__(self, bookingId: int, startDate: date, endDate: date, created: date, internalComments: str, externalComments: str, checkedIn: bool, checkedOut: bool, roomTypes: str, HotelManagementClassDiagram_Booking: "HotelManagementClassDiagram_Creditcard" = None, HotelManagementClassDiagram_Booking3: set["HotelManagementClassDiagram_Addon"] = None, HotelManagementClassDiagram_Booking5: set["HotelManagementClassDiagram_Room"] = None, HotelManagementClassDiagram_Booking7: "HotelManagementClassDiagram_Customer" = None, HotelManagementClassDiagram_Booking9: set["HotelManagementClassDiagram_Discount"] = None, HotelManagementClassDiagram_Booking11: "HotelManagementClassDiagram_Bill" = None, HotelManagementClassDiagram_Booking40: "HotelManagementClassDiagram_Interaction5" = None):
        self.bookingId = bookingId
        self.startDate = startDate
        self.endDate = endDate
        self.created = created
        self.internalComments = internalComments
        self.externalComments = externalComments
        self.checkedIn = checkedIn
        self.checkedOut = checkedOut
        self.roomTypes = roomTypes
        self.HotelManagementClassDiagram_Booking = HotelManagementClassDiagram_Booking
        self.HotelManagementClassDiagram_Booking3 = HotelManagementClassDiagram_Booking3 if HotelManagementClassDiagram_Booking3 is not None else set()
        self.HotelManagementClassDiagram_Booking5 = HotelManagementClassDiagram_Booking5 if HotelManagementClassDiagram_Booking5 is not None else set()
        self.HotelManagementClassDiagram_Booking7 = HotelManagementClassDiagram_Booking7
        self.HotelManagementClassDiagram_Booking9 = HotelManagementClassDiagram_Booking9 if HotelManagementClassDiagram_Booking9 is not None else set()
        self.HotelManagementClassDiagram_Booking11 = HotelManagementClassDiagram_Booking11
        self.HotelManagementClassDiagram_Booking40 = HotelManagementClassDiagram_Booking40
        
    @property
    def internalComments(self) -> str:
        return self.__internalComments

    @internalComments.setter
    def internalComments(self, internalComments: str):
        self.__internalComments = internalComments

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def checkedOut(self) -> bool:
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: bool):
        self.__checkedOut = checkedOut

    @property
    def roomTypes(self) -> str:
        return self.__roomTypes

    @roomTypes.setter
    def roomTypes(self, roomTypes: str):
        self.__roomTypes = roomTypes

    @property
    def externalComments(self) -> str:
        return self.__externalComments

    @externalComments.setter
    def externalComments(self, externalComments: str):
        self.__externalComments = externalComments

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def checkedIn(self) -> bool:
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn

    @property
    def bookingId(self) -> int:
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId

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

    def removeDiscount(self, discount: str):
        # TODO: Implement removeDiscount method
        pass

    def pay(self, bill: str) -> bool:
        # TODO: Implement pay method
        pass

    def checkOut(self) -> str:
        # TODO: Implement checkOut method
        pass

    def removeAddon(self, addon: str):
        # TODO: Implement removeAddon method
        pass

    def addDiscount(self, discount: str):
        # TODO: Implement addDiscount method
        pass

    def removeRoom(self, room: str):
        # TODO: Implement removeRoom method
        pass

    def checkIn(self):
        # TODO: Implement checkIn method
        pass

    def addAddon(self, addon: str):
        # TODO: Implement addAddon method
        pass

    def generateBill(self) -> str:
        # TODO: Implement generateBill method
        pass

    def addRoom(self, room: str):
        # TODO: Implement addRoom method
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
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SSNumber(self) -> str:
        return self.__SSNumber

    @SSNumber.setter
    def SSNumber(self, SSNumber: str):
        self.__SSNumber = SSNumber

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

class HotelManagementClassDiagram_EmployeeType:

    def __init__(self, type: str, acessLevel: int, HotelManagementClassDiagram_EmployeeType: "HotelManagementClassDiagram_Employee" = None):
        self.type = type
        self.acessLevel = acessLevel
        self.HotelManagementClassDiagram_EmployeeType = HotelManagementClassDiagram_EmployeeType
        
    @property
    def acessLevel(self) -> int:
        return self.__acessLevel

    @acessLevel.setter
    def acessLevel(self, acessLevel: int):
        self.__acessLevel = acessLevel

    @property
    def type(self) -> str:
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
        
    @property
    def miscInfo(self) -> str:
        return self.__miscInfo

    @miscInfo.setter
    def miscInfo(self, miscInfo: str):
        self.__miscInfo = miscInfo

    @property
    def bonusPoints(self) -> int:
        return self.__bonusPoints

    @bonusPoints.setter
    def bonusPoints(self, bonusPoints: int):
        self.__bonusPoints = bonusPoints

    @property
    def customerID(self) -> int:
        return self.__customerID

    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

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

    def addBonusPoints(self, bonusPoints: int):
        # TODO: Implement addBonusPoints method
        pass

class HotelManagementClassDiagram_Employee(Person):

    def __init__(self, employeeID: int, workRate: float, salary: float, password: str, HotelManagementClassDiagram_Employee: "HotelManagementClassDiagram_EmployeeType" = None, HotelManagementClassDiagram_Employee30: "HotelManagementClassDiagram_Hotel" = None, HotelManagementClassDiagram_Employee32: "HotelManagementClassDiagram_Interaction1" = None, HotelManagementClassDiagram_Employee34: "HotelManagementClassDiagram_Interaction2" = None, HotelManagementClassDiagram_Employee38: "HotelManagementClassDiagram_Interaction4" = None):
        self.employeeID = employeeID
        self.workRate = workRate
        self.salary = salary
        self.password = password
        self.HotelManagementClassDiagram_Employee = HotelManagementClassDiagram_Employee
        self.HotelManagementClassDiagram_Employee30 = HotelManagementClassDiagram_Employee30
        self.HotelManagementClassDiagram_Employee32 = HotelManagementClassDiagram_Employee32
        self.HotelManagementClassDiagram_Employee34 = HotelManagementClassDiagram_Employee34
        self.HotelManagementClassDiagram_Employee38 = HotelManagementClassDiagram_Employee38
        
    @property
    def workRate(self) -> float:
        return self.__workRate

    @workRate.setter
    def workRate(self, workRate: float):
        self.__workRate = workRate

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def employeeID(self) -> int:
        return self.__employeeID

    @employeeID.setter
    def employeeID(self, employeeID: int):
        self.__employeeID = employeeID

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

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

    def Booking(self):
        # TODO: Implement Booking method
        pass

    def Boolean(self):
        # TODO: Implement Boolean method
        pass

    def roomTypes(self):
        # TODO: Implement roomTypes method
        pass
