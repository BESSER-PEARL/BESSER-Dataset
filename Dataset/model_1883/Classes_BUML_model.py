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

# Enumerations
RoomStatus: Enumeration = Enumeration(
    name="RoomStatus",
    literals={
            EnumerationLiteral(name="Occupied"),
			EnumerationLiteral(name="Available"),
			EnumerationLiteral(name="Cleaning"),
			EnumerationLiteral(name="Maintenance")
    }
)

RoomTypeName: Enumeration = Enumeration(
    name="RoomTypeName",
    literals={
            EnumerationLiteral(name="SingleRoom"),
			EnumerationLiteral(name="DoubleRoom"),
			EnumerationLiteral(name="FamilySuite")
    }
)

ChargeType: Enumeration = Enumeration(
    name="ChargeType",
    literals={
            EnumerationLiteral(name="CancellationFee"),
			EnumerationLiteral(name="Breakfast"),
			EnumerationLiteral(name="SingleRoom"),
			EnumerationLiteral(name="DoubleRoom"),
			EnumerationLiteral(name="FamilySuite"),
			EnumerationLiteral(name="LateCheckOutFee")
    }
)

# Classes
Classes_RoomType = Class(name="Classes::RoomType")
Classes_Booking = Class(name="Classes::Booking")
Classes_IBookingManagementImpl = Class(name="Classes::IBookingManagementImpl")
Classes_Room = Class(name="Classes::Room")
Classes_Customer = Class(name="Classes::Customer")
Classes_Bill = Class(name="Classes::Bill")
IPerson = Class(name="IPerson")
IBookingManagement = Class(name="IBookingManagement")
Classes_IHotelManagerImpl = Class(name="Classes::IHotelManagerImpl")
Classes_IFinanceImpl = Class(name="Classes::IFinanceImpl")
IHotelManager = Class(name="IHotelManager")
Classes_StaffMember = Class(name="Classes::StaffMember")
Classes_IPerson = Class(name="Classes::IPerson", is_abstract=True)
Classes_IHotelManager = Class(name="Classes::IHotelManager", is_abstract=True)
IFinance = Class(name="IFinance")
Classes_CustomerProvides = Class(name="Classes::CustomerProvides", is_abstract=True)
Classes_IFinance = Class(name="Classes::IFinance", is_abstract=True)
Classes_IBookingManagement = Class(name="Classes::IBookingManagement", is_abstract=True)
Classes_Charge = Class(name="Classes::Charge")
Classes_AdministratorProvides = Class(name="Classes::AdministratorProvides", is_abstract=True)

# Classes_RoomType class attributes and methods
Classes_RoomType_roomTypeName: Property = Property(name="roomTypeName", type=StringType)
Classes_RoomType_features: Property = Property(name="features", type=StringType)
Classes_RoomType_numberOfGuests: Property = Property(name="numberOfGuests", type=StringType)
Classes_RoomType_description: Property = Property(name="description", type=StringType)
Classes_RoomType_price: Property = Property(name="price", type=StringType)
Classes_RoomType.attributes={Classes_RoomType_roomTypeName, Classes_RoomType_price, Classes_RoomType_description, Classes_RoomType_numberOfGuests, Classes_RoomType_features}

# Classes_Booking class attributes and methods
Classes_Booking_checkIn: Property = Property(name="checkIn", type=DateType)
Classes_Booking_checkOut: Property = Property(name="checkOut", type=DateType)
Classes_Booking_bookingID: Property = Property(name="bookingID", type=StringType)
Classes_Booking_numberOfGuests: Property = Property(name="numberOfGuests", type=StringType)
Classes_Booking.attributes={Classes_Booking_checkOut, Classes_Booking_bookingID, Classes_Booking_numberOfGuests, Classes_Booking_checkIn}

# Classes_IBookingManagementImpl class attributes and methods

# Classes_Room class attributes and methods
Classes_Room_status: Property = Property(name="status", type=StringType)
Classes_Room_roomNumber: Property = Property(name="roomNumber", type=StringType)
Classes_Room.attributes={Classes_Room_status, Classes_Room_roomNumber}

