from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomApproval(Enum):
    pass
class DisabilityApproval(Enum):
    pass

############################################
# Definition of Classes
############################################

class tda593_booking_LegalEntity(ABC):

    def __init__(self, phone: str, email: str, id: int):
        self.phone = phone
        self.email = email
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    def getName(self) :
        # TODO: Implement getName method
        pass

class booking_LegalEntityDataService:

    pass
class LegalEntityManager:

    pass
class tda593_booking_LegalEntityManagerImpl(LegalEntityManager):

    pass
class tda593_booking_LegalEntityDataService:

    def __init__(self):
        
        pass
    def getPerson(self, tda593_SSN) :
        # TODO: Implement getPerson method
        pass

    def findOrganization(self, tda593_name) :
        # TODO: Implement findOrganization method
        pass

    def getOrganization(self, tda593_organizationNumber) :
        # TODO: Implement getOrganization method
        pass

    def findPerson(self, tda593_lastname, tda593_firstname) :
        # TODO: Implement findPerson method
        pass

class tda593_booking_LegalEntityManager(ABC):

    def __init__(self):
        
        pass
    def findOrganization(self, tda593_name) :
        # TODO: Implement findOrganization method
        pass

    def createOrganization(self, tda593_organizationNumber, tda593_phone, tda593_email, tda593_name) :
        # TODO: Implement createOrganization method
        pass

    def getLegalEntity(self, tda593_id) :
        # TODO: Implement getLegalEntity method
        pass

    def getPerson(self, tda593_SSN) :
        # TODO: Implement getPerson method
        pass

    def getOrganization(self, tda593_organizationNumber) :
        # TODO: Implement getOrganization method
        pass

    def findPerson(self, tda593_lastname, tda593_firstname) :
        # TODO: Implement findPerson method
        pass

    def createPerson(self, tda593_firstname, tda593_lastname, tda593_phone, tda593_email, tda593_SSN) :
        # TODO: Implement createPerson method
        pass

class tda593_booking_BookingDataService:

    def __init__(self):
        
        pass
    def commitTransaction(self):
        # TODO: Implement commitTransaction method
        pass

    def getAll(self, tda593_roomNumber, tda593_to, tda593_from_) :
        # TODO: Implement getAll method
        pass

    def beginTransaction(self):
        # TODO: Implement beginTransaction method
        pass

    def rollbackTransaction(self):
        # TODO: Implement rollbackTransaction method
        pass

class facilities_RoomManager:

    pass
class booking_BookingDataService:

    pass
class BookingManager:

    pass
class tda593_booking_BookingManagerImpl(BookingManager):

    pass
class tda593_booking_BookingManager(ABC):

    def __init__(self):
        
        pass
    def getAvailableRoomTypeAmounts(self, tda593_from_, tda593_to):
        # TODO: Implement getAvailableRoomTypeAmounts method
        pass

    def isRoomTypeAvailable(self, tda593_from_, tda593_roomType, tda593_to) :
        # TODO: Implement isRoomTypeAvailable method
        pass

    def createBooking(self, tda593_to, tda593_room, tda593_customer, tda593_from_) :
        # TODO: Implement createBooking method
        pass

    def removeStayRequest(self, tda593_booking, tda593_stayRequest):
        # TODO: Implement removeStayRequest method
        pass

    def changeBookingDates(self, tda593_booking, tda593_newStart, tda593_newEnd) :
        # TODO: Implement changeBookingDates method
        pass

    def getStayRequests(self):
        # TODO: Implement getStayRequests method
        pass

    def registerRoom(self, tda593_booking, tda593_room):
        # TODO: Implement registerRoom method
        pass

    def getActiveBooking(self, tda593_roomNumber) :
        # TODO: Implement getActiveBooking method
        pass

    def getAvailableRoomTypeAmount(self, tda593_roomType, tda593_from_, tda593_to) :
        # TODO: Implement getAvailableRoomTypeAmount method
        pass

    def getAvailableRooms(self, tda593_roomType, tda593_to, tda593_from_) :
        # TODO: Implement getAvailableRooms method
        pass

    def getBookings(self, tda593_customer) :
        # TODO: Implement getBookings method
        pass

    def getBooking(self, tda593_bookingId) :
        # TODO: Implement getBooking method
        pass

    def isRoomAvailable(self, tda593_from_, tda593_to, tda593_roomNumber) :
        # TODO: Implement isRoomAvailable method
        pass

    def checkOut(self, tda593_booking):
        # TODO: Implement checkOut method
        pass

    def cancelBooking(self, tda593_booking):
        # TODO: Implement cancelBooking method
        pass

    def setSpecialRequest(self, tda593_specialRequest, tda593_booking):
        # TODO: Implement setSpecialRequest method
        pass

    def checkIn(self, tda593_booking, tda593_guests):
        # TODO: Implement checkIn method
        pass

    def addStayRequest(self, tda593_booking, tda593_stayRequest) :
        # TODO: Implement addStayRequest method
        pass

