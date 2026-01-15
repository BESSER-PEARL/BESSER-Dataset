from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookingStatus(Enum):
    NONE = "NONE"
    BOOKED = "BOOKED"
    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"


############################################
# Definition of Classes
############################################

class HotelSystem:

    pass
class RootElement_Hotel(HotelSystem):

    pass
class RootElement_HotelSystem(ABC):

    def __init__(self):
        
    def getNationality(self) -> str:
        # TODO: Implement getNationality method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def getSystemAdministrator(self) -> SysAdmin:
        # TODO: Implement getSystemAdministrator method
        pass

    def getClerk(self, staffID: str) -> Clerk:
        # TODO: Implement getClerk method
        pass

    def getManager(self, staffID: str) -> str:
        # TODO: Implement getManager method
        pass

    def getGuest(self) -> str:
        # TODO: Implement getGuest method
        pass

    def getStaff(self, staffID: str) -> Staff:
        # TODO: Implement getStaff method
        pass

class RoomFetcher:

    pass
class RoomBooking:

    pass
class RootElement_HourlyRoomBooking(RoomBooking):

    pass
class RootElement_DailyRoomBooking(RoomBooking):

    def __init__(self, nbrOfGuests: str):
        self.nbrOfGuests = nbrOfGuests
        
    @property
    def nbrOfGuests(self) -> str:
        return self.__nbrOfGuests

    @nbrOfGuests.setter
    def nbrOfGuests(self, nbrOfGuests: str):
        self.__nbrOfGuests = nbrOfGuests

