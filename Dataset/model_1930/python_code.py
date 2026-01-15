from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class newClasses_ManagerInterface(ABC):

    def __init__(self):
        
    def login(self, userName: str, password: str):
        # TODO: Implement login method
        pass

    def SessionData(self):
        # TODO: Implement SessionData method
        pass

    def logout(self):
        # TODO: Implement logout method
        pass

    def validateLogin(self, password: str, userName: str) -> str:
        # TODO: Implement validateLogin method
        pass

class newClasses_AdministratorProvides(ABC):

    def __init__(self):
        
    def addCreditCard(self, expiryYear: int, ccv: str, expiryMonth: int, firstName: str, ccNumber: str, lastName: str) -> bool:
        # TODO: Implement addCreditCard method
        pass

    def getBalance(self, expiryYear: int, ccNumber: str, lastName: str, ccv: str, expiryMonth: int, firstName: str) -> float:
        # TODO: Implement getBalance method
        pass

    def removeCreditCard(self, ccNumber: str, firstName: str, ccv: str, expiryYear: int, lastName: str, expiryMonth: int) -> bool:
        # TODO: Implement removeCreditCard method
        pass

    def makeDeposit(self, lastName: str, firstName: str, expiryYear: int, ccv: str, ccNumber: str, expiryMonth: int, sum: float) -> float:
        # TODO: Implement makeDeposit method
        pass

class AdministratorProvides:

    pass
class newClasses_RoomHandlerInterface(ABC):

    def __init__(self):
        
    def addRoom(self, price: str, roomNum: str, roomType: str):
        # TODO: Implement addRoom method
        pass

    def changeRoomPrice(self, roomNum: str, newPrice: str):
        # TODO: Implement changeRoomPrice method
        pass

    def changeRoomType(self, roomNum: str, roomType: str):
        # TODO: Implement changeRoomType method
        pass

    def removeRoom(self, roomNum: str):
        # TODO: Implement removeRoom method
        pass

class newClasses_ServiceHandlerInterface(ABC):

    def __init__(self):
        
    def changeServiceType(self, newType: str, ID: str):
        # TODO: Implement changeServiceType method
        pass

    def addService(self, ID: str, type: str, price: str):
        # TODO: Implement addService method
        pass

    def removeService(self, ID: str):
        # TODO: Implement removeService method
        pass

    def changeServicePrice(self, newPrice: str, ID: str):
        # TODO: Implement changeServicePrice method
        pass

class newClasses_ServiceType:

    def __init__(self, type: str, price: str):
        self.type = type
        self.price = price
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

class ServiceType:

    pass
class RoomHandlerInterface:

    pass
class ManagerInterface:

    pass
class newClasses_LoginChecker(ManagerInterface):

    pass
class newClasses_RoomType:

    def __init__(self, type: str, price: str):
        self.type = type
        self.price = price
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

class newClasses_GuestInterface(ABC):

    def __init__(self):
        
    def changeRoom(self, guest: str, roomNum: str, newRoomType: str):
        # TODO: Implement changeRoom method
        pass

    def checkIn(self, checkInDate: str, conformationNum: str) -> str:
        # TODO: Implement checkIn method
        pass

    def extendStay(self, roomNum: str, guest: str, newCheckOutDate: str):
        # TODO: Implement extendStay method
        pass

