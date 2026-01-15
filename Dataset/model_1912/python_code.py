from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomApproval(Enum):
class DisabilityApproval(Enum):


############################################
# Definition of Classes
############################################

class LegalEntityManager:

    pass
class tda593_booking_LegalEntityManagerImpl(LegalEntityManager):

    pass
class tda593_booking_LegalEntity(ABC):

    def __init__(self, phone: str, email: str, id: int):
        self.phone = phone
        self.email = email
        self.id = id
        
    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class tda593_booking_LegalEntityDataService:

    def __init__(self):
        
    def getPerson(self, SSN: str) -> str:
        # TODO: Implement getPerson method
        pass

    def findPerson(self, firstname: str, lastname: str) -> str:
        # TODO: Implement findPerson method
        pass

    def findOrganization(self, name: str) -> str:
        # TODO: Implement findOrganization method
        pass

    def getOrganization(self, organizationNumber: str) -> str:
        # TODO: Implement getOrganization method
        pass

class booking_LegalEntityDataService:

    pass
class tda593_booking_LegalEntityManager(ABC):

    def __init__(self):
        
    def createOrganization(self, phone: str, organizationNumber: str, name: str, email: str) -> str:
        # TODO: Implement createOrganization method
        pass

    def findPerson(self, firstname: str, lastname: str) -> str:
        # TODO: Implement findPerson method
        pass

    def createPerson(self, SSN: str, firstname: str, lastname: str, email: str, phone: str) -> str:
        # TODO: Implement createPerson method
        pass

    def getOrganization(self, organizationNumber: str) -> str:
        # TODO: Implement getOrganization method
        pass

    def getLegalEntity(self, id: int) -> str:
        # TODO: Implement getLegalEntity method
        pass

    def findOrganization(self, name: str) -> str:
        # TODO: Implement findOrganization method
        pass

    def getPerson(self, SSN: str) -> str:
        # TODO: Implement getPerson method
        pass

class tda593_booking_BookingDataService:

    def __init__(self):
        
    def getAll(self, to: date, roomNumber: str, from: date) -> str:
        # TODO: Implement getAll method
        pass

    def commitTransaction(self):
        # TODO: Implement commitTransaction method
        pass

    def beginTransaction(self):
        # TODO: Implement beginTransaction method
        pass

    def rollbackTransaction(self):
        # TODO: Implement rollbackTransaction method
        pass

    def getAll(self, to: date, from: date) -> str:
        # TODO: Implement getAll method
        pass

    def getAll(self, to: date, legal: str, from: date) -> str:
        # TODO: Implement getAll method
        pass

    def getAll(self, customer: str) -> str:
        # TODO: Implement getAll method
        pass

class facilities_RoomManager:

    pass
class booking_BookingDataService:

    pass
class BookingManager:

    pass
class tda593_booking_BookingManagerImpl(BookingManager):

    pass
class tda593_booking_StayRequest:

    def __init__(self, text: str, timeStamp: date, id: int):
        self.text = text
        self.timeStamp = timeStamp
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def timeStamp(self) -> date:
        return self.__timeStamp

    @timeStamp.setter
    def timeStamp(self, timeStamp: date):
        self.__timeStamp = timeStamp

class facilities_Room:

    pass
class booking_Person:

    pass
class booking_StayRequest:

    pass
