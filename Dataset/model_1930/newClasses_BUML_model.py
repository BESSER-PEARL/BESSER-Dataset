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
newClasses_Customer = Class(name="newClasses::Customer")
newClasses_Booking = Class(name="newClasses::Booking")
Booker = Class(name="Booker")
newClasses_Database = Class(name="newClasses::Database")
Receipt = Class(name="Receipt")
newClasses_CreditCard = Class(name="newClasses::CreditCard")
RoomProvider = Class(name="RoomProvider")
Biller = Class(name="Biller")
ServiceProvider = Class(name="ServiceProvider")
Validator = Class(name="Validator")
CustomerProvides = Class(name="CustomerProvides")
newClasses_ReceiptCreator = Class(name="newClasses::ReceiptCreator")
newClasses_RoomProvider = Class(name="newClasses::RoomProvider", is_abstract=True)
newClasses_Receipt = Class(name="newClasses::Receipt", is_abstract=True)
DB_interface = Class(name="DB::interface")
newClasses_DB_interface = Class(name="newClasses::DB::interface", is_abstract=True)
newClasses_Biller = Class(name="newClasses::Biller", is_abstract=True)
newClasses_ServiceProvider = Class(name="newClasses::ServiceProvider", is_abstract=True)
newClasses_Booker = Class(name="newClasses::Booker", is_abstract=True)
newClasses_Validator = Class(name="newClasses::Validator", is_abstract=True)
newClasses_CustomerProvides = Class(name="newClasses::CustomerProvides", is_abstract=True)
newClasses_Guest = Class(name="newClasses::Guest")
Customer = Class(name="Customer")
GuestBiller = Class(name="GuestBiller")
GuestInterface = Class(name="GuestInterface")
newClasses_GuestBiller = Class(name="newClasses::GuestBiller", is_abstract=True)
newClasses_Room = Class(name="newClasses::Room")
RoomType = Class(name="RoomType")
newClasses_InformationValidator = Class(name="newClasses::InformationValidator")
newClasses_ServiceHandler = Class(name="newClasses::ServiceHandler")
ServiceHandlerInterface = Class(name="ServiceHandlerInterface")
newClasses_Service = Class(name="newClasses::Service")
newClasses_GuestInterface = Class(name="newClasses::GuestInterface", is_abstract=True)
newClasses_RoomType = Class(name="newClasses::RoomType")
newClasses_Manager = Class(name="newClasses::Manager")
ManagerInterface = Class(name="ManagerInterface")
RoomHandlerInterface = Class(name="RoomHandlerInterface")
newClasses_RoomHandler = Class(name="newClasses::RoomHandler")
ServiceType = Class(name="ServiceType")
newClasses_ServiceType = Class(name="newClasses::ServiceType")
newClasses_ServiceHandlerInterface = Class(name="newClasses::ServiceHandlerInterface", is_abstract=True)
newClasses_RoomHandlerInterface = Class(name="newClasses::RoomHandlerInterface", is_abstract=True)
newClasses_BankComponent = Class(name="newClasses::BankComponent")
AdministratorProvides = Class(name="AdministratorProvides")
newClasses_AdministratorProvides = Class(name="newClasses::AdministratorProvides", is_abstract=True)
newClasses_ManagerInterface = Class(name="newClasses::ManagerInterface", is_abstract=True)
newClasses_Billing = Class(name="newClasses::Billing")
newClasses_LoginChecker = Class(name="newClasses::LoginChecker")