# Classes_Customer class attributes and methods

# Classes_Bill class attributes and methods

# IPerson class attributes and methods

# IBookingManagement class attributes and methods

# Classes_IHotelManagerImpl class attributes and methods

# Classes_IFinanceImpl class attributes and methods

# IHotelManager class attributes and methods

# Classes_StaffMember class attributes and methods
Classes_StaffMember_admin: Property = Property(name="admin", type=StringType)
Classes_StaffMember_username: Property = Property(name="username", type=StringType)
Classes_StaffMember_password: Property = Property(name="password", type=StringType)
Classes_StaffMember_isLoggedIn: Property = Property(name="isLoggedIn", type=BooleanType)
Classes_StaffMember.attributes={Classes_StaffMember_username, Classes_StaffMember_isLoggedIn, Classes_StaffMember_password, Classes_StaffMember_admin}

# Classes_IPerson class attributes and methods
Classes_IPerson_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Classes_IPerson_firstName: Property = Property(name="firstName", type=StringType)
Classes_IPerson_lastName: Property = Property(name="lastName", type=StringType)
Classes_IPerson_address: Property = Property(name="address", type=StringType)
Classes_IPerson_email: Property = Property(name="email", type=StringType)
Classes_IPerson.attributes={Classes_IPerson_firstName, Classes_IPerson_email, Classes_IPerson_lastName, Classes_IPerson_address, Classes_IPerson_phoneNumber}

# Classes_IHotelManager class attributes and methods
Classes_IHotelManager_m_isPasswordSecure: Method = Method(name="isPasswordSecure", parameters={Parameter(name='password')}, type=BooleanType)
Classes_IHotelManager_m_isValidUsername: Method = Method(name="isValidUsername", parameters={Parameter(name='username')}, type=BooleanType)
Classes_IHotelManager_m_isStaffMemberLoggedIn: Method = Method(name="isStaffMemberLoggedIn", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_isStaffMemberAdmin: Method = Method(name="isStaffMemberAdmin", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberPassword: Method = Method(name="getStaffMemberPassword", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberFirstName: Method = Method(name="getStaffMemberFirstName", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberLastName: Method = Method(name="getStaffMemberLastName", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_login: Method = Method(name="login", parameters={Parameter(name='password'), Parameter(name='username')}, type=BooleanType)
Classes_IHotelManager_m_addStaffMember: Method = Method(name="addStaffMember", parameters={Parameter(name='username'), Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='admin'), Parameter(name='phoneNumber'), Parameter(name='email'), Parameter(name='adminUsername'), Parameter(name='address'), Parameter(name='password')}, type=BooleanType)
Classes_IHotelManager_m_changeStatusOfRoom: Method = Method(name="changeStatusOfRoom", parameters={Parameter(name='roomID'), Parameter(name='staffMemberUsername'), Parameter(name='status')}, type=StringType)
Classes_IHotelManager_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='staffMemberUsername'), Parameter(name='bookingID')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberEmail: Method = Method(name="getStaffMemberEmail", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberPhoneNumber: Method = Method(name="getStaffMemberPhoneNumber", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_getStaffMemberAddress: Method = Method(name="getStaffMemberAddress", parameters={Parameter(name='username')}, type=StringType)
Classes_IHotelManager_m_logout: Method = Method(name="logout", parameters={Parameter(name='username')}, type=BooleanType)
Classes_IHotelManager_m_checkInBooking: Method = Method(name="checkInBooking", parameters={Parameter(name='bookingID'), Parameter(name='staffMemberUsername')}, type=StringType)
Classes_IHotelManager.methods={Classes_IHotelManager_m_isStaffMemberAdmin, Classes_IHotelManager_m_getStaffMemberLastName, Classes_IHotelManager_m_getStaffMemberFirstName, Classes_IHotelManager_m_login, Classes_IHotelManager_m_getStaffMemberEmail, Classes_IHotelManager_m_isPasswordSecure, Classes_IHotelManager_m_getStaffMemberPhoneNumber, Classes_IHotelManager_m_logout, Classes_IHotelManager_m_changeStatusOfRoom, Classes_IHotelManager_m_checkInBooking, Classes_IHotelManager_m_getStaffMemberPassword, Classes_IHotelManager_m_checkOut, Classes_IHotelManager_m_isStaffMemberLoggedIn, Classes_IHotelManager_m_getStaffMemberAddress, Classes_IHotelManager_m_addStaffMember, Classes_IHotelManager_m_isValidUsername}

# IFinance class attributes and methods

# Classes_CustomerProvides class attributes and methods
Classes_CustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='ccNumber'), Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='firstName'), Parameter(name='sum'), Parameter(name='ccv'), Parameter(name='lastName')}, type=BooleanType)
Classes_CustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='lastName'), Parameter(name='ccv'), Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='firstName'), Parameter(name='ccNumber')}, type=BooleanType)
Classes_CustomerProvides.methods={Classes_CustomerProvides_m_isCreditCardValid, Classes_CustomerProvides_m_makePayment}