class tda593_booking_BookingManager(ABC):

    def __init__(self):
        
    def isRoomTypeAvailable(self, roomType: str, to: date, from: date) -> bool:
        # TODO: Implement isRoomTypeAvailable method
        pass

    def addStayRequest(self, booking: str, stayRequest: str) -> str:
        # TODO: Implement addStayRequest method
        pass

    def getBookings(self, customer: str) -> str:
        # TODO: Implement getBookings method
        pass

    def cancelBooking(self, booking: str):
        # TODO: Implement cancelBooking method
        pass

    def registerRoom(self, room: str, booking: str):
        # TODO: Implement registerRoom method
        pass

    def checkIn(self, guests: str, booking: str):
        # TODO: Implement checkIn method
        pass

    def getBookings(self, from: date, to: date) -> str:
        # TODO: Implement getBookings method
        pass

    def changeBookingDates(self, newEnd: date, booking: str, newStart: date) -> bool:
        # TODO: Implement changeBookingDates method
        pass

    def getBooking(self, bookingId: int) -> str:
        # TODO: Implement getBooking method
        pass

    def isRoomAvailable(self, roomNumber: str, to: date, from: date) -> bool:
        # TODO: Implement isRoomAvailable method
        pass

    def getBookings(self, customer: str, to: date, from: date) -> str:
        # TODO: Implement getBookings method
        pass

    def removeStayRequest(self, booking: str, stayRequest: str):
        # TODO: Implement removeStayRequest method
        pass

    def createBooking(self, customer: str, to: date, roomType: str, from: date) -> str:
        # TODO: Implement createBooking method
        pass

    def getStayRequests(self):
        # TODO: Implement getStayRequests method
        pass

    def getAvailableRooms(self, roomType: str, from: date, to: date) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def getAvailableRooms(self, to: date, from: date) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def getAvailableRoomTypeAmount(self, from: date, roomType: str, to: date) -> int:
        # TODO: Implement getAvailableRoomTypeAmount method
        pass

    def createBooking(self, room: str, to: date, customer: str, from: date) -> str:
        # TODO: Implement createBooking method
        pass

    def getActiveBooking(self, roomNumber: str) -> str:
        # TODO: Implement getActiveBooking method
        pass

    def setSpecialRequest(self, specialRequest: str, booking: str):
        # TODO: Implement setSpecialRequest method
        pass

    def checkOut(self, booking: str):
        # TODO: Implement checkOut method
        pass

    def getAvailableRoomTypeAmounts(self, from: date, to: date):
        # TODO: Implement getAvailableRoomTypeAmounts method
        pass

class tda593_booking_Booking:

    def __init__(self, endDate: date, specialRequest: str, price: float, isCanceled: bool, id: int, startDate: date, tda593_booking_Booking: "facilities_RoomType" = None, tda593_booking_Booking32: "booking_TravelInformation" = None, tda593_booking_Booking34: "booking_LegalEntity" = None, tda593_booking_Booking37: "booking_RoomStay" = None):
        self.endDate = endDate
        self.specialRequest = specialRequest
        self.price = price
        self.isCanceled = isCanceled
        self.id = id
        self.startDate = startDate
        self.tda593_booking_Booking = tda593_booking_Booking
        self.tda593_booking_Booking32 = tda593_booking_Booking32
        self.tda593_booking_Booking34 = tda593_booking_Booking34
        self.tda593_booking_Booking37 = tda593_booking_Booking37
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def specialRequest(self) -> str:
        return self.__specialRequest

    @specialRequest.setter
    def specialRequest(self, specialRequest: str):
        self.__specialRequest = specialRequest

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
    def isCanceled(self) -> bool:
        return self.__isCanceled

    @isCanceled.setter
    def isCanceled(self, isCanceled: bool):
        self.__isCanceled = isCanceled

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

    def registerTravelInformation(self, travelInformation: str):
        # TODO: Implement registerTravelInformation method
        pass

    def getGuests(self) -> str:
        # TODO: Implement getGuests method
        pass

    def unregisterTravelInformation(self, travelInformation: str):
        # TODO: Implement unregisterTravelInformation method
        pass

    def getStayRequests(self) -> str:
        # TODO: Implement getStayRequests method
        pass

class tda593_booking_RoomStay:

    def __init__(self, active: bool, id: int, tda593_booking_RoomStay: set["booking_StayRequest"] = None, tda593_booking_RoomStay42: set["booking_Person"] = None, tda593_booking_RoomStay44: "facilities_Room" = None):
        self.active = active
        self.id = id
        self.tda593_booking_RoomStay = tda593_booking_RoomStay if tda593_booking_RoomStay is not None else set()
        self.tda593_booking_RoomStay42 = tda593_booking_RoomStay42 if tda593_booking_RoomStay42 is not None else set()
        self.tda593_booking_RoomStay44 = tda593_booking_RoomStay44
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
                    

class tda593_booking_TravelInformation:

    def __init__(self, id: int, trackingId: str, comment: str, tda593_booking_TravelInformation: "booking_TravelInformation" = None):
        self.id = id
        self.trackingId = trackingId
        self.comment = comment
        self.tda593_booking_TravelInformation = tda593_booking_TravelInformation
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def trackingId(self) -> str:
        return self.__trackingId

    @trackingId.setter
    def trackingId(self, trackingId: str):
        self.__trackingId = trackingId

    @property
    def comment(self) -> str:
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
class booking_TravelInformation:

    pass
