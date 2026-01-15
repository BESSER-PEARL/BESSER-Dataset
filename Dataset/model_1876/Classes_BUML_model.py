####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Guest = Class(name="Guest")
Classes_Datalayer_Database = Class(name="Classes::Datalayer::Database")
UserHandler = Class(name="UserHandler")
Employee = Class(name="Employee")
Booking = Class(name="Booking")
Room = Class(name="Room")
Classes_Buissnesslayer_Room = Class(name="Classes::Buissnesslayer::Room")
Classes_Buissnesslayer_Booking = Class(name="Classes::Buissnesslayer::Booking")
Classes_Buissnesslayer_BookingHandler = Class(name="Classes::Buissnesslayer::BookingHandler")
User = Class(name="User")
Database = Class(name="Database")
Classes_Buissnesslayer_User = Class(name="Classes::Buissnesslayer::User", is_abstract=True)
LoginController = Class(name="LoginController")
Address = Class(name="Address")
BookingHandler = Class(name="BookingHandler")
Classes_Buissnesslayer_UserHandler = Class(name="Classes::Buissnesslayer::UserHandler")
Classes_Buissnesslayer_Employee = Class(name="Classes::Buissnesslayer::Employee")
Classes_Buissnesslayer_Address = Class(name="Classes::Buissnesslayer::Address")
Classes_Buissnesslayer_Guest = Class(name="Classes::Buissnesslayer::Guest")
Classes_Interactionlayer_GUI = Class(name="Classes::Interactionlayer::GUI")
GUIController = Class(name="GUIController")
Classes_Interactionlayer_GUIController = Class(name="Classes::Interactionlayer::GUIController")
GUI = Class(name="GUI")
Classes_Interactionlayer_LoginController = Class(name="Classes::Interactionlayer::LoginController")
PaymentHandler = Class(name="PaymentHandler")
Classes_Interactionlayer_LoginController_DataType1 = Class(name="Classes::Interactionlayer::LoginController::DataType1")
Classes_BuisnessLogicLayer_PaymentHandler = Class(name="Classes::BuisnessLogicLayer::PaymentHandler")
Classes_BuisnessLogicLayer_PaymentInfo = Class(name="Classes::BuisnessLogicLayer::PaymentInfo")

# Guest class attributes and methods

# Classes_Datalayer_Database class attributes and methods
Classes_Datalayer_Database_extrasDB: Property = Property(name="extrasDB", type=StringType)
Classes_Datalayer_Database.attributes={Classes_Datalayer_Database_extrasDB}

# UserHandler class attributes and methods

# Employee class attributes and methods

# Booking class attributes and methods

# Room class attributes and methods

# Classes_Buissnesslayer_Room class attributes and methods
Classes_Buissnesslayer_Room_roomType: Property = Property(name="roomType", type=IntegerType)
Classes_Buissnesslayer_Room.attributes={Classes_Buissnesslayer_Room_roomType}

# Classes_Buissnesslayer_Booking class attributes and methods
Classes_Buissnesslayer_Booking_bookingID: Property = Property(name="bookingID", type=IntegerType)
Classes_Buissnesslayer_Booking_guest: Property = Property(name="guest", type=IntegerType)
Classes_Buissnesslayer_Booking_nrOfGuests: Property = Property(name="nrOfGuests", type=IntegerType)
Classes_Buissnesslayer_Booking_startDate: Property = Property(name="startDate", type=StringType)
Classes_Buissnesslayer_Booking_endDate: Property = Property(name="endDate", type=StringType)
Classes_Buissnesslayer_Booking_extras: Property = Property(name="extras", type=StringType)
Classes_Buissnesslayer_Booking_parkings: Property = Property(name="parkings", type=StringType)
Classes_Buissnesslayer_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
Classes_Buissnesslayer_Booking_checkedOut: Property = Property(name="checkedOut", type=BooleanType)
Classes_Buissnesslayer_Booking_payment: Property = Property(name="payment", type=StringType)
Classes_Buissnesslayer_Booking_paymentComplete: Property = Property(name="paymentComplete", type=BooleanType)
Classes_Buissnesslayer_Booking.attributes={Classes_Buissnesslayer_Booking_nrOfGuests, Classes_Buissnesslayer_Booking_parkings, Classes_Buissnesslayer_Booking_endDate, Classes_Buissnesslayer_Booking_checkedIn, Classes_Buissnesslayer_Booking_bookingID, Classes_Buissnesslayer_Booking_payment, Classes_Buissnesslayer_Booking_startDate, Classes_Buissnesslayer_Booking_guest, Classes_Buissnesslayer_Booking_checkedOut, Classes_Buissnesslayer_Booking_paymentComplete, Classes_Buissnesslayer_Booking_extras}

