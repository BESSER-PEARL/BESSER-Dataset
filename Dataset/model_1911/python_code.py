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
class ClassDiagram_IHotelAdministration(ABC):

    def __init__(self):
        
        pass
    def addHotel(self):
        # TODO: Implement addHotel method
        pass

    def editHotel(self):
        # TODO: Implement editHotel method
        pass

    def removeHotel(self):
        # TODO: Implement removeHotel method
        pass

class ClassDiagram_IStaffAdministration(ABC):

    def __init__(self):
        
        pass
    def addStaff(self):
        # TODO: Implement addStaff method
        pass

    def editStaff(self):
        # TODO: Implement editStaff method
        pass

    def removeStaff(self):
        # TODO: Implement removeStaff method
        pass

class BookingManager:

    pass
class ClassDiagram_StaffBooking(BookingManager):

    pass
class IBooking:

    pass
class ClassDiagram_GuestBooking(IBooking):

    pass
class ClassDiagram_IServiceBooking(ABC):

    def __init__(self):
        
        pass
    def findBookedService(self, ClassDiagram_bookedServiceID):
        # TODO: Implement findBookedService method
        pass

    def bookFacilityService(self, ClassDiagram_service, ClassDiagram_date, ClassDiagram_guest, ClassDiagram_booking, ClassDiagram_facility):
        # TODO: Implement bookFacilityService method
        pass

    def cancelBookedService(self, ClassDiagram_service):
        # TODO: Implement cancelBookedService method
        pass

    def getBookedServices(self, ClassDiagram_booking):
        # TODO: Implement getBookedServices method
        pass

    def findAvailableServices(self, ClassDiagram_facility, ClassDiagram_date):
        # TODO: Implement findAvailableServices method
        pass

class ClassDiagram_IBooking(ABC):

    def __init__(self):
        
        pass
    def getBookings(self, ClassDiagram_guest):
        # TODO: Implement getBookings method
        pass

    def editBooking(self, ClassDiagram_booking):
        # TODO: Implement editBooking method
        pass

    def cancelBooking(self, ClassDiagram_booking):
        # TODO: Implement cancelBooking method
        pass

    def findBooking(self, ClassDiagram_bookingNumber):
        # TODO: Implement findBooking method
        pass

    def createBooking(self, ClassDiagram_start, ClassDiagram_rooms, ClassDiagram_guest, ClassDiagram_end):
        # TODO: Implement createBooking method
        pass

    def findAvailableRooms(self, ClassDiagram_end, ClassDiagram_roomType, ClassDiagram_start):
        # TODO: Implement findAvailableRooms method
        pass

class ClassDiagram_IFacilityAdministration(ABC):

    def __init__(self):
        
        pass
    def addFacility(self, ClassDiagram_name, ClassDiagram_facilityType):
        # TODO: Implement addFacility method
        pass

    def addService(self, ClassDiagram_name, ClassDiagram_facility, ClassDiagram_price):
        # TODO: Implement addService method
        pass

    def editFacility(self, ClassDiagram_facility):
        # TODO: Implement editFacility method
        pass

    def removeFacility(self, ClassDiagram_facility):
        # TODO: Implement removeFacility method
        pass

    def addFacilityType(self, ClassDiagram_kind):
        # TODO: Implement addFacilityType method
        pass

    def removeService(self, ClassDiagram_service):
        # TODO: Implement removeService method
        pass

    def editFacilityType(self, ClassDiagram_facilityType):
        # TODO: Implement editFacilityType method
        pass

    def editService(self, ClassDiagram_service):
        # TODO: Implement editService method
        pass

    def removeFacilityType(self, ClassDiagram_facilityType):
        # TODO: Implement removeFacilityType method
        pass

class ClassDiagram_IRoomAdministration(ABC):

    def __init__(self):
        
        pass
    def createRoomType(self):
        # TODO: Implement createRoomType method
        pass

    def editRoomType(self, ClassDiagram_roomType):
        # TODO: Implement editRoomType method
        pass

    def addRoom(self, ClassDiagram_roomNumber, ClassDiagram_roomType):
        # TODO: Implement addRoom method
        pass

    def editRoom(self, ClassDiagram_room):
        # TODO: Implement editRoom method
        pass

    def removeRoomType(self, ClassDiagram_roomType):
        # TODO: Implement removeRoomType method
        pass

    def removeRoom(self, ClassDiagram_room):
        # TODO: Implement removeRoom method
        pass