class tda593_booking_StayRequest:

    def __init__(self, text: str, timeStamp: date, id: int):
        self.text = text
        self.timeStamp = timeStamp
        self.id = id
        
        pass
    @property
    def timeStamp(self):
        return self.__timeStamp

    @timeStamp.setter
    def timeStamp(self, timeStamp: date):
        self.__timeStamp = timeStamp


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


class facilities_Room:

    pass
class booking_Person:

    pass
class booking_StayRequest:

    pass
class tda593_booking_RoomStay:

    def __init__(self, active: bool, id: int, tda593_booking_RoomStay: set["booking_StayRequest"] = None, tda593_booking_RoomStay42: set["booking_Person"] = None, tda593_booking_RoomStay44: "facilities_Room" = None):
        self.active = active
        self.id = id
        self.tda593_booking_RoomStay = tda593_booking_RoomStay if tda593_booking_RoomStay is not None else set()
        self.tda593_booking_RoomStay42 = tda593_booking_RoomStay42 if tda593_booking_RoomStay42 is not None else set()
        self.tda593_booking_RoomStay44 = tda593_booking_RoomStay44
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def tda593_booking_RoomStay42(self):
        return self.__tda593_booking_RoomStay42

    @tda593_booking_RoomStay42.setter
    def tda593_booking_RoomStay42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_RoomStay__tda593_booking_RoomStay42", None)
        self.__tda593_booking_RoomStay42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "booking_Person"):
                    opp_val = getattr(item, "booking_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "booking_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "booking_Person"):
                    opp_val = getattr(item, "booking_Person", None)
                    
                    setattr(item, "booking_Person", self)
                    

    @property
    def tda593_booking_RoomStay44(self):
        return self.__tda593_booking_RoomStay44

    @tda593_booking_RoomStay44.setter
    def tda593_booking_RoomStay44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_RoomStay__tda593_booking_RoomStay44", None)
        self.__tda593_booking_RoomStay44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facilities_Room"):
                opp_val = getattr(old_value, "facilities_Room", None)
                if opp_val == self:
                    setattr(old_value, "facilities_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facilities_Room"):
                opp_val = getattr(value, "facilities_Room", None)
                setattr(value, "facilities_Room", self)

    @property
    def tda593_booking_RoomStay(self):
        return self.__tda593_booking_RoomStay

    @tda593_booking_RoomStay.setter
    def tda593_booking_RoomStay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_RoomStay__tda593_booking_RoomStay", None)
        self.__tda593_booking_RoomStay = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "booking_StayRequest"):
                    opp_val = getattr(item, "booking_StayRequest", None)
                    
                    if opp_val == self:
                        setattr(item, "booking_StayRequest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "booking_StayRequest"):
                    opp_val = getattr(item, "booking_StayRequest", None)
                    
                    setattr(item, "booking_StayRequest", self)
                    

class booking_TravelInformation:

    pass
class tda593_booking_Booking:

    def __init__(self, isCanceled: bool, id: int, startDate: date, endDate: date, specialRequest: str, price: float, tda593_booking_Booking37: "booking_RoomStay" = None, tda593_booking_Booking: "facilities_RoomType" = None, tda593_booking_Booking32: "booking_TravelInformation" = None, tda593_booking_Booking34: "booking_LegalEntity" = None):
        self.isCanceled = isCanceled
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.specialRequest = specialRequest
        self.price = price
        self.tda593_booking_Booking37 = tda593_booking_Booking37
        self.tda593_booking_Booking = tda593_booking_Booking
        self.tda593_booking_Booking32 = tda593_booking_Booking32
        self.tda593_booking_Booking34 = tda593_booking_Booking34
        
        pass
    @property
    def specialRequest(self):
        return self.__specialRequest

    @specialRequest.setter
    def specialRequest(self, specialRequest: str):
        self.__specialRequest = specialRequest


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
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def isCanceled(self):
        return self.__isCanceled

    @isCanceled.setter
    def isCanceled(self, isCanceled: bool):
        self.__isCanceled = isCanceled


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def tda593_booking_Booking32(self):
        return self.__tda593_booking_Booking32

    @tda593_booking_Booking32.setter
    def tda593_booking_Booking32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_Booking__tda593_booking_Booking32", None)
        self.__tda593_booking_Booking32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_TravelInformation"):
                opp_val = getattr(old_value, "booking_TravelInformation", None)
                if opp_val == self:
                    setattr(old_value, "booking_TravelInformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_TravelInformation"):
                opp_val = getattr(value, "booking_TravelInformation", None)
                setattr(value, "booking_TravelInformation", self)

    @property
    def tda593_booking_Booking34(self):
        return self.__tda593_booking_Booking34

    @tda593_booking_Booking34.setter
    def tda593_booking_Booking34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_Booking__tda593_booking_Booking34", None)
        self.__tda593_booking_Booking34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_LegalEntity35"):
                opp_val = getattr(old_value, "booking_LegalEntity35", None)
                if opp_val == self:
                    setattr(old_value, "booking_LegalEntity35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_LegalEntity35"):
                opp_val = getattr(value, "booking_LegalEntity35", None)
                setattr(value, "booking_LegalEntity35", self)

    @property
    def tda593_booking_Booking37(self):
        return self.__tda593_booking_Booking37

    @tda593_booking_Booking37.setter
    def tda593_booking_Booking37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_Booking__tda593_booking_Booking37", None)
        self.__tda593_booking_Booking37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_RoomStay"):
                opp_val = getattr(old_value, "booking_RoomStay", None)
                if opp_val == self:
                    setattr(old_value, "booking_RoomStay", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_RoomStay"):
                opp_val = getattr(value, "booking_RoomStay", None)
                setattr(value, "booking_RoomStay", self)

    @property
    def tda593_booking_Booking(self):
        return self.__tda593_booking_Booking

    @tda593_booking_Booking.setter
    def tda593_booking_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_Booking__tda593_booking_Booking", None)
        self.__tda593_booking_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facilities_RoomType30"):
                opp_val = getattr(old_value, "facilities_RoomType30", None)
                if opp_val == self:
                    setattr(old_value, "facilities_RoomType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facilities_RoomType30"):
                opp_val = getattr(value, "facilities_RoomType30", None)
                setattr(value, "facilities_RoomType30", self)

    def getGuests(self) :
        # TODO: Implement getGuests method
        pass

    def unregisterTravelInformation(self, tda593_travelInformation):
        # TODO: Implement unregisterTravelInformation method
        pass

    def registerTravelInformation(self, tda593_travelInformation):
        # TODO: Implement registerTravelInformation method
        pass

    def getStayRequests(self) :
        # TODO: Implement getStayRequests method
        pass

class LegalEntity:

    pass
class tda593_booking_Person(LegalEntity):

    def __init__(self, firstname: str, lastname: str, socialSecurityNumber: str):
        self.firstname = firstname
        self.lastname = lastname
        self.socialSecurityNumber = socialSecurityNumber
        
        pass
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def socialSecurityNumber(self):
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: str):
        self.__socialSecurityNumber = socialSecurityNumber


class tda593_booking_Organization(LegalEntity):

    def __init__(self, name: str, organizationNumber: str):
        self.name = name
        self.organizationNumber = organizationNumber
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def organizationNumber(self):
        return self.__organizationNumber

    @organizationNumber.setter
    def organizationNumber(self, organizationNumber: str):
        self.__organizationNumber = organizationNumber


class billing_AdminDiscountManager:

    pass
class billing_DiscountManagerImpl:

    pass
class tda593_billing_AdminDiscountManagerImpl(billing_DiscountManagerImpl, billing_AdminDiscountManager):

    pass
class tda593_booking_TravelInformation:

    def __init__(self, id: int, trackingId: str, comment: str, tda593_booking_TravelInformation: "booking_TravelInformation" = None):
        self.id = id
        self.trackingId = trackingId
        self.comment = comment
        self.tda593_booking_TravelInformation = tda593_booking_TravelInformation
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def trackingId(self):
        return self.__trackingId

    @trackingId.setter
    def trackingId(self, trackingId: str):
        self.__trackingId = trackingId


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def tda593_booking_TravelInformation(self):
        return self.__tda593_booking_TravelInformation

    @tda593_booking_TravelInformation.setter
    def tda593_booking_TravelInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_booking_TravelInformation__tda593_booking_TravelInformation", None)
        self.__tda593_booking_TravelInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_TravelInformation39"):
                opp_val = getattr(old_value, "booking_TravelInformation39", None)
                if opp_val == self:
                    setattr(old_value, "booking_TravelInformation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_TravelInformation39"):
                opp_val = getattr(value, "booking_TravelInformation39", None)
                setattr(value, "booking_TravelInformation39", self)

class booking_RoomStay:

    pass
class billing_AdminServiceManager:

    pass
class billing_ServiceManagerImpl:

    pass
class tda593_billing_AdminServiceManagerImpl(billing_ServiceManagerImpl, billing_AdminServiceManager):

    pass
class tda593_billing_ServiceDataService:

    pass
class tda593_billing_ServiceManager(ABC):

    def __init__(self):
        
        pass
    def getService(self, tda593_id) :
        # TODO: Implement getService method
        pass

    def getAllServices(self) :
        # TODO: Implement getAllServices method
        pass

class billing_ServiceDataService:

    pass
class ServiceManager:

    pass
class tda593_billing_AdminServiceManager(ServiceManager):

    def __init__(self):
        
        pass
    def removeService(self, tda593_service):
        # TODO: Implement removeService method
        pass

    def createService(self, tda593_price, tda593_name) :
        # TODO: Implement createService method
        pass

class tda593_billing_ServiceManagerImpl(ServiceManager):

    pass
class billing_CreditCardInformationDataService:

    pass
class CreditCardManager:

    pass
class tda593_billing_CreditCardManagerImpl(CreditCardManager):

    pass
class tda593_billing_CreditCardInformationDataService:

    def __init__(self):
        
        pass
    def getByLegalEntity(self, tda593_legalEntityId) :
        # TODO: Implement getByLegalEntity method
        pass

class BankingManager:

    pass
class tda593_billing_BankingManagerImpl(BankingManager):

    pass
class tda593_billing_BillDataService:

    def __init__(self):
        
        pass
    def getBookingBill(self, tda593_booking) :
        # TODO: Implement getBookingBill method
        pass

    def getAll(self, tda593_customer) :
        # TODO: Implement getAll method
        pass

class booking_BookingManager:

    pass
class billing_BillDataService:

    pass
class BillManager:

    pass
class tda593_billing_BillManagerImpl(BillManager):

    pass
class tda593_billing_CreditCardInformation:

    def __init__(self, cardNumber: str, expirationDate: date, ccv: str, firstName: str, lastName: str, tda593_billing_CreditCardInformation: "booking_LegalEntity" = None):
        self.cardNumber = cardNumber
        self.expirationDate = expirationDate
        self.ccv = ccv
        self.firstName = firstName
        self.lastName = lastName
        self.tda593_billing_CreditCardInformation = tda593_billing_CreditCardInformation
        
        pass
    @property
    def ccv(self):
        return self.__ccv

    @ccv.setter
    def ccv(self, ccv: str):
        self.__ccv = ccv


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def expirationDate(self):
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: date):
        self.__expirationDate = expirationDate


    @property
    def cardNumber(self):
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, cardNumber: str):
        self.__cardNumber = cardNumber


    @property
    def tda593_billing_CreditCardInformation(self):
        return self.__tda593_billing_CreditCardInformation

    @tda593_billing_CreditCardInformation.setter
    def tda593_billing_CreditCardInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_CreditCardInformation__tda593_billing_CreditCardInformation", None)
        self.__tda593_billing_CreditCardInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_LegalEntity23"):
                opp_val = getattr(old_value, "booking_LegalEntity23", None)
                if opp_val == self:
                    setattr(old_value, "booking_LegalEntity23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_LegalEntity23"):
                opp_val = getattr(value, "booking_LegalEntity23", None)
                setattr(value, "booking_LegalEntity23", self)

