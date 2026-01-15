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
class Classes_mdsdAccount_AccountController(mdsdAccount_BookingToAccount, mdsdAccount_CustomerAccount):

    pass
class Classes_mdsdAccount_Pet:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Classes_mdsdAccount_CustomerAccount(ABC):

    def __init__(self):
        
    def logout(self, accountId: str):
        # TODO: Implement logout method
        pass

    def removePet(self, accountID: str, name: str, type: str):
        # TODO: Implement removePet method
        pass

    def login(self, email: str, password: str):
        # TODO: Implement login method
        pass

    def addPet(self, type: str, accountID: str, name: str):
        # TODO: Implement addPet method
        pass

    def createAccount(self, customerEmail: str, customerName: str, password: str) -> str:
        # TODO: Implement createAccount method
        pass

class Classes_mdsdAccount_BookingToAccount(ABC):

    def __init__(self):
        
    def getAccount(self, email: str) -> str:
        # TODO: Implement getAccount method
        pass

    def isUserLoggedIn(self, accountId: str) -> bool:
        # TODO: Implement isUserLoggedIn method
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
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isLoggedIn(self) -> bool:
        return self.__isLoggedIn

    @isLoggedIn.setter
    def isLoggedIn(self, isLoggedIn: bool):
        self.__isLoggedIn = isLoggedIn

    @property
    def accountID(self) -> str:
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
                    

class Classes_mdsdAdmin_Staff(ABC):

    def __init__(self):
        
    def staffLogin(self, password: str, ssn: str):
        # TODO: Implement staffLogin method
        pass

    def changeRoomStatus(self, roomNumber: int, status: str):
        # TODO: Implement changeRoomStatus method
        pass

    def staffLogout(self, ssn: str):
        # TODO: Implement staffLogout method
        pass

class Classes_mdsdAdmin_BookingToAdmin(ABC):

    def __init__(self):
        
    def getPetTypes(self) -> str:
        # TODO: Implement getPetTypes method
        pass

class Classes_mdsdAdmin_Room:

    def __init__(self, type: str, status: str, number: int):
        self.type = type
        self.status = status
        self.number = number
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

class Classes_mdsdAdmin_Admin(ABC):

    def __init__(self):
        
    def removeRoom(self, number: int):
        # TODO: Implement removeRoom method
        pass

    def createStaff(self, password: str, rank: int, SSN: str, name: str) -> str:
        # TODO: Implement createStaff method
        pass

    def modifyStaff(self, newName: str, SSN: str, newRank: int):
        # TODO: Implement modifyStaff method
        pass

    def addRoom(self, status: str, type: str, room: int) -> str:
        # TODO: Implement addRoom method
        pass

    def removeStaff(self, SSN: str):
        # TODO: Implement removeStaff method
        pass

class Room:

    pass
class mdsdAdmin_Staff:

    pass
class mdsdAdmin_BookingToAdmin:

    pass
class mdsdAdmin_Admin:

    pass
class Classes_mdsdAdmin_AdminController(mdsdAdmin_BookingToAdmin, mdsdAdmin_Staff, mdsdAdmin_Admin):

    def __init__(self, Classes_mdsdAdmin_AdminController: set["Room"] = None, Classes_mdsdAdmin_AdminController11: set["HotelStaff"] = None):
        self.Classes_mdsdAdmin_AdminController = Classes_mdsdAdmin_AdminController if Classes_mdsdAdmin_AdminController is not None else set()
        self.Classes_mdsdAdmin_AdminController11 = Classes_mdsdAdmin_AdminController11 if Classes_mdsdAdmin_AdminController11 is not None else set()
        
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
                    

    def isLoggedIn(self, ssn: str) -> bool:
        # TODO: Implement isLoggedIn method
        pass