class LegalEntity:

    pass
class tda593_booking_Person(LegalEntity):

    def __init__(self, firstname: str, lastname: str, socialSecurityNumber: str):
        self.firstname = firstname
        self.lastname = lastname
        self.socialSecurityNumber = socialSecurityNumber
        
    @property
    def socialSecurityNumber(self) -> str:
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: str):
        self.__socialSecurityNumber = socialSecurityNumber

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

class tda593_booking_Organization(LegalEntity):

    def __init__(self, name: str, organizationNumber: str):
        self.name = name
        self.organizationNumber = organizationNumber
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def organizationNumber(self) -> str:
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
class tda593_billing_BillDataService:

    def __init__(self):
        
    def getAll(self, customer: str) -> str:
        # TODO: Implement getAll method
        pass

    def getBookingBill(self, booking: str) -> str:
        # TODO: Implement getBookingBill method
        pass

class booking_BookingManager:

    pass
class billing_BillDataService:

    pass
class BillManager:

    pass
class tda593_billing_BillManagerImpl(BillManager):

    pass
class billing_AdminServiceManager:

    pass
class billing_ServiceManagerImpl:

    pass
class tda593_billing_AdminServiceManagerImpl(billing_AdminServiceManager, billing_ServiceManagerImpl):

    pass
class tda593_billing_ServiceDataService:

    pass
class tda593_billing_ServiceManager(ABC):

    def __init__(self):
        
    def getService(self, id: int) -> str:
        # TODO: Implement getService method
        pass

    def getAllServices(self) -> str:
        # TODO: Implement getAllServices method
        pass

class billing_ServiceDataService:

    pass
class ServiceManager:

    pass
class tda593_billing_AdminServiceManager(ServiceManager):

    def __init__(self):
        
    def createService(self, price: float, name: str) -> str:
        # TODO: Implement createService method
        pass

    def removeService(self, service: str):
        # TODO: Implement removeService method
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
        
    def getByLegalEntity(self, legalEntityId: int) -> str:
        # TODO: Implement getByLegalEntity method
        pass

class BankingManager:

    pass
class tda593_billing_BankingManagerImpl(BankingManager):

    pass
class tda593_billing_BankingManager(ABC):

    def __init__(self):
        
    def isCreditCardValid(self, lastName: str, expiryYear: int, firstName: str, expiryMonth: int, ccv: str, ccNumber: str) -> bool:
        # TODO: Implement isCreditCardValid method
        pass

    def makePayment(self, expiryMonth: int, sum: float, lastName: str, ccv: str, firstName: str, ccNumber: str, expiryYear: int) -> bool:
        # TODO: Implement makePayment method
        pass

class tda593_billing_CreditCardInformation:

    def __init__(self, cardNumber: str, expirationDate: date, ccv: str, firstName: str, lastName: str, tda593_billing_CreditCardInformation: "booking_LegalEntity" = None):
        self.cardNumber = cardNumber
        self.expirationDate = expirationDate
        self.ccv = ccv
        self.firstName = firstName
        self.lastName = lastName
        self.tda593_billing_CreditCardInformation = tda593_billing_CreditCardInformation
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def ccv(self) -> str:
        return self.__ccv

    @ccv.setter
    def ccv(self, ccv: str):
        self.__ccv = ccv

    @property
    def expirationDate(self) -> date:
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: date):
        self.__expirationDate = expirationDate

    @property
    def cardNumber(self) -> str:
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, cardNumber: str):
        self.__cardNumber = cardNumber

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

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
        
    def getCreditCardInformation(self, legalEntityId: int) -> str:
        # TODO: Implement getCreditCardInformation method
        pass

    def setCreditCardInformation(self, cardNumber: str, legalEntity: str, lastname: str, expirationDate: date, firstname: str, validator: str, ccv: str) -> bool:
        # TODO: Implement setCreditCardInformation method
        pass

    def revalidateCreditCardInformation(self, legalEntity: str, bankingManager: str) -> bool:
        # TODO: Implement revalidateCreditCardInformation method
        pass

    def getCreditCardInformation(self, legalEntity: str) -> str:
        # TODO: Implement getCreditCardInformation method
        pass

class booking_Booking:

    pass
class Bill:

    pass
