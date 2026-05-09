from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class se_hotelsystem_IHotelStartupProvides(ABC):

    def __init__(self):
        
        pass
    def startup(self, se_numRooms):
        # TODO: Implement startup method
        pass

class se_hotelsystem_IHotelAdministratorProvides(ABC):

    def __init__(self):
        
        pass
    def blockRoom(self, se_roomNumber) :
        # TODO: Implement blockRoom method
        pass

    def unblockRoom(self, se_roomNumber) :
        # TODO: Implement unblockRoom method
        pass

    def addRoom(self, se_roomNumber, se_roomTypeName) :
        # TODO: Implement addRoom method
        pass

    def removeRoom(self, se_roomNumber) :
        # TODO: Implement removeRoom method
        pass

    def changeRoomType(self, se_roomTypeName, se_roomNumber) :
        # TODO: Implement changeRoomType method
        pass

    def editRoomType(self, se_nbrOfBeds, se_roomTypeName, se_featuresDescription, se_price) :
        # TODO: Implement editRoomType method
        pass

    def addRoomType(self, se_nbrOfBeds, se_featureDescription, se_roomTypeName, se_price) :
        # TODO: Implement addRoomType method
        pass

    def removeRoomType(self, se_roomTypeName) :
        # TODO: Implement removeRoomType method
        pass

class hotelsystem_IHotelAdministratorProvides:

    pass
class se_hotelsystem_FreeRoomTypesDTO:

    def __init__(self, roomTypeDescription: str, numBeds: int, pricePerNight: float, numFreeRooms: int):
        self.roomTypeDescription = roomTypeDescription
        self.numBeds = numBeds
        self.pricePerNight = pricePerNight
        self.numFreeRooms = numFreeRooms
        
        pass
    @property
    def roomTypeDescription(self):
        return self.__roomTypeDescription

    @roomTypeDescription.setter
    def roomTypeDescription(self, roomTypeDescription: str):
        self.__roomTypeDescription = roomTypeDescription


    @property
    def pricePerNight(self):
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight


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


class se_hotelsystem_IHotelCustomerProvides(ABC):

    def __init__(self):
        
        pass
    def addRoomToBooking(self, se_roomTypeName, se_bookingID) :
        # TODO: Implement addRoomToBooking method
        pass

    def getFreeRooms(self, se_endDate, se_startDate, se_numBeds) :
        # TODO: Implement getFreeRooms method
        pass

    def confirmBooking(self, se_bookingID) :
        # TODO: Implement confirmBooking method
        pass

    def payDuringCheckout(self, se_expiryMonth, se_ccNumber, se_expiryYear, se_firstName, se_ccv, se_lastName) :
        # TODO: Implement payDuringCheckout method
        pass

    def payRoomDuringCheckout(self, se_roomNumber, se_ccv, se_expiryYear, se_expiryMonth, se_ccNumber, se_lastName, se_firstName) :
        # TODO: Implement payRoomDuringCheckout method
        pass

    def initiateRoomCheckout(self, se_roomNumber, se_bookingId) :
        # TODO: Implement initiateRoomCheckout method
        pass

    def checkInRoom(self, se_roomTypeName, se_bookindId) :
        # TODO: Implement checkInRoom method
        pass

    def initiateBooking(self, se_firstName, se_startDate, se_endDate, se_lastName) :
        # TODO: Implement initiateBooking method
        pass

    def initiateCheckout(self, se_bookingID) :
        # TODO: Implement initiateCheckout method
        pass