# Classes_Buissnesslayer_BookingHandler class attributes and methods
Classes_Buissnesslayer_BookingHandler_m_fetchAvailability: Method = Method(name="fetchAvailability", parameters={Parameter(name='roomType'), Parameter(name='startDate'), Parameter(name='endDate'), Parameter(name='nrOfGuests')}, type=StringType)
Classes_Buissnesslayer_BookingHandler_m_fetchBooking: Method = Method(name="fetchBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_Buissnesslayer_BookingHandler_m_attemptBookRoom: Method = Method(name="attemptBookRoom", parameters={Parameter(name='booking')}, type=BooleanType)
Classes_Buissnesslayer_BookingHandler_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_BookingHandler_m_changeBooking: Method = Method(name="changeBooking", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_BookingHandler_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_BookingHandler_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_BookingHandler_m_sendErrorMsg: Method = Method(name="sendErrorMsg", parameters={})
Classes_Buissnesslayer_BookingHandler_m_fetchAvailableExtras: Method = Method(name="fetchAvailableExtras", parameters={}, type=StringType)
Classes_Buissnesslayer_BookingHandler_m_displayPaymentOptions: Method = Method(name="displayPaymentOptions", parameters={}, type=StringType)
Classes_Buissnesslayer_BookingHandler_m_CalculatePayment: Method = Method(name="CalculatePayment", parameters={Parameter(name='booking')}, type=IntegerType)
Classes_Buissnesslayer_BookingHandler.methods={Classes_Buissnesslayer_BookingHandler_m_sendErrorMsg, Classes_Buissnesslayer_BookingHandler_m_fetchBooking, Classes_Buissnesslayer_BookingHandler_m_cancelBooking, Classes_Buissnesslayer_BookingHandler_m_attemptBookRoom, Classes_Buissnesslayer_BookingHandler_m_checkIn, Classes_Buissnesslayer_BookingHandler_m_CalculatePayment, Classes_Buissnesslayer_BookingHandler_m_checkOut, Classes_Buissnesslayer_BookingHandler_m_changeBooking, Classes_Buissnesslayer_BookingHandler_m_fetchAvailability, Classes_Buissnesslayer_BookingHandler_m_displayPaymentOptions, Classes_Buissnesslayer_BookingHandler_m_fetchAvailableExtras}

# User class attributes and methods

# Database class attributes and methods

# Classes_Buissnesslayer_User class attributes and methods
Classes_Buissnesslayer_User_Name: Property = Property(name="Name", type=StringType)
Classes_Buissnesslayer_User_Email: Property = Property(name="Email", type=StringType)
Classes_Buissnesslayer_User_m_bookRoom: Method = Method(name="bookRoom", parameters={Parameter(name='booking')}, type=BooleanType)
Classes_Buissnesslayer_User_m_changeBooking: Method = Method(name="changeBooking", parameters={Parameter(name='newBooking'), Parameter(name='oldBooking')})
Classes_Buissnesslayer_User_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_User_m_attemptCheckIn: Method = Method(name="attemptCheckIn", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_User_m_attemptCheckOut: Method = Method(name="attemptCheckOut", parameters={Parameter(name='booking')})
Classes_Buissnesslayer_User.attributes={Classes_Buissnesslayer_User_Name, Classes_Buissnesslayer_User_Email}
Classes_Buissnesslayer_User.methods={Classes_Buissnesslayer_User_m_attemptCheckOut, Classes_Buissnesslayer_User_m_changeBooking, Classes_Buissnesslayer_User_m_cancelBooking, Classes_Buissnesslayer_User_m_bookRoom, Classes_Buissnesslayer_User_m_attemptCheckIn}

# LoginController class attributes and methods

# Address class attributes and methods

# BookingHandler class attributes and methods

# Classes_Buissnesslayer_UserHandler class attributes and methods
Classes_Buissnesslayer_UserHandler_Users: Property = Property(name="Users", type=StringType)
Classes_Buissnesslayer_UserHandler_m_CreateEmployee: Method = Method(name="CreateEmployee", parameters={Parameter(name='ID')}, type=StringType)
Classes_Buissnesslayer_UserHandler_m_sendEmailVerification: Method = Method(name="sendEmailVerification", parameters={Parameter(name='email')})
Classes_Buissnesslayer_UserHandler_m_isEmailValid: Method = Method(name="isEmailValid", parameters={Parameter(name='email')}, type=BooleanType)
Classes_Buissnesslayer_UserHandler_m_identifyUser: Method = Method(name="identifyUser", parameters={Parameter(name='employeeID')}, type=StringType)
Classes_Buissnesslayer_UserHandler_m_AddNewGuest: Method = Method(name="AddNewGuest", parameters={Parameter(name='email')}, type=StringType)
Classes_Buissnesslayer_UserHandler_m_identifyUser: Method = Method(name="identifyUser", parameters={Parameter(name='email')}, type=StringType)
Classes_Buissnesslayer_UserHandler.attributes={Classes_Buissnesslayer_UserHandler_Users}
Classes_Buissnesslayer_UserHandler.methods={Classes_Buissnesslayer_UserHandler_m_CreateEmployee, Classes_Buissnesslayer_UserHandler_m_identifyUser, Classes_Buissnesslayer_UserHandler_m_sendEmailVerification, Classes_Buissnesslayer_UserHandler_m_identifyUser, Classes_Buissnesslayer_UserHandler_m_AddNewGuest, Classes_Buissnesslayer_UserHandler_m_isEmailValid}

# Classes_Buissnesslayer_Employee class attributes and methods
Classes_Buissnesslayer_Employee_ID: Property = Property(name="ID", type=IntegerType)
Classes_Buissnesslayer_Employee_Password: Property = Property(name="Password", type=StringType)
Classes_Buissnesslayer_Employee.attributes={Classes_Buissnesslayer_Employee_Password, Classes_Buissnesslayer_Employee_ID}

# Classes_Buissnesslayer_Address class attributes and methods
Classes_Buissnesslayer_Address_street: Property = Property(name="street", type=StringType)
Classes_Buissnesslayer_Address_postalNumber: Property = Property(name="postalNumber", type=IntegerType)
Classes_Buissnesslayer_Address_city: Property = Property(name="city", type=StringType)
Classes_Buissnesslayer_Address_country: Property = Property(name="country", type=StringType)
Classes_Buissnesslayer_Address.attributes={Classes_Buissnesslayer_Address_city, Classes_Buissnesslayer_Address_street, Classes_Buissnesslayer_Address_postalNumber, Classes_Buissnesslayer_Address_country}

# Classes_Buissnesslayer_Guest class attributes and methods
Classes_Buissnesslayer_Guest_wrokAround: Property = Property(name="wrokAround", type=IntegerType)
Classes_Buissnesslayer_Guest.attributes={Classes_Buissnesslayer_Guest_wrokAround}

# Classes_Interactionlayer_GUI class attributes and methods

# GUIController class attributes and methods

# Classes_Interactionlayer_GUIController class attributes and methods
Classes_Interactionlayer_GUIController_m_showAvailableRooms: Method = Method(name="showAvailableRooms", parameters={Parameter(name='endDate'), Parameter(name='nrOfGuests'), Parameter(name='startDate'), Parameter(name='roomType')}, type=IntegerType)
Classes_Interactionlayer_GUIController_m_displayError: Method = Method(name="displayError", parameters={})
Classes_Interactionlayer_GUIController_m_displayExtras: Method = Method(name="displayExtras", parameters={Parameter(name='extras')})
Classes_Interactionlayer_GUIController_m_displayParkings: Method = Method(name="displayParkings", parameters={Parameter(name='parkings')})
Classes_Interactionlayer_GUIController_m_displayRoomTypes: Method = Method(name="displayRoomTypes", parameters={}, type=IntegerType)
Classes_Interactionlayer_GUIController_m_displayRoomsGrid: Method = Method(name="displayRoomsGrid", parameters={Parameter(name='roomType')})
Classes_Interactionlayer_GUIController_m_displayPaymentOption: Method = Method(name="displayPaymentOption", parameters={})
Classes_Interactionlayer_GUIController_m_displayRoomsByID: Method = Method(name="displayRoomsByID", parameters={Parameter(name='bookingID')})
Classes_Interactionlayer_GUIController_m_displayBookingsByIDintbookingID: Method = Method(name="displayBookingsByIDintbookingID", parameters={Parameter(name='bookingID')})
Classes_Interactionlayer_GUIController_m_displayBookingCancelled: Method = Method(name="displayBookingCancelled", parameters={})
Classes_Interactionlayer_GUIController_m_displayDateOptions: Method = Method(name="displayDateOptions", parameters={})
Classes_Interactionlayer_GUIController.methods={Classes_Interactionlayer_GUIController_m_displayBookingCancelled, Classes_Interactionlayer_GUIController_m_displayExtras, Classes_Interactionlayer_GUIController_m_displayPaymentOption, Classes_Interactionlayer_GUIController_m_displayRoomsGrid, Classes_Interactionlayer_GUIController_m_displayError, Classes_Interactionlayer_GUIController_m_displayParkings, Classes_Interactionlayer_GUIController_m_displayBookingsByIDintbookingID, Classes_Interactionlayer_GUIController_m_showAvailableRooms, Classes_Interactionlayer_GUIController_m_displayDateOptions, Classes_Interactionlayer_GUIController_m_displayRoomsByID, Classes_Interactionlayer_GUIController_m_displayRoomTypes}

# GUI class attributes and methods

# Classes_Interactionlayer_LoginController class attributes and methods
Classes_Interactionlayer_LoginController_m_loginEmployee: Method = Method(name="loginEmployee", parameters={Parameter(name='ID')}, type=BooleanType)
Classes_Interactionlayer_LoginController_m_loginGuest: Method = Method(name="loginGuest", parameters={Parameter(name='bookingID')}, type=BooleanType)
Classes_Interactionlayer_LoginController_m_loginCreateGuest: Method = Method(name="loginCreateGuest", parameters={Parameter(name='email')}, type=StringType)
Classes_Interactionlayer_LoginController.methods={Classes_Interactionlayer_LoginController_m_loginGuest, Classes_Interactionlayer_LoginController_m_loginEmployee, Classes_Interactionlayer_LoginController_m_loginCreateGuest}

# PaymentHandler class attributes and methods

# Classes_Interactionlayer_LoginController_DataType1 class attributes and methods

# Classes_BuisnessLogicLayer_PaymentHandler class attributes and methods
Classes_BuisnessLogicLayer_PaymentHandler_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='paymentInfo'), Parameter(name='booking')})
Classes_BuisnessLogicLayer_PaymentHandler.methods={Classes_BuisnessLogicLayer_PaymentHandler_m_makePayment}

