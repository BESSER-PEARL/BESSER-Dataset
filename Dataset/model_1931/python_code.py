from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
class se_bankcomponents_ICustomerProvides(ABC):

    def __init__(self):
        
    def isCreditCardValid(self, lastName: str, expiryMonth: int, ccNumber: str, expiryYear: int, firstName: str, ccv: str) -> bool:
        # TODO: Implement isCreditCardValid method
        pass

    def makePayment(self, firstName: str, ccNumber: str, ccv: str, sum: float, expiryYear: int, expiryMonth: int, lastName: str) -> bool:
        # TODO: Implement makePayment method
        pass

class se_hotelsystem_IHotelStartupProvides(ABC):

    def __init__(self):
        
    def startup(self, numRooms: int):
        # TODO: Implement startup method
        pass

class se_bankcomponents_IAdministratorProvides(ABC):

    def __init__(self):
        
    def getBalance(self, ccv: str, expiryYear: int, ccNumber: str, expiryMonth: int, firstName: str, lastName: str) -> float:
        # TODO: Implement getBalance method
        pass

    def makeDeposit(self, expiryMonth: int, ccv: str, lastName: str, firstName: str, expiryYear: int, sum: float, ccNumber: str) -> float:
        # TODO: Implement makeDeposit method
        pass

    def removeCreditCard(self, ccNumber: str, ccv: str, firstName: str, expiryYear: int, lastName: str, expiryMonth: int) -> bool:
        # TODO: Implement removeCreditCard method
        pass

    def addCreditCard(self, expiryYear: int, ccv: str, lastName: str, ccNumber: str, firstName: str, expiryMonth: int) -> bool:
        # TODO: Implement addCreditCard method
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
class se_hotelsystem_IHotelAdministratorProvides(ABC):

    def __init__(self):
        
    def changeRoomType(self, roomTypeName: str, roomNumber: int) -> bool:
        # TODO: Implement changeRoomType method
        pass

    def addRoom(self, roomNumber: int, roomTypeName: str) -> bool:
        # TODO: Implement addRoom method
        pass

    def blockRoom(self, roomNumber: int) -> bool:
        # TODO: Implement blockRoom method
        pass

    def addRoomType(self, price: float, roomTypeName: str, nbrOfBeds: int, featureDescription: str) -> bool:
        # TODO: Implement addRoomType method
        pass

    def removeRoom(self, roomNumber: int) -> bool:
        # TODO: Implement removeRoom method
        pass

    def editRoomType(self, nbrOfBeds: int, featuresDescription: str, roomTypeName: str, price: float) -> bool:
        # TODO: Implement editRoomType method
        pass

    def unblockRoom(self, roomNumber: int) -> bool:
        # TODO: Implement unblockRoom method
        pass

    def removeRoomType(self, roomTypeName: str) -> bool:
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
        
    @property
    def roomTypeDescription(self) -> str:
        return self.__roomTypeDescription

    @roomTypeDescription.setter
    def roomTypeDescription(self, roomTypeDescription: str):
        self.__roomTypeDescription = roomTypeDescription

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
    def numBeds(self) -> int:
        return self.__numBeds

    @numBeds.setter
    def numBeds(self, numBeds: int):
        self.__numBeds = numBeds