# newClasses_Customer class attributes and methods
newClasses_Customer_zipCode: Property = Property(name="zipCode", type=StringType)
newClasses_Customer_city: Property = Property(name="city", type=StringType)
newClasses_Customer_country: Property = Property(name="country", type=StringType)
newClasses_Customer_phoneNum: Property = Property(name="phoneNum", type=StringType)
newClasses_Customer_email: Property = Property(name="email", type=StringType)
newClasses_Customer_firstName: Property = Property(name="firstName", type=StringType)
newClasses_Customer_lastName: Property = Property(name="lastName", type=StringType)
newClasses_Customer_personalNum: Property = Property(name="personalNum", type=StringType)
newClasses_Customer_address: Property = Property(name="address", type=StringType)
newClasses_Customer_bookingNum: Property = Property(name="bookingNum", type=StringType)
newClasses_Customer_bookingCost: Property = Property(name="bookingCost", type=StringType)
newClasses_Customer.attributes={newClasses_Customer_address, newClasses_Customer_city, newClasses_Customer_phoneNum, newClasses_Customer_bookingCost, newClasses_Customer_lastName, newClasses_Customer_email, newClasses_Customer_personalNum, newClasses_Customer_bookingNum, newClasses_Customer_country, newClasses_Customer_zipCode, newClasses_Customer_firstName}

# newClasses_Booking class attributes and methods
newClasses_Booking_roomType: Property = Property(name="roomType", type=StringType)
newClasses_Booking_services: Property = Property(name="services", type=StringType)
newClasses_Booking_isPaid: Property = Property(name="isPaid", type=StringType)
newClasses_Booking_checkInDate: Property = Property(name="checkInDate", type=StringType)
newClasses_Booking_checkOutDate: Property = Property(name="checkOutDate", type=StringType)
newClasses_Booking_conformationNum: Property = Property(name="conformationNum", type=StringType)
newClasses_Booking_cost: Property = Property(name="cost", type=StringType)
newClasses_Booking.attributes={newClasses_Booking_isPaid, newClasses_Booking_checkInDate, newClasses_Booking_roomType, newClasses_Booking_cost, newClasses_Booking_checkOutDate, newClasses_Booking_services, newClasses_Booking_conformationNum}

# Booker class attributes and methods

# newClasses_Database class attributes and methods

# Receipt class attributes and methods

# newClasses_CreditCard class attributes and methods
newClasses_CreditCard_creditCardNumber: Property = Property(name="creditCardNumber", type=StringType)
newClasses_CreditCard_month: Property = Property(name="month", type=StringType)
newClasses_CreditCard_year: Property = Property(name="year", type=StringType)
newClasses_CreditCard_firstName: Property = Property(name="firstName", type=StringType)
newClasses_CreditCard_lastName: Property = Property(name="lastName", type=StringType)
newClasses_CreditCard_cvc: Property = Property(name="cvc", type=StringType)
newClasses_CreditCard.attributes={newClasses_CreditCard_firstName, newClasses_CreditCard_lastName, newClasses_CreditCard_cvc, newClasses_CreditCard_month, newClasses_CreditCard_year, newClasses_CreditCard_creditCardNumber}

# RoomProvider class attributes and methods

# Biller class attributes and methods

# ServiceProvider class attributes and methods

# Validator class attributes and methods

# CustomerProvides class attributes and methods

# newClasses_ReceiptCreator class attributes and methods

# newClasses_RoomProvider class attributes and methods
newClasses_RoomProvider_m_setAvalibility: Method = Method(name="setAvalibility", parameters={Parameter(name='roomType'), Parameter(name='checkInDate'), Parameter(name='status'), Parameter(name='checkOutDate')})
newClasses_RoomProvider_m_checkAvalibility: Method = Method(name="checkAvalibility", parameters={Parameter(name='roomType'), Parameter(name='checkInDate'), Parameter(name='checkOutDate')}, type=StringType)
newClasses_RoomProvider_m_dateChecker: Method = Method(name="dateChecker", parameters={Parameter(name='DBcheckIn'), Parameter(name='checkOutDate'), Parameter(name='checkInDate'), Parameter(name='DBcheckOut')}, type=StringType)
newClasses_RoomProvider.methods={newClasses_RoomProvider_m_setAvalibility, newClasses_RoomProvider_m_checkAvalibility, newClasses_RoomProvider_m_dateChecker}

