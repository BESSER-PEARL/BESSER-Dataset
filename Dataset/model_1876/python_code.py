from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classes_BuisnessLogicLayer_PaymentInfo:

    def __init__(self, PaymentComplete: bool, CreditCard: int, CVV: int, ExpiryDate: int, Classes_BuisnessLogicLayer_PaymentInfo: "PaymentHandler" = None):
        self.PaymentComplete = PaymentComplete
        self.CreditCard = CreditCard
        self.CVV = CVV
        self.ExpiryDate = ExpiryDate
        self.Classes_BuisnessLogicLayer_PaymentInfo = Classes_BuisnessLogicLayer_PaymentInfo
        
    @property
    def CreditCard(self) -> int:
        return self.__CreditCard

    @CreditCard.setter
    def CreditCard(self, CreditCard: int):
        self.__CreditCard = CreditCard

    @property
    def PaymentComplete(self) -> bool:
        return self.__PaymentComplete

    @PaymentComplete.setter
    def PaymentComplete(self, PaymentComplete: bool):
        self.__PaymentComplete = PaymentComplete

    @property
    def CVV(self) -> int:
        return self.__CVV

    @CVV.setter
    def CVV(self, CVV: int):
        self.__CVV = CVV

    @property
    def ExpiryDate(self) -> int:
        return self.__ExpiryDate

    @ExpiryDate.setter
    def ExpiryDate(self, ExpiryDate: int):
        self.__ExpiryDate = ExpiryDate

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
            if hasattr(old_value, "PaymentHandler56"):
                opp_val = getattr(old_value, "PaymentHandler56", None)
                if opp_val == self:
                    setattr(old_value, "PaymentHandler56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PaymentHandler56"):
                opp_val = getattr(value, "PaymentHandler56", None)
                setattr(value, "PaymentHandler56", self)

class Classes_BuisnessLogicLayer_PaymentHandler:

    def __init__(self):
        
    def makePayment(self, paymentInfo: str, booking: str):
        # TODO: Implement makePayment method
        pass

class Classes_Interactionlayer_LoginController_DataType1:

    pass
class PaymentHandler:

    pass
class Classes_Interactionlayer_LoginController:

    def __init__(self, GUIController46: "GUIController" = None, Classes_Interactionlayer_LoginController: "User" = None, Classes_Interactionlayer_LoginController51: "PaymentHandler" = None, UserHandler53: "UserHandler" = None):
        self.GUIController46 = GUIController46
        self.Classes_Interactionlayer_LoginController = Classes_Interactionlayer_LoginController
        self.Classes_Interactionlayer_LoginController51 = Classes_Interactionlayer_LoginController51
        self.UserHandler53 = UserHandler53
        
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
            if hasattr(old_value, "User49"):
                opp_val = getattr(old_value, "User49", None)
                if opp_val == self:
                    setattr(old_value, "User49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User49"):
                opp_val = getattr(value, "User49", None)
                setattr(value, "User49", self)

    @property
    def UserHandler53(self):
        return self.__UserHandler53

    @UserHandler53.setter
    def UserHandler53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__UserHandler53", None)
        self.__UserHandler53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buissnesslayer54"):
                opp_val = getattr(old_value, "Buissnesslayer54", None)
                if opp_val == self:
                    setattr(old_value, "Buissnesslayer54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buissnesslayer54"):
                opp_val = getattr(value, "Buissnesslayer54", None)
                setattr(value, "Buissnesslayer54", self)

    @property
    def GUIController46(self):
        return self.__GUIController46

    @GUIController46.setter
    def GUIController46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__GUIController46", None)
        self.__GUIController46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interactionlayer47"):
                opp_val = getattr(old_value, "Interactionlayer47", None)
                if opp_val == self:
                    setattr(old_value, "Interactionlayer47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interactionlayer47"):
                opp_val = getattr(value, "Interactionlayer47", None)
                setattr(value, "Interactionlayer47", self)

    @property
    def Classes_Interactionlayer_LoginController51(self):
        return self.__Classes_Interactionlayer_LoginController51

    @Classes_Interactionlayer_LoginController51.setter
    def Classes_Interactionlayer_LoginController51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_LoginController__Classes_Interactionlayer_LoginController51", None)
        self.__Classes_Interactionlayer_LoginController51 = value
        
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

    def loginGuest(self, bookingID: int) -> bool:
        # TODO: Implement loginGuest method
        pass

    def loginEmployee(self, ID: int) -> bool:
        # TODO: Implement loginEmployee method
        pass

    def loginCreateGuest(self, email: str) -> str:
        # TODO: Implement loginCreateGuest method
        pass