class ClassDiagram_IApplianceAdministration(ABC):

    def __init__(self):
        
        pass
    def removeAppliance(self, ClassDiagram_appliance):
        # TODO: Implement removeAppliance method
        pass

    def editApplianceType(self, ClassDiagram_applianceType):
        # TODO: Implement editApplianceType method
        pass

    def addApplianceService(self, ClassDiagram_price, ClassDiagram_name):
        # TODO: Implement addApplianceService method
        pass

    def editAppliance(self, ClassDiagram_appliance):
        # TODO: Implement editAppliance method
        pass

    def addAppliance(self, ClassDiagram_room):
        # TODO: Implement addAppliance method
        pass

    def removeApplianceType(self, ClassDiagram_applianceType):
        # TODO: Implement removeApplianceType method
        pass

    def removeApplianceService(self, ClassDiagram_service):
        # TODO: Implement removeApplianceService method
        pass

    def editApplianceService(self, ClassDiagram_service):
        # TODO: Implement editApplianceService method
        pass

    def addApplianceType(self, ClassDiagram_name):
        # TODO: Implement addApplianceType method
        pass

class ClassDiagram_IFacilityManager(ABC):

    def __init__(self):
        
        pass
    def findBookedService(self, ClassDiagram_facilityService, ClassDiagram_date):
        # TODO: Implement findBookedService method
        pass

    def findBookedServices(self, ClassDiagram_guest):
        # TODO: Implement findBookedServices method
        pass

class ClassDiagram_IBillManager(ABC):

    def __init__(self):
        
        pass
    def getAmount(self, ClassDiagram_bill):
        # TODO: Implement getAmount method
        pass

    def pay(self, ClassDiagram_bill, ClassDiagram_amount):
        # TODO: Implement pay method
        pass

    def findBill(self, ClassDiagram_booking):
        # TODO: Implement findBill method
        pass

    def createReceipt(self, ClassDiagram_bill):
        # TODO: Implement createReceipt method
        pass

    def addPurchesedService(self, ClassDiagram_amount, ClassDiagram_item, ClassDiagram_bill):
        # TODO: Implement addPurchesedService method
        pass

class ClassDiagram_IGuestManager(ABC):

    def __init__(self):
        
        pass
    def editGuestRecord(self, ClassDiagram_guest):
        # TODO: Implement editGuestRecord method
        pass

    def createGuestRecord(self, ClassDiagram_phoneNumber, ClassDiagram_ssn, ClassDiagram_adress, ClassDiagram_lastName, ClassDiagram_firstName):
        # TODO: Implement createGuestRecord method
        pass

    def removeGuestRecord(self, ClassDiagram_guest):
        # TODO: Implement removeGuestRecord method
        pass

    def findGuests(self, ClassDiagram_firstName, ClassDiagram_lastName):
        # TODO: Implement findGuests method
        pass

    def findGuest(self, ClassDiagram_ssn):
        # TODO: Implement findGuest method
        pass

class ClassDiagram_BookingManager(ABC):

    def __init__(self):
        
        pass
    def checkIn(self, ClassDiagram_booking):
        # TODO: Implement checkIn method
        pass

    def assignKey(self, ClassDiagram_expirationDate, ClassDiagram_rooms, ClassDiagram_booking):
        # TODO: Implement assignKey method
        pass

    def findBooking(self, ClassDiagram_date, ClassDiagram_roomNr):
        # TODO: Implement findBooking method
        pass

    def checkOut(self, ClassDiagram_booking):
        # TODO: Implement checkOut method
        pass