class se_hotelsystem_IHotelCustomerProvides(ABC):

    def __init__(self):
        
    def payDuringCheckout(self, firstName: str, expiryMonth: int, lastName: str, ccNumber: str, expiryYear: int, ccv: str) -> bool:
        # TODO: Implement payDuringCheckout method
        pass

    def initiateRoomCheckout(self, bookingId: int, roomNumber: int) -> float:
        # TODO: Implement initiateRoomCheckout method
        pass

    def initiateBooking(self, startDate: str, firstName: str, endDate: str, lastName: str) -> int:
        # TODO: Implement initiateBooking method
        pass

    def getFreeRooms(self, startDate: str, numBeds: int, endDate: str) -> str:
        # TODO: Implement getFreeRooms method
        pass

    def checkInRoom(self, roomTypeName: str, bookindId: int) -> int:
        # TODO: Implement checkInRoom method
        pass

    def initiateCheckout(self, bookingID: int) -> float:
        # TODO: Implement initiateCheckout method
        pass

    def payRoomDuringCheckout(self, ccv: str, expiryMonth: int, lastName: str, firstName: str, ccNumber: str, roomNumber: int, expiryYear: int) -> bool:
        # TODO: Implement payRoomDuringCheckout method
        pass

    def addRoomToBooking(self, roomTypeName: str, bookingID: int) -> bool:
        # TODO: Implement addRoomToBooking method
        pass

    def confirmBooking(self, bookingID: int) -> bool:
        # TODO: Implement confirmBooking method
        pass

class se_hotelsystem_IHotelReceptionistProvides(ABC):

    def __init__(self):
        
    def editBookingTime(self, reservationId: int, startDate: str, endDate: str) -> bool:
        # TODO: Implement editBookingTime method
        pass

    def listCheckouts(self, endDate: str, startDate: str) -> str:
        # TODO: Implement listCheckouts method
        pass

    def listOccupiedRooms(self, date: str) -> str:
        # TODO: Implement listOccupiedRooms method
        pass

    def getFreeRoom(self, startDate: str, endDate: str, roomType: str) -> str:
        # TODO: Implement getFreeRoom method
        pass

    def addExtraToRoom(self, extraDescription: str, bookingId: int, roomNumber: int, price: int) -> bool:
        # TODO: Implement addExtraToRoom method
        pass

    def removeRoomTypeFromBooking(self, bookingId: int, roomType: str, nbrToRemove: int) -> bool:
        # TODO: Implement removeRoomTypeFromBooking method
        pass

    def addRoomTypeToBooking(self, bookingId: int, numberOfRoomsForType: int, roomTypeName: str) -> bool:
        # TODO: Implement addRoomTypeToBooking method
        pass

    def listCheckins(self, startDate: str, endDate: str) -> str:
        # TODO: Implement listCheckins method
        pass

    def checkIn(self, roomNumbers: int, bookingId: int) -> str:
        # TODO: Implement checkIn method
        pass

    def cancelBooking(self, bookingId: int) -> bool:
        # TODO: Implement cancelBooking method
        pass

    def listFreeRooms(self, bookingId: int) -> int:
        # TODO: Implement listFreeRooms method
        pass

    def listBookings(self) -> str:
        # TODO: Implement listBookings method
        pass

class bankcomponents_ICustomerProvides:

    pass
class se_hotelsystem_PaymentHandler:

    def __init__(self, se_hotelsystem_PaymentHandler: "bankcomponents_ICustomerProvides" = None):
        self.se_hotelsystem_PaymentHandler = se_hotelsystem_PaymentHandler
        
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

    def payIfCardValid(self, firstName: str, expiryMonth: int, expiryYear: int, lastName: str, ccNumber: str, ccv: str, sum: float) -> bool:
        # TODO: Implement payIfCardValid method
        pass

class se_hotelsystem_IRoomHandler(ABC):

    def __init__(self):
        
    def getFreeRoomByType(self, roomType: str) -> str:
        # TODO: Implement getFreeRoomByType method
        pass

    def getAllRooms(self) -> str:
        # TODO: Implement getAllRooms method
        pass

    def getFreeRooms(self) -> int:
        # TODO: Implement getFreeRooms method
        pass

    def getAllRoomTypes(self, nrOfBeds: int) -> str:
        # TODO: Implement getAllRoomTypes method
        pass

    def getAllRoomsByType(self, roomType: str) -> str:
        # TODO: Implement getAllRoomsByType method
        pass

    def getRoomType(self, roomTypeName: str) -> str:
        # TODO: Implement getRoomType method
        pass

