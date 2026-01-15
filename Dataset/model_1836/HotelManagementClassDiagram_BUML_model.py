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
            EnumerationLiteral(name="Family"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Suite")
    }
)

# Classes
HotelManagementClassDiagram_Employee = Class(name="HotelManagementClassDiagram::Employee")
Person = Class(name="Person")
HotelManagementClassDiagram_EmployeeType = Class(name="HotelManagementClassDiagram::EmployeeType")
HotelManagementClassDiagram_Person = Class(name="HotelManagementClassDiagram::Person", is_abstract=True)
HotelManagementClassDiagram_Booking = Class(name="HotelManagementClassDiagram::Booking")
HotelManagementClassDiagram_Creditcard = Class(name="HotelManagementClassDiagram::Creditcard")
HotelManagementClassDiagram_Addon = Class(name="HotelManagementClassDiagram::Addon")
HotelManagementClassDiagram_Room = Class(name="HotelManagementClassDiagram::Room")
HotelManagementClassDiagram_Customer = Class(name="HotelManagementClassDiagram::Customer")
HotelManagementClassDiagram_Discount = Class(name="HotelManagementClassDiagram::Discount")
HotelManagementClassDiagram_Bill = Class(name="HotelManagementClassDiagram::Bill")
Extra = Class(name="Extra")
Costable = Class(name="Costable")
HotelManagementClassDiagram_Extra = Class(name="HotelManagementClassDiagram::Extra")
HotelManagementClassDiagram_Costable = Class(name="HotelManagementClassDiagram::Costable", is_abstract=True)
HotelManagementClassDiagram_BookingController = Class(name="HotelManagementClassDiagram::BookingController")
HotelManagementClassDiagram_ManagementController = Class(name="HotelManagementClassDiagram::ManagementController")
HotelManagementClassDiagram_MaintenanceController = Class(name="HotelManagementClassDiagram::MaintenanceController")
HotelManagementClassDiagram_Hotel = Class(name="HotelManagementClassDiagram::Hotel")
HotelManagementClassDiagram_Interaction1 = Class(name="HotelManagementClassDiagram::Interaction1")
HotelManagementClassDiagram_Interaction2 = Class(name="HotelManagementClassDiagram::Interaction2")
HotelManagementClassDiagram_Interaction3 = Class(name="HotelManagementClassDiagram::Interaction3")
HotelManagementClassDiagram_Interaction4 = Class(name="HotelManagementClassDiagram::Interaction4")
HotelManagementClassDiagram_Interaction5 = Class(name="HotelManagementClassDiagram::Interaction5")
HotelManagementClassDiagram_DBInterface = Class(name="HotelManagementClassDiagram::DBInterface", is_abstract=True)
HotelManagementClassDiagram_FakeDBContext = Class(name="HotelManagementClassDiagram::FakeDBContext")
DBInterface = Class(name="DBInterface")

# HotelManagementClassDiagram_Employee class attributes and methods
HotelManagementClassDiagram_Employee_employeeID: Property = Property(name="employeeID", type=IntegerType)
HotelManagementClassDiagram_Employee_workRate: Property = Property(name="workRate", type=FloatType)
HotelManagementClassDiagram_Employee_salary: Property = Property(name="salary", type=FloatType)
HotelManagementClassDiagram_Employee_password: Property = Property(name="password", type=StringType)
HotelManagementClassDiagram_Employee_m_Booking: Method = Method(name="Booking", parameters={})
HotelManagementClassDiagram_Employee_m_Boolean: Method = Method(name="Boolean", parameters={})
HotelManagementClassDiagram_Employee_m_roomTypes: Method = Method(name="roomTypes", parameters={})
HotelManagementClassDiagram_Employee.attributes={HotelManagementClassDiagram_Employee_workRate, HotelManagementClassDiagram_Employee_password, HotelManagementClassDiagram_Employee_employeeID, HotelManagementClassDiagram_Employee_salary}
HotelManagementClassDiagram_Employee.methods={HotelManagementClassDiagram_Employee_m_Booking, HotelManagementClassDiagram_Employee_m_Boolean, HotelManagementClassDiagram_Employee_m_roomTypes}

# Person class attributes and methods

