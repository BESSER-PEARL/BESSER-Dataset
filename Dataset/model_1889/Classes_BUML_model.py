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
Classes_mdsdBilling_BillingController = Class(name="Classes::mdsdBilling::BillingController")
mdsdBilling_StaffBilling = Class(name="mdsdBilling::StaffBilling")
mdsdBilling_BookingToBill = Class(name="mdsdBilling::BookingToBill")
mdsdBilling_CustomerBilling = Class(name="mdsdBilling::CustomerBilling")
Bill = Class(name="Bill")
Classes_mdsdBilling_Bill = Class(name="Classes::mdsdBilling::Bill")
Transaction = Class(name="Transaction")
Classes_mdsdBilling_Transaction = Class(name="Classes::mdsdBilling::Transaction")
Classes_mdsdBilling_StaffBilling = Class(name="Classes::mdsdBilling::StaffBilling", is_abstract=True)
Classes_mdsdBooking_BookingController = Class(name="Classes::mdsdBooking::BookingController")
mdsdBooking_UserBooking = Class(name="mdsdBooking::UserBooking")
mdsdBooking_StaffBooking = Class(name="mdsdBooking::StaffBooking")
Booking = Class(name="Booking")
Classes_mdsdBilling_BookingToBill = Class(name="Classes::mdsdBilling::BookingToBill", is_abstract=True)
Classes_mdsdBilling_CustomerBilling = Class(name="Classes::mdsdBilling::CustomerBilling", is_abstract=True)
Service = Class(name="Service")
Classes_mdsdBooking_Service = Class(name="Classes::mdsdBooking::Service")
Classes_mdsdBooking_UserBooking = Class(name="Classes::mdsdBooking::UserBooking", is_abstract=True)
Classes_mdsdBooking_StaffBooking = Class(name="Classes::mdsdBooking::StaffBooking", is_abstract=True)
Meal = Class(name="Meal")
Classes_mdsdBooking_Meal = Class(name="Classes::mdsdBooking::Meal")
Classes_mdsdBooking_Booking = Class(name="Classes::mdsdBooking::Booking")
HotelStaff = Class(name="HotelStaff")
Classes_mdsdAdmin_HotelStaff = Class(name="Classes::mdsdAdmin::HotelStaff")
Classes_mdsdAdmin_AdminController = Class(name="Classes::mdsdAdmin::AdminController")
mdsdAdmin_Admin = Class(name="mdsdAdmin::Admin")
mdsdAdmin_BookingToAdmin = Class(name="mdsdAdmin::BookingToAdmin")
mdsdAdmin_Staff = Class(name="mdsdAdmin::Staff")
Room = Class(name="Room")
Classes_mdsdAdmin_Admin = Class(name="Classes::mdsdAdmin::Admin", is_abstract=True)
Classes_mdsdAdmin_Room = Class(name="Classes::mdsdAdmin::Room")
Classes_mdsdAdmin_BookingToAdmin = Class(name="Classes::mdsdAdmin::BookingToAdmin", is_abstract=True)
Classes_mdsdAdmin_Staff = Class(name="Classes::mdsdAdmin::Staff", is_abstract=True)
Classes_mdsdAccount_Account = Class(name="Classes::mdsdAccount::Account")
Pet = Class(name="Pet")
Classes_mdsdAccount_BookingToAccount = Class(name="Classes::mdsdAccount::BookingToAccount", is_abstract=True)
Classes_mdsdAccount_CustomerAccount = Class(name="Classes::mdsdAccount::CustomerAccount", is_abstract=True)
Classes_mdsdAccount_Pet = Class(name="Classes::mdsdAccount::Pet")
Classes_mdsdAccount_AccountController = Class(name="Classes::mdsdAccount::AccountController")
mdsdAccount_BookingToAccount = Class(name="mdsdAccount::BookingToAccount")
mdsdAccount_CustomerAccount = Class(name="mdsdAccount::CustomerAccount")
Account = Class(name="Account")

# Classes_mdsdBilling_BillingController class attributes and methods

# mdsdBilling_StaffBilling class attributes and methods

# mdsdBilling_BookingToBill class attributes and methods

# mdsdBilling_CustomerBilling class attributes and methods

# Bill class attributes and methods