# newClasses_Receipt class attributes and methods
newClasses_Receipt_m_createGuestReceipt: Method = Method(name="createGuestReceipt", parameters={Parameter(name='totalBillCost'), Parameter(name='guest'), Parameter(name='booking')})
newClasses_Receipt_m_createCustomerReceipt: Method = Method(name="createCustomerReceipt", parameters={Parameter(name='bookingCost'), Parameter(name='booking'), Parameter(name='customer')})
newClasses_Receipt.methods={newClasses_Receipt_m_createCustomerReceipt, newClasses_Receipt_m_createGuestReceipt}

# DB_interface class attributes and methods

# newClasses_DB_interface class attributes and methods
newClasses_DB_interface_m_storeGuest: Method = Method(name="storeGuest", parameters={Parameter(name='guest')})
newClasses_DB_interface_m_storeBooking: Method = Method(name="storeBooking", parameters={Parameter(name='booking')})
newClasses_DB_interface_m_storeCustomer: Method = Method(name="storeCustomer", parameters={Parameter(name='customer')})
newClasses_DB_interface_m_connect: Method = Method(name="connect", parameters={})
newClasses_DB_interface_m_registerCustomerPayment: Method = Method(name="registerCustomerPayment", parameters={Parameter(name='customer'), Parameter(name='bookingCost')})
newClasses_DB_interface_m_registerGuestPayment: Method = Method(name="registerGuestPayment", parameters={Parameter(name='guest'), Parameter(name='totalBillCost')})
newClasses_DB_interface.methods={newClasses_DB_interface_m_registerCustomerPayment, newClasses_DB_interface_m_storeCustomer, newClasses_DB_interface_m_storeGuest, newClasses_DB_interface_m_connect, newClasses_DB_interface_m_registerGuestPayment, newClasses_DB_interface_m_storeBooking}

# newClasses_Biller class attributes and methods
newClasses_Biller_m_pay: Method = Method(name="pay", parameters={Parameter(name='creditCardNum'), Parameter(name='cvc'), Parameter(name='addedServices'), Parameter(name='bookingCost'), Parameter(name='extraDays'), Parameter(name='month'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='year'), Parameter(name='isPaid')}, type=StringType)
newClasses_Biller_m_calculateCost: Method = Method(name="calculateCost", parameters={Parameter(name='checkInDate'), Parameter(name='checkOutDate'), Parameter(name='roomType'), Parameter(name='services')}, type=StringType)
newClasses_Biller_m_calculateBill: Method = Method(name="calculateBill", parameters={Parameter(name='extraDays'), Parameter(name='addedServices'), Parameter(name='bookingCost'), Parameter(name='isPaid')}, type=StringType)
newClasses_Biller.methods={newClasses_Biller_m_calculateBill, newClasses_Biller_m_calculateCost, newClasses_Biller_m_pay}

# newClasses_ServiceProvider class attributes and methods
newClasses_ServiceProvider_m_checkAvalibility: Method = Method(name="checkAvalibility", parameters={Parameter(name='service'), Parameter(name='checkInDate'), Parameter(name='checkOutDate')}, type=StringType)
newClasses_ServiceProvider_m_setAvalibility: Method = Method(name="setAvalibility", parameters={Parameter(name='status'), Parameter(name='service')})
newClasses_ServiceProvider.methods={newClasses_ServiceProvider_m_checkAvalibility, newClasses_ServiceProvider_m_setAvalibility}

# newClasses_Booker class attributes and methods
newClasses_Booker_m_generateConfirmNum: Method = Method(name="generateConfirmNum", parameters={}, type=StringType)
newClasses_Booker_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='services'), Parameter(name='roomType'), Parameter(name='checkOutDate'), Parameter(name='checkInDate')}, type=StringType)
newClasses_Booker_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='conformationNum')})
newClasses_Booker_m_reBook: Method = Method(name="reBook", parameters={Parameter(name='serviceType'), Parameter(name='comformationNum'), Parameter(name='roomType'), Parameter(name='checkInDate'), Parameter(name='checkOutDate')})
newClasses_Booker.methods={newClasses_Booker_m_createBooking, newClasses_Booker_m_generateConfirmNum, newClasses_Booker_m_reBook, newClasses_Booker_m_cancelBooking}