class tda593_billing_CreditCardManager(ABC):

    def __init__(self):
        
        pass
    def setCreditCardInformation(self, tda593_lastname, tda593_validator, tda593_ccv, tda593_expirationDate, tda593_cardNumber, tda593_firstname, tda593_legalEntity) :
        # TODO: Implement setCreditCardInformation method
        pass

    def getCreditCardInformation(self, tda593_legalEntity) :
        # TODO: Implement getCreditCardInformation method
        pass

    def revalidateCreditCardInformation(self, tda593_bankingManager, tda593_legalEntity) :
        # TODO: Implement revalidateCreditCardInformation method
        pass

class tda593_billing_BankingManager(ABC):

    def __init__(self):
        
        pass
    def makePayment(self, tda593_sum, tda593_ccNumber, tda593_firstName, tda593_lastName, tda593_expiryYear, tda593_ccv, tda593_expiryMonth) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, tda593_ccv, tda593_firstName, tda593_lastName, tda593_ccNumber, tda593_expiryMonth, tda593_expiryYear) :
        # TODO: Implement isCreditCardValid method
        pass

class billing_DiscountDataService:

    pass
class DiscountManager:

    pass
class tda593_billing_AdminDiscountManager(DiscountManager):

    def __init__(self):
        
        pass
    def createDiscountLimitForDiscount(self, tda593_usesAmount, tda593_from_, tda593_discount, tda593_to, tda593_users):
        # TODO: Implement createDiscountLimitForDiscount method
        pass

    def setAmountLimit(self, tda593_usesAmount, tda593_discount):
        # TODO: Implement setAmountLimit method
        pass

    def addSumDiscount(self, tda593_sum, tda593_name, tda593_code) :
        # TODO: Implement addSumDiscount method
        pass

    def setDateRangeLimit(self, tda593_validTo, tda593_validFrom, tda593_discount):
        # TODO: Implement setDateRangeLimit method
        pass

    def addPercentageDiscount(self, tda593_name, tda593_percentage, tda593_code) :
        # TODO: Implement addPercentageDiscount method
        pass

    def addAllowedUsers(self, tda593_discount, tda593_legalEntities):
        # TODO: Implement addAllowedUsers method
        pass

