from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Account:

    pass
class mdsdAccount_CustomerAccount:

    pass
class mdsdAccount_BookingToAccount:

    pass
class Classes_mdsdAccount_AccountController(mdsdAccount_CustomerAccount, mdsdAccount_BookingToAccount):

    pass
class Classes_mdsdAccount_CustomerAccount(ABC):

    def __init__(self):
        
        pass
    def removePet(self, Classes_type, Classes_accountID, Classes_name):
        # TODO: Implement removePet method
        pass

    def createAccount(self, Classes_customerName, Classes_password, Classes_customerEmail) :
        # TODO: Implement createAccount method
        pass

    def logout(self, Classes_accountId):
        # TODO: Implement logout method
        pass

    def addPet(self, Classes_name, Classes_type, Classes_accountID):
        # TODO: Implement addPet method
        pass

    def login(self, Classes_email, Classes_password):
        # TODO: Implement login method
        pass

class Classes_mdsdAccount_Pet:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Classes_mdsdAdmin_Staff(ABC):

    def __init__(self):
        
        pass
    def staffLogin(self, Classes_password, Classes_ssn):
        # TODO: Implement staffLogin method
        pass

    def staffLogout(self, Classes_ssn):
        # TODO: Implement staffLogout method
        pass

    def changeRoomStatus(self, Classes_roomNumber, Classes_status):
        # TODO: Implement changeRoomStatus method
        pass

class Classes_mdsdAdmin_BookingToAdmin(ABC):

    def __init__(self):
        
        pass
    def getPetTypes(self) :
        # TODO: Implement getPetTypes method
        pass

class Classes_mdsdAdmin_Admin(ABC):

    def __init__(self):
        
        pass
    def createStaff(self, Classes_rank, Classes_name, Classes_SSN, Classes_password) :
        # TODO: Implement createStaff method
        pass

    def removeRoom(self, Classes_number):
        # TODO: Implement removeRoom method
        pass

    def addRoom(self, Classes_type, Classes_status, Classes_room) :
        # TODO: Implement addRoom method
        pass

    def removeStaff(self, Classes_SSN):
        # TODO: Implement removeStaff method
        pass

    def modifyStaff(self, Classes_SSN, Classes_newRank, Classes_newName):
        # TODO: Implement modifyStaff method
        pass

class Pet:

    pass
class Classes_mdsdAccount_Account:

    def __init__(self, accountID: str, password: str, name: str, email: str, isLoggedIn: bool, Classes_mdsdAccount_Account: set["Pet"] = None):
        self.accountID = accountID
        self.password = password
        self.name = name
        self.email = email
        self.isLoggedIn = isLoggedIn
        self.Classes_mdsdAccount_Account = Classes_mdsdAccount_Account if Classes_mdsdAccount_Account is not None else set()
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def isLoggedIn(self):
        return self.__isLoggedIn

    @isLoggedIn.setter
    def isLoggedIn(self, isLoggedIn: bool):
        self.__isLoggedIn = isLoggedIn


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def accountID(self):
        return self.__accountID

    @accountID.setter
    def accountID(self, accountID: str):
        self.__accountID = accountID


    @property
    def Classes_mdsdAccount_Account(self):
        return self.__Classes_mdsdAccount_Account

    @Classes_mdsdAccount_Account.setter
    def Classes_mdsdAccount_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdAccount_Account__Classes_mdsdAccount_Account", None)
        self.__Classes_mdsdAccount_Account = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pet"):
                    opp_val = getattr(item, "Pet", None)
                    
                    if opp_val == self:
                        setattr(item, "Pet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pet"):
                    opp_val = getattr(item, "Pet", None)
                    
                    setattr(item, "Pet", self)
                    

class Classes_mdsdAccount_BookingToAccount(ABC):

    def __init__(self):
        
        pass
    def getAccount(self, Classes_email) :
        # TODO: Implement getAccount method
        pass

    def isUserLoggedIn(self, Classes_accountId) :
        # TODO: Implement isUserLoggedIn method
        pass

