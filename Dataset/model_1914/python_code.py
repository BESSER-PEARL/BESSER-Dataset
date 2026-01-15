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
        
    def getRoomType(self) -> str:
        # TODO: Implement getRoomType method
        pass

    def setExtraCostDescription(self, extraCostDescription: str):
        # TODO: Implement setExtraCostDescription method
        pass

    def getExtraCostDescription(self) -> str:
        # TODO: Implement getExtraCostDescription method
        pass

    def setRoomType(self, roomType: str):
        # TODO: Implement setRoomType method
        pass

    def setOccupied(self, status: bool):
        # TODO: Implement setOccupied method
        pass

    def addExtraCost(self, extraCostPrice: float):
        # TODO: Implement addExtraCost method
        pass

    def getExtraCostPrice(self) -> float:
        # TODO: Implement getExtraCostPrice method
        pass

    def setIsBlocked(self, blocked: bool):
        # TODO: Implement setIsBlocked method
        pass

    def getRoomNumber(self) -> int:
        # TODO: Implement getRoomNumber method
        pass

    def isBlocked(self) -> bool:
        # TODO: Implement isBlocked method
        pass

    def isOccupied(self) -> bool:
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
        
    @property
    def blocked(self) -> bool:
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked

    @property
    def extraCostDescriptions(self) -> str:
        return self.__extraCostDescriptions

    @extraCostDescriptions.setter
    def extraCostDescriptions(self, extraCostDescriptions: str):
        self.__extraCostDescriptions = extraCostDescriptions

    @property
    def occupied(self) -> bool:
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied

    @property
    def extraCostPrice(self) -> float:
        return self.__extraCostPrice

    @extraCostPrice.setter
    def extraCostPrice(self, extraCostPrice: float):
        self.__extraCostPrice = extraCostPrice

    @property
    def roomNumber(self) -> int:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber

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
        
    def changeRoomType(self, roomNumber: int, roomType: str) -> bool:
        # TODO: Implement changeRoomType method
        pass

    def removeRoom(self, roomNumber: int) -> str:
        # TODO: Implement removeRoom method
        pass

    def getRoomTypes(self) -> str:
        # TODO: Implement getRoomTypes method
        pass

    def addRoom(self, roomNumber: int, roomType: str) -> bool:
        # TODO: Implement addRoom method
        pass

    def removeRoomType(self, roomType: str) -> str:
        # TODO: Implement removeRoomType method
        pass

    def blockRoom(self, roomNumber: int):
        # TODO: Implement blockRoom method
        pass

    def unblockRoom(self, roomNumber: int):
        # TODO: Implement unblockRoom method
        pass

    def addRoomType(self, name: str, price: float, description: str, numberOfBeds: int) -> bool:
        # TODO: Implement addRoomType method
        pass

    def updateRoomType(self, name: str, price: float, numberOfBeds: int, roomType: str, description: str):
        # TODO: Implement updateRoomType method
        pass

class se_roomManager_IHotelRoomProvider(ABC):

    def __init__(self):
        
    def getRooms(self) -> str:
        # TODO: Implement getRooms method
        pass

class se_roomManager_IHotelStartupProvies(ABC):

    def __init__(self):
        
    def startup(self, numRoom: int):
        # TODO: Implement startup method
        pass

class roomManager_IRoomType:

    pass
class roomManager_IHotelRoomManager:

    pass
class roomManager_IHotelStartupProvies:

    pass
class IRoomType:

    pass
class se_roomManager_RoomType(IRoomType):

    def __init__(self, price: float, name: str, numberOfBeds: int, description: str):
        self.price = price
        self.name = name
        self.numberOfBeds = numberOfBeds
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def numberOfBeds(self) -> int:
        return self.__numberOfBeds

    @numberOfBeds.setter
    def numberOfBeds(self, numberOfBeds: int):
        self.__numberOfBeds = numberOfBeds

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

class se_roomManager_IRoomType(ABC):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getPrice(self) -> float:
        # TODO: Implement getPrice method
        pass

    def setPrice(self, price: float):
        # TODO: Implement setPrice method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

    def setName(self, name: str):
        # TODO: Implement setName method
        pass

    def setNumberOfBeds(self, beds: int):
        # TODO: Implement setNumberOfBeds method
        pass

    def getNumberOfBeds(self) -> int:
        # TODO: Implement getNumberOfBeds method
        pass

