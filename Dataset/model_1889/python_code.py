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
class bookingmodel_BookingProvides(IBookingProvidesForCustomer, IBookingProvidesForHost, IBookingProvidesForGuest):

    def __init__(self, bookingmodel_BookingProvides: "bookingmodel_BookingHandler" = None):
        self.bookingmodel_BookingProvides = bookingmodel_BookingProvides
        
        pass
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

    def stringToList(self, bookingmodel_text) :
        # TODO: Implement stringToList method
        pass

class bookingmodel_IBookingProvidesForGuest(ABC):

    def __init__(self):
        
        pass
    def payRoom(self, bookingmodel_roomID, bookingmodel_expYear, bookingmodel_expMonth, bookingmodel_firstName, bookingmodel_ccv, bookingmodel_ccNumber, bookingmodel_lastName) :
        # TODO: Implement payRoom method
        pass

    def checkIn(self, bookingmodel_guestEmail, bookingmodel_roomType, bookingmodel_bookingRef) :
        # TODO: Implement checkIn method
        pass

    def checkOut(self, bookingmodel_roomID) :
        # TODO: Implement checkOut method
        pass

    def addExtra(self, bookingmodel_roomID, bookingmodel_extraIDs) :
        # TODO: Implement addExtra method
        pass

    def payExtra(self, bookingmodel_ccNumber, bookingmodel_expMonth, bookingmodel_expYear, bookingmodel_firstName, bookingmodel_extra, bookingmodel_lastName, bookingmodel_roomID, bookingmodel_ccv) :
        # TODO: Implement payExtra method
        pass

    def removeExtra(self, bookingmodel_roomID, bookingmodel_extraIDs) :
        # TODO: Implement removeExtra method
        pass

class bookingmodel_CustomerInfo(ABC):

    def __init__(self):
        
        pass
    def getCustomerAge(self, bookingmodel_bookingRef) :
        # TODO: Implement getCustomerAge method
        pass

    def getCardFirstName(self, bookingmodel_bookingRef) :
        # TODO: Implement getCardFirstName method
        pass

    def getCustomerEmail(self, bookingmodel_bookingRef) :
        # TODO: Implement getCustomerEmail method
        pass

    def getCcNr(self, bookingmodel_bookingRef) :
        # TODO: Implement getCcNr method
        pass

    def getCardLastName(self, bookingmodel_bookingRef) :
        # TODO: Implement getCardLastName method
        pass

    def getCcV(self, bookingmodel_bookingRef) :
        # TODO: Implement getCcV method
        pass

    def getCustomerName(self, bookingmodel_bookingRef) :
        # TODO: Implement getCustomerName method
        pass

    def getCustomerLastName(self, bookingmodel_bookingRef) :
        # TODO: Implement getCustomerLastName method
        pass

    def getExpYear(self, bookingmodel_bookingRef) :
        # TODO: Implement getExpYear method
        pass

    def getExpMonth(self, bookingmodel_bookingRef) :
        # TODO: Implement getExpMonth method
        pass

class bookingmodel_BookingInfo(ABC):

    def __init__(self):
        
        pass
    def getStartDate(self, bookingmodel_bookingRef) :
        # TODO: Implement getStartDate method
        pass

    def getRoomTypes(self, bookingmodel_bookingRef) :
        # TODO: Implement getRoomTypes method
        pass

    def getServiceNotes(self, bookingmodel_bookingRef) :
        # TODO: Implement getServiceNotes method
        pass

    def getBookingRef(self, bookingmodel_customerEmail) :
        # TODO: Implement getBookingRef method
        pass

    def getPaymentMethod(self, bookingmodel_bookingRef) :
        # TODO: Implement getPaymentMethod method
        pass

    def getNrOfGuests(self, bookingmodel_bookingRef) :
        # TODO: Implement getNrOfGuests method
        pass

    def getExtras(self, bookingmodel_bookingRef) :
        # TODO: Implement getExtras method
        pass

    def getRooms(self, bookingmodel_bookingRef) :
        # TODO: Implement getRooms method
        pass

    def getEndDate(self, bookingmodel_bookingRef) :
        # TODO: Implement getEndDate method
        pass

class CustomerInfo:

    pass
class BookingInfo:

    pass
