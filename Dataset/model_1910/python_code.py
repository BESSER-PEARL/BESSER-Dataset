from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StaffType(Enum):
    Manager = "Manager"
    Receptionist = "Receptionist"
    Janitor = "Janitor"
    HouseKeeper = "HouseKeeper"


############################################
# Definition of Classes
############################################

class IApplianceAdministration:

    pass
class ClassDiagram_ApplianceAdministration(IApplianceAdministration):

    pass
class IRoomAdministration:

    pass
class ClassDiagram_RoomAdministration(IRoomAdministration):

    pass
class IRoomManager:

    pass
class ClassDiagram_RoomManager(IRoomManager):

    pass
class IStaffAdministration:

    pass
class ClassDiagram_StaffAdministration(IStaffAdministration):

    pass
class IHotelAdministration:

    pass
class ClassDiagram_HotelAdministration(IHotelAdministration):

    pass
class BookingManager:

    pass
class ClassDiagram_StaffBooking(BookingManager):

    pass
class IBooking:

    pass
class ClassDiagram_GuestBooking(IBooking):

    pass
class IBillManager:

    pass
class ClassDiagram_BillManager(IBillManager):

    pass
class IGuestManager:

    pass
class ClassDiagram_GuestManager(IGuestManager):

    pass
class IFacilityManager:

    pass
class ClassDiagram_FacilityManager(IFacilityManager):

    pass
class IServiceBooking:

    pass
class ClassDiagram_ServiceBooking(IServiceBooking):

    pass
class IFacilityAdministration:

    pass
class ClassDiagram_FacilityAdministration(IFacilityAdministration):

    pass
class ClassDiagram_IBooking(ABC):

    def __init__(self):
        
    def cancelBooking(self, booking: str):
        # TODO: Implement cancelBooking method
        pass

    def findBooking(self, bookingNumber: int):
        # TODO: Implement findBooking method
        pass

    def editBooking(self, booking: str):
        # TODO: Implement editBooking method
        pass

    def createBooking(self, end: date, guest: str, rooms: str, start: date):
        # TODO: Implement createBooking method
        pass

    def getBookings(self, guest: str):
        # TODO: Implement getBookings method
        pass

    def findAvailableRooms(self, end: date, roomType: str, start: date):
        # TODO: Implement findAvailableRooms method
        pass

class ClassDiagram_IServiceBooking(ABC):

    def __init__(self):
        
    def bookFacilityService(self, facility: str, service: str, booking: str, guest: str, date: date):
        # TODO: Implement bookFacilityService method
        pass

    def findBookedService(self, bookedServiceID: int):
        # TODO: Implement findBookedService method
        pass

    def getBookedServices(self, booking: str):
        # TODO: Implement getBookedServices method
        pass

    def findAvailableServices(self, facility: str, date: date):
        # TODO: Implement findAvailableServices method
        pass

    def cancelBookedService(self, service: str):
        # TODO: Implement cancelBookedService method
        pass

class ClassDiagram_IHotelAdministration(ABC):

    def __init__(self):
        
    def addHotel(self):
        # TODO: Implement addHotel method
        pass

    def removeHotel(self):
        # TODO: Implement removeHotel method
        pass

    def editHotel(self):
        # TODO: Implement editHotel method
        pass

class ClassDiagram_IStaffAdministration(ABC):

    def __init__(self):
        
    def addStaff(self):
        # TODO: Implement addStaff method
        pass

    def editStaff(self):
        # TODO: Implement editStaff method
        pass

    def removeStaff(self):
        # TODO: Implement removeStaff method
        pass

class ClassDiagram_IRoomAdministration(ABC):

    def __init__(self):
        
    def removeRoom(self, room: str):
        # TODO: Implement removeRoom method
        pass

    def addRoom(self, roomNumber: int, roomType: str):
        # TODO: Implement addRoom method
        pass

    def editRoomType(self, roomType: str):
        # TODO: Implement editRoomType method
        pass

    def editRoom(self, room: str):
        # TODO: Implement editRoom method
        pass

    def removeRoomType(self, roomType: str):
        # TODO: Implement removeRoomType method
        pass

    def createRoomType(self):
        # TODO: Implement createRoomType method
        pass