class tda593_billing_BookingBill(Bill):

    pass
class tda593_billing_BillManager(ABC):

    def __init__(self):
        
    def getBookingBill(self, booking: str) -> str:
        # TODO: Implement getBookingBill method
        pass

    def getBills(self, customer: str) -> str:
        # TODO: Implement getBills method
        pass

    def getUnpaidBills(self, customer: str) -> str:
        # TODO: Implement getUnpaidBills method
        pass

    def billItem(self, quantity: int, bill: str, service: str):
        # TODO: Implement billItem method
        pass

    def getBill(self, id: int) -> str:
        # TODO: Implement getBill method
        pass

    def markBillAsPaid(self, bill: str, isPaid: bool, creditCardManager: str, bankingManager: str) -> bool:
        # TODO: Implement markBillAsPaid method
        pass

    def applyDiscount(self, discount: str, bill: str):
        # TODO: Implement applyDiscount method
        pass

    def createBill(self, customer: str) -> str:
        # TODO: Implement createBill method
        pass

    def publishBill(self, bill: str):
        # TODO: Implement publishBill method
        pass

    def createBookingBill(self, booking: str, customer: str) -> str:
        # TODO: Implement createBookingBill method
        pass

    def addSubBill(self, toBill: str, subBill: str):
        # TODO: Implement addSubBill method
        pass

class tda593_billing_Service:

    def __init__(self, id: int, price: float, name: str):
        self.id = id
        self.price = price
        self.name = name
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class billing_Service:

    pass
class tda593_billing_Purchase:

    def __init__(self, id: int, quantity: int, price: float, tda593_billing_Purchase: "billing_Service" = None):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.tda593_billing_Purchase = tda593_billing_Purchase
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
class tda593_billing_Discount(ABC):

    def __init__(self, code: str, name: str, tda593_billing_Discount: "billing_DiscountLimit" = None):
        self.code = code
        self.name = name
        self.tda593_billing_Discount = tda593_billing_Discount
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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

    def getPriceWithDiscount(self, price: float) -> float:
        # TODO: Implement getPriceWithDiscount method
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
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def isPublished(self) -> bool:
        return self.__isPublished

    @isPublished.setter
    def isPublished(self, isPublished: bool):
        self.__isPublished = isPublished

    @property
    def isPaid(self) -> bool:
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: bool):
        self.__isPaid = isPaid

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
                    

    def applyDiscount(self, discount: str):
        # TODO: Implement applyDiscount method
        pass

    def addSubBill(self, subBill: str):
        # TODO: Implement addSubBill method
        pass

    def getPrice(self) -> float:
        # TODO: Implement getPrice method
        pass

    def unregisterPurchase(self, purchase: str):
        # TODO: Implement unregisterPurchase method
        pass

    def removeDiscount(self, discount: str):
        # TODO: Implement removeDiscount method
        pass

    def unPublishBill(self):
        # TODO: Implement unPublishBill method
        pass

    def registerPurchase(self, purchase: str):
        # TODO: Implement registerPurchase method
        pass

    def removeSubBill(self, subBill: str):
        # TODO: Implement removeSubBill method
        pass

    def publishBill(self):
        # TODO: Implement publishBill method
        pass

class billing_DiscountDataService:

    pass
class DiscountManager:

    pass
class tda593_billing_AdminDiscountManager(DiscountManager):

    def __init__(self):
        
    def setAmountLimit(self, usesAmount: int, discount: str):
        # TODO: Implement setAmountLimit method
        pass

    def addPercentageDiscount(self, percentage: float, code: str, name: str) -> str:
        # TODO: Implement addPercentageDiscount method
        pass

    def createDiscountLimitForDiscount(self, users: str, usesAmount: int, to: date, from: date, discount: str):
        # TODO: Implement createDiscountLimitForDiscount method
        pass

    def addSumDiscount(self, code: str, name: str, sum: float) -> str:
        # TODO: Implement addSumDiscount method
        pass

    def addAllowedUsers(self, legalEntities: str, discount: str):
        # TODO: Implement addAllowedUsers method
        pass

    def setDateRangeLimit(self, discount: str, validTo: date, validFrom: date):
        # TODO: Implement setDateRangeLimit method
        pass

class tda593_billing_DiscountManagerImpl(DiscountManager):

    pass
class tda593_billing_DiscountDataService:

    pass