class bookingmodel_IBookingProvidesForCustomer(CustomerInfo, BookingInfo):

    def __init__(self):
        
        pass
    def payBooking(self, bookingmodel_bookingRef) :
        # TODO: Implement payBooking method
        pass

    def setPaymentMethod(self, bookingmodel_method, bookingmodel_bookingRef) :
        # TODO: Implement setPaymentMethod method
        pass

    def editBooking(self, bookingmodel_extras, bookingmodel_endDate, bookingmodel_nrOfGuests, bookingmodel_startDate, bookingmodel_services, bookingmodel_roomTypes, bookingmodel_bookingRef) :
        # TODO: Implement editBooking method
        pass

    def getPrice(self, bookingmodel_bookingRef) :
        # TODO: Implement getPrice method
        pass

    def removeExtra(self, bookingmodel_roomID, bookingmodel_extraID) :
        # TODO: Implement removeExtra method
        pass

    def addExtra(self, bookingmodel_bookingRef, bookingmodel_extraID) :
        # TODO: Implement addExtra method
        pass

    def setPersonalDetails(self, bookingmodel_bookingRef, bookingmodel_firstName, bookingmodel_email, bookingmodel_age, bookingmodel_lastName) :
        # TODO: Implement setPersonalDetails method
        pass

    def book(self, bookingmodel_extras, bookingmodel_nrOfGuests, bookingmodel_endDate, bookingmodel_roomTypes, bookingmodel_services, bookingmodel_startDate) :
        # TODO: Implement book method
        pass

    def editPaymentDetails(self, bookingmodel_ccv, bookingmodel_customerEmail, bookingmodel_lastName, bookingmodel_bookingRef, bookingmodel_expiryYear, bookingmodel_firstName, bookingmodel_ccNumber, bookingmodel_expiryMonth) :
        # TODO: Implement editPaymentDetails method
        pass

    def removeBooking(self, bookingmodel_bookingRef) :
        # TODO: Implement removeBooking method
        pass

    def setPaymentDetails(self, bookingmodel_customerEmail, bookingmodel_bookingRef, bookingmodel_expiryMonth, bookingmodel_expiryYear, bookingmodel_ccv, bookingmodel_ccNumber, bookingmodel_firstName, bookingmodel_lastName) :
        # TODO: Implement setPaymentDetails method
        pass