class ClassDiagram_IFacilityAdministration(ABC):

    def __init__(self):
        
    def addFacility(self, facilityType: str, name: str):
        # TODO: Implement addFacility method
        pass

    def editFacility(self, facility: str):
        # TODO: Implement editFacility method
        pass

    def addFacilityType(self, kind: str):
        # TODO: Implement addFacilityType method
        pass

    def editService(self, service: str):
        # TODO: Implement editService method
        pass

    def editFacilityType(self, facilityType: str):
        # TODO: Implement editFacilityType method
        pass

    def removeFacility(self, facility: str):
        # TODO: Implement removeFacility method
        pass

    def removeFacilityType(self, facilityType: str):
        # TODO: Implement removeFacilityType method
        pass

    def addService(self, price: float, facility: str, name: str):
        # TODO: Implement addService method
        pass

    def removeService(self, service: str):
        # TODO: Implement removeService method
        pass

class ClassDiagram_IApplianceAdministration(ABC):

    def __init__(self):
        
    def addAppliance(self, room: str):
        # TODO: Implement addAppliance method
        pass

    def addApplianceType(self, name: str):
        # TODO: Implement addApplianceType method
        pass

    def removeAppliance(self, appliance: str):
        # TODO: Implement removeAppliance method
        pass

    def editApplianceService(self, service: str):
        # TODO: Implement editApplianceService method
        pass

    def editApplianceType(self, applianceType: str):
        # TODO: Implement editApplianceType method
        pass

    def removeApplianceService(self, service: str):
        # TODO: Implement removeApplianceService method
        pass

    def removeApplianceType(self, applianceType: str):
        # TODO: Implement removeApplianceType method
        pass

    def addApplianceService(self, price: float, name: str):
        # TODO: Implement addApplianceService method
        pass

    def editAppliance(self, appliance: str):
        # TODO: Implement editAppliance method
        pass

class ClassDiagram_IBillManager(ABC):

    def __init__(self):
        
    def findBill(self, booking: str):
        # TODO: Implement findBill method
        pass

    def addPurchesedService(self, item: str, bill: str, amount: float):
        # TODO: Implement addPurchesedService method
        pass

    def pay(self, bill: str, amount: float):
        # TODO: Implement pay method
        pass

    def createReceipt(self, bill: str):
        # TODO: Implement createReceipt method
        pass

    def getAmount(self, bill: str):
        # TODO: Implement getAmount method
        pass

class ClassDiagram_IFacilityManager(ABC):

    def __init__(self):
        
    def findBookedServices(self, guest: str):
        # TODO: Implement findBookedServices method
        pass

    def findBookedService(self, date: date, facilityService: str):
        # TODO: Implement findBookedService method
        pass

class ClassDiagram_IGuestManager(ABC):

    def __init__(self):
        
    def removeGuestRecord(self, guest: str):
        # TODO: Implement removeGuestRecord method
        pass

    def createGuestRecord(self, lastName: str, phoneNumber: str, firstName: str, adress: str, ssn: str):
        # TODO: Implement createGuestRecord method
        pass

    def findGuests(self, firstName: str, lastName: str):
        # TODO: Implement findGuests method
        pass

    def editGuestRecord(self, guest: str):
        # TODO: Implement editGuestRecord method
        pass

    def findGuest(self, ssn: str):
        # TODO: Implement findGuest method
        pass

class ClassDiagram_IRoomManager(ABC):

    def __init__(self):
        
    def maintenanceStatus(self, room: str):
        # TODO: Implement maintenanceStatus method
        pass

    def getRoomsToClean(self):
        # TODO: Implement getRoomsToClean method
        pass

    def getRoomsToMaintain(self):
        # TODO: Implement getRoomsToMaintain method
        pass

    def cleaningStatus(self, room: str):
        # TODO: Implement cleaningStatus method
        pass

    def findRoom(self, roomNumber: int):
        # TODO: Implement findRoom method
        pass