class ClassDiagram_IRoomManager(ABC):

    def __init__(self):
        
        pass
    def maintenanceStatus(self, ClassDiagram_room):
        # TODO: Implement maintenanceStatus method
        pass

    def getRoomsToClean(self):
        # TODO: Implement getRoomsToClean method
        pass

    def findRoom(self, ClassDiagram_roomNumber):
        # TODO: Implement findRoom method
        pass

    def cleaningStatus(self, ClassDiagram_room):
        # TODO: Implement cleaningStatus method
        pass

    def getRoomsToMaintain(self):
        # TODO: Implement getRoomsToMaintain method
        pass

class ClassDiagram_Room_RoomAppliance:

    def __init__(self, name: str, ClassDiagram_Room_RoomAppliance: "ClassDiagram_Hotel_Room" = None, ClassDiagram_Room_RoomAppliance21: "ClassDiagram_RoomAppliance_ApplianceType" = None, ClassDiagram_Room_RoomAppliance24: "ClassDiagram_Room_RoomType" = None):
        self.name = name
        self.ClassDiagram_Room_RoomAppliance = ClassDiagram_Room_RoomAppliance
        self.ClassDiagram_Room_RoomAppliance21 = ClassDiagram_Room_RoomAppliance21
        self.ClassDiagram_Room_RoomAppliance24 = ClassDiagram_Room_RoomAppliance24
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class ClassDiagram_Booking_PurchasedService:

    def __init__(self, name: str, price: float, ClassDiagram_Booking_PurchasedService: "ClassDiagram_Booking_Bill" = None):
        self.name = name
        self.price = price
        self.ClassDiagram_Booking_PurchasedService = ClassDiagram_Booking_PurchasedService
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


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

class ClassDiagram_Facility_FacilityService:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ClassDiagram_Facility_FacilityType:

    def __init__(self, kind: str, ClassDiagram_Facility_FacilityType: "ClassDiagram_Hotel_Facility" = None):
        self.kind = kind
        self.ClassDiagram_Facility_FacilityType = ClassDiagram_Facility_FacilityType
        
        pass
    @property
    def kind(self):
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

class ClassDiagram_ApplianceType_ApplianceService:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ClassDiagram_RoomAppliance_ApplianceType:

    def __init__(self, name: str, ClassDiagram_RoomAppliance_ApplianceType: "ClassDiagram_Room_RoomAppliance" = None):
        self.name = name
        self.ClassDiagram_RoomAppliance_ApplianceType = ClassDiagram_RoomAppliance_ApplianceType
        
        pass
    @property
    def name(self):
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
        
        pass
    @property
    def expirationDate(self):
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
        
        pass
    @property
    def maxNumberOfGuests(self):
        return self.__maxNumberOfGuests

    @maxNumberOfGuests.setter
    def maxNumberOfGuests(self, maxNumberOfGuests: int):
        self.__maxNumberOfGuests = maxNumberOfGuests


    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


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
                    

class ClassDiagram_Booking_Bill:

    def __init__(self, paidAmount: float, ClassDiagram_Booking_Bill: set["ClassDiagram_Booking_PurchasedService"] = None):
        self.paidAmount = paidAmount
        self.ClassDiagram_Booking_Bill = ClassDiagram_Booking_Bill if ClassDiagram_Booking_Bill is not None else set()
        
        pass
    @property
    def paidAmount(self):
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
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def price(self):
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

class ClassDiagram_Hotel_Staff:

    def __init__(self, ssn: str, firstName: str, lastName: str, stafftype: str, ClassDiagram_Hotel_Staff: "ClassDiagram_Company_Hotel" = None):
        self.ssn = ssn
        self.firstName = firstName
        self.lastName = lastName
        self.stafftype = stafftype
        self.ClassDiagram_Hotel_Staff = ClassDiagram_Hotel_Staff
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn


    @property
    def stafftype(self):
        return self.__stafftype

    @stafftype.setter
    def stafftype(self, stafftype: str):
        self.__stafftype = stafftype


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
        
        pass
    @property
    def name(self):
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