# Classes_BuisnessLogicLayer_PaymentInfo class attributes and methods
Classes_BuisnessLogicLayer_PaymentInfo_PaymentComplete: Property = Property(name="PaymentComplete", type=BooleanType)
Classes_BuisnessLogicLayer_PaymentInfo_CreditCard: Property = Property(name="CreditCard", type=IntegerType)
Classes_BuisnessLogicLayer_PaymentInfo_CVV: Property = Property(name="CVV", type=IntegerType)
Classes_BuisnessLogicLayer_PaymentInfo_ExpiryDate: Property = Property(name="ExpiryDate", type=IntegerType)
Classes_BuisnessLogicLayer_PaymentInfo.attributes={Classes_BuisnessLogicLayer_PaymentInfo_CreditCard, Classes_BuisnessLogicLayer_PaymentInfo_PaymentComplete, Classes_BuisnessLogicLayer_PaymentInfo_CVV, Classes_BuisnessLogicLayer_PaymentInfo_ExpiryDate}

# Relationships
userDB0: BinaryAssociation = BinaryAssociation(
    name="userDB0",
    ends={
        Property(name="Guest", type=Classes_Datalayer_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Datalayer_Database", type=Guest, multiplicity=Multiplicity(0, 9999))
    }
)
userhandler1: BinaryAssociation = BinaryAssociation(
    name="userhandler1",
    ends={
        Property(name="Buissnesslayer", type=Classes_Datalayer_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="UserHandler", type=UserHandler, multiplicity=Multiplicity(1, 1))
    }
)
employeeDB2: BinaryAssociation = BinaryAssociation(
    name="employeeDB2",
    ends={
        Property(name="Employee", type=Classes_Datalayer_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Datalayer_Database3", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
bookingDB4: BinaryAssociation = BinaryAssociation(
    name="bookingDB4",
    ends={
        Property(name="Booking", type=Classes_Datalayer_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Datalayer_Database5", type=Booking, multiplicity=Multiplicity(0, 9999))
    }
)
roomDB6: BinaryAssociation = BinaryAssociation(
    name="roomDB6",
    ends={
        Property(name="Room", type=Classes_Datalayer_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Datalayer_Database7", type=Room, multiplicity=Multiplicity(0, 9999))
    }
)
room8: BinaryAssociation = BinaryAssociation(
    name="room8",
    ends={
        Property(name="Room9", type=Classes_Buissnesslayer_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_Booking", type=Room, multiplicity=Multiplicity(1, 9999))
    }
)
Rooms10: BinaryAssociation = BinaryAssociation(
    name="Rooms10",
    ends={
        Property(name="Room12", type=Classes_Buissnesslayer_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_Booking11", type=Room, multiplicity=Multiplicity(0, 9999))
    }
)
booking13: BinaryAssociation = BinaryAssociation(
    name="booking13",
    ends={
        Property(name="Booking14", type=Classes_Buissnesslayer_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_BookingHandler", type=Booking, multiplicity=Multiplicity(1, 1))
    }
)
Bookings15: BinaryAssociation = BinaryAssociation(
    name="Bookings15",
    ends={
        Property(name="Booking17", type=Classes_Buissnesslayer_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_BookingHandler16", type=Booking, multiplicity=Multiplicity(1, 1))
    }
)
User18: BinaryAssociation = BinaryAssociation(
    name="User18",
    ends={
        Property(name="Buissnesslayer19", type=Classes_Buissnesslayer_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
database20: BinaryAssociation = BinaryAssociation(
    name="database20",
    ends={
        Property(name="Database", type=Classes_Buissnesslayer_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_BookingHandler21", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
userhandler22: BinaryAssociation = BinaryAssociation(
    name="userhandler22",
    ends={
        Property(name="UserHandler24", type=Classes_Buissnesslayer_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_BookingHandler23", type=UserHandler, multiplicity=Multiplicity(1, 1))
    }
)
logincontroller25: BinaryAssociation = BinaryAssociation(
    name="logincontroller25",
    ends={
        Property(name="LoginController", type=Classes_Buissnesslayer_User, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_User", type=LoginController, multiplicity=Multiplicity(1, 1))
    }
)
userhandler26: BinaryAssociation = BinaryAssociation(
    name="userhandler26",
    ends={
        Property(name="UserHandler28", type=Classes_Buissnesslayer_User, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_User27", type=UserHandler, multiplicity=Multiplicity(1, 1))
    }
)
address29: BinaryAssociation = BinaryAssociation(
    name="address29",
    ends={
        Property(name="Address", type=Classes_Buissnesslayer_User, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Buissnesslayer_User30", type=Address, multiplicity=Multiplicity(1, 1))
    }
)
bookinghandler31: BinaryAssociation = BinaryAssociation(
    name="bookinghandler31",
    ends={
        Property(name="Buissnesslayer32", type=Classes_Buissnesslayer_User, multiplicity=Multiplicity(1, 1)),
        Property(name="BookingHandler", type=BookingHandler, multiplicity=Multiplicity(1, 1))
    }
)
database33: BinaryAssociation = BinaryAssociation(
    name="database33",
    ends={
        Property(name="Datalayer", type=Classes_Buissnesslayer_UserHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Database34", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
logincontroller35: BinaryAssociation = BinaryAssociation(
    name="logincontroller35",
    ends={
        Property(name="Interactionlayer", type=Classes_Buissnesslayer_UserHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="LoginController36", type=LoginController, multiplicity=Multiplicity(1, 1))
    }
)
guicontroller37: BinaryAssociation = BinaryAssociation(
    name="guicontroller37",
    ends={
        Property(name="GUIController", type=Classes_Interactionlayer_GUI, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interactionlayer_GUI", type=GUIController, multiplicity=Multiplicity(1, 1))
    }
)
display38: BinaryAssociation = BinaryAssociation(
    name="display38",
    ends={
        Property(name="Classes_Interactionlayer_GUIController", type=GUI, multiplicity=Multiplicity(1, 1)),
        Property(name="GUI", type=Classes_Interactionlayer_GUIController, multiplicity=Multiplicity(1, 1))
    }
)
logincontroller39: BinaryAssociation = BinaryAssociation(
    name="logincontroller39",
    ends={
        Property(name="Interactionlayer41", type=Classes_Interactionlayer_GUIController, multiplicity=Multiplicity(1, 1)),
        Property(name="LoginController40", type=LoginController, multiplicity=Multiplicity(1, 1))
    }
)
bookinghandler42: BinaryAssociation = BinaryAssociation(
    name="bookinghandler42",
    ends={
        Property(name="BookingHandler44", type=Classes_Interactionlayer_GUIController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interactionlayer_GUIController43", type=BookingHandler, multiplicity=Multiplicity(1, 1))
    }
)
guicontroller45: BinaryAssociation = BinaryAssociation(
    name="guicontroller45",
    ends={
        Property(name="Interactionlayer47", type=Classes_Interactionlayer_LoginController, multiplicity=Multiplicity(1, 1)),
        Property(name="GUIController46", type=GUIController, multiplicity=Multiplicity(1, 1))
    }
)
currentUser48: BinaryAssociation = BinaryAssociation(
    name="currentUser48",
    ends={
        Property(name="User49", type=Classes_Interactionlayer_LoginController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interactionlayer_LoginController", type=User, multiplicity=Multiplicity(1, 1))
    }
)
paymenthandler50: BinaryAssociation = BinaryAssociation(
    name="paymenthandler50",
    ends={
        Property(name="PaymentHandler", type=Classes_Interactionlayer_LoginController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interactionlayer_LoginController51", type=PaymentHandler, multiplicity=Multiplicity(1, 1))
    }
)
userhandler52: BinaryAssociation = BinaryAssociation(
    name="userhandler52",
    ends={
        Property(name="Buissnesslayer54", type=Classes_Interactionlayer_LoginController, multiplicity=Multiplicity(1, 1)),
        Property(name="UserHandler53", type=UserHandler, multiplicity=Multiplicity(1, 1))
    }
)
paymenthandler55: BinaryAssociation = BinaryAssociation(
    name="paymenthandler55",
    ends={
        Property(name="PaymentHandler56", type=Classes_BuisnessLogicLayer_PaymentInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_BuisnessLogicLayer_PaymentInfo", type=PaymentHandler, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Classes_Buissnesslayer_Employee_User = Generalization(general=User, specific=Classes_Buissnesslayer_Employee)
gen_Classes_Buissnesslayer_Guest_User = Generalization(general=User, specific=Classes_Buissnesslayer_Guest)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Guest, Classes_Datalayer_Database, UserHandler, Employee, Booking, Room, Classes_Buissnesslayer_Room, Classes_Buissnesslayer_Booking, Classes_Buissnesslayer_BookingHandler, User, Database, Classes_Buissnesslayer_User, LoginController, Address, BookingHandler, Classes_Buissnesslayer_UserHandler, Classes_Buissnesslayer_Employee, Classes_Buissnesslayer_Address, Classes_Buissnesslayer_Guest, Classes_Interactionlayer_GUI, GUIController, Classes_Interactionlayer_GUIController, GUI, Classes_Interactionlayer_LoginController, PaymentHandler, Classes_Interactionlayer_LoginController_DataType1, Classes_BuisnessLogicLayer_PaymentHandler, Classes_BuisnessLogicLayer_PaymentInfo},
    associations={userDB0, userhandler1, employeeDB2, bookingDB4, roomDB6, room8, Rooms10, booking13, Bookings15, User18, database20, userhandler22, logincontroller25, userhandler26, address29, bookinghandler31, database33, logincontroller35, guicontroller37, display38, logincontroller39, bookinghandler42, guicontroller45, currentUser48, paymenthandler50, userhandler52, paymenthandler55},
    generalizations={gen_Classes_Buissnesslayer_Employee_User, gen_Classes_Buissnesslayer_Guest_User},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)