class newClasses_Service(ServiceType):

    def __init__(self, id: str, status: str, newClasses_Service: "newClasses_ServiceHandler" = None):
        self.id = id
        self.status = status
        self.newClasses_Service = newClasses_Service
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def newClasses_Service(self):
        return self.__newClasses_Service

    @newClasses_Service.setter
    def newClasses_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Service__newClasses_Service", None)
        self.__newClasses_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_ServiceHandler"):
                opp_val = getattr(old_value, "newClasses_ServiceHandler", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_ServiceHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_ServiceHandler"):
                opp_val = getattr(value, "newClasses_ServiceHandler", None)
                setattr(value, "newClasses_ServiceHandler", self)

class ServiceHandlerInterface:

    pass
class newClasses_Manager(ServiceHandlerInterface, ManagerInterface, RoomHandlerInterface):

    def __init__(self, userName: str, password: str, newClasses_Manager: "newClasses_RoomHandler" = None, newClasses_Manager10: "newClasses_ServiceHandler" = None, newClasses_Manager18: "newClasses_LoginChecker" = None):
        self.userName = userName
        self.password = password
        self.newClasses_Manager = newClasses_Manager
        self.newClasses_Manager10 = newClasses_Manager10
        self.newClasses_Manager18 = newClasses_Manager18
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def newClasses_Manager18(self):
        return self.__newClasses_Manager18

    @newClasses_Manager18.setter
    def newClasses_Manager18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Manager__newClasses_Manager18", None)
        self.__newClasses_Manager18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_LoginChecker"):
                opp_val = getattr(old_value, "newClasses_LoginChecker", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_LoginChecker", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_LoginChecker"):
                opp_val = getattr(value, "newClasses_LoginChecker", None)
                setattr(value, "newClasses_LoginChecker", self)

    @property
    def newClasses_Manager(self):
        return self.__newClasses_Manager

    @newClasses_Manager.setter
    def newClasses_Manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Manager__newClasses_Manager", None)
        self.__newClasses_Manager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_RoomHandler"):
                opp_val = getattr(old_value, "newClasses_RoomHandler", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_RoomHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_RoomHandler"):
                opp_val = getattr(value, "newClasses_RoomHandler", None)
                setattr(value, "newClasses_RoomHandler", self)

    @property
    def newClasses_Manager10(self):
        return self.__newClasses_Manager10

    @newClasses_Manager10.setter
    def newClasses_Manager10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Manager__newClasses_Manager10", None)
        self.__newClasses_Manager10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_ServiceHandler11"):
                opp_val = getattr(old_value, "newClasses_ServiceHandler11", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_ServiceHandler11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_ServiceHandler11"):
                opp_val = getattr(value, "newClasses_ServiceHandler11", None)
                setattr(value, "newClasses_ServiceHandler11", self)

class RoomType:

    pass
class newClasses_Room(RoomType):

    def __init__(self, roomNum: str, status: str, newClasses_Room: "newClasses_RoomHandler" = None):
        self.roomNum = roomNum
        self.status = status
        self.newClasses_Room = newClasses_Room
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def roomNum(self) -> str:
        return self.__roomNum

    @roomNum.setter
    def roomNum(self, roomNum: str):
        self.__roomNum = roomNum

    @property
    def newClasses_Room(self):
        return self.__newClasses_Room

    @newClasses_Room.setter
    def newClasses_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Room__newClasses_Room", None)
        self.__newClasses_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_RoomHandler13"):
                opp_val = getattr(old_value, "newClasses_RoomHandler13", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_RoomHandler13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_RoomHandler13"):
                opp_val = getattr(value, "newClasses_RoomHandler13", None)
                setattr(value, "newClasses_RoomHandler13", self)

class newClasses_GuestBiller(ABC):

    def __init__(self):
        
    def checkOut(self, lastName: str, year: str, cost: str, creditCardNum: str, cvc: str, roomNum: str, firstName: str, checkOutDate: str, month: str) -> str:
        # TODO: Implement checkOut method
        pass

    def addServiceToBill(self, type: str, guest: str) -> str:
        # TODO: Implement addServiceToBill method
        pass

class GuestInterface:

    pass
class GuestBiller:

    pass
class Customer:

    pass
class newClasses_Guest(Customer, GuestBiller, GuestInterface):

    def __init__(self, checkInDate: str, checkOutDate: str, roomNum: str, checkedIn: str, checkedOut: str, addedServices: str, extraDays: str, cost: str, bookingPaid: str):
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.roomNum = roomNum
        self.checkedIn = checkedIn
        self.checkedOut = checkedOut
        self.addedServices = addedServices
        self.extraDays = extraDays
        self.cost = cost
        self.bookingPaid = bookingPaid
        
    @property
    def extraDays(self) -> str:
        return self.__extraDays

    @extraDays.setter
    def extraDays(self, extraDays: str):
        self.__extraDays = extraDays

    @property
    def addedServices(self) -> str:
        return self.__addedServices

    @addedServices.setter
    def addedServices(self, addedServices: str):
        self.__addedServices = addedServices

    @property
    def checkedOut(self) -> str:
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: str):
        self.__checkedOut = checkedOut

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def checkInDate(self) -> str:
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate

    @property
    def roomNum(self) -> str:
        return self.__roomNum

    @roomNum.setter
    def roomNum(self, roomNum: str):
        self.__roomNum = roomNum

    @property
    def checkedIn(self) -> str:
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: str):
        self.__checkedIn = checkedIn

    @property
    def checkOutDate(self) -> str:
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate

    @property
    def bookingPaid(self) -> str:
        return self.__bookingPaid

    @bookingPaid.setter
    def bookingPaid(self, bookingPaid: str):
        self.__bookingPaid = bookingPaid

class newClasses_CustomerProvides(ABC):

    def __init__(self):
        
    def isCreditCardValid(self, ccNumber: str, ccv: str, expiryYear: int, lastName: str, firstName: str, expiryMonth: int) -> bool:
        # TODO: Implement isCreditCardValid method
        pass

    def makePayment(self, expiryYear: int, lastName: str, sum: float, firstName: str, ccv: str, expiryMonth: int, ccNumber: str) -> bool:
        # TODO: Implement makePayment method
        pass

class newClasses_Validator(ABC):

    def __init__(self):
        
    def validatePersonalNum(self, personalNum: str) -> str:
        # TODO: Implement validatePersonalNum method
        pass

    def checkDateOrder(self, checkOutDate: str, checkInDate: str) -> str:
        # TODO: Implement checkDateOrder method
        pass

    def validateEmail(self, email: str) -> str:
        # TODO: Implement validateEmail method
        pass

    def validatePhoneNum(self, phoneNum: str) -> str:
        # TODO: Implement validatePhoneNum method
        pass

    def validateDates(self, checkInDate: str, checkOutDate: str) -> str:
        # TODO: Implement validateDates method
        pass

    def checkAgeRestriction(self, personalNum: str) -> str:
        # TODO: Implement checkAgeRestriction method
        pass

    def validateNames(self, firstName: str, lastName: str) -> str:
        # TODO: Implement validateNames method
        pass

    def validateAddress(self, city: str, country: str, zipCode: str, address: str) -> str:
        # TODO: Implement validateAddress method
        pass

    def validateConfirmationNum(self, conformationNum: str) -> str:
        # TODO: Implement validateConfirmationNum method
        pass

    def checkAge(self, day: str, month: str, year: str) -> str:
        # TODO: Implement checkAge method
        pass

class newClasses_Booker(ABC):

    def __init__(self):
        
    def createBooking(self, services: str, roomType: str, checkOutDate: str, checkInDate: str) -> str:
        # TODO: Implement createBooking method
        pass

    def generateConfirmNum(self) -> str:
        # TODO: Implement generateConfirmNum method
        pass

    def reBook(self, serviceType: str, comformationNum: str, roomType: str, checkInDate: str, checkOutDate: str):
        # TODO: Implement reBook method
        pass

    def cancelBooking(self, conformationNum: str):
        # TODO: Implement cancelBooking method
        pass

class newClasses_ServiceProvider(ABC):

    def __init__(self):
        
    def checkAvalibility(self, service: str, checkInDate: str, checkOutDate: str) -> str:
        # TODO: Implement checkAvalibility method
        pass

    def setAvalibility(self, status: str, service: str):
        # TODO: Implement setAvalibility method
        pass

class newClasses_Biller(ABC):

    def __init__(self):
        
    def calculateBill(self, extraDays: str, addedServices: str, bookingCost: str, isPaid: str) -> str:
        # TODO: Implement calculateBill method
        pass

    def calculateCost(self, checkInDate: str, checkOutDate: str, roomType: str, services: str) -> str:
        # TODO: Implement calculateCost method
        pass

    def pay(self, creditCardNum: str, cvc: str, addedServices: str, bookingCost: str, extraDays: str, month: str, lastName: str, firstName: str, year: str, isPaid: str) -> str:
        # TODO: Implement pay method
        pass

class newClasses_DB_interface(ABC):

    def __init__(self):
        
    def registerCustomerPayment(self, customer: str, bookingCost: str):
        # TODO: Implement registerCustomerPayment method
        pass

    def storeCustomer(self, customer: str):
        # TODO: Implement storeCustomer method
        pass

    def storeGuest(self, guest: str):
        # TODO: Implement storeGuest method
        pass

    def connect(self):
        # TODO: Implement connect method
        pass

    def registerGuestPayment(self, guest: str, totalBillCost: str):
        # TODO: Implement registerGuestPayment method
        pass

    def storeBooking(self, booking: str):
        # TODO: Implement storeBooking method
        pass

class DB_interface:

    pass
class newClasses_Receipt(ABC):

    def __init__(self):
        
    def createCustomerReceipt(self, bookingCost: str, booking: str, customer: str):
        # TODO: Implement createCustomerReceipt method
        pass

    def createGuestReceipt(self, totalBillCost: str, guest: str, booking: str):
        # TODO: Implement createGuestReceipt method
        pass

class newClasses_RoomProvider(ABC):

    def __init__(self):
        
    def setAvalibility(self, roomType: str, checkInDate: str, status: str, checkOutDate: str):
        # TODO: Implement setAvalibility method
        pass

    def checkAvalibility(self, roomType: str, checkInDate: str, checkOutDate: str) -> str:
        # TODO: Implement checkAvalibility method
        pass

    def dateChecker(self, DBcheckIn: str, checkOutDate: str, checkInDate: str, DBcheckOut: str) -> str:
        # TODO: Implement dateChecker method
        pass

class CustomerProvides:

    pass
class newClasses_BankComponent(CustomerProvides, AdministratorProvides):

    pass
class Validator:

    pass
class newClasses_InformationValidator(Validator):

    pass
class ServiceProvider:

    pass
class newClasses_ServiceHandler(ServiceHandlerInterface, ServiceProvider):

    pass
class Biller:

    pass
class newClasses_Billing(Biller, GuestBiller, CustomerProvides):

    def __init__(self, totalCost: str, isPaid: str):
        self.totalCost = totalCost
        self.isPaid = isPaid
        
    @property
    def totalCost(self) -> str:
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, totalCost: str):
        self.__totalCost = totalCost

    @property
    def isPaid(self) -> str:
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid

class RoomProvider:

    pass
class newClasses_RoomHandler(RoomProvider, GuestInterface, RoomHandlerInterface):

    pass
class newClasses_CreditCard:

    def __init__(self, creditCardNumber: str, month: str, year: str, firstName: str, lastName: str, cvc: str, newClasses_CreditCard: "newClasses_Customer" = None):
        self.creditCardNumber = creditCardNumber
        self.month = month
        self.year = year
        self.firstName = firstName
        self.lastName = lastName
        self.cvc = cvc
        self.newClasses_CreditCard = newClasses_CreditCard
        
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

    @property
    def cvc(self) -> str:
        return self.__cvc

    @cvc.setter
    def cvc(self, cvc: str):
        self.__cvc = cvc

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def creditCardNumber(self) -> str:
        return self.__creditCardNumber

    @creditCardNumber.setter
    def creditCardNumber(self, creditCardNumber: str):
        self.__creditCardNumber = creditCardNumber

    @property
    def newClasses_CreditCard(self):
        return self.__newClasses_CreditCard

    @newClasses_CreditCard.setter
    def newClasses_CreditCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_CreditCard__newClasses_CreditCard", None)
        self.__newClasses_CreditCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_Customer2"):
                opp_val = getattr(old_value, "newClasses_Customer2", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_Customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_Customer2"):
                opp_val = getattr(value, "newClasses_Customer2", None)
                setattr(value, "newClasses_Customer2", self)

class Receipt:

    pass
class newClasses_ReceiptCreator(Receipt):

    pass
class newClasses_Database(DB_interface):

    pass
class Booker:

    pass
class newClasses_Booking(Validator, Booker, ServiceProvider, CustomerProvides, Biller, RoomProvider):

    def __init__(self, roomType: str, services: str, isPaid: str, checkInDate: str, checkOutDate: str, conformationNum: str, cost: str, newClasses_Booking: "newClasses_Customer" = None, newClasses_Booking6: "newClasses_Database" = None, newClasses_Booking4: "newClasses_ReceiptCreator" = None):
        self.roomType = roomType
        self.services = services
        self.isPaid = isPaid
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.conformationNum = conformationNum
        self.cost = cost
        self.newClasses_Booking = newClasses_Booking
        self.newClasses_Booking6 = newClasses_Booking6
        self.newClasses_Booking4 = newClasses_Booking4
        
    @property
    def isPaid(self) -> str:
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid

    @property
    def checkInDate(self) -> str:
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate

    @property
    def roomType(self) -> str:
        return self.__roomType

    @roomType.setter
    def roomType(self, roomType: str):
        self.__roomType = roomType

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def checkOutDate(self) -> str:
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate

    @property
    def services(self) -> str:
        return self.__services

    @services.setter
    def services(self, services: str):
        self.__services = services

    @property
    def conformationNum(self) -> str:
        return self.__conformationNum

    @conformationNum.setter
    def conformationNum(self, conformationNum: str):
        self.__conformationNum = conformationNum

    @property
    def newClasses_Booking4(self):
        return self.__newClasses_Booking4

    @newClasses_Booking4.setter
    def newClasses_Booking4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Booking__newClasses_Booking4", None)
        self.__newClasses_Booking4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_ReceiptCreator"):
                opp_val = getattr(old_value, "newClasses_ReceiptCreator", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_ReceiptCreator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_ReceiptCreator"):
                opp_val = getattr(value, "newClasses_ReceiptCreator", None)
                setattr(value, "newClasses_ReceiptCreator", self)

    @property
    def newClasses_Booking(self):
        return self.__newClasses_Booking

    @newClasses_Booking.setter
    def newClasses_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Booking__newClasses_Booking", None)
        self.__newClasses_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_Customer"):
                opp_val = getattr(old_value, "newClasses_Customer", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_Customer"):
                opp_val = getattr(value, "newClasses_Customer", None)
                setattr(value, "newClasses_Customer", self)

    @property
    def newClasses_Booking6(self):
        return self.__newClasses_Booking6

    @newClasses_Booking6.setter
    def newClasses_Booking6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Booking__newClasses_Booking6", None)
        self.__newClasses_Booking6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_Database"):
                opp_val = getattr(old_value, "newClasses_Database", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_Database"):
                opp_val = getattr(value, "newClasses_Database", None)
                setattr(value, "newClasses_Database", self)

class newClasses_Customer(Booker):

    def __init__(self, zipCode: str, city: str, country: str, phoneNum: str, email: str, firstName: str, lastName: str, personalNum: str, address: str, bookingNum: str, bookingCost: str, newClasses_Customer: "newClasses_Booking" = None, newClasses_Customer2: "newClasses_CreditCard" = None):
        self.zipCode = zipCode
        self.city = city
        self.country = country
        self.phoneNum = phoneNum
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.personalNum = personalNum
        self.address = address
        self.bookingNum = bookingNum
        self.bookingCost = bookingCost
        self.newClasses_Customer = newClasses_Customer
        self.newClasses_Customer2 = newClasses_Customer2
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def phoneNum(self) -> str:
        return self.__phoneNum

    @phoneNum.setter
    def phoneNum(self, phoneNum: str):
        self.__phoneNum = phoneNum

    @property
    def bookingCost(self) -> str:
        return self.__bookingCost

    @bookingCost.setter
    def bookingCost(self, bookingCost: str):
        self.__bookingCost = bookingCost

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def personalNum(self) -> str:
        return self.__personalNum

    @personalNum.setter
    def personalNum(self, personalNum: str):
        self.__personalNum = personalNum

    @property
    def bookingNum(self) -> str:
        return self.__bookingNum

    @bookingNum.setter
    def bookingNum(self, bookingNum: str):
        self.__bookingNum = bookingNum

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def newClasses_Customer2(self):
        return self.__newClasses_Customer2

    @newClasses_Customer2.setter
    def newClasses_Customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Customer__newClasses_Customer2", None)
        self.__newClasses_Customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_CreditCard"):
                opp_val = getattr(old_value, "newClasses_CreditCard", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_CreditCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_CreditCard"):
                opp_val = getattr(value, "newClasses_CreditCard", None)
                setattr(value, "newClasses_CreditCard", self)

    @property
    def newClasses_Customer(self):
        return self.__newClasses_Customer

    @newClasses_Customer.setter
    def newClasses_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_newClasses_Customer__newClasses_Customer", None)
        self.__newClasses_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newClasses_Booking"):
                opp_val = getattr(old_value, "newClasses_Booking", None)
                if opp_val == self:
                    setattr(old_value, "newClasses_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newClasses_Booking"):
                opp_val = getattr(value, "newClasses_Booking", None)
                setattr(value, "newClasses_Booking", self)
