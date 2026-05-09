from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class newClasses_ManagerInterface(ABC):

    def __init__(self):
        
        pass
    def validateLogin(self, newClasses_userName, newClasses_password) :
        # TODO: Implement validateLogin method
        pass

    def SessionData(self):
        # TODO: Implement SessionData method
        pass

    def login(self, newClasses_password, newClasses_userName):
        # TODO: Implement login method
        pass

    def logout(self):
        # TODO: Implement logout method
        pass

class newClasses_AdministratorProvides(ABC):

    def __init__(self):
        
        pass
    def getBalance(self, newClasses_expiryMonth, newClasses_expiryYear, newClasses_ccNumber, newClasses_lastName, newClasses_ccv, newClasses_firstName) :
        # TODO: Implement getBalance method
        pass

    def removeCreditCard(self, newClasses_firstName, newClasses_ccv, newClasses_ccNumber, newClasses_lastName, newClasses_expiryMonth, newClasses_expiryYear) :
        # TODO: Implement removeCreditCard method
        pass

    def makeDeposit(self, newClasses_ccNumber, newClasses_sum, newClasses_firstName, newClasses_ccv, newClasses_expiryMonth, newClasses_lastName, newClasses_expiryYear) :
        # TODO: Implement makeDeposit method
        pass

    def addCreditCard(self, newClasses_firstName, newClasses_lastName, newClasses_expiryMonth, newClasses_ccv, newClasses_expiryYear, newClasses_ccNumber) :
        # TODO: Implement addCreditCard method
        pass

class AdministratorProvides:

    pass
class newClasses_ServiceHandlerInterface(ABC):

    def __init__(self):
        
        pass
    def removeService(self, newClasses_ID):
        # TODO: Implement removeService method
        pass

    def addService(self, newClasses_price, newClasses_type, newClasses_ID):
        # TODO: Implement addService method
        pass

    def changeServicePrice(self, newClasses_newPrice, newClasses_ID):
        # TODO: Implement changeServicePrice method
        pass

    def changeServiceType(self, newClasses_newType, newClasses_ID):
        # TODO: Implement changeServiceType method
        pass

class newClasses_ServiceType:

    def __init__(self, type: str, price: str):
        self.type = type
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class ServiceType:

    pass
class newClasses_Service(ServiceType):

    def __init__(self, id: str, status: str, newClasses_Service: "newClasses_ServiceHandler" = None):
        self.id = id
        self.status = status
        self.newClasses_Service = newClasses_Service
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def id(self):
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

class newClasses_RoomHandlerInterface(ABC):

    def __init__(self):
        
        pass
    def addRoom(self, newClasses_price, newClasses_roomType, newClasses_roomNum):
        # TODO: Implement addRoom method
        pass

    def changeRoomType(self, newClasses_roomType, newClasses_roomNum):
        # TODO: Implement changeRoomType method
        pass

    def changeRoomPrice(self, newClasses_newPrice, newClasses_roomNum):
        # TODO: Implement changeRoomPrice method
        pass

    def removeRoom(self, newClasses_roomNum):
        # TODO: Implement removeRoom method
        pass

class RoomHandlerInterface:

    pass
class ManagerInterface:

    pass
class newClasses_LoginChecker(ManagerInterface):

    pass
class newClasses_GuestBiller(ABC):

    def __init__(self):
        
        pass
    def checkOut(self, newClasses_cvc, newClasses_lastName, newClasses_year, newClasses_month, newClasses_checkOutDate, newClasses_creditCardNum, newClasses_cost, newClasses_roomNum, newClasses_firstName) :
        # TODO: Implement checkOut method
        pass

    def addServiceToBill(self, newClasses_type, newClasses_guest) :
        # TODO: Implement addServiceToBill method
        pass

class ServiceHandlerInterface:

    pass