# Classes_IFinance class attributes and methods
Classes_IFinance_m_calculatePayment: Method = Method(name="calculatePayment", parameters={Parameter(name='bookingID')}, type=IntegerType)
Classes_IFinance_m_payBill: Method = Method(name="payBill", parameters={Parameter(name='ccv'), Parameter(name='ccNumber'), Parameter(name='cost'), Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='bookingID'), Parameter(name='firstName'), Parameter(name='expiryYear')}, type=StringType)
Classes_IFinance_m_bankSendInvoice: Method = Method(name="bankSendInvoice", parameters={})
Classes_IFinance.methods={Classes_IFinance_m_calculatePayment, Classes_IFinance_m_payBill, Classes_IFinance_m_bankSendInvoice}

# Classes_IBookingManagement class attributes and methods
Classes_IBookingManagement_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_IBookingManagement_m_searchRoom: Method = Method(name="searchRoom", parameters={Parameter(name='numberOfGuests'), Parameter(name='maximumPrice'), Parameter(name='checkOut'), Parameter(name='roomType'), Parameter(name='checkIn')}, type=StringType)
Classes_IBookingManagement_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_IBookingManagement_m_addCustomerInformationToBooking: Method = Method(name="addCustomerInformationToBooking", parameters={Parameter(name='ph'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='email'), Parameter(name='bookingID')}, type=BooleanType)
Classes_IBookingManagement_m_updateBooking: Method = Method(name="updateBooking", parameters={Parameter(name='checkOut'), Parameter(name='checkIn'), Parameter(name='roomID'), Parameter(name='nrOfGuests'), Parameter(name='bookingID')}, type=StringType)
Classes_IBookingManagement_m_addRoomPending: Method = Method(name="addRoomPending", parameters={Parameter(name='bookingID'), Parameter(name='room')}, type=StringType)
Classes_IBookingManagement_m_getRoomsOfBooking: Method = Method(name="getRoomsOfBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_IBookingManagement_m_createPendingBooking: Method = Method(name="createPendingBooking", parameters={Parameter(name='checkOut'), Parameter(name='checkIn'), Parameter(name='guestCount')}, type=IntegerType)
Classes_IBookingManagement_m_sendConfirmation: Method = Method(name="sendConfirmation", parameters={Parameter(name='message'), Parameter(name='bookingID')}, type=StringType)
Classes_IBookingManagement_m_addExtraCharge: Method = Method(name="addExtraCharge", parameters={Parameter(name='charge'), Parameter(name='bookingID'), Parameter(name='quantity')}, type=StringType)
Classes_IBookingManagement.methods={Classes_IBookingManagement_m_getRoomsOfBooking, Classes_IBookingManagement_m_sendConfirmation, Classes_IBookingManagement_m_searchRoom, Classes_IBookingManagement_m_addRoomPending, Classes_IBookingManagement_m_updateBooking, Classes_IBookingManagement_m_confirmBooking, Classes_IBookingManagement_m_addExtraCharge, Classes_IBookingManagement_m_createPendingBooking, Classes_IBookingManagement_m_cancelBooking, Classes_IBookingManagement_m_addCustomerInformationToBooking}

# Classes_Charge class attributes and methods
Classes_Charge_amount: Property = Property(name="amount", type=IntegerType)
Classes_Charge_date: Property = Property(name="date", type=DateType)
Classes_Charge_chargeType: Property = Property(name="chargeType", type=StringType)
Classes_Charge.attributes={Classes_Charge_amount, Classes_Charge_date, Classes_Charge_chargeType}

# Classes_AdministratorProvides class attributes and methods
Classes_AdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='expiryMonth'), Parameter(name='lastName'), Parameter(name='expiryYear'), Parameter(name='ccv'), Parameter(name='ccNumber'), Parameter(name='firstName')}, type=BooleanType)
Classes_AdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='ccNumber')}, type=FloatType)
Classes_AdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='ccv'), Parameter(name='sum'), Parameter(name='firstName')}, type=FloatType)
Classes_AdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='ccNumber'), Parameter(name='expiryYear')}, type=BooleanType)
Classes_AdministratorProvides.methods={Classes_AdministratorProvides_m_makeDeposit, Classes_AdministratorProvides_m_removeCreditCard, Classes_AdministratorProvides_m_addCreditCard, Classes_AdministratorProvides_m_getBalance}