class ClassDiagram_BookingManager(ABC):

    def __init__(self):
        
    def checkIn(self, booking: str):
        # TODO: Implement checkIn method
        pass

    def assignKey(self, booking: str, rooms: str, expirationDate: date):
        # TODO: Implement assignKey method
        pass

    def checkOut(self, booking: str):
        # TODO: Implement checkOut method
        pass

    def findBooking(self, roomNr: int, date: date):
        # TODO: Implement findBooking method
        pass

    def findBooking(self, guestSSN: str, date: date):
        # TODO: Implement findBooking method
        pass

class ClassDiagram_Facility_FacilityService:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

class ClassDiagram_Facility_FacilityType:

    def __init__(self, kind: str, ClassDiagram_Facility_FacilityType: "ClassDiagram_Hotel_Facility" = None):
        self.kind = kind
        self.ClassDiagram_Facility_FacilityType = ClassDiagram_Facility_FacilityType
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ClassDiagram_Facility_FacilityType(self):
        return self.__ClassDiagram_Facility_FacilityType

    @ClassDiagram_Facility_FacilityType.setter
    def ClassDiagram_Facility_FacilityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Facility_FacilityType__ClassDiagram_Facility_FacilityType", None)
        self.__ClassDiagram_Facility_FacilityType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Facility26"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Facility26", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Facility26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Facility26"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Facility26", None)
                setattr(value, "ClassDiagram_Hotel_Facility26", self)

class ClassDiagram_RoomAppliance_ApplianceType:

    def __init__(self, name: str, ClassDiagram_RoomAppliance_ApplianceType: "ClassDiagram_Room_RoomAppliance" = None):
        self.name = name
        self.ClassDiagram_RoomAppliance_ApplianceType = ClassDiagram_RoomAppliance_ApplianceType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_RoomAppliance_ApplianceType(self):
        return self.__ClassDiagram_RoomAppliance_ApplianceType

    @ClassDiagram_RoomAppliance_ApplianceType.setter
    def ClassDiagram_RoomAppliance_ApplianceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_RoomAppliance_ApplianceType__ClassDiagram_RoomAppliance_ApplianceType", None)
        self.__ClassDiagram_RoomAppliance_ApplianceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Room_RoomAppliance21"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomAppliance21", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Room_RoomAppliance21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomAppliance21"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomAppliance21", None)
                setattr(value, "ClassDiagram_Room_RoomAppliance21", self)

class ClassDiagram_Room_RoomKey:

    def __init__(self, expirationDate: date, ClassDiagram_Room_RoomKey: "ClassDiagram_Hotel_Room" = None):
        self.expirationDate = expirationDate
        self.ClassDiagram_Room_RoomKey = ClassDiagram_Room_RoomKey
        
    @property
    def expirationDate(self) -> date:
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: date):
        self.__expirationDate = expirationDate

    @property
    def ClassDiagram_Room_RoomKey(self):
        return self.__ClassDiagram_Room_RoomKey

    @ClassDiagram_Room_RoomKey.setter
    def ClassDiagram_Room_RoomKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomKey__ClassDiagram_Room_RoomKey", None)
        self.__ClassDiagram_Room_RoomKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Room19"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Room19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Room19"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Room19", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Room19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Room_RoomType:

    def __init__(self, price: float, maxNumberOfGuests: int, area: float, ClassDiagram_Room_RoomType: "ClassDiagram_Hotel_Room" = None, ClassDiagram_Room_RoomType23: set["ClassDiagram_Room_RoomAppliance"] = None):
        self.price = price
        self.maxNumberOfGuests = maxNumberOfGuests
        self.area = area
        self.ClassDiagram_Room_RoomType = ClassDiagram_Room_RoomType
        self.ClassDiagram_Room_RoomType23 = ClassDiagram_Room_RoomType23 if ClassDiagram_Room_RoomType23 is not None else set()
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def maxNumberOfGuests(self) -> int:
        return self.__maxNumberOfGuests

    @maxNumberOfGuests.setter
    def maxNumberOfGuests(self, maxNumberOfGuests: int):
        self.__maxNumberOfGuests = maxNumberOfGuests

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

    @property
    def ClassDiagram_Room_RoomType(self):
        return self.__ClassDiagram_Room_RoomType

    @ClassDiagram_Room_RoomType.setter
    def ClassDiagram_Room_RoomType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomType__ClassDiagram_Room_RoomType", None)
        self.__ClassDiagram_Room_RoomType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Room17"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Room17", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Room17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Room17"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Room17", None)
                setattr(value, "ClassDiagram_Hotel_Room17", self)

    @property
    def ClassDiagram_Room_RoomType23(self):
        return self.__ClassDiagram_Room_RoomType23

    @ClassDiagram_Room_RoomType23.setter
    def ClassDiagram_Room_RoomType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomType__ClassDiagram_Room_RoomType23", None)
        self.__ClassDiagram_Room_RoomType23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Room_RoomAppliance24"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomAppliance24", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Room_RoomAppliance24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Room_RoomAppliance24"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomAppliance24", None)
                    
                    setattr(item, "ClassDiagram_Room_RoomAppliance24", self)
                    