class tda593_billing_DiscountManagerImpl(DiscountManager):

    pass
class tda593_billing_DiscountDataService:

    pass
class tda593_billing_BillManager(ABC):

    def __init__(self):
        
        pass
    def getBills(self, tda593_customer) :
        # TODO: Implement getBills method
        pass

    def createBookingBill(self, tda593_customer, tda593_booking) :
        # TODO: Implement createBookingBill method
        pass

    def billItem(self, tda593_service, tda593_quantity, tda593_bill):
        # TODO: Implement billItem method
        pass

    def addSubBill(self, tda593_subBill, tda593_toBill):
        # TODO: Implement addSubBill method
        pass

    def createBill(self, tda593_customer) :
        # TODO: Implement createBill method
        pass

    def markBillAsPaid(self, tda593_isPaid, tda593_bankingManager, tda593_creditCardManager, tda593_bill) :
        # TODO: Implement markBillAsPaid method
        pass

    def getUnpaidBills(self, tda593_customer) :
        # TODO: Implement getUnpaidBills method
        pass

    def getBill(self, tda593_id) :
        # TODO: Implement getBill method
        pass

    def publishBill(self, tda593_bill):
        # TODO: Implement publishBill method
        pass

    def getBookingBill(self, tda593_booking) :
        # TODO: Implement getBookingBill method
        pass

    def applyDiscount(self, tda593_bill, tda593_discount):
        # TODO: Implement applyDiscount method
        pass