class Classes_mdsdAdmin_Room:

    def __init__(self, type: str, status: str, number: int):
        self.type = type
        self.status = status
        self.number = number
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


class Classes_mdsdBooking_Booking:

    def __init__(self, roomNumber: int, dateFrom: date, dateTo: date, bill_Id: str, petName: str, customerName: str, customerEmail: str, bookingId: str, isCheckedIn: bool, isCheckedOut: bool, Classes_mdsdBooking_Booking8: "Meal" = None, Classes_mdsdBooking_Booking: set["Service"] = None):
        self.roomNumber = roomNumber
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.bill_Id = bill_Id
        self.petName = petName
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.bookingId = bookingId
        self.isCheckedIn = isCheckedIn
        self.isCheckedOut = isCheckedOut
        self.Classes_mdsdBooking_Booking8 = Classes_mdsdBooking_Booking8
        self.Classes_mdsdBooking_Booking = Classes_mdsdBooking_Booking if Classes_mdsdBooking_Booking is not None else set()
        
        pass
    @property
    def dateTo(self):
        return self.__dateTo

    @dateTo.setter
    def dateTo(self, dateTo: date):
        self.__dateTo = dateTo


    @property
    def customerName(self):
        return self.__customerName

    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName


    @property
    def roomNumber(self):
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber


    @property
    def petName(self):
        return self.__petName

    @petName.setter
    def petName(self, petName: str):
        self.__petName = petName


    @property
    def isCheckedIn(self):
        return self.__isCheckedIn

    @isCheckedIn.setter
    def isCheckedIn(self, isCheckedIn: bool):
        self.__isCheckedIn = isCheckedIn


    @property
    def customerEmail(self):
        return self.__customerEmail

    @customerEmail.setter
    def customerEmail(self, customerEmail: str):
        self.__customerEmail = customerEmail


    @property
    def dateFrom(self):
        return self.__dateFrom

    @dateFrom.setter
    def dateFrom(self, dateFrom: date):
        self.__dateFrom = dateFrom


    @property
    def bill_Id(self):
        return self.__bill_Id

    @bill_Id.setter
    def bill_Id(self, bill_Id: str):
        self.__bill_Id = bill_Id


    @property
    def bookingId(self):
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: str):
        self.__bookingId = bookingId


    @property
    def isCheckedOut(self):
        return self.__isCheckedOut

    @isCheckedOut.setter
    def isCheckedOut(self, isCheckedOut: bool):
        self.__isCheckedOut = isCheckedOut


    @property
    def Classes_mdsdBooking_Booking8(self):
        return self.__Classes_mdsdBooking_Booking8

    @Classes_mdsdBooking_Booking8.setter
    def Classes_mdsdBooking_Booking8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdBooking_Booking__Classes_mdsdBooking_Booking8", None)
        self.__Classes_mdsdBooking_Booking8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Meal"):
                opp_val = getattr(old_value, "Meal", None)
                if opp_val == self:
                    setattr(old_value, "Meal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Meal"):
                opp_val = getattr(value, "Meal", None)
                setattr(value, "Meal", self)

    @property
    def Classes_mdsdBooking_Booking(self):
        return self.__Classes_mdsdBooking_Booking

    @Classes_mdsdBooking_Booking.setter
    def Classes_mdsdBooking_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdBooking_Booking__Classes_mdsdBooking_Booking", None)
        self.__Classes_mdsdBooking_Booking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service6"):
                    opp_val = getattr(item, "Service6", None)
                    
                    if opp_val == self:
                        setattr(item, "Service6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service6"):
                    opp_val = getattr(item, "Service6", None)
                    
                    setattr(item, "Service6", self)
                    

class Classes_mdsdBooking_Meal:

    def __init__(self, foodType: str, schedule: str, amountOfFood: float, price: float):
        self.foodType = foodType
        self.schedule = schedule
        self.amountOfFood = amountOfFood
        self.price = price
        
        pass
    @property
    def foodType(self):
        return self.__foodType

    @foodType.setter
    def foodType(self, foodType: str):
        self.__foodType = foodType


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def amountOfFood(self):
        return self.__amountOfFood

    @amountOfFood.setter
    def amountOfFood(self, amountOfFood: float):
        self.__amountOfFood = amountOfFood


    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule: str):
        self.__schedule = schedule