class GUI:

    pass
class Classes_Interactionlayer_GUIController:

    def __init__(self, Classes_Interactionlayer_GUIController: "GUI" = None, LoginController40: "LoginController" = None, Classes_Interactionlayer_GUIController43: "BookingHandler" = None):
        self.Classes_Interactionlayer_GUIController = Classes_Interactionlayer_GUIController
        self.LoginController40 = LoginController40
        self.Classes_Interactionlayer_GUIController43 = Classes_Interactionlayer_GUIController43
        
    @property
    def LoginController40(self):
        return self.__LoginController40

    @LoginController40.setter
    def LoginController40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_GUIController__LoginController40", None)
        self.__LoginController40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interactionlayer41"):
                opp_val = getattr(old_value, "Interactionlayer41", None)
                if opp_val == self:
                    setattr(old_value, "Interactionlayer41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interactionlayer41"):
                opp_val = getattr(value, "Interactionlayer41", None)
                setattr(value, "Interactionlayer41", self)

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
    def Classes_Interactionlayer_GUIController43(self):
        return self.__Classes_Interactionlayer_GUIController43

    @Classes_Interactionlayer_GUIController43.setter
    def Classes_Interactionlayer_GUIController43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Interactionlayer_GUIController__Classes_Interactionlayer_GUIController43", None)
        self.__Classes_Interactionlayer_GUIController43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookingHandler44"):
                opp_val = getattr(old_value, "BookingHandler44", None)
                if opp_val == self:
                    setattr(old_value, "BookingHandler44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookingHandler44"):
                opp_val = getattr(value, "BookingHandler44", None)
                setattr(value, "BookingHandler44", self)

    def displayBookingCancelled(self):
        # TODO: Implement displayBookingCancelled method
        pass

    def displayExtras(self, extras: str):
        # TODO: Implement displayExtras method
        pass

    def displayPaymentOption(self):
        # TODO: Implement displayPaymentOption method
        pass

    def displayRoomsGrid(self, roomType: int):
        # TODO: Implement displayRoomsGrid method
        pass

    def displayError(self):
        # TODO: Implement displayError method
        pass

    def displayParkings(self, parkings: int):
        # TODO: Implement displayParkings method
        pass

    def displayBookingsByIDintbookingID(self, bookingID: int):
        # TODO: Implement displayBookingsByIDintbookingID method
        pass

    def showAvailableRooms(self, endDate: str, nrOfGuests: int, startDate: str, roomType: str) -> int:
        # TODO: Implement showAvailableRooms method
        pass

    def displayDateOptions(self):
        # TODO: Implement displayDateOptions method
        pass

    def displayRoomsByID(self, bookingID: int):
        # TODO: Implement displayRoomsByID method
        pass

    def displayRoomTypes(self) -> int:
        # TODO: Implement displayRoomTypes method
        pass

class GUIController:

    pass
class Classes_Interactionlayer_GUI:

    pass
class Classes_Buissnesslayer_Address:

    def __init__(self, street: str, postalNumber: int, city: str, country: str):
        self.street = street
        self.postalNumber = postalNumber
        self.city = city
        self.country = country
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def postalNumber(self) -> int:
        return self.__postalNumber

    @postalNumber.setter
    def postalNumber(self, postalNumber: int):
        self.__postalNumber = postalNumber

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