class Classes_mdsdAdmin_HotelStaff:

    def __init__(self, Name: str, rank: int, SSN: str, isLoggedIn: bool, password: str):
        self.Name = Name
        self.rank = rank
        self.SSN = SSN
        self.isLoggedIn = isLoggedIn
        self.password = password
        
    @property
    def isLoggedIn(self) -> bool:
        return self.__isLoggedIn

    @isLoggedIn.setter
    def isLoggedIn(self, isLoggedIn: bool):
        self.__isLoggedIn = isLoggedIn

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def SSN(self) -> str:
        return self.__SSN

    @SSN.setter
    def SSN(self, SSN: str):
        self.__SSN = SSN

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class HotelStaff:

    pass
class Classes_mdsdBooking_Booking:

    def __init__(self, bookingId: str, isCheckedIn: bool, isCheckedOut: bool, roomNumber: int, dateFrom: date, customerName: str, customerEmail: str, dateTo: date, bill_Id: str, petName: str, Classes_mdsdBooking_Booking: set["Service"] = None, Classes_mdsdBooking_Booking8: "Meal" = None):
        self.bookingId = bookingId
        self.isCheckedIn = isCheckedIn
        self.isCheckedOut = isCheckedOut
        self.roomNumber = roomNumber
        self.dateFrom = dateFrom
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.dateTo = dateTo
        self.bill_Id = bill_Id
        self.petName = petName
        self.Classes_mdsdBooking_Booking = Classes_mdsdBooking_Booking if Classes_mdsdBooking_Booking is not None else set()
        self.Classes_mdsdBooking_Booking8 = Classes_mdsdBooking_Booking8
        
    @property
    def roomNumber(self) -> int:
        return self.__roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int):
        self.__roomNumber = roomNumber

    @property
    def dateFrom(self) -> date:
        return self.__dateFrom

    @dateFrom.setter
    def dateFrom(self, dateFrom: date):
        self.__dateFrom = dateFrom

    @property
    def dateTo(self) -> date:
        return self.__dateTo

    @dateTo.setter
    def dateTo(self, dateTo: date):
        self.__dateTo = dateTo

    @property
    def bookingId(self) -> str:
        return self.__bookingId

    @bookingId.setter
    def bookingId(self, bookingId: str):
        self.__bookingId = bookingId

    @property
    def bill_Id(self) -> str:
        return self.__bill_Id

    @bill_Id.setter
    def bill_Id(self, bill_Id: str):
        self.__bill_Id = bill_Id

    @property
    def isCheckedOut(self) -> bool:
        return self.__isCheckedOut

    @isCheckedOut.setter
    def isCheckedOut(self, isCheckedOut: bool):
        self.__isCheckedOut = isCheckedOut

    @property
    def customerName(self) -> str:
        return self.__customerName

    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def isCheckedIn(self) -> bool:
        return self.__isCheckedIn

    @isCheckedIn.setter
    def isCheckedIn(self, isCheckedIn: bool):
        self.__isCheckedIn = isCheckedIn

    @property
    def customerEmail(self) -> str:
        return self.__customerEmail

    @customerEmail.setter
    def customerEmail(self, customerEmail: str):
        self.__customerEmail = customerEmail

    @property
    def petName(self) -> str:
        return self.__petName

    @petName.setter
    def petName(self, petName: str):
        self.__petName = petName

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

class Classes_mdsdBooking_Meal:

    def __init__(self, foodType: str, schedule: str, amountOfFood: float, price: float):
        self.foodType = foodType
        self.schedule = schedule
        self.amountOfFood = amountOfFood
        self.price = price
        
    @property
    def foodType(self) -> str:
        return self.__foodType

    @foodType.setter
    def foodType(self, foodType: str):
        self.__foodType = foodType

    @property
    def amountOfFood(self) -> float:
        return self.__amountOfFood

    @amountOfFood.setter
    def amountOfFood(self, amountOfFood: float):
        self.__amountOfFood = amountOfFood

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def schedule(self) -> str:
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule: str):
        self.__schedule = schedule

class Meal:

    pass