# Classes_mdsdBilling_Bill class attributes and methods
Classes_mdsdBilling_Bill_isPaid: Property = Property(name="isPaid", type=BooleanType)
Classes_mdsdBilling_Bill_ID: Property = Property(name="ID", type=StringType)
Classes_mdsdBilling_Bill_m_getTotalAmount: Method = Method(name="getTotalAmount", parameters={}, type=FloatType)
Classes_mdsdBilling_Bill.attributes={Classes_mdsdBilling_Bill_isPaid, Classes_mdsdBilling_Bill_ID}
Classes_mdsdBilling_Bill.methods={Classes_mdsdBilling_Bill_m_getTotalAmount}

# Transaction class attributes and methods

# Classes_mdsdBilling_Transaction class attributes and methods
Classes_mdsdBilling_Transaction_description: Property = Property(name="description", type=StringType)
Classes_mdsdBilling_Transaction_price: Property = Property(name="price", type=FloatType)
Classes_mdsdBilling_Transaction.attributes={Classes_mdsdBilling_Transaction_price, Classes_mdsdBilling_Transaction_description}

# Classes_mdsdBilling_StaffBilling class attributes and methods
Classes_mdsdBilling_StaffBilling_m_giveRefund: Method = Method(name="giveRefund", parameters={Parameter(name='transaction'), Parameter(name='billId')})
Classes_mdsdBilling_StaffBilling_m_isPaid: Method = Method(name="isPaid", parameters={Parameter(name='billID')}, type=BooleanType)
Classes_mdsdBilling_StaffBilling_m_printReceipt: Method = Method(name="printReceipt", parameters={Parameter(name='billID')})
Classes_mdsdBilling_StaffBilling_m_modifyBill: Method = Method(name="modifyBill", parameters={Parameter(name='newPrice'), Parameter(name='billID'), Parameter(name='transaction')})
Classes_mdsdBilling_StaffBilling.methods={Classes_mdsdBilling_StaffBilling_m_isPaid, Classes_mdsdBilling_StaffBilling_m_printReceipt, Classes_mdsdBilling_StaffBilling_m_giveRefund, Classes_mdsdBilling_StaffBilling_m_modifyBill}

# Classes_mdsdBooking_BookingController class attributes and methods
Classes_mdsdBooking_BookingController_m_getBookingList: Method = Method(name="getBookingList", parameters={Parameter(name='email')}, type=StringType)
Classes_mdsdBooking_BookingController.methods={Classes_mdsdBooking_BookingController_m_getBookingList}

# mdsdBooking_UserBooking class attributes and methods

# mdsdBooking_StaffBooking class attributes and methods

# Booking class attributes and methods

# Classes_mdsdBilling_BookingToBill class attributes and methods
Classes_mdsdBilling_BookingToBill_m_addTransaction: Method = Method(name="addTransaction", parameters={Parameter(name='description'), Parameter(name='booking'), Parameter(name='amount')})
Classes_mdsdBilling_BookingToBill.methods={Classes_mdsdBilling_BookingToBill_m_addTransaction}

# Classes_mdsdBilling_CustomerBilling class attributes and methods

# Service class attributes and methods

# Classes_mdsdBooking_Service class attributes and methods
Classes_mdsdBooking_Service_description: Property = Property(name="description", type=StringType)
Classes_mdsdBooking_Service_price: Property = Property(name="price", type=FloatType)
Classes_mdsdBooking_Service.attributes={Classes_mdsdBooking_Service_price, Classes_mdsdBooking_Service_description}

# Classes_mdsdBooking_UserBooking class attributes and methods
Classes_mdsdBooking_UserBooking_m_enterCustomerInfo: Method = Method(name="enterCustomerInfo", parameters={Parameter(name='rooms'), Parameter(name='booking'), Parameter(name='customerEmail'), Parameter(name='customerName'), Parameter(name='petName')})
Classes_mdsdBooking_UserBooking_m_enterDatesOfStay: Method = Method(name="enterDatesOfStay", parameters={Parameter(name='rooms'), Parameter(name='stayFrom'), Parameter(name='stayTo'), Parameter(name='petType')}, type=StringType)
Classes_mdsdBooking_UserBooking_m_modifyBooking: Method = Method(name="modifyBooking", parameters={Parameter(name='bookingId')})
Classes_mdsdBooking_UserBooking_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='bookingId')})
Classes_mdsdBooking_UserBooking_m_enterMealInfo: Method = Method(name="enterMealInfo", parameters={Parameter(name='amountOfFood'), Parameter(name='price'), Parameter(name='schedule'), Parameter(name='bookingId'), Parameter(name='foodType')})
Classes_mdsdBooking_UserBooking_m_enterService: Method = Method(name="enterService", parameters={Parameter(name='service'), Parameter(name='bookingId')})
Classes_mdsdBooking_UserBooking.methods={Classes_mdsdBooking_UserBooking_m_enterMealInfo, Classes_mdsdBooking_UserBooking_m_enterDatesOfStay, Classes_mdsdBooking_UserBooking_m_cancelBooking, Classes_mdsdBooking_UserBooking_m_enterService, Classes_mdsdBooking_UserBooking_m_enterCustomerInfo, Classes_mdsdBooking_UserBooking_m_modifyBooking}