class Classes_Buissnesslayer_UserHandler:

    def __init__(self, Users: str, Database34: "Database" = None, LoginController36: "LoginController" = None):
        self.Users = Users
        self.Database34 = Database34
        self.LoginController36 = LoginController36
        
    @property
    def Users(self) -> str:
        return self.__Users

    @Users.setter
    def Users(self, Users: str):
        self.__Users = Users

    @property
    def Database34(self):
        return self.__Database34

    @Database34.setter
    def Database34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_UserHandler__Database34", None)
        self.__Database34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Datalayer"):
                opp_val = getattr(old_value, "Datalayer", None)
                if opp_val == self:
                    setattr(old_value, "Datalayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Datalayer"):
                opp_val = getattr(value, "Datalayer", None)
                setattr(value, "Datalayer", self)

    @property
    def LoginController36(self):
        return self.__LoginController36

    @LoginController36.setter
    def LoginController36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_UserHandler__LoginController36", None)
        self.__LoginController36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interactionlayer"):
                opp_val = getattr(old_value, "Interactionlayer", None)
                if opp_val == self:
                    setattr(old_value, "Interactionlayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interactionlayer"):
                opp_val = getattr(value, "Interactionlayer", None)
                setattr(value, "Interactionlayer", self)

    def CreateEmployee(self, ID: int) -> str:
        # TODO: Implement CreateEmployee method
        pass

    def identifyUser(self, email: str) -> str:
        # TODO: Implement identifyUser method
        pass

    def sendEmailVerification(self, email: str):
        # TODO: Implement sendEmailVerification method
        pass

    def identifyUser(self, employeeID: int) -> str:
        # TODO: Implement identifyUser method
        pass

    def AddNewGuest(self, email: str) -> str:
        # TODO: Implement AddNewGuest method
        pass

    def isEmailValid(self, email: str) -> bool:
        # TODO: Implement isEmailValid method
        pass

class BookingHandler:

    pass
class Address:

    pass
class LoginController:

    pass