class ClassDiagram_Hotel_Room:

    def __init__(self, cleaningStatus: bool, maintenceStatus: bool, roomNumber: int, ClassDiagram_Hotel_Room: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Room15: set["ClassDiagram_Room_RoomAppliance"] = None, ClassDiagram_Hotel_Room17: "ClassDiagram_Room_RoomType" = None, ClassDiagram_Hotel_Room19: set["ClassDiagram_Room_RoomKey"] = None):
        self.cleaningStatus = cleaningStatus
        self.maintenceStatus = maintenceStatus
        self.roomNumber = roomNumber
        self.ClassDiagram_Hotel_Room = ClassDiagram_Hotel_Room
        self.ClassDiagram_Hotel_Room15 = ClassDiagram_Hotel_Room15 if ClassDiagram_Hotel_Room15 is not None else set()
        self.ClassDiagram_Hotel_Room17 = ClassDiagram_Hotel_Room17
        self.ClassDiagram_Hotel_Room19 = ClassDiagram_Hotel_Room19 if ClassDiagram_Hotel_Room19 is not None else set()
        
        pass
    @property
    def maintenceStatus(self):
        return self.__maintenceStatus

    @maintenceStatus.setter
    def maintenceStatus(self, maintenceStatus: bool):
        self.__maintenceStatus = maintenceStatus


    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber


    @property
    def cleaningStatus(self):
        return self.__cleaningStatus

    @cleaningStatus.setter
    def cleaningStatus(self, cleaningStatus: bool):
        self.__cleaningStatus = cleaningStatus


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
                    

class ClassDiagram_Hotel_Booking:

    def __init__(self, startDate: date, endDate: date, price: float, checkedIn: bool, bookingID: int, ClassDiagram_Hotel_Booking: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Booking12: set["ClassDiagram_Booking_BookedService"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.checkedIn = checkedIn
        self.bookingID = bookingID
        self.ClassDiagram_Hotel_Booking = ClassDiagram_Hotel_Booking
        self.ClassDiagram_Hotel_Booking12 = ClassDiagram_Hotel_Booking12 if ClassDiagram_Hotel_Booking12 is not None else set()
        
        pass
    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def bookingID(self):
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

    def __init__(self, phoneNumber: str, ssn: str, payment: str, name: str, adress: str, ClassDiagram_Company_GuestRecord: "ClassDiagram_Company" = None):
        self.phoneNumber = phoneNumber
        self.ssn = ssn
        self.payment = payment
        self.name = name
        self.adress = adress
        self.ClassDiagram_Company_GuestRecord = ClassDiagram_Company_GuestRecord
        
        pass
    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress


    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn


    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, payment: str):
        self.__payment = payment


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

    def __init__(self, name: str, ClassDiagram_Company_Hotel: "ClassDiagram_Company" = None, ClassDiagram_Company_Hotel4: set["ClassDiagram_Hotel_Booking"] = None, ClassDiagram_Company_Hotel6: set["ClassDiagram_Hotel_Room"] = None, ClassDiagram_Company_Hotel8: set["ClassDiagram_Hotel_Facility"] = None, ClassDiagram_Company_Hotel10: set["ClassDiagram_Hotel_Staff"] = None):
        self.name = name
        self.ClassDiagram_Company_Hotel = ClassDiagram_Company_Hotel
        self.ClassDiagram_Company_Hotel4 = ClassDiagram_Company_Hotel4 if ClassDiagram_Company_Hotel4 is not None else set()
        self.ClassDiagram_Company_Hotel6 = ClassDiagram_Company_Hotel6 if ClassDiagram_Company_Hotel6 is not None else set()
        self.ClassDiagram_Company_Hotel8 = ClassDiagram_Company_Hotel8 if ClassDiagram_Company_Hotel8 is not None else set()
        self.ClassDiagram_Company_Hotel10 = ClassDiagram_Company_Hotel10 if ClassDiagram_Company_Hotel10 is not None else set()
        
        pass
    @property
    def name(self):
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
                    

class ClassDiagram_Company:

    def __init__(self, name: str, ClassDiagram_Company: set["ClassDiagram_Company_Hotel"] = None, ClassDiagram_Company2: set["ClassDiagram_Company_GuestRecord"] = None):
        self.name = name
        self.ClassDiagram_Company = ClassDiagram_Company if ClassDiagram_Company is not None else set()
        self.ClassDiagram_Company2 = ClassDiagram_Company2 if ClassDiagram_Company2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                    