class booking_Booking:

    pass
class Bill:

    pass
class tda593_billing_BookingBill(Bill):

    pass
class tda593_billing_Service:

    def __init__(self, id: int, price: float, name: str):
        self.id = id
        self.price = price
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


class billing_Service:

    pass
class tda593_billing_Purchase:

    def __init__(self, id: int, quantity: int, price: float, tda593_billing_Purchase: "billing_Service" = None):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.tda593_billing_Purchase = tda593_billing_Purchase
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity


    @property
    def tda593_billing_Purchase(self):
        return self.__tda593_billing_Purchase

    @tda593_billing_Purchase.setter
    def tda593_billing_Purchase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Purchase__tda593_billing_Purchase", None)
        self.__tda593_billing_Purchase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing_Service"):
                opp_val = getattr(old_value, "billing_Service", None)
                if opp_val == self:
                    setattr(old_value, "billing_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing_Service"):
                opp_val = getattr(value, "billing_Service", None)
                setattr(value, "billing_Service", self)

class billing_Bill:

    pass
class billing_Discount:

    pass
class billing_Purchase:

    pass
class tda593_billing_Bill:

    def __init__(self, id: int, date: date, isPublished: bool, isPaid: bool, tda593_billing_Bill: set["billing_Purchase"] = None, tda593_billing_Bill14: set["billing_Discount"] = None, tda593_billing_Bill16: "booking_LegalEntity" = None, tda593_billing_Bill19: set["billing_Bill"] = None):
        self.id = id
        self.date = date
        self.isPublished = isPublished
        self.isPaid = isPaid
        self.tda593_billing_Bill = tda593_billing_Bill if tda593_billing_Bill is not None else set()
        self.tda593_billing_Bill14 = tda593_billing_Bill14 if tda593_billing_Bill14 is not None else set()
        self.tda593_billing_Bill16 = tda593_billing_Bill16
        self.tda593_billing_Bill19 = tda593_billing_Bill19 if tda593_billing_Bill19 is not None else set()
        
        pass
    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: bool):
        self.__isPaid = isPaid


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def isPublished(self):
        return self.__isPublished

    @isPublished.setter
    def isPublished(self, isPublished: bool):
        self.__isPublished = isPublished


    @property
    def tda593_billing_Bill(self):
        return self.__tda593_billing_Bill

    @tda593_billing_Bill.setter
    def tda593_billing_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Bill__tda593_billing_Bill", None)
        self.__tda593_billing_Bill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "billing_Purchase"):
                    opp_val = getattr(item, "billing_Purchase", None)
                    
                    if opp_val == self:
                        setattr(item, "billing_Purchase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "billing_Purchase"):
                    opp_val = getattr(item, "billing_Purchase", None)
                    
                    setattr(item, "billing_Purchase", self)
                    

    @property
    def tda593_billing_Bill14(self):
        return self.__tda593_billing_Bill14

    @tda593_billing_Bill14.setter
    def tda593_billing_Bill14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Bill__tda593_billing_Bill14", None)
        self.__tda593_billing_Bill14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "billing_Discount"):
                    opp_val = getattr(item, "billing_Discount", None)
                    
                    if opp_val == self:
                        setattr(item, "billing_Discount", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "billing_Discount"):
                    opp_val = getattr(item, "billing_Discount", None)
                    
                    setattr(item, "billing_Discount", self)
                    

    @property
    def tda593_billing_Bill19(self):
        return self.__tda593_billing_Bill19

    @tda593_billing_Bill19.setter
    def tda593_billing_Bill19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Bill__tda593_billing_Bill19", None)
        self.__tda593_billing_Bill19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "billing_Bill"):
                    opp_val = getattr(item, "billing_Bill", None)
                    
                    if opp_val == self:
                        setattr(item, "billing_Bill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "billing_Bill"):
                    opp_val = getattr(item, "billing_Bill", None)
                    
                    setattr(item, "billing_Bill", self)
                    

    @property
    def tda593_billing_Bill16(self):
        return self.__tda593_billing_Bill16

    @tda593_billing_Bill16.setter
    def tda593_billing_Bill16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Bill__tda593_billing_Bill16", None)
        self.__tda593_billing_Bill16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking_LegalEntity17"):
                opp_val = getattr(old_value, "booking_LegalEntity17", None)
                if opp_val == self:
                    setattr(old_value, "booking_LegalEntity17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking_LegalEntity17"):
                opp_val = getattr(value, "booking_LegalEntity17", None)
                setattr(value, "booking_LegalEntity17", self)

    def registerPurchase(self, tda593_purchase):
        # TODO: Implement registerPurchase method
        pass

    def unPublishBill(self):
        # TODO: Implement unPublishBill method
        pass

    def applyDiscount(self, tda593_discount):
        # TODO: Implement applyDiscount method
        pass

    def unregisterPurchase(self, tda593_purchase):
        # TODO: Implement unregisterPurchase method
        pass

    def getPrice(self) :
        # TODO: Implement getPrice method
        pass

    def removeDiscount(self, tda593_discount):
        # TODO: Implement removeDiscount method
        pass

    def addSubBill(self, tda593_subBill):
        # TODO: Implement addSubBill method
        pass

    def removeSubBill(self, tda593_subBill):
        # TODO: Implement removeSubBill method
        pass

    def publishBill(self):
        # TODO: Implement publishBill method
        pass

class tda593_facilities_RoomDataService:

    def __init__(self):
        
        pass
    def getGuestRoom(self, tda593_id) :
        # TODO: Implement getGuestRoom method
        pass

    def getConferenceRoom(self, tda593_id) :
        # TODO: Implement getConferenceRoom method
        pass

    def getAllConferenceRooms(self) :
        # TODO: Implement getAllConferenceRooms method
        pass

    def getAllGuestRooms(self) :
        # TODO: Implement getAllGuestRooms method
        pass

class facilities_KeyCardManager:

    pass
class Discount:

    pass
class tda593_billing_PercentageDiscount(Discount):

    def __init__(self, percentage: float):
        self.percentage = percentage
        
        pass
    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage: float):
        self.__percentage = percentage