class Classes_Buissnesslayer_User(ABC):

    def __init__(self, Name: str, Email: str, Classes_Buissnesslayer_User: "LoginController" = None, Classes_Buissnesslayer_User27: "UserHandler" = None, Classes_Buissnesslayer_User30: "Address" = None, BookingHandler: "BookingHandler" = None):
        self.Name = Name
        self.Email = Email
        self.Classes_Buissnesslayer_User = Classes_Buissnesslayer_User
        self.Classes_Buissnesslayer_User27 = Classes_Buissnesslayer_User27
        self.Classes_Buissnesslayer_User30 = Classes_Buissnesslayer_User30
        self.BookingHandler = BookingHandler
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self) -> str:
        return self.__Email

    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

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
    def Classes_Buissnesslayer_User30(self):
        return self.__Classes_Buissnesslayer_User30

    @Classes_Buissnesslayer_User30.setter
    def Classes_Buissnesslayer_User30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__Classes_Buissnesslayer_User30", None)
        self.__Classes_Buissnesslayer_User30 = value
        
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

    @property
    def BookingHandler(self):
        return self.__BookingHandler

    @BookingHandler.setter
    def BookingHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__BookingHandler", None)
        self.__BookingHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buissnesslayer32"):
                opp_val = getattr(old_value, "Buissnesslayer32", None)
                if opp_val == self:
                    setattr(old_value, "Buissnesslayer32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buissnesslayer32"):
                opp_val = getattr(value, "Buissnesslayer32", None)
                setattr(value, "Buissnesslayer32", self)

    @property
    def Classes_Buissnesslayer_User27(self):
        return self.__Classes_Buissnesslayer_User27

    @Classes_Buissnesslayer_User27.setter
    def Classes_Buissnesslayer_User27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_User__Classes_Buissnesslayer_User27", None)
        self.__Classes_Buissnesslayer_User27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler28"):
                opp_val = getattr(old_value, "UserHandler28", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler28"):
                opp_val = getattr(value, "UserHandler28", None)
                setattr(value, "UserHandler28", self)

    def attemptCheckOut(self, booking: str):
        # TODO: Implement attemptCheckOut method
        pass

    def changeBooking(self, newBooking: str, oldBooking: str):
        # TODO: Implement changeBooking method
        pass

    def cancelBooking(self, booking: str):
        # TODO: Implement cancelBooking method
        pass

    def bookRoom(self, booking: str) -> bool:
        # TODO: Implement bookRoom method
        pass

    def attemptCheckIn(self, booking: str):
        # TODO: Implement attemptCheckIn method
        pass

class Database:

    pass
class User:

    pass
class Classes_Buissnesslayer_Employee(User):

    def __init__(self, ID: int, Password: str, User49: "Classes_Interactionlayer_LoginController", Buissnesslayer19: "Classes_Buissnesslayer_BookingHandler"):
        self.ID = ID
        self.Password = Password
        
    @property
    def Password(self) -> str:
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

class Classes_Buissnesslayer_Guest(User):

    def __init__(self, wrokAround: int, User49: "Classes_Interactionlayer_LoginController", Buissnesslayer19: "Classes_Buissnesslayer_BookingHandler"):
        self.wrokAround = wrokAround
        
    @property
    def wrokAround(self) -> int:
        return self.__wrokAround

    @wrokAround.setter
    def wrokAround(self, wrokAround: int):
        self.__wrokAround = wrokAround

class Classes_Buissnesslayer_BookingHandler:

    def __init__(self, Classes_Buissnesslayer_BookingHandler: "Booking" = None, Classes_Buissnesslayer_BookingHandler16: "Booking" = None, User: set["User"] = None, Classes_Buissnesslayer_BookingHandler21: "Database" = None, Classes_Buissnesslayer_BookingHandler23: "UserHandler" = None):
        self.Classes_Buissnesslayer_BookingHandler = Classes_Buissnesslayer_BookingHandler
        self.Classes_Buissnesslayer_BookingHandler16 = Classes_Buissnesslayer_BookingHandler16
        self.User = User if User is not None else set()
        self.Classes_Buissnesslayer_BookingHandler21 = Classes_Buissnesslayer_BookingHandler21
        self.Classes_Buissnesslayer_BookingHandler23 = Classes_Buissnesslayer_BookingHandler23
        
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

    @property
    def User(self):
        return self.__User

    @User.setter
    def User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__User", None)
        self.__User = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Buissnesslayer19"):
                    opp_val = getattr(item, "Buissnesslayer19", None)
                    
                    if opp_val == self:
                        setattr(item, "Buissnesslayer19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Buissnesslayer19"):
                    opp_val = getattr(item, "Buissnesslayer19", None)
                    
                    setattr(item, "Buissnesslayer19", self)
                    

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
    def Classes_Buissnesslayer_BookingHandler21(self):
        return self.__Classes_Buissnesslayer_BookingHandler21

    @Classes_Buissnesslayer_BookingHandler21.setter
    def Classes_Buissnesslayer_BookingHandler21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler21", None)
        self.__Classes_Buissnesslayer_BookingHandler21 = value
        
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
    def Classes_Buissnesslayer_BookingHandler23(self):
        return self.__Classes_Buissnesslayer_BookingHandler23

    @Classes_Buissnesslayer_BookingHandler23.setter
    def Classes_Buissnesslayer_BookingHandler23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Buissnesslayer_BookingHandler__Classes_Buissnesslayer_BookingHandler23", None)
        self.__Classes_Buissnesslayer_BookingHandler23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserHandler24"):
                opp_val = getattr(old_value, "UserHandler24", None)
                if opp_val == self:
                    setattr(old_value, "UserHandler24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserHandler24"):
                opp_val = getattr(value, "UserHandler24", None)
                setattr(value, "UserHandler24", self)

    def sendErrorMsg(self):
        # TODO: Implement sendErrorMsg method
        pass

    def fetchBooking(self, bookingID: int) -> str:
        # TODO: Implement fetchBooking method
        pass

    def cancelBooking(self, booking: str):
        # TODO: Implement cancelBooking method
        pass

    def attemptBookRoom(self, booking: str) -> bool:
        # TODO: Implement attemptBookRoom method
        pass

    def checkIn(self, booking: str):
        # TODO: Implement checkIn method
        pass

    def CalculatePayment(self, booking: str) -> int:
        # TODO: Implement CalculatePayment method
        pass

    def checkOut(self, booking: str):
        # TODO: Implement checkOut method
        pass

    def changeBooking(self, booking: str):
        # TODO: Implement changeBooking method
        pass

    def fetchAvailability(self, roomType: int, startDate: str, endDate: str, nrOfGuests: int) -> str:
        # TODO: Implement fetchAvailability method
        pass

    def displayPaymentOptions(self) -> str:
        # TODO: Implement displayPaymentOptions method
        pass

    def fetchAvailableExtras(self) -> str:
        # TODO: Implement fetchAvailableExtras method
        pass

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
        
    @property
    def nrOfGuests(self) -> int:
        return self.__nrOfGuests

    @nrOfGuests.setter
    def nrOfGuests(self, nrOfGuests: int):
        self.__nrOfGuests = nrOfGuests

    @property
    def parkings(self) -> str:
        return self.__parkings

    @parkings.setter
    def parkings(self, parkings: str):
        self.__parkings = parkings

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def checkedIn(self) -> bool:
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: bool):
        self.__checkedIn = checkedIn

    @property
    def bookingID(self) -> int:
        return self.__bookingID

    @bookingID.setter
    def bookingID(self, bookingID: int):
        self.__bookingID = bookingID

    @property
    def payment(self) -> str:
        return self.__payment

    @payment.setter
    def payment(self, payment: str):
        self.__payment = payment

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def guest(self) -> int:
        return self.__guest

    @guest.setter
    def guest(self, guest: int):
        self.__guest = guest

    @property
    def checkedOut(self) -> bool:
        return self.__checkedOut

    @checkedOut.setter
    def checkedOut(self, checkedOut: bool):
        self.__checkedOut = checkedOut

    @property
    def paymentComplete(self) -> bool:
        return self.__paymentComplete

    @paymentComplete.setter
    def paymentComplete(self, paymentComplete: bool):
        self.__paymentComplete = paymentComplete

    @property
    def extras(self) -> str:
        return self.__extras

    @extras.setter
    def extras(self, extras: str):
        self.__extras = extras

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
                    