class bookingmodel_GuestEmailToRoomIDEntry:

    def __init__(self, key: str, value: int, bookingmodel_GuestEmailToRoomIDEntry: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.value = value
        self.bookingmodel_GuestEmailToRoomIDEntry = bookingmodel_GuestEmailToRoomIDEntry
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def key(self):
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
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
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

class bookingmodel_RoomIDToBookingRefEntry:

    def __init__(self, value: str, key: str, bookingmodel_RoomIDToBookingRefEntry: "bookingmodel_BookingHandler" = None):
        self.value = value
        self.key = key
        self.bookingmodel_RoomIDToBookingRefEntry = bookingmodel_RoomIDToBookingRefEntry
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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

class bookingmodel_IBookingProvidesForHost(ABC):

    def __init__(self):
        
        pass
    def getExistingBookings(self) :
        # TODO: Implement getExistingBookings method
        pass

    def existBooking(self, bookingmodel_bookingRef) :
        # TODO: Implement existBooking method
        pass

    def getRoomID(self, bookingmodel_guestEmail) :
        # TODO: Implement getRoomID method
        pass

    def isBookingPayed(self, bookingmodel_bookingRef) :
        # TODO: Implement isBookingPayed method
        pass

    def isRoomPayed(self, bookingmodel_roomID) :
        # TODO: Implement isRoomPayed method
        pass

    def getResponsibleGuest(self, bookingmodel_roomID) :
        # TODO: Implement getResponsibleGuest method
        pass

    def isCheckedOut(self, bookingmodel_roomID) :
        # TODO: Implement isCheckedOut method
        pass

    def removeServiceNotes(self, bookingmodel_serviceNote, bookingmodel_roomID) :
        # TODO: Implement removeServiceNotes method
        pass

    def isExtraPayed(self, bookingmodel_roomID) :
        # TODO: Implement isExtraPayed method
        pass

    def isCheckedIn(self, bookingmodel_roomID) :
        # TODO: Implement isCheckedIn method
        pass

    def addServiceNotes(self, bookingmodel_serviceNote, bookingmodel_roomID) :
        # TODO: Implement addServiceNotes method
        pass

class bookingmodel_BookingHandler:

    def __init__(self, bookingmodel_BookingHandler: set["bookingmodel_BookingRefToBookingEntry"] = None, bookingmodel_BookingHandler16: set["bookingmodel_RoomIDToBookingRefEntry"] = None, bookingmodel_BookingHandler18: set["bookingmodel_CustomerEmailToBookingRefEntry"] = None, bookingmodel_BookingHandler20: set["bookingmodel_GuestEmailToRoomIDEntry"] = None, bookingmodel_BookingHandler22: "bookingmodel_BookingProvides" = None):
        self.bookingmodel_BookingHandler = bookingmodel_BookingHandler if bookingmodel_BookingHandler is not None else set()
        self.bookingmodel_BookingHandler16 = bookingmodel_BookingHandler16 if bookingmodel_BookingHandler16 is not None else set()
        self.bookingmodel_BookingHandler18 = bookingmodel_BookingHandler18 if bookingmodel_BookingHandler18 is not None else set()
        self.bookingmodel_BookingHandler20 = bookingmodel_BookingHandler20 if bookingmodel_BookingHandler20 is not None else set()
        self.bookingmodel_BookingHandler22 = bookingmodel_BookingHandler22
        
        pass
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

    def getBooking(self, bookingmodel_roomID) :
        # TODO: Implement getBooking method
        pass

    def editBooking(self, bookingmodel_startDate, bookingmodel_nrOfGuests, bookingmodel_roomTypes, bookingmodel_bookingRef, bookingmodel_endDate, bookingmodel_extras, bookingmodel_services) :
        # TODO: Implement editBooking method
        pass

    def removeBooking(self, bookingmodel_bookingRef) :
        # TODO: Implement removeBooking method
        pass

    def addBooking(self, bookingmodel_endDate, bookingmodel_startDate, bookingmodel_roomTypes, bookingmodel_services, bookingmodel_extras, bookingmodel_nrOfGuests) :
        # TODO: Implement addBooking method
        pass

    def isActive(self, bookingmodel_bookingRef) :
        # TODO: Implement isActive method
        pass

    def exists(self, bookingmodel_bookingRef) :
        # TODO: Implement exists method
        pass

class bookingmodel_Person(ABC):

    def __init__(self, firstName: str, lastName: str, email: str, telephoneNr: str, Address: str, age: str):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.telephoneNr = telephoneNr
        self.Address = Address
        self.age = age
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def telephoneNr(self):
        return self.__telephoneNr

    @telephoneNr.setter
    def telephoneNr(self, telephoneNr: str):
        self.__telephoneNr = telephoneNr


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address


    @property
    def age(self):
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
        
        pass
    @property
    def expMonth(self):
        return self.__expMonth

    @expMonth.setter
    def expMonth(self, expMonth: str):
        self.__expMonth = expMonth


    @property
    def expYear(self):
        return self.__expYear

    @expYear.setter
    def expYear(self, expYear: str):
        self.__expYear = expYear


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def ccNr(self):
        return self.__ccNr

    @ccNr.setter
    def ccNr(self, ccNr: str):
        self.__ccNr = ccNr


    @property
    def ccV(self):
        return self.__ccV

    @ccV.setter
    def ccV(self, ccV: str):
        self.__ccV = ccV


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


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

class Person:

    pass
class bookingmodel_ExtraToIsPayedEntry:

    def __init__(self, key: str, value: str, bookingmodel_ExtraToIsPayedEntry: "bookingmodel_Booking" = None):
        self.key = key
        self.value = value
        self.bookingmodel_ExtraToIsPayedEntry = bookingmodel_ExtraToIsPayedEntry
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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

    def __init__(self, roomNr: str, guestTypes: str, bookingmodel_Guest: "bookingmodel_Booking" = None):
        self.roomNr = roomNr
        self.guestTypes = guestTypes
        self.bookingmodel_Guest = bookingmodel_Guest
        
        pass
    @property
    def guestTypes(self):
        return self.__guestTypes

    @guestTypes.setter
    def guestTypes(self, guestTypes: str):
        self.__guestTypes = guestTypes


    @property
    def roomNr(self):
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

class bookingmodel_Customer(Person):

    pass
class bookingmodel_BookingRefToBookingEntry:

    def __init__(self, key: str, bookingmodel_BookingRefToBookingEntry: "bookingmodel_Booking" = None, bookingmodel_BookingRefToBookingEntry14: "bookingmodel_BookingHandler" = None):
        self.key = key
        self.bookingmodel_BookingRefToBookingEntry = bookingmodel_BookingRefToBookingEntry
        self.bookingmodel_BookingRefToBookingEntry14 = bookingmodel_BookingRefToBookingEntry14
        
        pass
    @property
    def key(self):
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
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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

class bookingmodel_Booking:

    def __init__(self, serviceNotes: str, nrOfGuests: str, isPayed: str, paymentMethod: str, bookingRef: str, startDate: str, endDate: str, bookingmodel_Booking: "bookingmodel_BookingRefToBookingEntry" = None, bookingmodel_Booking2: "bookingmodel_Customer" = None, bookingmodel_Booking4: set["bookingmodel_Guest"] = None, bookingmodel_Booking6: set["bookingmodel_RoomToGuestIDEntry"] = None, bookingmodel_Booking8: set["bookingmodel_RoomIDToRoomTypeEntry"] = None, bookingmodel_Booking10: set["bookingmodel_ExtraToIsPayedEntry"] = None):
        self.serviceNotes = serviceNotes
        self.nrOfGuests = nrOfGuests
        self.isPayed = isPayed
        self.paymentMethod = paymentMethod
        self.bookingRef = bookingRef
        self.startDate = startDate
        self.endDate = endDate
        self.bookingmodel_Booking = bookingmodel_Booking
        self.bookingmodel_Booking2 = bookingmodel_Booking2
        self.bookingmodel_Booking4 = bookingmodel_Booking4 if bookingmodel_Booking4 is not None else set()
        self.bookingmodel_Booking6 = bookingmodel_Booking6 if bookingmodel_Booking6 is not None else set()
        self.bookingmodel_Booking8 = bookingmodel_Booking8 if bookingmodel_Booking8 is not None else set()
        self.bookingmodel_Booking10 = bookingmodel_Booking10 if bookingmodel_Booking10 is not None else set()
        
        pass
    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate


    @property
    def serviceNotes(self):
        return self.__serviceNotes

    @serviceNotes.setter
    def serviceNotes(self, serviceNotes: str):
        self.__serviceNotes = serviceNotes


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate


    @property
    def nrOfGuests(self):
        return self.__nrOfGuests

    @nrOfGuests.setter
    def nrOfGuests(self, nrOfGuests: str):
        self.__nrOfGuests = nrOfGuests


    @property
    def paymentMethod(self):
        return self.__paymentMethod

    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: str):
        self.__paymentMethod = paymentMethod


    @property
    def bookingRef(self):
        return self.__bookingRef

    @bookingRef.setter
    def bookingRef(self, bookingRef: str):
        self.__bookingRef = bookingRef


    @property
    def isPayed(self):
        return self.__isPayed

    @isPayed.setter
    def isPayed(self, isPayed: str):
        self.__isPayed = isPayed


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

    def checkedInRoom(self, bookingmodel_roomID) :
        # TODO: Implement checkedInRoom method
        pass

    def setExtras(self, bookingmodel_extras) :
        # TODO: Implement setExtras method
        pass

    def getRoomTypes(self) :
        # TODO: Implement getRoomTypes method
        pass

    def setRoomTypes(self, bookingmodel_roomTypes) :
        # TODO: Implement setRoomTypes method
        pass

    def setResponsibleGuest(self, bookingmodel_roomID, bookingmodel_guestEmail) :
        # TODO: Implement setResponsibleGuest method
        pass

    def setServiceNotes(self, bookingmodel_services) :
        # TODO: Implement setServiceNotes method
        pass

    def setResponsibleGuestToAllRooms(self, bookingmodel_guestEmail) :
        # TODO: Implement setResponsibleGuestToAllRooms method
        pass

    def checkedOutAllRooms(self) :
        # TODO: Implement checkedOutAllRooms method
        pass

    def getRoomIDs(self) :
        # TODO: Implement getRoomIDs method
        pass

    def allExtrasPayed(self) :
        # TODO: Implement allExtrasPayed method
        pass

    def isExtraPayed(self, bookingmodel_extra) :
        # TODO: Implement isExtraPayed method
        pass

    def removeServiceNotes(self, bookingmodel_serviceNotes) :
        # TODO: Implement removeServiceNotes method
        pass

    def removeResponsibleGuestToAllRooms(self, bookingmodel_guestEmail) :
        # TODO: Implement removeResponsibleGuestToAllRooms method
        pass

    def checkedOutRoom(self, bookingmodel_roomID) :
        # TODO: Implement checkedOutRoom method
        pass

    def setRoomIDs(self, bookingmodel_roomIDs) :
        # TODO: Implement setRoomIDs method
        pass

    def checkedInAllRooms(self) :
        # TODO: Implement checkedInAllRooms method
        pass

    def removeResponsibleGuest(self, bookingmodel_guestEmail, bookingmodel_roomID) :
        # TODO: Implement removeResponsibleGuest method
        pass

    def getNrOfRooms(self) :
        # TODO: Implement getNrOfRooms method
        pass

    def setExtrasAsPayed(self, bookingmodel_extras) :
        # TODO: Implement setExtrasAsPayed method
        pass

    def getExtras(self) :
        # TODO: Implement getExtras method
        pass

    def getUnPayedExtras(self) :
        # TODO: Implement getUnPayedExtras method
        pass

class bookingmodel_RoomToGuestIDEntry:

    def __init__(self, key: str, value: str, bookingmodel_RoomToGuestIDEntry: "bookingmodel_Booking" = None):
        self.key = key
        self.value = value
        self.bookingmodel_RoomToGuestIDEntry = bookingmodel_RoomToGuestIDEntry
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
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