class tda593_billing_SumDiscount(Discount):

    def __init__(self, discountSum: float):
        self.discountSum = discountSum
        
        pass
    @property
    def discountSum(self):
        return self.__discountSum

    @discountSum.setter
    def discountSum(self, discountSum: float):
        self.__discountSum = discountSum


class booking_LegalEntity:

    pass
class tda593_billing_DiscountLimit:

    def __init__(self, id: int, startDate: date, endDate: date, timesLeftToUse: int, tda593_billing_DiscountLimit: set["booking_LegalEntity"] = None):
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.timesLeftToUse = timesLeftToUse
        self.tda593_billing_DiscountLimit = tda593_billing_DiscountLimit if tda593_billing_DiscountLimit is not None else set()
        
        pass
    @property
    def timesLeftToUse(self):
        return self.__timesLeftToUse

    @timesLeftToUse.setter
    def timesLeftToUse(self, timesLeftToUse: int):
        self.__timesLeftToUse = timesLeftToUse


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


    @property
    def tda593_billing_DiscountLimit(self):
        return self.__tda593_billing_DiscountLimit

    @tda593_billing_DiscountLimit.setter
    def tda593_billing_DiscountLimit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_DiscountLimit__tda593_billing_DiscountLimit", None)
        self.__tda593_billing_DiscountLimit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "booking_LegalEntity"):
                    opp_val = getattr(item, "booking_LegalEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "booking_LegalEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "booking_LegalEntity"):
                    opp_val = getattr(item, "booking_LegalEntity", None)
                    
                    setattr(item, "booking_LegalEntity", self)
                    

class billing_DiscountLimit:

    pass
class tda593_billing_Discount(ABC):

    def __init__(self, code: str, name: str, tda593_billing_Discount: "billing_DiscountLimit" = None):
        self.code = code
        self.name = name
        self.tda593_billing_Discount = tda593_billing_Discount
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def tda593_billing_Discount(self):
        return self.__tda593_billing_Discount

    @tda593_billing_Discount.setter
    def tda593_billing_Discount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_billing_Discount__tda593_billing_Discount", None)
        self.__tda593_billing_Discount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing_DiscountLimit"):
                opp_val = getattr(old_value, "billing_DiscountLimit", None)
                if opp_val == self:
                    setattr(old_value, "billing_DiscountLimit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing_DiscountLimit"):
                opp_val = getattr(value, "billing_DiscountLimit", None)
                setattr(value, "billing_DiscountLimit", self)

    def getPriceWithDiscount(self, tda593_price) :
        # TODO: Implement getPriceWithDiscount method
        pass