class Discount:

    pass
class tda593_billing_PercentageDiscount(Discount):

    def __init__(self, percentage: float):
        self.percentage = percentage
        
    @property
    def percentage(self) -> float:
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage: float):
        self.__percentage = percentage

class tda593_billing_SumDiscount(Discount):

    def __init__(self, discountSum: float):
        self.discountSum = discountSum
        
    @property
    def discountSum(self) -> float:
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
        
    @property
    def timesLeftToUse(self) -> int:
        return self.__timesLeftToUse

    @timesLeftToUse.setter
    def timesLeftToUse(self, timesLeftToUse: int):
        self.__timesLeftToUse = timesLeftToUse

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def startDate(self) -> date:
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
class Room:

    pass
class tda593_facilities_ConferenceRoom(Room):

    def __init__(self, equipment: str, numberOfSeats: int):
        self.equipment = equipment
        self.numberOfSeats = numberOfSeats
        
    @property
    def equipment(self) -> str:
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment: str):
        self.__equipment = equipment

    @property
    def numberOfSeats(self) -> int:
        return self.__numberOfSeats

    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: int):
        self.__numberOfSeats = numberOfSeats

class tda593_facilities_GuestRoom(Room):

    def __init__(self, numberOfBeds: int, numberOfExtrabeds: int):
        self.numberOfBeds = numberOfBeds
        self.numberOfExtrabeds = numberOfExtrabeds
        
    @property
    def numberOfExtrabeds(self) -> int:
        return self.__numberOfExtrabeds

    @numberOfExtrabeds.setter
    def numberOfExtrabeds(self, numberOfExtrabeds: int):
        self.__numberOfExtrabeds = numberOfExtrabeds

    @property
    def numberOfBeds(self) -> int:
        return self.__numberOfBeds

    @numberOfBeds.setter
    def numberOfBeds(self, numberOfBeds: int):
        self.__numberOfBeds = numberOfBeds

class facilities_RoomType:

    pass
class tda593_billing_DiscountManager(ABC):

    def __init__(self):
        
    def getDiscount(self, code: str) -> str:
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
class tda593_facilities_AdminRoomManagerImpl(facilities_AdminRoomManager, facilities_RoomManagerImpl):

    pass
class tda593_facilities_KeyCardDataService:

    pass
class facilities_KeyCardDataService:

    pass
class tda593_facilities_RoomTypeDataService:

    pass
class tda593_facilities_RoomDataService:

    def __init__(self):
        
    def getGuestRoom(self, id: str) -> str:
        # TODO: Implement getGuestRoom method
        pass

    def getAllConferenceRooms(self) -> str:
        # TODO: Implement getAllConferenceRooms method
        pass

    def getAllGuestRooms(self) -> str:
        # TODO: Implement getAllGuestRooms method
        pass

    def getConferenceRoom(self, id: str) -> str:
        # TODO: Implement getConferenceRoom method
        pass

class facilities_KeyCardManager:

    pass
class facilities_RoomTypeDataService:

    pass
class facilities_RoomDataService:

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
        
    @property
    def floor(self) -> int:
        return self.__floor

    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def isBeingCleaned(self) -> bool:
        return self.__isBeingCleaned

    @isBeingCleaned.setter
    def isBeingCleaned(self, isBeingCleaned: bool):
        self.__isBeingCleaned = isBeingCleaned

    @property
    def disabilityApprovals(self) -> str:
        return self.__disabilityApprovals

    @disabilityApprovals.setter
    def disabilityApprovals(self, disabilityApprovals: str):
        self.__disabilityApprovals = disabilityApprovals

    @property
    def isOperational(self) -> bool:
        return self.__isOperational

    @isOperational.setter
    def isOperational(self, isOperational: bool):
        self.__isOperational = isOperational

    @property
    def roomNumber(self) -> str:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: str):
        self.__roomNumber = roomNumber

    @property
    def photos(self) -> str:
        return self.__photos

    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

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
                    

    def unregisterKeyCard(self, keyCard: str):
        # TODO: Implement unregisterKeyCard method
        pass

    def registerKeyCard(self, keyCard: str):
        # TODO: Implement registerKeyCard method
        pass

    def unregisterKeyCards(self):
        # TODO: Implement unregisterKeyCards method
        pass

