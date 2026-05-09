from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RoomStatus(Enum):
    Occupied = "Occupied"
    Available = "Available"
    Cleaning = "Cleaning"
    Maintenance = "Maintenance"
class ChargeType(Enum):
    CancellationFee = "CancellationFee"
    Breakfast = "Breakfast"
    SingleRoom = "SingleRoom"
    DoubleRoom = "DoubleRoom"
    FamilySuite = "FamilySuite"
    LateCheckOutFee = "LateCheckOutFee"
class RoomTypeName(Enum):
    SingleRoom = "SingleRoom"
    DoubleRoom = "DoubleRoom"
    FamilySuite = "FamilySuite"


############################################
# Definition of Classes
############################################

class Classes_AdministratorProvides(ABC):

    def __init__(self):
        
        pass
    def makeDeposit(self, Classes_firstName, Classes_expiryYear, Classes_ccv, Classes_expiryMonth, Classes_ccNumber, Classes_sum, Classes_lastName) :
        # TODO: Implement makeDeposit method
        pass

    def addCreditCard(self, Classes_ccNumber, Classes_expiryYear, Classes_lastName, Classes_expiryMonth, Classes_ccv, Classes_firstName) :
        # TODO: Implement addCreditCard method
        pass

    def getBalance(self, Classes_lastName, Classes_firstName, Classes_expiryYear, Classes_expiryMonth, Classes_ccv, Classes_ccNumber) :
        # TODO: Implement getBalance method
        pass

    def removeCreditCard(self, Classes_expiryMonth, Classes_lastName, Classes_ccNumber, Classes_ccv, Classes_firstName, Classes_expiryYear) :
        # TODO: Implement removeCreditCard method
        pass