class newClasses_Manager(RoomHandlerInterface, ServiceHandlerInterface, ManagerInterface):

    def __init__(self, userName: str, password: str, newClasses_Manager: "newClasses_RoomHandler" = None, newClasses_Manager10: "newClasses_ServiceHandler" = None, newClasses_Manager18: "newClasses_LoginChecker" = None):
        self.userName = userName
        self.password = password
        self.newClasses_Manager = newClasses_Manager
        self.newClasses_Manager10 = newClasses_Manager10
        self.newClasses_Manager18 = newClasses_Manager18
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def userName(self):
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
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def roomNum(self):
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

class newClasses_RoomType:

    def __init__(self, type: str, price: str):
        self.type = type
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class newClasses_GuestInterface(ABC):

    def __init__(self):
        
        pass
    def checkIn(self, newClasses_conformationNum, newClasses_checkInDate) :
        # TODO: Implement checkIn method
        pass

    def changeRoom(self, newClasses_roomNum, newClasses_guest, newClasses_newRoomType):
        # TODO: Implement changeRoom method
        pass

    def extendStay(self, newClasses_roomNum, newClasses_guest, newClasses_newCheckOutDate):
        # TODO: Implement extendStay method
        pass

class newClasses_CustomerProvides(ABC):

    def __init__(self):
        
        pass
    def makePayment(self, newClasses_expiryMonth, newClasses_ccNumber, newClasses_firstName, newClasses_sum, newClasses_expiryYear, newClasses_ccv, newClasses_lastName) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, newClasses_lastName, newClasses_ccv, newClasses_ccNumber, newClasses_firstName, newClasses_expiryMonth, newClasses_expiryYear) :
        # TODO: Implement isCreditCardValid method
        pass

class GuestInterface:

    pass
class GuestBiller:

    pass
class Customer:

    pass
class newClasses_Guest(GuestInterface, Customer, GuestBiller):

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
        
        pass
    @property
    def checkOutDate(self):
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate


    @property
    def addedServices(self):
        return self.__addedServices

    @addedServices.setter
    def addedServices(self, addedServices: str):
        self.__addedServices = addedServices


    @property
    def checkedIn(self):
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: str):
        self.__checkedIn = checkedIn


    @property
    def checkedOut(self):
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: str):
        self.__checkedOut = checkedOut


    @property
    def extraDays(self):
        return self.__extraDays

    @extraDays.setter
    def extraDays(self, extraDays: str):
        self.__extraDays = extraDays


    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost


    @property
    def bookingPaid(self):
        return self.__bookingPaid

    @bookingPaid.setter
    def bookingPaid(self, bookingPaid: str):
        self.__bookingPaid = bookingPaid


    @property
    def roomNum(self):
        return self.__roomNum

    @roomNum.setter
    def roomNum(self, roomNum: str):
        self.__roomNum = roomNum


    @property
    def checkInDate(self):
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate


class newClasses_Validator(ABC):

    def __init__(self):
        
        pass
    def checkAgeRestriction(self, newClasses_personalNum) :
        # TODO: Implement checkAgeRestriction method
        pass

    def validateDates(self, newClasses_checkOutDate, newClasses_checkInDate) :
        # TODO: Implement validateDates method
        pass

    def validatePersonalNum(self, newClasses_personalNum) :
        # TODO: Implement validatePersonalNum method
        pass

    def validateEmail(self, newClasses_email) :
        # TODO: Implement validateEmail method
        pass

    def validateAddress(self, newClasses_address, newClasses_country, newClasses_city, newClasses_zipCode) :
        # TODO: Implement validateAddress method
        pass

    def checkAge(self, newClasses_day, newClasses_year, newClasses_month) :
        # TODO: Implement checkAge method
        pass

    def checkDateOrder(self, newClasses_checkOutDate, newClasses_checkInDate) :
        # TODO: Implement checkDateOrder method
        pass

    def validatePhoneNum(self, newClasses_phoneNum) :
        # TODO: Implement validatePhoneNum method
        pass

    def validateNames(self, newClasses_firstName, newClasses_lastName) :
        # TODO: Implement validateNames method
        pass

    def validateConfirmationNum(self, newClasses_conformationNum) :
        # TODO: Implement validateConfirmationNum method
        pass