class se_hotelsystem_Room:

    def __init__(self, occupied: bool, blocked: bool, roomNumber: int, se_hotelsystem_Room: "hotelsystem_RoomType" = None):
        self.occupied = occupied
        self.blocked = blocked
        self.roomNumber = roomNumber
        self.se_hotelsystem_Room = se_hotelsystem_Room
        
    @property
    def occupied(self) -> bool:
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied

    @property
    def roomNumber(self) -> int:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber

    @property
    def blocked(self) -> bool:
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked

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
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

class se_hotelsystem_Bill:

    def __init__(self, price: float, billID: int, se_hotelsystem_Bill: "hotelsystem_RoomReservation" = None):
        self.price = price
        self.billID = billID
        self.se_hotelsystem_Bill = se_hotelsystem_Bill
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def billID(self) -> int:
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

class se_hotelsystem_RoomType:

    def __init__(self, description: str, numBeds: int, pricePerNight: float, name: str):
        self.description = description
        self.numBeds = numBeds
        self.pricePerNight = pricePerNight
        self.name = name
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def pricePerNight(self) -> float:
        return self.__pricePerNight

    @pricePerNight.setter
    def pricePerNight(self, pricePerNight: float):
        self.__pricePerNight = pricePerNight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numBeds(self) -> int:
        return self.__numBeds

    @numBeds.setter
    def numBeds(self, numBeds: int):
        self.__numBeds = numBeds

class hotelsystem_Room:

    pass
class hotelsystem_RoomExtra:

    pass
class hotelsystem_RoomType:

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
        
    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def checkInDate(self) -> str:
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate

    @property
    def checkOuDate(self) -> str:
        return self.__checkOuDate

    @checkOuDate.setter
    def checkOuDate(self, checkOuDate: str):
        self.__checkOuDate = checkOuDate

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

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

    def addExtra(self, extra: str):
        # TODO: Implement addExtra method
        pass

    def checkIn(self):
        # TODO: Implement checkIn method
        pass

    def getRoomId(self) -> int:
        # TODO: Implement getRoomId method
        pass

    def checkOut(self, nrOfNights: int) -> float:
        # TODO: Implement checkOut method
        pass

    def getRoomIfOccupied(self, date: str) -> str:
        # TODO: Implement getRoomIfOccupied method
        pass

class se_hotelsystem_Customer:

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
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

class hotelsystem_RoomReservation:

    pass
class hotelsystem_Customer:

    pass
class hotelsystem_Bill:

    pass
class se_hotelsystem_Booking:

    def __init__(self, canceled: bool, bookingId: int, startDate: str, endDate: str, confirmed: bool, se_hotelsystem_Booking: "hotelsystem_Customer" = None, se_hotelsystem_Booking7: set["hotelsystem_RoomReservation"] = None, se_hotelsystem_Booking9: set["hotelsystem_Bill"] = None):
        self.canceled = canceled
        self.bookingId = bookingId
        self.startDate = startDate
        self.endDate = endDate
        self.confirmed = confirmed
        self.se_hotelsystem_Booking = se_hotelsystem_Booking
        self.se_hotelsystem_Booking7 = se_hotelsystem_Booking7 if se_hotelsystem_Booking7 is not None else set()
        self.se_hotelsystem_Booking9 = se_hotelsystem_Booking9 if se_hotelsystem_Booking9 is not None else set()
        
    @property
    def canceled(self) -> bool:
        return self.__canceled

    @canceled.setter
    def canceled(self, canceled: bool):
        self.__canceled = canceled

    @property
    def bookingId(self) -> int:
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: int):
        self.__bookingId = bookingId

    @property
    def confirmed(self) -> bool:
        return self.__confirmed

    @confirmed.setter
    def confirmed(self, confirmed: bool):
        self.__confirmed = confirmed

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

    def isFree(self, endDate: str, startDate: str, roomId: int) -> bool:
        # TODO: Implement isFree method
        pass

    def getRoomPrice(self, roomNumber: int) -> float:
        # TODO: Implement getRoomPrice method
        pass

    def checkOutRoom(self, roomNumber: int) -> float:
        # TODO: Implement checkOutRoom method
        pass

    def isCheckedIn(self) -> bool:
        # TODO: Implement isCheckedIn method
        pass

    def checkOut(self) -> float:
        # TODO: Implement checkOut method
        pass

    def nrOfNights(self) -> int:
        # TODO: Implement nrOfNights method
        pass

    def getOccupiedRooms(self, date: str) -> str:
        # TODO: Implement getOccupiedRooms method
        pass

    def cancel(self):
        # TODO: Implement cancel method
        pass

    def checkIn(self, room: str) -> bool:
        # TODO: Implement checkIn method
        pass

    def addExtra(self, extra: str, roomNbr: int) -> bool:
        # TODO: Implement addExtra method
        pass

    def getBookingPrice(self) -> float:
        # TODO: Implement getBookingPrice method
        pass