class tda593_facilities_RoomType:

    def __init__(self, name: str, description: str, roomApprovals: str, price: float):
        self.name = name
        self.description = description
        self.roomApprovals = roomApprovals
        self.price = price
        
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

    @property
    def roomApprovals(self) -> str:
        return self.__roomApprovals

    @roomApprovals.setter
    def roomApprovals(self, roomApprovals: str):
        self.__roomApprovals = roomApprovals

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

class tda593_facilities_RoomManager(ABC):

    def __init__(self):
        
    def getGuestRooms(self) -> str:
        # TODO: Implement getGuestRooms method
        pass

    def getRooms(self) -> str:
        # TODO: Implement getRooms method
        pass

    def getConferenceRooms(self) -> str:
        # TODO: Implement getConferenceRooms method
        pass

    def unregisterKeyCard(self, roomNumber: str, keyCard: str):
        # TODO: Implement unregisterKeyCard method
        pass

    def getRoomType(self, name: str) -> str:
        # TODO: Implement getRoomType method
        pass

    def setIsBeingCleaned(self, value: bool, room: str):
        # TODO: Implement setIsBeingCleaned method
        pass

    def registerKeyCard(self, roomNumber: str, keyCardNbr: str):
        # TODO: Implement registerKeyCard method
        pass

    def getRoomTypeAmount(self, roomType: str) -> int:
        # TODO: Implement getRoomTypeAmount method
        pass

    def getRoomTypeAmounts(self):
        # TODO: Implement getRoomTypeAmounts method
        pass

    def getRoomTypes(self) -> str:
        # TODO: Implement getRoomTypes method
        pass

    def getRoom(self, roomNumber: str) -> str:
        # TODO: Implement getRoom method
        pass

    def registerKeyCard(self, keyCard: str, roomNumber: str):
        # TODO: Implement registerKeyCard method
        pass

    def unregisterAllKeyCards(self, roomNumber: str):
        # TODO: Implement unregisterAllKeyCards method
        pass

    def unregisterKeyCard(self, keyCardNbr: str, roomNumber: str):
        # TODO: Implement unregisterKeyCard method
        pass

class RoomManager:

    pass
class tda593_facilities_RoomManagerImpl(RoomManager):

    pass
class tda593_facilities_AdminRoomManager(RoomManager):

    def __init__(self):
        
    def addRoomType(self, description: str, roomApprovals: str, name: str, price: float) -> str:
        # TODO: Implement addRoomType method
        pass

    def removeRoomType(self, roomType: str) -> bool:
        # TODO: Implement removeRoomType method
        pass

    def addGuestRoom(self, description: str, disabilityApprovals: str, numberOfExtraBeds: int, roomType: str, numberOfBeds: int, floor: int, photos: str, number: str) -> str:
        # TODO: Implement addGuestRoom method
        pass

    def addConferenceRoom(self, photos: str, numberOfSeats: int, description: str, disabilityApprovals: str, number: str, equipment: str, floor: int, roomType: str) -> str:
        # TODO: Implement addConferenceRoom method
        pass

    def removeRoom(self, roomNumber: str) -> bool:
        # TODO: Implement removeRoom method
        pass

class tda593_facilities_KeyCard:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class tda593_facilities_KeyCardManager(ABC):

    def __init__(self):
        
    def getKeyCard(self, keyCardNbr: str) -> str:
        # TODO: Implement getKeyCard method
        pass

class KeyCardManager:

    pass
class tda593_facilities_KeyCardManagerImpl(KeyCardManager):

    pass
class tda593_facilities_AdminKeyCardManager(KeyCardManager):

    def __init__(self):
        
    def addKeyCard(self, cardNumber: str):
        # TODO: Implement addKeyCard method
        pass

    def removeKeyCard(self, cardNumber: str):
        # TODO: Implement removeKeyCard method
        pass

class tda593_california_DataService(ABC):

    def __init__(self):
        
    def count(self) -> int:
        # TODO: Implement count method
        pass

    def delete(self, object: str):
        # TODO: Implement delete method
        pass

    def setAll(self, objects: str):
        # TODO: Implement setAll method
        pass

    def getAll(self):
        # TODO: Implement getAll method
        pass

    def set(self, object: str):
        # TODO: Implement set method
        pass

    def exist(self, object: str) -> bool:
        # TODO: Implement exist method
        pass

    def get(self, id: str):
        # TODO: Implement get method
        pass