class tda593_billing_DiscountManager(ABC):

    def __init__(self):
        
        pass
    def getDiscount(self, tda593_code) :
        # TODO: Implement getDiscount method
        pass

class facilities_AdminKeyCardManager:

    pass
class facilities_KeyCardManagerImpl:

    pass
class tda593_facilities_AdminKeyCardManagerImpl(facilities_AdminKeyCardManager, facilities_KeyCardManagerImpl):

    pass
class facilities_AdminRoomManager:

    pass
class facilities_RoomManagerImpl:

    pass
class tda593_facilities_AdminRoomManagerImpl(facilities_RoomManagerImpl, facilities_AdminRoomManager):

    pass
class tda593_facilities_KeyCardDataService:

    pass
class facilities_KeyCardDataService:

    pass
class tda593_facilities_RoomTypeDataService:

    pass
class facilities_RoomTypeDataService:

    pass
class facilities_RoomDataService:

    pass
class Room:

    pass
class tda593_facilities_ConferenceRoom(Room):

    def __init__(self, numberOfSeats: int, equipment: str):
        self.numberOfSeats = numberOfSeats
        self.equipment = equipment
        
        pass
    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment: str):
        self.__equipment = equipment


    @property
    def numberOfSeats(self):
        return self.__numberOfSeats

    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: int):
        self.__numberOfSeats = numberOfSeats


class tda593_facilities_GuestRoom(Room):

    def __init__(self, numberOfBeds: int, numberOfExtrabeds: int):
        self.numberOfBeds = numberOfBeds
        self.numberOfExtrabeds = numberOfExtrabeds
        
        pass
    @property
    def numberOfBeds(self):
        return self.__numberOfBeds

    @numberOfBeds.setter
    def numberOfBeds(self, numberOfBeds: int):
        self.__numberOfBeds = numberOfBeds


    @property
    def numberOfExtrabeds(self):
        return self.__numberOfExtrabeds

    @numberOfExtrabeds.setter
    def numberOfExtrabeds(self, numberOfExtrabeds: int):
        self.__numberOfExtrabeds = numberOfExtrabeds


class facilities_RoomType:

    pass
class facilities_KeyCard:

    pass