class Classes_Buissnesslayer_Room:

    def __init__(self, roomType: int):
        self.roomType = roomType
        
    @property
    def roomType(self) -> int:
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
class Classes_Datalayer_Database:

    def __init__(self, extrasDB: str, Classes_Datalayer_Database: set["Guest"] = None, UserHandler: "UserHandler" = None, Classes_Datalayer_Database3: set["Employee"] = None, Classes_Datalayer_Database5: set["Booking"] = None, Classes_Datalayer_Database7: set["Room"] = None):
        self.extrasDB = extrasDB
        self.Classes_Datalayer_Database = Classes_Datalayer_Database if Classes_Datalayer_Database is not None else set()
        self.UserHandler = UserHandler
        self.Classes_Datalayer_Database3 = Classes_Datalayer_Database3 if Classes_Datalayer_Database3 is not None else set()
        self.Classes_Datalayer_Database5 = Classes_Datalayer_Database5 if Classes_Datalayer_Database5 is not None else set()
        self.Classes_Datalayer_Database7 = Classes_Datalayer_Database7 if Classes_Datalayer_Database7 is not None else set()
        
    @property
    def extrasDB(self) -> str:
        return self.__extrasDB

    @extrasDB.setter
    def extrasDB(self, extrasDB: str):
        self.__extrasDB = extrasDB

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
    def UserHandler(self):
        return self.__UserHandler

    @UserHandler.setter
    def UserHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Datalayer_Database__UserHandler", None)
        self.__UserHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buissnesslayer"):
                opp_val = getattr(old_value, "Buissnesslayer", None)
                if opp_val == self:
                    setattr(old_value, "Buissnesslayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buissnesslayer"):
                opp_val = getattr(value, "Buissnesslayer", None)
                setattr(value, "Buissnesslayer", self)

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
                    

class Guest:

    pass