class ClassDiagram_Room_RoomAppliance:

    def __init__(self, name: str, ClassDiagram_Room_RoomAppliance: "ClassDiagram_Hotel_Room" = None, ClassDiagram_Room_RoomAppliance21: "ClassDiagram_RoomAppliance_ApplianceType" = None, ClassDiagram_Room_RoomAppliance24: "ClassDiagram_Room_RoomType" = None):
        self.name = name
        self.ClassDiagram_Room_RoomAppliance = ClassDiagram_Room_RoomAppliance
        self.ClassDiagram_Room_RoomAppliance21 = ClassDiagram_Room_RoomAppliance21
        self.ClassDiagram_Room_RoomAppliance24 = ClassDiagram_Room_RoomAppliance24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Room_RoomAppliance24(self):
        return self.__ClassDiagram_Room_RoomAppliance24

    @ClassDiagram_Room_RoomAppliance24.setter
    def ClassDiagram_Room_RoomAppliance24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomAppliance__ClassDiagram_Room_RoomAppliance24", None)
        self.__ClassDiagram_Room_RoomAppliance24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Room_RoomType23"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomType23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomType23"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomType23", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Room_RoomType23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Room_RoomAppliance(self):
        return self.__ClassDiagram_Room_RoomAppliance

    @ClassDiagram_Room_RoomAppliance.setter
    def ClassDiagram_Room_RoomAppliance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomAppliance__ClassDiagram_Room_RoomAppliance", None)
        self.__ClassDiagram_Room_RoomAppliance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Room15"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Room15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Room15"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Room15", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Room15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Room_RoomAppliance21(self):
        return self.__ClassDiagram_Room_RoomAppliance21

    @ClassDiagram_Room_RoomAppliance21.setter
    def ClassDiagram_Room_RoomAppliance21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomAppliance__ClassDiagram_Room_RoomAppliance21", None)
        self.__ClassDiagram_Room_RoomAppliance21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType"):
                opp_val = getattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_RoomAppliance_ApplianceType"):
                opp_val = getattr(value, "ClassDiagram_RoomAppliance_ApplianceType", None)
                setattr(value, "ClassDiagram_RoomAppliance_ApplianceType", self)

class ClassDiagram_ApplianceType_ApplianceService:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