class tda593_facilities_Room(ABC):

    def __init__(self, floor: int, roomNumber: str, isOperational: bool, isBeingCleaned: bool, description: str, photos: str, disabilityApprovals: str, tda593_facilities_Room: set["facilities_KeyCard"] = None, tda593_facilities_Room2: "facilities_RoomType" = None):
        self.floor = floor
        self.roomNumber = roomNumber
        self.isOperational = isOperational
        self.isBeingCleaned = isBeingCleaned
        self.description = description
        self.photos = photos
        self.disabilityApprovals = disabilityApprovals
        self.tda593_facilities_Room = tda593_facilities_Room if tda593_facilities_Room is not None else set()
        self.tda593_facilities_Room2 = tda593_facilities_Room2
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: str):
        self.__roomNumber = roomNumber


    @property
    def isOperational(self):
        return self.__isOperational

    @isOperational.setter
    def isOperational(self, isOperational: bool):
        self.__isOperational = isOperational


    @property
    def isBeingCleaned(self):
        return self.__isBeingCleaned

    @isBeingCleaned.setter
    def isBeingCleaned(self, isBeingCleaned: bool):
        self.__isBeingCleaned = isBeingCleaned


    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor


    @property
    def disabilityApprovals(self):
        return self.__disabilityApprovals

    @disabilityApprovals.setter
    def disabilityApprovals(self, disabilityApprovals: str):
        self.__disabilityApprovals = disabilityApprovals


    @property
    def photos(self):
        return self.__photos

    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos


    @property
    def tda593_facilities_Room(self):
        return self.__tda593_facilities_Room

    @tda593_facilities_Room.setter
    def tda593_facilities_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_facilities_Room__tda593_facilities_Room", None)
        self.__tda593_facilities_Room = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "facilities_KeyCard"):
                    opp_val = getattr(item, "facilities_KeyCard", None)
                    
                    if opp_val == self:
                        setattr(item, "facilities_KeyCard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "facilities_KeyCard"):
                    opp_val = getattr(item, "facilities_KeyCard", None)
                    
                    setattr(item, "facilities_KeyCard", self)
                    

    @property
    def tda593_facilities_Room2(self):
        return self.__tda593_facilities_Room2

    @tda593_facilities_Room2.setter
    def tda593_facilities_Room2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tda593_facilities_Room__tda593_facilities_Room2", None)
        self.__tda593_facilities_Room2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facilities_RoomType"):
                opp_val = getattr(old_value, "facilities_RoomType", None)
                if opp_val == self:
                    setattr(old_value, "facilities_RoomType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facilities_RoomType"):
                opp_val = getattr(value, "facilities_RoomType", None)
                setattr(value, "facilities_RoomType", self)

    def registerKeyCard(self, tda593_keyCard):
        # TODO: Implement registerKeyCard method
        pass

    def unregisterKeyCards(self):
        # TODO: Implement unregisterKeyCards method
        pass

    def unregisterKeyCard(self, tda593_keyCard):
        # TODO: Implement unregisterKeyCard method
        pass

class tda593_facilities_RoomType:

    def __init__(self, name: str, description: str, roomApprovals: str, price: float):
        self.name = name
        self.description = description
        self.roomApprovals = roomApprovals
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def roomApprovals(self):
        return self.__roomApprovals

    @roomApprovals.setter
    def roomApprovals(self, roomApprovals: str):
        self.__roomApprovals = roomApprovals


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class tda593_facilities_RoomManager(ABC):

    def __init__(self):
        
        pass
    def getRoomType(self, tda593_name) :
        # TODO: Implement getRoomType method
        pass

    def getRooms(self) :
        # TODO: Implement getRooms method
        pass

    def setIsBeingCleaned(self, tda593_room, tda593_value):
        # TODO: Implement setIsBeingCleaned method
        pass

    def getConferenceRooms(self) :
        # TODO: Implement getConferenceRooms method
        pass

    def getRoomTypeAmounts(self):
        # TODO: Implement getRoomTypeAmounts method
        pass

    def getRoom(self, tda593_roomNumber) :
        # TODO: Implement getRoom method
        pass

    def getRoomTypes(self) :
        # TODO: Implement getRoomTypes method
        pass

    def getGuestRooms(self) :
        # TODO: Implement getGuestRooms method
        pass

    def unregisterKeyCard(self, tda593_roomNumber, tda593_keyCardNbr):
        # TODO: Implement unregisterKeyCard method
        pass

    def getRoomTypeAmount(self, tda593_roomType) :
        # TODO: Implement getRoomTypeAmount method
        pass

    def unregisterAllKeyCards(self, tda593_roomNumber):
        # TODO: Implement unregisterAllKeyCards method
        pass

    def registerKeyCard(self, tda593_keyCardNbr, tda593_roomNumber):
        # TODO: Implement registerKeyCard method
        pass

class tda593_california_DataService(ABC):

    def __init__(self):
        
        pass
    def set(self, tda593_object):
        # TODO: Implement set method
        pass

    def count(self) :
        # TODO: Implement count method
        pass

    def delete(self, tda593_object):
        # TODO: Implement delete method
        pass

    def exist(self, tda593_object) :
        # TODO: Implement exist method
        pass

    def getAll(self):
        # TODO: Implement getAll method
        pass

    def setAll(self, tda593_objects):
        # TODO: Implement setAll method
        pass

    def get(self, tda593_id):
        # TODO: Implement get method
        pass

class RoomManager:

    pass
class tda593_facilities_RoomManagerImpl(RoomManager):

    pass
class tda593_facilities_AdminRoomManager(RoomManager):

    def __init__(self):
        
        pass
    def removeRoomType(self, tda593_roomType) :
        # TODO: Implement removeRoomType method
        pass

    def addGuestRoom(self, tda593_description, tda593_numberOfBeds, tda593_number, tda593_photos, tda593_roomType, tda593_disabilityApprovals, tda593_floor, tda593_numberOfExtraBeds) :
        # TODO: Implement addGuestRoom method
        pass

    def addRoomType(self, tda593_price, tda593_name, tda593_description, tda593_roomApprovals) :
        # TODO: Implement addRoomType method
        pass

    def removeRoom(self, tda593_roomNumber) :
        # TODO: Implement removeRoom method
        pass

    def addConferenceRoom(self, tda593_description, tda593_floor, tda593_equipment, tda593_roomType, tda593_disabilityApprovals, tda593_photos, tda593_number, tda593_numberOfSeats) :
        # TODO: Implement addConferenceRoom method
        pass

class tda593_facilities_KeyCard:

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class tda593_facilities_KeyCardManager(ABC):

    def __init__(self):
        
        pass
    def getKeyCard(self, tda593_keyCardNbr) :
        # TODO: Implement getKeyCard method
        pass

class KeyCardManager:

    pass
class tda593_facilities_KeyCardManagerImpl(KeyCardManager):

    pass
class tda593_facilities_AdminKeyCardManager(KeyCardManager):

    def __init__(self):
        
        pass
    def addKeyCard(self, tda593_cardNumber):
        # TODO: Implement addKeyCard method
        pass

    def removeKeyCard(self, tda593_cardNumber):
        # TODO: Implement removeKeyCard method
        pass