class IBooking:

    pass
class se_bookingSystem_Booking(IBooking):

    def __init__(self, lastName: str, id: int, firstName: str, startDate: str, endDate: str, se_bookingSystem_Booking: set["roomManager_IRoom"] = None, se_bookingSystem_Booking10: set["roomManager_IRoom"] = None):
        self.lastName = lastName
        self.id = id
        self.firstName = firstName
        self.startDate = startDate
        self.endDate = endDate
        self.se_bookingSystem_Booking = se_bookingSystem_Booking if se_bookingSystem_Booking is not None else set()
        self.se_bookingSystem_Booking10 = se_bookingSystem_Booking10 if se_bookingSystem_Booking10 is not None else set()
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

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
        
    @property
    def pricePerNight(self) -> float:
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight

    @property
    def numFreeRooms(self) -> int:
        return self.__numFreeRooms

    @numFreeRooms.setter
    def numFreeRooms(self, numFreeRooms: int):
        self.__numFreeRooms = numFreeRooms

    @property
    def roomTypeDescription(self) -> str:
        return self.__roomTypeDescription

    @roomTypeDescription.setter
    def roomTypeDescription(self, roomTypeDescription: str):
        self.__roomTypeDescription = roomTypeDescription

    @property
    def numBeds(self) -> int:
        return self.__numBeds

    @numBeds.setter
    def numBeds(self, numBeds: int):
        self.__numBeds = numBeds

class se_bookingSystem_IHotelCustomerProvides(ABC):

    def __init__(self):
        
    def checkInRoom(self, bookingId: int, roomTypeDescription: str) -> int:
        # TODO: Implement checkInRoom method
        pass

    def getFreeRooms(self, endDate: str, numBeds: int, startDate: str) -> str:
        # TODO: Implement getFreeRooms method
        pass

    def initiateCheckout(self, bookingID: int) -> float:
        # TODO: Implement initiateCheckout method
        pass

    def confirmBooking(self, bookingID: int) -> bool:
        # TODO: Implement confirmBooking method
        pass

    def initiateRoomCheckout(self, roomNumber: int, bookingId: int) -> float:
        # TODO: Implement initiateRoomCheckout method
        pass

    def initiateBooking(self, startDate: str, endDate: str, lastName: str, firstName: str) -> int:
        # TODO: Implement initiateBooking method
        pass

    def addRoomToBooking(self, roomTypeDescription: str, bookingID: int) -> bool:
        # TODO: Implement addRoomToBooking method
        pass

    def payRoomDuringCheckout(self, lastName: str, ccv: str, expiryYear: int, firstName: str, ccNumber: str, roomNumber: int, expiryMonth: int) -> bool:
        # TODO: Implement payRoomDuringCheckout method
        pass

    def payDuringCheckout(self, firstName: str, lastName: str, expiryYear: int, expiryMonth: int, ccv: str, ccNumber: str) -> bool:
        # TODO: Implement payDuringCheckout method
        pass

class IHotelCustomerProvides:

    pass
class se_bookingSystem_IHotelBookingManager(IHotelCustomerProvides):

    def __init__(self):
        
    def listBooking(self) -> str:
        # TODO: Implement listBooking method
        pass

    def listCheckouts(self, endTime: str, startTime: str) -> str:
        # TODO: Implement listCheckouts method
        pass

    def editBookingRooms(self, numOfRooms: int, bookingID: int, roomType: str):
        # TODO: Implement editBookingRooms method
        pass

    def listCheckins(self, startTime: str, endTime: str) -> str:
        # TODO: Implement listCheckins method
        pass

    def addExtraCostToRoom(self, priceOfCost: float, roomNumber: int, bookingId: int, descriptionOfCost: str):
        # TODO: Implement addExtraCostToRoom method
        pass

    def editBookingPeriod(self, startDate: str, endDate: str, bookingId: int) -> bool:
        # TODO: Implement editBookingPeriod method
        pass

    def cancelBooking(self, bookingId: int):
        # TODO: Implement cancelBooking method
        pass

    def listOccupiedRooms(self, date: str) -> str:
        # TODO: Implement listOccupiedRooms method
        pass

    def initiateCheckin(self, bookingId: int) -> str:
        # TODO: Implement initiateCheckin method
        pass