class Classes_Charge:

    def __init__(self, amount: int, date: date, chargeType: str, Classes_Charge: "Classes_Bill" = None):
        self.amount = amount
        self.date = date
        self.chargeType = chargeType
        self.Classes_Charge = Classes_Charge
        
        pass
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount


    @property
    def chargeType(self):
        return self.__chargeType

    @chargeType.setter
    def chargeType(self, chargeType: str):
        self.__chargeType = chargeType


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def Classes_Charge(self):
        return self.__Classes_Charge

    @Classes_Charge.setter
    def Classes_Charge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Charge__Classes_Charge", None)
        self.__Classes_Charge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_Bill36"):
                opp_val = getattr(old_value, "Classes_Bill36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_Bill36"):
                opp_val = getattr(value, "Classes_Bill36", None)
                if opp_val is None:
                    setattr(value, "Classes_Bill36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classes_IFinance(ABC):

    def __init__(self):
        
        pass
    def payBill(self, Classes_expiryYear, Classes_expiryMonth, Classes_bookingID, Classes_lastName, Classes_firstName, Classes_ccv, Classes_ccNumber, Classes_cost) :
        # TODO: Implement payBill method
        pass

    def calculatePayment(self, Classes_bookingID) :
        # TODO: Implement calculatePayment method
        pass

    def bankSendInvoice(self):
        # TODO: Implement bankSendInvoice method
        pass

class Classes_IBookingManagement(ABC):

    def __init__(self):
        
        pass
    def updateBooking(self, Classes_nrOfGuests, Classes_roomID, Classes_checkOut, Classes_checkIn, Classes_bookingID) :
        # TODO: Implement updateBooking method
        pass

    def confirmBooking(self, Classes_bookingID) :
        # TODO: Implement confirmBooking method
        pass

    def sendConfirmation(self, Classes_message, Classes_bookingID) :
        # TODO: Implement sendConfirmation method
        pass

    def createPendingBooking(self, Classes_checkIn, Classes_checkOut, Classes_guestCount) :
        # TODO: Implement createPendingBooking method
        pass

    def cancelBooking(self, Classes_bookingID) :
        # TODO: Implement cancelBooking method
        pass

    def addRoomPending(self, Classes_room, Classes_bookingID) :
        # TODO: Implement addRoomPending method
        pass

    def getRoomsOfBooking(self, Classes_bookingID) :
        # TODO: Implement getRoomsOfBooking method
        pass

    def addCustomerInformationToBooking(self, Classes_bookingID, Classes_lastName, Classes_ph, Classes_email, Classes_firstName) :
        # TODO: Implement addCustomerInformationToBooking method
        pass

    def searchRoom(self, Classes_numberOfGuests, Classes_checkOut, Classes_roomType, Classes_checkIn, Classes_maximumPrice) :
        # TODO: Implement searchRoom method
        pass

    def addExtraCharge(self, Classes_quantity, Classes_bookingID, Classes_charge) :
        # TODO: Implement addExtraCharge method
        pass

class Classes_CustomerProvides(ABC):

    def __init__(self, Classes_CustomerProvides: "Classes_IFinanceImpl" = None):
        self.Classes_CustomerProvides = Classes_CustomerProvides
        
        pass
    @property
    def Classes_CustomerProvides(self):
        return self.__Classes_CustomerProvides

    @Classes_CustomerProvides.setter
    def Classes_CustomerProvides(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_CustomerProvides__Classes_CustomerProvides", None)
        self.__Classes_CustomerProvides = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_IFinanceImpl"):
                opp_val = getattr(old_value, "Classes_IFinanceImpl", None)
                if opp_val == self:
                    setattr(old_value, "Classes_IFinanceImpl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_IFinanceImpl"):
                opp_val = getattr(value, "Classes_IFinanceImpl", None)
                setattr(value, "Classes_IFinanceImpl", self)

    def makePayment(self, Classes_firstName, Classes_expiryYear, Classes_ccNumber, Classes_lastName, Classes_sum, Classes_ccv, Classes_expiryMonth) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, Classes_firstName, Classes_ccNumber, Classes_expiryMonth, Classes_lastName, Classes_expiryYear, Classes_ccv) :
        # TODO: Implement isCreditCardValid method
        pass

class IFinance:

    pass
class IPerson:

    pass
class Classes_StaffMember(IPerson):

    def __init__(self, admin: str, username: str, password: str, isLoggedIn: bool, Classes_StaffMember: "Classes_IHotelManagerImpl" = None):
        self.admin = admin
        self.username = username
        self.password = password
        self.isLoggedIn = isLoggedIn
        self.Classes_StaffMember = Classes_StaffMember
        
        pass
    @property
    def isLoggedIn(self):
        return self.__isLoggedIn

    @isLoggedIn.setter
    def isLoggedIn(self, isLoggedIn: bool):
        self.__isLoggedIn = isLoggedIn


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, admin: str):
        self.__admin = admin


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username


    @property
    def Classes_StaffMember(self):
        return self.__Classes_StaffMember

    @Classes_StaffMember.setter
    def Classes_StaffMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_StaffMember__Classes_StaffMember", None)
        self.__Classes_StaffMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_IHotelManagerImpl"):
                opp_val = getattr(old_value, "Classes_IHotelManagerImpl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_IHotelManagerImpl"):
                opp_val = getattr(value, "Classes_IHotelManagerImpl", None)
                if opp_val is None:
                    setattr(value, "Classes_IHotelManagerImpl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IHotelManager:

    pass
class Classes_IFinanceImpl(IFinance):

    pass
class Classes_IHotelManagerImpl(IHotelManager):

    pass
class IBookingManagement:

    pass
class Classes_Booking:

    def __init__(self, checkIn: date, checkOut: date, bookingID: str, numberOfGuests: str, booking: "Classes_Customer" = None, confirmedBookings: "Classes_IBookingManagementImpl" = None, Classes_Booking: "Classes_Bill" = None, bookings: set["Classes_Room"] = None, Booking: "Classes_Room" = None, Classes_Booking18: "Classes_IBookingManagementImpl" = None, Classes_Booking23: "Classes_IBookingManagementImpl" = None, Booking28: "Classes_IBookingManagementImpl" = None, Booking12: "Classes_Customer" = None):
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.bookingID = bookingID
        self.numberOfGuests = numberOfGuests
        self.booking = booking
        self.confirmedBookings = confirmedBookings
        self.Classes_Booking = Classes_Booking
        self.bookings = bookings if bookings is not None else set()
        self.Booking = Booking
        self.Classes_Booking18 = Classes_Booking18
        self.Classes_Booking23 = Classes_Booking23
        self.Booking28 = Booking28
        self.Booking12 = Booking12
        
        pass
    @property
    def checkIn(self):
        return self.__checkIn

    @checkIn.setter
    def checkIn(self, checkIn: date):
        self.__checkIn = checkIn


    @property
    def numberOfGuests(self):
        return self.__numberOfGuests

    @numberOfGuests.setter
    def numberOfGuests(self, numberOfGuests: str):
        self.__numberOfGuests = numberOfGuests


    @property
    def bookingID(self):
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: str):
        self.__bookingID = bookingID


    @property
    def checkOut(self):
        return self.__checkOut

    @checkOut.setter
    def checkOut(self, checkOut: date):
        self.__checkOut = checkOut


    @property
    def Booking(self):
        return self.__Booking

    @Booking.setter
    def Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Booking", None)
        self.__Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms"):
                opp_val = getattr(old_value, "rooms", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms"):
                opp_val = getattr(value, "rooms", None)
                if opp_val is None:
                    setattr(value, "rooms", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classes_Booking18(self):
        return self.__Classes_Booking18

    @Classes_Booking18.setter
    def Classes_Booking18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Classes_Booking18", None)
        self.__Classes_Booking18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_IBookingManagementImpl17"):
                opp_val = getattr(old_value, "Classes_IBookingManagementImpl17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_IBookingManagementImpl17"):
                opp_val = getattr(value, "Classes_IBookingManagementImpl17", None)
                if opp_val is None:
                    setattr(value, "Classes_IBookingManagementImpl17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def confirmedBookings(self):
        return self.__confirmedBookings

    @confirmedBookings.setter
    def confirmedBookings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__confirmedBookings", None)
        self.__confirmedBookings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IBookingManagementImpl7"):
                opp_val = getattr(old_value, "IBookingManagementImpl7", None)
                if opp_val == self:
                    setattr(old_value, "IBookingManagementImpl7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IBookingManagementImpl7"):
                opp_val = getattr(value, "IBookingManagementImpl7", None)
                setattr(value, "IBookingManagementImpl7", self)

    @property
    def Classes_Booking23(self):
        return self.__Classes_Booking23

    @Classes_Booking23.setter
    def Classes_Booking23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Classes_Booking23", None)
        self.__Classes_Booking23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_IBookingManagementImpl22"):
                opp_val = getattr(old_value, "Classes_IBookingManagementImpl22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_IBookingManagementImpl22"):
                opp_val = getattr(value, "Classes_IBookingManagementImpl22", None)
                if opp_val is None:
                    setattr(value, "Classes_IBookingManagementImpl22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookings(self):
        return self.__bookings

    @bookings.setter
    def bookings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__bookings", None)
        self.__bookings = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room10"):
                    opp_val = getattr(item, "Room10", None)
                    
                    if opp_val == self:
                        setattr(item, "Room10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room10"):
                    opp_val = getattr(item, "Room10", None)
                    
                    setattr(item, "Room10", self)
                    

    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__booking", None)
        self.__booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def Booking28(self):
        return self.__Booking28

    @Booking28.setter
    def Booking28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Booking28", None)
        self.__Booking28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iBookingManagementImpl27"):
                opp_val = getattr(old_value, "iBookingManagementImpl27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iBookingManagementImpl27"):
                opp_val = getattr(value, "iBookingManagementImpl27", None)
                if opp_val is None:
                    setattr(value, "iBookingManagementImpl27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Booking12(self):
        return self.__Booking12

    @Booking12.setter
    def Booking12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Booking12", None)
        self.__Booking12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classes_Booking(self):
        return self.__Classes_Booking

    @Classes_Booking.setter
    def Classes_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Booking__Classes_Booking", None)
        self.__Classes_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classes_Bill"):
                opp_val = getattr(old_value, "Classes_Bill", None)
                if opp_val == self:
                    setattr(old_value, "Classes_Bill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classes_Bill"):
                opp_val = getattr(value, "Classes_Bill", None)
                setattr(value, "Classes_Bill", self)

class Classes_IHotelManager(ABC):

    def __init__(self):
        
        pass
    def getStaffMemberPhoneNumber(self, Classes_username) :
        # TODO: Implement getStaffMemberPhoneNumber method
        pass

    def isValidUsername(self, Classes_username) :
        # TODO: Implement isValidUsername method
        pass

    def getStaffMemberEmail(self, Classes_username) :
        # TODO: Implement getStaffMemberEmail method
        pass

    def getStaffMemberFirstName(self, Classes_username) :
        # TODO: Implement getStaffMemberFirstName method
        pass

    def logout(self, Classes_username) :
        # TODO: Implement logout method
        pass

    def addStaffMember(self, Classes_lastName, Classes_password, Classes_adminUsername, Classes_address, Classes_firstName, Classes_admin, Classes_username, Classes_email, Classes_phoneNumber) :
        # TODO: Implement addStaffMember method
        pass

    def checkOut(self, Classes_staffMemberUsername, Classes_bookingID) :
        # TODO: Implement checkOut method
        pass

    def isStaffMemberAdmin(self, Classes_username) :
        # TODO: Implement isStaffMemberAdmin method
        pass

    def changeStatusOfRoom(self, Classes_status, Classes_roomID, Classes_staffMemberUsername) :
        # TODO: Implement changeStatusOfRoom method
        pass

    def login(self, Classes_password, Classes_username) :
        # TODO: Implement login method
        pass

    def getStaffMemberLastName(self, Classes_username) :
        # TODO: Implement getStaffMemberLastName method
        pass

    def isStaffMemberLoggedIn(self, Classes_username) :
        # TODO: Implement isStaffMemberLoggedIn method
        pass

    def isPasswordSecure(self, Classes_password) :
        # TODO: Implement isPasswordSecure method
        pass

    def checkInBooking(self, Classes_staffMemberUsername, Classes_bookingID) :
        # TODO: Implement checkInBooking method
        pass

    def getStaffMemberAddress(self, Classes_username) :
        # TODO: Implement getStaffMemberAddress method
        pass

    def getStaffMemberPassword(self, Classes_username) :
        # TODO: Implement getStaffMemberPassword method
        pass

class Classes_IPerson(ABC):

    def __init__(self, firstName: str, lastName: str, address: str, email: str, phoneNumber: str):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


class Classes_Bill:

    pass
class Classes_Customer(IPerson):

    pass
class Classes_IBookingManagementImpl(IBookingManagement):

    pass
class Classes_RoomType:

    def __init__(self, roomTypeName: str, features: str, numberOfGuests: str, description: str, price: str, RoomType: "Classes_Room" = None, roomType: set["Classes_Room"] = None):
        self.roomTypeName = roomTypeName
        self.features = features
        self.numberOfGuests = numberOfGuests
        self.description = description
        self.price = price
        self.RoomType = RoomType
        self.roomType = roomType if roomType is not None else set()
        
        pass
    @property
    def roomTypeName(self):
        return self.__roomTypeName

    @roomTypeName.setter
    def roomTypeName(self, roomTypeName: str):
        self.__roomTypeName = roomTypeName


    @property
    def numberOfGuests(self):
        return self.__numberOfGuests

    @numberOfGuests.setter
    def numberOfGuests(self, numberOfGuests: str):
        self.__numberOfGuests = numberOfGuests


    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features


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
    def price(self, price: str):
        self.__price = price


    @property
    def RoomType(self):
        return self.__RoomType

    @RoomType.setter
    def RoomType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_RoomType__RoomType", None)
        self.__RoomType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room"):
                opp_val = getattr(old_value, "room", None)
                if opp_val == self:
                    setattr(old_value, "room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room"):
                opp_val = getattr(value, "room", None)
                setattr(value, "room", self)

    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_RoomType__roomType", None)
        self.__roomType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room"):
                    opp_val = getattr(item, "Room", None)
                    
                    if opp_val == self:
                        setattr(item, "Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room"):
                    opp_val = getattr(item, "Room", None)
                    
                    setattr(item, "Room", self)
                    

class Classes_Room:

    def __init__(self, status: str, roomNumber: str, room: "Classes_RoomType" = None, room3: "Classes_IBookingManagementImpl" = None, Room: "Classes_RoomType" = None, Room10: "Classes_Booking" = None, rooms: set["Classes_Booking"] = None, Room15: "Classes_IBookingManagementImpl" = None):
        self.status = status
        self.roomNumber = roomNumber
        self.room = room
        self.room3 = room3
        self.Room = Room
        self.Room10 = Room10
        self.rooms = rooms if rooms is not None else set()
        self.Room15 = Room15
        
        pass
    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: str):
        self.__roomNumber = roomNumber


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def Room(self):
        return self.__Room

    @Room.setter
    def Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__Room", None)
        self.__Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roomType"):
                opp_val = getattr(old_value, "roomType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roomType"):
                opp_val = getattr(value, "roomType", None)
                if opp_val is None:
                    setattr(value, "roomType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__rooms", None)
        self.__rooms = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Booking"):
                    opp_val = getattr(item, "Booking", None)
                    
                    if opp_val == self:
                        setattr(item, "Booking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Booking"):
                    opp_val = getattr(item, "Booking", None)
                    
                    setattr(item, "Booking", self)
                    

    @property
    def Room15(self):
        return self.__Room15

    @Room15.setter
    def Room15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__Room15", None)
        self.__Room15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iBookingManagementImpl"):
                opp_val = getattr(old_value, "iBookingManagementImpl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iBookingManagementImpl"):
                opp_val = getattr(value, "iBookingManagementImpl", None)
                if opp_val is None:
                    setattr(value, "iBookingManagementImpl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__room", None)
        self.__room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoomType"):
                opp_val = getattr(old_value, "RoomType", None)
                if opp_val == self:
                    setattr(old_value, "RoomType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoomType"):
                opp_val = getattr(value, "RoomType", None)
                setattr(value, "RoomType", self)

    @property
    def Room10(self):
        return self.__Room10

    @Room10.setter
    def Room10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__Room10", None)
        self.__Room10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookings"):
                opp_val = getattr(old_value, "bookings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookings"):
                opp_val = getattr(value, "bookings", None)
                if opp_val is None:
                    setattr(value, "bookings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room3(self):
        return self.__room3

    @room3.setter
    def room3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Room__room3", None)
        self.__room3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IBookingManagementImpl"):
                opp_val = getattr(old_value, "IBookingManagementImpl", None)
                if opp_val == self:
                    setattr(old_value, "IBookingManagementImpl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IBookingManagementImpl"):
                opp_val = getattr(value, "IBookingManagementImpl", None)
                setattr(value, "IBookingManagementImpl", self)
