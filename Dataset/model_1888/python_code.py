from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PaymentMethod(Enum):
    bankcard = "bankcard"
    cash = "cash"
    voucher = "voucher"
class GuestTypes(Enum):
    Regular = "Regular"
    BlackListed = "BlackListed"
    VIP = "VIP"


############################################
# Definition of Classes
############################################

class IBookingProvidesForHost:

    pass
class IBookingProvidesForGuest:

    pass
class IBookingProvidesForCustomer:

    pass
class bookingmodel_BookingProvides(IBookingProvidesForHost, IBookingProvidesForCustomer, IBookingProvidesForGuest):

    def __init__(self, bookingmodel_BookingProvides: "bookingmodel_BookingHandler" = None):
        self.bookingmodel_BookingProvides = bookingmodel_BookingProvides
        
    @property
    def bookingmodel_BookingProvides(self):
        return self.__bookingmodel_BookingProvides

    @bookingmodel_BookingProvides.setter
    def bookingmodel_BookingProvides(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingProvides__bookingmodel_BookingProvides", None)
        self.__bookingmodel_BookingProvides = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingHandler22"):
                opp_val = getattr(old_value, "bookingmodel_BookingHandler22", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_BookingHandler22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingHandler22"):
                opp_val = getattr(value, "bookingmodel_BookingHandler22", None)
                setattr(value, "bookingmodel_BookingHandler22", self)

    def stringToList(self, text: str) -> str:
        # TODO: Implement stringToList method
        pass

class bookingmodel_IBookingProvidesForGuest(ABC):

    def __init__(self):
        
    def checkOut(self, roomID: str) -> str:
        # TODO: Implement checkOut method
        pass

    def removeExtra(self, extraIDs: str, roomID: str) -> str:
        # TODO: Implement removeExtra method
        pass

    def payExtra(self, lastName: str, extra: str, expYear: str, ccNumber: str, ccv: str, firstName: str, roomID: str, expMonth: str) -> str:
        # TODO: Implement payExtra method
        pass

    def payRoom(self, firstName: str, lastName: str, roomID: str, ccNumber: str, expYear: str, expMonth: str, ccv: str) -> str:
        # TODO: Implement payRoom method
        pass

    def checkIn(self, bookingRef: str, guestEmail: str, roomType: str) -> str:
        # TODO: Implement checkIn method
        pass

    def addExtra(self, roomID: str, extraIDs: str) -> str:
        # TODO: Implement addExtra method
        pass

class bookingmodel_CustomerInfo(ABC):

    def __init__(self):
        
    def getExpYear(self, bookingRef: str) -> str:
        # TODO: Implement getExpYear method
        pass

    def getCardFirstName(self, bookingRef: str) -> str:
        # TODO: Implement getCardFirstName method
        pass

    def getCcNr(self, bookingRef: str) -> str:
        # TODO: Implement getCcNr method
        pass

    def getCustomerAge(self, bookingRef: str) -> str:
        # TODO: Implement getCustomerAge method
        pass

    def getCcV(self, bookingRef: str) -> str:
        # TODO: Implement getCcV method
        pass

    def getCardLastName(self, bookingRef: str) -> str:
        # TODO: Implement getCardLastName method
        pass

    def getExpMonth(self, bookingRef: str) -> str:
        # TODO: Implement getExpMonth method
        pass

    def getCustomerLastName(self, bookingRef: str) -> str:
        # TODO: Implement getCustomerLastName method
        pass

    def getCustomerName(self, bookingRef: str) -> str:
        # TODO: Implement getCustomerName method
        pass

    def getCustomerEmail(self, bookingRef: str) -> str:
        # TODO: Implement getCustomerEmail method
        pass

class bookingmodel_BookingInfo(ABC):

    def __init__(self):
        
    def getBookingRef(self, customerEmail: str) -> str:
        # TODO: Implement getBookingRef method
        pass

    def getRooms(self, bookingRef: str) -> str:
        # TODO: Implement getRooms method
        pass

    def getRoomTypes(self, bookingRef: str) -> str:
        # TODO: Implement getRoomTypes method
        pass

    def getServiceNotes(self, bookingRef: str) -> str:
        # TODO: Implement getServiceNotes method
        pass

    def getNrOfGuests(self, bookingRef: str) -> str:
        # TODO: Implement getNrOfGuests method
        pass

    def getExtras(self, bookingRef: str) -> str:
        # TODO: Implement getExtras method
        pass

    def getStartDate(self, bookingRef: str) -> str:
        # TODO: Implement getStartDate method
        pass

    def getPaymentMethod(self, bookingRef: str) -> str:
        # TODO: Implement getPaymentMethod method
        pass

    def getEndDate(self, bookingRef: str) -> str:
        # TODO: Implement getEndDate method
        pass

class CustomerInfo:

    pass
class BookingInfo:

    pass
class bookingmodel_IBookingProvidesForCustomer(CustomerInfo, BookingInfo):

    def __init__(self):
        
    def removeBooking(self, bookingRef: str) -> str:
        # TODO: Implement removeBooking method
        pass

    def book(self, roomTypes: str, nrOfGuests: str, startDate: str, extras: str, endDate: str, services: str) -> str:
        # TODO: Implement book method
        pass

    def addExtra(self, extraID: str, bookingRef: str) -> str:
        # TODO: Implement addExtra method
        pass

    def editBooking(self, extras: str, bookingRef: str, services: str, startDate: str, nrOfGuests: str, endDate: str, roomTypes: str) -> str:
        # TODO: Implement editBooking method
        pass

    def getPrice(self, bookingRef: str) -> str:
        # TODO: Implement getPrice method
        pass

    def setPaymentMethod(self, bookingRef: str, method: str) -> str:
        # TODO: Implement setPaymentMethod method
        pass

    def editPaymentDetails(self, ccv: str, bookingRef: str, firstName: str, expiryYear: str, customerEmail: str, ccNumber: str, lastName: str, expiryMonth: str) -> str:
        # TODO: Implement editPaymentDetails method
        pass

    def payBooking(self, bookingRef: str) -> str:
        # TODO: Implement payBooking method
        pass

    def setPaymentDetails(self, expiryMonth: str, expiryYear: str, lastName: str, bookingRef: str, customerEmail: str, ccv: str, firstName: str, ccNumber: str) -> str:
        # TODO: Implement setPaymentDetails method
        pass

    def removeExtra(self, roomID: str, extraID: str) -> str:
        # TODO: Implement removeExtra method
        pass

    def setPersonalDetails(self, bookingRef: str, email: str, firstName: str, lastName: str, age: str) -> str:
        # TODO: Implement setPersonalDetails method
        pass

class bookingmodel_IBookingProvidesForHost(ABC):

    def __init__(self):
        
    def isCheckedIn(self, roomID: str) -> str:
        # TODO: Implement isCheckedIn method
        pass

    def removeServiceNotes(self, roomID: str, serviceNote: str) -> str:
        # TODO: Implement removeServiceNotes method
        pass

    def isRoomPayed(self, roomID: str) -> str:
        # TODO: Implement isRoomPayed method
        pass

    def getExistingBookings(self) -> str:
        # TODO: Implement getExistingBookings method
        pass

    def getRoomID(self, guestEmail: str) -> str:
        # TODO: Implement getRoomID method
        pass

    def isExtraPayed(self, roomID: str) -> str:
        # TODO: Implement isExtraPayed method
        pass

    def isBookingPayed(self, bookingRef: str) -> str:
        # TODO: Implement isBookingPayed method
        pass

    def isCheckedOut(self, roomID: str) -> str:
        # TODO: Implement isCheckedOut method
        pass

    def addServiceNotes(self, serviceNote: str, roomID: str) -> str:
        # TODO: Implement addServiceNotes method
        pass

    def getResponsibleGuest(self, roomID: str) -> str:
        # TODO: Implement getResponsibleGuest method
        pass

    def existBooking(self, bookingRef: str) -> str:
        # TODO: Implement existBooking method
        pass

class bookingmodel_RoomIDToBookingRefEntry:

    def __init__(self, key: str, value: str, bookingmodel_RoomIDToBookingRefEntry: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.value = value
        self.bookingmodel_RoomIDToBookingRefEntry = bookingmodel_RoomIDToBookingRefEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bookingmodel_RoomIDToBookingRefEntry(self):
        return self.__bookingmodel_RoomIDToBookingRefEntry

    @bookingmodel_RoomIDToBookingRefEntry.setter
    def bookingmodel_RoomIDToBookingRefEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_RoomIDToBookingRefEntry__bookingmodel_RoomIDToBookingRefEntry", None)
        self.__bookingmodel_RoomIDToBookingRefEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingHandler16"):
                opp_val = getattr(old_value, "bookingmodel_BookingHandler16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingHandler16"):
                opp_val = getattr(value, "bookingmodel_BookingHandler16", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_BookingHandler16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_GuestEmailToRoomIDEntry:

    def __init__(self, key: str, value: int, bookingmodel_GuestEmailToRoomIDEntry: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.value = value
        self.bookingmodel_GuestEmailToRoomIDEntry = bookingmodel_GuestEmailToRoomIDEntry
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bookingmodel_GuestEmailToRoomIDEntry(self):
        return self.__bookingmodel_GuestEmailToRoomIDEntry

    @bookingmodel_GuestEmailToRoomIDEntry.setter
    def bookingmodel_GuestEmailToRoomIDEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_GuestEmailToRoomIDEntry__bookingmodel_GuestEmailToRoomIDEntry", None)
        self.__bookingmodel_GuestEmailToRoomIDEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingHandler20"):
                opp_val = getattr(old_value, "bookingmodel_BookingHandler20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingHandler20"):
                opp_val = getattr(value, "bookingmodel_BookingHandler20", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_BookingHandler20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_CustomerEmailToBookingRefEntry:

    def __init__(self, key: str, value: str, bookingmodel_CustomerEmailToBookingRefEntry: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.value = value
        self.bookingmodel_CustomerEmailToBookingRefEntry = bookingmodel_CustomerEmailToBookingRefEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bookingmodel_CustomerEmailToBookingRefEntry(self):
        return self.__bookingmodel_CustomerEmailToBookingRefEntry

    @bookingmodel_CustomerEmailToBookingRefEntry.setter
    def bookingmodel_CustomerEmailToBookingRefEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_CustomerEmailToBookingRefEntry__bookingmodel_CustomerEmailToBookingRefEntry", None)
        self.__bookingmodel_CustomerEmailToBookingRefEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingHandler18"):
                opp_val = getattr(old_value, "bookingmodel_BookingHandler18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingHandler18"):
                opp_val = getattr(value, "bookingmodel_BookingHandler18", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_BookingHandler18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_BookingHandler:

    def __init__(self, bookingmodel_BookingHandler18: set["bookingmodel_CustomerEmailToBookingRefEntry"] = None, bookingmodel_BookingHandler20: set["bookingmodel_GuestEmailToRoomIDEntry"] = None, bookingmodel_BookingHandler: set["bookingmodel_BookingRefToBookingEntry"] = None, bookingmodel_BookingHandler16: set["bookingmodel_RoomIDToBookingRefEntry"] = None, bookingmodel_BookingHandler22: "bookingmodel_BookingProvides" = None):
        self.bookingmodel_BookingHandler18 = bookingmodel_BookingHandler18 if bookingmodel_BookingHandler18 is not None else set()
        self.bookingmodel_BookingHandler20 = bookingmodel_BookingHandler20 if bookingmodel_BookingHandler20 is not None else set()
        self.bookingmodel_BookingHandler = bookingmodel_BookingHandler if bookingmodel_BookingHandler is not None else set()
        self.bookingmodel_BookingHandler16 = bookingmodel_BookingHandler16 if bookingmodel_BookingHandler16 is not None else set()
        self.bookingmodel_BookingHandler22 = bookingmodel_BookingHandler22
        
    @property
    def bookingmodel_BookingHandler18(self):
        return self.__bookingmodel_BookingHandler18

    @bookingmodel_BookingHandler18.setter
    def bookingmodel_BookingHandler18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingHandler__bookingmodel_BookingHandler18", None)
        self.__bookingmodel_BookingHandler18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_CustomerEmailToBookingRefEntry"):
                    opp_val = getattr(item, "bookingmodel_CustomerEmailToBookingRefEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_CustomerEmailToBookingRefEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_CustomerEmailToBookingRefEntry"):
                    opp_val = getattr(item, "bookingmodel_CustomerEmailToBookingRefEntry", None)
                    
                    setattr(item, "bookingmodel_CustomerEmailToBookingRefEntry", self)
                    

    @property
    def bookingmodel_BookingHandler22(self):
        return self.__bookingmodel_BookingHandler22

    @bookingmodel_BookingHandler22.setter
    def bookingmodel_BookingHandler22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingHandler__bookingmodel_BookingHandler22", None)
        self.__bookingmodel_BookingHandler22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingProvides"):
                opp_val = getattr(old_value, "bookingmodel_BookingProvides", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_BookingProvides", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingProvides"):
                opp_val = getattr(value, "bookingmodel_BookingProvides", None)
                setattr(value, "bookingmodel_BookingProvides", self)

    @property
    def bookingmodel_BookingHandler20(self):
        return self.__bookingmodel_BookingHandler20

    @bookingmodel_BookingHandler20.setter
    def bookingmodel_BookingHandler20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingHandler__bookingmodel_BookingHandler20", None)
        self.__bookingmodel_BookingHandler20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_GuestEmailToRoomIDEntry"):
                    opp_val = getattr(item, "bookingmodel_GuestEmailToRoomIDEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_GuestEmailToRoomIDEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_GuestEmailToRoomIDEntry"):
                    opp_val = getattr(item, "bookingmodel_GuestEmailToRoomIDEntry", None)
                    
                    setattr(item, "bookingmodel_GuestEmailToRoomIDEntry", self)
                    

    @property
    def bookingmodel_BookingHandler16(self):
        return self.__bookingmodel_BookingHandler16

    @bookingmodel_BookingHandler16.setter
    def bookingmodel_BookingHandler16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingHandler__bookingmodel_BookingHandler16", None)
        self.__bookingmodel_BookingHandler16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_RoomIDToBookingRefEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomIDToBookingRefEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_RoomIDToBookingRefEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_RoomIDToBookingRefEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomIDToBookingRefEntry", None)
                    
                    setattr(item, "bookingmodel_RoomIDToBookingRefEntry", self)
                    

    @property
    def bookingmodel_BookingHandler(self):
        return self.__bookingmodel_BookingHandler

    @bookingmodel_BookingHandler.setter
    def bookingmodel_BookingHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingHandler__bookingmodel_BookingHandler", None)
        self.__bookingmodel_BookingHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_BookingRefToBookingEntry14"):
                    opp_val = getattr(item, "bookingmodel_BookingRefToBookingEntry14", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_BookingRefToBookingEntry14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_BookingRefToBookingEntry14"):
                    opp_val = getattr(item, "bookingmodel_BookingRefToBookingEntry14", None)
                    
                    setattr(item, "bookingmodel_BookingRefToBookingEntry14", self)
                    

    def exists(self, bookingRef: str) -> str:
        # TODO: Implement exists method
        pass

    def removeBooking(self, bookingRef: str) -> str:
        # TODO: Implement removeBooking method
        pass

    def getBooking(self, bookingRef: str) -> str:
        # TODO: Implement getBooking method
        pass

    def addBooking(self, services: str, roomTypes: str, extras: str, startDate: str, nrOfGuests: str, endDate: str) -> str:
        # TODO: Implement addBooking method
        pass

    def isActive(self, bookingRef: str) -> str:
        # TODO: Implement isActive method
        pass

    def editBooking(self, bookingRef: str, startDate: str, roomTypes: str, nrOfGuests: str, extras: str, services: str, endDate: str) -> str:
        # TODO: Implement editBooking method
        pass

    def getBooking(self, roomID: str) -> str:
        # TODO: Implement getBooking method
        pass

class Person:

    pass
class bookingmodel_ExtraToIsPayedEntry:

    def __init__(self, key: str, value: str, bookingmodel_ExtraToIsPayedEntry: "bookingmodel_Booking" = None):
        self.key = key
        self.value = value
        self.bookingmodel_ExtraToIsPayedEntry = bookingmodel_ExtraToIsPayedEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bookingmodel_ExtraToIsPayedEntry(self):
        return self.__bookingmodel_ExtraToIsPayedEntry

    @bookingmodel_ExtraToIsPayedEntry.setter
    def bookingmodel_ExtraToIsPayedEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_ExtraToIsPayedEntry__bookingmodel_ExtraToIsPayedEntry", None)
        self.__bookingmodel_ExtraToIsPayedEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Booking10"):
                opp_val = getattr(old_value, "bookingmodel_Booking10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Booking10"):
                opp_val = getattr(value, "bookingmodel_Booking10", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_Booking10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_Guest(Person):

    def __init__(self, guestTypes: str, roomNr: str, bookingmodel_Guest: "bookingmodel_Booking" = None):
        self.guestTypes = guestTypes
        self.roomNr = roomNr
        self.bookingmodel_Guest = bookingmodel_Guest
        
    @property
    def guestTypes(self) -> str:
        return self.__guestTypes

    @guestTypes.setter
    def guestTypes(self, guestTypes: str):
        self.__guestTypes = guestTypes

    @property
    def roomNr(self) -> str:
        return self.__roomNr

    @roomNr.setter
    def roomNr(self, roomNr: str):
        self.__roomNr = roomNr

    @property
    def bookingmodel_Guest(self):
        return self.__bookingmodel_Guest

    @bookingmodel_Guest.setter
    def bookingmodel_Guest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Guest__bookingmodel_Guest", None)
        self.__bookingmodel_Guest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Booking4"):
                opp_val = getattr(old_value, "bookingmodel_Booking4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Booking4"):
                opp_val = getattr(value, "bookingmodel_Booking4", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_Booking4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_Person(ABC):

    def __init__(self, firstName: str, lastName: str, email: str, telephoneNr: str, Address: str, age: str):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.telephoneNr = telephoneNr
        self.Address = Address
        self.age = age
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def telephoneNr(self) -> str:
        return self.__telephoneNr

    @telephoneNr.setter
    def telephoneNr(self, telephoneNr: str):
        self.__telephoneNr = telephoneNr

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Address(self) -> str:
        return self.__Address

    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

class bookingmodel_PaymentDetails:

    def __init__(self, ccNr: str, ccV: str, expMonth: str, expYear: str, firstName: str, lastName: str, bookingmodel_PaymentDetails: "bookingmodel_Customer" = None):
        self.ccNr = ccNr
        self.ccV = ccV
        self.expMonth = expMonth
        self.expYear = expYear
        self.firstName = firstName
        self.lastName = lastName
        self.bookingmodel_PaymentDetails = bookingmodel_PaymentDetails
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def expMonth(self) -> str:
        return self.__expMonth

    @expMonth.setter
    def expMonth(self, expMonth: str):
        self.__expMonth = expMonth

    @property
    def expYear(self) -> str:
        return self.__expYear

    @expYear.setter
    def expYear(self, expYear: str):
        self.__expYear = expYear

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def ccV(self) -> str:
        return self.__ccV

    @ccV.setter
    def ccV(self, ccV: str):
        self.__ccV = ccV

    @property
    def ccNr(self) -> str:
        return self.__ccNr

    @ccNr.setter
    def ccNr(self, ccNr: str):
        self.__ccNr = ccNr

    @property
    def bookingmodel_PaymentDetails(self):
        return self.__bookingmodel_PaymentDetails

    @bookingmodel_PaymentDetails.setter
    def bookingmodel_PaymentDetails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_PaymentDetails__bookingmodel_PaymentDetails", None)
        self.__bookingmodel_PaymentDetails = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Customer12"):
                opp_val = getattr(old_value, "bookingmodel_Customer12", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_Customer12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Customer12"):
                opp_val = getattr(value, "bookingmodel_Customer12", None)
                setattr(value, "bookingmodel_Customer12", self)

class bookingmodel_Customer(Person):

    pass
class bookingmodel_BookingRefToBookingEntry:

    def __init__(self, key: str, bookingmodel_BookingRefToBookingEntry: "bookingmodel_Booking" = None, bookingmodel_BookingRefToBookingEntry14: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.bookingmodel_BookingRefToBookingEntry = bookingmodel_BookingRefToBookingEntry
        self.bookingmodel_BookingRefToBookingEntry14 = bookingmodel_BookingRefToBookingEntry14
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bookingmodel_BookingRefToBookingEntry(self):
        return self.__bookingmodel_BookingRefToBookingEntry

    @bookingmodel_BookingRefToBookingEntry.setter
    def bookingmodel_BookingRefToBookingEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingRefToBookingEntry__bookingmodel_BookingRefToBookingEntry", None)
        self.__bookingmodel_BookingRefToBookingEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Booking"):
                opp_val = getattr(old_value, "bookingmodel_Booking", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Booking"):
                opp_val = getattr(value, "bookingmodel_Booking", None)
                setattr(value, "bookingmodel_Booking", self)

    @property
    def bookingmodel_BookingRefToBookingEntry14(self):
        return self.__bookingmodel_BookingRefToBookingEntry14

    @bookingmodel_BookingRefToBookingEntry14.setter
    def bookingmodel_BookingRefToBookingEntry14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_BookingRefToBookingEntry__bookingmodel_BookingRefToBookingEntry14", None)
        self.__bookingmodel_BookingRefToBookingEntry14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingHandler"):
                opp_val = getattr(old_value, "bookingmodel_BookingHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingHandler"):
                opp_val = getattr(value, "bookingmodel_BookingHandler", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_BookingHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_RoomIDToRoomTypeEntry:

    def __init__(self, key: str, value: str, bookingmodel_RoomIDToRoomTypeEntry: "bookingmodel_Booking" = None):
        self.key = key
        self.value = value
        self.bookingmodel_RoomIDToRoomTypeEntry = bookingmodel_RoomIDToRoomTypeEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def bookingmodel_RoomIDToRoomTypeEntry(self):
        return self.__bookingmodel_RoomIDToRoomTypeEntry

    @bookingmodel_RoomIDToRoomTypeEntry.setter
    def bookingmodel_RoomIDToRoomTypeEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_RoomIDToRoomTypeEntry__bookingmodel_RoomIDToRoomTypeEntry", None)
        self.__bookingmodel_RoomIDToRoomTypeEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Booking8"):
                opp_val = getattr(old_value, "bookingmodel_Booking8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Booking8"):
                opp_val = getattr(value, "bookingmodel_Booking8", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_Booking8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_RoomToGuestIDEntry:

    def __init__(self, key: str, value: str, bookingmodel_RoomToGuestIDEntry: "bookingmodel_Booking" = None):
        self.key = key
        self.value = value
        self.bookingmodel_RoomToGuestIDEntry = bookingmodel_RoomToGuestIDEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bookingmodel_RoomToGuestIDEntry(self):
        return self.__bookingmodel_RoomToGuestIDEntry

    @bookingmodel_RoomToGuestIDEntry.setter
    def bookingmodel_RoomToGuestIDEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_RoomToGuestIDEntry__bookingmodel_RoomToGuestIDEntry", None)
        self.__bookingmodel_RoomToGuestIDEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Booking6"):
                opp_val = getattr(old_value, "bookingmodel_Booking6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Booking6"):
                opp_val = getattr(value, "bookingmodel_Booking6", None)
                if opp_val is None:
                    setattr(value, "bookingmodel_Booking6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookingmodel_Booking:

    def __init__(self, startDate: str, endDate: str, serviceNotes: str, nrOfGuests: str, bookingRef: str, isPayed: str, paymentMethod: str, bookingmodel_Booking: "bookingmodel_BookingRefToBookingEntry" = None, bookingmodel_Booking2: "bookingmodel_Customer" = None, bookingmodel_Booking4: set["bookingmodel_Guest"] = None, bookingmodel_Booking6: set["bookingmodel_RoomToGuestIDEntry"] = None, bookingmodel_Booking8: set["bookingmodel_RoomIDToRoomTypeEntry"] = None, bookingmodel_Booking10: set["bookingmodel_ExtraToIsPayedEntry"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.serviceNotes = serviceNotes
        self.nrOfGuests = nrOfGuests
        self.bookingRef = bookingRef
        self.isPayed = isPayed
        self.paymentMethod = paymentMethod
        self.bookingmodel_Booking = bookingmodel_Booking
        self.bookingmodel_Booking2 = bookingmodel_Booking2
        self.bookingmodel_Booking4 = bookingmodel_Booking4 if bookingmodel_Booking4 is not None else set()
        self.bookingmodel_Booking6 = bookingmodel_Booking6 if bookingmodel_Booking6 is not None else set()
        self.bookingmodel_Booking8 = bookingmodel_Booking8 if bookingmodel_Booking8 is not None else set()
        self.bookingmodel_Booking10 = bookingmodel_Booking10 if bookingmodel_Booking10 is not None else set()
        
    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def serviceNotes(self) -> str:
        return self.__serviceNotes

    @serviceNotes.setter
    def serviceNotes(self, serviceNotes: str):
        self.__serviceNotes = serviceNotes

    @property
    def isPayed(self) -> str:
        return self.__isPayed

    @isPayed.setter
    def isPayed(self, isPayed: str):
        self.__isPayed = isPayed

    @property
    def nrOfGuests(self) -> str:
        return self.__nrOfGuests

    @nrOfGuests.setter
    def nrOfGuests(self, nrOfGuests: str):
        self.__nrOfGuests = nrOfGuests

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def paymentMethod(self) -> str:
        return self.__paymentMethod

    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: str):
        self.__paymentMethod = paymentMethod

    @property
    def bookingRef(self) -> str:
        return self.__bookingRef

    @bookingRef.setter
    def bookingRef(self, bookingRef: str):
        self.__bookingRef = bookingRef

    @property
    def bookingmodel_Booking(self):
        return self.__bookingmodel_Booking

    @bookingmodel_Booking.setter
    def bookingmodel_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking", None)
        self.__bookingmodel_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_BookingRefToBookingEntry"):
                opp_val = getattr(old_value, "bookingmodel_BookingRefToBookingEntry", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_BookingRefToBookingEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_BookingRefToBookingEntry"):
                opp_val = getattr(value, "bookingmodel_BookingRefToBookingEntry", None)
                setattr(value, "bookingmodel_BookingRefToBookingEntry", self)

    @property
    def bookingmodel_Booking6(self):
        return self.__bookingmodel_Booking6

    @bookingmodel_Booking6.setter
    def bookingmodel_Booking6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking6", None)
        self.__bookingmodel_Booking6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_RoomToGuestIDEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomToGuestIDEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_RoomToGuestIDEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_RoomToGuestIDEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomToGuestIDEntry", None)
                    
                    setattr(item, "bookingmodel_RoomToGuestIDEntry", self)
                    

    @property
    def bookingmodel_Booking4(self):
        return self.__bookingmodel_Booking4

    @bookingmodel_Booking4.setter
    def bookingmodel_Booking4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking4", None)
        self.__bookingmodel_Booking4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_Guest"):
                    opp_val = getattr(item, "bookingmodel_Guest", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_Guest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_Guest"):
                    opp_val = getattr(item, "bookingmodel_Guest", None)
                    
                    setattr(item, "bookingmodel_Guest", self)
                    

    @property
    def bookingmodel_Booking2(self):
        return self.__bookingmodel_Booking2

    @bookingmodel_Booking2.setter
    def bookingmodel_Booking2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking2", None)
        self.__bookingmodel_Booking2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookingmodel_Customer"):
                opp_val = getattr(old_value, "bookingmodel_Customer", None)
                if opp_val == self:
                    setattr(old_value, "bookingmodel_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookingmodel_Customer"):
                opp_val = getattr(value, "bookingmodel_Customer", None)
                setattr(value, "bookingmodel_Customer", self)

    @property
    def bookingmodel_Booking10(self):
        return self.__bookingmodel_Booking10

    @bookingmodel_Booking10.setter
    def bookingmodel_Booking10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking10", None)
        self.__bookingmodel_Booking10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_ExtraToIsPayedEntry"):
                    opp_val = getattr(item, "bookingmodel_ExtraToIsPayedEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_ExtraToIsPayedEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_ExtraToIsPayedEntry"):
                    opp_val = getattr(item, "bookingmodel_ExtraToIsPayedEntry", None)
                    
                    setattr(item, "bookingmodel_ExtraToIsPayedEntry", self)
                    

    @property
    def bookingmodel_Booking8(self):
        return self.__bookingmodel_Booking8

    @bookingmodel_Booking8.setter
    def bookingmodel_Booking8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookingmodel_Booking__bookingmodel_Booking8", None)
        self.__bookingmodel_Booking8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingmodel_RoomIDToRoomTypeEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomIDToRoomTypeEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingmodel_RoomIDToRoomTypeEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingmodel_RoomIDToRoomTypeEntry"):
                    opp_val = getattr(item, "bookingmodel_RoomIDToRoomTypeEntry", None)
                    
                    setattr(item, "bookingmodel_RoomIDToRoomTypeEntry", self)
                    

    def checkedOutAllRooms(self) -> str:
        # TODO: Implement checkedOutAllRooms method
        pass

    def checkedInRoom(self, roomID: str) -> str:
        # TODO: Implement checkedInRoom method
        pass

    def getExtras(self) -> str:
        # TODO: Implement getExtras method
        pass

    def checkedOutRoom(self, roomID: str) -> str:
        # TODO: Implement checkedOutRoom method
        pass

    def getRoomIDs(self) -> str:
        # TODO: Implement getRoomIDs method
        pass

    def removeResponsibleGuest(self, roomID: str, guestEmail: str) -> str:
        # TODO: Implement removeResponsibleGuest method
        pass

    def setExtras(self, extras: str) -> str:
        # TODO: Implement setExtras method
        pass

    def removeServiceNotes(self, serviceNotes: str) -> str:
        # TODO: Implement removeServiceNotes method
        pass

    def allExtrasPayed(self) -> str:
        # TODO: Implement allExtrasPayed method
        pass

    def getRoomTypes(self) -> str:
        # TODO: Implement getRoomTypes method
        pass

    def setServiceNotes(self, services: str) -> str:
        # TODO: Implement setServiceNotes method
        pass

    def setRoomIDs(self, roomIDs: str) -> str:
        # TODO: Implement setRoomIDs method
        pass

    def setExtrasAsPayed(self, extras: str) -> str:
        # TODO: Implement setExtrasAsPayed method
        pass

    def checkedInAllRooms(self) -> str:
        # TODO: Implement checkedInAllRooms method
        pass

    def setRoomTypes(self, roomTypes: str) -> str:
        # TODO: Implement setRoomTypes method
        pass

    def isExtraPayed(self, extra: str) -> str:
        # TODO: Implement isExtraPayed method
        pass

    def getUnPayedExtras(self) -> str:
        # TODO: Implement getUnPayedExtras method
        pass

    def removeResponsibleGuestToAllRooms(self, guestEmail: str) -> str:
        # TODO: Implement removeResponsibleGuestToAllRooms method
        pass

    def setResponsibleGuestToAllRooms(self, guestEmail: str) -> str:
        # TODO: Implement setResponsibleGuestToAllRooms method
        pass

    def setResponsibleGuest(self, guestEmail: str, roomID: str) -> str:
        # TODO: Implement setResponsibleGuest method
        pass

    def getNrOfRooms(self) -> str:
        # TODO: Implement getNrOfRooms method
        pass
