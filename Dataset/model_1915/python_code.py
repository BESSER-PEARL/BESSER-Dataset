from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventType(Enum):
    CHECK_IN = "CHECK_IN"
    CHECK_OUT = "CHECK_OUT"


############################################
# Definition of Classes
############################################

class se_roomManager_IRoom(ABC):

    def __init__(self):
        
        pass
    def getRoomNumber(self) :
        # TODO: Implement getRoomNumber method
        pass

    def setOccupied(self, se_status):
        # TODO: Implement setOccupied method
        pass

    def getExtraCostDescription(self) :
        # TODO: Implement getExtraCostDescription method
        pass

    def addExtraCost(self, se_extraCostPrice):
        # TODO: Implement addExtraCost method
        pass

    def isBlocked(self) :
        # TODO: Implement isBlocked method
        pass

    def setExtraCostDescription(self, se_extraCostDescription):
        # TODO: Implement setExtraCostDescription method
        pass

    def getExtraCostPrice(self) :
        # TODO: Implement getExtraCostPrice method
        pass

    def setRoomType(self, se_roomType):
        # TODO: Implement setRoomType method
        pass

    def setIsBlocked(self, se_blocked):
        # TODO: Implement setIsBlocked method
        pass

    def getRoomType(self) :
        # TODO: Implement getRoomType method
        pass

    def isOccupied(self) :
        # TODO: Implement isOccupied method
        pass

class IRoom:

    pass
class se_roomManager_Room(IRoom):

    def __init__(self, roomNumber: int, blocked: bool, extraCostDescriptions: str, extraCostPrice: float, occupied: bool, se_roomManager_Room: "roomManager_IRoomType" = None):
        self.roomNumber = roomNumber
        self.blocked = blocked
        self.extraCostDescriptions = extraCostDescriptions
        self.extraCostPrice = extraCostPrice
        self.occupied = occupied
        self.se_roomManager_Room = se_roomManager_Room
        
        pass
    @property
    def extraCostPrice(self):
        return self.__extraCostPrice

    @extraCostPrice.setter
    def extraCostPrice(self, extraCostPrice: float):
        self.__extraCostPrice = extraCostPrice


    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied


    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber


    @property
    def extraCostDescriptions(self):
        return self.__extraCostDescriptions

    @extraCostDescriptions.setter
    def extraCostDescriptions(self, extraCostDescriptions: str):
        self.__extraCostDescriptions = extraCostDescriptions


    @property
    def blocked(self):
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked


    @property
    def se_roomManager_Room(self):
        return self.__se_roomManager_Room

    @se_roomManager_Room.setter
    def se_roomManager_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_roomManager_Room__se_roomManager_Room", None)
        self.__se_roomManager_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roomManager_IRoomType17"):
                opp_val = getattr(old_value, "roomManager_IRoomType17", None)
                if opp_val == self:
                    setattr(old_value, "roomManager_IRoomType17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roomManager_IRoomType17"):
                opp_val = getattr(value, "roomManager_IRoomType17", None)
                setattr(value, "roomManager_IRoomType17", self)

class IHotelRoomProvider:

    pass
class se_roomManager_IHotelRoomManager(IHotelRoomProvider):

    def __init__(self):
        
        pass
    def removeRoom(self, se_roomNumber) :
        # TODO: Implement removeRoom method
        pass

    def addRoom(self, se_roomType, se_roomNumber) :
        # TODO: Implement addRoom method
        pass

    def changeRoomType(self, se_roomNumber, se_roomType) :
        # TODO: Implement changeRoomType method
        pass

    def addRoomType(self, se_numberOfBeds, se_price, se_name, se_description) :
        # TODO: Implement addRoomType method
        pass

    def blockRoom(self, se_roomNumber):
        # TODO: Implement blockRoom method
        pass

    def unblockRoom(self, se_roomNumber):
        # TODO: Implement unblockRoom method
        pass

    def updateRoomType(self, se_price, se_numberOfBeds, se_name, se_description, se_roomType):
        # TODO: Implement updateRoomType method
        pass

    def removeRoomType(self, se_roomType) :
        # TODO: Implement removeRoomType method
        pass

    def getRoomTypes(self) :
        # TODO: Implement getRoomTypes method
        pass

class se_roomManager_IHotelRoomProvider(ABC):

    def __init__(self):
        
        pass
    def getRooms(self) :
        # TODO: Implement getRooms method
        pass

class se_roomManager_IHotelStartupProvies(ABC):

    def __init__(self):
        
        pass
    def startup(self, se_numRoom):
        # TODO: Implement startup method
        pass

