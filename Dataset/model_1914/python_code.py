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

class ClassDiagram_FacilityManager:

    def __init__(self, ClassDiagram_FacilityManager: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_FacilityManager = ClassDiagram_FacilityManager
        
        pass
    @property
    def ClassDiagram_FacilityManager(self):
        return self.__ClassDiagram_FacilityManager

    @ClassDiagram_FacilityManager.setter
    def ClassDiagram_FacilityManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_FacilityManager__ClassDiagram_FacilityManager", None)
        self.__ClassDiagram_FacilityManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel63"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel63", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel63"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel63", None)
                setattr(value, "ClassDiagram_Company_Hotel63", self)

    def findBookedServices(self, ClassDiagram_guest):
        # TODO: Implement findBookedServices method
        pass

    def findServices(self, ClassDiagram_start, ClassDiagram_end, ClassDiagram_facility):
        # TODO: Implement findServices method
        pass

class ClassDiagram_HotelAdministration:

    def __init__(self, ClassDiagram_HotelAdministration: "ClassDiagram_Company" = None):
        self.ClassDiagram_HotelAdministration = ClassDiagram_HotelAdministration
        
        pass
    @property
    def ClassDiagram_HotelAdministration(self):
        return self.__ClassDiagram_HotelAdministration

    @ClassDiagram_HotelAdministration.setter
    def ClassDiagram_HotelAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_HotelAdministration__ClassDiagram_HotelAdministration", None)
        self.__ClassDiagram_HotelAdministration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company61"):
                opp_val = getattr(old_value, "ClassDiagram_Company61", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company61"):
                opp_val = getattr(value, "ClassDiagram_Company61", None)
                setattr(value, "ClassDiagram_Company61", self)

    def editHotel(self, ClassDiagram_hotel):
        # TODO: Implement editHotel method
        pass

    def removeHotel(self, ClassDiagram_hotel):
        # TODO: Implement removeHotel method
        pass

    def addHotel(self, ClassDiagram_name):
        # TODO: Implement addHotel method
        pass

class ClassDiagram_FacilityAdministration:

    def __init__(self, ClassDiagram_FacilityAdministration: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_FacilityAdministration = ClassDiagram_FacilityAdministration
        
        pass
    @property
    def ClassDiagram_FacilityAdministration(self):
        return self.__ClassDiagram_FacilityAdministration

    @ClassDiagram_FacilityAdministration.setter
    def ClassDiagram_FacilityAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_FacilityAdministration__ClassDiagram_FacilityAdministration", None)
        self.__ClassDiagram_FacilityAdministration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel59"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel59", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel59"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel59", None)
                setattr(value, "ClassDiagram_Company_Hotel59", self)

    def removeFacilityType(self, ClassDiagram_facility):
        # TODO: Implement removeFacilityType method
        pass

    def addFacility(self, ClassDiagram_facilityType, ClassDiagram_name):
        # TODO: Implement addFacility method
        pass

    def removeService(self, ClassDiagram_service):
        # TODO: Implement removeService method
        pass

    def removeFacility(self, ClassDiagram_facility):
        # TODO: Implement removeFacility method
        pass

    def editFacility(self, ClassDiagram_facility):
        # TODO: Implement editFacility method
        pass

    def addService(self, ClassDiagram_facility, ClassDiagram_name, ClassDiagram_price):
        # TODO: Implement addService method
        pass

    def addFacilityType(self, ClassDiagram_name):
        # TODO: Implement addFacilityType method
        pass

    def editService(self, ClassDiagram_service):
        # TODO: Implement editService method
        pass

    def editFacilityType(self, ClassDiagram_facility):
        # TODO: Implement editFacilityType method
        pass

class ClassDiagram_StaffAdministration:

    def __init__(self, ClassDiagram_StaffAdministration: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_StaffAdministration = ClassDiagram_StaffAdministration
        
        pass
    @property
    def ClassDiagram_StaffAdministration(self):
        return self.__ClassDiagram_StaffAdministration

    @ClassDiagram_StaffAdministration.setter
    def ClassDiagram_StaffAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_StaffAdministration__ClassDiagram_StaffAdministration", None)
        self.__ClassDiagram_StaffAdministration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel53"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel53", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel53"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel53", None)
                setattr(value, "ClassDiagram_Company_Hotel53", self)

    def editStaff(self, ClassDiagram_staff):
        # TODO: Implement editStaff method
        pass

    def removeStaff(self, ClassDiagram_staff):
        # TODO: Implement removeStaff method
        pass

    def addStaff(self, ClassDiagram_workTitel, ClassDiagram_lastName, ClassDiagram_ssn, ClassDiagram_firstName):
        # TODO: Implement addStaff method
        pass

class ClassDiagram_ApplianceAdministration:

    def __init__(self, ClassDiagram_ApplianceAdministration: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_ApplianceAdministration = ClassDiagram_ApplianceAdministration
        
        pass
    @property
    def ClassDiagram_ApplianceAdministration(self):
        return self.__ClassDiagram_ApplianceAdministration

    @ClassDiagram_ApplianceAdministration.setter
    def ClassDiagram_ApplianceAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_ApplianceAdministration__ClassDiagram_ApplianceAdministration", None)
        self.__ClassDiagram_ApplianceAdministration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel57"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel57", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel57"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel57", None)
                setattr(value, "ClassDiagram_Company_Hotel57", self)

    def editApplianceService(self, ClassDiagram_applianceService):
        # TODO: Implement editApplianceService method
        pass

    def removeApplianceServer(self, ClassDiagram_applianceService):
        # TODO: Implement removeApplianceServer method
        pass

    def addApplianceType(self, ClassDiagram_name):
        # TODO: Implement addApplianceType method
        pass

    def editApplianceType(self, ClassDiagram_applianceType):
        # TODO: Implement editApplianceType method
        pass

    def addAppliance(self, ClassDiagram_room):
        # TODO: Implement addAppliance method
        pass

    def addApplianceService(self, ClassDiagram_applianceService):
        # TODO: Implement addApplianceService method
        pass

    def removeApplianceType(self, ClassDiagram_applianceType):
        # TODO: Implement removeApplianceType method
        pass

    def removeAppliance(self, ClassDiagram_appliance):
        # TODO: Implement removeAppliance method
        pass

    def editAppliance(self, ClassDiagram_appliance):
        # TODO: Implement editAppliance method
        pass

class ClassDiagram_RoomAdministration:

    def __init__(self, ClassDiagram_RoomAdministration: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_RoomAdministration = ClassDiagram_RoomAdministration
        
        pass
    @property
    def ClassDiagram_RoomAdministration(self):
        return self.__ClassDiagram_RoomAdministration

    @ClassDiagram_RoomAdministration.setter
    def ClassDiagram_RoomAdministration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_RoomAdministration__ClassDiagram_RoomAdministration", None)
        self.__ClassDiagram_RoomAdministration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel55"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel55", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel55"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel55", None)
                setattr(value, "ClassDiagram_Company_Hotel55", self)

    def editRoom(self, ClassDiagram_room):
        # TODO: Implement editRoom method
        pass

    def editRoomType(self, ClassDiagram_roomType):
        # TODO: Implement editRoomType method
        pass

    def createRoomType(self, ClassDiagram_maxNumberOfGuests, ClassDiagram_area, ClassDiagram_price, ClassDiagram_applianceTypes):
        # TODO: Implement createRoomType method
        pass

    def removeRoom(self, ClassDiagram_room):
        # TODO: Implement removeRoom method
        pass

    def addRoom(self, ClassDiagram_roomType, ClassDiagram_appliances, ClassDiagram_roomNumber):
        # TODO: Implement addRoom method
        pass

    def removeRoomType(self, ClassDiagram_roomType):
        # TODO: Implement removeRoomType method
        pass

class ClassDiagram_BillManager:

    def __init__(self, ClassDiagram_BillManager: "ClassDiagram_BookingManager" = None, ClassDiagram_BillManager50: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_BillManager = ClassDiagram_BillManager
        self.ClassDiagram_BillManager50 = ClassDiagram_BillManager50
        
        pass
    @property
    def ClassDiagram_BillManager(self):
        return self.__ClassDiagram_BillManager

    @ClassDiagram_BillManager.setter
    def ClassDiagram_BillManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BillManager__ClassDiagram_BillManager", None)
        self.__ClassDiagram_BillManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BookingManager42"):
                opp_val = getattr(old_value, "ClassDiagram_BookingManager42", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BookingManager42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BookingManager42"):
                opp_val = getattr(value, "ClassDiagram_BookingManager42", None)
                setattr(value, "ClassDiagram_BookingManager42", self)

    @property
    def ClassDiagram_BillManager50(self):
        return self.__ClassDiagram_BillManager50

    @ClassDiagram_BillManager50.setter
    def ClassDiagram_BillManager50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BillManager__ClassDiagram_BillManager50", None)
        self.__ClassDiagram_BillManager50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel51"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel51", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel51"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel51", None)
                setattr(value, "ClassDiagram_Company_Hotel51", self)

    def getAmount(self, ClassDiagram_bookingID):
        # TODO: Implement getAmount method
        pass

    def createReceipt(self, ClassDiagram_bookingID):
        # TODO: Implement createReceipt method
        pass

    def pay(self, ClassDiagram_bookingID):
        # TODO: Implement pay method
        pass

    def findBill(self, ClassDiagram_bookingID):
        # TODO: Implement findBill method
        pass

    def addPurchasedService(self, ClassDiagram_item, ClassDiagram_amount, ClassDiagram_bookingID):
        # TODO: Implement addPurchasedService method
        pass

class ClassDiagram_GuestManager:

    def __init__(self, ClassDiagram_GuestManager: "ClassDiagram_BookingManager" = None, ClassDiagram_GuestManager47: "ClassDiagram_Company" = None):
        self.ClassDiagram_GuestManager = ClassDiagram_GuestManager
        self.ClassDiagram_GuestManager47 = ClassDiagram_GuestManager47
        
        pass
    @property
    def ClassDiagram_GuestManager(self):
        return self.__ClassDiagram_GuestManager

    @ClassDiagram_GuestManager.setter
    def ClassDiagram_GuestManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_GuestManager__ClassDiagram_GuestManager", None)
        self.__ClassDiagram_GuestManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BookingManager40"):
                opp_val = getattr(old_value, "ClassDiagram_BookingManager40", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BookingManager40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BookingManager40"):
                opp_val = getattr(value, "ClassDiagram_BookingManager40", None)
                setattr(value, "ClassDiagram_BookingManager40", self)

    @property
    def ClassDiagram_GuestManager47(self):
        return self.__ClassDiagram_GuestManager47

    @ClassDiagram_GuestManager47.setter
    def ClassDiagram_GuestManager47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_GuestManager__ClassDiagram_GuestManager47", None)
        self.__ClassDiagram_GuestManager47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company48"):
                opp_val = getattr(old_value, "ClassDiagram_Company48", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company48"):
                opp_val = getattr(value, "ClassDiagram_Company48", None)
                setattr(value, "ClassDiagram_Company48", self)

    def createGuestRecord(self, ClassDiagram_adress, ClassDiagram_lastName, ClassDiagram_phoneNumber, ClassDiagram_paymentInformation, ClassDiagram_firstName, ClassDiagram_ssn):
        # TODO: Implement createGuestRecord method
        pass

    def editGuestRecord(self, ClassDiagram_ssn):
        # TODO: Implement editGuestRecord method
        pass

    def findGuestRecord(self, ClassDiagram_ssn):
        # TODO: Implement findGuestRecord method
        pass

    def removeGuestRecord(self, ClassDiagram_ssn):
        # TODO: Implement removeGuestRecord method
        pass

    def findGuestRecords(self, ClassDiagram_firstName, ClassDiagram_lastName):
        # TODO: Implement findGuestRecords method
        pass

class ClassDiagram_RoomManager:

    def __init__(self, ClassDiagram_RoomManager: "ClassDiagram_BookingManager" = None, ClassDiagram_RoomManager44: "ClassDiagram_Company_Hotel" = None):
        self.ClassDiagram_RoomManager = ClassDiagram_RoomManager
        self.ClassDiagram_RoomManager44 = ClassDiagram_RoomManager44
        
        pass
    @property
    def ClassDiagram_RoomManager(self):
        return self.__ClassDiagram_RoomManager

    @ClassDiagram_RoomManager.setter
    def ClassDiagram_RoomManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_RoomManager__ClassDiagram_RoomManager", None)
        self.__ClassDiagram_RoomManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BookingManager38"):
                opp_val = getattr(old_value, "ClassDiagram_BookingManager38", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BookingManager38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BookingManager38"):
                opp_val = getattr(value, "ClassDiagram_BookingManager38", None)
                setattr(value, "ClassDiagram_BookingManager38", self)

    @property
    def ClassDiagram_RoomManager44(self):
        return self.__ClassDiagram_RoomManager44

    @ClassDiagram_RoomManager44.setter
    def ClassDiagram_RoomManager44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_RoomManager__ClassDiagram_RoomManager44", None)
        self.__ClassDiagram_RoomManager44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel45"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel45", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel45"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel45", None)
                setattr(value, "ClassDiagram_Company_Hotel45", self)

    def getRoomsToClean(self):
        # TODO: Implement getRoomsToClean method
        pass

    def getRoomsToMaintain(self):
        # TODO: Implement getRoomsToMaintain method
        pass

    def cleaningStatus(self, ClassDiagram_room):
        # TODO: Implement cleaningStatus method
        pass

    def maintenanceStatus(self, ClassDiagram_room):
        # TODO: Implement maintenanceStatus method
        pass

    def roomExists(self, ClassDiagram_roomNumber, ClassDiagram_rooms):
        # TODO: Implement roomExists method
        pass

    def findRoom(self, ClassDiagram_roomNumber):
        # TODO: Implement findRoom method
        pass

class ClassDiagram_Booking_PurchasedService:

    def __init__(self, name: str, price: float, ClassDiagram_Booking_PurchasedService: "ClassDiagram_Booking_Bill" = None):
        self.name = name
        self.price = price
        self.ClassDiagram_Booking_PurchasedService = ClassDiagram_Booking_PurchasedService
        
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
            if hasattr(old_value, "ClassDiagram_Booking_Bill33"):
                opp_val = getattr(old_value, "ClassDiagram_Booking_Bill33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Booking_Bill33"):
                opp_val = getattr(value, "ClassDiagram_Booking_Bill33", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Booking_Bill33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_BookingManager:

    def __init__(self, ClassDiagram_BookingManager: "ClassDiagram_Company_Hotel" = None, ClassDiagram_BookingManager38: "ClassDiagram_RoomManager" = None, ClassDiagram_BookingManager40: "ClassDiagram_GuestManager" = None, ClassDiagram_BookingManager42: "ClassDiagram_BillManager" = None):
        self.ClassDiagram_BookingManager = ClassDiagram_BookingManager
        self.ClassDiagram_BookingManager38 = ClassDiagram_BookingManager38
        self.ClassDiagram_BookingManager40 = ClassDiagram_BookingManager40
        self.ClassDiagram_BookingManager42 = ClassDiagram_BookingManager42
        
        pass
    @property
    def ClassDiagram_BookingManager38(self):
        return self.__ClassDiagram_BookingManager38

    @ClassDiagram_BookingManager38.setter
    def ClassDiagram_BookingManager38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BookingManager__ClassDiagram_BookingManager38", None)
        self.__ClassDiagram_BookingManager38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_RoomManager"):
                opp_val = getattr(old_value, "ClassDiagram_RoomManager", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_RoomManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_RoomManager"):
                opp_val = getattr(value, "ClassDiagram_RoomManager", None)
                setattr(value, "ClassDiagram_RoomManager", self)

    @property
    def ClassDiagram_BookingManager42(self):
        return self.__ClassDiagram_BookingManager42

    @ClassDiagram_BookingManager42.setter
    def ClassDiagram_BookingManager42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BookingManager__ClassDiagram_BookingManager42", None)
        self.__ClassDiagram_BookingManager42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BillManager"):
                opp_val = getattr(old_value, "ClassDiagram_BillManager", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BillManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BillManager"):
                opp_val = getattr(value, "ClassDiagram_BillManager", None)
                setattr(value, "ClassDiagram_BillManager", self)

    @property
    def ClassDiagram_BookingManager40(self):
        return self.__ClassDiagram_BookingManager40

    @ClassDiagram_BookingManager40.setter
    def ClassDiagram_BookingManager40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BookingManager__ClassDiagram_BookingManager40", None)
        self.__ClassDiagram_BookingManager40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_GuestManager"):
                opp_val = getattr(old_value, "ClassDiagram_GuestManager", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_GuestManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_GuestManager"):
                opp_val = getattr(value, "ClassDiagram_GuestManager", None)
                setattr(value, "ClassDiagram_GuestManager", self)

    @property
    def ClassDiagram_BookingManager(self):
        return self.__ClassDiagram_BookingManager

    @ClassDiagram_BookingManager.setter
    def ClassDiagram_BookingManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_BookingManager__ClassDiagram_BookingManager", None)
        self.__ClassDiagram_BookingManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_Hotel36"):
                opp_val = getattr(old_value, "ClassDiagram_Company_Hotel36", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_Hotel36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_Hotel36"):
                opp_val = getattr(value, "ClassDiagram_Company_Hotel36", None)
                setattr(value, "ClassDiagram_Company_Hotel36", self)

    def editBooking(self, ClassDiagram_bookingId):
        # TODO: Implement editBooking method
        pass

    def getBookings(self, ClassDiagram_ssn):
        # TODO: Implement getBookings method
        pass

    def findAvailableRooms(self, ClassDiagram__people, ClassDiagram_roomType, ClassDiagram_end, ClassDiagram_start):
        # TODO: Implement findAvailableRooms method
        pass

    def createBooking(self, ClassDiagram_end, ClassDiagram_rooms, ClassDiagram_numberOfPeople, ClassDiagram_guest, ClassDiagram_start):
        # TODO: Implement createBooking method
        pass

    def checkOut(self, ClassDiagram_bookingID):
        # TODO: Implement checkOut method
        pass

    def cancelBooking(self, ClassDiagram_bookingId):
        # TODO: Implement cancelBooking method
        pass

    def findAvailableRoomTypes(self, ClassDiagram_end, ClassDiagram_start):
        # TODO: Implement findAvailableRoomTypes method
        pass

    def initBooking(self):
        # TODO: Implement initBooking method
        pass

    def assignKey(self, ClassDiagram_booking, ClassDiagram_expirationDate, ClassDiagram_room):
        # TODO: Implement assignKey method
        pass

    def findBooking(self, ClassDiagram_bookingID):
        # TODO: Implement findBooking method
        pass

    def checkIn(self, ClassDiagram_bookingID):
        # TODO: Implement checkIn method
        pass

class ClassDiagram_IServiceBooking(ABC):

    def __init__(self):
        
        pass
    def cancelBookedService(self, ClassDiagram_service):
        # TODO: Implement cancelBookedService method
        pass

    def findBookedService(self, ClassDiagram_bookedServiceID):
        # TODO: Implement findBookedService method
        pass

    def bookFacilityService(self, ClassDiagram_guest, ClassDiagram_date, ClassDiagram_facility, ClassDiagram_service, ClassDiagram_booking):
        # TODO: Implement bookFacilityService method
        pass

    def getBookedServices(self, ClassDiagram_booking):
        # TODO: Implement getBookedServices method
        pass

    def findAvailableServices(self, ClassDiagram_date, ClassDiagram_facility):
        # TODO: Implement findAvailableServices method
        pass

class ClassDiagram_Facility_FacilityType:

    def __init__(self, name: str, ClassDiagram_Facility_FacilityType: "ClassDiagram_Hotel_Facility" = None):
        self.name = name
        self.ClassDiagram_Facility_FacilityType = ClassDiagram_Facility_FacilityType
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "ClassDiagram_Hotel_Facility"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Facility", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Facility", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Facility"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Facility", None)
                setattr(value, "ClassDiagram_Hotel_Facility", self)

class ClassDiagram_Hotel_Facility:

    def __init__(self, name: str, ClassDiagram_Hotel_Facility: "ClassDiagram_Facility_FacilityType" = None):
        self.name = name
        self.ClassDiagram_Hotel_Facility = ClassDiagram_Hotel_Facility
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "ClassDiagram_Facility_FacilityType"):
                opp_val = getattr(old_value, "ClassDiagram_Facility_FacilityType", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Facility_FacilityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Facility_FacilityType"):
                opp_val = getattr(value, "ClassDiagram_Facility_FacilityType", None)
                setattr(value, "ClassDiagram_Facility_FacilityType", self)

class ClassDiagram_Room_RoomAppliance:

    def __init__(self, name: str, ClassDiagram_Room_RoomAppliance: "ClassDiagram_RoomAppliance_ApplianceType" = None):
        self.name = name
        self.ClassDiagram_Room_RoomAppliance = ClassDiagram_Room_RoomAppliance
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType19"):
                opp_val = getattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType19", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_RoomAppliance_ApplianceType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_RoomAppliance_ApplianceType19"):
                opp_val = getattr(value, "ClassDiagram_RoomAppliance_ApplianceType19", None)
                setattr(value, "ClassDiagram_RoomAppliance_ApplianceType19", self)

class ClassDiagram_ApplianceType_ApplianceService:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
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


class ClassDiagram_RoomAppliance_ApplianceType:

    def __init__(self, name: str, ClassDiagram_RoomAppliance_ApplianceType19: "ClassDiagram_Room_RoomAppliance" = None, ClassDiagram_RoomAppliance_ApplianceType: "ClassDiagram_Room_RoomType" = None):
        self.name = name
        self.ClassDiagram_RoomAppliance_ApplianceType19 = ClassDiagram_RoomAppliance_ApplianceType19
        self.ClassDiagram_RoomAppliance_ApplianceType = ClassDiagram_RoomAppliance_ApplianceType
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ClassDiagram_RoomAppliance_ApplianceType19(self):
        return self.__ClassDiagram_RoomAppliance_ApplianceType19

    @ClassDiagram_RoomAppliance_ApplianceType19.setter
    def ClassDiagram_RoomAppliance_ApplianceType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_RoomAppliance_ApplianceType__ClassDiagram_RoomAppliance_ApplianceType19", None)
        self.__ClassDiagram_RoomAppliance_ApplianceType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Room_RoomAppliance"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomAppliance", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Room_RoomAppliance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomAppliance"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomAppliance", None)
                setattr(value, "ClassDiagram_Room_RoomAppliance", self)

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
            if hasattr(old_value, "ClassDiagram_Room_RoomType17"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomType17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomType17"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomType17", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Room_RoomType17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Facility_FacilityService:

    def __init__(self, name: str, price: float, ClassDiagram_Facility_FacilityService: "ClassDiagram_Booking_BookedService" = None):
        self.name = name
        self.price = price
        self.ClassDiagram_Facility_FacilityService = ClassDiagram_Facility_FacilityService
        
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


    @property
    def ClassDiagram_Facility_FacilityService(self):
        return self.__ClassDiagram_Facility_FacilityService

    @ClassDiagram_Facility_FacilityService.setter
    def ClassDiagram_Facility_FacilityService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Facility_FacilityService__ClassDiagram_Facility_FacilityService", None)
        self.__ClassDiagram_Facility_FacilityService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Booking_BookedService31"):
                opp_val = getattr(old_value, "ClassDiagram_Booking_BookedService31", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Booking_BookedService31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Booking_BookedService31"):
                opp_val = getattr(value, "ClassDiagram_Booking_BookedService31", None)
                setattr(value, "ClassDiagram_Booking_BookedService31", self)

class ClassDiagram_Booking_Bill:

    def __init__(self, paidAmount: float, ClassDiagram_Booking_Bill: "ClassDiagram_Hotel_Booking" = None, ClassDiagram_Booking_Bill33: set["ClassDiagram_Booking_PurchasedService"] = None):
        self.paidAmount = paidAmount
        self.ClassDiagram_Booking_Bill = ClassDiagram_Booking_Bill
        self.ClassDiagram_Booking_Bill33 = ClassDiagram_Booking_Bill33 if ClassDiagram_Booking_Bill33 is not None else set()
        
        pass
    @property
    def paidAmount(self):
        return self.__paidAmount

    @paidAmount.setter
    def paidAmount(self, paidAmount: float):
        self.__paidAmount = paidAmount


    @property
    def ClassDiagram_Booking_Bill33(self):
        return self.__ClassDiagram_Booking_Bill33

    @ClassDiagram_Booking_Bill33.setter
    def ClassDiagram_Booking_Bill33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_Bill__ClassDiagram_Booking_Bill33", None)
        self.__ClassDiagram_Booking_Bill33 = value if value is not None else set()
        
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
                    

    @property
    def ClassDiagram_Booking_Bill(self):
        return self.__ClassDiagram_Booking_Bill

    @ClassDiagram_Booking_Bill.setter
    def ClassDiagram_Booking_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_Bill__ClassDiagram_Booking_Bill", None)
        self.__ClassDiagram_Booking_Bill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Booking29"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Booking29", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Booking29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Booking29"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Booking29", None)
                setattr(value, "ClassDiagram_Hotel_Booking29", self)

class ClassDiagram_Booking_BookedService:

    def __init__(self, date: date, ClassDiagram_Booking_BookedService: "ClassDiagram_Hotel_Booking" = None, ClassDiagram_Booking_BookedService31: "ClassDiagram_Facility_FacilityService" = None):
        self.date = date
        self.ClassDiagram_Booking_BookedService = ClassDiagram_Booking_BookedService
        self.ClassDiagram_Booking_BookedService31 = ClassDiagram_Booking_BookedService31
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


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
            if hasattr(old_value, "ClassDiagram_Hotel_Booking21"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Booking21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Booking21"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Booking21", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Booking21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassDiagram_Booking_BookedService31(self):
        return self.__ClassDiagram_Booking_BookedService31

    @ClassDiagram_Booking_BookedService31.setter
    def ClassDiagram_Booking_BookedService31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Booking_BookedService__ClassDiagram_Booking_BookedService31", None)
        self.__ClassDiagram_Booking_BookedService31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Facility_FacilityService"):
                opp_val = getattr(old_value, "ClassDiagram_Facility_FacilityService", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Facility_FacilityService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Facility_FacilityService"):
                opp_val = getattr(value, "ClassDiagram_Facility_FacilityService", None)
                setattr(value, "ClassDiagram_Facility_FacilityService", self)

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
            if hasattr(old_value, "ClassDiagram_Hotel_Room12"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Room12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Room12"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Room12", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Room12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Room_RoomType:

    def __init__(self, price: float, maxNumberOfGuests: int, area: float, name: str, ClassDiagram_Room_RoomType: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Room_RoomType15: "ClassDiagram_Hotel_Room" = None, ClassDiagram_Room_RoomType17: set["ClassDiagram_RoomAppliance_ApplianceType"] = None):
        self.price = price
        self.maxNumberOfGuests = maxNumberOfGuests
        self.area = area
        self.name = name
        self.ClassDiagram_Room_RoomType = ClassDiagram_Room_RoomType
        self.ClassDiagram_Room_RoomType15 = ClassDiagram_Room_RoomType15
        self.ClassDiagram_Room_RoomType17 = ClassDiagram_Room_RoomType17 if ClassDiagram_Room_RoomType17 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def maxNumberOfGuests(self):
        return self.__maxNumberOfGuests

    @maxNumberOfGuests.setter
    def maxNumberOfGuests(self, maxNumberOfGuests: int):
        self.__maxNumberOfGuests = maxNumberOfGuests


    @property
    def ClassDiagram_Room_RoomType17(self):
        return self.__ClassDiagram_Room_RoomType17

    @ClassDiagram_Room_RoomType17.setter
    def ClassDiagram_Room_RoomType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomType__ClassDiagram_Room_RoomType17", None)
        self.__ClassDiagram_Room_RoomType17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_RoomAppliance_ApplianceType"):
                    opp_val = getattr(item, "ClassDiagram_RoomAppliance_ApplianceType", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_RoomAppliance_ApplianceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_RoomAppliance_ApplianceType"):
                    opp_val = getattr(item, "ClassDiagram_RoomAppliance_ApplianceType", None)
                    
                    setattr(item, "ClassDiagram_RoomAppliance_ApplianceType", self)
                    

    @property
    def ClassDiagram_Room_RoomType15(self):
        return self.__ClassDiagram_Room_RoomType15

    @ClassDiagram_Room_RoomType15.setter
    def ClassDiagram_Room_RoomType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Room_RoomType__ClassDiagram_Room_RoomType15", None)
        self.__ClassDiagram_Room_RoomType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Room14"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Room14", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Room14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Room14"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Room14", None)
                setattr(value, "ClassDiagram_Hotel_Room14", self)

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

class ClassDiagram_Hotel_Booking:

    def __init__(self, startDate: date, endDate: date, price: float, checkedIn: bool, bookingID: int, ClassDiagram_Hotel_Booking: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Booking21: set["ClassDiagram_Booking_BookedService"] = None, ClassDiagram_Hotel_Booking23: set["ClassDiagram_Hotel_Room"] = None, ClassDiagram_Hotel_Booking26: "ClassDiagram_Company_GuestRecord" = None, ClassDiagram_Hotel_Booking29: "ClassDiagram_Booking_Bill" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.price = price
        self.checkedIn = checkedIn
        self.bookingID = bookingID
        self.ClassDiagram_Hotel_Booking = ClassDiagram_Hotel_Booking
        self.ClassDiagram_Hotel_Booking21 = ClassDiagram_Hotel_Booking21 if ClassDiagram_Hotel_Booking21 is not None else set()
        self.ClassDiagram_Hotel_Booking23 = ClassDiagram_Hotel_Booking23 if ClassDiagram_Hotel_Booking23 is not None else set()
        self.ClassDiagram_Hotel_Booking26 = ClassDiagram_Hotel_Booking26
        self.ClassDiagram_Hotel_Booking29 = ClassDiagram_Hotel_Booking29
        
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
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


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

    @property
    def ClassDiagram_Hotel_Booking29(self):
        return self.__ClassDiagram_Hotel_Booking29

    @ClassDiagram_Hotel_Booking29.setter
    def ClassDiagram_Hotel_Booking29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking29", None)
        self.__ClassDiagram_Hotel_Booking29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Booking_Bill"):
                opp_val = getattr(old_value, "ClassDiagram_Booking_Bill", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Booking_Bill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Booking_Bill"):
                opp_val = getattr(value, "ClassDiagram_Booking_Bill", None)
                setattr(value, "ClassDiagram_Booking_Bill", self)

    @property
    def ClassDiagram_Hotel_Booking23(self):
        return self.__ClassDiagram_Hotel_Booking23

    @ClassDiagram_Hotel_Booking23.setter
    def ClassDiagram_Hotel_Booking23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking23", None)
        self.__ClassDiagram_Hotel_Booking23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassDiagram_Hotel_Room24"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Room24", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Hotel_Room24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Hotel_Room24"):
                    opp_val = getattr(item, "ClassDiagram_Hotel_Room24", None)
                    
                    setattr(item, "ClassDiagram_Hotel_Room24", self)
                    

    @property
    def ClassDiagram_Hotel_Booking21(self):
        return self.__ClassDiagram_Hotel_Booking21

    @ClassDiagram_Hotel_Booking21.setter
    def ClassDiagram_Hotel_Booking21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking21", None)
        self.__ClassDiagram_Hotel_Booking21 = value if value is not None else set()
        
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
                    

    @property
    def ClassDiagram_Hotel_Booking26(self):
        return self.__ClassDiagram_Hotel_Booking26

    @ClassDiagram_Hotel_Booking26.setter
    def ClassDiagram_Hotel_Booking26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Booking__ClassDiagram_Hotel_Booking26", None)
        self.__ClassDiagram_Hotel_Booking26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Company_GuestRecord27"):
                opp_val = getattr(old_value, "ClassDiagram_Company_GuestRecord27", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Company_GuestRecord27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Company_GuestRecord27"):
                opp_val = getattr(value, "ClassDiagram_Company_GuestRecord27", None)
                setattr(value, "ClassDiagram_Company_GuestRecord27", self)

class ClassDiagram_Hotel_Staff:

    def __init__(self, ssn: str, firstName: str, lastName: str, hasWorkTitel: str, ClassDiagram_Hotel_Staff: "ClassDiagram_Company_Hotel" = None):
        self.ssn = ssn
        self.firstName = firstName
        self.lastName = lastName
        self.hasWorkTitel = hasWorkTitel
        self.ClassDiagram_Hotel_Staff = ClassDiagram_Hotel_Staff
        
        pass
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
    def hasWorkTitel(self):
        return self.__hasWorkTitel

    @hasWorkTitel.setter
    def hasWorkTitel(self, hasWorkTitel: str):
        self.__hasWorkTitel = hasWorkTitel


    @property
    def firstName(self):
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

class ClassDiagram_Hotel_Room:

    def __init__(self, roomNumber: int, cleaningStatus: bool, maintenceStatus: bool, ClassDiagram_Hotel_Room: "ClassDiagram_Company_Hotel" = None, ClassDiagram_Hotel_Room12: set["ClassDiagram_Room_RoomKey"] = None, ClassDiagram_Hotel_Room14: "ClassDiagram_Room_RoomType" = None, ClassDiagram_Hotel_Room24: "ClassDiagram_Hotel_Booking" = None):
        self.roomNumber = roomNumber
        self.cleaningStatus = cleaningStatus
        self.maintenceStatus = maintenceStatus
        self.ClassDiagram_Hotel_Room = ClassDiagram_Hotel_Room
        self.ClassDiagram_Hotel_Room12 = ClassDiagram_Hotel_Room12 if ClassDiagram_Hotel_Room12 is not None else set()
        self.ClassDiagram_Hotel_Room14 = ClassDiagram_Hotel_Room14
        self.ClassDiagram_Hotel_Room24 = ClassDiagram_Hotel_Room24
        
        pass
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
    def maintenceStatus(self):
        return self.__maintenceStatus

    @maintenceStatus.setter
    def maintenceStatus(self, maintenceStatus: bool):
        self.__maintenceStatus = maintenceStatus


    @property
    def ClassDiagram_Hotel_Room12(self):
        return self.__ClassDiagram_Hotel_Room12

    @ClassDiagram_Hotel_Room12.setter
    def ClassDiagram_Hotel_Room12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room12", None)
        self.__ClassDiagram_Hotel_Room12 = value if value is not None else set()
        
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
    def ClassDiagram_Hotel_Room14(self):
        return self.__ClassDiagram_Hotel_Room14

    @ClassDiagram_Hotel_Room14.setter
    def ClassDiagram_Hotel_Room14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room14", None)
        self.__ClassDiagram_Hotel_Room14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Room_RoomType15"):
                opp_val = getattr(old_value, "ClassDiagram_Room_RoomType15", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Room_RoomType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Room_RoomType15"):
                opp_val = getattr(value, "ClassDiagram_Room_RoomType15", None)
                setattr(value, "ClassDiagram_Room_RoomType15", self)

    @property
    def ClassDiagram_Hotel_Room24(self):
        return self.__ClassDiagram_Hotel_Room24

    @ClassDiagram_Hotel_Room24.setter
    def ClassDiagram_Hotel_Room24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Hotel_Room__ClassDiagram_Hotel_Room24", None)
        self.__ClassDiagram_Hotel_Room24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Booking23"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Booking23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Booking23"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Booking23", None)
                if opp_val is None:
                    setattr(value, "ClassDiagram_Hotel_Booking23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassDiagram_Company_GuestRecord:

    def __init__(self, name: str, adress: str, phoneNumber: str, ssn: str, paymentInformation: str, ClassDiagram_Company_GuestRecord: "ClassDiagram_Company" = None, ClassDiagram_Company_GuestRecord27: "ClassDiagram_Hotel_Booking" = None):
        self.name = name
        self.adress = adress
        self.phoneNumber = phoneNumber
        self.ssn = ssn
        self.paymentInformation = paymentInformation
        self.ClassDiagram_Company_GuestRecord = ClassDiagram_Company_GuestRecord
        self.ClassDiagram_Company_GuestRecord27 = ClassDiagram_Company_GuestRecord27
        
        pass
    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def paymentInformation(self):
        return self.__paymentInformation

    @paymentInformation.setter
    def paymentInformation(self, paymentInformation: str):
        self.__paymentInformation = paymentInformation


    @property
    def ClassDiagram_Company_GuestRecord27(self):
        return self.__ClassDiagram_Company_GuestRecord27

    @ClassDiagram_Company_GuestRecord27.setter
    def ClassDiagram_Company_GuestRecord27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_GuestRecord__ClassDiagram_Company_GuestRecord27", None)
        self.__ClassDiagram_Company_GuestRecord27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_Hotel_Booking26"):
                opp_val = getattr(old_value, "ClassDiagram_Hotel_Booking26", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_Hotel_Booking26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_Hotel_Booking26"):
                opp_val = getattr(value, "ClassDiagram_Hotel_Booking26", None)
                setattr(value, "ClassDiagram_Hotel_Booking26", self)

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

    def __init__(self, name: str, ClassDiagram_Company_Hotel4: set["ClassDiagram_Hotel_Room"] = None, ClassDiagram_Company_Hotel6: set["ClassDiagram_Hotel_Staff"] = None, ClassDiagram_Company_Hotel8: set["ClassDiagram_Hotel_Booking"] = None, ClassDiagram_Company_Hotel10: set["ClassDiagram_Room_RoomType"] = None, ClassDiagram_Company_Hotel: "ClassDiagram_Company" = None, ClassDiagram_Company_Hotel36: "ClassDiagram_BookingManager" = None, ClassDiagram_Company_Hotel45: "ClassDiagram_RoomManager" = None, ClassDiagram_Company_Hotel53: "ClassDiagram_StaffAdministration" = None, ClassDiagram_Company_Hotel55: "ClassDiagram_RoomAdministration" = None, ClassDiagram_Company_Hotel51: "ClassDiagram_BillManager" = None, ClassDiagram_Company_Hotel57: "ClassDiagram_ApplianceAdministration" = None, ClassDiagram_Company_Hotel59: "ClassDiagram_FacilityAdministration" = None, ClassDiagram_Company_Hotel63: "ClassDiagram_FacilityManager" = None):
        self.name = name
        self.ClassDiagram_Company_Hotel4 = ClassDiagram_Company_Hotel4 if ClassDiagram_Company_Hotel4 is not None else set()
        self.ClassDiagram_Company_Hotel6 = ClassDiagram_Company_Hotel6 if ClassDiagram_Company_Hotel6 is not None else set()
        self.ClassDiagram_Company_Hotel8 = ClassDiagram_Company_Hotel8 if ClassDiagram_Company_Hotel8 is not None else set()
        self.ClassDiagram_Company_Hotel10 = ClassDiagram_Company_Hotel10 if ClassDiagram_Company_Hotel10 is not None else set()
        self.ClassDiagram_Company_Hotel = ClassDiagram_Company_Hotel
        self.ClassDiagram_Company_Hotel36 = ClassDiagram_Company_Hotel36
        self.ClassDiagram_Company_Hotel45 = ClassDiagram_Company_Hotel45
        self.ClassDiagram_Company_Hotel53 = ClassDiagram_Company_Hotel53
        self.ClassDiagram_Company_Hotel55 = ClassDiagram_Company_Hotel55
        self.ClassDiagram_Company_Hotel51 = ClassDiagram_Company_Hotel51
        self.ClassDiagram_Company_Hotel57 = ClassDiagram_Company_Hotel57
        self.ClassDiagram_Company_Hotel59 = ClassDiagram_Company_Hotel59
        self.ClassDiagram_Company_Hotel63 = ClassDiagram_Company_Hotel63
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ClassDiagram_Company_Hotel36(self):
        return self.__ClassDiagram_Company_Hotel36

    @ClassDiagram_Company_Hotel36.setter
    def ClassDiagram_Company_Hotel36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel36", None)
        self.__ClassDiagram_Company_Hotel36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BookingManager"):
                opp_val = getattr(old_value, "ClassDiagram_BookingManager", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BookingManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BookingManager"):
                opp_val = getattr(value, "ClassDiagram_BookingManager", None)
                setattr(value, "ClassDiagram_BookingManager", self)

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
    def ClassDiagram_Company_Hotel63(self):
        return self.__ClassDiagram_Company_Hotel63

    @ClassDiagram_Company_Hotel63.setter
    def ClassDiagram_Company_Hotel63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel63", None)
        self.__ClassDiagram_Company_Hotel63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_FacilityManager"):
                opp_val = getattr(old_value, "ClassDiagram_FacilityManager", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_FacilityManager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_FacilityManager"):
                opp_val = getattr(value, "ClassDiagram_FacilityManager", None)
                setattr(value, "ClassDiagram_FacilityManager", self)

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
    def ClassDiagram_Company_Hotel57(self):
        return self.__ClassDiagram_Company_Hotel57

    @ClassDiagram_Company_Hotel57.setter
    def ClassDiagram_Company_Hotel57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel57", None)
        self.__ClassDiagram_Company_Hotel57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_ApplianceAdministration"):
                opp_val = getattr(old_value, "ClassDiagram_ApplianceAdministration", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_ApplianceAdministration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_ApplianceAdministration"):
                opp_val = getattr(value, "ClassDiagram_ApplianceAdministration", None)
                setattr(value, "ClassDiagram_ApplianceAdministration", self)

    @property
    def ClassDiagram_Company_Hotel55(self):
        return self.__ClassDiagram_Company_Hotel55

    @ClassDiagram_Company_Hotel55.setter
    def ClassDiagram_Company_Hotel55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel55", None)
        self.__ClassDiagram_Company_Hotel55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_RoomAdministration"):
                opp_val = getattr(old_value, "ClassDiagram_RoomAdministration", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_RoomAdministration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_RoomAdministration"):
                opp_val = getattr(value, "ClassDiagram_RoomAdministration", None)
                setattr(value, "ClassDiagram_RoomAdministration", self)

    @property
    def ClassDiagram_Company_Hotel45(self):
        return self.__ClassDiagram_Company_Hotel45

    @ClassDiagram_Company_Hotel45.setter
    def ClassDiagram_Company_Hotel45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel45", None)
        self.__ClassDiagram_Company_Hotel45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_RoomManager44"):
                opp_val = getattr(old_value, "ClassDiagram_RoomManager44", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_RoomManager44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_RoomManager44"):
                opp_val = getattr(value, "ClassDiagram_RoomManager44", None)
                setattr(value, "ClassDiagram_RoomManager44", self)

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
                if hasattr(item, "ClassDiagram_Room_RoomType"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomType", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassDiagram_Room_RoomType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassDiagram_Room_RoomType"):
                    opp_val = getattr(item, "ClassDiagram_Room_RoomType", None)
                    
                    setattr(item, "ClassDiagram_Room_RoomType", self)
                    

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
    def ClassDiagram_Company_Hotel51(self):
        return self.__ClassDiagram_Company_Hotel51

    @ClassDiagram_Company_Hotel51.setter
    def ClassDiagram_Company_Hotel51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel51", None)
        self.__ClassDiagram_Company_Hotel51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_BillManager50"):
                opp_val = getattr(old_value, "ClassDiagram_BillManager50", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_BillManager50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_BillManager50"):
                opp_val = getattr(value, "ClassDiagram_BillManager50", None)
                setattr(value, "ClassDiagram_BillManager50", self)

    @property
    def ClassDiagram_Company_Hotel53(self):
        return self.__ClassDiagram_Company_Hotel53

    @ClassDiagram_Company_Hotel53.setter
    def ClassDiagram_Company_Hotel53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel53", None)
        self.__ClassDiagram_Company_Hotel53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_StaffAdministration"):
                opp_val = getattr(old_value, "ClassDiagram_StaffAdministration", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_StaffAdministration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_StaffAdministration"):
                opp_val = getattr(value, "ClassDiagram_StaffAdministration", None)
                setattr(value, "ClassDiagram_StaffAdministration", self)

    @property
    def ClassDiagram_Company_Hotel59(self):
        return self.__ClassDiagram_Company_Hotel59

    @ClassDiagram_Company_Hotel59.setter
    def ClassDiagram_Company_Hotel59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company_Hotel__ClassDiagram_Company_Hotel59", None)
        self.__ClassDiagram_Company_Hotel59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_FacilityAdministration"):
                opp_val = getattr(old_value, "ClassDiagram_FacilityAdministration", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_FacilityAdministration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_FacilityAdministration"):
                opp_val = getattr(value, "ClassDiagram_FacilityAdministration", None)
                setattr(value, "ClassDiagram_FacilityAdministration", self)

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

    def __init__(self, name: str, ClassDiagram_Company2: set["ClassDiagram_Company_GuestRecord"] = None, ClassDiagram_Company: set["ClassDiagram_Company_Hotel"] = None, ClassDiagram_Company48: "ClassDiagram_GuestManager" = None, ClassDiagram_Company61: "ClassDiagram_HotelAdministration" = None):
        self.name = name
        self.ClassDiagram_Company2 = ClassDiagram_Company2 if ClassDiagram_Company2 is not None else set()
        self.ClassDiagram_Company = ClassDiagram_Company if ClassDiagram_Company is not None else set()
        self.ClassDiagram_Company48 = ClassDiagram_Company48
        self.ClassDiagram_Company61 = ClassDiagram_Company61
        
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
    def ClassDiagram_Company48(self):
        return self.__ClassDiagram_Company48

    @ClassDiagram_Company48.setter
    def ClassDiagram_Company48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company__ClassDiagram_Company48", None)
        self.__ClassDiagram_Company48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_GuestManager47"):
                opp_val = getattr(old_value, "ClassDiagram_GuestManager47", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_GuestManager47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_GuestManager47"):
                opp_val = getattr(value, "ClassDiagram_GuestManager47", None)
                setattr(value, "ClassDiagram_GuestManager47", self)

    @property
    def ClassDiagram_Company61(self):
        return self.__ClassDiagram_Company61

    @ClassDiagram_Company61.setter
    def ClassDiagram_Company61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassDiagram_Company__ClassDiagram_Company61", None)
        self.__ClassDiagram_Company61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDiagram_HotelAdministration"):
                opp_val = getattr(old_value, "ClassDiagram_HotelAdministration", None)
                if opp_val == self:
                    setattr(old_value, "ClassDiagram_HotelAdministration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDiagram_HotelAdministration"):
                opp_val = getattr(value, "ClassDiagram_HotelAdministration", None)
                setattr(value, "ClassDiagram_HotelAdministration", self)

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
                    