class Classes_mdsdBooking_StaffBooking(ABC):

    def __init__(self):
        
    def checkIn(self, bookingID: str, rooms: str):
        # TODO: Implement checkIn method
        pass

    def addNewService(self, description: str, price: float):
        # TODO: Implement addNewService method
        pass

    def checkOut(self, bills: str, rooms: str, bookingID: str) -> bool:
        # TODO: Implement checkOut method
        pass

class Classes_mdsdBooking_UserBooking(ABC):

    def __init__(self):
        
    def enterMealInfo(self, amountOfFood: float, price: float, schedule: str, bookingId: str, foodType: str):
        # TODO: Implement enterMealInfo method
        pass

    def enterDatesOfStay(self, rooms: str, stayFrom: date, stayTo: date, petType: str) -> str:
        # TODO: Implement enterDatesOfStay method
        pass

    def cancelBooking(self, bookingId: str):
        # TODO: Implement cancelBooking method
        pass

    def enterService(self, service: str, bookingId: str):
        # TODO: Implement enterService method
        pass

    def enterCustomerInfo(self, rooms: str, booking: str, customerEmail: str, customerName: str, petName: str):
        # TODO: Implement enterCustomerInfo method
        pass

    def modifyBooking(self, bookingId: str):
        # TODO: Implement modifyBooking method
        pass

class Classes_mdsdBooking_Service:

    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Service:

    pass
class Classes_mdsdBilling_CustomerBilling(ABC):

    pass
class Classes_mdsdBilling_BookingToBill(ABC):

    def __init__(self):
        
    def addTransaction(self, description: str, booking: str, amount: float):
        # TODO: Implement addTransaction method
        pass

class Booking:

    pass
class mdsdBooking_StaffBooking:

    pass
class mdsdBooking_UserBooking:

    pass
class Classes_mdsdBooking_BookingController(mdsdBooking_UserBooking, mdsdBooking_StaffBooking):

    def __init__(self, Classes_mdsdBooking_BookingController: set["Booking"] = None, Classes_mdsdBooking_BookingController4: set["Service"] = None):
        self.Classes_mdsdBooking_BookingController = Classes_mdsdBooking_BookingController if Classes_mdsdBooking_BookingController is not None else set()
        self.Classes_mdsdBooking_BookingController4 = Classes_mdsdBooking_BookingController4 if Classes_mdsdBooking_BookingController4 is not None else set()
        
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
                    

    def getBookingList(self, email: str) -> str:
        # TODO: Implement getBookingList method
        pass

class Classes_mdsdBilling_StaffBilling(ABC):

    def __init__(self):
        
    def isPaid(self, billID: str) -> bool:
        # TODO: Implement isPaid method
        pass

    def printReceipt(self, billID: str):
        # TODO: Implement printReceipt method
        pass

    def giveRefund(self, transaction: str, billId: str):
        # TODO: Implement giveRefund method
        pass

    def modifyBill(self, newPrice: float, billID: str, transaction: str):
        # TODO: Implement modifyBill method
        pass

class Classes_mdsdBilling_Transaction:

    def __init__(self, description: str, price: float):
        self.description = description
        self.price = price
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Transaction:

    pass
class Classes_mdsdBilling_Bill:

    def __init__(self, isPaid: bool, ID: str, Classes_mdsdBilling_Bill: set["Transaction"] = None):
        self.isPaid = isPaid
        self.ID = ID
        self.Classes_mdsdBilling_Bill = Classes_mdsdBilling_Bill if Classes_mdsdBilling_Bill is not None else set()
        
    @property
    def isPaid(self) -> bool:
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: bool):
        self.__isPaid = isPaid

    @property
    def ID(self) -> str:
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
                    

    def getTotalAmount(self) -> float:
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
class Classes_mdsdBilling_BillingController(mdsdBilling_StaffBilling, mdsdBilling_BookingToBill, mdsdBilling_CustomerBilling):

    pass