class newClasses_ServiceProvider(ABC):

    def __init__(self):
        
        pass
    def setAvalibility(self, newClasses_service, newClasses_status):
        # TODO: Implement setAvalibility method
        pass

    def checkAvalibility(self, newClasses_checkInDate, newClasses_checkOutDate, newClasses_service) :
        # TODO: Implement checkAvalibility method
        pass

class newClasses_Booker(ABC):

    def __init__(self):
        
        pass
    def cancelBooking(self, newClasses_conformationNum):
        # TODO: Implement cancelBooking method
        pass

    def createBooking(self, newClasses_services, newClasses_roomType, newClasses_checkInDate, newClasses_checkOutDate) :
        # TODO: Implement createBooking method
        pass

    def reBook(self, newClasses_serviceType, newClasses_checkOutDate, newClasses_checkInDate, newClasses_roomType, newClasses_comformationNum):
        # TODO: Implement reBook method
        pass

    def generateConfirmNum(self) :
        # TODO: Implement generateConfirmNum method
        pass

class newClasses_DB_interface(ABC):

    def __init__(self):
        
        pass
    def storeCustomer(self, newClasses_customer):
        # TODO: Implement storeCustomer method
        pass

    def registerCustomerPayment(self, newClasses_customer, newClasses_bookingCost):
        # TODO: Implement registerCustomerPayment method
        pass

    def connect(self):
        # TODO: Implement connect method
        pass

    def storeBooking(self, newClasses_booking):
        # TODO: Implement storeBooking method
        pass

    def storeGuest(self, newClasses_guest):
        # TODO: Implement storeGuest method
        pass

    def registerGuestPayment(self, newClasses_guest, newClasses_totalBillCost):
        # TODO: Implement registerGuestPayment method
        pass

class DB_interface:

    pass
class newClasses_Biller(ABC):

    def __init__(self):
        
        pass
    def pay(self, newClasses_firstName, newClasses_cvc, newClasses_extraDays, newClasses_bookingCost, newClasses_isPaid, newClasses_lastName, newClasses_addedServices, newClasses_month, newClasses_creditCardNum, newClasses_year) :
        # TODO: Implement pay method
        pass

    def calculateBill(self, newClasses_addedServices, newClasses_isPaid, newClasses_bookingCost, newClasses_extraDays) :
        # TODO: Implement calculateBill method
        pass

    def calculateCost(self, newClasses_checkInDate, newClasses_roomType, newClasses_checkOutDate, newClasses_services) :
        # TODO: Implement calculateCost method
        pass

class newClasses_RoomProvider(ABC):

    def __init__(self):
        
        pass
    def checkAvalibility(self, newClasses_checkOutDate, newClasses_roomType, newClasses_checkInDate) :
        # TODO: Implement checkAvalibility method
        pass

    def setAvalibility(self, newClasses_roomType, newClasses_checkOutDate, newClasses_status, newClasses_checkInDate):
        # TODO: Implement setAvalibility method
        pass

    def dateChecker(self, newClasses_DBcheckOut, newClasses_DBcheckIn, newClasses_checkOutDate, newClasses_checkInDate) :
        # TODO: Implement dateChecker method
        pass

class CustomerProvides:

    pass
class newClasses_BankComponent(AdministratorProvides, CustomerProvides):

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
        
        pass
    @property
    def totalCost(self):
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, totalCost: str):
        self.__totalCost = totalCost


    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid


class RoomProvider:

    pass
class newClasses_RoomHandler(RoomProvider, RoomHandlerInterface, GuestInterface):

    pass