# Relationships
roomType0: BinaryAssociation = BinaryAssociation(
    name="roomType0",
    ends={
        Property(name="RoomType", type=Classes_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room", type=Classes_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
bookings1: BinaryAssociation = BinaryAssociation(
    name="bookings1",
    ends={
        Property(name="Booking", type=Classes_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="rooms", type=Classes_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
iBookingManagementImpl2: BinaryAssociation = BinaryAssociation(
    name="iBookingManagementImpl2",
    ends={
        Property(name="IBookingManagementImpl", type=Classes_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="room3", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1))
    }
)
customer5: BinaryAssociation = BinaryAssociation(
    name="customer5",
    ends={
        Property(name="Customer", type=Classes_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="booking", type=Classes_Customer, multiplicity=Multiplicity(1, 1))
    }
)
iBookingManagementImpl6: BinaryAssociation = BinaryAssociation(
    name="iBookingManagementImpl6",
    ends={
        Property(name="IBookingManagementImpl7", type=Classes_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="confirmedBookings", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1))
    }
)
bill8: BinaryAssociation = BinaryAssociation(
    name="bill8",
    ends={
        Property(name="Classes_Bill", type=Classes_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Booking", type=Classes_Bill, multiplicity=Multiplicity(1, 1))
    }
)
rooms9: BinaryAssociation = BinaryAssociation(
    name="rooms9",
    ends={
        Property(name="Room10", type=Classes_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookings", type=Classes_Room, multiplicity=Multiplicity(0, 9999))
    }
)
room4: BinaryAssociation = BinaryAssociation(
    name="room4",
    ends={
        Property(name="Room", type=Classes_RoomType, multiplicity=Multiplicity(1, 1)),
        Property(name="roomType", type=Classes_Room, multiplicity=Multiplicity(0, 9999))
    }
)
customer13: BinaryAssociation = BinaryAssociation(
    name="customer13",
    ends={
        Property(name="Classes_Customer", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_IBookingManagementImpl", type=Classes_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
room14: BinaryAssociation = BinaryAssociation(
    name="room14",
    ends={
        Property(name="Room15", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iBookingManagementImpl", type=Classes_Room, multiplicity=Multiplicity(0, 9999))
    }
)
pendingBookings16: BinaryAssociation = BinaryAssociation(
    name="pendingBookings16",
    ends={
        Property(name="Classes_Booking18", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_IBookingManagementImpl17", type=Classes_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
iHotelManagerImpl19: BinaryAssociation = BinaryAssociation(
    name="iHotelManagerImpl19",
    ends={
        Property(name="IHotelManagerImpl", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iBookingManagementImpl20", type=Classes_IHotelManagerImpl, multiplicity=Multiplicity(1, 1))
    }
)
bookingHistory21: BinaryAssociation = BinaryAssociation(
    name="bookingHistory21",
    ends={
        Property(name="Classes_Booking23", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_IBookingManagementImpl22", type=Classes_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
iFinanceImpl24: BinaryAssociation = BinaryAssociation(
    name="iFinanceImpl24",
    ends={
        Property(name="IFinanceImpl", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iBookingManagementImpl25", type=Classes_IFinanceImpl, multiplicity=Multiplicity(1, 1))
    }
)
confirmedBookings26: BinaryAssociation = BinaryAssociation(
    name="confirmedBookings26",
    ends={
        Property(name="Booking28", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iBookingManagementImpl27", type=Classes_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
staff29: BinaryAssociation = BinaryAssociation(
    name="staff29",
    ends={
        Property(name="Classes_StaffMember", type=Classes_IHotelManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_IHotelManagerImpl", type=Classes_StaffMember, multiplicity=Multiplicity(0, 9999))
    }
)
booking11: BinaryAssociation = BinaryAssociation(
    name="booking11",
    ends={
        Property(name="Booking12", type=Classes_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=Classes_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
iBookingManagementImpl30: BinaryAssociation = BinaryAssociation(
    name="iBookingManagementImpl30",
    ends={
        Property(name="IBookingManagementImpl31", type=Classes_IHotelManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iHotelManagerImpl", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1))
    }
)
customerProvides32: BinaryAssociation = BinaryAssociation(
    name="customerProvides32",
    ends={
        Property(name="Classes_CustomerProvides", type=Classes_IFinanceImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_IFinanceImpl", type=Classes_CustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
iBookingManagementImpl33: BinaryAssociation = BinaryAssociation(
    name="iBookingManagementImpl33",
    ends={
        Property(name="IBookingManagementImpl34", type=Classes_IFinanceImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="iFinanceImpl", type=Classes_IBookingManagementImpl, multiplicity=Multiplicity(1, 1))
    }
)
charge35: BinaryAssociation = BinaryAssociation(
    name="charge35",
    ends={
        Property(name="Classes_Charge", type=Classes_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bill36", type=Classes_Charge, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_Classes_Customer_IPerson = Generalization(general=IPerson, specific=Classes_Customer)
gen_Classes_IBookingManagementImpl_IBookingManagement = Generalization(general=IBookingManagement, specific=Classes_IBookingManagementImpl)
gen_Classes_IHotelManagerImpl_IHotelManager = Generalization(general=IHotelManager, specific=Classes_IHotelManagerImpl)
gen_Classes_StaffMember_IPerson = Generalization(general=IPerson, specific=Classes_StaffMember)
gen_Classes_IFinanceImpl_IFinance = Generalization(general=IFinance, specific=Classes_IFinanceImpl)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Classes_RoomType, Classes_Booking, Classes_IBookingManagementImpl, Classes_Room, Classes_Customer, Classes_Bill, IPerson, IBookingManagement, Classes_IHotelManagerImpl, Classes_IFinanceImpl, IHotelManager, Classes_StaffMember, Classes_IPerson, Classes_IHotelManager, IFinance, Classes_CustomerProvides, Classes_IFinance, Classes_IBookingManagement, Classes_Charge, Classes_AdministratorProvides, RoomStatus, RoomTypeName, ChargeType},
    associations={roomType0, bookings1, iBookingManagementImpl2, customer5, iBookingManagementImpl6, bill8, rooms9, room4, customer13, room14, pendingBookings16, iHotelManagerImpl19, bookingHistory21, iFinanceImpl24, confirmedBookings26, staff29, booking11, iBookingManagementImpl30, customerProvides32, iBookingManagementImpl33, charge35},
    generalizations={gen_Classes_Customer_IPerson, gen_Classes_IBookingManagementImpl_IBookingManagement, gen_Classes_IHotelManagerImpl_IHotelManager, gen_Classes_StaffMember_IPerson, gen_Classes_IFinanceImpl_IFinance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)