class Classes_mdsdBooking_StaffBooking(ABC):

    def __init__(self):
        
        pass
    def checkIn(self, Classes_rooms, Classes_bookingID):
        # TODO: Implement checkIn method
        pass

    def checkOut(self, Classes_rooms, Classes_bills, Classes_bookingID) :
        # TODO: Implement checkOut method
        pass

    def addNewService(self, Classes_description, Classes_price):
        # TODO: Implement addNewService method
        pass

class Classes_mdsdAdmin_HotelStaff:

    def __init__(self, Name: str, rank: int, SSN: str, isLoggedIn: bool, password: str):
        self.Name = Name
        self.rank = rank
        self.SSN = SSN
        self.isLoggedIn = isLoggedIn
        self.password = password
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank


    @property
    def SSN(self):
        return self.__SSN

    @SSN.setter
    def SSN(self, SSN: str):
        self.__SSN = SSN


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


class HotelStaff:

    pass
class Room:

    pass
class mdsdAdmin_Staff:

    pass
class mdsdAdmin_BookingToAdmin:

    pass
class mdsdAdmin_Admin:

    pass
class Classes_mdsdAdmin_AdminController(mdsdAdmin_BookingToAdmin, mdsdAdmin_Admin, mdsdAdmin_Staff):

    def __init__(self, Classes_mdsdAdmin_AdminController: set["Room"] = None, Classes_mdsdAdmin_AdminController11: set["HotelStaff"] = None):
        self.Classes_mdsdAdmin_AdminController = Classes_mdsdAdmin_AdminController if Classes_mdsdAdmin_AdminController is not None else set()
        self.Classes_mdsdAdmin_AdminController11 = Classes_mdsdAdmin_AdminController11 if Classes_mdsdAdmin_AdminController11 is not None else set()
        
        pass
    @property
    def Classes_mdsdAdmin_AdminController(self):
        return self.__Classes_mdsdAdmin_AdminController

    @Classes_mdsdAdmin_AdminController.setter
    def Classes_mdsdAdmin_AdminController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdAdmin_AdminController__Classes_mdsdAdmin_AdminController", None)
        self.__Classes_mdsdAdmin_AdminController = value if value is not None else set()
        
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
                    

    @property
    def Classes_mdsdAdmin_AdminController11(self):
        return self.__Classes_mdsdAdmin_AdminController11

    @Classes_mdsdAdmin_AdminController11.setter
    def Classes_mdsdAdmin_AdminController11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdAdmin_AdminController__Classes_mdsdAdmin_AdminController11", None)
        self.__Classes_mdsdAdmin_AdminController11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HotelStaff"):
                    opp_val = getattr(item, "HotelStaff", None)
                    
                    if opp_val == self:
                        setattr(item, "HotelStaff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HotelStaff"):
                    opp_val = getattr(item, "HotelStaff", None)
                    
                    setattr(item, "HotelStaff", self)
                    

    def isLoggedIn(self, Classes_ssn) :
        # TODO: Implement isLoggedIn method
        pass

class Meal:

    pass
class Classes_mdsdBooking_Service:

    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price
        
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


class Service:

    pass
class Booking:

    pass
class mdsdBooking_StaffBooking:

    pass
class mdsdBooking_UserBooking:

    pass