# newClasses_Validator class attributes and methods
newClasses_Validator_m_validateDates: Method = Method(name="validateDates", parameters={Parameter(name='checkInDate'), Parameter(name='checkOutDate')}, type=StringType)
newClasses_Validator_m_checkDateOrder: Method = Method(name="checkDateOrder", parameters={Parameter(name='checkOutDate'), Parameter(name='checkInDate')}, type=StringType)
newClasses_Validator_m_validateEmail: Method = Method(name="validateEmail", parameters={Parameter(name='email')}, type=StringType)
newClasses_Validator_m_validatePhoneNum: Method = Method(name="validatePhoneNum", parameters={Parameter(name='phoneNum')}, type=StringType)
newClasses_Validator_m_validatePersonalNum: Method = Method(name="validatePersonalNum", parameters={Parameter(name='personalNum')}, type=StringType)
newClasses_Validator_m_validateNames: Method = Method(name="validateNames", parameters={Parameter(name='firstName'), Parameter(name='lastName')}, type=StringType)
newClasses_Validator_m_validateAddress: Method = Method(name="validateAddress", parameters={Parameter(name='city'), Parameter(name='country'), Parameter(name='zipCode'), Parameter(name='address')}, type=StringType)
newClasses_Validator_m_checkAgeRestriction: Method = Method(name="checkAgeRestriction", parameters={Parameter(name='personalNum')}, type=StringType)
newClasses_Validator_m_validateConfirmationNum: Method = Method(name="validateConfirmationNum", parameters={Parameter(name='conformationNum')}, type=StringType)
newClasses_Validator_m_checkAge: Method = Method(name="checkAge", parameters={Parameter(name='day'), Parameter(name='month'), Parameter(name='year')}, type=StringType)
newClasses_Validator.methods={newClasses_Validator_m_validatePersonalNum, newClasses_Validator_m_checkDateOrder, newClasses_Validator_m_validateEmail, newClasses_Validator_m_validatePhoneNum, newClasses_Validator_m_validateDates, newClasses_Validator_m_checkAgeRestriction, newClasses_Validator_m_validateNames, newClasses_Validator_m_validateAddress, newClasses_Validator_m_validateConfirmationNum, newClasses_Validator_m_checkAge}

# newClasses_CustomerProvides class attributes and methods
newClasses_CustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='sum'), Parameter(name='firstName'), Parameter(name='ccv'), Parameter(name='expiryMonth'), Parameter(name='ccNumber')}, type=BooleanType)
newClasses_CustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='ccNumber'), Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='expiryMonth')}, type=BooleanType)
newClasses_CustomerProvides.methods={newClasses_CustomerProvides_m_isCreditCardValid, newClasses_CustomerProvides_m_makePayment}

# newClasses_Guest class attributes and methods
newClasses_Guest_checkInDate: Property = Property(name="checkInDate", type=StringType)
newClasses_Guest_checkOutDate: Property = Property(name="checkOutDate", type=StringType)
newClasses_Guest_roomNum: Property = Property(name="roomNum", type=StringType)
newClasses_Guest_checkedIn: Property = Property(name="checkedIn", type=StringType)
newClasses_Guest_checkedOut: Property = Property(name="checkedOut", type=StringType)
newClasses_Guest_addedServices: Property = Property(name="addedServices", type=StringType)
newClasses_Guest_extraDays: Property = Property(name="extraDays", type=StringType)
newClasses_Guest_cost: Property = Property(name="cost", type=StringType)
newClasses_Guest_bookingPaid: Property = Property(name="bookingPaid", type=StringType)
newClasses_Guest.attributes={newClasses_Guest_extraDays, newClasses_Guest_addedServices, newClasses_Guest_checkedOut, newClasses_Guest_cost, newClasses_Guest_checkInDate, newClasses_Guest_roomNum, newClasses_Guest_checkedIn, newClasses_Guest_checkOutDate, newClasses_Guest_bookingPaid}

# Customer class attributes and methods

# GuestBiller class attributes and methods

# GuestInterface class attributes and methods