# Classes_mdsdBooking_StaffBooking class attributes and methods
Classes_mdsdBooking_StaffBooking_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='bookingID'), Parameter(name='rooms')})
Classes_mdsdBooking_StaffBooking_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='bills'), Parameter(name='rooms'), Parameter(name='bookingID')}, type=BooleanType)
Classes_mdsdBooking_StaffBooking_m_addNewService: Method = Method(name="addNewService", parameters={Parameter(name='description'), Parameter(name='price')})
Classes_mdsdBooking_StaffBooking.methods={Classes_mdsdBooking_StaffBooking_m_checkIn, Classes_mdsdBooking_StaffBooking_m_addNewService, Classes_mdsdBooking_StaffBooking_m_checkOut}

# Meal class attributes and methods

# Classes_mdsdBooking_Meal class attributes and methods
Classes_mdsdBooking_Meal_foodType: Property = Property(name="foodType", type=StringType)
Classes_mdsdBooking_Meal_schedule: Property = Property(name="schedule", type=StringType)
Classes_mdsdBooking_Meal_amountOfFood: Property = Property(name="amountOfFood", type=FloatType)
Classes_mdsdBooking_Meal_price: Property = Property(name="price", type=FloatType)
Classes_mdsdBooking_Meal.attributes={Classes_mdsdBooking_Meal_foodType, Classes_mdsdBooking_Meal_amountOfFood, Classes_mdsdBooking_Meal_price, Classes_mdsdBooking_Meal_schedule}

# Classes_mdsdBooking_Booking class attributes and methods
Classes_mdsdBooking_Booking_bookingId: Property = Property(name="bookingId", type=StringType)
Classes_mdsdBooking_Booking_isCheckedIn: Property = Property(name="isCheckedIn", type=BooleanType)
Classes_mdsdBooking_Booking_isCheckedOut: Property = Property(name="isCheckedOut", type=BooleanType)
Classes_mdsdBooking_Booking_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
Classes_mdsdBooking_Booking_dateFrom: Property = Property(name="dateFrom", type=DateType)
Classes_mdsdBooking_Booking_customerName: Property = Property(name="customerName", type=StringType)
Classes_mdsdBooking_Booking_customerEmail: Property = Property(name="customerEmail", type=StringType)
Classes_mdsdBooking_Booking_dateTo: Property = Property(name="dateTo", type=DateType)
Classes_mdsdBooking_Booking_bill_Id: Property = Property(name="bill_Id", type=StringType)
Classes_mdsdBooking_Booking_petName: Property = Property(name="petName", type=StringType)
Classes_mdsdBooking_Booking.attributes={Classes_mdsdBooking_Booking_roomNumber, Classes_mdsdBooking_Booking_dateFrom, Classes_mdsdBooking_Booking_dateTo, Classes_mdsdBooking_Booking_bookingId, Classes_mdsdBooking_Booking_bill_Id, Classes_mdsdBooking_Booking_isCheckedOut, Classes_mdsdBooking_Booking_customerName, Classes_mdsdBooking_Booking_isCheckedIn, Classes_mdsdBooking_Booking_customerEmail, Classes_mdsdBooking_Booking_petName}

# HotelStaff class attributes and methods

# Classes_mdsdAdmin_HotelStaff class attributes and methods
Classes_mdsdAdmin_HotelStaff_Name: Property = Property(name="Name", type=StringType)
Classes_mdsdAdmin_HotelStaff_rank: Property = Property(name="rank", type=IntegerType)
Classes_mdsdAdmin_HotelStaff_SSN: Property = Property(name="SSN", type=StringType)
Classes_mdsdAdmin_HotelStaff_isLoggedIn: Property = Property(name="isLoggedIn", type=BooleanType)
Classes_mdsdAdmin_HotelStaff_password: Property = Property(name="password", type=StringType)
Classes_mdsdAdmin_HotelStaff.attributes={Classes_mdsdAdmin_HotelStaff_isLoggedIn, Classes_mdsdAdmin_HotelStaff_password, Classes_mdsdAdmin_HotelStaff_SSN, Classes_mdsdAdmin_HotelStaff_rank, Classes_mdsdAdmin_HotelStaff_Name}