class se_bookingSystem_IBooking(ABC):

    def __init__(self):
        
    def getRooms(self) -> str:
        # TODO: Implement getRooms method
        pass

    def getEndDate(self) -> str:
        # TODO: Implement getEndDate method
        pass

    def setStartDate(self, startDate: str):
        # TODO: Implement setStartDate method
        pass

    def getCheckedInRooms(self) -> str:
        # TODO: Implement getCheckedInRooms method
        pass

    def setRooms(self, rooms: str):
        # TODO: Implement setRooms method
        pass

    def checkOutRoom(self, roomToCheckOut: str) -> bool:
        # TODO: Implement checkOutRoom method
        pass

    def getLastName(self) -> str:
        # TODO: Implement getLastName method
        pass

    def checkInRoom(self, roomToCheckIn: str) -> bool:
        # TODO: Implement checkInRoom method
        pass

    def getStartDate(self) -> str:
        # TODO: Implement getStartDate method
        pass

    def getID(self) -> int:
        # TODO: Implement getID method
        pass

    def setEndDate(self, endDate: str):
        # TODO: Implement setEndDate method
        pass

    def addRoom(self, room: str) -> bool:
        # TODO: Implement addRoom method
        pass

    def getFirstName(self) -> str:
        # TODO: Implement getFirstName method
        pass

class roomManager_IRoom:

    pass
class roomManager_IHotelRoomProvider:

    pass
class se_roomManager_RoomManager(roomManager_IHotelRoomProvider, roomManager_IHotelRoomManager, roomManager_IHotelStartupProvies):

    pass
class bookingSystem_IBooking:

    pass
class bookingSystem_IEvent:

    pass
class bookingSystem_IHotelCustomerProvides:

    pass
class bookingSystem_IHotelBookingManager:

    pass
class se_bookingSystem_BookingSystem(bookingSystem_IHotelBookingManager, bookingSystem_IHotelCustomerProvides):

    def __init__(self, bookingId: int, se_bookingSystem_BookingSystem: set["bookingSystem_IEvent"] = None, se_bookingSystem_BookingSystem2: set["bookingSystem_IBooking"] = None, se_bookingSystem_BookingSystem6: set["roomManager_IRoom"] = None, se_bookingSystem_BookingSystem4: "roomManager_IHotelRoomProvider" = None):
        self.bookingId = bookingId
        self.se_bookingSystem_BookingSystem = se_bookingSystem_BookingSystem if se_bookingSystem_BookingSystem is not None else set()
        self.se_bookingSystem_BookingSystem2 = se_bookingSystem_BookingSystem2 if se_bookingSystem_BookingSystem2 is not None else set()
        self.se_bookingSystem_BookingSystem6 = se_bookingSystem_BookingSystem6 if se_bookingSystem_BookingSystem6 is not None else set()
        self.se_bookingSystem_BookingSystem4 = se_bookingSystem_BookingSystem4
        
    @property
    def bookingId(self) -> int:
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
                    

class se_bookingSystem_IEvent(ABC):

    def __init__(self):
        
    def getTimestamp(self) -> str:
        # TODO: Implement getTimestamp method
        pass

    def getBookingId(self) -> int:
        # TODO: Implement getBookingId method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class IEvent:

    pass
class se_bookingSystem_AbstractEvent(IEvent):

    def __init__(self, eventType: str, bookingID: int, timestamp: str):
        self.eventType = eventType
        self.bookingID = bookingID
        self.timestamp = timestamp
        
    @property
    def bookingID(self) -> int:
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: int):
        self.__bookingID = bookingID

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def eventType(self) -> str:
        return self.__eventType

    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

class AbstractEvent:

    pass
class se_bookingSystem_CheckOutEvent(AbstractEvent):

    pass
class se_bookingSystem_CheckInEvent(AbstractEvent):

    pass