class RootElement_RoomFetcher(ABC):

    def __init__(self, RootElement_RoomFetcher: "RootElement_BookingHandler" = None, RootElement_RoomFetcher47: "RootElement_CleaningHandler" = None):
        self.RootElement_RoomFetcher = RootElement_RoomFetcher
        self.RootElement_RoomFetcher47 = RootElement_RoomFetcher47
        
    @property
    def RootElement_RoomFetcher47(self):
        return self.__RootElement_RoomFetcher47

    @RootElement_RoomFetcher47.setter
    def RootElement_RoomFetcher47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomFetcher__RootElement_RoomFetcher47", None)
        self.__RootElement_RoomFetcher47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_CleaningHandler"):
                opp_val = getattr(old_value, "RootElement_CleaningHandler", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_CleaningHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_CleaningHandler"):
                opp_val = getattr(value, "RootElement_CleaningHandler", None)
                setattr(value, "RootElement_CleaningHandler", self)

    @property
    def RootElement_RoomFetcher(self):
        return self.__RootElement_RoomFetcher

    @RootElement_RoomFetcher.setter
    def RootElement_RoomFetcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomFetcher__RootElement_RoomFetcher", None)
        self.__RootElement_RoomFetcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_BookingHandler35"):
                opp_val = getattr(old_value, "RootElement_BookingHandler35", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_BookingHandler35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_BookingHandler35"):
                opp_val = getattr(value, "RootElement_BookingHandler35", None)
                setattr(value, "RootElement_BookingHandler35", self)

    def getAllCleanableRooms(self) -> str:
        # TODO: Implement getAllCleanableRooms method
        pass

    def getAvailableRooms(self) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def getBookableRooms(self) -> str:
        # TODO: Implement getBookableRooms method
        pass

class RootElement_RoomTypeHandling(ABC):

    def __init__(self):
        
    def removeAttributeFromRoomType(self, roomType: str, roomAttribute: str) -> str:
        # TODO: Implement removeAttributeFromRoomType method
        pass

    def addAttributeToRoomType(self, roomAttribute: str, roomType: str) -> str:
        # TODO: Implement addAttributeToRoomType method
        pass

    def addRoomType(self, name: str, capacity: str, cost: str) -> str:
        # TODO: Implement addRoomType method
        pass

    def findRoomType(self, name: str) -> str:
        # TODO: Implement findRoomType method
        pass

    def removeRoomType(self, roomType: str) -> str:
        # TODO: Implement removeRoomType method
        pass

    def editRoomType(self, newName: str, roomType: str, newCapacity: str, newCost: str) -> str:
        # TODO: Implement editRoomType method
        pass

    def getAllRoomTypes(self) -> str:
        # TODO: Implement getAllRoomTypes method
        pass

class RootElement_RoomHandling(ABC):

    def __init__(self):
        
    def removeRoom(self, room: str) -> str:
        # TODO: Implement removeRoom method
        pass

    def findRoom(self, roomName: str) -> str:
        # TODO: Implement findRoom method
        pass

    def addRoom(self, roomType: str, roomName: str) -> str:
        # TODO: Implement addRoom method
        pass

    def getAllRooms(self) -> str:
        # TODO: Implement getAllRooms method
        pass

    def editRoom(self, newRoomName: str, room: str, newRoomType: str) -> str:
        # TODO: Implement editRoom method
        pass

class RootElement_RoomAttributeHandling(ABC):

    def __init__(self):
        
    def findRoomAttribute(self, name: str) -> str:
        # TODO: Implement findRoomAttribute method
        pass

    def getAllRoomAttributes(self) -> str:
        # TODO: Implement getAllRoomAttributes method
        pass

    def addRoomAttribute(self, description: str, name: str) -> str:
        # TODO: Implement addRoomAttribute method
        pass

    def removeRoomAttribute(self, roomAttribute: str) -> str:
        # TODO: Implement removeRoomAttribute method
        pass

    def editRoomAttribute(self, roomAttribute: str, newName: str, newDescription: str) -> str:
        # TODO: Implement editRoomAttribute method
        pass

class RoomTypeHandling:

    pass
class RoomHandling:

    pass
class RoomAttributeHandling:

    pass
class RootElement_RoomStructure(RoomFetcher, RoomTypeHandling, RoomAttributeHandling, RoomHandling):

    pass
class RootElement_SysAdmin(RoomTypeHandling, RoomAttributeHandling, RoomHandling):

    pass
class RootElement_FeedbackReader(ABC):

    def __init__(self, RootElement_FeedbackReader: "RootElement_Manager" = None):
        self.RootElement_FeedbackReader = RootElement_FeedbackReader
        
    @property
    def RootElement_FeedbackReader(self):
        return self.__RootElement_FeedbackReader

    @RootElement_FeedbackReader.setter
    def RootElement_FeedbackReader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_FeedbackReader__RootElement_FeedbackReader", None)
        self.__RootElement_FeedbackReader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Manager"):
                opp_val = getattr(old_value, "RootElement_Manager", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Manager"):
                opp_val = getattr(value, "RootElement_Manager", None)
                setattr(value, "RootElement_Manager", self)

    def getAllFeedback(self) -> str:
        # TODO: Implement getAllFeedback method
        pass

    def getUnreadFeedback(self) -> str:
        # TODO: Implement getUnreadFeedback method
        pass

class FeedbackReader:

    pass
class SysAdmin:

    pass
class Clerk:

    pass
class RootElement_Manager(SysAdmin, Clerk, FeedbackReader):

    pass
class RootElement_Payment(ABC):

    def __init__(self, RootElement_Payment: "RootElement_Clerk" = None):
        self.RootElement_Payment = RootElement_Payment
        
    @property
    def RootElement_Payment(self):
        return self.__RootElement_Payment

    @RootElement_Payment.setter
    def RootElement_Payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Payment__RootElement_Payment", None)
        self.__RootElement_Payment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Clerk30"):
                opp_val = getattr(old_value, "RootElement_Clerk30", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Clerk30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Clerk30"):
                opp_val = getattr(value, "RootElement_Clerk30", None)
                setattr(value, "RootElement_Clerk30", self)

    def debitCard(self, creditCard: str, amount: str) -> str:
        # TODO: Implement debitCard method
        pass

    def verifyCreditCard(self, creditCard: str) -> str:
        # TODO: Implement verifyCreditCard method
        pass

class RootElement_ServiceItemHandling(ABC):

    def __init__(self, RootElement_ServiceItemHandling: "RootElement_Clerk" = None):
        self.RootElement_ServiceItemHandling = RootElement_ServiceItemHandling
        
    @property
    def RootElement_ServiceItemHandling(self):
        return self.__RootElement_ServiceItemHandling

    @RootElement_ServiceItemHandling.setter
    def RootElement_ServiceItemHandling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_ServiceItemHandling__RootElement_ServiceItemHandling", None)
        self.__RootElement_ServiceItemHandling = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Clerk25"):
                opp_val = getattr(old_value, "RootElement_Clerk25", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Clerk25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Clerk25"):
                opp_val = getattr(value, "RootElement_Clerk25", None)
                setattr(value, "RootElement_Clerk25", self)

    def findAllServiceItems(self, booking: str) -> str:
        # TODO: Implement findAllServiceItems method
        pass

    def addServiceItem(self, description: str, booking: str, price: str, name: str):
        # TODO: Implement addServiceItem method
        pass

    def removeServiceItem(self, booking: str, serviceItem: str):
        # TODO: Implement removeServiceItem method
        pass

class RootElement_ReceptionHandling(ABC):

    def __init__(self, RootElement_ReceptionHandling: "RootElement_Clerk" = None):
        self.RootElement_ReceptionHandling = RootElement_ReceptionHandling
        
    @property
    def RootElement_ReceptionHandling(self):
        return self.__RootElement_ReceptionHandling

    @RootElement_ReceptionHandling.setter
    def RootElement_ReceptionHandling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_ReceptionHandling__RootElement_ReceptionHandling", None)
        self.__RootElement_ReceptionHandling = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Clerk"):
                opp_val = getattr(old_value, "RootElement_Clerk", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Clerk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Clerk"):
                opp_val = getattr(value, "RootElement_Clerk", None)
                setattr(value, "RootElement_Clerk", self)

    def findActiveBooking(self, roomName: str) -> str:
        # TODO: Implement findActiveBooking method
        pass

    def checkOut(self, booking: str) -> str:
        # TODO: Implement checkOut method
        pass

    def checkIn(self, booking: str) -> str:
        # TODO: Implement checkIn method
        pass

    def findBookings(self, name: str) -> str:
        # TODO: Implement findBookings method
        pass

class Payment:

    pass
class RootElement_PaymentHandler(Payment):

    pass
class ServiceItemHandling:

    pass
class ReceptionHandling:

    pass
class Staff:

    pass
class RootElement_SupportTicket:

    def __init__(self, problemDescription: str, roomName: str, fixed: str, RootElement_SupportTicket: "RootElement_SupportTicketHandler" = None):
        self.problemDescription = problemDescription
        self.roomName = roomName
        self.fixed = fixed
        self.RootElement_SupportTicket = RootElement_SupportTicket
        
    @property
    def fixed(self) -> str:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: str):
        self.__fixed = fixed

    @property
    def roomName(self) -> str:
        return self.__roomName

    @roomName.setter
    def roomName(self, roomName: str):
        self.__roomName = roomName

    @property
    def problemDescription(self) -> str:
        return self.__problemDescription

    @problemDescription.setter
    def problemDescription(self, problemDescription: str):
        self.__problemDescription = problemDescription

    @property
    def RootElement_SupportTicket(self):
        return self.__RootElement_SupportTicket

    @RootElement_SupportTicket.setter
    def RootElement_SupportTicket(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_SupportTicket__RootElement_SupportTicket", None)
        self.__RootElement_SupportTicket = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_SupportTicketHandler"):
                opp_val = getattr(old_value, "RootElement_SupportTicketHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_SupportTicketHandler"):
                opp_val = getattr(value, "RootElement_SupportTicketHandler", None)
                if opp_val is None:
                    setattr(value, "RootElement_SupportTicketHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RootElement_SupportTicketReader(ABC):

    def __init__(self, RootElement_SupportTicketReader: "RootElement_Staff" = None):
        self.RootElement_SupportTicketReader = RootElement_SupportTicketReader
        
    @property
    def RootElement_SupportTicketReader(self):
        return self.__RootElement_SupportTicketReader

    @RootElement_SupportTicketReader.setter
    def RootElement_SupportTicketReader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_SupportTicketReader__RootElement_SupportTicketReader", None)
        self.__RootElement_SupportTicketReader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Staff19"):
                opp_val = getattr(old_value, "RootElement_Staff19", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Staff19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Staff19"):
                opp_val = getattr(value, "RootElement_Staff19", None)
                setattr(value, "RootElement_Staff19", self)

    def getUnfixedTickets(self) -> str:
        # TODO: Implement getUnfixedTickets method
        pass

    def getSupportTicketsForRoom(self, roomName: str) -> str:
        # TODO: Implement getSupportTicketsForRoom method
        pass

    def markAsCompleted(self, supportTicket: str):
        # TODO: Implement markAsCompleted method
        pass

class RootElement_Cleaning(ABC):

    def __init__(self, RootElement_Cleaning: "RootElement_Staff" = None):
        self.RootElement_Cleaning = RootElement_Cleaning
        
    @property
    def RootElement_Cleaning(self):
        return self.__RootElement_Cleaning

    @RootElement_Cleaning.setter
    def RootElement_Cleaning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Cleaning__RootElement_Cleaning", None)
        self.__RootElement_Cleaning = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Staff"):
                opp_val = getattr(old_value, "RootElement_Staff", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Staff", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Staff"):
                opp_val = getattr(value, "RootElement_Staff", None)
                setattr(value, "RootElement_Staff", self)

    def markRoomAsCleaned(self, room: str):
        # TODO: Implement markRoomAsCleaned method
        pass

    def getListOfUncleanRooms(self) -> str:
        # TODO: Implement getListOfUncleanRooms method
        pass

    def checkIfRoomCleaned(self, roomName: str) -> str:
        # TODO: Implement checkIfRoomCleaned method
        pass

class Cleaning:

    pass
class RootElement_CleaningHandler(Cleaning):

    pass
class RootElement_Feedback:

    def __init__(self, feedbackDescription: str, rating: str, read: str, RootElement_Feedback: "RootElement_FeedbackHandler" = None):
        self.feedbackDescription = feedbackDescription
        self.rating = rating
        self.read = read
        self.RootElement_Feedback = RootElement_Feedback
        
    @property
    def feedbackDescription(self) -> str:
        return self.__feedbackDescription

    @feedbackDescription.setter
    def feedbackDescription(self, feedbackDescription: str):
        self.__feedbackDescription = feedbackDescription

    @property
    def read(self) -> str:
        return self.__read

    @read.setter
    def read(self, read: str):
        self.__read = read

    @property
    def rating(self) -> str:
        return self.__rating

    @rating.setter
    def rating(self, rating: str):
        self.__rating = rating

    @property
    def RootElement_Feedback(self):
        return self.__RootElement_Feedback

    @RootElement_Feedback.setter
    def RootElement_Feedback(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Feedback__RootElement_Feedback", None)
        self.__RootElement_Feedback = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_FeedbackHandler"):
                opp_val = getattr(old_value, "RootElement_FeedbackHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_FeedbackHandler"):
                opp_val = getattr(value, "RootElement_FeedbackHandler", None)
                if opp_val is None:
                    setattr(value, "RootElement_FeedbackHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SupportTicketReader:

    pass
class RootElement_RoomAttribute:

    def __init__(self, id: str, name: str, description: str, RootElement_RoomAttribute: "RootElement_RoomType" = None, RootElement_RoomAttribute43: "RootElement_RoomStructure" = None):
        self.id = id
        self.name = name
        self.description = description
        self.RootElement_RoomAttribute = RootElement_RoomAttribute
        self.RootElement_RoomAttribute43 = RootElement_RoomAttribute43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def RootElement_RoomAttribute(self):
        return self.__RootElement_RoomAttribute

    @RootElement_RoomAttribute.setter
    def RootElement_RoomAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomAttribute__RootElement_RoomAttribute", None)
        self.__RootElement_RoomAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomType16"):
                opp_val = getattr(old_value, "RootElement_RoomType16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomType16"):
                opp_val = getattr(value, "RootElement_RoomType16", None)
                if opp_val is None:
                    setattr(value, "RootElement_RoomType16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RootElement_RoomAttribute43(self):
        return self.__RootElement_RoomAttribute43

    @RootElement_RoomAttribute43.setter
    def RootElement_RoomAttribute43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomAttribute__RootElement_RoomAttribute43", None)
        self.__RootElement_RoomAttribute43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomStructure42"):
                opp_val = getattr(old_value, "RootElement_RoomStructure42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomStructure42"):
                opp_val = getattr(value, "RootElement_RoomStructure42", None)
                if opp_val is None:
                    setattr(value, "RootElement_RoomStructure42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RootElement_RoomType:

    def __init__(self, name: str, price: str, capacity: str, RootElement_RoomType: "RootElement_Room" = None, RootElement_RoomType16: set["RootElement_RoomAttribute"] = None, RootElement_RoomType40: "RootElement_RoomStructure" = None):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.RootElement_RoomType = RootElement_RoomType
        self.RootElement_RoomType16 = RootElement_RoomType16 if RootElement_RoomType16 is not None else set()
        self.RootElement_RoomType40 = RootElement_RoomType40
        
    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RootElement_RoomType(self):
        return self.__RootElement_RoomType

    @RootElement_RoomType.setter
    def RootElement_RoomType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomType__RootElement_RoomType", None)
        self.__RootElement_RoomType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Room14"):
                opp_val = getattr(old_value, "RootElement_Room14", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Room14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Room14"):
                opp_val = getattr(value, "RootElement_Room14", None)
                setattr(value, "RootElement_Room14", self)

    @property
    def RootElement_RoomType16(self):
        return self.__RootElement_RoomType16

    @RootElement_RoomType16.setter
    def RootElement_RoomType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomType__RootElement_RoomType16", None)
        self.__RootElement_RoomType16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootElement_RoomAttribute"):
                    opp_val = getattr(item, "RootElement_RoomAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "RootElement_RoomAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootElement_RoomAttribute"):
                    opp_val = getattr(item, "RootElement_RoomAttribute", None)
                    
                    setattr(item, "RootElement_RoomAttribute", self)
                    

    @property
    def RootElement_RoomType40(self):
        return self.__RootElement_RoomType40

    @RootElement_RoomType40.setter
    def RootElement_RoomType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomType__RootElement_RoomType40", None)
        self.__RootElement_RoomType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomStructure39"):
                opp_val = getattr(old_value, "RootElement_RoomStructure39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomStructure39"):
                opp_val = getattr(value, "RootElement_RoomStructure39", None)
                if opp_val is None:
                    setattr(value, "RootElement_RoomStructure39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def removeRoomAttribute(self, roomAttribute: str) -> bool:
        # TODO: Implement removeRoomAttribute method
        pass

    def addRoomAttribute(self, roomAttribute: str) -> bool:
        # TODO: Implement addRoomAttribute method
        pass

class RootElement_Room:

    def __init__(self, isOccupied: str, name: str, needCleaning: str, RootElement_Room: "RootElement_RoomBooking" = None, RootElement_Room14: "RootElement_RoomType" = None, RootElement_Room37: "RootElement_RoomStructure" = None):
        self.isOccupied = isOccupied
        self.name = name
        self.needCleaning = needCleaning
        self.RootElement_Room = RootElement_Room
        self.RootElement_Room14 = RootElement_Room14
        self.RootElement_Room37 = RootElement_Room37
        
    @property
    def isOccupied(self) -> str:
        return self.__isOccupied

    @isOccupied.setter
    def isOccupied(self, isOccupied: str):
        self.__isOccupied = isOccupied

    @property
    def needCleaning(self) -> str:
        return self.__needCleaning

    @needCleaning.setter
    def needCleaning(self, needCleaning: str):
        self.__needCleaning = needCleaning

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RootElement_Room14(self):
        return self.__RootElement_Room14

    @RootElement_Room14.setter
    def RootElement_Room14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Room__RootElement_Room14", None)
        self.__RootElement_Room14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomType"):
                opp_val = getattr(old_value, "RootElement_RoomType", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_RoomType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomType"):
                opp_val = getattr(value, "RootElement_RoomType", None)
                setattr(value, "RootElement_RoomType", self)

    @property
    def RootElement_Room(self):
        return self.__RootElement_Room

    @RootElement_Room.setter
    def RootElement_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Room__RootElement_Room", None)
        self.__RootElement_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomBooking12"):
                opp_val = getattr(old_value, "RootElement_RoomBooking12", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_RoomBooking12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomBooking12"):
                opp_val = getattr(value, "RootElement_RoomBooking12", None)
                setattr(value, "RootElement_RoomBooking12", self)

    @property
    def RootElement_Room37(self):
        return self.__RootElement_Room37

    @RootElement_Room37.setter
    def RootElement_Room37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Room__RootElement_Room37", None)
        self.__RootElement_Room37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_RoomStructure"):
                opp_val = getattr(old_value, "RootElement_RoomStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_RoomStructure"):
                opp_val = getattr(value, "RootElement_RoomStructure", None)
                if opp_val is None:
                    setattr(value, "RootElement_RoomStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RootElement_ServiceItem:

    def __init__(self, name: str, description: str, price: str, RootElement_ServiceItem: "RootElement_Booking" = None):
        self.name = name
        self.description = description
        self.price = price
        self.RootElement_ServiceItem = RootElement_ServiceItem
        
    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RootElement_ServiceItem(self):
        return self.__RootElement_ServiceItem

    @RootElement_ServiceItem.setter
    def RootElement_ServiceItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_ServiceItem__RootElement_ServiceItem", None)
        self.__RootElement_ServiceItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Booking10"):
                opp_val = getattr(old_value, "RootElement_Booking10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Booking10"):
                opp_val = getattr(value, "RootElement_Booking10", None)
                if opp_val is None:
                    setattr(value, "RootElement_Booking10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RootElement_RoomBooking(ABC):

    def __init__(self, startDate: date, endDate: date, bookingStatus: str, RootElement_RoomBooking: "RootElement_Booking" = None, RootElement_RoomBooking12: "RootElement_Room" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.bookingStatus = bookingStatus
        self.RootElement_RoomBooking = RootElement_RoomBooking
        self.RootElement_RoomBooking12 = RootElement_RoomBooking12
        
    @property
    def bookingStatus(self) -> str:
        return self.__bookingStatus

    @bookingStatus.setter
    def bookingStatus(self, bookingStatus: str):
        self.__bookingStatus = bookingStatus

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def RootElement_RoomBooking(self):
        return self.__RootElement_RoomBooking

    @RootElement_RoomBooking.setter
    def RootElement_RoomBooking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomBooking__RootElement_RoomBooking", None)
        self.__RootElement_RoomBooking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Booking"):
                opp_val = getattr(old_value, "RootElement_Booking", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Booking"):
                opp_val = getattr(value, "RootElement_Booking", None)
                if opp_val is None:
                    setattr(value, "RootElement_Booking", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RootElement_RoomBooking12(self):
        return self.__RootElement_RoomBooking12

    @RootElement_RoomBooking12.setter
    def RootElement_RoomBooking12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_RoomBooking__RootElement_RoomBooking12", None)
        self.__RootElement_RoomBooking12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Room"):
                opp_val = getattr(old_value, "RootElement_Room", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Room"):
                opp_val = getattr(value, "RootElement_Room", None)
                setattr(value, "RootElement_Room", self)

    def calculateCost(self) -> str:
        # TODO: Implement calculateCost method
        pass

class RootElement_Booking:

    def __init__(self, bookingID: str, RootElement_Booking: set["RootElement_RoomBooking"] = None, RootElement_Booking7: "RootElement_Guest" = None, RootElement_Booking10: set["RootElement_ServiceItem"] = None, RootElement_Booking33: "RootElement_BookingHandler" = None):
        self.bookingID = bookingID
        self.RootElement_Booking = RootElement_Booking if RootElement_Booking is not None else set()
        self.RootElement_Booking7 = RootElement_Booking7
        self.RootElement_Booking10 = RootElement_Booking10 if RootElement_Booking10 is not None else set()
        self.RootElement_Booking33 = RootElement_Booking33
        
    @property
    def bookingID(self) -> str:
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: str):
        self.__bookingID = bookingID

    @property
    def RootElement_Booking7(self):
        return self.__RootElement_Booking7

    @RootElement_Booking7.setter
    def RootElement_Booking7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Booking__RootElement_Booking7", None)
        self.__RootElement_Booking7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Guest8"):
                opp_val = getattr(old_value, "RootElement_Guest8", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Guest8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Guest8"):
                opp_val = getattr(value, "RootElement_Guest8", None)
                setattr(value, "RootElement_Guest8", self)

    @property
    def RootElement_Booking(self):
        return self.__RootElement_Booking

    @RootElement_Booking.setter
    def RootElement_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Booking__RootElement_Booking", None)
        self.__RootElement_Booking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootElement_RoomBooking"):
                    opp_val = getattr(item, "RootElement_RoomBooking", None)
                    
                    if opp_val == self:
                        setattr(item, "RootElement_RoomBooking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootElement_RoomBooking"):
                    opp_val = getattr(item, "RootElement_RoomBooking", None)
                    
                    setattr(item, "RootElement_RoomBooking", self)
                    

    @property
    def RootElement_Booking33(self):
        return self.__RootElement_Booking33

    @RootElement_Booking33.setter
    def RootElement_Booking33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Booking__RootElement_Booking33", None)
        self.__RootElement_Booking33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_BookingHandler"):
                opp_val = getattr(old_value, "RootElement_BookingHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_BookingHandler"):
                opp_val = getattr(value, "RootElement_BookingHandler", None)
                if opp_val is None:
                    setattr(value, "RootElement_BookingHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RootElement_Booking10(self):
        return self.__RootElement_Booking10

    @RootElement_Booking10.setter
    def RootElement_Booking10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Booking__RootElement_Booking10", None)
        self.__RootElement_Booking10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootElement_ServiceItem"):
                    opp_val = getattr(item, "RootElement_ServiceItem", None)
                    
                    if opp_val == self:
                        setattr(item, "RootElement_ServiceItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootElement_ServiceItem"):
                    opp_val = getattr(item, "RootElement_ServiceItem", None)
                    
                    setattr(item, "RootElement_ServiceItem", self)
                    

    def calculateCost(self) -> str:
        # TODO: Implement calculateCost method
        pass

class RootElement_FeedbackWriter(ABC):

    def __init__(self, RootElement_FeedbackWriter: "RootElement_Guest" = None):
        self.RootElement_FeedbackWriter = RootElement_FeedbackWriter
        
    @property
    def RootElement_FeedbackWriter(self):
        return self.__RootElement_FeedbackWriter

    @RootElement_FeedbackWriter.setter
    def RootElement_FeedbackWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_FeedbackWriter__RootElement_FeedbackWriter", None)
        self.__RootElement_FeedbackWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Guest4"):
                opp_val = getattr(old_value, "RootElement_Guest4", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Guest4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Guest4"):
                opp_val = getattr(value, "RootElement_Guest4", None)
                setattr(value, "RootElement_Guest4", self)

    def giveFeedback(self, rating: str, feedback: str):
        # TODO: Implement giveFeedback method
        pass

class RootElement_MakeBooking(ABC):

    def __init__(self, RootElement_MakeBooking: "RootElement_Guest" = None, RootElement_MakeBooking28: "RootElement_Clerk" = None):
        self.RootElement_MakeBooking = RootElement_MakeBooking
        self.RootElement_MakeBooking28 = RootElement_MakeBooking28
        
    @property
    def RootElement_MakeBooking28(self):
        return self.__RootElement_MakeBooking28

    @RootElement_MakeBooking28.setter
    def RootElement_MakeBooking28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_MakeBooking__RootElement_MakeBooking28", None)
        self.__RootElement_MakeBooking28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Clerk27"):
                opp_val = getattr(old_value, "RootElement_Clerk27", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Clerk27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Clerk27"):
                opp_val = getattr(value, "RootElement_Clerk27", None)
                setattr(value, "RootElement_Clerk27", self)

    @property
    def RootElement_MakeBooking(self):
        return self.__RootElement_MakeBooking

    @RootElement_MakeBooking.setter
    def RootElement_MakeBooking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_MakeBooking__RootElement_MakeBooking", None)
        self.__RootElement_MakeBooking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Guest2"):
                opp_val = getattr(old_value, "RootElement_Guest2", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Guest2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Guest2"):
                opp_val = getattr(value, "RootElement_Guest2", None)
                setattr(value, "RootElement_Guest2", self)

    def getAvailableRooms(self, endDate: date, nbrOfAdults: str, startDate: date, nbrOfChildren: str) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def lookupBooking(self, name: str, phoneNumber: str) -> str:
        # TODO: Implement lookupBooking method
        pass

    def confirmBooking(self, phone: str, nationality: str, mail: str, name: str, booking: str, passportNr: str, nextDestination: str) -> str:
        # TODO: Implement confirmBooking method
        pass

    def addRoom(self, booking: str, nbrOfChildren: str, endDate: date, startDate: date, room: str, nbrOfAdults: str) -> str:
        # TODO: Implement addRoom method
        pass

    def cancelBooking(self, booking: str) -> str:
        # TODO: Implement cancelBooking method
        pass

    def createBooking(self) -> str:
        # TODO: Implement createBooking method
        pass

class RootElement_SupportTicketWriter(ABC):

    def __init__(self, RootElement_SupportTicketWriter: "RootElement_Guest" = None, RootElement_SupportTicketWriter22: "RootElement_Staff" = None):
        self.RootElement_SupportTicketWriter = RootElement_SupportTicketWriter
        self.RootElement_SupportTicketWriter22 = RootElement_SupportTicketWriter22
        
    @property
    def RootElement_SupportTicketWriter22(self):
        return self.__RootElement_SupportTicketWriter22

    @RootElement_SupportTicketWriter22.setter
    def RootElement_SupportTicketWriter22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_SupportTicketWriter__RootElement_SupportTicketWriter22", None)
        self.__RootElement_SupportTicketWriter22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Staff21"):
                opp_val = getattr(old_value, "RootElement_Staff21", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Staff21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Staff21"):
                opp_val = getattr(value, "RootElement_Staff21", None)
                setattr(value, "RootElement_Staff21", self)

    @property
    def RootElement_SupportTicketWriter(self):
        return self.__RootElement_SupportTicketWriter

    @RootElement_SupportTicketWriter.setter
    def RootElement_SupportTicketWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_SupportTicketWriter__RootElement_SupportTicketWriter", None)
        self.__RootElement_SupportTicketWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Guest"):
                opp_val = getattr(old_value, "RootElement_Guest", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Guest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Guest"):
                opp_val = getattr(value, "RootElement_Guest", None)
                setattr(value, "RootElement_Guest", self)

    def newSupportTicket(self, roomName: str, description: str):
        # TODO: Implement newSupportTicket method
        pass

class MakeBooking:

    pass
class RootElement_BookingHandler(ReceptionHandling, MakeBooking, ServiceItemHandling):

    pass
class RootElement_Clerk(ServiceItemHandling, ReceptionHandling, MakeBooking, Staff, Payment):

    pass
class FeedbackWriter:

    pass
class RootElement_FeedbackHandler(FeedbackWriter, FeedbackReader):

    pass
class SupportTicketWriter:

    pass
class RootElement_Staff(Cleaning, SupportTicketWriter, SupportTicketReader):

    def __init__(self, staffID: str, name: str, RootElement_Staff: "RootElement_Cleaning" = None, RootElement_Staff19: "RootElement_SupportTicketReader" = None, RootElement_Staff21: "RootElement_SupportTicketWriter" = None):
        self.staffID = staffID
        self.name = name
        self.RootElement_Staff = RootElement_Staff
        self.RootElement_Staff19 = RootElement_Staff19
        self.RootElement_Staff21 = RootElement_Staff21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def staffID(self) -> str:
        return self.__staffID

    @staffID.setter
    def staffID(self, staffID: str):
        self.__staffID = staffID

    @property
    def RootElement_Staff19(self):
        return self.__RootElement_Staff19

    @RootElement_Staff19.setter
    def RootElement_Staff19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Staff__RootElement_Staff19", None)
        self.__RootElement_Staff19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_SupportTicketReader"):
                opp_val = getattr(old_value, "RootElement_SupportTicketReader", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_SupportTicketReader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_SupportTicketReader"):
                opp_val = getattr(value, "RootElement_SupportTicketReader", None)
                setattr(value, "RootElement_SupportTicketReader", self)

    @property
    def RootElement_Staff(self):
        return self.__RootElement_Staff

    @RootElement_Staff.setter
    def RootElement_Staff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Staff__RootElement_Staff", None)
        self.__RootElement_Staff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Cleaning"):
                opp_val = getattr(old_value, "RootElement_Cleaning", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Cleaning", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Cleaning"):
                opp_val = getattr(value, "RootElement_Cleaning", None)
                setattr(value, "RootElement_Cleaning", self)

    @property
    def RootElement_Staff21(self):
        return self.__RootElement_Staff21

    @RootElement_Staff21.setter
    def RootElement_Staff21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Staff__RootElement_Staff21", None)
        self.__RootElement_Staff21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_SupportTicketWriter22"):
                opp_val = getattr(old_value, "RootElement_SupportTicketWriter22", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_SupportTicketWriter22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_SupportTicketWriter22"):
                opp_val = getattr(value, "RootElement_SupportTicketWriter22", None)
                setattr(value, "RootElement_SupportTicketWriter22", self)

class RootElement_SupportTicketHandler(SupportTicketWriter, SupportTicketReader):

    pass
class RootElement_Guest(SupportTicketWriter, FeedbackWriter, MakeBooking):

    def __init__(self, phoneNumber: str, nextDestination: str, nationality: str, name: str, mail: str, socialSecurityNumber: str, RootElement_Guest: "RootElement_SupportTicketWriter" = None, RootElement_Guest2: "RootElement_MakeBooking" = None, RootElement_Guest4: "RootElement_FeedbackWriter" = None, RootElement_Guest8: "RootElement_Booking" = None):
        self.phoneNumber = phoneNumber
        self.nextDestination = nextDestination
        self.nationality = nationality
        self.name = name
        self.mail = mail
        self.socialSecurityNumber = socialSecurityNumber
        self.RootElement_Guest = RootElement_Guest
        self.RootElement_Guest2 = RootElement_Guest2
        self.RootElement_Guest4 = RootElement_Guest4
        self.RootElement_Guest8 = RootElement_Guest8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def mail(self) -> str:
        return self.__mail

    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def nextDestination(self) -> str:
        return self.__nextDestination

    @nextDestination.setter
    def nextDestination(self, nextDestination: str):
        self.__nextDestination = nextDestination

    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str):
        self.__nationality = nationality

    @property
    def socialSecurityNumber(self) -> str:
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: str):
        self.__socialSecurityNumber = socialSecurityNumber

    @property
    def RootElement_Guest8(self):
        return self.__RootElement_Guest8

    @RootElement_Guest8.setter
    def RootElement_Guest8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Guest__RootElement_Guest8", None)
        self.__RootElement_Guest8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_Booking7"):
                opp_val = getattr(old_value, "RootElement_Booking7", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_Booking7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_Booking7"):
                opp_val = getattr(value, "RootElement_Booking7", None)
                setattr(value, "RootElement_Booking7", self)

    @property
    def RootElement_Guest2(self):
        return self.__RootElement_Guest2

    @RootElement_Guest2.setter
    def RootElement_Guest2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Guest__RootElement_Guest2", None)
        self.__RootElement_Guest2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_MakeBooking"):
                opp_val = getattr(old_value, "RootElement_MakeBooking", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_MakeBooking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_MakeBooking"):
                opp_val = getattr(value, "RootElement_MakeBooking", None)
                setattr(value, "RootElement_MakeBooking", self)

    @property
    def RootElement_Guest(self):
        return self.__RootElement_Guest

    @RootElement_Guest.setter
    def RootElement_Guest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Guest__RootElement_Guest", None)
        self.__RootElement_Guest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_SupportTicketWriter"):
                opp_val = getattr(old_value, "RootElement_SupportTicketWriter", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_SupportTicketWriter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_SupportTicketWriter"):
                opp_val = getattr(value, "RootElement_SupportTicketWriter", None)
                setattr(value, "RootElement_SupportTicketWriter", self)

    @property
    def RootElement_Guest4(self):
        return self.__RootElement_Guest4

    @RootElement_Guest4.setter
    def RootElement_Guest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RootElement_Guest__RootElement_Guest4", None)
        self.__RootElement_Guest4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootElement_FeedbackWriter"):
                opp_val = getattr(old_value, "RootElement_FeedbackWriter", None)
                if opp_val == self:
                    setattr(old_value, "RootElement_FeedbackWriter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootElement_FeedbackWriter"):
                opp_val = getattr(value, "RootElement_FeedbackWriter", None)
                setattr(value, "RootElement_FeedbackWriter", self)