# Classes_mdsdAdmin_AdminController class attributes and methods
Classes_mdsdAdmin_AdminController_m_isLoggedIn: Method = Method(name="isLoggedIn", parameters={Parameter(name='ssn')}, type=BooleanType)
Classes_mdsdAdmin_AdminController.methods={Classes_mdsdAdmin_AdminController_m_isLoggedIn}

# mdsdAdmin_Admin class attributes and methods

# mdsdAdmin_BookingToAdmin class attributes and methods

# mdsdAdmin_Staff class attributes and methods

# Room class attributes and methods

# Classes_mdsdAdmin_Admin class attributes and methods
Classes_mdsdAdmin_Admin_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='status'), Parameter(name='type'), Parameter(name='room')}, type=StringType)
Classes_mdsdAdmin_Admin_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='number')})
Classes_mdsdAdmin_Admin_m_removeStaff: Method = Method(name="removeStaff", parameters={Parameter(name='SSN')})
Classes_mdsdAdmin_Admin_m_modifyStaff: Method = Method(name="modifyStaff", parameters={Parameter(name='newName'), Parameter(name='SSN'), Parameter(name='newRank')})
Classes_mdsdAdmin_Admin_m_createStaff: Method = Method(name="createStaff", parameters={Parameter(name='password'), Parameter(name='rank'), Parameter(name='SSN'), Parameter(name='name')}, type=StringType)
Classes_mdsdAdmin_Admin.methods={Classes_mdsdAdmin_Admin_m_removeRoom, Classes_mdsdAdmin_Admin_m_createStaff, Classes_mdsdAdmin_Admin_m_modifyStaff, Classes_mdsdAdmin_Admin_m_addRoom, Classes_mdsdAdmin_Admin_m_removeStaff}

# Classes_mdsdAdmin_Room class attributes and methods
Classes_mdsdAdmin_Room_type: Property = Property(name="type", type=StringType)
Classes_mdsdAdmin_Room_status: Property = Property(name="status", type=StringType)
Classes_mdsdAdmin_Room_number: Property = Property(name="number", type=IntegerType)
Classes_mdsdAdmin_Room.attributes={Classes_mdsdAdmin_Room_type, Classes_mdsdAdmin_Room_status, Classes_mdsdAdmin_Room_number}

# Classes_mdsdAdmin_BookingToAdmin class attributes and methods
Classes_mdsdAdmin_BookingToAdmin_m_getPetTypes: Method = Method(name="getPetTypes", parameters={}, type=StringType)
Classes_mdsdAdmin_BookingToAdmin.methods={Classes_mdsdAdmin_BookingToAdmin_m_getPetTypes}

# Classes_mdsdAdmin_Staff class attributes and methods
Classes_mdsdAdmin_Staff_m_changeRoomStatus: Method = Method(name="changeRoomStatus", parameters={Parameter(name='roomNumber'), Parameter(name='status')})
Classes_mdsdAdmin_Staff_m_staffLogin: Method = Method(name="staffLogin", parameters={Parameter(name='password'), Parameter(name='ssn')})
Classes_mdsdAdmin_Staff_m_staffLogout: Method = Method(name="staffLogout", parameters={Parameter(name='ssn')})
Classes_mdsdAdmin_Staff.methods={Classes_mdsdAdmin_Staff_m_staffLogin, Classes_mdsdAdmin_Staff_m_changeRoomStatus, Classes_mdsdAdmin_Staff_m_staffLogout}

# Classes_mdsdAccount_Account class attributes and methods
Classes_mdsdAccount_Account_accountID: Property = Property(name="accountID", type=StringType)
Classes_mdsdAccount_Account_password: Property = Property(name="password", type=StringType)
Classes_mdsdAccount_Account_name: Property = Property(name="name", type=StringType)
Classes_mdsdAccount_Account_email: Property = Property(name="email", type=StringType)
Classes_mdsdAccount_Account_isLoggedIn: Property = Property(name="isLoggedIn", type=BooleanType)
Classes_mdsdAccount_Account.attributes={Classes_mdsdAccount_Account_email, Classes_mdsdAccount_Account_password, Classes_mdsdAccount_Account_name, Classes_mdsdAccount_Account_isLoggedIn, Classes_mdsdAccount_Account_accountID}