class Classes_mdsdBooking_BookingController(mdsdBooking_StaffBooking, mdsdBooking_UserBooking):

    def __init__(self, Classes_mdsdBooking_BookingController: set["Booking"] = None, Classes_mdsdBooking_BookingController4: set["Service"] = None):
        self.Classes_mdsdBooking_BookingController = Classes_mdsdBooking_BookingController if Classes_mdsdBooking_BookingController is not None else set()
        self.Classes_mdsdBooking_BookingController4 = Classes_mdsdBooking_BookingController4 if Classes_mdsdBooking_BookingController4 is not None else set()
        
        pass
    @property
    def Classes_mdsdBooking_BookingController(self):
        return self.__Classes_mdsdBooking_BookingController

    @Classes_mdsdBooking_BookingController.setter
    def Classes_mdsdBooking_BookingController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController", None)
        self.__Classes_mdsdBooking_BookingController = value if value is not None else set()
        
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
    def Classes_mdsdBooking_BookingController4(self):
        return self.__Classes_mdsdBooking_BookingController4

    @Classes_mdsdBooking_BookingController4.setter
    def Classes_mdsdBooking_BookingController4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4", None)
        self.__Classes_mdsdBooking_BookingController4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

    def getBookingList(self, Classes_email) :
        # TODO: Implement getBookingList method
        pass

class Classes_mdsdBilling_CustomerBilling(ABC):

    pass
class Classes_mdsdBilling_BookingToBill(ABC):

    def __init__(self):
        
        pass
    def addTransaction(self, Classes_booking, Classes_description, Classes_amount):
        # TODO: Implement addTransaction method
        pass

class Classes_mdsdBilling_StaffBilling(ABC):

    def __init__(self):
        
        pass
    def modifyBill(self, Classes_transaction, Classes_billID, Classes_newPrice):
        # TODO: Implement modifyBill method
        pass

    def printReceipt(self, Classes_billID):
        # TODO: Implement printReceipt method
        pass

    def isPaid(self, Classes_billID) :
        # TODO: Implement isPaid method
        pass

    def giveRefund(self, Classes_billId, Classes_transaction):
        # TODO: Implement giveRefund method
        pass

class Classes_mdsdBooking_UserBooking(ABC):

    def __init__(self):
        
        pass
    def enterCustomerInfo(self, Classes_rooms, Classes_customerName, Classes_customerEmail, Classes_petName, Classes_booking):
        # TODO: Implement enterCustomerInfo method
        pass

    def enterDatesOfStay(self, Classes_stayTo, Classes_stayFrom, Classes_petType, Classes_rooms) :
        # TODO: Implement enterDatesOfStay method
        pass

    def cancelBooking(self, Classes_bookingId):
        # TODO: Implement cancelBooking method
        pass

    def enterMealInfo(self, Classes_bookingId, Classes_foodType, Classes_schedule, Classes_amountOfFood, Classes_price):
        # TODO: Implement enterMealInfo method
        pass

    def enterService(self, Classes_service, Classes_bookingId):
        # TODO: Implement enterService method
        pass

    def modifyBooking(self, Classes_bookingId):
        # TODO: Implement modifyBooking method
        pass

class Classes_mdsdBilling_Transaction:

    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price
        
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


class Transaction:

    pass
class Classes_mdsdBilling_Bill:

    def __init__(self, isPaid: bool, ID: str, Classes_mdsdBilling_Bill: set["Transaction"] = None):
        self.isPaid = isPaid
        self.ID = ID
        self.Classes_mdsdBilling_Bill = Classes_mdsdBilling_Bill if Classes_mdsdBilling_Bill is not None else set()
        
        pass
    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: bool):
        self.__isPaid = isPaid


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def Classes_mdsdBilling_Bill(self):
        return self.__Classes_mdsdBilling_Bill

    @Classes_mdsdBilling_Bill.setter
    def Classes_mdsdBilling_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_mdsdBilling_Bill__Classes_mdsdBilling_Bill", None)
        self.__Classes_mdsdBilling_Bill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    setattr(item, "Transaction", self)
                    

    def getTotalAmount(self) :
        # TODO: Implement getTotalAmount method
        pass

class Bill:

    pass
class mdsdBilling_CustomerBilling:

    pass
class mdsdBilling_BookingToBill:

    pass
class mdsdBilling_StaffBilling:

    pass
class Classes_mdsdBilling_BillingController(mdsdBilling_CustomerBilling, mdsdBilling_BookingToBill, mdsdBilling_StaffBilling):

    pass