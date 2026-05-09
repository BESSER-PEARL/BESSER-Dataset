from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classes_Buissnesslayer_UserHandler:

    def __init__(self, Users: str, userhandler: "Database" = None, userhandler35: "LoginController" = None):
        self.Users = Users
        self.userhandler = userhandler
        self.userhandler35 = userhandler35
        
        pass
    @property
    def Users(self):
        return self.__Users

    @Users.setter
    def Users(self, Users: str):
        self.__Users = Users


    @property
    def userhandler(self):
        return self.__userhandler

    @userhandler.setter
    def userhandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_UserHandler__userhandler", None)
        self.__userhandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database33"):
                opp_val = getattr(old_value, "Database33", None)
                if opp_val == self:
                    setattr(old_value, "Database33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database33"):
                opp_val = getattr(value, "Database33", None)
                setattr(value, "Database33", self)

    @property
    def userhandler35(self):
        return self.__userhandler35

    @userhandler35.setter
    def userhandler35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_UserHandler__userhandler35", None)
        self.__userhandler35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoginController36"):
                opp_val = getattr(old_value, "LoginController36", None)
                if opp_val == self:
                    setattr(old_value, "LoginController36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoginController36"):
                opp_val = getattr(value, "LoginController36", None)
                setattr(value, "LoginController36", self)

    def identifyUser(self, Classes_email) :
        # TODO: Implement identifyUser method
        pass

    def isEmailValid(self, Classes_email) :
        # TODO: Implement isEmailValid method
        pass

    def AddNewGuest(self, Classes_email) :
        # TODO: Implement AddNewGuest method
        pass

    def sendEmailVerification(self, Classes_email):
        # TODO: Implement sendEmailVerification method
        pass

    def CreateEmployee(self, Classes_ID) :
        # TODO: Implement CreateEmployee method
        pass

class BookingHandler:

    pass
class Address:

    pass
class LoginController:

    pass
