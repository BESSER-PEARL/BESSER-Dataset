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
EType: Enumeration = Enumeration(
    name="EType",
    literals={
            EnumerationLiteral(name="Receptionist"),
			EnumerationLiteral(name="Cleaner"),
			EnumerationLiteral(name="Manager")
    }
)

RoomType: Enumeration = Enumeration(
    name="RoomType",
    literals={
            EnumerationLiteral(name="Handicapable"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Suite")
    }
)

# Classes
HotelManagementClassDiagram_EmployeeType = Class(name="HotelManagementClassDiagram::EmployeeType")
HotelManagementClassDiagram_Employee = Class(name="HotelManagementClassDiagram::Employee")
Person = Class(name="Person")
HotelManagementClassDiagram_Person = Class(name="HotelManagementClassDiagram::Person", is_abstract=True)
HotelManagementClassDiagram_Booking = Class(name="HotelManagementClassDiagram::Booking")
HotelManagementClassDiagram_Discount = Class(name="HotelManagementClassDiagram::Discount")
HotelManagementClassDiagram_Creditcard = Class(name="HotelManagementClassDiagram::Creditcard")
HotelManagementClassDiagram_Customer = Class(name="HotelManagementClassDiagram::Customer")
HotelManagementClassDiagram_Addon = Class(name="HotelManagementClassDiagram::Addon")
HotelManagementClassDiagram_Room = Class(name="HotelManagementClassDiagram::Room")
HotelManagementClassDiagram_Bill = Class(name="HotelManagementClassDiagram::Bill")
HotelManagementClassDiagram_Costable = Class(name="HotelManagementClassDiagram::Costable", is_abstract=True)
HotelManagementClassDiagram_BookingController = Class(name="HotelManagementClassDiagram::BookingController")
HotelManagementClassDiagram_ManagementController = Class(name="HotelManagementClassDiagram::ManagementController")
HotelManagementClassDiagram_MaintenanceController = Class(name="HotelManagementClassDiagram::MaintenanceController")
HotelManagementClassDiagram_Hotel = Class(name="HotelManagementClassDiagram::Hotel")
HotelManagementClassDiagram_BookedRoom = Class(name="HotelManagementClassDiagram::BookedRoom")
Room = Class(name="Room")
HotelManagementClassDiagram_Interaction3 = Class(name="HotelManagementClassDiagram::Interaction3")
HotelManagementClassDiagram_Interaction1 = Class(name="HotelManagementClassDiagram::Interaction1")
HotelManagementClassDiagram_Interaction2 = Class(name="HotelManagementClassDiagram::Interaction2")
HotelManagementClassDiagram_Interaction4 = Class(name="HotelManagementClassDiagram::Interaction4")
HotelManagementClassDiagram_Interaction5 = Class(name="HotelManagementClassDiagram::Interaction5")

# HotelManagementClassDiagram_EmployeeType class attributes and methods
HotelManagementClassDiagram_EmployeeType_type: Property = Property(name="type", type=StringType)
HotelManagementClassDiagram_EmployeeType_acessLevel: Property = Property(name="acessLevel", type=IntegerType)
HotelManagementClassDiagram_EmployeeType.attributes={HotelManagementClassDiagram_EmployeeType_type, HotelManagementClassDiagram_EmployeeType_acessLevel}

# HotelManagementClassDiagram_Employee class attributes and methods
HotelManagementClassDiagram_Employee_employeeID: Property = Property(name="employeeID", type=IntegerType)
HotelManagementClassDiagram_Employee_workRate: Property = Property(name="workRate", type=IntegerType)
HotelManagementClassDiagram_Employee_salary: Property = Property(name="salary", type=FloatType)
HotelManagementClassDiagram_Employee_m_Booking: Method = Method(name="Booking", parameters={})
HotelManagementClassDiagram_Employee_m_Boolean: Method = Method(name="Boolean", parameters={})
HotelManagementClassDiagram_Employee_m_roomTypes: Method = Method(name="roomTypes", parameters={})
HotelManagementClassDiagram_Employee.attributes={HotelManagementClassDiagram_Employee_salary, HotelManagementClassDiagram_Employee_employeeID, HotelManagementClassDiagram_Employee_workRate}
HotelManagementClassDiagram_Employee.methods={HotelManagementClassDiagram_Employee_m_roomTypes, HotelManagementClassDiagram_Employee_m_Boolean, HotelManagementClassDiagram_Employee_m_Booking}

# Person class attributes and methods

# HotelManagementClassDiagram_Person class attributes and methods
HotelManagementClassDiagram_Person_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Person_SSNumber: Property = Property(name="SSNumber", type=StringType)
HotelManagementClassDiagram_Person_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
HotelManagementClassDiagram_Person_street: Property = Property(name="street", type=StringType)
HotelManagementClassDiagram_Person_city: Property = Property(name="city", type=StringType)
HotelManagementClassDiagram_Person_postalCode: Property = Property(name="postalCode", type=StringType)
HotelManagementClassDiagram_Person_country: Property = Property(name="country", type=StringType)
HotelManagementClassDiagram_Person_gender: Property = Property(name="gender", type=StringType)
HotelManagementClassDiagram_Person_title: Property = Property(name="title", type=StringType)
HotelManagementClassDiagram_Person.attributes={HotelManagementClassDiagram_Person_gender, HotelManagementClassDiagram_Person_street, HotelManagementClassDiagram_Person_name, HotelManagementClassDiagram_Person_country, HotelManagementClassDiagram_Person_postalCode, HotelManagementClassDiagram_Person_title, HotelManagementClassDiagram_Person_phoneNumber, HotelManagementClassDiagram_Person_SSNumber, HotelManagementClassDiagram_Person_city}

# HotelManagementClassDiagram_Booking class attributes and methods
HotelManagementClassDiagram_Booking_bookingId: Property = Property(name="bookingId", type=IntegerType)
HotelManagementClassDiagram_Booking_startDate: Property = Property(name="startDate", type=DateType)
HotelManagementClassDiagram_Booking_endDate: Property = Property(name="endDate", type=DateType)
HotelManagementClassDiagram_Booking_created: Property = Property(name="created", type=DateType)
HotelManagementClassDiagram_Booking_internalComments: Property = Property(name="internalComments", type=StringType)
HotelManagementClassDiagram_Booking_externalComments: Property = Property(name="externalComments", type=StringType)
HotelManagementClassDiagram_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
HotelManagementClassDiagram_Booking_checkedOut: Property = Property(name="checkedOut", type=BooleanType)
HotelManagementClassDiagram_Booking_m_removeDiscount: Method = Method(name="removeDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Booking_m_checkIn: Method = Method(name="checkIn", parameters={})
HotelManagementClassDiagram_Booking_m_checkOut: Method = Method(name="checkOut", parameters={}, type=StringType)
HotelManagementClassDiagram_Booking_m_addAddon: Method = Method(name="addAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_Booking_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_Booking_m_removeAddon: Method = Method(name="removeAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_Booking_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_Booking_m_generateBill: Method = Method(name="generateBill", parameters={}, type=StringType)
HotelManagementClassDiagram_Booking_m_pay: Method = Method(name="pay", parameters={Parameter(name='bill')}, type=BooleanType)
HotelManagementClassDiagram_Booking_m_addDiscount: Method = Method(name="addDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Booking.attributes={HotelManagementClassDiagram_Booking_startDate, HotelManagementClassDiagram_Booking_externalComments, HotelManagementClassDiagram_Booking_checkedOut, HotelManagementClassDiagram_Booking_created, HotelManagementClassDiagram_Booking_bookingId, HotelManagementClassDiagram_Booking_internalComments, HotelManagementClassDiagram_Booking_endDate, HotelManagementClassDiagram_Booking_checkedIn}
HotelManagementClassDiagram_Booking.methods={HotelManagementClassDiagram_Booking_m_checkOut, HotelManagementClassDiagram_Booking_m_addDiscount, HotelManagementClassDiagram_Booking_m_removeAddon, HotelManagementClassDiagram_Booking_m_removeRoom, HotelManagementClassDiagram_Booking_m_removeDiscount, HotelManagementClassDiagram_Booking_m_addRoom, HotelManagementClassDiagram_Booking_m_pay, HotelManagementClassDiagram_Booking_m_checkIn, HotelManagementClassDiagram_Booking_m_addAddon, HotelManagementClassDiagram_Booking_m_generateBill}

# HotelManagementClassDiagram_Discount class attributes and methods
HotelManagementClassDiagram_Discount_isPercentage: Property = Property(name="isPercentage", type=StringType)
HotelManagementClassDiagram_Discount_amount: Property = Property(name="amount", type=FloatType)
HotelManagementClassDiagram_Discount.attributes={HotelManagementClassDiagram_Discount_isPercentage, HotelManagementClassDiagram_Discount_amount}

# HotelManagementClassDiagram_Creditcard class attributes and methods
HotelManagementClassDiagram_Creditcard_number: Property = Property(name="number", type=StringType)
HotelManagementClassDiagram_Creditcard_cvc: Property = Property(name="cvc", type=IntegerType)
HotelManagementClassDiagram_Creditcard_owner: Property = Property(name="owner", type=StringType)
HotelManagementClassDiagram_Creditcard_expirationMonth: Property = Property(name="expirationMonth", type=IntegerType)
HotelManagementClassDiagram_Creditcard_expirationDay: Property = Property(name="expirationDay", type=IntegerType)
HotelManagementClassDiagram_Creditcard.attributes={HotelManagementClassDiagram_Creditcard_expirationDay, HotelManagementClassDiagram_Creditcard_number, HotelManagementClassDiagram_Creditcard_cvc, HotelManagementClassDiagram_Creditcard_owner, HotelManagementClassDiagram_Creditcard_expirationMonth}

# HotelManagementClassDiagram_Customer class attributes and methods
HotelManagementClassDiagram_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
HotelManagementClassDiagram_Customer_bonusPoints: Property = Property(name="bonusPoints", type=IntegerType)
HotelManagementClassDiagram_Customer_miscInfo: Property = Property(name="miscInfo", type=StringType)
HotelManagementClassDiagram_Customer_rank: Property = Property(name="rank", type=FloatType)
HotelManagementClassDiagram_Customer_m_addBonusPoints: Method = Method(name="addBonusPoints", parameters={Parameter(name='bonusPoints')})
HotelManagementClassDiagram_Customer.attributes={HotelManagementClassDiagram_Customer_bonusPoints, HotelManagementClassDiagram_Customer_miscInfo, HotelManagementClassDiagram_Customer_rank, HotelManagementClassDiagram_Customer_customerID}
HotelManagementClassDiagram_Customer.methods={HotelManagementClassDiagram_Customer_m_addBonusPoints}

# HotelManagementClassDiagram_Addon class attributes and methods
HotelManagementClassDiagram_Addon_description: Property = Property(name="description", type=StringType)
HotelManagementClassDiagram_Addon_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Addon.attributes={HotelManagementClassDiagram_Addon_description, HotelManagementClassDiagram_Addon_name}

# HotelManagementClassDiagram_Room class attributes and methods
HotelManagementClassDiagram_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
HotelManagementClassDiagram_Room_size: Property = Property(name="size", type=FloatType)
HotelManagementClassDiagram_Room_internalComment: Property = Property(name="internalComment", type=StringType)
HotelManagementClassDiagram_Room_booked: Property = Property(name="booked", type=BooleanType)
HotelManagementClassDiagram_Room_maxNbrPeople: Property = Property(name="maxNbrPeople", type=IntegerType)
HotelManagementClassDiagram_Room_underCleaning: Property = Property(name="underCleaning", type=BooleanType)
HotelManagementClassDiagram_Room_underRepair: Property = Property(name="underRepair", type=BooleanType)
HotelManagementClassDiagram_Room_types: Property = Property(name="types", type=StringType)
HotelManagementClassDiagram_Room_roomName: Property = Property(name="roomName", type=StringType)
HotelManagementClassDiagram_Room.attributes={HotelManagementClassDiagram_Room_internalComment, HotelManagementClassDiagram_Room_booked, HotelManagementClassDiagram_Room_roomNumber, HotelManagementClassDiagram_Room_types, HotelManagementClassDiagram_Room_roomName, HotelManagementClassDiagram_Room_underCleaning, HotelManagementClassDiagram_Room_size, HotelManagementClassDiagram_Room_maxNbrPeople, HotelManagementClassDiagram_Room_underRepair}

# HotelManagementClassDiagram_Bill class attributes and methods
HotelManagementClassDiagram_Bill_totalPrice: Property = Property(name="totalPrice", type=FloatType)
HotelManagementClassDiagram_Bill_valueAddedTax: Property = Property(name="valueAddedTax", type=FloatType)
HotelManagementClassDiagram_Bill_final: Property = Property(name="final", type=BooleanType)
HotelManagementClassDiagram_Bill_paid: Property = Property(name="paid", type=BooleanType)
HotelManagementClassDiagram_Bill_m_addCostable: Method = Method(name="addCostable", parameters={Parameter(name='costable')})
HotelManagementClassDiagram_Bill.attributes={HotelManagementClassDiagram_Bill_valueAddedTax, HotelManagementClassDiagram_Bill_final, HotelManagementClassDiagram_Bill_totalPrice, HotelManagementClassDiagram_Bill_paid}
HotelManagementClassDiagram_Bill.methods={HotelManagementClassDiagram_Bill_m_addCostable}

# HotelManagementClassDiagram_Costable class attributes and methods
HotelManagementClassDiagram_Costable_price: Property = Property(name="price", type=FloatType)
HotelManagementClassDiagram_Costable_m_addDiscount: Method = Method(name="addDiscount", parameters={})
HotelManagementClassDiagram_Costable_m_removeDiscount: Method = Method(name="removeDiscount", parameters={})
HotelManagementClassDiagram_Costable.attributes={HotelManagementClassDiagram_Costable_price}
HotelManagementClassDiagram_Costable.methods={HotelManagementClassDiagram_Costable_m_addDiscount, HotelManagementClassDiagram_Costable_m_removeDiscount}

# HotelManagementClassDiagram_BookingController class attributes and methods
HotelManagementClassDiagram_BookingController_m_searchAvailableRoomTypes: Method = Method(name="searchAvailableRoomTypes", parameters={Parameter(name='toDate'), Parameter(name='fromDate'), Parameter(name='nbrOfAdults'), Parameter(name='nbrOfChildren')}, type=StringType)
HotelManagementClassDiagram_BookingController_m_findCustomer: Method = Method(name="findCustomer", parameters={Parameter(name='ssNumber')})
HotelManagementClassDiagram_BookingController_m_assignRoom: Method = Method(name="assignRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_BookingController_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='roomTypes')}, type=BooleanType)
HotelManagementClassDiagram_BookingController_m_sendConfirmation: Method = Method(name="sendConfirmation", parameters={Parameter(name='booking')}, type=BooleanType)
HotelManagementClassDiagram_BookingController_m_updateBooking: Method = Method(name="updateBooking", parameters={Parameter(name='booking')}, type=BooleanType)
HotelManagementClassDiagram_BookingController_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='bookingId')}, type=StringType)
HotelManagementClassDiagram_BookingController_m_confirm: Method = Method(name="confirm", parameters={Parameter(name='booking')}, type=BooleanType)
HotelManagementClassDiagram_BookingController_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_BookingController_m_createKeyCard: Method = Method(name="createKeyCard", parameters={Parameter(name='room')})
HotelManagementClassDiagram_BookingController_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_BookingController_m_saveCustomer: Method = Method(name="saveCustomer", parameters={Parameter(name='customer')})
HotelManagementClassDiagram_BookingController.methods={HotelManagementClassDiagram_BookingController_m_searchAvailableRoomTypes, HotelManagementClassDiagram_BookingController_m_checkOut, HotelManagementClassDiagram_BookingController_m_assignRoom, HotelManagementClassDiagram_BookingController_m_getBooking, HotelManagementClassDiagram_BookingController_m_findCustomer, HotelManagementClassDiagram_BookingController_m_updateBooking, HotelManagementClassDiagram_BookingController_m_createBooking, HotelManagementClassDiagram_BookingController_m_createKeyCard, HotelManagementClassDiagram_BookingController_m_checkIn, HotelManagementClassDiagram_BookingController_m_sendConfirmation, HotelManagementClassDiagram_BookingController_m_saveCustomer, HotelManagementClassDiagram_BookingController_m_confirm}

# HotelManagementClassDiagram_ManagementController class attributes and methods
HotelManagementClassDiagram_ManagementController_m_registerDiscount: Method = Method(name="registerDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_ManagementController_m_modifyBooking: Method = Method(name="modifyBooking", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_ManagementController_m_setDateSpecificPrices: Method = Method(name="setDateSpecificPrices", parameters={Parameter(name='startDate'), Parameter(name='priceChange'), Parameter(name='costable'), Parameter(name='endDate')})
HotelManagementClassDiagram_ManagementController_m_registerRoom: Method = Method(name="registerRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_ManagementController_m_registerAddon: Method = Method(name="registerAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_ManagementController_m_updateRoom: Method = Method(name="updateRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_ManagementController_m_updateAddon: Method = Method(name="updateAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_ManagementController.methods={HotelManagementClassDiagram_ManagementController_m_registerAddon, HotelManagementClassDiagram_ManagementController_m_setDateSpecificPrices, HotelManagementClassDiagram_ManagementController_m_registerRoom, HotelManagementClassDiagram_ManagementController_m_registerDiscount, HotelManagementClassDiagram_ManagementController_m_updateRoom, HotelManagementClassDiagram_ManagementController_m_updateAddon, HotelManagementClassDiagram_ManagementController_m_modifyBooking}

# HotelManagementClassDiagram_MaintenanceController class attributes and methods
HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean: Method = Method(name="getNextRoomToClean", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_addToStack: Method = Method(name="addToStack", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_setStatus: Method = Method(name="setStatus", parameters={Parameter(name='status'), Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_notifyWorker: Method = Method(name="notifyWorker", parameters={Parameter(name='worker')})
HotelManagementClassDiagram_MaintenanceController_m_removeFromStack: Method = Method(name="removeFromStack", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController.methods={HotelManagementClassDiagram_MaintenanceController_m_setStatus, HotelManagementClassDiagram_MaintenanceController_m_addToStack, HotelManagementClassDiagram_MaintenanceController_m_removeFromStack, HotelManagementClassDiagram_MaintenanceController_m_notifyWorker, HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean}

# HotelManagementClassDiagram_Hotel class attributes and methods
HotelManagementClassDiagram_Hotel_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Hotel_address: Property = Property(name="address", type=StringType)
HotelManagementClassDiagram_Hotel_rank: Property = Property(name="rank", type=FloatType)
HotelManagementClassDiagram_Hotel_m_getManagementController: Method = Method(name="getManagementController", parameters={})
HotelManagementClassDiagram_Hotel_m_getMaintenanceController: Method = Method(name="getMaintenanceController", parameters={})
HotelManagementClassDiagram_Hotel_m_authenticate: Method = Method(name="authenticate", parameters={Parameter(name='login'), Parameter(name='password')})
HotelManagementClassDiagram_Hotel_m_getBookingController: Method = Method(name="getBookingController", parameters={})
HotelManagementClassDiagram_Hotel.attributes={HotelManagementClassDiagram_Hotel_rank, HotelManagementClassDiagram_Hotel_address, HotelManagementClassDiagram_Hotel_name}
HotelManagementClassDiagram_Hotel.methods={HotelManagementClassDiagram_Hotel_m_getBookingController, HotelManagementClassDiagram_Hotel_m_getManagementController, HotelManagementClassDiagram_Hotel_m_authenticate, HotelManagementClassDiagram_Hotel_m_getMaintenanceController}

# HotelManagementClassDiagram_BookedRoom class attributes and methods
HotelManagementClassDiagram_BookedRoom_m_addAddon: Method = Method(name="addAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_BookedRoom_m_removeAddon: Method = Method(name="removeAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_BookedRoom.methods={HotelManagementClassDiagram_BookedRoom_m_addAddon, HotelManagementClassDiagram_BookedRoom_m_removeAddon}

# Room class attributes and methods

# HotelManagementClassDiagram_Interaction3 class attributes and methods

# HotelManagementClassDiagram_Interaction1 class attributes and methods

# HotelManagementClassDiagram_Interaction2 class attributes and methods

# HotelManagementClassDiagram_Interaction4 class attributes and methods

# HotelManagementClassDiagram_Interaction5 class attributes and methods

# Relationships
employeeType0: BinaryAssociation = BinaryAssociation(
    name="employeeType0",
    ends={
        Property(name="HotelManagementClassDiagram_EmployeeType", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Employee", type=HotelManagementClassDiagram_EmployeeType, multiplicity=Multiplicity(1, 1))
    }
)
paymentMaster8: BinaryAssociation = BinaryAssociation(
    name="paymentMaster8",
    ends={
        Property(name="HotelManagementClassDiagram_Customer10", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking9", type=HotelManagementClassDiagram_Customer, multiplicity=Multiplicity(1, 1))
    }
)
discounts11: BinaryAssociation = BinaryAssociation(
    name="discounts11",
    ends={
        Property(name="HotelManagementClassDiagram_Discount", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking12", type=HotelManagementClassDiagram_Discount, multiplicity=Multiplicity(1, 9999))
    }
)
creditCard1: BinaryAssociation = BinaryAssociation(
    name="creditCard1",
    ends={
        Property(name="HotelManagementClassDiagram_Creditcard", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking", type=HotelManagementClassDiagram_Creditcard, multiplicity=Multiplicity(1, 1))
    }
)
customer2: BinaryAssociation = BinaryAssociation(
    name="customer2",
    ends={
        Property(name="HotelManagementClassDiagram_Customer", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking3", type=HotelManagementClassDiagram_Customer, multiplicity=Multiplicity(1, 1))
    }
)
addons4: BinaryAssociation = BinaryAssociation(
    name="addons4",
    ends={
        Property(name="HotelManagementClassDiagram_Addon", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking5", type=HotelManagementClassDiagram_Addon, multiplicity=Multiplicity(0, 9999))
    }
)
bookedRooms6: BinaryAssociation = BinaryAssociation(
    name="bookedRooms6",
    ends={
        Property(name="HotelManagementClassDiagram_Room", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking7", type=HotelManagementClassDiagram_Room, multiplicity=Multiplicity(1, 9999))
    }
)
costables13: BinaryAssociation = BinaryAssociation(
    name="costables13",
    ends={
        Property(name="HotelManagementClassDiagram_Costable", type=HotelManagementClassDiagram_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Bill", type=HotelManagementClassDiagram_Costable, multiplicity=Multiplicity(1, 9999))
    }
)
customer14: BinaryAssociation = BinaryAssociation(
    name="customer14",
    ends={
        Property(name="HotelManagementClassDiagram_Customer16", type=HotelManagementClassDiagram_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Bill15", type=HotelManagementClassDiagram_Customer, multiplicity=Multiplicity(1, 1))
    }
)
discounts17: BinaryAssociation = BinaryAssociation(
    name="discounts17",
    ends={
        Property(name="HotelManagementClassDiagram_Discount19", type=HotelManagementClassDiagram_Costable, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Costable18", type=HotelManagementClassDiagram_Discount, multiplicity=Multiplicity(1, 9999))
    }
)
roomStack20: BinaryAssociation = BinaryAssociation(
    name="roomStack20",
    ends={
        Property(name="HotelManagementClassDiagram_Room21", type=HotelManagementClassDiagram_MaintenanceController, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_MaintenanceController", type=HotelManagementClassDiagram_Room, multiplicity=Multiplicity(0, 9999))
    }
)
addons22: BinaryAssociation = BinaryAssociation(
    name="addons22",
    ends={
        Property(name="HotelManagementClassDiagram_Addon23", type=HotelManagementClassDiagram_BookedRoom, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_BookedRoom", type=HotelManagementClassDiagram_Addon, multiplicity=Multiplicity(0, 9999))
    }
)
_24: BinaryAssociation = BinaryAssociation(
    name="_24",
    ends={
        Property(name="HotelManagementClassDiagram_Employee25", type=HotelManagementClassDiagram_Interaction1, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction1", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)
_26: BinaryAssociation = BinaryAssociation(
    name="_26",
    ends={
        Property(name="HotelManagementClassDiagram_Employee27", type=HotelManagementClassDiagram_Interaction2, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction2", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)
_32: BinaryAssociation = BinaryAssociation(
    name="_32",
    ends={
        Property(name="HotelManagementClassDiagram_Booking33", type=HotelManagementClassDiagram_Interaction5, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction5", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1))
    }
)
_28: BinaryAssociation = BinaryAssociation(
    name="_28",
    ends={
        Property(name="HotelManagementClassDiagram_MaintenanceController29", type=HotelManagementClassDiagram_Interaction3, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction3", type=HotelManagementClassDiagram_MaintenanceController, multiplicity=Multiplicity(1, 1))
    }
)
_30: BinaryAssociation = BinaryAssociation(
    name="_30",
    ends={
        Property(name="HotelManagementClassDiagram_Employee31", type=HotelManagementClassDiagram_Interaction4, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction4", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HotelManagementClassDiagram_Employee_Person = Generalization(general=Person, specific=HotelManagementClassDiagram_Employee)
gen_HotelManagementClassDiagram_Customer_Person = Generalization(general=Person, specific=HotelManagementClassDiagram_Customer)
gen_HotelManagementClassDiagram_BookedRoom_Room = Generalization(general=Room, specific=HotelManagementClassDiagram_BookedRoom)

# Domain Model
domain_model = DomainModel(
    name="HotelManagementClassDiagram",
    types={HotelManagementClassDiagram_EmployeeType, HotelManagementClassDiagram_Employee, Person, HotelManagementClassDiagram_Person, HotelManagementClassDiagram_Booking, HotelManagementClassDiagram_Discount, HotelManagementClassDiagram_Creditcard, HotelManagementClassDiagram_Customer, HotelManagementClassDiagram_Addon, HotelManagementClassDiagram_Room, HotelManagementClassDiagram_Bill, HotelManagementClassDiagram_Costable, HotelManagementClassDiagram_BookingController, HotelManagementClassDiagram_ManagementController, HotelManagementClassDiagram_MaintenanceController, HotelManagementClassDiagram_Hotel, HotelManagementClassDiagram_BookedRoom, Room, HotelManagementClassDiagram_Interaction3, HotelManagementClassDiagram_Interaction1, HotelManagementClassDiagram_Interaction2, HotelManagementClassDiagram_Interaction4, HotelManagementClassDiagram_Interaction5, EType, RoomType},
    associations={employeeType0, paymentMaster8, discounts11, creditCard1, customer2, addons4, bookedRooms6, costables13, customer14, discounts17, roomStack20, addons22, _24, _26, _32, _28, _30},
    generalizations={gen_HotelManagementClassDiagram_Employee_Person, gen_HotelManagementClassDiagram_Customer_Person, gen_HotelManagementClassDiagram_BookedRoom_Room},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)