class se_hotelsystem_PaymentHandler:

    def __init__(self, se_hotelsystem_PaymentHandler: "bankcomponents_ICustomerProvides" = None):
        self.se_hotelsystem_PaymentHandler = se_hotelsystem_PaymentHandler
        
        pass
    @property
    def se_hotelsystem_PaymentHandler(self):
        return self.__se_hotelsystem_PaymentHandler

    @se_hotelsystem_PaymentHandler.setter
    def se_hotelsystem_PaymentHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_PaymentHandler__se_hotelsystem_PaymentHandler", None)
        self.__se_hotelsystem_PaymentHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bankcomponents_ICustomerProvides"):
                opp_val = getattr(old_value, "bankcomponents_ICustomerProvides", None)
                if opp_val == self:
                    setattr(old_value, "bankcomponents_ICustomerProvides", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bankcomponents_ICustomerProvides"):
                opp_val = getattr(value, "bankcomponents_ICustomerProvides", None)
                setattr(value, "bankcomponents_ICustomerProvides", self)

    def payIfCardValid(self, se_ccv, se_sum, se_firstName, se_expiryMonth, se_expiryYear, se_lastName, se_ccNumber) :
        # TODO: Implement payIfCardValid method
        pass

class se_hotelsystem_Bill:

    def __init__(self, price: float, billID: int, se_hotelsystem_Bill: "hotelsystem_RoomReservation" = None):
        self.price = price
        self.billID = billID
        self.se_hotelsystem_Bill = se_hotelsystem_Bill
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def billID(self):
        return self.__billID

    @billID.setter
    def billID(self, billID: int):
        self.__billID = billID


    @property
    def se_hotelsystem_Bill(self):
        return self.__se_hotelsystem_Bill

    @se_hotelsystem_Bill.setter
    def se_hotelsystem_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_Bill__se_hotelsystem_Bill", None)
        self.__se_hotelsystem_Bill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_RoomReservation18"):
                opp_val = getattr(old_value, "hotelsystem_RoomReservation18", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_RoomReservation18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_RoomReservation18"):
                opp_val = getattr(value, "hotelsystem_RoomReservation18", None)
                setattr(value, "hotelsystem_RoomReservation18", self)

class se_hotelsystem_IHotelReceptionistProvides(ABC):

    def __init__(self):
        
        pass
    def getFreeRoom(self, se_startDate, se_roomType, se_endDate) :
        # TODO: Implement getFreeRoom method
        pass

    def checkIn(self, se_bookingId, se_roomNumbers) :
        # TODO: Implement checkIn method
        pass

    def listFreeRooms(self, se_bookingId) :
        # TODO: Implement listFreeRooms method
        pass

    def addExtraToRoom(self, se_roomNumber, se_extraDescription, se_price, se_bookingId) :
        # TODO: Implement addExtraToRoom method
        pass

    def listCheckins(self, se_startDate, se_endDate) :
        # TODO: Implement listCheckins method
        pass

    def listOccupiedRooms(self, se_date) :
        # TODO: Implement listOccupiedRooms method
        pass

    def editBookingTime(self, se_reservationId, se_endDate, se_startDate) :
        # TODO: Implement editBookingTime method
        pass

    def listCheckouts(self, se_endDate, se_startDate) :
        # TODO: Implement listCheckouts method
        pass

    def listBookings(self) :
        # TODO: Implement listBookings method
        pass

    def cancelBooking(self, se_bookingId) :
        # TODO: Implement cancelBooking method
        pass

    def removeRoomTypeFromBooking(self, se_nbrToRemove, se_roomType, se_bookingId) :
        # TODO: Implement removeRoomTypeFromBooking method
        pass

    def addRoomTypeToBooking(self, se_numberOfRoomsForType, se_bookingId, se_roomTypeName) :
        # TODO: Implement addRoomTypeToBooking method
        pass

class se_hotelsystem_IRoomHandler(ABC):

    def __init__(self):
        
        pass
    def getAllRoomsByType(self, se_roomType) :
        # TODO: Implement getAllRoomsByType method
        pass

    def getAllRooms(self) :
        # TODO: Implement getAllRooms method
        pass

    def getFreeRooms(self) :
        # TODO: Implement getFreeRooms method
        pass

    def getRoomType(self, se_roomTypeName) :
        # TODO: Implement getRoomType method
        pass

    def getFreeRoomByType(self, se_roomType) :
        # TODO: Implement getFreeRoomByType method
        pass

    def getAllRoomTypes(self, se_nrOfBeds) :
        # TODO: Implement getAllRoomTypes method
        pass

class bankcomponents_ICustomerProvides:

    pass
class se_hotelsystem_RoomReservation:

    def __init__(self, startDate: str, endDate: str, checkInDate: str, checkOuDate: str, se_hotelsystem_RoomReservation: "hotelsystem_RoomType" = None, se_hotelsystem_RoomReservation12: set["hotelsystem_RoomExtra"] = None, se_hotelsystem_RoomReservation14: "hotelsystem_Room" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.checkInDate = checkInDate
        self.checkOuDate = checkOuDate
        self.se_hotelsystem_RoomReservation = se_hotelsystem_RoomReservation
        self.se_hotelsystem_RoomReservation12 = se_hotelsystem_RoomReservation12 if se_hotelsystem_RoomReservation12 is not None else set()
        self.se_hotelsystem_RoomReservation14 = se_hotelsystem_RoomReservation14
        
        pass
    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate


    @property
    def checkInDate(self):
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate


    @property
    def checkOuDate(self):
        return self.__checkOuDate

    @checkOuDate.setter
    def checkOuDate(self, checkOuDate: str):
        self.__checkOuDate = checkOuDate


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate


    @property
    def se_hotelsystem_RoomReservation14(self):
        return self.__se_hotelsystem_RoomReservation14

    @se_hotelsystem_RoomReservation14.setter
    def se_hotelsystem_RoomReservation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_RoomReservation__se_hotelsystem_RoomReservation14", None)
        self.__se_hotelsystem_RoomReservation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_Room"):
                opp_val = getattr(old_value, "hotelsystem_Room", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_Room"):
                opp_val = getattr(value, "hotelsystem_Room", None)
                setattr(value, "hotelsystem_Room", self)

    @property
    def se_hotelsystem_RoomReservation12(self):
        return self.__se_hotelsystem_RoomReservation12

    @se_hotelsystem_RoomReservation12.setter
    def se_hotelsystem_RoomReservation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_RoomReservation__se_hotelsystem_RoomReservation12", None)
        self.__se_hotelsystem_RoomReservation12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_RoomExtra"):
                    opp_val = getattr(item, "hotelsystem_RoomExtra", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_RoomExtra", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_RoomExtra"):
                    opp_val = getattr(item, "hotelsystem_RoomExtra", None)
                    
                    setattr(item, "hotelsystem_RoomExtra", self)
                    

    @property
    def se_hotelsystem_RoomReservation(self):
        return self.__se_hotelsystem_RoomReservation

    @se_hotelsystem_RoomReservation.setter
    def se_hotelsystem_RoomReservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_RoomReservation__se_hotelsystem_RoomReservation", None)
        self.__se_hotelsystem_RoomReservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_RoomType"):
                opp_val = getattr(old_value, "hotelsystem_RoomType", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_RoomType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_RoomType"):
                opp_val = getattr(value, "hotelsystem_RoomType", None)
                setattr(value, "hotelsystem_RoomType", self)

    def getRoomIfOccupied(self, se_date) :
        # TODO: Implement getRoomIfOccupied method
        pass

    def getRoomId(self) :
        # TODO: Implement getRoomId method
        pass

    def checkOut(self, se_nrOfNights) :
        # TODO: Implement checkOut method
        pass

    def addExtra(self, se_extra):
        # TODO: Implement addExtra method
        pass

    def checkIn(self):
        # TODO: Implement checkIn method
        pass

class se_hotelsystem_Customer:

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
        pass
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


class hotelsystem_Bill:

    pass
class se_hotelsystem_Room:

    def __init__(self, occupied: bool, blocked: bool, roomNumber: int, se_hotelsystem_Room: "hotelsystem_RoomType" = None):
        self.occupied = occupied
        self.blocked = blocked
        self.roomNumber = roomNumber
        self.se_hotelsystem_Room = se_hotelsystem_Room
        
        pass
    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber


    @property
    def blocked(self):
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked


    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied


    @property
    def se_hotelsystem_Room(self):
        return self.__se_hotelsystem_Room

    @se_hotelsystem_Room.setter
    def se_hotelsystem_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_Room__se_hotelsystem_Room", None)
        self.__se_hotelsystem_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_RoomType16"):
                opp_val = getattr(old_value, "hotelsystem_RoomType16", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_RoomType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_RoomType16"):
                opp_val = getattr(value, "hotelsystem_RoomType16", None)
                setattr(value, "hotelsystem_RoomType16", self)

class se_hotelsystem_RoomExtra:

    def __init__(self, price: float, description: str):
        self.price = price
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


class se_hotelsystem_RoomType:

    def __init__(self, description: str, numBeds: int, pricePerNight: float, name: str):
        self.description = description
        self.numBeds = numBeds
        self.pricePerNight = pricePerNight
        self.name = name
        
        pass
    @property
    def numBeds(self):
        return self.__numBeds

    @numBeds.setter
    def numBeds(self, numBeds: int):
        self.__numBeds = numBeds


    @property
    def pricePerNight(self):
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight


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


class hotelsystem_Room:

    pass
class hotelsystem_RoomExtra:

    pass
class hotelsystem_RoomType:

    pass
class hotelsystem_IHotelCustomerProvides:

    pass
class hotelsystem_IHotelReceptionistProvides:

    pass
class se_hotelsystem_BookingHandler(hotelsystem_IHotelReceptionistProvides, hotelsystem_IHotelCustomerProvides):

    def __init__(self, bookingCurrentlyCheckingOut: int, nextBookingId: int, se_hotelsystem_BookingHandler: set["hotelsystem_Booking"] = None, se_hotelsystem_BookingHandler2: "hotelsystem_PaymentHandler" = None, se_hotelsystem_BookingHandler4: "hotelsystem_IRoomHandler" = None, hotelsystem_IHotelReceptionistProvides: "se_actor_Receptionist" = None, hotelsystem_IHotelCustomerProvides: "se_actor_Receptionist" = None):
        self.bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut
        self.nextBookingId = nextBookingId
        self.se_hotelsystem_BookingHandler = se_hotelsystem_BookingHandler if se_hotelsystem_BookingHandler is not None else set()
        self.se_hotelsystem_BookingHandler2 = se_hotelsystem_BookingHandler2
        self.se_hotelsystem_BookingHandler4 = se_hotelsystem_BookingHandler4
        
        pass
    @property
    def nextBookingId(self):
        return self.__nextBookingId

    @nextBookingId.setter
    def nextBookingId(self, nextBookingId: int):
        self.__nextBookingId = nextBookingId


    @property
    def bookingCurrentlyCheckingOut(self):
        return self.__bookingCurrentlyCheckingOut

    @bookingCurrentlyCheckingOut.setter
    def bookingCurrentlyCheckingOut(self, bookingCurrentlyCheckingOut: int):
        self.__bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut


    @property
    def se_hotelsystem_BookingHandler(self):
        return self.__se_hotelsystem_BookingHandler

    @se_hotelsystem_BookingHandler.setter
    def se_hotelsystem_BookingHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_BookingHandler__se_hotelsystem_BookingHandler", None)
        self.__se_hotelsystem_BookingHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_Booking"):
                    opp_val = getattr(item, "hotelsystem_Booking", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_Booking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_Booking"):
                    opp_val = getattr(item, "hotelsystem_Booking", None)
                    
                    setattr(item, "hotelsystem_Booking", self)
                    

    @property
    def se_hotelsystem_BookingHandler4(self):
        return self.__se_hotelsystem_BookingHandler4

    @se_hotelsystem_BookingHandler4.setter
    def se_hotelsystem_BookingHandler4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_BookingHandler__se_hotelsystem_BookingHandler4", None)
        self.__se_hotelsystem_BookingHandler4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_IRoomHandler"):
                opp_val = getattr(old_value, "hotelsystem_IRoomHandler", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_IRoomHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_IRoomHandler"):
                opp_val = getattr(value, "hotelsystem_IRoomHandler", None)
                setattr(value, "hotelsystem_IRoomHandler", self)

    @property
    def se_hotelsystem_BookingHandler2(self):
        return self.__se_hotelsystem_BookingHandler2

    @se_hotelsystem_BookingHandler2.setter
    def se_hotelsystem_BookingHandler2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_BookingHandler__se_hotelsystem_BookingHandler2", None)
        self.__se_hotelsystem_BookingHandler2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_PaymentHandler"):
                opp_val = getattr(old_value, "hotelsystem_PaymentHandler", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_PaymentHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_PaymentHandler"):
                opp_val = getattr(value, "hotelsystem_PaymentHandler", None)
                setattr(value, "hotelsystem_PaymentHandler", self)

    def isFree(self, se_endDate, se_roomId, se_startDate) :
        # TODO: Implement isFree method
        pass

    def getBookingById(self, se_bookingId) :
        # TODO: Implement getBookingById method
        pass

class hotelsystem_RoomReservation:

    pass
class hotelsystem_Customer:

    pass
class se_hotelsystem_Booking:

    def __init__(self, startDate: str, endDate: str, canceled: bool, bookingId: int, confirmed: bool, se_hotelsystem_Booking: "hotelsystem_Customer" = None, se_hotelsystem_Booking7: set["hotelsystem_RoomReservation"] = None, se_hotelsystem_Booking9: set["hotelsystem_Bill"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.canceled = canceled
        self.bookingId = bookingId
        self.confirmed = confirmed
        self.se_hotelsystem_Booking = se_hotelsystem_Booking
        self.se_hotelsystem_Booking7 = se_hotelsystem_Booking7 if se_hotelsystem_Booking7 is not None else set()
        self.se_hotelsystem_Booking9 = se_hotelsystem_Booking9 if se_hotelsystem_Booking9 is not None else set()
        
        pass
    @property
    def confirmed(self):
        return self.__confirmed

    @confirmed.setter
    def confirmed(self, confirmed: bool):
        self.__confirmed = confirmed


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
    def bookingId(self):
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId


    @property
    def canceled(self):
        return self.__canceled

    @canceled.setter
    def canceled(self, canceled: bool):
        self.__canceled = canceled


    @property
    def se_hotelsystem_Booking7(self):
        return self.__se_hotelsystem_Booking7

    @se_hotelsystem_Booking7.setter
    def se_hotelsystem_Booking7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_Booking__se_hotelsystem_Booking7", None)
        self.__se_hotelsystem_Booking7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_RoomReservation"):
                    opp_val = getattr(item, "hotelsystem_RoomReservation", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_RoomReservation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_RoomReservation"):
                    opp_val = getattr(item, "hotelsystem_RoomReservation", None)
                    
                    setattr(item, "hotelsystem_RoomReservation", self)
                    

    @property
    def se_hotelsystem_Booking(self):
        return self.__se_hotelsystem_Booking

    @se_hotelsystem_Booking.setter
    def se_hotelsystem_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_Booking__se_hotelsystem_Booking", None)
        self.__se_hotelsystem_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotelsystem_Customer"):
                opp_val = getattr(old_value, "hotelsystem_Customer", None)
                if opp_val == self:
                    setattr(old_value, "hotelsystem_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotelsystem_Customer"):
                opp_val = getattr(value, "hotelsystem_Customer", None)
                setattr(value, "hotelsystem_Customer", self)

    @property
    def se_hotelsystem_Booking9(self):
        return self.__se_hotelsystem_Booking9

    @se_hotelsystem_Booking9.setter
    def se_hotelsystem_Booking9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_Booking__se_hotelsystem_Booking9", None)
        self.__se_hotelsystem_Booking9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_Bill"):
                    opp_val = getattr(item, "hotelsystem_Bill", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_Bill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_Bill"):
                    opp_val = getattr(item, "hotelsystem_Bill", None)
                    
                    setattr(item, "hotelsystem_Bill", self)
                    

    def checkIn(self, se_room) :
        # TODO: Implement checkIn method
        pass

    def cancel(self):
        # TODO: Implement cancel method
        pass

    def checkOut(self) :
        # TODO: Implement checkOut method
        pass

    def addExtra(self, se_extra, se_roomNbr) :
        # TODO: Implement addExtra method
        pass

    def checkOutRoom(self, se_roomNumber) :
        # TODO: Implement checkOutRoom method
        pass

    def isCheckedIn(self) :
        # TODO: Implement isCheckedIn method
        pass

    def nrOfNights(self) :
        # TODO: Implement nrOfNights method
        pass

    def getRoomPrice(self, se_roomNumber) :
        # TODO: Implement getRoomPrice method
        pass

    def getOccupiedRooms(self, se_date) :
        # TODO: Implement getOccupiedRooms method
        pass

    def getBookingPrice(self) :
        # TODO: Implement getBookingPrice method
        pass

    def isFree(self, se_endDate, se_roomId, se_startDate) :
        # TODO: Implement isFree method
        pass

class hotelsystem_IRoomHandler:

    pass
class se_hotelsystem_RoomHandler(hotelsystem_IHotelAdministratorProvides, hotelsystem_IRoomHandler):

    def __init__(self, se_hotelsystem_RoomHandler: set["hotelsystem_RoomType"] = None, se_hotelsystem_RoomHandler23: set["hotelsystem_Room"] = None, hotelsystem_IRoomHandler: "se_hotelsystem_BookingHandler" = None, hotelsystem_IHotelAdministratorProvides: "se_actor_Administrator" = None):
        self.se_hotelsystem_RoomHandler = se_hotelsystem_RoomHandler if se_hotelsystem_RoomHandler is not None else set()
        self.se_hotelsystem_RoomHandler23 = se_hotelsystem_RoomHandler23 if se_hotelsystem_RoomHandler23 is not None else set()
        
        pass
    @property
    def se_hotelsystem_RoomHandler23(self):
        return self.__se_hotelsystem_RoomHandler23

    @se_hotelsystem_RoomHandler23.setter
    def se_hotelsystem_RoomHandler23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_RoomHandler__se_hotelsystem_RoomHandler23", None)
        self.__se_hotelsystem_RoomHandler23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_Room24"):
                    opp_val = getattr(item, "hotelsystem_Room24", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_Room24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_Room24"):
                    opp_val = getattr(item, "hotelsystem_Room24", None)
                    
                    setattr(item, "hotelsystem_Room24", self)
                    

    @property
    def se_hotelsystem_RoomHandler(self):
        return self.__se_hotelsystem_RoomHandler

    @se_hotelsystem_RoomHandler.setter
    def se_hotelsystem_RoomHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_se_hotelsystem_RoomHandler__se_hotelsystem_RoomHandler", None)
        self.__se_hotelsystem_RoomHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotelsystem_RoomType21"):
                    opp_val = getattr(item, "hotelsystem_RoomType21", None)
                    
                    if opp_val == self:
                        setattr(item, "hotelsystem_RoomType21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotelsystem_RoomType21"):
                    opp_val = getattr(item, "hotelsystem_RoomType21", None)
                    
                    setattr(item, "hotelsystem_RoomType21", self)
                    

    def getRoom(self, se_roomNumber) :
        # TODO: Implement getRoom method
        pass

    def initialize(self, se_numberOfRooms):
        # TODO: Implement initialize method
        pass

class hotelsystem_PaymentHandler:

    pass
class hotelsystem_Booking:

    pass
class se_bankcomponents_ICustomerProvides(ABC):

    def __init__(self):
        
        pass
    def makePayment(self, se_ccNumber, se_firstName, se_expiryMonth, se_ccv, se_lastName, se_sum, se_expiryYear) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, se_firstName, se_expiryMonth, se_ccv, se_ccNumber, se_expiryYear, se_lastName) :
        # TODO: Implement isCreditCardValid method
        pass

class hotelsystem_IHotelStartupProvides:

    pass
class User:

    pass
class se_actor_Administrator(User):

    pass
class se_actor_Receptionist(User):

    pass
class se_actor_User:

    pass
class se_bankcomponents_IAdministratorProvides(ABC):

    def __init__(self):
        
        pass
    def addCreditCard(self, se_ccv, se_lastName, se_expiryYear, se_expiryMonth, se_firstName, se_ccNumber) :
        # TODO: Implement addCreditCard method
        pass

    def getBalance(self, se_firstName, se_lastName, se_expiryYear, se_expiryMonth, se_ccNumber, se_ccv) :
        # TODO: Implement getBalance method
        pass

    def removeCreditCard(self, se_ccNumber, se_lastName, se_expiryMonth, se_expiryYear, se_ccv, se_firstName) :
        # TODO: Implement removeCreditCard method
        pass

    def makeDeposit(self, se_expiryYear, se_expiryMonth, se_lastName, se_sum, se_ccv, se_firstName, se_ccNumber) :
        # TODO: Implement makeDeposit method
        pass

class IAdministratorProvides:

    pass
class se_bankcomponents_BankAdministrator(IAdministratorProvides):

    pass
class hotelsystem_RoomHandler:

    pass
class IHotelStartupProvides:

    pass
class se_hotelsystem_HotelInitializer(IHotelStartupProvides):

    pass