# newClasses_GuestBiller class attributes and methods
newClasses_GuestBiller_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='lastName'), Parameter(name='year'), Parameter(name='cost'), Parameter(name='creditCardNum'), Parameter(name='cvc'), Parameter(name='roomNum'), Parameter(name='firstName'), Parameter(name='checkOutDate'), Parameter(name='month')}, type=StringType)
newClasses_GuestBiller_m_addServiceToBill: Method = Method(name="addServiceToBill", parameters={Parameter(name='type'), Parameter(name='guest')}, type=StringType)
newClasses_GuestBiller.methods={newClasses_GuestBiller_m_checkOut, newClasses_GuestBiller_m_addServiceToBill}

# newClasses_Room class attributes and methods
newClasses_Room_roomNum: Property = Property(name="roomNum", type=StringType)
newClasses_Room_status: Property = Property(name="status", type=StringType)
newClasses_Room.attributes={newClasses_Room_status, newClasses_Room_roomNum}

# RoomType class attributes and methods

# newClasses_InformationValidator class attributes and methods

# newClasses_ServiceHandler class attributes and methods

# ServiceHandlerInterface class attributes and methods

# newClasses_Service class attributes and methods
newClasses_Service_id: Property = Property(name="id", type=StringType)
newClasses_Service_status: Property = Property(name="status", type=StringType)
newClasses_Service.attributes={newClasses_Service_status, newClasses_Service_id}

# newClasses_GuestInterface class attributes and methods
newClasses_GuestInterface_m_extendStay: Method = Method(name="extendStay", parameters={Parameter(name='roomNum'), Parameter(name='guest'), Parameter(name='newCheckOutDate')})
newClasses_GuestInterface_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='checkInDate'), Parameter(name='conformationNum')}, type=StringType)
newClasses_GuestInterface_m_changeRoom: Method = Method(name="changeRoom", parameters={Parameter(name='guest'), Parameter(name='roomNum'), Parameter(name='newRoomType')})
newClasses_GuestInterface.methods={newClasses_GuestInterface_m_changeRoom, newClasses_GuestInterface_m_checkIn, newClasses_GuestInterface_m_extendStay}

# newClasses_RoomType class attributes and methods
newClasses_RoomType_type: Property = Property(name="type", type=StringType)
newClasses_RoomType_price: Property = Property(name="price", type=StringType)
newClasses_RoomType.attributes={newClasses_RoomType_type, newClasses_RoomType_price}

# newClasses_Manager class attributes and methods
newClasses_Manager_userName: Property = Property(name="userName", type=StringType)
newClasses_Manager_password: Property = Property(name="password", type=StringType)
newClasses_Manager.attributes={newClasses_Manager_password, newClasses_Manager_userName}

# ManagerInterface class attributes and methods

# RoomHandlerInterface class attributes and methods

# newClasses_RoomHandler class attributes and methods

# ServiceType class attributes and methods

# newClasses_ServiceType class attributes and methods
newClasses_ServiceType_type: Property = Property(name="type", type=StringType)
newClasses_ServiceType_price: Property = Property(name="price", type=StringType)
newClasses_ServiceType.attributes={newClasses_ServiceType_type, newClasses_ServiceType_price}

# newClasses_ServiceHandlerInterface class attributes and methods
newClasses_ServiceHandlerInterface_m_changeServiceType: Method = Method(name="changeServiceType", parameters={Parameter(name='newType'), Parameter(name='ID')})
newClasses_ServiceHandlerInterface_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='ID')})
newClasses_ServiceHandlerInterface_m_changeServicePrice: Method = Method(name="changeServicePrice", parameters={Parameter(name='newPrice'), Parameter(name='ID')})
newClasses_ServiceHandlerInterface_m_addService: Method = Method(name="addService", parameters={Parameter(name='ID'), Parameter(name='type'), Parameter(name='price')})
newClasses_ServiceHandlerInterface.methods={newClasses_ServiceHandlerInterface_m_changeServiceType, newClasses_ServiceHandlerInterface_m_addService, newClasses_ServiceHandlerInterface_m_removeService, newClasses_ServiceHandlerInterface_m_changeServicePrice}