class IRoomType:

    pass
class se_roomManager_RoomType(IRoomType):

    def __init__(self, description: str, price: float, name: str, numberOfBeds: int):
        self.description = description
        self.price = price
        self.name = name
        self.numberOfBeds = numberOfBeds
        
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
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def numberOfBeds(self):
        return self.__numberOfBeds

    @numberOfBeds.setter
    def numberOfBeds(self, numberOfBeds: int):
        self.__numberOfBeds = numberOfBeds


class se_roomManager_IRoomType(ABC):

    def __init__(self):
        
        pass
    def getNumberOfBeds(self) :
        # TODO: Implement getNumberOfBeds method
        pass

    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

    def getPrice(self) :
        # TODO: Implement getPrice method
        pass

    def setDescription(self, se_description):
        # TODO: Implement setDescription method
        pass

    def getName(self) :
        # TODO: Implement getName method
        pass

    def setPrice(self, se_price):
        # TODO: Implement setPrice method
        pass

    def setName(self, se_name):
        # TODO: Implement setName method
        pass

    def setNumberOfBeds(self, se_beds):
        # TODO: Implement setNumberOfBeds method
        pass

class IBooking:

    pass
class se_bookingSystem_Booking(IBooking):

    def __init__(self, id: int, firstName: str, lastName: str, startDate: str, endDate: str, se_bookingSystem_Booking: set["roomManager_IRoom"] = None, se_bookingSystem_Booking10: set["roomManager_IRoom"] = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.startDate = startDate
        self.endDate = endDate
        self.se_bookingSystem_Booking = se_bookingSystem_Booking if se_bookingSystem_Booking is not None else set()
        self.se_bookingSystem_Booking10 = se_bookingSystem_Booking10 if se_bookingSystem_Booking10 is not None else set()
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def se_bookingSystem_Booking(self):
        return self.__se_bookingSystem_Booking

    @se_bookingSystem_Booking.setter
    def se_bookingSystem_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_Booking__se_bookingSystem_Booking", None)
        self.__se_bookingSystem_Booking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roomManager_IRoom8"):
                    opp_val = getattr(item, "roomManager_IRoom8", None)
                    
                    if opp_val == self:
                        setattr(item, "roomManager_IRoom8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roomManager_IRoom8"):
                    opp_val = getattr(item, "roomManager_IRoom8", None)
                    
                    setattr(item, "roomManager_IRoom8", self)
                    

    @property
    def se_bookingSystem_Booking10(self):
        return self.__se_bookingSystem_Booking10

    @se_bookingSystem_Booking10.setter
    def se_bookingSystem_Booking10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_Booking__se_bookingSystem_Booking10", None)
        self.__se_bookingSystem_Booking10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roomManager_IRoom11"):
                    opp_val = getattr(item, "roomManager_IRoom11", None)
                    
                    if opp_val == self:
                        setattr(item, "roomManager_IRoom11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roomManager_IRoom11"):
                    opp_val = getattr(item, "roomManager_IRoom11", None)
                    
                    setattr(item, "roomManager_IRoom11", self)
                    

class se_bookingSystem_FreeRoomTypesDTO:

    def __init__(self, roomTypeDescription: str, numBeds: int, pricePerNight: float, numFreeRooms: int):
        self.roomTypeDescription = roomTypeDescription
        self.numBeds = numBeds
        self.pricePerNight = pricePerNight
        self.numFreeRooms = numFreeRooms
        
        pass
    @property
    def pricePerNight(self):
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight


    @property
    def roomTypeDescription(self):
        return self.__roomTypeDescription

    @roomTypeDescription.setter
    def roomTypeDescription(self, roomTypeDescription: str):
        self.__roomTypeDescription = roomTypeDescription


    @property
    def numFreeRooms(self):
        return self.__numFreeRooms

    @numFreeRooms.setter
    def numFreeRooms(self, numFreeRooms: int):
        self.__numFreeRooms = numFreeRooms


    @property
    def numBeds(self):
        return self.__numBeds

    @numBeds.setter
    def numBeds(self, numBeds: int):
        self.__numBeds = numBeds


class roomManager_IRoomType:

    pass
class roomManager_IHotelRoomManager:

    pass
class roomManager_IHotelStartupProvies:

    pass
class se_bookingSystem_IHotelCustomerProvides(ABC):

    def __init__(self):
        
        pass
    def initiateRoomCheckout(self, se_roomNumber, se_bookingId) :
        # TODO: Implement initiateRoomCheckout method
        pass

    def payRoomDuringCheckout(self, se_firstName, se_expiryYear, se_expiryMonth, se_lastName, se_roomNumber, se_ccNumber, se_ccv) :
        # TODO: Implement payRoomDuringCheckout method
        pass

    def payDuringCheckout(self, se_lastName, se_ccNumber, se_ccv, se_expiryYear, se_firstName, se_expiryMonth) :
        # TODO: Implement payDuringCheckout method
        pass

    def addRoomToBooking(self, se_bookingID, se_roomTypeDescription) :
        # TODO: Implement addRoomToBooking method
        pass

    def confirmBooking(self, se_bookingID) :
        # TODO: Implement confirmBooking method
        pass

    def initiateBooking(self, se_endDate, se_lastName, se_startDate, se_firstName) :
        # TODO: Implement initiateBooking method
        pass

    def initiateCheckout(self, se_bookingID) :
        # TODO: Implement initiateCheckout method
        pass

    def getFreeRooms(self, se_endDate, se_numBeds, se_startDate) :
        # TODO: Implement getFreeRooms method
        pass

    def checkInRoom(self, se_bookingId, se_roomTypeDescription) :
        # TODO: Implement checkInRoom method
        pass

class se_bookingSystem_IBooking(ABC):

    def __init__(self):
        
        pass
    def setEndDate(self, se_endDate):
        # TODO: Implement setEndDate method
        pass

    def checkInRoom(self, se_roomToCheckIn) :
        # TODO: Implement checkInRoom method
        pass

    def getStartDate(self) :
        # TODO: Implement getStartDate method
        pass

    def getEndDate(self) :
        # TODO: Implement getEndDate method
        pass

    def addRoom(self, se_room) :
        # TODO: Implement addRoom method
        pass

    def setRooms(self, se_rooms):
        # TODO: Implement setRooms method
        pass

    def checkOutRoom(self, se_roomToCheckOut) :
        # TODO: Implement checkOutRoom method
        pass

    def getRooms(self) :
        # TODO: Implement getRooms method
        pass

    def setStartDate(self, se_startDate):
        # TODO: Implement setStartDate method
        pass

    def getLastName(self) :
        # TODO: Implement getLastName method
        pass

    def getFirstName(self) :
        # TODO: Implement getFirstName method
        pass

    def getID(self) :
        # TODO: Implement getID method
        pass

    def getCheckedInRooms(self) :
        # TODO: Implement getCheckedInRooms method
        pass

class roomManager_IRoom:

    pass
class roomManager_IHotelRoomProvider:

    pass
class se_roomManager_RoomManager(roomManager_IHotelStartupProvies, roomManager_IHotelRoomProvider, roomManager_IHotelRoomManager):

    pass
class bookingSystem_IBooking:

    pass
class bookingSystem_IEvent:

    pass
class bookingSystem_IHotelCustomerProvides:

    pass
class bookingSystem_IHotelBookingManager:

    pass
class se_bookingSystem_BookingSystem(bookingSystem_IHotelCustomerProvides, bookingSystem_IHotelBookingManager):

    def __init__(self, bookingId: int, se_bookingSystem_BookingSystem: set["bookingSystem_IEvent"] = None, se_bookingSystem_BookingSystem2: set["bookingSystem_IBooking"] = None, se_bookingSystem_BookingSystem4: "roomManager_IHotelRoomProvider" = None, se_bookingSystem_BookingSystem6: set["roomManager_IRoom"] = None):
        self.bookingId = bookingId
        self.se_bookingSystem_BookingSystem = se_bookingSystem_BookingSystem if se_bookingSystem_BookingSystem is not None else set()
        self.se_bookingSystem_BookingSystem2 = se_bookingSystem_BookingSystem2 if se_bookingSystem_BookingSystem2 is not None else set()
        self.se_bookingSystem_BookingSystem4 = se_bookingSystem_BookingSystem4
        self.se_bookingSystem_BookingSystem6 = se_bookingSystem_BookingSystem6 if se_bookingSystem_BookingSystem6 is not None else set()
        
        pass
    @property
    def bookingId(self):
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId


    @property
    def se_bookingSystem_BookingSystem4(self):
        return self.__se_bookingSystem_BookingSystem4

    @se_bookingSystem_BookingSystem4.setter
    def se_bookingSystem_BookingSystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_BookingSystem__se_bookingSystem_BookingSystem4", None)
        self.__se_bookingSystem_BookingSystem4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roomManager_IHotelRoomProvider"):
                opp_val = getattr(old_value, "roomManager_IHotelRoomProvider", None)
                if opp_val == self:
                    setattr(old_value, "roomManager_IHotelRoomProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roomManager_IHotelRoomProvider"):
                opp_val = getattr(value, "roomManager_IHotelRoomProvider", None)
                setattr(value, "roomManager_IHotelRoomProvider", self)

    @property
    def se_bookingSystem_BookingSystem2(self):
        return self.__se_bookingSystem_BookingSystem2

    @se_bookingSystem_BookingSystem2.setter
    def se_bookingSystem_BookingSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_BookingSystem__se_bookingSystem_BookingSystem2", None)
        self.__se_bookingSystem_BookingSystem2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingSystem_IBooking"):
                    opp_val = getattr(item, "bookingSystem_IBooking", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingSystem_IBooking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingSystem_IBooking"):
                    opp_val = getattr(item, "bookingSystem_IBooking", None)
                    
                    setattr(item, "bookingSystem_IBooking", self)
                    

    @property
    def se_bookingSystem_BookingSystem6(self):
        return self.__se_bookingSystem_BookingSystem6

    @se_bookingSystem_BookingSystem6.setter
    def se_bookingSystem_BookingSystem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_BookingSystem__se_bookingSystem_BookingSystem6", None)
        self.__se_bookingSystem_BookingSystem6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roomManager_IRoom"):
                    opp_val = getattr(item, "roomManager_IRoom", None)
                    
                    if opp_val == self:
                        setattr(item, "roomManager_IRoom", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roomManager_IRoom"):
                    opp_val = getattr(item, "roomManager_IRoom", None)
                    
                    setattr(item, "roomManager_IRoom", self)
                    

    @property
    def se_bookingSystem_BookingSystem(self):
        return self.__se_bookingSystem_BookingSystem

    @se_bookingSystem_BookingSystem.setter
    def se_bookingSystem_BookingSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_bookingSystem_BookingSystem__se_bookingSystem_BookingSystem", None)
        self.__se_bookingSystem_BookingSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookingSystem_IEvent"):
                    opp_val = getattr(item, "bookingSystem_IEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "bookingSystem_IEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookingSystem_IEvent"):
                    opp_val = getattr(item, "bookingSystem_IEvent", None)
                    
                    setattr(item, "bookingSystem_IEvent", self)
                    

class se_bookingSystem_IEvent(ABC):

    def __init__(self):
        
        pass
    def getType(self) :
        # TODO: Implement getType method
        pass

    def getTimestamp(self) :
        # TODO: Implement getTimestamp method
        pass

    def getBookingId(self) :
        # TODO: Implement getBookingId method
        pass

class IHotelCustomerProvides:

    pass
class se_bookingSystem_IHotelBookingManager(IHotelCustomerProvides):

    def __init__(self):
        
        pass
    def editBookingRooms(self, se_roomType, se_bookingID, se_numOfRooms):
        # TODO: Implement editBookingRooms method
        pass

    def listBooking(self) :
        # TODO: Implement listBooking method
        pass

    def cancelBooking(self, se_bookingId):
        # TODO: Implement cancelBooking method
        pass

    def listCheckouts(self, se_startTime, se_endTime) :
        # TODO: Implement listCheckouts method
        pass

    def addExtraCostToRoom(self, se_priceOfCost, se_bookingId, se_descriptionOfCost, se_roomNumber):
        # TODO: Implement addExtraCostToRoom method
        pass

    def editBookingPeriod(self, se_startDate, se_endDate, se_bookingId) :
        # TODO: Implement editBookingPeriod method
        pass

    def listOccupiedRooms(self, se_date) :
        # TODO: Implement listOccupiedRooms method
        pass

    def listCheckins(self, se_endTime, se_startTime) :
        # TODO: Implement listCheckins method
        pass

    def initiateCheckin(self, se_bookingId) :
        # TODO: Implement initiateCheckin method
        pass

class IEvent:

    pass
class se_bookingSystem_AbstractEvent(IEvent):

    def __init__(self, timestamp: str, eventType: str, bookingID: int):
        self.timestamp = timestamp
        self.eventType = eventType
        self.bookingID = bookingID
        
        pass
    @property
    def eventType(self):
        return self.__eventType

    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType


    @property
    def bookingID(self):
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: int):
        self.__bookingID = bookingID


    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp


class AbstractEvent:

    pass
class se_bookingSystem_CheckOutEvent(AbstractEvent):

    pass
class se_bookingSystem_CheckInEvent(AbstractEvent):

    pass