class Classes_Buissnesslayer_BookingHandler:

    def __init__(self, Classes_Buissnesslayer_BookingHandler: "Booking" = None, Classes_Buissnesslayer_BookingHandler16: "Booking" = None, bookinghandler: set["User"] = None, Classes_Buissnesslayer_BookingHandler20: "Database" = None, Classes_Buissnesslayer_BookingHandler22: "UserHandler" = None):
        self.Classes_Buissnesslayer_BookingHandler = Classes_Buissnesslayer_BookingHandler
        self.Classes_Buissnesslayer_BookingHandler16 = Classes_Buissnesslayer_BookingHandler16
        self.bookinghandler = bookinghandler if bookinghandler is not None else set()
        self.Classes_Buissnesslayer_BookingHandler20 = Classes_Buissnesslayer_BookingHandler20
        self.Classes_Buissnesslayer_BookingHandler22 = Classes_Buissnesslayer_BookingHandler22
        
        pass
    @property
    def Classes_Buissnesslayer_BookingHandler(self):
        return self.__Classes_Buissnesslayer_BookingHandler

    @Classes_Buissnesslayer_BookingHandler.setter
    def Classes_Buissnesslayer_BookingHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler", None)
        self.__Classes_Buissnesslayer_BookingHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking14"):
                opp_val = getattr(old_value, "Booking14", None)
                if opp_val == self:
                    setattr(old_value, "Booking14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking14"):
                opp_val = getattr(value, "Booking14", None)
                setattr(value, "Booking14", self)

    @property
    def Classes_Buissnesslayer_BookingHandler20(self):
        return self.__Classes_Buissnesslayer_BookingHandler20

    @Classes_Buissnesslayer_BookingHandler20.setter
    def Classes_Buissnesslayer_BookingHandler20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler20", None)
        self.__Classes_Buissnesslayer_BookingHandler20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database"):
                opp_val = getattr(old_value, "Database", None)
                if opp_val == self:
                    setattr(old_value, "Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database"):
                opp_val = getattr(value, "Database", None)
                setattr(value, "Database", self)

    @property
    def Classes_Buissnesslayer_BookingHandler22(self):
        return self.__Classes_Buissnesslayer_BookingHandler22

    @Classes_Buissnesslayer_BookingHandler22.setter
    def Classes_Buissnesslayer_BookingHandler22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler22", None)
        self.__Classes_Buissnesslayer_BookingHandler22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler23"):
                opp_val = getattr(old_value, "UserHandler23", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler23"):
                opp_val = getattr(value, "UserHandler23", None)
                setattr(value, "UserHandler23", self)

    @property
    def bookinghandler(self):
        return self.__bookinghandler

    @bookinghandler.setter
    def bookinghandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__bookinghandler", None)
        self.__bookinghandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    if opp_val == self:
                        setattr(item, "User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    setattr(item, "User", self)
                    

    @property
    def Classes_Buissnesslayer_BookingHandler16(self):
        return self.__Classes_Buissnesslayer_BookingHandler16

    @Classes_Buissnesslayer_BookingHandler16.setter
    def Classes_Buissnesslayer_BookingHandler16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler16", None)
        self.__Classes_Buissnesslayer_BookingHandler16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking17"):
                opp_val = getattr(old_value, "Booking17", None)
                if opp_val == self:
                    setattr(old_value, "Booking17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking17"):
                opp_val = getattr(value, "Booking17", None)
                setattr(value, "Booking17", self)

    def checkOut(self, Classes_booking):
        # TODO: Implement checkOut method
        pass

    def fetchBooking(self, Classes_bookingID) :
        # TODO: Implement fetchBooking method
        pass

    def attemptBookRoom(self, Classes_booking) :
        # TODO: Implement attemptBookRoom method
        pass

    def fetchAvailableExtras(self) :
        # TODO: Implement fetchAvailableExtras method
        pass

    def cancelBooking(self, Classes_booking):
        # TODO: Implement cancelBooking method
        pass

    def CalculatePayment(self, Classes_booking) :
        # TODO: Implement CalculatePayment method
        pass

    def checkIn(self, Classes_booking):
        # TODO: Implement checkIn method
        pass

    def fetchAvailability(self, Classes_roomType, Classes_startDate, Classes_nrOfGuests, Classes_endDate) :
        # TODO: Implement fetchAvailability method
        pass

    def displayPaymentOptions(self) :
        # TODO: Implement displayPaymentOptions method
        pass

    def sendErrorMsg(self):
        # TODO: Implement sendErrorMsg method
        pass

    def changeBooking(self, Classes_booking):
        # TODO: Implement changeBooking method
        pass

class Classes_Buissnesslayer_User(ABC):

    def __init__(self, Name: str, Email: str, Classes_Buissnesslayer_User: "LoginController" = None, Classes_Buissnesslayer_User26: "UserHandler" = None, Classes_Buissnesslayer_User29: "Address" = None, User31: "BookingHandler" = None):
        self.Name = Name
        self.Email = Email
        self.Classes_Buissnesslayer_User = Classes_Buissnesslayer_User
        self.Classes_Buissnesslayer_User26 = Classes_Buissnesslayer_User26
        self.Classes_Buissnesslayer_User29 = Classes_Buissnesslayer_User29
        self.User31 = User31
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email


    @property
    def Classes_Buissnesslayer_User26(self):
        return self.__Classes_Buissnesslayer_User26

    @Classes_Buissnesslayer_User26.setter
    def Classes_Buissnesslayer_User26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__Classes_Buissnesslayer_User26", None)
        self.__Classes_Buissnesslayer_User26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler27"):
                opp_val = getattr(old_value, "UserHandler27", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler27"):
                opp_val = getattr(value, "UserHandler27", None)
                setattr(value, "UserHandler27", self)

    @property
    def User31(self):
        return self.__User31

    @User31.setter
    def User31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__User31", None)
        self.__User31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookingHandler"):
                opp_val = getattr(old_value, "BookingHandler", None)
                if opp_val == self:
                    setattr(old_value, "BookingHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookingHandler"):
                opp_val = getattr(value, "BookingHandler", None)
                setattr(value, "BookingHandler", self)

    @property
    def Classes_Buissnesslayer_User(self):
        return self.__Classes_Buissnesslayer_User

    @Classes_Buissnesslayer_User.setter
    def Classes_Buissnesslayer_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__Classes_Buissnesslayer_User", None)
        self.__Classes_Buissnesslayer_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoginController"):
                opp_val = getattr(old_value, "LoginController", None)
                if opp_val == self:
                    setattr(old_value, "LoginController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoginController"):
                opp_val = getattr(value, "LoginController", None)
                setattr(value, "LoginController", self)

    @property
    def Classes_Buissnesslayer_User29(self):
        return self.__Classes_Buissnesslayer_User29

    @Classes_Buissnesslayer_User29.setter
    def Classes_Buissnesslayer_User29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__Classes_Buissnesslayer_User29", None)
        self.__Classes_Buissnesslayer_User29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Address"):
                opp_val = getattr(old_value, "Address", None)
                if opp_val == self:
                    setattr(old_value, "Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Address"):
                opp_val = getattr(value, "Address", None)
                setattr(value, "Address", self)

    def bookRoom(self, Classes_booking) :
        # TODO: Implement bookRoom method
        pass

    def attemptCheckOut(self, Classes_booking):
        # TODO: Implement attemptCheckOut method
        pass

    def cancelBooking(self, Classes_booking):
        # TODO: Implement cancelBooking method
        pass

    def changeBooking(self, Classes_newBooking, Classes_oldBooking):
        # TODO: Implement changeBooking method
        pass

    def attemptCheckIn(self, Classes_booking):
        # TODO: Implement attemptCheckIn method
        pass

class Database:

    pass
class User:

    pass
class Classes_Datalayer_Database:

    def __init__(self, extrasDB: str, Classes_Datalayer_Database: set["Guest"] = None, database: "UserHandler" = None, Classes_Datalayer_Database3: set["Employee"] = None, Classes_Datalayer_Database5: set["Booking"] = None, Classes_Datalayer_Database7: set["Room"] = None):
        self.extrasDB = extrasDB
        self.Classes_Datalayer_Database = Classes_Datalayer_Database if Classes_Datalayer_Database is not None else set()
        self.database = database
        self.Classes_Datalayer_Database3 = Classes_Datalayer_Database3 if Classes_Datalayer_Database3 is not None else set()
        self.Classes_Datalayer_Database5 = Classes_Datalayer_Database5 if Classes_Datalayer_Database5 is not None else set()
        self.Classes_Datalayer_Database7 = Classes_Datalayer_Database7 if Classes_Datalayer_Database7 is not None else set()
        
        pass
    @property
    def extrasDB(self):
        return self.__extrasDB

    @extrasDB.setter
    def extrasDB(self, extrasDB: str):
        self.__extrasDB = extrasDB


    @property
    def Classes_Datalayer_Database(self):
        return self.__Classes_Datalayer_Database

    @Classes_Datalayer_Database.setter
    def Classes_Datalayer_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__Classes_Datalayer_Database", None)
        self.__Classes_Datalayer_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Guest"):
                    opp_val = getattr(item, "Guest", None)
                    
                    if opp_val == self:
                        setattr(item, "Guest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Guest"):
                    opp_val = getattr(item, "Guest", None)
                    
                    setattr(item, "Guest", self)
                    

    @property
    def Classes_Datalayer_Database3(self):
        return self.__Classes_Datalayer_Database3

    @Classes_Datalayer_Database3.setter
    def Classes_Datalayer_Database3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__Classes_Datalayer_Database3", None)
        self.__Classes_Datalayer_Database3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def Classes_Datalayer_Database7(self):
        return self.__Classes_Datalayer_Database7

    @Classes_Datalayer_Database7.setter
    def Classes_Datalayer_Database7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__Classes_Datalayer_Database7", None)
        self.__Classes_Datalayer_Database7 = value if value is not None else set()
        
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
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__database", None)
        self.__database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler"):
                opp_val = getattr(old_value, "UserHandler", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler"):
                opp_val = getattr(value, "UserHandler", None)
                setattr(value, "UserHandler", self)

    @property
    def Classes_Datalayer_Database5(self):
        return self.__Classes_Datalayer_Database5

    @Classes_Datalayer_Database5.setter
    def Classes_Datalayer_Database5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__Classes_Datalayer_Database5", None)
        self.__Classes_Datalayer_Database5 = value if value is not None else set()
        
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
                    

class Classes_Interactionlayer_LoginController:

    def __init__(self, logincontroller: "GUIController" = None, Classes_Interactionlayer_LoginController: "User" = None, Classes_Interactionlayer_LoginController49: "PaymentHandler" = None, logincontroller51: "UserHandler" = None):
        self.logincontroller = logincontroller
        self.Classes_Interactionlayer_LoginController = Classes_Interactionlayer_LoginController
        self.Classes_Interactionlayer_LoginController49 = Classes_Interactionlayer_LoginController49
        self.logincontroller51 = logincontroller51
        
        pass
    @property
    def logincontroller51(self):
        return self.__logincontroller51

    @logincontroller51.setter
    def logincontroller51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__logincontroller51", None)
        self.__logincontroller51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler52"):
                opp_val = getattr(old_value, "UserHandler52", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler52"):
                opp_val = getattr(value, "UserHandler52", None)
                setattr(value, "UserHandler52", self)

    @property
    def logincontroller(self):
        return self.__logincontroller

    @logincontroller.setter
    def logincontroller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__logincontroller", None)
        self.__logincontroller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUIController45"):
                opp_val = getattr(old_value, "GUIController45", None)
                if opp_val == self:
                    setattr(old_value, "GUIController45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUIController45"):
                opp_val = getattr(value, "GUIController45", None)
                setattr(value, "GUIController45", self)

    @property
    def Classes_Interactionlayer_LoginController49(self):
        return self.__Classes_Interactionlayer_LoginController49

    @Classes_Interactionlayer_LoginController49.setter
    def Classes_Interactionlayer_LoginController49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__Classes_Interactionlayer_LoginController49", None)
        self.__Classes_Interactionlayer_LoginController49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PaymentHandler"):
                opp_val = getattr(old_value, "PaymentHandler", None)
                if opp_val == self:
                    setattr(old_value, "PaymentHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PaymentHandler"):
                opp_val = getattr(value, "PaymentHandler", None)
                setattr(value, "PaymentHandler", self)

    @property
    def Classes_Interactionlayer_LoginController(self):
        return self.__Classes_Interactionlayer_LoginController

    @Classes_Interactionlayer_LoginController.setter
    def Classes_Interactionlayer_LoginController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__Classes_Interactionlayer_LoginController", None)
        self.__Classes_Interactionlayer_LoginController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User47"):
                opp_val = getattr(old_value, "User47", None)
                if opp_val == self:
                    setattr(old_value, "User47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User47"):
                opp_val = getattr(value, "User47", None)
                setattr(value, "User47", self)

    def loginEmployee(self, Classes_ID) :
        # TODO: Implement loginEmployee method
        pass

    def loginGuest(self, Classes_bookingID) :
        # TODO: Implement loginGuest method
        pass

    def loginCreateGuest(self, Classes_email) :
        # TODO: Implement loginCreateGuest method
        pass

class Classes_BuisnessLogicLayer_PaymentHandler:

    def __init__(self):
        
        pass
    def makePayment(self, Classes_booking, Classes_paymentInfo):
        # TODO: Implement makePayment method
        pass

class Classes_BuisnessLogicLayer_PaymentInfo:

    def __init__(self, PaymentComplete: bool, CreditCard: int, CVV: int, ExpiryDate: int, Classes_BuisnessLogicLayer_PaymentInfo: "PaymentHandler" = None):
        self.PaymentComplete = PaymentComplete
        self.CreditCard = CreditCard
        self.CVV = CVV
        self.ExpiryDate = ExpiryDate
        self.Classes_BuisnessLogicLayer_PaymentInfo = Classes_BuisnessLogicLayer_PaymentInfo
        
        pass
    @property
    def CreditCard(self):
        return self.__CreditCard

    @CreditCard.setter
    def CreditCard(self, CreditCard: int):
        self.__CreditCard = CreditCard


    @property
    def ExpiryDate(self):
        return self.__ExpiryDate

    @ExpiryDate.setter
    def ExpiryDate(self, ExpiryDate: int):
        self.__ExpiryDate = ExpiryDate


    @property
    def PaymentComplete(self):
        return self.__PaymentComplete

    @PaymentComplete.setter
    def PaymentComplete(self, PaymentComplete: bool):
        self.__PaymentComplete = PaymentComplete


    @property
    def CVV(self):
        return self.__CVV

    @CVV.setter
    def CVV(self, CVV: int):
        self.__CVV = CVV


    @property
    def Classes_BuisnessLogicLayer_PaymentInfo(self):
        return self.__Classes_BuisnessLogicLayer_PaymentInfo

    @Classes_BuisnessLogicLayer_PaymentInfo.setter
    def Classes_BuisnessLogicLayer_PaymentInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_BuisnessLogicLayer_PaymentInfo__Classes_BuisnessLogicLayer_PaymentInfo", None)
        self.__Classes_BuisnessLogicLayer_PaymentInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PaymentHandler54"):
                opp_val = getattr(old_value, "PaymentHandler54", None)
                if opp_val == self:
                    setattr(old_value, "PaymentHandler54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PaymentHandler54"):
                opp_val = getattr(value, "PaymentHandler54", None)
                setattr(value, "PaymentHandler54", self)

class Classes_Interactionlayer_LoginController_DataType1:

    pass
class PaymentHandler:

    pass
class Classes_Buissnesslayer_Employee(User):

    def __init__(self, ID: int, Password: str, User47: "Classes_Interactionlayer_LoginController" = None, User: "Classes_Buissnesslayer_BookingHandler" = None):
        self.ID = ID
        self.Password = Password
        
        pass
    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID


class GUI:

    pass
class Classes_Interactionlayer_GUIController:

    def __init__(self, Classes_Interactionlayer_GUIController: "GUI" = None, guicontroller: "LoginController" = None, Classes_Interactionlayer_GUIController42: "BookingHandler" = None):
        self.Classes_Interactionlayer_GUIController = Classes_Interactionlayer_GUIController
        self.guicontroller = guicontroller
        self.Classes_Interactionlayer_GUIController42 = Classes_Interactionlayer_GUIController42
        
        pass
    @property
    def Classes_Interactionlayer_GUIController(self):
        return self.__Classes_Interactionlayer_GUIController

    @Classes_Interactionlayer_GUIController.setter
    def Classes_Interactionlayer_GUIController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_GUIController__Classes_Interactionlayer_GUIController", None)
        self.__Classes_Interactionlayer_GUIController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI"):
                opp_val = getattr(old_value, "GUI", None)
                if opp_val == self:
                    setattr(old_value, "GUI", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI"):
                opp_val = getattr(value, "GUI", None)
                setattr(value, "GUI", self)

    @property
    def guicontroller(self):
        return self.__guicontroller

    @guicontroller.setter
    def guicontroller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_GUIController__guicontroller", None)
        self.__guicontroller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoginController40"):
                opp_val = getattr(old_value, "LoginController40", None)
                if opp_val == self:
                    setattr(old_value, "LoginController40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoginController40"):
                opp_val = getattr(value, "LoginController40", None)
                setattr(value, "LoginController40", self)

    @property
    def Classes_Interactionlayer_GUIController42(self):
        return self.__Classes_Interactionlayer_GUIController42

    @Classes_Interactionlayer_GUIController42.setter
    def Classes_Interactionlayer_GUIController42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_GUIController__Classes_Interactionlayer_GUIController42", None)
        self.__Classes_Interactionlayer_GUIController42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookingHandler43"):
                opp_val = getattr(old_value, "BookingHandler43", None)
                if opp_val == self:
                    setattr(old_value, "BookingHandler43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookingHandler43"):
                opp_val = getattr(value, "BookingHandler43", None)
                setattr(value, "BookingHandler43", self)

    def displayRoomsByID(self, Classes_bookingID):
        # TODO: Implement displayRoomsByID method
        pass

    def displayPaymentOption(self):
        # TODO: Implement displayPaymentOption method
        pass

    def displayExtras(self, Classes_extras):
        # TODO: Implement displayExtras method
        pass

    def displayRoomTypes(self) :
        # TODO: Implement displayRoomTypes method
        pass

    def displayRoomsGrid(self, Classes_roomType):
        # TODO: Implement displayRoomsGrid method
        pass

    def displayBookingCancelled(self):
        # TODO: Implement displayBookingCancelled method
        pass

    def showAvailableRooms(self, Classes_roomType, Classes_nrOfGuests, Classes_endDate, Classes_startDate) :
        # TODO: Implement showAvailableRooms method
        pass

    def displayBookingsByIDintbookingID(self, Classes_bookingID):
        # TODO: Implement displayBookingsByIDintbookingID method
        pass

    def displayParkings(self, Classes_parkings):
        # TODO: Implement displayParkings method
        pass

    def displayDateOptions(self):
        # TODO: Implement displayDateOptions method
        pass

    def displayError(self):
        # TODO: Implement displayError method
        pass

class GUIController:

    pass
class Classes_Interactionlayer_GUI:

    pass
class Classes_Buissnesslayer_Guest(User):

    def __init__(self, wrokAround: int, User47: "Classes_Interactionlayer_LoginController" = None, User: "Classes_Buissnesslayer_BookingHandler" = None):
        self.wrokAround = wrokAround
        
        pass
    @property
    def wrokAround(self):
        return self.__wrokAround

    @wrokAround.setter
    def wrokAround(self, wrokAround: int):
        self.__wrokAround = wrokAround


class Classes_Buissnesslayer_Address:

    def __init__(self, street: str, postalNumber: int, city: str, country: str):
        self.street = street
        self.postalNumber = postalNumber
        self.city = city
        self.country = country
        
        pass
    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street


    @property
    def postalNumber(self):
        return self.__postalNumber

    @postalNumber.setter
    def postalNumber(self, postalNumber: int):
        self.__postalNumber = postalNumber


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city


class Classes_Buissnesslayer_Booking:

    def __init__(self, bookingID: int, guest: int, nrOfGuests: int, startDate: str, endDate: str, extras: str, parkings: str, checkedIn: bool, checkedOut: bool, payment: str, paymentComplete: bool, Classes_Buissnesslayer_Booking: set["Room"] = None, Classes_Buissnesslayer_Booking11: set["Room"] = None):
        self.bookingID = bookingID
        self.guest = guest
        self.nrOfGuests = nrOfGuests
        self.startDate = startDate
        self.endDate = endDate
        self.extras = extras
        self.parkings = parkings
        self.checkedIn = checkedIn
        self.checkedOut = checkedOut
        self.payment = payment
        self.paymentComplete = paymentComplete
        self.Classes_Buissnesslayer_Booking = Classes_Buissnesslayer_Booking if Classes_Buissnesslayer_Booking is not None else set()
        self.Classes_Buissnesslayer_Booking11 = Classes_Buissnesslayer_Booking11 if Classes_Buissnesslayer_Booking11 is not None else set()
        
        pass
    @property
    def parkings(self):
        return self.__parkings

    @parkings.setter
    def parkings(self, parkings: str):
        self.__parkings = parkings


    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, guest: int):
        self.__guest = guest


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate


    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate


    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, payment: str):
        self.__payment = payment


    @property
    def checkedIn(self):
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn


    @property
    def bookingID(self):
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: int):
        self.__bookingID = bookingID


    @property
    def nrOfGuests(self):
        return self.__nrOfGuests

    @nrOfGuests.setter
    def nrOfGuests(self, nrOfGuests: int):
        self.__nrOfGuests = nrOfGuests


    @property
    def paymentComplete(self):
        return self.__paymentComplete

    @paymentComplete.setter
    def paymentComplete(self, paymentComplete: bool):
        self.__paymentComplete = paymentComplete


    @property
    def checkedOut(self):
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: bool):
        self.__checkedOut = checkedOut


    @property
    def extras(self):
        return self.__extras

    @extras.setter
    def extras(self, extras: str):
        self.__extras = extras


    @property
    def Classes_Buissnesslayer_Booking11(self):
        return self.__Classes_Buissnesslayer_Booking11

    @Classes_Buissnesslayer_Booking11.setter
    def Classes_Buissnesslayer_Booking11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_Booking__Classes_Buissnesslayer_Booking11", None)
        self.__Classes_Buissnesslayer_Booking11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room12"):
                    opp_val = getattr(item, "Room12", None)
                    
                    if opp_val == self:
                        setattr(item, "Room12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room12"):
                    opp_val = getattr(item, "Room12", None)
                    
                    setattr(item, "Room12", self)
                    

    @property
    def Classes_Buissnesslayer_Booking(self):
        return self.__Classes_Buissnesslayer_Booking

    @Classes_Buissnesslayer_Booking.setter
    def Classes_Buissnesslayer_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_Booking__Classes_Buissnesslayer_Booking", None)
        self.__Classes_Buissnesslayer_Booking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room9"):
                    opp_val = getattr(item, "Room9", None)
                    
                    if opp_val == self:
                        setattr(item, "Room9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room9"):
                    opp_val = getattr(item, "Room9", None)
                    
                    setattr(item, "Room9", self)
                    

class Classes_Buissnesslayer_Room:

    def __init__(self, roomType: int):
        self.roomType = roomType
        
        pass
    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, roomType: int):
        self.__roomType = roomType


class Room:

    pass
class Booking:

    pass
class Employee:

    pass
class UserHandler:

    pass
class Guest:

    pass