# Pet class attributes and methods

# Classes_mdsdAccount_BookingToAccount class attributes and methods
Classes_mdsdAccount_BookingToAccount_m_getAccount: Method = Method(name="getAccount", parameters={Parameter(name='email')}, type=StringType)
Classes_mdsdAccount_BookingToAccount_m_isUserLoggedIn: Method = Method(name="isUserLoggedIn", parameters={Parameter(name='accountId')}, type=BooleanType)
Classes_mdsdAccount_BookingToAccount.methods={Classes_mdsdAccount_BookingToAccount_m_getAccount, Classes_mdsdAccount_BookingToAccount_m_isUserLoggedIn}

# Classes_mdsdAccount_CustomerAccount class attributes and methods
Classes_mdsdAccount_CustomerAccount_m_createAccount: Method = Method(name="createAccount", parameters={Parameter(name='customerEmail'), Parameter(name='customerName'), Parameter(name='password')}, type=StringType)
Classes_mdsdAccount_CustomerAccount_m_removePet: Method = Method(name="removePet", parameters={Parameter(name='accountID'), Parameter(name='name'), Parameter(name='type')})
Classes_mdsdAccount_CustomerAccount_m_login: Method = Method(name="login", parameters={Parameter(name='email'), Parameter(name='password')})
Classes_mdsdAccount_CustomerAccount_m_logout: Method = Method(name="logout", parameters={Parameter(name='accountId')})
Classes_mdsdAccount_CustomerAccount_m_addPet: Method = Method(name="addPet", parameters={Parameter(name='type'), Parameter(name='accountID'), Parameter(name='name')})
Classes_mdsdAccount_CustomerAccount.methods={Classes_mdsdAccount_CustomerAccount_m_logout, Classes_mdsdAccount_CustomerAccount_m_removePet, Classes_mdsdAccount_CustomerAccount_m_login, Classes_mdsdAccount_CustomerAccount_m_addPet, Classes_mdsdAccount_CustomerAccount_m_createAccount}

# Classes_mdsdAccount_Pet class attributes and methods
Classes_mdsdAccount_Pet_name: Property = Property(name="name", type=StringType)
Classes_mdsdAccount_Pet_type: Property = Property(name="type", type=StringType)
Classes_mdsdAccount_Pet.attributes={Classes_mdsdAccount_Pet_name, Classes_mdsdAccount_Pet_type}

# Classes_mdsdAccount_AccountController class attributes and methods

# mdsdAccount_BookingToAccount class attributes and methods

# mdsdAccount_CustomerAccount class attributes and methods

# Account class attributes and methods