# newClasses_RoomHandlerInterface class attributes and methods
newClasses_RoomHandlerInterface_m_changeRoomType: Method = Method(name="changeRoomType", parameters={Parameter(name='roomNum'), Parameter(name='roomType')})
newClasses_RoomHandlerInterface_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='roomNum')})
newClasses_RoomHandlerInterface_m_changeRoomPrice: Method = Method(name="changeRoomPrice", parameters={Parameter(name='roomNum'), Parameter(name='newPrice')})
newClasses_RoomHandlerInterface_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='price'), Parameter(name='roomNum'), Parameter(name='roomType')})
newClasses_RoomHandlerInterface.methods={newClasses_RoomHandlerInterface_m_addRoom, newClasses_RoomHandlerInterface_m_changeRoomPrice, newClasses_RoomHandlerInterface_m_changeRoomType, newClasses_RoomHandlerInterface_m_removeRoom}

# newClasses_BankComponent class attributes and methods

# AdministratorProvides class attributes and methods

# newClasses_AdministratorProvides class attributes and methods
newClasses_AdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='expiryYear'), Parameter(name='ccv'), Parameter(name='ccNumber'), Parameter(name='expiryMonth'), Parameter(name='sum')}, type=FloatType)
newClasses_AdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='expiryYear'), Parameter(name='ccv'), Parameter(name='expiryMonth'), Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='lastName')}, type=BooleanType)
newClasses_AdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='ccNumber'), Parameter(name='firstName'), Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='expiryMonth')}, type=BooleanType)
newClasses_AdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='expiryYear'), Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='ccv'), Parameter(name='expiryMonth'), Parameter(name='firstName')}, type=FloatType)
newClasses_AdministratorProvides.methods={newClasses_AdministratorProvides_m_addCreditCard, newClasses_AdministratorProvides_m_getBalance, newClasses_AdministratorProvides_m_removeCreditCard, newClasses_AdministratorProvides_m_makeDeposit}

# newClasses_ManagerInterface class attributes and methods
newClasses_ManagerInterface_m_logout: Method = Method(name="logout", parameters={})
newClasses_ManagerInterface_m_login: Method = Method(name="login", parameters={Parameter(name='userName'), Parameter(name='password')})
newClasses_ManagerInterface_m_validateLogin: Method = Method(name="validateLogin", parameters={Parameter(name='password'), Parameter(name='userName')}, type=StringType)
newClasses_ManagerInterface_m_SessionData: Method = Method(name="SessionData", parameters={})
newClasses_ManagerInterface.methods={newClasses_ManagerInterface_m_login, newClasses_ManagerInterface_m_SessionData, newClasses_ManagerInterface_m_logout, newClasses_ManagerInterface_m_validateLogin}

# newClasses_Billing class attributes and methods
newClasses_Billing_totalCost: Property = Property(name="totalCost", type=StringType)
newClasses_Billing_isPaid: Property = Property(name="isPaid", type=StringType)
newClasses_Billing.attributes={newClasses_Billing_totalCost, newClasses_Billing_isPaid}

# newClasses_LoginChecker class attributes and methods