# HotelManagementClassDiagram_EmployeeType class attributes and methods
HotelManagementClassDiagram_EmployeeType_type: Property = Property(name="type", type=StringType)
HotelManagementClassDiagram_EmployeeType_acessLevel: Property = Property(name="acessLevel", type=IntegerType)
HotelManagementClassDiagram_EmployeeType.attributes={HotelManagementClassDiagram_EmployeeType_acessLevel, HotelManagementClassDiagram_EmployeeType_type}

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
HotelManagementClassDiagram_Person.attributes={HotelManagementClassDiagram_Person_country, HotelManagementClassDiagram_Person_postalCode, HotelManagementClassDiagram_Person_phoneNumber, HotelManagementClassDiagram_Person_gender, HotelManagementClassDiagram_Person_title, HotelManagementClassDiagram_Person_name, HotelManagementClassDiagram_Person_SSNumber, HotelManagementClassDiagram_Person_city, HotelManagementClassDiagram_Person_street}

# HotelManagementClassDiagram_Booking class attributes and methods
HotelManagementClassDiagram_Booking_bookingId: Property = Property(name="bookingId", type=IntegerType)
HotelManagementClassDiagram_Booking_startDate: Property = Property(name="startDate", type=DateType)
HotelManagementClassDiagram_Booking_endDate: Property = Property(name="endDate", type=DateType)
HotelManagementClassDiagram_Booking_created: Property = Property(name="created", type=DateType)
HotelManagementClassDiagram_Booking_internalComments: Property = Property(name="internalComments", type=StringType)
HotelManagementClassDiagram_Booking_externalComments: Property = Property(name="externalComments", type=StringType)
HotelManagementClassDiagram_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
HotelManagementClassDiagram_Booking_checkedOut: Property = Property(name="checkedOut", type=BooleanType)
HotelManagementClassDiagram_Booking_roomTypes: Property = Property(name="roomTypes", type=StringType)
HotelManagementClassDiagram_Booking_m_addDiscount: Method = Method(name="addDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Booking_m_checkIn: Method = Method(name="checkIn", parameters={})
HotelManagementClassDiagram_Booking_m_checkOut: Method = Method(name="checkOut", parameters={}, type=StringType)
HotelManagementClassDiagram_Booking_m_addAddon: Method = Method(name="addAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_Booking_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_Booking_m_removeAddon: Method = Method(name="removeAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_Booking_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_Booking_m_generateBill: Method = Method(name="generateBill", parameters={}, type=StringType)
HotelManagementClassDiagram_Booking_m_pay: Method = Method(name="pay", parameters={Parameter(name='bill')}, type=BooleanType)
HotelManagementClassDiagram_Booking_m_removeDiscount: Method = Method(name="removeDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Booking.attributes={HotelManagementClassDiagram_Booking_internalComments, HotelManagementClassDiagram_Booking_startDate, HotelManagementClassDiagram_Booking_checkedOut, HotelManagementClassDiagram_Booking_roomTypes, HotelManagementClassDiagram_Booking_externalComments, HotelManagementClassDiagram_Booking_created, HotelManagementClassDiagram_Booking_endDate, HotelManagementClassDiagram_Booking_checkedIn, HotelManagementClassDiagram_Booking_bookingId}
HotelManagementClassDiagram_Booking.methods={HotelManagementClassDiagram_Booking_m_removeDiscount, HotelManagementClassDiagram_Booking_m_pay, HotelManagementClassDiagram_Booking_m_checkOut, HotelManagementClassDiagram_Booking_m_removeAddon, HotelManagementClassDiagram_Booking_m_addDiscount, HotelManagementClassDiagram_Booking_m_removeRoom, HotelManagementClassDiagram_Booking_m_checkIn, HotelManagementClassDiagram_Booking_m_addAddon, HotelManagementClassDiagram_Booking_m_generateBill, HotelManagementClassDiagram_Booking_m_addRoom}

# HotelManagementClassDiagram_Creditcard class attributes and methods
HotelManagementClassDiagram_Creditcard_number: Property = Property(name="number", type=StringType)
HotelManagementClassDiagram_Creditcard_cvc: Property = Property(name="cvc", type=IntegerType)
HotelManagementClassDiagram_Creditcard_owner: Property = Property(name="owner", type=StringType)
HotelManagementClassDiagram_Creditcard_expirationMonth: Property = Property(name="expirationMonth", type=IntegerType)
HotelManagementClassDiagram_Creditcard_expirationYear: Property = Property(name="expirationYear", type=IntegerType)
HotelManagementClassDiagram_Creditcard.attributes={HotelManagementClassDiagram_Creditcard_number, HotelManagementClassDiagram_Creditcard_expirationYear, HotelManagementClassDiagram_Creditcard_cvc, HotelManagementClassDiagram_Creditcard_owner, HotelManagementClassDiagram_Creditcard_expirationMonth}

# HotelManagementClassDiagram_Addon class attributes and methods

# HotelManagementClassDiagram_Room class attributes and methods
HotelManagementClassDiagram_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
HotelManagementClassDiagram_Room_size: Property = Property(name="size", type=FloatType)
HotelManagementClassDiagram_Room_internalComment: Property = Property(name="internalComment", type=StringType)
HotelManagementClassDiagram_Room_maxNbrPeople: Property = Property(name="maxNbrPeople", type=IntegerType)
HotelManagementClassDiagram_Room_underCleaning: Property = Property(name="underCleaning", type=BooleanType)
HotelManagementClassDiagram_Room_underRepair: Property = Property(name="underRepair", type=BooleanType)
HotelManagementClassDiagram_Room_type: Property = Property(name="type", type=StringType)
HotelManagementClassDiagram_Room.attributes={HotelManagementClassDiagram_Room_internalComment, HotelManagementClassDiagram_Room_underCleaning, HotelManagementClassDiagram_Room_size, HotelManagementClassDiagram_Room_maxNbrPeople, HotelManagementClassDiagram_Room_type, HotelManagementClassDiagram_Room_roomNumber, HotelManagementClassDiagram_Room_underRepair}

# HotelManagementClassDiagram_Customer class attributes and methods
HotelManagementClassDiagram_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
HotelManagementClassDiagram_Customer_bonusPoints: Property = Property(name="bonusPoints", type=IntegerType)
HotelManagementClassDiagram_Customer_miscInfo: Property = Property(name="miscInfo", type=StringType)
HotelManagementClassDiagram_Customer_m_addBonusPoints: Method = Method(name="addBonusPoints", parameters={Parameter(name='bonusPoints')})
HotelManagementClassDiagram_Customer.attributes={HotelManagementClassDiagram_Customer_miscInfo, HotelManagementClassDiagram_Customer_bonusPoints, HotelManagementClassDiagram_Customer_customerID}
HotelManagementClassDiagram_Customer.methods={HotelManagementClassDiagram_Customer_m_addBonusPoints}

# HotelManagementClassDiagram_Discount class attributes and methods
HotelManagementClassDiagram_Discount_isPercentage: Property = Property(name="isPercentage", type=StringType)
HotelManagementClassDiagram_Discount_amount: Property = Property(name="amount", type=FloatType)
HotelManagementClassDiagram_Discount_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Discount.attributes={HotelManagementClassDiagram_Discount_amount, HotelManagementClassDiagram_Discount_isPercentage, HotelManagementClassDiagram_Discount_name}

# HotelManagementClassDiagram_Bill class attributes and methods
HotelManagementClassDiagram_Bill_totalPrice: Property = Property(name="totalPrice", type=FloatType)
HotelManagementClassDiagram_Bill_final: Property = Property(name="final", type=BooleanType)
HotelManagementClassDiagram_Bill_paid: Property = Property(name="paid", type=BooleanType)
HotelManagementClassDiagram_Bill_m_addCostable: Method = Method(name="addCostable", parameters={Parameter(name='costable')})
HotelManagementClassDiagram_Bill.attributes={HotelManagementClassDiagram_Bill_paid, HotelManagementClassDiagram_Bill_final, HotelManagementClassDiagram_Bill_totalPrice}
HotelManagementClassDiagram_Bill.methods={HotelManagementClassDiagram_Bill_m_addCostable}

# Extra class attributes and methods

# Costable class attributes and methods

# HotelManagementClassDiagram_Extra class attributes and methods
HotelManagementClassDiagram_Extra_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Extra_description: Property = Property(name="description", type=StringType)
HotelManagementClassDiagram_Extra.attributes={HotelManagementClassDiagram_Extra_name, HotelManagementClassDiagram_Extra_description}

# HotelManagementClassDiagram_Costable class attributes and methods
HotelManagementClassDiagram_Costable_price: Property = Property(name="price", type=FloatType)
HotelManagementClassDiagram_Costable_m_removeDiscount: Method = Method(name="removeDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Costable_m_addDiscount: Method = Method(name="addDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_Costable.attributes={HotelManagementClassDiagram_Costable_price}
HotelManagementClassDiagram_Costable.methods={HotelManagementClassDiagram_Costable_m_removeDiscount, HotelManagementClassDiagram_Costable_m_addDiscount}

# HotelManagementClassDiagram_BookingController class attributes and methods
HotelManagementClassDiagram_BookingController_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_BookingController_m_searchAvailableRoomTypes: Method = Method(name="searchAvailableRoomTypes", parameters={Parameter(name='fromDate'), Parameter(name='nbrOfChildren'), Parameter(name='nbrOfAdults'), Parameter(name='toDate')}, type=StringType)
HotelManagementClassDiagram_BookingController_m_sendConfirmation: Method = Method(name="sendConfirmation", parameters={Parameter(name='booking')}, type=BooleanType)
HotelManagementClassDiagram_BookingController_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='bookingId')}, type=StringType)
HotelManagementClassDiagram_BookingController_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_BookingController_m_saveCustomer: Method = Method(name="saveCustomer", parameters={Parameter(name='customer')})
HotelManagementClassDiagram_BookingController_m_findCustomer: Method = Method(name="findCustomer", parameters={Parameter(name='ssNumber')})
HotelManagementClassDiagram_BookingController_m_assignRoom: Method = Method(name="assignRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_BookingController_m_getCustomer: Method = Method(name="getCustomer", parameters={Parameter(name='SSN')}, type=StringType)
HotelManagementClassDiagram_BookingController_m_updateOrAddCustomer: Method = Method(name="updateOrAddCustomer", parameters={Parameter(name='customer')})
HotelManagementClassDiagram_BookingController_m_updateOrAddBooking: Method = Method(name="updateOrAddBooking", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_BookingController_m_getAllBookings: Method = Method(name="getAllBookings", parameters={}, type=StringType)
HotelManagementClassDiagram_BookingController_m_getAllCustomers: Method = Method(name="getAllCustomers", parameters={}, type=StringType)
HotelManagementClassDiagram_BookingController.methods={HotelManagementClassDiagram_BookingController_m_checkOut, HotelManagementClassDiagram_BookingController_m_updateOrAddCustomer, HotelManagementClassDiagram_BookingController_m_assignRoom, HotelManagementClassDiagram_BookingController_m_getCustomer, HotelManagementClassDiagram_BookingController_m_findCustomer, HotelManagementClassDiagram_BookingController_m_getAllBookings, HotelManagementClassDiagram_BookingController_m_sendConfirmation, HotelManagementClassDiagram_BookingController_m_searchAvailableRoomTypes, HotelManagementClassDiagram_BookingController_m_getAllCustomers, HotelManagementClassDiagram_BookingController_m_updateOrAddBooking, HotelManagementClassDiagram_BookingController_m_saveCustomer, HotelManagementClassDiagram_BookingController_m_checkIn, HotelManagementClassDiagram_BookingController_m_getBooking}

# HotelManagementClassDiagram_ManagementController class attributes and methods
HotelManagementClassDiagram_ManagementController_m_updateOrAddEmployee: Method = Method(name="updateOrAddEmployee", parameters={Parameter(name='employee')})
HotelManagementClassDiagram_ManagementController_m_getAllExtras: Method = Method(name="getAllExtras", parameters={}, type=Extra)
HotelManagementClassDiagram_ManagementController_m_updateOrAddEmployeeType: Method = Method(name="updateOrAddEmployeeType", parameters={Parameter(name='employeeType')})
HotelManagementClassDiagram_ManagementController_m_updateOrAddRoom: Method = Method(name="updateOrAddRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_ManagementController_m_updateOrAddRoomType: Method = Method(name="updateOrAddRoomType", parameters={Parameter(name='roomType')})
HotelManagementClassDiagram_ManagementController_m_updateOrAddDiscount: Method = Method(name="updateOrAddDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_ManagementController_m_updateOrAddAddon: Method = Method(name="updateOrAddAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_ManagementController_m_updateOrAddExtra: Method = Method(name="updateOrAddExtra", parameters={Parameter(name='extra')})
HotelManagementClassDiagram_ManagementController_m_getAllEmployees: Method = Method(name="getAllEmployees", parameters={}, type=StringType)
HotelManagementClassDiagram_ManagementController_m_getAllAddons: Method = Method(name="getAllAddons", parameters={}, type=StringType)
HotelManagementClassDiagram_ManagementController_m_getAllDiscounts: Method = Method(name="getAllDiscounts", parameters={}, type=StringType)
HotelManagementClassDiagram_ManagementController_m_getEmployee: Method = Method(name="getEmployee", parameters={Parameter(name='SSN')}, type=StringType)
HotelManagementClassDiagram_ManagementController.methods={HotelManagementClassDiagram_ManagementController_m_getAllDiscounts, HotelManagementClassDiagram_ManagementController_m_updateOrAddRoomType, HotelManagementClassDiagram_ManagementController_m_updateOrAddAddon, HotelManagementClassDiagram_ManagementController_m_updateOrAddEmployee, HotelManagementClassDiagram_ManagementController_m_getEmployee, HotelManagementClassDiagram_ManagementController_m_getAllAddons, HotelManagementClassDiagram_ManagementController_m_updateOrAddEmployeeType, HotelManagementClassDiagram_ManagementController_m_updateOrAddRoom, HotelManagementClassDiagram_ManagementController_m_updateOrAddDiscount, HotelManagementClassDiagram_ManagementController_m_updateOrAddExtra, HotelManagementClassDiagram_ManagementController_m_getAllExtras, HotelManagementClassDiagram_ManagementController_m_getAllEmployees}

# HotelManagementClassDiagram_MaintenanceController class attributes and methods
HotelManagementClassDiagram_MaintenanceController_m_addToQueue: Method = Method(name="addToQueue", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_setCleanedStatus: Method = Method(name="setCleanedStatus", parameters={Parameter(name='room'), Parameter(name='status')})
HotelManagementClassDiagram_MaintenanceController_m_removeFromQueue: Method = Method(name="removeFromQueue", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean: Method = Method(name="getNextRoomToClean", parameters={Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_setRepairedStatus: Method = Method(name="setRepairedStatus", parameters={Parameter(name='repaired'), Parameter(name='room')})
HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean: Method = Method(name="getNextRoomToClean", parameters={}, type=StringType)
HotelManagementClassDiagram_MaintenanceController.methods={HotelManagementClassDiagram_MaintenanceController_m_addToQueue, HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean, HotelManagementClassDiagram_MaintenanceController_m_removeFromQueue, HotelManagementClassDiagram_MaintenanceController_m_setRepairedStatus, HotelManagementClassDiagram_MaintenanceController_m_setCleanedStatus, HotelManagementClassDiagram_MaintenanceController_m_getNextRoomToClean}

# HotelManagementClassDiagram_Hotel class attributes and methods
HotelManagementClassDiagram_Hotel_name: Property = Property(name="name", type=StringType)
HotelManagementClassDiagram_Hotel_address: Property = Property(name="address", type=StringType)
HotelManagementClassDiagram_Hotel_rank: Property = Property(name="rank", type=FloatType)
HotelManagementClassDiagram_Hotel_m_logIn: Method = Method(name="logIn", parameters={Parameter(name='password'), Parameter(name='SSN')}, type=StringType)
HotelManagementClassDiagram_Hotel.attributes={HotelManagementClassDiagram_Hotel_name, HotelManagementClassDiagram_Hotel_address, HotelManagementClassDiagram_Hotel_rank}
HotelManagementClassDiagram_Hotel.methods={HotelManagementClassDiagram_Hotel_m_logIn}

# HotelManagementClassDiagram_Interaction1 class attributes and methods

# HotelManagementClassDiagram_Interaction2 class attributes and methods

# HotelManagementClassDiagram_Interaction3 class attributes and methods

# HotelManagementClassDiagram_Interaction4 class attributes and methods

# HotelManagementClassDiagram_Interaction5 class attributes and methods

# HotelManagementClassDiagram_DBInterface class attributes and methods
HotelManagementClassDiagram_DBInterface_m__getAllRooms: Method = Method(name="_getAllRooms", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='roomNumber')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllRoomTypes: Method = Method(name="getAllRoomTypes", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAvaliableRoomTypes: Method = Method(name="getAvaliableRoomTypes", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllAddons: Method = Method(name="getAllAddons", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAddon: Method = Method(name="getAddon", parameters={Parameter(name='addonName')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllDiscounts: Method = Method(name="getAllDiscounts", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getDiscount: Method = Method(name="getDiscount", parameters={Parameter(name='discountName')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllBookings: Method = Method(name="getAllBookings", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='fromDate'), Parameter(name='toDate')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getPastBookings: Method = Method(name="getPastBookings", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getFutureBookings: Method = Method(name="getFutureBookings", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getCurrentBookings: Method = Method(name="getCurrentBookings", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_findBookings: Method = Method(name="findBookings", parameters={Parameter(name='customerName')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllCustomers: Method = Method(name="getAllCustomers", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getCustomer: Method = Method(name="getCustomer", parameters={Parameter(name='customerSSNumber')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_findCustomers: Method = Method(name="findCustomers", parameters={Parameter(name='partOfCustomerName')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllEmployees: Method = Method(name="getAllEmployees", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getEmployee: Method = Method(name="getEmployee", parameters={Parameter(name='employeeSSNumber')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllManagers: Method = Method(name="getAllManagers", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllCleaners: Method = Method(name="getAllCleaners", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getAllReceptionists: Method = Method(name="getAllReceptionists", parameters={}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_updateOrAddRoom: Method = Method(name="updateOrAddRoom", parameters={Parameter(name='room')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddCustomer: Method = Method(name="updateOrAddCustomer", parameters={Parameter(name='customer')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddBooking: Method = Method(name="updateOrAddBooking", parameters={Parameter(name='booking')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddDiscount: Method = Method(name="updateOrAddDiscount", parameters={Parameter(name='discount')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddAddon: Method = Method(name="updateOrAddAddon", parameters={Parameter(name='addon')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddEmployee: Method = Method(name="updateOrAddEmployee", parameters={Parameter(name='employee')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddRoomType: Method = Method(name="updateOrAddRoomType", parameters={Parameter(name='type')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddEmployeeType: Method = Method(name="updateOrAddEmployeeType", parameters={Parameter(name='type')})
HotelManagementClassDiagram_DBInterface_m_updateOrAddExtra: Method = Method(name="updateOrAddExtra", parameters={Parameter(name='extra')})
HotelManagementClassDiagram_DBInterface_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='type'), Parameter(name='to'), Parameter(name='from')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getRooms: Method = Method(name="getRooms", parameters={Parameter(name='type')}, type=StringType)
HotelManagementClassDiagram_DBInterface_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='bookingID')}, type=StringType)
HotelManagementClassDiagram_DBInterface.methods={HotelManagementClassDiagram_DBInterface_m_getAllDiscounts, HotelManagementClassDiagram_DBInterface_m_getDiscount, HotelManagementClassDiagram_DBInterface_m_getAvailableRooms, HotelManagementClassDiagram_DBInterface_m_getAllCustomers, HotelManagementClassDiagram_DBInterface_m_updateOrAddEmployee, HotelManagementClassDiagram_DBInterface_m_getFutureBookings, HotelManagementClassDiagram_DBInterface_m_updateOrAddRoom, HotelManagementClassDiagram_DBInterface_m_getAllBookings, HotelManagementClassDiagram_DBInterface_m_getAddon, HotelManagementClassDiagram_DBInterface_m_getAllAddons, HotelManagementClassDiagram_DBInterface_m_updateOrAddDiscount, HotelManagementClassDiagram_DBInterface_m_updateOrAddEmployeeType, HotelManagementClassDiagram_DBInterface_m_updateOrAddAddon, HotelManagementClassDiagram_DBInterface_m_getCustomer, HotelManagementClassDiagram_DBInterface_m_getBooking, HotelManagementClassDiagram_DBInterface_m_getRoom, HotelManagementClassDiagram_DBInterface_m__getAllRooms, HotelManagementClassDiagram_DBInterface_m_findCustomers, HotelManagementClassDiagram_DBInterface_m_getAllCleaners, HotelManagementClassDiagram_DBInterface_m_getRooms, HotelManagementClassDiagram_DBInterface_m_getAllEmployees, HotelManagementClassDiagram_DBInterface_m_getBookings, HotelManagementClassDiagram_DBInterface_m_getCurrentBookings, HotelManagementClassDiagram_DBInterface_m_getAllManagers, HotelManagementClassDiagram_DBInterface_m_getPastBookings, HotelManagementClassDiagram_DBInterface_m_getAllReceptionists, HotelManagementClassDiagram_DBInterface_m_updateOrAddExtra, HotelManagementClassDiagram_DBInterface_m_updateOrAddCustomer, HotelManagementClassDiagram_DBInterface_m_findBookings, HotelManagementClassDiagram_DBInterface_m_getAllRoomTypes, HotelManagementClassDiagram_DBInterface_m_getEmployee, HotelManagementClassDiagram_DBInterface_m_updateOrAddBooking, HotelManagementClassDiagram_DBInterface_m_updateOrAddRoomType, HotelManagementClassDiagram_DBInterface_m_getAvaliableRoomTypes}

# HotelManagementClassDiagram_FakeDBContext class attributes and methods

# DBInterface class attributes and methods

# Relationships
employeeType0: BinaryAssociation = BinaryAssociation(
    name="employeeType0",
    ends={
        Property(name="HotelManagementClassDiagram_EmployeeType", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Employee", type=HotelManagementClassDiagram_EmployeeType, multiplicity=Multiplicity(1, 1))
    }
)
creditCard1: BinaryAssociation = BinaryAssociation(
    name="creditCard1",
    ends={
        Property(name="HotelManagementClassDiagram_Creditcard", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking", type=HotelManagementClassDiagram_Creditcard, multiplicity=Multiplicity(1, 1))
    }
)
addons2: BinaryAssociation = BinaryAssociation(
    name="addons2",
    ends={
        Property(name="HotelManagementClassDiagram_Addon", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking3", type=HotelManagementClassDiagram_Addon, multiplicity=Multiplicity(0, 9999))
    }
)
bookedRooms4: BinaryAssociation = BinaryAssociation(
    name="bookedRooms4",
    ends={
        Property(name="HotelManagementClassDiagram_Room", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking5", type=HotelManagementClassDiagram_Room, multiplicity=Multiplicity(1, 9999))
    }
)
paymentMaster6: BinaryAssociation = BinaryAssociation(
    name="paymentMaster6",
    ends={
        Property(name="HotelManagementClassDiagram_Customer", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking7", type=HotelManagementClassDiagram_Customer, multiplicity=Multiplicity(1, 1))
    }
)
discounts8: BinaryAssociation = BinaryAssociation(
    name="discounts8",
    ends={
        Property(name="HotelManagementClassDiagram_Discount", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking9", type=HotelManagementClassDiagram_Discount, multiplicity=Multiplicity(1, 9999))
    }
)
finalBill10: BinaryAssociation = BinaryAssociation(
    name="finalBill10",
    ends={
        Property(name="HotelManagementClassDiagram_Bill", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Booking11", type=HotelManagementClassDiagram_Bill, multiplicity=Multiplicity(1, 1))
    }
)
discounts12: BinaryAssociation = BinaryAssociation(
    name="discounts12",
    ends={
        Property(name="HotelManagementClassDiagram_Discount13", type=HotelManagementClassDiagram_Costable, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Costable", type=HotelManagementClassDiagram_Discount, multiplicity=Multiplicity(1, 9999))
    }
)
costables14: BinaryAssociation = BinaryAssociation(
    name="costables14",
    ends={
        Property(name="HotelManagementClassDiagram_Costable16", type=HotelManagementClassDiagram_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Bill15", type=HotelManagementClassDiagram_Costable, multiplicity=Multiplicity(1, 9999))
    }
)
customer17: BinaryAssociation = BinaryAssociation(
    name="customer17",
    ends={
        Property(name="HotelManagementClassDiagram_Customer19", type=HotelManagementClassDiagram_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Bill18", type=HotelManagementClassDiagram_Customer, multiplicity=Multiplicity(1, 1))
    }
)
roomQueue20: BinaryAssociation = BinaryAssociation(
    name="roomQueue20",
    ends={
        Property(name="HotelManagementClassDiagram_Room21", type=HotelManagementClassDiagram_MaintenanceController, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_MaintenanceController", type=HotelManagementClassDiagram_Room, multiplicity=Multiplicity(1, 9999))
    }
)
user28: BinaryAssociation = BinaryAssociation(
    name="user28",
    ends={
        Property(name="HotelManagementClassDiagram_Employee30", type=HotelManagementClassDiagram_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Hotel29", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)
bookingController22: BinaryAssociation = BinaryAssociation(
    name="bookingController22",
    ends={
        Property(name="HotelManagementClassDiagram_BookingController", type=HotelManagementClassDiagram_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Hotel", type=HotelManagementClassDiagram_BookingController, multiplicity=Multiplicity(1, 1))
    }
)
maintenanceController23: BinaryAssociation = BinaryAssociation(
    name="maintenanceController23",
    ends={
        Property(name="HotelManagementClassDiagram_MaintenanceController25", type=HotelManagementClassDiagram_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Hotel24", type=HotelManagementClassDiagram_MaintenanceController, multiplicity=Multiplicity(1, 1))
    }
)
managementController26: BinaryAssociation = BinaryAssociation(
    name="managementController26",
    ends={
        Property(name="HotelManagementClassDiagram_ManagementController", type=HotelManagementClassDiagram_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Hotel27", type=HotelManagementClassDiagram_ManagementController, multiplicity=Multiplicity(1, 1))
    }
)
_39: BinaryAssociation = BinaryAssociation(
    name="_39",
    ends={
        Property(name="HotelManagementClassDiagram_Booking40", type=HotelManagementClassDiagram_Interaction5, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction5", type=HotelManagementClassDiagram_Booking, multiplicity=Multiplicity(1, 1))
    }
)
_31: BinaryAssociation = BinaryAssociation(
    name="_31",
    ends={
        Property(name="HotelManagementClassDiagram_Employee32", type=HotelManagementClassDiagram_Interaction1, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction1", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)
_33: BinaryAssociation = BinaryAssociation(
    name="_33",
    ends={
        Property(name="HotelManagementClassDiagram_Employee34", type=HotelManagementClassDiagram_Interaction2, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction2", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)
_35: BinaryAssociation = BinaryAssociation(
    name="_35",
    ends={
        Property(name="HotelManagementClassDiagram_MaintenanceController36", type=HotelManagementClassDiagram_Interaction3, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction3", type=HotelManagementClassDiagram_MaintenanceController, multiplicity=Multiplicity(1, 1))
    }
)
_37: BinaryAssociation = BinaryAssociation(
    name="_37",
    ends={
        Property(name="HotelManagementClassDiagram_Employee38", type=HotelManagementClassDiagram_Interaction4, multiplicity=Multiplicity(1, 1)),
        Property(name="HotelManagementClassDiagram_Interaction4", type=HotelManagementClassDiagram_Employee, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HotelManagementClassDiagram_Employee_Person = Generalization(general=Person, specific=HotelManagementClassDiagram_Employee)
gen_HotelManagementClassDiagram_Addon_Extra = Generalization(general=Extra, specific=HotelManagementClassDiagram_Addon)
gen_HotelManagementClassDiagram_Addon_Costable = Generalization(general=Costable, specific=HotelManagementClassDiagram_Addon)
gen_HotelManagementClassDiagram_Customer_Person = Generalization(general=Person, specific=HotelManagementClassDiagram_Customer)
gen_HotelManagementClassDiagram_Room_Costable = Generalization(general=Costable, specific=HotelManagementClassDiagram_Room)
gen_HotelManagementClassDiagram_FakeDBContext_DBInterface = Generalization(general=DBInterface, specific=HotelManagementClassDiagram_FakeDBContext)

# Domain Model
domain_model = DomainModel(
    name="HotelManagementClassDiagram",
    types={HotelManagementClassDiagram_Employee, Person, HotelManagementClassDiagram_EmployeeType, HotelManagementClassDiagram_Person, HotelManagementClassDiagram_Booking, HotelManagementClassDiagram_Creditcard, HotelManagementClassDiagram_Addon, HotelManagementClassDiagram_Room, HotelManagementClassDiagram_Customer, HotelManagementClassDiagram_Discount, HotelManagementClassDiagram_Bill, Extra, Costable, HotelManagementClassDiagram_Extra, HotelManagementClassDiagram_Costable, HotelManagementClassDiagram_BookingController, HotelManagementClassDiagram_ManagementController, HotelManagementClassDiagram_MaintenanceController, HotelManagementClassDiagram_Hotel, HotelManagementClassDiagram_Interaction1, HotelManagementClassDiagram_Interaction2, HotelManagementClassDiagram_Interaction3, HotelManagementClassDiagram_Interaction4, HotelManagementClassDiagram_Interaction5, HotelManagementClassDiagram_DBInterface, HotelManagementClassDiagram_FakeDBContext, DBInterface, EType, RoomType},
    associations={employeeType0, creditCard1, addons2, bookedRooms4, paymentMaster6, discounts8, finalBill10, discounts12, costables14, customer17, roomQueue20, user28, bookingController22, maintenanceController23, managementController26, _39, _31, _33, _35, _37},
    generalizations={gen_HotelManagementClassDiagram_Employee_Person, gen_HotelManagementClassDiagram_Addon_Extra, gen_HotelManagementClassDiagram_Addon_Costable, gen_HotelManagementClassDiagram_Customer_Person, gen_HotelManagementClassDiagram_Room_Costable, gen_HotelManagementClassDiagram_FakeDBContext_DBInterface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)