class ClassDiagram_Booking_Bill:

    def __init__(self, paidAmount: float, ClassDiagram_Booking_Bill: set["ClassDiagram_Booking_PurchasedService"] = None):
        self.paidAmount = paidAmount
        self.ClassDiagram_Booking_Bill = ClassDiagram_Booking_Bill if ClassDiagram_Booking_Bill is not None else set()
        
    @property
    def paidAmount(self) -> float:
        return self.__paidAmount

    @paidAmount.setter
    def paidAmount(self, paidAmount: float):
        self.__paidAmount = paidAmount

    @property
    def ClassDiagram_Booking_Bill(self):
        return self.__ClassDiagram_Booking_Bill

    @ClassDiagram_Booking_Bill.setter
    def ClassDiagram_Booking_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_Bill__ClassDiagram_Booking_Bill", None)
        self.__ClassDiagram_Booking_Bill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Booking_PurchasedService"):
                    opp_val = getattr(item, "ClassDiagram_Booking_PurchasedService", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Booking_PurchasedService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Booking_PurchasedService"):
                    opp_val = getattr(item, "ClassDiagram_Booking_PurchasedService", None)
                    
                    setattr(item, "ClassDiagram_Booking_PurchasedService", self)
                    

class ClassDiagram_Booking_BookedService:

    def __init__(self, date: date, price: float, ClassDiagram_Booking_BookedService: "ClassDiagram_Hotel_Booking" = None):
        self.date = date
        self.price = price
        self.ClassDiagram_Booking_BookedService = ClassDiagram_Booking_BookedService
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def ClassDiagram_Booking_BookedService(self):
        return self.__ClassDiagram_Booking_BookedService

    @ClassDiagram_Booking_BookedService.setter
    def ClassDiagram_Booking_BookedService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_BookedService__ClassDiagram_Booking_BookedService", None)
        self.__ClassDiagram_Booking_BookedService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Booking12"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Booking12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Booking12"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Booking12", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Booking12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Booking_PurchasedService:

    def __init__(self, name: str, price: float, ClassDiagram_Booking_PurchasedService: "ClassDiagram_Booking_Bill" = None):
        self.name = name
        self.price = price
        self.ClassDiagram_Booking_PurchasedService = ClassDiagram_Booking_PurchasedService
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Booking_PurchasedService(self):
        return self.__ClassDiagram_Booking_PurchasedService

    @ClassDiagram_Booking_PurchasedService.setter
    def ClassDiagram_Booking_PurchasedService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_PurchasedService__ClassDiagram_Booking_PurchasedService", None)
        self.__ClassDiagram_Booking_PurchasedService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Booking_Bill"):
                opp_val = getattr(old_value, "ClassDiagram_Booking_Bill", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Booking_Bill"):
                opp_val = getattr(value, "ClassDiagram_Booking_Bill", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Booking_Bill", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Hotel_Room:

    def __init__(self, roomNumber: int, cleaningStatus: bool, maintenceStatus: bool, ClassDiagram_Hotel_Room: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Room15: set["ClassDiagram_Room_RoomAppliance"] = None, ClassDiagram_Hotel_Room17: "ClassDiagram_Room_RoomType" = None, ClassDiagram_Hotel_Room19: set["ClassDiagram_Room_RoomKey"] = None):
        self.roomNumber = roomNumber
        self.cleaningStatus = cleaningStatus
        self.maintenceStatus = maintenceStatus
        self.ClassDiagram_Hotel_Room = ClassDiagram_Hotel_Room
        self.ClassDiagram_Hotel_Room15 = ClassDiagram_Hotel_Room15 if ClassDiagram_Hotel_Room15 is not None else set()
        self.ClassDiagram_Hotel_Room17 = ClassDiagram_Hotel_Room17
        self.ClassDiagram_Hotel_Room19 = ClassDiagram_Hotel_Room19 if ClassDiagram_Hotel_Room19 is not None else set()
        
    @property
    def maintenceStatus(self) -> bool:
        return self.__maintenceStatus

    @maintenceStatus.setter
    def maintenceStatus(self, maintenceStatus: bool):
        self.__maintenceStatus = maintenceStatus

    @property
    def cleaningStatus(self) -> bool:
        return self.__cleaningStatus

    @cleaningStatus.setter
    def cleaningStatus(self, cleaningStatus: bool):
        self.__cleaningStatus = cleaningStatus

    @property
    def roomNumber(self) -> int:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber

    @property
    def ClassDiagram_Hotel_Room15(self):
        return self.__ClassDiagram_Hotel_Room15

    @ClassDiagram_Hotel_Room15.setter
    def ClassDiagram_Hotel_Room15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room15", None)
        self.__ClassDiagram_Hotel_Room15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Room_RoomAppliance"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomAppliance", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Room_RoomAppliance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Room_RoomAppliance"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomAppliance", None)
                    
                    setattr(item, "ClassDiagram_Room_RoomAppliance", self)
                    

    @property
    def ClassDiagram_Hotel_Room19(self):
        return self.__ClassDiagram_Hotel_Room19

    @ClassDiagram_Hotel_Room19.setter
    def ClassDiagram_Hotel_Room19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room19", None)
        self.__ClassDiagram_Hotel_Room19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Room_RoomKey"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Room_RoomKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Room_RoomKey"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomKey", None)
                    
                    setattr(item, "ClassDiagram_Room_RoomKey", self)
                    

    @property
    def ClassDiagram_Hotel_Room17(self):
        return self.__ClassDiagram_Hotel_Room17

    @ClassDiagram_Hotel_Room17.setter
    def ClassDiagram_Hotel_Room17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room17", None)
        self.__ClassDiagram_Hotel_Room17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Room_RoomType"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomType", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Room_RoomType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomType"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomType", None)
                setattr(value, "ClassDiagram_Room_RoomType", self)

    @property
    def ClassDiagram_Hotel_Room(self):
        return self.__ClassDiagram_Hotel_Room

    @ClassDiagram_Hotel_Room.setter
    def ClassDiagram_Hotel_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room", None)
        self.__ClassDiagram_Hotel_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel6"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel6"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel6", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company_Hotel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Hotel_Booking:

    def __init__(self, startDate: date, endDate: date, price: float, checkedIn: bool, bookingID: int, ClassDiagram_Hotel_Booking: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Booking12: set["ClassDiagram_Booking_BookedService"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.checkedIn = checkedIn
        self.bookingID = bookingID
        self.ClassDiagram_Hotel_Booking = ClassDiagram_Hotel_Booking
        self.ClassDiagram_Hotel_Booking12 = ClassDiagram_Hotel_Booking12 if ClassDiagram_Hotel_Booking12 is not None else set()
        
    @property
    def checkedIn(self) -> bool:
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def bookingID(self) -> int:
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: int):
        self.__bookingID = bookingID

    @property
    def ClassDiagram_Hotel_Booking(self):
        return self.__ClassDiagram_Hotel_Booking

    @ClassDiagram_Hotel_Booking.setter
    def ClassDiagram_Hotel_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking", None)
        self.__ClassDiagram_Hotel_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel4"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel4"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel4", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company_Hotel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Hotel_Booking12(self):
        return self.__ClassDiagram_Hotel_Booking12

    @ClassDiagram_Hotel_Booking12.setter
    def ClassDiagram_Hotel_Booking12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking12", None)
        self.__ClassDiagram_Hotel_Booking12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Booking_BookedService"):
                    opp_val = getattr(item, "ClassDiagram_Booking_BookedService", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Booking_BookedService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Booking_BookedService"):
                    opp_val = getattr(item, "ClassDiagram_Booking_BookedService", None)
                    
                    setattr(item, "ClassDiagram_Booking_BookedService", self)
                    

class ClassDiagram_Company_GuestRecord:

    def __init__(self, name: str, adress: str, phoneNumber: str, ssn: str, payment: str, ClassDiagram_Company_GuestRecord: "ClassDiagram_Company" = None):
        self.name = name
        self.adress = adress
        self.phoneNumber = phoneNumber
        self.ssn = ssn
        self.payment = payment
        self.ClassDiagram_Company_GuestRecord = ClassDiagram_Company_GuestRecord
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ssn(self) -> str:
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn

    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress

    @property
    def payment(self) -> str:
        return self.__payment

    @payment.setter
    def payment(self, payment: str):
        self.__payment = payment

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def ClassDiagram_Company_GuestRecord(self):
        return self.__ClassDiagram_Company_GuestRecord

    @ClassDiagram_Company_GuestRecord.setter
    def ClassDiagram_Company_GuestRecord(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_GuestRecord__ClassDiagram_Company_GuestRecord", None)
        self.__ClassDiagram_Company_GuestRecord = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company2"):
                opp_val = getattr(old_value, "ClassDiagram_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company2"):
                opp_val = getattr(value, "ClassDiagram_Company2", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Company_Hotel:

    def __init__(self, name: str, ClassDiagram_Company_Hotel6: set["ClassDiagram_Hotel_Room"] = None, ClassDiagram_Company_Hotel8: set["ClassDiagram_Hotel_Facility"] = None, ClassDiagram_Company_Hotel10: set["ClassDiagram_Hotel_Staff"] = None, ClassDiagram_Company_Hotel: "ClassDiagram_Company" = None, ClassDiagram_Company_Hotel4: set["ClassDiagram_Hotel_Booking"] = None):
        self.name = name
        self.ClassDiagram_Company_Hotel6 = ClassDiagram_Company_Hotel6 if ClassDiagram_Company_Hotel6 is not None else set()
        self.ClassDiagram_Company_Hotel8 = ClassDiagram_Company_Hotel8 if ClassDiagram_Company_Hotel8 is not None else set()
        self.ClassDiagram_Company_Hotel10 = ClassDiagram_Company_Hotel10 if ClassDiagram_Company_Hotel10 is not None else set()
        self.ClassDiagram_Company_Hotel = ClassDiagram_Company_Hotel
        self.ClassDiagram_Company_Hotel4 = ClassDiagram_Company_Hotel4 if ClassDiagram_Company_Hotel4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Company_Hotel10(self):
        return self.__ClassDiagram_Company_Hotel10

    @ClassDiagram_Company_Hotel10.setter
    def ClassDiagram_Company_Hotel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel10", None)
        self.__ClassDiagram_Company_Hotel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Hotel_Staff"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Staff", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Hotel_Staff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Hotel_Staff"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Staff", None)
                    
                    setattr(item, "ClassDiagram_Hotel_Staff", self)
                    

    @property
    def ClassDiagram_Company_Hotel6(self):
        return self.__ClassDiagram_Company_Hotel6

    @ClassDiagram_Company_Hotel6.setter
    def ClassDiagram_Company_Hotel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel6", None)
        self.__ClassDiagram_Company_Hotel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Hotel_Room"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Hotel_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Hotel_Room"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Room", None)
                    
                    setattr(item, "ClassDiagram_Hotel_Room", self)
                    

    @property
    def ClassDiagram_Company_Hotel8(self):
        return self.__ClassDiagram_Company_Hotel8

    @ClassDiagram_Company_Hotel8.setter
    def ClassDiagram_Company_Hotel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel8", None)
        self.__ClassDiagram_Company_Hotel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Hotel_Facility"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Facility", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Hotel_Facility", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Hotel_Facility"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Facility", None)
                    
                    setattr(item, "ClassDiagram_Hotel_Facility", self)
                    

    @property
    def ClassDiagram_Company_Hotel4(self):
        return self.__ClassDiagram_Company_Hotel4

    @ClassDiagram_Company_Hotel4.setter
    def ClassDiagram_Company_Hotel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel4", None)
        self.__ClassDiagram_Company_Hotel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Hotel_Booking"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Booking", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Hotel_Booking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Hotel_Booking"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Booking", None)
                    
                    setattr(item, "ClassDiagram_Hotel_Booking", self)
                    

    @property
    def ClassDiagram_Company_Hotel(self):
        return self.__ClassDiagram_Company_Hotel

    @ClassDiagram_Company_Hotel.setter
    def ClassDiagram_Company_Hotel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel", None)
        self.__ClassDiagram_Company_Hotel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company"):
                opp_val = getattr(old_value, "ClassDiagram_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company"):
                opp_val = getattr(value, "ClassDiagram_Company", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Company:

    def __init__(self, name: str, ClassDiagram_Company: set["ClassDiagram_Company_Hotel"] = None, ClassDiagram_Company2: set["ClassDiagram_Company_GuestRecord"] = None):
        self.name = name
        self.ClassDiagram_Company = ClassDiagram_Company if ClassDiagram_Company is not None else set()
        self.ClassDiagram_Company2 = ClassDiagram_Company2 if ClassDiagram_Company2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Company(self):
        return self.__ClassDiagram_Company

    @ClassDiagram_Company.setter
    def ClassDiagram_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company__ClassDiagram_Company", None)
        self.__ClassDiagram_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Company_Hotel"):
                    opp_val = getattr(item, "ClassDiagram_Company_Hotel", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Company_Hotel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Company_Hotel"):
                    opp_val = getattr(item, "ClassDiagram_Company_Hotel", None)
                    
                    setattr(item, "ClassDiagram_Company_Hotel", self)
                    

    @property
    def ClassDiagram_Company2(self):
        return self.__ClassDiagram_Company2

    @ClassDiagram_Company2.setter
    def ClassDiagram_Company2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company__ClassDiagram_Company2", None)
        self.__ClassDiagram_Company2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Company_GuestRecord"):
                    opp_val = getattr(item, "ClassDiagram_Company_GuestRecord", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Company_GuestRecord", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Company_GuestRecord"):
                    opp_val = getattr(item, "ClassDiagram_Company_GuestRecord", None)
                    
                    setattr(item, "ClassDiagram_Company_GuestRecord", self)
                    

class ClassDiagram_Hotel_Staff:

    def __init__(self, ssn: str, firstName: str, lastName: str, stafftype: str, ClassDiagram_Hotel_Staff: "ClassDiagram_Company_Hotel" = None):
        self.ssn = ssn
        self.firstName = firstName
        self.lastName = lastName
        self.stafftype = stafftype
        self.ClassDiagram_Hotel_Staff = ClassDiagram_Hotel_Staff
        
    @property
    def stafftype(self) -> str:
        return self.__stafftype

    @stafftype.setter
    def stafftype(self, stafftype: str):
        self.__stafftype = stafftype

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def ssn(self) -> str:
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def ClassDiagram_Hotel_Staff(self):
        return self.__ClassDiagram_Hotel_Staff

    @ClassDiagram_Hotel_Staff.setter
    def ClassDiagram_Hotel_Staff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Staff__ClassDiagram_Hotel_Staff", None)
        self.__ClassDiagram_Hotel_Staff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel10"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel10"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel10", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company_Hotel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Hotel_Facility:

    def __init__(self, name: str, ClassDiagram_Hotel_Facility: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Facility26: "ClassDiagram_Facility_FacilityType" = None):
        self.name = name
        self.ClassDiagram_Hotel_Facility = ClassDiagram_Hotel_Facility
        self.ClassDiagram_Hotel_Facility26 = ClassDiagram_Hotel_Facility26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassDiagram_Hotel_Facility26(self):
        return self.__ClassDiagram_Hotel_Facility26

    @ClassDiagram_Hotel_Facility26.setter
    def ClassDiagram_Hotel_Facility26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Facility__ClassDiagram_Hotel_Facility26", None)
        self.__ClassDiagram_Hotel_Facility26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Facility_FacilityType"):
                opp_val = getattr(old_value, "ClassDiagram_Facility_FacilityType", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Facility_FacilityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Facility_FacilityType"):
                opp_val = getattr(value, "ClassDiagram_Facility_FacilityType", None)
                setattr(value, "ClassDiagram_Facility_FacilityType", self)

    @property
    def ClassDiagram_Hotel_Facility(self):
        return self.__ClassDiagram_Hotel_Facility

    @ClassDiagram_Hotel_Facility.setter
    def ClassDiagram_Hotel_Facility(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Facility__ClassDiagram_Hotel_Facility", None)
        self.__ClassDiagram_Hotel_Facility = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel8"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel8"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel8", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Company_Hotel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