class hotelsystem_IRoomHandler:

    pass
class se_hotelsystem_RoomHandler(hotelsystem_IRoomHandler, hotelsystem_IHotelAdministratorProvides):

    def __init__(self, se_hotelsystem_RoomHandler: set["hotelsystem_RoomType"] = None, se_hotelsystem_RoomHandler23: set["hotelsystem_Room"] = None, hotelsystem_IRoomHandler: "se_hotelsystem_BookingHandler", hotelsystem_IHotelAdministratorProvides: "se_actor_Administrator"):
        self.se_hotelsystem_RoomHandler = se_hotelsystem_RoomHandler if se_hotelsystem_RoomHandler is not None else set()
        self.se_hotelsystem_RoomHandler23 = se_hotelsystem_RoomHandler23 if se_hotelsystem_RoomHandler23 is not None else set()
        
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
                    

    def initialize(self, numberOfRooms: int):
        # TODO: Implement initialize method
        pass

    def getRoom(self, roomNumber: int) -> str:
        # TODO: Implement getRoom method
        pass

class hotelsystem_PaymentHandler:

    pass
class hotelsystem_Booking:

    pass
class hotelsystem_IHotelCustomerProvides:

    pass
class hotelsystem_IHotelReceptionistProvides:

    pass
class se_hotelsystem_BookingHandler(hotelsystem_IHotelCustomerProvides, hotelsystem_IHotelReceptionistProvides):

    def __init__(self, bookingCurrentlyCheckingOut: int, nextBookingId: int, se_hotelsystem_BookingHandler: set["hotelsystem_Booking"] = None, se_hotelsystem_BookingHandler2: "hotelsystem_PaymentHandler" = None, se_hotelsystem_BookingHandler4: "hotelsystem_IRoomHandler" = None, hotelsystem_IHotelReceptionistProvides: "se_actor_Receptionist", hotelsystem_IHotelCustomerProvides: "se_actor_Receptionist"):
        self.bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut
        self.nextBookingId = nextBookingId
        self.se_hotelsystem_BookingHandler = se_hotelsystem_BookingHandler if se_hotelsystem_BookingHandler is not None else set()
        self.se_hotelsystem_BookingHandler2 = se_hotelsystem_BookingHandler2
        self.se_hotelsystem_BookingHandler4 = se_hotelsystem_BookingHandler4
        
    @property
    def nextBookingId(self) -> int:
        return self.__nextBookingId

    @nextBookingId.setter
    def nextBookingId(self, nextBookingId: int):
        self.__nextBookingId = nextBookingId

    @property
    def bookingCurrentlyCheckingOut(self) -> int:
        return self.__bookingCurrentlyCheckingOut

    @bookingCurrentlyCheckingOut.setter
    def bookingCurrentlyCheckingOut(self, bookingCurrentlyCheckingOut: int):
        self.__bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut

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
                    

    def isFree(self, startDate: str, roomId: int, endDate: str) -> bool:
        # TODO: Implement isFree method
        pass

    def getBookingById(self, bookingId: int) -> str:
        # TODO: Implement getBookingById method
        pass