class newClasses_CreditCard:

    def __init__(self, creditCardNumber: str, cvc: str, month: str, year: str, firstName: str, lastName: str, newClasses_CreditCard: "newClasses_Customer" = None):
        self.creditCardNumber = creditCardNumber
        self.cvc = cvc
        self.month = month
        self.year = year
        self.firstName = firstName
        self.lastName = lastName
        self.newClasses_CreditCard = newClasses_CreditCard
        
        pass
    @property
    def cvc(self):
        return self.__cvc

    @cvc.setter
    def cvc(self, cvc: str):
        self.__cvc = cvc


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def creditCardNumber(self):
        return self.__creditCardNumber

    @creditCardNumber.setter
    def creditCardNumber(self, creditCardNumber: str):
        self.__creditCardNumber = creditCardNumber


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


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

class newClasses_Receipt(ABC):

    def __init__(self):
        
        pass
    def createGuestReceipt(self, newClasses_booking, newClasses_guest, newClasses_totalBillCost):
        # TODO: Implement createGuestReceipt method
        pass

    def createCustomerReceipt(self, newClasses_customer, newClasses_bookingCost, newClasses_booking):
        # TODO: Implement createCustomerReceipt method
        pass

class Receipt:

    pass
class newClasses_ReceiptCreator(Receipt):

    pass
class newClasses_Database(DB_interface):

    pass
class Booker:

    pass
class newClasses_Booking(ServiceProvider, RoomProvider, Validator, Biller, CustomerProvides, Booker):

    def __init__(self, roomType: str, services: str, isPaid: str, checkInDate: str, checkOutDate: str, conformationNum: str, cost: str, newClasses_Booking6: "newClasses_Database" = None, newClasses_Booking: "newClasses_Customer" = None, newClasses_Booking4: "newClasses_ReceiptCreator" = None):
        self.roomType = roomType
        self.services = services
        self.isPaid = isPaid
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.conformationNum = conformationNum
        self.cost = cost
        self.newClasses_Booking6 = newClasses_Booking6
        self.newClasses_Booking = newClasses_Booking
        self.newClasses_Booking4 = newClasses_Booking4
        
        pass
    @property
    def conformationNum(self):
        return self.__conformationNum

    @conformationNum.setter
    def conformationNum(self, conformationNum: str):
        self.__conformationNum = conformationNum


    @property
    def services(self):
        return self.__services

    @services.setter
    def services(self, services: str):
        self.__services = services


    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost


    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, roomType: str):
        self.__roomType = roomType


    @property
    def checkOutDate(self):
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, checkOutDate: str):
        self.__checkOutDate = checkOutDate


    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid


    @property
    def checkInDate(self):
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, checkInDate: str):
        self.__checkInDate = checkInDate


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

class newClasses_Customer(Booker):

    def __init__(self, firstName: str, lastName: str, personalNum: str, address: str, zipCode: str, city: str, country: str, phoneNum: str, email: str, bookingNum: str, bookingCost: str, newClasses_Customer: "newClasses_Booking" = None, newClasses_Customer2: "newClasses_CreditCard" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.personalNum = personalNum
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.country = country
        self.phoneNum = phoneNum
        self.email = email
        self.bookingNum = bookingNum
        self.bookingCost = bookingCost
        self.newClasses_Customer = newClasses_Customer
        self.newClasses_Customer2 = newClasses_Customer2
        
        pass
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city


    @property
    def zipCode(self):
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode


    @property
    def phoneNum(self):
        return self.__phoneNum

    @phoneNum.setter
    def phoneNum(self, phoneNum: str):
        self.__phoneNum = phoneNum


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def personalNum(self):
        return self.__personalNum

    @personalNum.setter
    def personalNum(self, personalNum: str):
        self.__personalNum = personalNum


    @property
    def bookingCost(self):
        return self.__bookingCost

    @bookingCost.setter
    def bookingCost(self, bookingCost: str):
        self.__bookingCost = bookingCost


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def bookingNum(self):
        return self.__bookingNum

    @bookingNum.setter
    def bookingNum(self, bookingNum: str):
        self.__bookingNum = bookingNum


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


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