# Relationships
booking0: BinaryAssociation = BinaryAssociation(
    name="booking0",
    ends={
        Property(name="newClasses_Booking", type=newClasses_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Customer", type=newClasses_Booking, multiplicity=Multiplicity(1, 1))
    }
)
databaseHandler5: BinaryAssociation = BinaryAssociation(
    name="databaseHandler5",
    ends={
        Property(name="newClasses_Database", type=newClasses_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Booking6", type=newClasses_Database, multiplicity=Multiplicity(1, 1))
    }
)
creditCard1: BinaryAssociation = BinaryAssociation(
    name="creditCard1",
    ends={
        Property(name="newClasses_CreditCard", type=newClasses_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Customer2", type=newClasses_CreditCard, multiplicity=Multiplicity(1, 1))
    }
)
receiptCreator3: BinaryAssociation = BinaryAssociation(
    name="receiptCreator3",
    ends={
        Property(name="newClasses_ReceiptCreator", type=newClasses_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Booking4", type=newClasses_ReceiptCreator, multiplicity=Multiplicity(1, 1))
    }
)
service7: BinaryAssociation = BinaryAssociation(
    name="service7",
    ends={
        Property(name="newClasses_Service", type=newClasses_ServiceHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_ServiceHandler", type=newClasses_Service, multiplicity=Multiplicity(1, 1))
    }
)
roomHandler8: BinaryAssociation = BinaryAssociation(
    name="roomHandler8",
    ends={
        Property(name="newClasses_RoomHandler", type=newClasses_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Manager", type=newClasses_RoomHandler, multiplicity=Multiplicity(1, 1))
    }
)
serviceHandler9: BinaryAssociation = BinaryAssociation(
    name="serviceHandler9",
    ends={
        Property(name="newClasses_ServiceHandler11", type=newClasses_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_Manager10", type=newClasses_ServiceHandler, multiplicity=Multiplicity(1, 1))
    }
)
room12: BinaryAssociation = BinaryAssociation(
    name="room12",
    ends={
        Property(name="newClasses_Room", type=newClasses_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_RoomHandler13", type=newClasses_Room, multiplicity=Multiplicity(1, 1))
    }
)
database14: BinaryAssociation = BinaryAssociation(
    name="database14",
    ends={
        Property(name="newClasses_Database16", type=newClasses_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_RoomHandler15", type=newClasses_Database, multiplicity=Multiplicity(1, 1))
    }
)
manager17: BinaryAssociation = BinaryAssociation(
    name="manager17",
    ends={
        Property(name="newClasses_Manager18", type=newClasses_LoginChecker, multiplicity=Multiplicity(1, 1)),
        Property(name="newClasses_LoginChecker", type=newClasses_Manager, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_newClasses_Customer_Booker = Generalization(general=Booker, specific=newClasses_Customer)
gen_newClasses_Booking_RoomProvider = Generalization(general=RoomProvider, specific=newClasses_Booking)
gen_newClasses_Booking_Biller = Generalization(general=Biller, specific=newClasses_Booking)
gen_newClasses_Booking_Booker = Generalization(general=Booker, specific=newClasses_Booking)
gen_newClasses_Booking_ServiceProvider = Generalization(general=ServiceProvider, specific=newClasses_Booking)
gen_newClasses_Booking_Validator = Generalization(general=Validator, specific=newClasses_Booking)
gen_newClasses_Booking_CustomerProvides = Generalization(general=CustomerProvides, specific=newClasses_Booking)
gen_newClasses_ReceiptCreator_Receipt = Generalization(general=Receipt, specific=newClasses_ReceiptCreator)
gen_newClasses_Database_DB_interface = Generalization(general=DB_interface, specific=newClasses_Database)
gen_newClasses_Guest_Customer = Generalization(general=Customer, specific=newClasses_Guest)
gen_newClasses_Guest_GuestBiller = Generalization(general=GuestBiller, specific=newClasses_Guest)
gen_newClasses_Guest_GuestInterface = Generalization(general=GuestInterface, specific=newClasses_Guest)
gen_newClasses_Room_RoomType = Generalization(general=RoomType, specific=newClasses_Room)
gen_newClasses_InformationValidator_Validator = Generalization(general=Validator, specific=newClasses_InformationValidator)
gen_newClasses_ServiceHandler_ServiceProvider = Generalization(general=ServiceProvider, specific=newClasses_ServiceHandler)
gen_newClasses_ServiceHandler_ServiceHandlerInterface = Generalization(general=ServiceHandlerInterface, specific=newClasses_ServiceHandler)
gen_newClasses_Manager_ManagerInterface = Generalization(general=ManagerInterface, specific=newClasses_Manager)
gen_newClasses_Manager_RoomHandlerInterface = Generalization(general=RoomHandlerInterface, specific=newClasses_Manager)
gen_newClasses_Manager_ServiceHandlerInterface = Generalization(general=ServiceHandlerInterface, specific=newClasses_Manager)
gen_newClasses_Service_ServiceType = Generalization(general=ServiceType, specific=newClasses_Service)
gen_newClasses_RoomHandler_RoomProvider = Generalization(general=RoomProvider, specific=newClasses_RoomHandler)
gen_newClasses_RoomHandler_RoomHandlerInterface = Generalization(general=RoomHandlerInterface, specific=newClasses_RoomHandler)
gen_newClasses_RoomHandler_GuestInterface = Generalization(general=GuestInterface, specific=newClasses_RoomHandler)
gen_newClasses_Billing_Biller = Generalization(general=Biller, specific=newClasses_Billing)
gen_newClasses_Billing_CustomerProvides = Generalization(general=CustomerProvides, specific=newClasses_Billing)
gen_newClasses_Billing_GuestBiller = Generalization(general=GuestBiller, specific=newClasses_Billing)
gen_newClasses_BankComponent_CustomerProvides = Generalization(general=CustomerProvides, specific=newClasses_BankComponent)
gen_newClasses_BankComponent_AdministratorProvides = Generalization(general=AdministratorProvides, specific=newClasses_BankComponent)
gen_newClasses_LoginChecker_ManagerInterface = Generalization(general=ManagerInterface, specific=newClasses_LoginChecker)

# Domain Model
domain_model = DomainModel(
    name="newClasses",
    types={newClasses_Customer, newClasses_Booking, Booker, newClasses_Database, Receipt, newClasses_CreditCard, RoomProvider, Biller, ServiceProvider, Validator, CustomerProvides, newClasses_ReceiptCreator, newClasses_RoomProvider, newClasses_Receipt, DB_interface, newClasses_DB_interface, newClasses_Biller, newClasses_ServiceProvider, newClasses_Booker, newClasses_Validator, newClasses_CustomerProvides, newClasses_Guest, Customer, GuestBiller, GuestInterface, newClasses_GuestBiller, newClasses_Room, RoomType, newClasses_InformationValidator, newClasses_ServiceHandler, ServiceHandlerInterface, newClasses_Service, newClasses_GuestInterface, newClasses_RoomType, newClasses_Manager, ManagerInterface, RoomHandlerInterface, newClasses_RoomHandler, ServiceType, newClasses_ServiceType, newClasses_ServiceHandlerInterface, newClasses_RoomHandlerInterface, newClasses_BankComponent, AdministratorProvides, newClasses_AdministratorProvides, newClasses_ManagerInterface, newClasses_Billing, newClasses_LoginChecker},
    associations={booking0, databaseHandler5, creditCard1, receiptCreator3, service7, roomHandler8, serviceHandler9, room12, database14, manager17},
    generalizations={gen_newClasses_Customer_Booker, gen_newClasses_Booking_RoomProvider, gen_newClasses_Booking_Biller, gen_newClasses_Booking_Booker, gen_newClasses_Booking_ServiceProvider, gen_newClasses_Booking_Validator, gen_newClasses_Booking_CustomerProvides, gen_newClasses_ReceiptCreator_Receipt, gen_newClasses_Database_DB_interface, gen_newClasses_Guest_Customer, gen_newClasses_Guest_GuestBiller, gen_newClasses_Guest_GuestInterface, gen_newClasses_Room_RoomType, gen_newClasses_InformationValidator_Validator, gen_newClasses_ServiceHandler_ServiceProvider, gen_newClasses_ServiceHandler_ServiceHandlerInterface, gen_newClasses_Manager_ManagerInterface, gen_newClasses_Manager_RoomHandlerInterface, gen_newClasses_Manager_ServiceHandlerInterface, gen_newClasses_Service_ServiceType, gen_newClasses_RoomHandler_RoomProvider, gen_newClasses_RoomHandler_RoomHandlerInterface, gen_newClasses_RoomHandler_GuestInterface, gen_newClasses_Billing_Biller, gen_newClasses_Billing_CustomerProvides, gen_newClasses_Billing_GuestBiller, gen_newClasses_BankComponent_CustomerProvides, gen_newClasses_BankComponent_AdministratorProvides, gen_newClasses_LoginChecker_ManagerInterface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)