# Relationships
bills0: BinaryAssociation = BinaryAssociation(
    name="bills0",
    ends={
        Property(name="Bill", type=Classes_mdsdBilling_BillingController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBilling_BillingController", type=Bill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transactions1: BinaryAssociation = BinaryAssociation(
    name="transactions1",
    ends={
        Property(name="Transaction", type=Classes_mdsdBilling_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBilling_Bill", type=Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookings2: BinaryAssociation = BinaryAssociation(
    name="bookings2",
    ends={
        Property(name="Booking", type=Classes_mdsdBooking_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBooking_BookingController", type=Booking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services3: BinaryAssociation = BinaryAssociation(
    name="services3",
    ends={
        Property(name="Service", type=Classes_mdsdBooking_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBooking_BookingController4", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookedServices5: BinaryAssociation = BinaryAssociation(
    name="bookedServices5",
    ends={
        Property(name="Service6", type=Classes_mdsdBooking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBooking_Booking", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
mealInfo7: BinaryAssociation = BinaryAssociation(
    name="mealInfo7",
    ends={
        Property(name="Meal", type=Classes_mdsdBooking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdBooking_Booking8", type=Meal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rooms9: BinaryAssociation = BinaryAssociation(
    name="rooms9",
    ends={
        Property(name="Room", type=Classes_mdsdAdmin_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdAdmin_AdminController", type=Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staff10: BinaryAssociation = BinaryAssociation(
    name="staff10",
    ends={
        Property(name="HotelStaff", type=Classes_mdsdAdmin_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdAdmin_AdminController11", type=HotelStaff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pets12: BinaryAssociation = BinaryAssociation(
    name="pets12",
    ends={
        Property(name="Pet", type=Classes_mdsdAccount_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdAccount_Account", type=Pet, multiplicity=Multiplicity(0, 9999))
    }
)
accounts13: BinaryAssociation = BinaryAssociation(
    name="accounts13",
    ends={
        Property(name="Account", type=Classes_mdsdAccount_AccountController, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_mdsdAccount_AccountController", type=Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Classes_mdsdBilling_BillingController_mdsdBilling_StaffBilling = Generalization(general=mdsdBilling_StaffBilling, specific=Classes_mdsdBilling_BillingController)
gen_Classes_mdsdBilling_BillingController_mdsdBilling_BookingToBill = Generalization(general=mdsdBilling_BookingToBill, specific=Classes_mdsdBilling_BillingController)
gen_Classes_mdsdBilling_BillingController_mdsdBilling_CustomerBilling = Generalization(general=mdsdBilling_CustomerBilling, specific=Classes_mdsdBilling_BillingController)
gen_Classes_mdsdBooking_BookingController_mdsdBooking_UserBooking = Generalization(general=mdsdBooking_UserBooking, specific=Classes_mdsdBooking_BookingController)
gen_Classes_mdsdBooking_BookingController_mdsdBooking_StaffBooking = Generalization(general=mdsdBooking_StaffBooking, specific=Classes_mdsdBooking_BookingController)
gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_Admin = Generalization(general=mdsdAdmin_Admin, specific=Classes_mdsdAdmin_AdminController)
gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_BookingToAdmin = Generalization(general=mdsdAdmin_BookingToAdmin, specific=Classes_mdsdAdmin_AdminController)
gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_Staff = Generalization(general=mdsdAdmin_Staff, specific=Classes_mdsdAdmin_AdminController)
gen_Classes_mdsdAccount_AccountController_mdsdAccount_BookingToAccount = Generalization(general=mdsdAccount_BookingToAccount, specific=Classes_mdsdAccount_AccountController)
gen_Classes_mdsdAccount_AccountController_mdsdAccount_CustomerAccount = Generalization(general=mdsdAccount_CustomerAccount, specific=Classes_mdsdAccount_AccountController)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Classes_mdsdBilling_BillingController, mdsdBilling_StaffBilling, mdsdBilling_BookingToBill, mdsdBilling_CustomerBilling, Bill, Classes_mdsdBilling_Bill, Transaction, Classes_mdsdBilling_Transaction, Classes_mdsdBilling_StaffBilling, Classes_mdsdBooking_BookingController, mdsdBooking_UserBooking, mdsdBooking_StaffBooking, Booking, Classes_mdsdBilling_BookingToBill, Classes_mdsdBilling_CustomerBilling, Service, Classes_mdsdBooking_Service, Classes_mdsdBooking_UserBooking, Classes_mdsdBooking_StaffBooking, Meal, Classes_mdsdBooking_Meal, Classes_mdsdBooking_Booking, HotelStaff, Classes_mdsdAdmin_HotelStaff, Classes_mdsdAdmin_AdminController, mdsdAdmin_Admin, mdsdAdmin_BookingToAdmin, mdsdAdmin_Staff, Room, Classes_mdsdAdmin_Admin, Classes_mdsdAdmin_Room, Classes_mdsdAdmin_BookingToAdmin, Classes_mdsdAdmin_Staff, Classes_mdsdAccount_Account, Pet, Classes_mdsdAccount_BookingToAccount, Classes_mdsdAccount_CustomerAccount, Classes_mdsdAccount_Pet, Classes_mdsdAccount_AccountController, mdsdAccount_BookingToAccount, mdsdAccount_CustomerAccount, Account},
    associations={bills0, transactions1, bookings2, services3, bookedServices5, mealInfo7, rooms9, staff10, pets12, accounts13},
    generalizations={gen_Classes_mdsdBilling_BillingController_mdsdBilling_StaffBilling, gen_Classes_mdsdBilling_BillingController_mdsdBilling_BookingToBill, gen_Classes_mdsdBilling_BillingController_mdsdBilling_CustomerBilling, gen_Classes_mdsdBooking_BookingController_mdsdBooking_UserBooking, gen_Classes_mdsdBooking_BookingController_mdsdBooking_StaffBooking, gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_Admin, gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_BookingToAdmin, gen_Classes_mdsdAdmin_AdminController_mdsdAdmin_Staff, gen_Classes_mdsdAccount_AccountController_mdsdAccount_BookingToAccount, gen_Classes_mdsdAccount_AccountController_mdsdAccount_CustomerAccount},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)