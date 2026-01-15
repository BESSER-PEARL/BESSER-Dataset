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
HotelRoomCategory: Enumeration = Enumeration(
    name="HotelRoomCategory",
    literals={
            EnumerationLiteral(name="StandardRoom"),
			EnumerationLiteral(name="FamilyRoom"),
			EnumerationLiteral(name="Suite")
    }
)

ConferenceRoomCategory: Enumeration = Enumeration(
    name="ConferenceRoomCategory",
    literals={
            EnumerationLiteral(name="DiningRoom"),
			EnumerationLiteral(name="LectureRoom"),
			EnumerationLiteral(name="MeetingRoom"),
			EnumerationLiteral(name="Other")
    }
)

AccountType: Enumeration = Enumeration(
    name="AccountType",
    literals={
            EnumerationLiteral(name="Manager"),
			EnumerationLiteral(name="CustomerService"),
			EnumerationLiteral(name="Guest"),
			EnumerationLiteral(name="Staff")
    }
)

# Classes
Classes_Bookables_Bookable = Class(name="Classes::Bookables::Bookable", is_abstract=True)
Classes_Bookables_Room = Class(name="Classes::Bookables::Room", is_abstract=True)
Bookable = Class(name="Bookable")
RoomLocation = Class(name="RoomLocation")
Classes_Bookables_RoomLocation = Class(name="Classes::Bookables::RoomLocation")
Classes_Bookables_ConferenceRoom = Class(name="Classes::Bookables::ConferenceRoom")
Classes_Bookables_HostelBed = Class(name="Classes::Bookables::HostelBed")
HotelRoom = Class(name="HotelRoom")
Classes_Bookables_HotelRoom = Class(name="Classes::Bookables::HotelRoom")
Room = Class(name="Room")
Classes_Bookables_IBookablesManage = Class(name="Classes::Bookables::IBookablesManage", is_abstract=True)
IBookablesAccess = Class(name="IBookablesAccess")
Classes_Bookables_IBookablesAccess = Class(name="Classes::Bookables::IBookablesAccess", is_abstract=True)
Classes_Bookables_BookablesManager = Class(name="Classes::Bookables::BookablesManager")
IBookablesManage = Class(name="IBookablesManage")
CreditCard = Class(name="CreditCard")
Classes_Stays_CreditCard = Class(name="Classes::Stays::CreditCard")
IStays = Class(name="IStays")
Classes_Stays_Stay = Class(name="Classes::Stays::Stay")
IGuests = Class(name="IGuests")
Classes_Stays_IStays = Class(name="Classes::Stays::IStays", is_abstract=True)
Classes_Stays_StaysManager = Class(name="Classes::Stays::StaysManager")
Stay = Class(name="Stay")
CustomerProvides = Class(name="CustomerProvides")
IBills = Class(name="IBills")
Classes_Banking_AdministratorProvides = Class(name="Classes::Banking::AdministratorProvides", is_abstract=True)
Classes_Banking_CustomerProvides = Class(name="Classes::Banking::CustomerProvides", is_abstract=True)
Classes_Bills_BillsManager = Class(name="Classes::Bills::BillsManager")
Bill = Class(name="Bill")
IInventoryAccess = Class(name="IInventoryAccess")
IServicesAccess = Class(name="IServicesAccess")
Classes_Bills_Bill = Class(name="Classes::Bills::Bill")
Classes_Bills_IBills = Class(name="Classes::Bills::IBills", is_abstract=True)
Classes_Inventory_IManageInventory = Class(name="Classes::Inventory::IManageInventory", is_abstract=True)
Classes_Inventory_InventoryManager = Class(name="Classes::Inventory::InventoryManager")
IManageInventory = Class(name="IManageInventory")
Item = Class(name="Item")
Classes_Inventory_Item = Class(name="Classes::Inventory::Item")
Classes_Inventory_IInventoryAccess = Class(name="Classes::Inventory::IInventoryAccess", is_abstract=True)
Classes_Services_RoomServiceMenu = Class(name="Classes::Services::RoomServiceMenu")
Classes_Services_ServiceManager = Class(name="Classes::Services::ServiceManager")
IServicesManage = Class(name="IServicesManage")
Service = Class(name="Service")
RoomServiceOrder = Class(name="RoomServiceOrder")
RoomServiceMenu = Class(name="RoomServiceMenu")
Classes_Services_Service = Class(name="Classes::Services::Service")
Classes_Services_RoomServiceOrder = Class(name="Classes::Services::RoomServiceOrder")
Classes_Services_IServicesManage = Class(name="Classes::Services::IServicesManage", is_abstract=True)
Classes_Services_IServicesAccess = Class(name="Classes::Services::IServicesAccess", is_abstract=True)
Classes_Guests_GuestsManager = Class(name="Classes::Guests::GuestsManager")
Guest = Class(name="Guest")
IManageAccounts = Class(name="IManageAccounts")
Classes_Guests_Guest = Class(name="Classes::Guests::Guest")
Classes_Guests_IGuests = Class(name="Classes::Guests::IGuests", is_abstract=True)
Classes_Accounts_Account = Class(name="Classes::Accounts::Account")
Classes_Accounts_AccountsManager = Class(name="Classes::Accounts::AccountsManager")
Accounts_IManageAccounts = Class(name="Accounts::IManageAccounts")
Accounts_IAccountsAccess = Class(name="Accounts::IAccountsAccess")
Account = Class(name="Account")
Classes_Accounts_IAccountsAccess = Class(name="Classes::Accounts::IAccountsAccess", is_abstract=True)
Classes_Accounts_IManageAccounts = Class(name="Classes::Accounts::IManageAccounts", is_abstract=True)
Classes_Bookings_Booking = Class(name="Classes::Bookings::Booking")
Classes_Bookings_BookingsManager = Class(name="Classes::Bookings::BookingsManager")
IBookings = Class(name="IBookings")
Booking = Class(name="Booking")
ICustomers = Class(name="ICustomers")
Classes_Bookings_IBookings = Class(name="Classes::Bookings::IBookings", is_abstract=True)
Classes_Customers_CustomersManager = Class(name="Classes::Customers::CustomersManager")
Customer = Class(name="Customer")
Classes_Customers_Customer = Class(name="Classes::Customers::Customer")
Classes_Customers_ICustomers = Class(name="Classes::Customers::ICustomers", is_abstract=True)
Classes_Statistics_Statistic = Class(name="Classes::Statistics::Statistic")
StatisticEntry = Class(name="StatisticEntry")
Date = Class(name="Date")
Classes_Statistics_StatisticEntry = Class(name="Classes::Statistics::StatisticEntry")
Classes_Statistics_Date = Class(name="Classes::Statistics::Date")
Classes_Statistics_IStatisticsGenerator = Class(name="Classes::Statistics::IStatisticsGenerator", is_abstract=True)
Classes_Staff_MonthlySalaryContract = Class(name="Classes::Staff::MonthlySalaryContract")
Classes_Statistics_StatisticsGenerator = Class(name="Classes::Statistics::StatisticsGenerator")
IStatisticsGenerator = Class(name="IStatisticsGenerator")
IStaff = Class(name="IStaff")
Classes_Staff_StaffManager = Class(name="Classes::Staff::StaffManager")
Staff = Class(name="Staff")
Classes_Staff_Staff = Class(name="Classes::Staff::Staff")
SalaryContract = Class(name="SalaryContract")
Classes_Staff_SalaryContract = Class(name="Classes::Staff::SalaryContract", is_abstract=True)
Classes_Staff_HourlySalaryContract = Class(name="Classes::Staff::HourlySalaryContract")
Classes_Staff_IStaff = Class(name="Classes::Staff::IStaff", is_abstract=True)
Classes_Restaurants_IRestaurantsManage = Class(name="Classes::Restaurants::IRestaurantsManage", is_abstract=True)
IRestaurantsAccess = Class(name="IRestaurantsAccess")
Classes_Restaurants_IRestaurantsAccess = Class(name="Classes::Restaurants::IRestaurantsAccess", is_abstract=True)
Classes_Restaurants_RestaurantsManager = Class(name="Classes::Restaurants::RestaurantsManager")
IRestaurantsManage = Class(name="IRestaurantsManage")
Restaurant = Class(name="Restaurant")
Classes_Restaurants_Restaurant = Class(name="Classes::Restaurants::Restaurant")
Reservation = Class(name="Reservation")
RestaurantTable = Class(name="RestaurantTable")
RestaurantMenu = Class(name="RestaurantMenu")
Classes_Restaurants_Reservation = Class(name="Classes::Restaurants::Reservation")
Classes_Restaurants_RestaurantMenu = Class(name="Classes::Restaurants::RestaurantMenu")
Classes_Feedback_IFeedback = Class(name="Classes::Feedback::IFeedback", is_abstract=True)
Classes_Restaurants_RestaurantTable = Class(name="Classes::Restaurants::RestaurantTable")
Classes_Feedback_FeedbackManager = Class(name="Classes::Feedback::FeedbackManager")
IFeedback = Class(name="IFeedback")
Feedback = Class(name="Feedback")
Classes_Feedback_Feedback = Class(name="Classes::Feedback::Feedback")
Classes_Requests_IRequests = Class(name="Classes::Requests::IRequests", is_abstract=True)
Classes_Requests_RequestsManager = Class(name="Classes::Requests::RequestsManager")
IRequests = Class(name="IRequests")
Request = Class(name="Request")
Classes_Requests_Request = Class(name="Classes::Requests::Request")

# Classes_Bookables_Bookable class attributes and methods
Classes_Bookables_Bookable_baseprice: Property = Property(name="baseprice", type=FloatType)
Classes_Bookables_Bookable_id: Property = Property(name="id", type=StringType)
Classes_Bookables_Bookable_description: Property = Property(name="description", type=StringType)
Classes_Bookables_Bookable.attributes={Classes_Bookables_Bookable_id, Classes_Bookables_Bookable_description, Classes_Bookables_Bookable_baseprice}

# Classes_Bookables_Room class attributes and methods

# Bookable class attributes and methods

# RoomLocation class attributes and methods

# Classes_Bookables_RoomLocation class attributes and methods
Classes_Bookables_RoomLocation_floor: Property = Property(name="floor", type=StringType)
Classes_Bookables_RoomLocation_addtionalInfo: Property = Property(name="addtionalInfo", type=StringType)
Classes_Bookables_RoomLocation.attributes={Classes_Bookables_RoomLocation_floor, Classes_Bookables_RoomLocation_addtionalInfo}

# Classes_Bookables_ConferenceRoom class attributes and methods
Classes_Bookables_ConferenceRoom_category: Property = Property(name="category", type=StringType)
Classes_Bookables_ConferenceRoom_capacity: Property = Property(name="capacity", type=StringType)
Classes_Bookables_ConferenceRoom.attributes={Classes_Bookables_ConferenceRoom_category, Classes_Bookables_ConferenceRoom_capacity}

# Classes_Bookables_HostelBed class attributes and methods

# HotelRoom class attributes and methods

# Classes_Bookables_HotelRoom class attributes and methods
Classes_Bookables_HotelRoom_category: Property = Property(name="category", type=StringType)
Classes_Bookables_HotelRoom_nbrBeds: Property = Property(name="nbrBeds", type=StringType)
Classes_Bookables_HotelRoom.attributes={Classes_Bookables_HotelRoom_category, Classes_Bookables_HotelRoom_nbrBeds}

# Room class attributes and methods

# Classes_Bookables_IBookablesManage class attributes and methods
Classes_Bookables_IBookablesManage_m_changeRoomLocation: Method = Method(name="changeRoomLocation", parameters={Parameter(name='floor'), Parameter(name='roomID'), Parameter(name='additionalInfo')})
Classes_Bookables_IBookablesManage_m_changeHotelRoomCategory: Method = Method(name="changeHotelRoomCategory", parameters={Parameter(name='category'), Parameter(name='roomID')})
Classes_Bookables_IBookablesManage_m_changeConferenceRoomCategory: Method = Method(name="changeConferenceRoomCategory", parameters={Parameter(name='category'), Parameter(name='roomID')})
Classes_Bookables_IBookablesManage_m_changeHostelBedRoom: Method = Method(name="changeHostelBedRoom", parameters={Parameter(name='hostelBedID'), Parameter(name='roomID')})
Classes_Bookables_IBookablesManage_m_deleteBookable: Method = Method(name="deleteBookable", parameters={Parameter(name='bookableID')})
Classes_Bookables_IBookablesManage_m_addHostelBed: Method = Method(name="addHostelBed", parameters={Parameter(name='roomID'), Parameter(name='basePrice'), Parameter(name='description'), Parameter(name='bedNumber')}, type=StringType)
Classes_Bookables_IBookablesManage_m_addConferenceRoom: Method = Method(name="addConferenceRoom", parameters={Parameter(name='floor'), Parameter(name='capacity'), Parameter(name='description'), Parameter(name='roomNumber'), Parameter(name='basePrice'), Parameter(name='locationInfo'), Parameter(name='category')}, type=StringType)
Classes_Bookables_IBookablesManage_m_changeBookableBasePrice: Method = Method(name="changeBookableBasePrice", parameters={Parameter(name='bookableID'), Parameter(name='basePrice')})
Classes_Bookables_IBookablesManage_m_changeBookableDescription: Method = Method(name="changeBookableDescription", parameters={Parameter(name='description'), Parameter(name='bookableID')})
Classes_Bookables_IBookablesManage_m_addHotelRoom: Method = Method(name="addHotelRoom", parameters={Parameter(name='nbrBeds'), Parameter(name='floor'), Parameter(name='basePrice'), Parameter(name='locationInfo'), Parameter(name='category'), Parameter(name='roomNumber'), Parameter(name='description')}, type=StringType)
Classes_Bookables_IBookablesManage_m_changeHotelRoomNumberBeds: Method = Method(name="changeHotelRoomNumberBeds", parameters={Parameter(name='roomID'), Parameter(name='nbrBeds')})
Classes_Bookables_IBookablesManage_m_changeConferenceRoomCapacity: Method = Method(name="changeConferenceRoomCapacity", parameters={Parameter(name='roomID'), Parameter(name='capacity')})
Classes_Bookables_IBookablesManage.methods={Classes_Bookables_IBookablesManage_m_addConferenceRoom, Classes_Bookables_IBookablesManage_m_changeRoomLocation, Classes_Bookables_IBookablesManage_m_changeHotelRoomNumberBeds, Classes_Bookables_IBookablesManage_m_changeHostelBedRoom, Classes_Bookables_IBookablesManage_m_changeConferenceRoomCapacity, Classes_Bookables_IBookablesManage_m_changeBookableBasePrice, Classes_Bookables_IBookablesManage_m_changeConferenceRoomCategory, Classes_Bookables_IBookablesManage_m_changeBookableDescription, Classes_Bookables_IBookablesManage_m_changeHotelRoomCategory, Classes_Bookables_IBookablesManage_m_addHostelBed, Classes_Bookables_IBookablesManage_m_addHotelRoom, Classes_Bookables_IBookablesManage_m_deleteBookable}

# IBookablesAccess class attributes and methods

# Classes_Bookables_IBookablesAccess class attributes and methods
Classes_Bookables_IBookablesAccess_m_getRoomLocationInfo: Method = Method(name="getRoomLocationInfo", parameters={Parameter(name='roomID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getBookableDescription: Method = Method(name="getBookableDescription", parameters={Parameter(name='bookableID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getAllBookableIDs: Method = Method(name="getAllBookableIDs", parameters={}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getRoomOfHostelBed: Method = Method(name="getRoomOfHostelBed", parameters={Parameter(name='hostelBedID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getHotelRoomCategory: Method = Method(name="getHotelRoomCategory", parameters={Parameter(name='roomID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getConferenceRoomCapacity: Method = Method(name="getConferenceRoomCapacity", parameters={Parameter(name='roomID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getBookableBasePrice: Method = Method(name="getBookableBasePrice", parameters={Parameter(name='bookableID')}, type=FloatType)
Classes_Bookables_IBookablesAccess_m_searchHostelBeds: Method = Method(name="searchHostelBeds", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_searchConferenceRooms: Method = Method(name="searchConferenceRooms", parameters={Parameter(name='category'), Parameter(name='keyword')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getHotelRoomNbrBeds: Method = Method(name="getHotelRoomNbrBeds", parameters={Parameter(name='ID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_searchForBookable: Method = Method(name="searchForBookable", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getRoomLocationFloor: Method = Method(name="getRoomLocationFloor", parameters={Parameter(name='roomID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getAllHotelRoomIDs: Method = Method(name="getAllHotelRoomIDs", parameters={}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getAllConferenceRoomIDs: Method = Method(name="getAllConferenceRoomIDs", parameters={}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getAllHostelBedIDs: Method = Method(name="getAllHostelBedIDs", parameters={}, type=StringType)
Classes_Bookables_IBookablesAccess_m_getConferenceRoomCategory: Method = Method(name="getConferenceRoomCategory", parameters={Parameter(name='roomID')}, type=StringType)
Classes_Bookables_IBookablesAccess_m_searchHotelRooms: Method = Method(name="searchHotelRooms", parameters={Parameter(name='category'), Parameter(name='keyword')}, type=StringType)
Classes_Bookables_IBookablesAccess.methods={Classes_Bookables_IBookablesAccess_m_getBookableBasePrice, Classes_Bookables_IBookablesAccess_m_getRoomLocationFloor, Classes_Bookables_IBookablesAccess_m_getAllHostelBedIDs, Classes_Bookables_IBookablesAccess_m_getAllConferenceRoomIDs, Classes_Bookables_IBookablesAccess_m_getAllBookableIDs, Classes_Bookables_IBookablesAccess_m_searchConferenceRooms, Classes_Bookables_IBookablesAccess_m_getRoomOfHostelBed, Classes_Bookables_IBookablesAccess_m_getHotelRoomNbrBeds, Classes_Bookables_IBookablesAccess_m_searchForBookable, Classes_Bookables_IBookablesAccess_m_getAllHotelRoomIDs, Classes_Bookables_IBookablesAccess_m_getRoomLocationInfo, Classes_Bookables_IBookablesAccess_m_getConferenceRoomCapacity, Classes_Bookables_IBookablesAccess_m_getConferenceRoomCategory, Classes_Bookables_IBookablesAccess_m_searchHotelRooms, Classes_Bookables_IBookablesAccess_m_getBookableDescription, Classes_Bookables_IBookablesAccess_m_getHotelRoomCategory, Classes_Bookables_IBookablesAccess_m_searchHostelBeds}

# Classes_Bookables_BookablesManager class attributes and methods

# IBookablesManage class attributes and methods

# CreditCard class attributes and methods

# Classes_Stays_CreditCard class attributes and methods
Classes_Stays_CreditCard_ccNumber: Property = Property(name="ccNumber", type=StringType)
Classes_Stays_CreditCard_ccv: Property = Property(name="ccv", type=StringType)
Classes_Stays_CreditCard_expiryMonth: Property = Property(name="expiryMonth", type=StringType)
Classes_Stays_CreditCard_expiryYear: Property = Property(name="expiryYear", type=StringType)
Classes_Stays_CreditCard_firstName: Property = Property(name="firstName", type=StringType)
Classes_Stays_CreditCard_lastName: Property = Property(name="lastName", type=StringType)
Classes_Stays_CreditCard.attributes={Classes_Stays_CreditCard_ccv, Classes_Stays_CreditCard_lastName, Classes_Stays_CreditCard_expiryYear, Classes_Stays_CreditCard_ccNumber, Classes_Stays_CreditCard_expiryMonth, Classes_Stays_CreditCard_firstName}

# IStays class attributes and methods

# Classes_Stays_Stay class attributes and methods
Classes_Stays_Stay_checkedInGuests: Property = Property(name="checkedInGuests", type=StringType)
Classes_Stays_Stay_booking: Property = Property(name="booking", type=StringType)
Classes_Stays_Stay_checkedOutGuests: Property = Property(name="checkedOutGuests", type=StringType)
Classes_Stays_Stay_fromDate: Property = Property(name="fromDate", type=DateType)
Classes_Stays_Stay_toDate: Property = Property(name="toDate", type=DateType)
Classes_Stays_Stay_ID: Property = Property(name="ID", type=StringType)
Classes_Stays_Stay_bookable: Property = Property(name="bookable", type=StringType)
Classes_Stays_Stay_bills: Property = Property(name="bills", type=StringType)
Classes_Stays_Stay_m_addBill: Method = Method(name="addBill", parameters={Parameter(name='billID')})
Classes_Stays_Stay_m_addCheckedInGuest: Method = Method(name="addCheckedInGuest", parameters={Parameter(name='SSID')})
Classes_Stays_Stay_m_checkOutGuest: Method = Method(name="checkOutGuest", parameters={})
Classes_Stays_Stay.attributes={Classes_Stays_Stay_bookable, Classes_Stays_Stay_checkedInGuests, Classes_Stays_Stay_bills, Classes_Stays_Stay_toDate, Classes_Stays_Stay_booking, Classes_Stays_Stay_checkedOutGuests, Classes_Stays_Stay_fromDate, Classes_Stays_Stay_ID}
Classes_Stays_Stay.methods={Classes_Stays_Stay_m_checkOutGuest, Classes_Stays_Stay_m_addCheckedInGuest, Classes_Stays_Stay_m_addBill}

# IGuests class attributes and methods

# Classes_Stays_IStays class attributes and methods
Classes_Stays_IStays_m_checkInGuest: Method = Method(name="checkInGuest", parameters={Parameter(name='guestID'), Parameter(name='stayID')})
Classes_Stays_IStays_m_changeBookableOfStay: Method = Method(name="changeBookableOfStay", parameters={Parameter(name='stayID'), Parameter(name='bookableID')})
Classes_Stays_IStays_m_addNewStay: Method = Method(name="addNewStay", parameters={Parameter(name='bookingID'), Parameter(name='fromDate'), Parameter(name='toDate'), Parameter(name='bookableID')})
Classes_Stays_IStays_m_changeResponsibleCreditCard: Method = Method(name="changeResponsibleCreditCard", parameters={Parameter(name='stayID'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='ccNumber'), Parameter(name='expiryMonth'), Parameter(name='ccv'), Parameter(name='firstName')})
Classes_Stays_IStays_m_removeStay: Method = Method(name="removeStay", parameters={Parameter(name='stayID')})
Classes_Stays_IStays_m_addBillToStay: Method = Method(name="addBillToStay", parameters={Parameter(name='billID'), Parameter(name='stayID')})
Classes_Stays_IStays_m_checkOutGuest: Method = Method(name="checkOutGuest", parameters={Parameter(name='guestID'), Parameter(name='stayID')})
Classes_Stays_IStays_m_addResponsibleCreditCard: Method = Method(name="addResponsibleCreditCard", parameters={Parameter(name='ccv'), Parameter(name='stayID'), Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='ccNumber')})
Classes_Stays_IStays_m_getCheckedInGuestsOfHotelStay: Method = Method(name="getCheckedInGuestsOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_getCheckedOutGuestsOfHotelStay: Method = Method(name="getCheckedOutGuestsOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_searchHotelStays: Method = Method(name="searchHotelStays", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Stays_IStays_m_searchHotelStaysWithinPeriod: Method = Method(name="searchHotelStaysWithinPeriod", parameters={Parameter(name='to'), Parameter(name='from'), Parameter(name='keyword')}, type=StringType)
Classes_Stays_IStays_m_getGuestsOfHotelStay: Method = Method(name="getGuestsOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_getBillsOfHotelStay: Method = Method(name="getBillsOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_getBookableOfHotelStay: Method = Method(name="getBookableOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_getBookingOfHotelStay: Method = Method(name="getBookingOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_changePeriodOfStay: Method = Method(name="changePeriodOfStay", parameters={Parameter(name='to'), Parameter(name='from'), Parameter(name='stayID')})
Classes_Stays_IStays_m_getAllHotelStayIDs: Method = Method(name="getAllHotelStayIDs", parameters={}, type=StringType)
Classes_Stays_IStays_m_removeBillFromStay: Method = Method(name="removeBillFromStay", parameters={Parameter(name='billID'), Parameter(name='stayID')})
Classes_Stays_IStays_m_getAllHotelStaysWithinPeriod: Method = Method(name="getAllHotelStaysWithinPeriod", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Stays_IStays_m_getAllUnpayedBillsOfHotelStay: Method = Method(name="getAllUnpayedBillsOfHotelStay", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays_m_billCreditCardWithAllUnpaidBillsOfHotelStay: Method = Method(name="billCreditCardWithAllUnpaidBillsOfHotelStay", parameters={Parameter(name='stayID')})
Classes_Stays_IStays_m_isResponsibleCreditCardAdded: Method = Method(name="isResponsibleCreditCardAdded", parameters={Parameter(name='stayID')}, type=StringType)
Classes_Stays_IStays.methods={Classes_Stays_IStays_m_addBillToStay, Classes_Stays_IStays_m_removeStay, Classes_Stays_IStays_m_searchHotelStays, Classes_Stays_IStays_m_getAllUnpayedBillsOfHotelStay, Classes_Stays_IStays_m_checkOutGuest, Classes_Stays_IStays_m_getAllHotelStayIDs, Classes_Stays_IStays_m_getBillsOfHotelStay, Classes_Stays_IStays_m_checkInGuest, Classes_Stays_IStays_m_addNewStay, Classes_Stays_IStays_m_removeBillFromStay, Classes_Stays_IStays_m_getGuestsOfHotelStay, Classes_Stays_IStays_m_changeBookableOfStay, Classes_Stays_IStays_m_getCheckedInGuestsOfHotelStay, Classes_Stays_IStays_m_getBookingOfHotelStay, Classes_Stays_IStays_m_searchHotelStaysWithinPeriod, Classes_Stays_IStays_m_addResponsibleCreditCard, Classes_Stays_IStays_m_getBookableOfHotelStay, Classes_Stays_IStays_m_changeResponsibleCreditCard, Classes_Stays_IStays_m_changePeriodOfStay, Classes_Stays_IStays_m_billCreditCardWithAllUnpaidBillsOfHotelStay, Classes_Stays_IStays_m_isResponsibleCreditCardAdded, Classes_Stays_IStays_m_getAllHotelStaysWithinPeriod, Classes_Stays_IStays_m_getCheckedOutGuestsOfHotelStay}

# Classes_Stays_StaysManager class attributes and methods

# Stay class attributes and methods

# CustomerProvides class attributes and methods

# IBills class attributes and methods

# Classes_Banking_AdministratorProvides class attributes and methods
Classes_Banking_AdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='sum'), Parameter(name='ccv'), Parameter(name='lastName')}, type=FloatType)
Classes_Banking_AdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='ccv'), Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='firstName')}, type=BooleanType)
Classes_Banking_AdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='firstName')}, type=BooleanType)
Classes_Banking_AdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='ccNumber'), Parameter(name='firstName'), Parameter(name='ccv'), Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='expiryYear')}, type=FloatType)
Classes_Banking_AdministratorProvides.methods={Classes_Banking_AdministratorProvides_m_makeDeposit, Classes_Banking_AdministratorProvides_m_addCreditCard, Classes_Banking_AdministratorProvides_m_removeCreditCard, Classes_Banking_AdministratorProvides_m_getBalance}

# Classes_Banking_CustomerProvides class attributes and methods
Classes_Banking_CustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='ccNumber'), Parameter(name='expiryMonth'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='ccv'), Parameter(name='sum'), Parameter(name='expiryYear')}, type=BooleanType)
Classes_Banking_CustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='ccNumber'), Parameter(name='expiryYear'), Parameter(name='ccv')}, type=BooleanType)
Classes_Banking_CustomerProvides.methods={Classes_Banking_CustomerProvides_m_makePayment, Classes_Banking_CustomerProvides_m_isCreditCardValid}

# Classes_Bills_BillsManager class attributes and methods

# Bill class attributes and methods

# IInventoryAccess class attributes and methods

# IServicesAccess class attributes and methods

# Classes_Bills_Bill class attributes and methods
Classes_Bills_Bill_isPaid: Property = Property(name="isPaid", type=StringType)
Classes_Bills_Bill_paymentType: Property = Property(name="paymentType", type=StringType)
Classes_Bills_Bill_id: Property = Property(name="id", type=StringType)
Classes_Bills_Bill_items: Property = Property(name="items", type=StringType)
Classes_Bills_Bill_services: Property = Property(name="services", type=StringType)
Classes_Bills_Bill_bookable: Property = Property(name="bookable", type=StringType)
Classes_Bills_Bill_issueDate: Property = Property(name="issueDate", type=DateType)
Classes_Bills_Bill_paymentDate: Property = Property(name="paymentDate", type=DateType)
Classes_Bills_Bill_totalAmount: Property = Property(name="totalAmount", type=FloatType)
Classes_Bills_Bill_m_addService: Method = Method(name="addService", parameters={Parameter(name='serviceID')})
Classes_Bills_Bill_m_addItem: Method = Method(name="addItem", parameters={Parameter(name='itemID')})
Classes_Bills_Bill.attributes={Classes_Bills_Bill_paymentType, Classes_Bills_Bill_services, Classes_Bills_Bill_id, Classes_Bills_Bill_items, Classes_Bills_Bill_paymentDate, Classes_Bills_Bill_issueDate, Classes_Bills_Bill_totalAmount, Classes_Bills_Bill_isPaid, Classes_Bills_Bill_bookable}
Classes_Bills_Bill.methods={Classes_Bills_Bill_m_addService, Classes_Bills_Bill_m_addItem}

# Classes_Bills_IBills class attributes and methods
Classes_Bills_IBills_m_getAllPayedBills: Method = Method(name="getAllPayedBills", parameters={}, type=StringType)
Classes_Bills_IBills_m_addBill: Method = Method(name="addBill", parameters={Parameter(name='bookable'), Parameter(name='items'), Parameter(name='services')})
Classes_Bills_IBills_m_getIsBillPaid: Method = Method(name="getIsBillPaid", parameters={Parameter(name='billID')}, type=StringType)
Classes_Bills_IBills_m_getAllBillsNotPaid: Method = Method(name="getAllBillsNotPaid", parameters={}, type=StringType)
Classes_Bills_IBills_m_getBillPaymentDate: Method = Method(name="getBillPaymentDate", parameters={Parameter(name='billID')}, type=DateType)
Classes_Bills_IBills_m_getAllBillIDs: Method = Method(name="getAllBillIDs", parameters={}, type=StringType)
Classes_Bills_IBills_m_searchBills: Method = Method(name="searchBills", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Bills_IBills_m_payBillsWithCreditCard: Method = Method(name="payBillsWithCreditCard", parameters={Parameter(name='ccv'), Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='bills'), Parameter(name='expiryMonth'), Parameter(name='expiryYear')})
Classes_Bills_IBills_m_getBillItems: Method = Method(name="getBillItems", parameters={Parameter(name='billID')}, type=StringType)
Classes_Bills_IBills_m_getBillBookable: Method = Method(name="getBillBookable", parameters={Parameter(name='billID')}, type=StringType)
Classes_Bills_IBills_m_getBillServices: Method = Method(name="getBillServices", parameters={Parameter(name='billID')}, type=StringType)
Classes_Bills_IBills_m_getBillIssueDate: Method = Method(name="getBillIssueDate", parameters={Parameter(name='billID')}, type=DateType)
Classes_Bills_IBills_m_getBillPaymentType: Method = Method(name="getBillPaymentType", parameters={Parameter(name='billID')}, type=StringType)
Classes_Bills_IBills_m_payBillsWithCash: Method = Method(name="payBillsWithCash", parameters={Parameter(name='bills')})
Classes_Bills_IBills_m_sendInvoice: Method = Method(name="sendInvoice", parameters={Parameter(name='email'), Parameter(name='billID')})
Classes_Bills_IBills_m_removeBill: Method = Method(name="removeBill", parameters={Parameter(name='billID')})
Classes_Bills_IBills_m_getBillTotalAmount: Method = Method(name="getBillTotalAmount", parameters={Parameter(name='billID')}, type=FloatType)
Classes_Bills_IBills.methods={Classes_Bills_IBills_m_getBillPaymentType, Classes_Bills_IBills_m_getAllBillIDs, Classes_Bills_IBills_m_getAllPayedBills, Classes_Bills_IBills_m_getBillPaymentDate, Classes_Bills_IBills_m_getIsBillPaid, Classes_Bills_IBills_m_getAllBillsNotPaid, Classes_Bills_IBills_m_removeBill, Classes_Bills_IBills_m_getBillServices, Classes_Bills_IBills_m_searchBills, Classes_Bills_IBills_m_addBill, Classes_Bills_IBills_m_getBillIssueDate, Classes_Bills_IBills_m_sendInvoice, Classes_Bills_IBills_m_payBillsWithCreditCard, Classes_Bills_IBills_m_getBillItems, Classes_Bills_IBills_m_getBillTotalAmount, Classes_Bills_IBills_m_payBillsWithCash, Classes_Bills_IBills_m_getBillBookable}

# Classes_Inventory_IManageInventory class attributes and methods
Classes_Inventory_IManageInventory_m_addItem: Method = Method(name="addItem", parameters={Parameter(name='price'), Parameter(name='stock'), Parameter(name='expense'), Parameter(name='name')})
Classes_Inventory_IManageInventory_m_changeItemName: Method = Method(name="changeItemName", parameters={Parameter(name='name'), Parameter(name='id')})
Classes_Inventory_IManageInventory_m_changeItemPrice: Method = Method(name="changeItemPrice", parameters={Parameter(name='price'), Parameter(name='id')})
Classes_Inventory_IManageInventory_m_changeItemExpense: Method = Method(name="changeItemExpense", parameters={Parameter(name='expense'), Parameter(name='id')})
Classes_Inventory_IManageInventory_m_removeItem: Method = Method(name="removeItem", parameters={Parameter(name='id')})
Classes_Inventory_IManageInventory.methods={Classes_Inventory_IManageInventory_m_addItem, Classes_Inventory_IManageInventory_m_changeItemExpense, Classes_Inventory_IManageInventory_m_changeItemPrice, Classes_Inventory_IManageInventory_m_changeItemName, Classes_Inventory_IManageInventory_m_removeItem}

# Classes_Inventory_InventoryManager class attributes and methods

# IManageInventory class attributes and methods

# Item class attributes and methods

# Classes_Inventory_Item class attributes and methods
Classes_Inventory_Item_name: Property = Property(name="name", type=StringType)
Classes_Inventory_Item_price: Property = Property(name="price", type=FloatType)
Classes_Inventory_Item_expense: Property = Property(name="expense", type=FloatType)
Classes_Inventory_Item_stock: Property = Property(name="stock", type=StringType)
Classes_Inventory_Item_id: Property = Property(name="id", type=StringType)
Classes_Inventory_Item.attributes={Classes_Inventory_Item_id, Classes_Inventory_Item_price, Classes_Inventory_Item_name, Classes_Inventory_Item_expense, Classes_Inventory_Item_stock}

# Classes_Inventory_IInventoryAccess class attributes and methods
Classes_Inventory_IInventoryAccess_m_changeItemStock: Method = Method(name="changeItemStock", parameters={Parameter(name='stock'), Parameter(name='id')})
Classes_Inventory_IInventoryAccess_m_getItemPrice: Method = Method(name="getItemPrice", parameters={Parameter(name='id')}, type=FloatType)
Classes_Inventory_IInventoryAccess_m_getItemStock: Method = Method(name="getItemStock", parameters={Parameter(name='id')}, type=StringType)
Classes_Inventory_IInventoryAccess_m_getItemName: Method = Method(name="getItemName", parameters={Parameter(name='id')}, type=StringType)
Classes_Inventory_IInventoryAccess_m_getItemExpense: Method = Method(name="getItemExpense", parameters={Parameter(name='id')}, type=FloatType)
Classes_Inventory_IInventoryAccess_m_getAllItemIDs: Method = Method(name="getAllItemIDs", parameters={}, type=StringType)
Classes_Inventory_IInventoryAccess_m_searchItems: Method = Method(name="searchItems", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Inventory_IInventoryAccess.methods={Classes_Inventory_IInventoryAccess_m_searchItems, Classes_Inventory_IInventoryAccess_m_getItemName, Classes_Inventory_IInventoryAccess_m_getItemStock, Classes_Inventory_IInventoryAccess_m_getItemPrice, Classes_Inventory_IInventoryAccess_m_getAllItemIDs, Classes_Inventory_IInventoryAccess_m_getItemExpense, Classes_Inventory_IInventoryAccess_m_changeItemStock}

# Classes_Services_RoomServiceMenu class attributes and methods
Classes_Services_RoomServiceMenu_name: Property = Property(name="name", type=StringType)
Classes_Services_RoomServiceMenu_items: Property = Property(name="items", type=StringType)
Classes_Services_RoomServiceMenu_m_addItem: Method = Method(name="addItem", parameters={Parameter(name='itemID')})
Classes_Services_RoomServiceMenu_m_removeItem: Method = Method(name="removeItem", parameters={Parameter(name='itemID')})
Classes_Services_RoomServiceMenu.attributes={Classes_Services_RoomServiceMenu_items, Classes_Services_RoomServiceMenu_name}
Classes_Services_RoomServiceMenu.methods={Classes_Services_RoomServiceMenu_m_addItem, Classes_Services_RoomServiceMenu_m_removeItem}

# Classes_Services_ServiceManager class attributes and methods

# IServicesManage class attributes and methods

# Service class attributes and methods

# RoomServiceOrder class attributes and methods

# RoomServiceMenu class attributes and methods

# Classes_Services_Service class attributes and methods
Classes_Services_Service_name: Property = Property(name="name", type=StringType)
Classes_Services_Service_price: Property = Property(name="price", type=FloatType)
Classes_Services_Service_expense: Property = Property(name="expense", type=FloatType)
Classes_Services_Service_id: Property = Property(name="id", type=StringType)
Classes_Services_Service.attributes={Classes_Services_Service_expense, Classes_Services_Service_price, Classes_Services_Service_id, Classes_Services_Service_name}

# Classes_Services_RoomServiceOrder class attributes and methods
Classes_Services_RoomServiceOrder_isDelivered: Property = Property(name="isDelivered", type=StringType)
Classes_Services_RoomServiceOrder_deliveryDate: Property = Property(name="deliveryDate", type=DateType)
Classes_Services_RoomServiceOrder_bookable: Property = Property(name="bookable", type=StringType)
Classes_Services_RoomServiceOrder_items: Property = Property(name="items", type=StringType)
Classes_Services_RoomServiceOrder_id: Property = Property(name="id", type=StringType)
Classes_Services_RoomServiceOrder_bill: Property = Property(name="bill", type=StringType)
Classes_Services_RoomServiceOrder_m_addService: Method = Method(name="addService", parameters={})
Classes_Services_RoomServiceOrder_m_addItem: Method = Method(name="addItem", parameters={})
Classes_Services_RoomServiceOrder_m_removeItem: Method = Method(name="removeItem", parameters={})
Classes_Services_RoomServiceOrder_m_removeService: Method = Method(name="removeService", parameters={})
Classes_Services_RoomServiceOrder.attributes={Classes_Services_RoomServiceOrder_id, Classes_Services_RoomServiceOrder_isDelivered, Classes_Services_RoomServiceOrder_bill, Classes_Services_RoomServiceOrder_deliveryDate, Classes_Services_RoomServiceOrder_items, Classes_Services_RoomServiceOrder_bookable}
Classes_Services_RoomServiceOrder.methods={Classes_Services_RoomServiceOrder_m_addItem, Classes_Services_RoomServiceOrder_m_removeService, Classes_Services_RoomServiceOrder_m_removeItem, Classes_Services_RoomServiceOrder_m_addService}

# Classes_Services_IServicesManage class attributes and methods
Classes_Services_IServicesManage_m_changeServiceName: Method = Method(name="changeServiceName", parameters={Parameter(name='serviceID'), Parameter(name='name')})
Classes_Services_IServicesManage_m_changeServicePrice: Method = Method(name="changeServicePrice", parameters={Parameter(name='serviceID'), Parameter(name='price')})
Classes_Services_IServicesManage_m_changeServiceExpense: Method = Method(name="changeServiceExpense", parameters={Parameter(name='expense'), Parameter(name='serviceID')})
Classes_Services_IServicesManage_m_addRoomServiceMenuItem: Method = Method(name="addRoomServiceMenuItem", parameters={Parameter(name='itemID')})
Classes_Services_IServicesManage_m_removeRoomServiceMenuItem: Method = Method(name="removeRoomServiceMenuItem", parameters={Parameter(name='itemID')})
Classes_Services_IServicesManage_m_changeRoomServiceMenuName: Method = Method(name="changeRoomServiceMenuName", parameters={Parameter(name='name')})
Classes_Services_IServicesManage_m_addService: Method = Method(name="addService", parameters={Parameter(name='name'), Parameter(name='price'), Parameter(name='expense')})
Classes_Services_IServicesManage.methods={Classes_Services_IServicesManage_m_addService, Classes_Services_IServicesManage_m_changeServiceName, Classes_Services_IServicesManage_m_changeServiceExpense, Classes_Services_IServicesManage_m_removeRoomServiceMenuItem, Classes_Services_IServicesManage_m_addRoomServiceMenuItem, Classes_Services_IServicesManage_m_changeServicePrice, Classes_Services_IServicesManage_m_changeRoomServiceMenuName}

# Classes_Services_IServicesAccess class attributes and methods
Classes_Services_IServicesAccess_m_getAllServiceIDs: Method = Method(name="getAllServiceIDs", parameters={}, type=StringType)
Classes_Services_IServicesAccess_m_getAllRoomServiceOrderIDs: Method = Method(name="getAllRoomServiceOrderIDs", parameters={}, type=StringType)
Classes_Services_IServicesAccess_m_searchServices: Method = Method(name="searchServices", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Services_IServicesAccess_m_searchRoomServiceOrders: Method = Method(name="searchRoomServiceOrders", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Services_IServicesAccess_m_getServiceName: Method = Method(name="getServiceName", parameters={Parameter(name='serviceID')}, type=StringType)
Classes_Services_IServicesAccess_m_getServicePrice: Method = Method(name="getServicePrice", parameters={Parameter(name='serviceID')}, type=FloatType)
Classes_Services_IServicesAccess_m_getServiceExpense: Method = Method(name="getServiceExpense", parameters={Parameter(name='serviceID')}, type=FloatType)
Classes_Services_IServicesAccess_m_isRSODelivered: Method = Method(name="isRSODelivered", parameters={Parameter(name='orderID')}, type=StringType)
Classes_Services_IServicesAccess_m_getRSODeliveryDate: Method = Method(name="getRSODeliveryDate", parameters={Parameter(name='orderID')}, type=DateType)
Classes_Services_IServicesAccess_m_getRSOBookable: Method = Method(name="getRSOBookable", parameters={Parameter(name='orderID')}, type=StringType)
Classes_Services_IServicesAccess_m_getRSOItems: Method = Method(name="getRSOItems", parameters={Parameter(name='orderID')}, type=StringType)
Classes_Services_IServicesAccess_m_getRSOServices: Method = Method(name="getRSOServices", parameters={Parameter(name='orderID')}, type=StringType)
Classes_Services_IServicesAccess_m_changeRSOISDelivered: Method = Method(name="changeRSOISDelivered", parameters={Parameter(name='isDelivered'), Parameter(name='orderID')})
Classes_Services_IServicesAccess_m_changeRSODeliveryDate: Method = Method(name="changeRSODeliveryDate", parameters={Parameter(name='date'), Parameter(name='orderID')})
Classes_Services_IServicesAccess_m_getRoomServiceMenuName: Method = Method(name="getRoomServiceMenuName", parameters={}, type=StringType)
Classes_Services_IServicesAccess_m_getRoomServiceMenuItems: Method = Method(name="getRoomServiceMenuItems", parameters={}, type=StringType)
Classes_Services_IServicesAccess_m_setRSOBill: Method = Method(name="setRSOBill", parameters={Parameter(name='billID'), Parameter(name='orderID')})
Classes_Services_IServicesAccess_m_getRSOBill: Method = Method(name="getRSOBill", parameters={Parameter(name='orderID')}, type=StringType)
Classes_Services_IServicesAccess_m_makeRoomServiceOrder: Method = Method(name="makeRoomServiceOrder", parameters={Parameter(name='services'), Parameter(name='isDelivered'), Parameter(name='bill'), Parameter(name='bookable'), Parameter(name='deliveryDate'), Parameter(name='items')})
Classes_Services_IServicesAccess.methods={Classes_Services_IServicesAccess_m_getRoomServiceMenuName, Classes_Services_IServicesAccess_m_setRSOBill, Classes_Services_IServicesAccess_m_makeRoomServiceOrder, Classes_Services_IServicesAccess_m_getRoomServiceMenuItems, Classes_Services_IServicesAccess_m_changeRSODeliveryDate, Classes_Services_IServicesAccess_m_getAllServiceIDs, Classes_Services_IServicesAccess_m_changeRSOISDelivered, Classes_Services_IServicesAccess_m_getRSOItems, Classes_Services_IServicesAccess_m_getRSOBookable, Classes_Services_IServicesAccess_m_isRSODelivered, Classes_Services_IServicesAccess_m_getRSOServices, Classes_Services_IServicesAccess_m_getRSOBill, Classes_Services_IServicesAccess_m_getServicePrice, Classes_Services_IServicesAccess_m_getServiceName, Classes_Services_IServicesAccess_m_searchServices, Classes_Services_IServicesAccess_m_getServiceExpense, Classes_Services_IServicesAccess_m_searchRoomServiceOrders, Classes_Services_IServicesAccess_m_getRSODeliveryDate, Classes_Services_IServicesAccess_m_getAllRoomServiceOrderIDs}

# Classes_Guests_GuestsManager class attributes and methods

# Guest class attributes and methods

# IManageAccounts class attributes and methods

# Classes_Guests_Guest class attributes and methods
Classes_Guests_Guest_firstname: Property = Property(name="firstname", type=StringType)
Classes_Guests_Guest_lastname: Property = Property(name="lastname", type=StringType)
Classes_Guests_Guest_title: Property = Property(name="title", type=StringType)
Classes_Guests_Guest_email: Property = Property(name="email", type=StringType)
Classes_Guests_Guest_phone: Property = Property(name="phone", type=StringType)
Classes_Guests_Guest_ssid: Property = Property(name="ssid", type=StringType)
Classes_Guests_Guest_requests: Property = Property(name="requests", type=StringType)
Classes_Guests_Guest_stays: Property = Property(name="stays", type=StringType)
Classes_Guests_Guest_account: Property = Property(name="account", type=StringType)
Classes_Guests_Guest_m_addStay: Method = Method(name="addStay", parameters={Parameter(name='bookingID'), Parameter(name='bookableID'), Parameter(name='fromDate'), Parameter(name='toDate')})
Classes_Guests_Guest_m_removeStay: Method = Method(name="removeStay", parameters={Parameter(name='stayID')})
Classes_Guests_Guest_m_addRequest: Method = Method(name="addRequest", parameters={Parameter(name='requestID'), Parameter(name='description')})
Classes_Guests_Guest_m_removeRequest: Method = Method(name="removeRequest", parameters={Parameter(name='requestID')})
Classes_Guests_Guest.attributes={Classes_Guests_Guest_email, Classes_Guests_Guest_title, Classes_Guests_Guest_ssid, Classes_Guests_Guest_requests, Classes_Guests_Guest_firstname, Classes_Guests_Guest_phone, Classes_Guests_Guest_lastname, Classes_Guests_Guest_stays, Classes_Guests_Guest_account}
Classes_Guests_Guest.methods={Classes_Guests_Guest_m_addRequest, Classes_Guests_Guest_m_removeRequest, Classes_Guests_Guest_m_removeStay, Classes_Guests_Guest_m_addStay}

# Classes_Guests_IGuests class attributes and methods
Classes_Guests_IGuests_m_getAllGuestIDs: Method = Method(name="getAllGuestIDs", parameters={}, type=StringType)
Classes_Guests_IGuests_m_addGuest: Method = Method(name="addGuest", parameters={Parameter(name='title'), Parameter(name='phone'), Parameter(name='firstname'), Parameter(name='SSID'), Parameter(name='lastname'), Parameter(name='email')})
Classes_Guests_IGuests_m_changeGuestFirstName: Method = Method(name="changeGuestFirstName", parameters={Parameter(name='SSID'), Parameter(name='firstName')})
Classes_Guests_IGuests_m_getGuestRequests: Method = Method(name="getGuestRequests", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_changeGuestLastName: Method = Method(name="changeGuestLastName", parameters={Parameter(name='lastName'), Parameter(name='SSID')})
Classes_Guests_IGuests_m_changeGuestTitle: Method = Method(name="changeGuestTitle", parameters={Parameter(name='SSID'), Parameter(name='title')})
Classes_Guests_IGuests_m_changeGuestEmail: Method = Method(name="changeGuestEmail", parameters={Parameter(name='eMail'), Parameter(name='SSID')})
Classes_Guests_IGuests_m_changeGuestPhone: Method = Method(name="changeGuestPhone", parameters={Parameter(name='SSID'), Parameter(name='phoneNr')})
Classes_Guests_IGuests_m_getGuestFirstName: Method = Method(name="getGuestFirstName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_getGuestLastName: Method = Method(name="getGuestLastName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_getGuestTitle: Method = Method(name="getGuestTitle", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_getGuestEmail: Method = Method(name="getGuestEmail", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_getGuestPhone: Method = Method(name="getGuestPhone", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_searchGuests: Method = Method(name="searchGuests", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Guests_IGuests_m_getGuestStays: Method = Method(name="getGuestStays", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_removeGuestStay: Method = Method(name="removeGuestStay", parameters={Parameter(name='SSID'), Parameter(name='stayID')})
Classes_Guests_IGuests_m_addGuestRequest: Method = Method(name="addGuestRequest", parameters={Parameter(name='SSID'), Parameter(name='desctiption'), Parameter(name='requestID')})
Classes_Guests_IGuests_m_removeGuestRequest: Method = Method(name="removeGuestRequest", parameters={Parameter(name='requestID'), Parameter(name='SSID')})
Classes_Guests_IGuests_m_getGuestAccountUsername: Method = Method(name="getGuestAccountUsername", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_getGuestAccountPassword: Method = Method(name="getGuestAccountPassword", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Guests_IGuests_m_generateGuestAccount: Method = Method(name="generateGuestAccount", parameters={Parameter(name='SSID')})
Classes_Guests_IGuests_m_removeGuestAccount: Method = Method(name="removeGuestAccount", parameters={Parameter(name='SSID')})
Classes_Guests_IGuests.methods={Classes_Guests_IGuests_m_changeGuestEmail, Classes_Guests_IGuests_m_getGuestTitle, Classes_Guests_IGuests_m_getGuestFirstName, Classes_Guests_IGuests_m_changeGuestLastName, Classes_Guests_IGuests_m_changeGuestTitle, Classes_Guests_IGuests_m_getGuestRequests, Classes_Guests_IGuests_m_changeGuestPhone, Classes_Guests_IGuests_m_generateGuestAccount, Classes_Guests_IGuests_m_getGuestStays, Classes_Guests_IGuests_m_removeGuestRequest, Classes_Guests_IGuests_m_getGuestAccountUsername, Classes_Guests_IGuests_m_getGuestLastName, Classes_Guests_IGuests_m_getGuestAccountPassword, Classes_Guests_IGuests_m_removeGuestStay, Classes_Guests_IGuests_m_changeGuestFirstName, Classes_Guests_IGuests_m_removeGuestAccount, Classes_Guests_IGuests_m_getAllGuestIDs, Classes_Guests_IGuests_m_addGuest, Classes_Guests_IGuests_m_getGuestEmail, Classes_Guests_IGuests_m_addGuestRequest, Classes_Guests_IGuests_m_getGuestPhone, Classes_Guests_IGuests_m_searchGuests}

# Classes_Accounts_Account class attributes and methods
Classes_Accounts_Account_accountType: Property = Property(name="accountType", type=StringType)
Classes_Accounts_Account_username: Property = Property(name="username", type=StringType)
Classes_Accounts_Account_password: Property = Property(name="password", type=StringType)
Classes_Accounts_Account.attributes={Classes_Accounts_Account_password, Classes_Accounts_Account_username, Classes_Accounts_Account_accountType}

# Classes_Accounts_AccountsManager class attributes and methods

# Accounts_IManageAccounts class attributes and methods

# Accounts_IAccountsAccess class attributes and methods

# Account class attributes and methods

# Classes_Accounts_IAccountsAccess class attributes and methods
Classes_Accounts_IAccountsAccess_m_validateAccount: Method = Method(name="validateAccount", parameters={Parameter(name='password'), Parameter(name='username')}, type=StringType)
Classes_Accounts_IAccountsAccess_m_login: Method = Method(name="login", parameters={Parameter(name='password'), Parameter(name='username')}, type=StringType)
Classes_Accounts_IAccountsAccess.methods={Classes_Accounts_IAccountsAccess_m_validateAccount, Classes_Accounts_IAccountsAccess_m_login}

# Classes_Accounts_IManageAccounts class attributes and methods
Classes_Accounts_IManageAccounts_m_addAccount: Method = Method(name="addAccount", parameters={Parameter(name='password'), Parameter(name='type'), Parameter(name='username')})
Classes_Accounts_IManageAccounts_m_deleteAccount: Method = Method(name="deleteAccount", parameters={Parameter(name='username')})
Classes_Accounts_IManageAccounts_m_renameAccount: Method = Method(name="renameAccount", parameters={Parameter(name='oldUsername'), Parameter(name='newUsername')})
Classes_Accounts_IManageAccounts_m_changePassword: Method = Method(name="changePassword", parameters={Parameter(name='username'), Parameter(name='newPassword')})
Classes_Accounts_IManageAccounts_m_getAccountPassword: Method = Method(name="getAccountPassword", parameters={Parameter(name='username')}, type=StringType)
Classes_Accounts_IManageAccounts_m_getAccountName: Method = Method(name="getAccountName", parameters={Parameter(name='username')}, type=StringType)
Classes_Accounts_IManageAccounts_m_searchAccounts: Method = Method(name="searchAccounts", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Accounts_IManageAccounts.methods={Classes_Accounts_IManageAccounts_m_addAccount, Classes_Accounts_IManageAccounts_m_renameAccount, Classes_Accounts_IManageAccounts_m_searchAccounts, Classes_Accounts_IManageAccounts_m_changePassword, Classes_Accounts_IManageAccounts_m_getAccountName, Classes_Accounts_IManageAccounts_m_getAccountPassword, Classes_Accounts_IManageAccounts_m_deleteAccount}

# Classes_Bookings_Booking class attributes and methods
Classes_Bookings_Booking_customer: Property = Property(name="customer", type=StringType)
Classes_Bookings_Booking_bookedStays: Property = Property(name="bookedStays", type=StringType)
Classes_Bookings_Booking_bookingNbr: Property = Property(name="bookingNbr", type=StringType)
Classes_Bookings_Booking_nbrGuests: Property = Property(name="nbrGuests", type=StringType)
Classes_Bookings_Booking_issueDate: Property = Property(name="issueDate", type=DateType)
Classes_Bookings_Booking_requests: Property = Property(name="requests", type=StringType)
Classes_Bookings_Booking_m_addBookedStay: Method = Method(name="addBookedStay", parameters={Parameter(name='stayID')})
Classes_Bookings_Booking_m_cancelBookedStay: Method = Method(name="cancelBookedStay", parameters={Parameter(name='stayID')})
Classes_Bookings_Booking_m_addRequest: Method = Method(name="addRequest", parameters={Parameter(name='requestID')})
Classes_Bookings_Booking_m_removeRequest: Method = Method(name="removeRequest", parameters={Parameter(name='requestID')})
Classes_Bookings_Booking.attributes={Classes_Bookings_Booking_bookedStays, Classes_Bookings_Booking_issueDate, Classes_Bookings_Booking_bookingNbr, Classes_Bookings_Booking_customer, Classes_Bookings_Booking_requests, Classes_Bookings_Booking_nbrGuests}
Classes_Bookings_Booking.methods={Classes_Bookings_Booking_m_removeRequest, Classes_Bookings_Booking_m_addBookedStay, Classes_Bookings_Booking_m_cancelBookedStay, Classes_Bookings_Booking_m_addRequest}

# Classes_Bookings_BookingsManager class attributes and methods

# IBookings class attributes and methods

# Booking class attributes and methods

# ICustomers class attributes and methods

# Classes_Bookings_IBookings class attributes and methods
Classes_Bookings_IBookings_m_makeBooking: Method = Method(name="makeBooking", parameters={Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='guests'), Parameter(name='firstName'), Parameter(name='requests'), Parameter(name='expiryMonth'), Parameter(name='ccNumber'), Parameter(name='bookables'), Parameter(name='customerID'), Parameter(name='lastName')})
Classes_Bookings_IBookings_m_searchBookings: Method = Method(name="searchBookings", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Bookings_IBookings_m_getBookedStaysOfBooking: Method = Method(name="getBookedStaysOfBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_Bookings_IBookings_m_getCustomerOfBooking: Method = Method(name="getCustomerOfBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_Bookings_IBookings_m_getNbrGuestOfBooking: Method = Method(name="getNbrGuestOfBooking", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_Bookings_IBookings_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='bookingID')})
Classes_Bookings_IBookings_m_cancelStayOfBooking: Method = Method(name="cancelStayOfBooking", parameters={Parameter(name='bookingID'), Parameter(name='stayID')})
Classes_Bookings_IBookings_m_addBookedStayToBooking: Method = Method(name="addBookedStayToBooking", parameters={Parameter(name='stayID'), Parameter(name='bookingID')})
Classes_Bookings_IBookings_m_changeNbrGuestsOfBooking: Method = Method(name="changeNbrGuestsOfBooking", parameters={Parameter(name='bookingID'), Parameter(name='nbrGuests')})
Classes_Bookings_IBookings_m_getAllBookings: Method = Method(name="getAllBookings", parameters={}, type=StringType)
Classes_Bookings_IBookings_m_getAllBookingsWithinPeriod: Method = Method(name="getAllBookingsWithinPeriod", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Bookings_IBookings_m_getAllBookingsWithStaysInPeriod: Method = Method(name="getAllBookingsWithStaysInPeriod", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_searchBookingsMadeInPeriod: Method = Method(name="searchBookingsMadeInPeriod", parameters={Parameter(name='keyword'), Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_searchBookingsWithStaysInPeriod: Method = Method(name="searchBookingsWithStaysInPeriod", parameters={Parameter(name='to'), Parameter(name='from'), Parameter(name='keyword')}, type=StringType)
Classes_Bookings_IBookings_m_searchForAvailableBookablesInPeriod: Method = Method(name="searchForAvailableBookablesInPeriod", parameters={Parameter(name='to'), Parameter(name='keyword'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_getAvailableBookablesInPeriod: Method = Method(name="getAvailableBookablesInPeriod", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_addBookingRequest: Method = Method(name="addBookingRequest", parameters={Parameter(name='bookingID'), Parameter(name='requestID')})
Classes_Bookings_IBookings_m_removeBookingRequest: Method = Method(name="removeBookingRequest", parameters={Parameter(name='bookingID'), Parameter(name='requestID')})
Classes_Bookings_IBookings_m_getBookingRequests: Method = Method(name="getBookingRequests", parameters={Parameter(name='bookingID')}, type=StringType)
Classes_Bookings_IBookings_m_payBookingBills: Method = Method(name="payBookingBills", parameters={Parameter(name='bookingID')})
Classes_Bookings_IBookings_m_payStayBills: Method = Method(name="payStayBills", parameters={Parameter(name='stayID'), Parameter(name='bookingID')})
Classes_Bookings_IBookings_m_searchForAvailableHotelRoomsInPeriod: Method = Method(name="searchForAvailableHotelRoomsInPeriod", parameters={Parameter(name='keyword'), Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_searchForAvailableHostelBedsInPeriod: Method = Method(name="searchForAvailableHostelBedsInPeriod", parameters={Parameter(name='to'), Parameter(name='keyword'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_searchForAvailableConferenceRoomsInPeriod: Method = Method(name="searchForAvailableConferenceRoomsInPeriod", parameters={Parameter(name='keyword'), Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Bookings_IBookings_m_getAvailableHotelRoomsInPeriod: Method = Method(name="getAvailableHotelRoomsInPeriod", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Bookings_IBookings_m_getAvailableConferenceRoomsInPeriod: Method = Method(name="getAvailableConferenceRoomsInPeriod", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Bookings_IBookings_m_getAvailableHostelBedsInPeriod: Method = Method(name="getAvailableHostelBedsInPeriod", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Bookings_IBookings.methods={Classes_Bookings_IBookings_m_removeBookingRequest, Classes_Bookings_IBookings_m_getAllBookingsWithinPeriod, Classes_Bookings_IBookings_m_payBookingBills, Classes_Bookings_IBookings_m_getNbrGuestOfBooking, Classes_Bookings_IBookings_m_makeBooking, Classes_Bookings_IBookings_m_getAvailableConferenceRoomsInPeriod, Classes_Bookings_IBookings_m_searchForAvailableConferenceRoomsInPeriod, Classes_Bookings_IBookings_m_getCustomerOfBooking, Classes_Bookings_IBookings_m_cancelBooking, Classes_Bookings_IBookings_m_searchBookingsWithStaysInPeriod, Classes_Bookings_IBookings_m_getAvailableHostelBedsInPeriod, Classes_Bookings_IBookings_m_cancelStayOfBooking, Classes_Bookings_IBookings_m_getAllBookings, Classes_Bookings_IBookings_m_addBookedStayToBooking, Classes_Bookings_IBookings_m_searchBookingsMadeInPeriod, Classes_Bookings_IBookings_m_getBookingRequests, Classes_Bookings_IBookings_m_getAvailableHotelRoomsInPeriod, Classes_Bookings_IBookings_m_searchForAvailableHostelBedsInPeriod, Classes_Bookings_IBookings_m_getAvailableBookablesInPeriod, Classes_Bookings_IBookings_m_addBookingRequest, Classes_Bookings_IBookings_m_getAllBookingsWithStaysInPeriod, Classes_Bookings_IBookings_m_searchForAvailableHotelRoomsInPeriod, Classes_Bookings_IBookings_m_changeNbrGuestsOfBooking, Classes_Bookings_IBookings_m_payStayBills, Classes_Bookings_IBookings_m_searchBookings, Classes_Bookings_IBookings_m_getBookedStaysOfBooking, Classes_Bookings_IBookings_m_searchForAvailableBookablesInPeriod}

# Classes_Customers_CustomersManager class attributes and methods

# Customer class attributes and methods

# Classes_Customers_Customer class attributes and methods
Classes_Customers_Customer_firstname: Property = Property(name="firstname", type=StringType)
Classes_Customers_Customer_lastname: Property = Property(name="lastname", type=StringType)
Classes_Customers_Customer_title: Property = Property(name="title", type=StringType)
Classes_Customers_Customer_email: Property = Property(name="email", type=StringType)
Classes_Customers_Customer_phone: Property = Property(name="phone", type=StringType)
Classes_Customers_Customer_ssid: Property = Property(name="ssid", type=StringType)
Classes_Customers_Customer_bookings: Property = Property(name="bookings", type=StringType)
Classes_Customers_Customer_requests: Property = Property(name="requests", type=StringType)
Classes_Customers_Customer_m_removeRequest: Method = Method(name="removeRequest", parameters={})
Classes_Customers_Customer_m_addBooking: Method = Method(name="addBooking", parameters={})
Classes_Customers_Customer_m_removeBooking: Method = Method(name="removeBooking", parameters={})
Classes_Customers_Customer_m_addRequest: Method = Method(name="addRequest", parameters={})
Classes_Customers_Customer.attributes={Classes_Customers_Customer_title, Classes_Customers_Customer_requests, Classes_Customers_Customer_firstname, Classes_Customers_Customer_bookings, Classes_Customers_Customer_email, Classes_Customers_Customer_phone, Classes_Customers_Customer_ssid, Classes_Customers_Customer_lastname}
Classes_Customers_Customer.methods={Classes_Customers_Customer_m_removeRequest, Classes_Customers_Customer_m_addRequest, Classes_Customers_Customer_m_removeBooking, Classes_Customers_Customer_m_addBooking}

# Classes_Customers_ICustomers class attributes and methods
Classes_Customers_ICustomers_m_getAllCustomers: Method = Method(name="getAllCustomers", parameters={}, type=StringType)
Classes_Customers_ICustomers_m_addCustomer: Method = Method(name="addCustomer", parameters={Parameter(name='email'), Parameter(name='lastname'), Parameter(name='SSID'), Parameter(name='firstname'), Parameter(name='phone'), Parameter(name='title')})
Classes_Customers_ICustomers_m_changeCustomerFirstName: Method = Method(name="changeCustomerFirstName", parameters={Parameter(name='SSID'), Parameter(name='firstName')})
Classes_Customers_ICustomers_m_changeCustomerLastName: Method = Method(name="changeCustomerLastName", parameters={Parameter(name='lastName'), Parameter(name='SSID')})
Classes_Customers_ICustomers_m_changeCustomerTitle: Method = Method(name="changeCustomerTitle", parameters={Parameter(name='SSID'), Parameter(name='title')})
Classes_Customers_ICustomers_m_changeCustomerEmail: Method = Method(name="changeCustomerEmail", parameters={Parameter(name='SSID'), Parameter(name='eMail')})
Classes_Customers_ICustomers_m_changeCustomerPhone: Method = Method(name="changeCustomerPhone", parameters={Parameter(name='phoneNr'), Parameter(name='SSID')})
Classes_Customers_ICustomers_m_getCustomerFirstName: Method = Method(name="getCustomerFirstName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_getCustomerLastName: Method = Method(name="getCustomerLastName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_getCustomerPhone: Method = Method(name="getCustomerPhone", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_getCustomerTitle: Method = Method(name="getCustomerTitle", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_searchCustomers: Method = Method(name="searchCustomers", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Customers_ICustomers_m_getCustomerBookings: Method = Method(name="getCustomerBookings", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_getCustomerRequests: Method = Method(name="getCustomerRequests", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers_m_addCustomerBooking: Method = Method(name="addCustomerBooking", parameters={Parameter(name='bookingID'), Parameter(name='SSID')})
Classes_Customers_ICustomers_m_removeCustomerBooking: Method = Method(name="removeCustomerBooking", parameters={Parameter(name='SSID'), Parameter(name='bookingID')})
Classes_Customers_ICustomers_m_addCustomerRequest: Method = Method(name="addCustomerRequest", parameters={Parameter(name='description'), Parameter(name='SSID')})
Classes_Customers_ICustomers_m_removeCustomerRequest: Method = Method(name="removeCustomerRequest", parameters={Parameter(name='SSID'), Parameter(name='requestID')})
Classes_Customers_ICustomers_m_getCustomerEmail: Method = Method(name="getCustomerEmail", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Customers_ICustomers.methods={Classes_Customers_ICustomers_m_changeCustomerLastName, Classes_Customers_ICustomers_m_getCustomerFirstName, Classes_Customers_ICustomers_m_getCustomerPhone, Classes_Customers_ICustomers_m_getCustomerRequests, Classes_Customers_ICustomers_m_getCustomerTitle, Classes_Customers_ICustomers_m_addCustomerRequest, Classes_Customers_ICustomers_m_changeCustomerTitle, Classes_Customers_ICustomers_m_searchCustomers, Classes_Customers_ICustomers_m_getAllCustomers, Classes_Customers_ICustomers_m_changeCustomerFirstName, Classes_Customers_ICustomers_m_getCustomerLastName, Classes_Customers_ICustomers_m_removeCustomerRequest, Classes_Customers_ICustomers_m_addCustomerBooking, Classes_Customers_ICustomers_m_removeCustomerBooking, Classes_Customers_ICustomers_m_changeCustomerPhone, Classes_Customers_ICustomers_m_getCustomerBookings, Classes_Customers_ICustomers_m_addCustomer, Classes_Customers_ICustomers_m_getCustomerEmail, Classes_Customers_ICustomers_m_changeCustomerEmail}

# Classes_Statistics_Statistic class attributes and methods
Classes_Statistics_Statistic_type: Property = Property(name="type", type=StringType)
Classes_Statistics_Statistic.attributes={Classes_Statistics_Statistic_type}

# StatisticEntry class attributes and methods

# Date class attributes and methods

# Classes_Statistics_StatisticEntry class attributes and methods
Classes_Statistics_StatisticEntry_value: Property = Property(name="value", type=StringType)
Classes_Statistics_StatisticEntry.attributes={Classes_Statistics_StatisticEntry_value}

# Classes_Statistics_Date class attributes and methods

# Classes_Statistics_IStatisticsGenerator class attributes and methods
Classes_Statistics_IStatisticsGenerator_m_getOccupancyStatistics: Method = Method(name="getOccupancyStatistics", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Statistics_IStatisticsGenerator_m_getRevenueStatistics: Method = Method(name="getRevenueStatistics", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Statistics_IStatisticsGenerator_m_getProfitStatistics: Method = Method(name="getProfitStatistics", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Statistics_IStatisticsGenerator.methods={Classes_Statistics_IStatisticsGenerator_m_getRevenueStatistics, Classes_Statistics_IStatisticsGenerator_m_getProfitStatistics, Classes_Statistics_IStatisticsGenerator_m_getOccupancyStatistics}

# Classes_Staff_MonthlySalaryContract class attributes and methods
Classes_Staff_MonthlySalaryContract_salary: Property = Property(name="salary", type=FloatType)
Classes_Staff_MonthlySalaryContract.attributes={Classes_Staff_MonthlySalaryContract_salary}

# Classes_Statistics_StatisticsGenerator class attributes and methods
Classes_Statistics_StatisticsGenerator_staticExpenses: Property = Property(name="staticExpenses", type=FloatType)
Classes_Statistics_StatisticsGenerator.attributes={Classes_Statistics_StatisticsGenerator_staticExpenses}

# IStatisticsGenerator class attributes and methods

# IStaff class attributes and methods

# Classes_Staff_StaffManager class attributes and methods

# Staff class attributes and methods

# Classes_Staff_Staff class attributes and methods
Classes_Staff_Staff_firstName: Property = Property(name="firstName", type=StringType)
Classes_Staff_Staff_lastName: Property = Property(name="lastName", type=StringType)
Classes_Staff_Staff_job: Property = Property(name="job", type=StringType)
Classes_Staff_Staff_phone: Property = Property(name="phone", type=StringType)
Classes_Staff_Staff_email: Property = Property(name="email", type=StringType)
Classes_Staff_Staff_ssid: Property = Property(name="ssid", type=StringType)
Classes_Staff_Staff.attributes={Classes_Staff_Staff_email, Classes_Staff_Staff_ssid, Classes_Staff_Staff_job, Classes_Staff_Staff_firstName, Classes_Staff_Staff_lastName, Classes_Staff_Staff_phone}

# SalaryContract class attributes and methods

# Classes_Staff_SalaryContract class attributes and methods
Classes_Staff_SalaryContract_m_setSalary: Method = Method(name="setSalary", parameters={Parameter(name='salary')})
Classes_Staff_SalaryContract_m_getSalary: Method = Method(name="getSalary", parameters={}, type=FloatType)
Classes_Staff_SalaryContract_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
Classes_Staff_SalaryContract.methods={Classes_Staff_SalaryContract_m_getSalary, Classes_Staff_SalaryContract_m_getType, Classes_Staff_SalaryContract_m_setSalary}

# Classes_Staff_HourlySalaryContract class attributes and methods
Classes_Staff_HourlySalaryContract_salary: Property = Property(name="salary", type=FloatType)
Classes_Staff_HourlySalaryContract.attributes={Classes_Staff_HourlySalaryContract_salary}

# Classes_Staff_IStaff class attributes and methods
Classes_Staff_IStaff_m_getAllStaff: Method = Method(name="getAllStaff", parameters={}, type=StringType)
Classes_Staff_IStaff_m_searchStaff: Method = Method(name="searchStaff", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Staff_IStaff_m_getStaffFirstName: Method = Method(name="getStaffFirstName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffLastName: Method = Method(name="getStaffLastName", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffJob: Method = Method(name="getStaffJob", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffPhone: Method = Method(name="getStaffPhone", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffEmail: Method = Method(name="getStaffEmail", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffSalaryContractType: Method = Method(name="getStaffSalaryContractType", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_getStaffSalary: Method = Method(name="getStaffSalary", parameters={Parameter(name='SSID')}, type=StringType)
Classes_Staff_IStaff_m_changeStaffFirstName: Method = Method(name="changeStaffFirstName", parameters={Parameter(name='firstName'), Parameter(name='SSID')})
Classes_Staff_IStaff_m_changeStaffLastName: Method = Method(name="changeStaffLastName", parameters={Parameter(name='SSID'), Parameter(name='lastName')})
Classes_Staff_IStaff_m_changeStaffJob: Method = Method(name="changeStaffJob", parameters={Parameter(name='SSID'), Parameter(name='job')})
Classes_Staff_IStaff_m_changeStaffPhone: Method = Method(name="changeStaffPhone", parameters={Parameter(name='phoneNumber'), Parameter(name='SSID')})
Classes_Staff_IStaff_m_changeStaffSalaryContract: Method = Method(name="changeStaffSalaryContract", parameters={Parameter(name='salaryContract'), Parameter(name='SSID')})
Classes_Staff_IStaff_m_scheduleStaff: Method = Method(name="scheduleStaff", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
Classes_Staff_IStaff_m_addEmployee: Method = Method(name="addEmployee", parameters={Parameter(name='phone'), Parameter(name='email'), Parameter(name='salaryContractType'), Parameter(name='lastname'), Parameter(name='salary'), Parameter(name='SSID'), Parameter(name='firstname'), Parameter(name='job')})
Classes_Staff_IStaff.methods={Classes_Staff_IStaff_m_changeStaffLastName, Classes_Staff_IStaff_m_changeStaffFirstName, Classes_Staff_IStaff_m_getAllStaff, Classes_Staff_IStaff_m_getStaffFirstName, Classes_Staff_IStaff_m_scheduleStaff, Classes_Staff_IStaff_m_searchStaff, Classes_Staff_IStaff_m_getStaffLastName, Classes_Staff_IStaff_m_getStaffSalary, Classes_Staff_IStaff_m_changeStaffJob, Classes_Staff_IStaff_m_changeStaffSalaryContract, Classes_Staff_IStaff_m_getStaffSalaryContractType, Classes_Staff_IStaff_m_addEmployee, Classes_Staff_IStaff_m_getStaffPhone, Classes_Staff_IStaff_m_getStaffEmail, Classes_Staff_IStaff_m_changeStaffPhone, Classes_Staff_IStaff_m_getStaffJob}

# Classes_Restaurants_IRestaurantsManage class attributes and methods
Classes_Restaurants_IRestaurantsManage_m_changeRestaurantName: Method = Method(name="changeRestaurantName", parameters={Parameter(name='name'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsManage_m_addRestaurant: Method = Method(name="addRestaurant", parameters={Parameter(name='name')})
Classes_Restaurants_IRestaurantsManage_m_removeRestaurant: Method = Method(name="removeRestaurant", parameters={Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsManage_m_addRestaurantTable: Method = Method(name="addRestaurantTable", parameters={Parameter(name='tableNbr'), Parameter(name='nbrSeats'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsManage_m_removeRestaurantTable: Method = Method(name="removeRestaurantTable", parameters={Parameter(name='tableNbr'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsManage_m_changeTableNumberOfSeats: Method = Method(name="changeTableNumberOfSeats", parameters={Parameter(name='nbrSeats'), Parameter(name='restaurantID'), Parameter(name='tableNbr')})
Classes_Restaurants_IRestaurantsManage_m_addMenuItem: Method = Method(name="addMenuItem", parameters={Parameter(name='itemID'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsManage_m_removeMenuItem: Method = Method(name="removeMenuItem", parameters={Parameter(name='restaurantID'), Parameter(name='itemID')})
Classes_Restaurants_IRestaurantsManage_m_changeMenuName: Method = Method(name="changeMenuName", parameters={Parameter(name='restaurantID'), Parameter(name='name')})
Classes_Restaurants_IRestaurantsManage_m_changeTableNumber: Method = Method(name="changeTableNumber", parameters={Parameter(name='newTableNbr'), Parameter(name='restaurantID'), Parameter(name='oldTableNbr')})
Classes_Restaurants_IRestaurantsManage.methods={Classes_Restaurants_IRestaurantsManage_m_removeRestaurant, Classes_Restaurants_IRestaurantsManage_m_addMenuItem, Classes_Restaurants_IRestaurantsManage_m_addRestaurant, Classes_Restaurants_IRestaurantsManage_m_changeTableNumber, Classes_Restaurants_IRestaurantsManage_m_removeMenuItem, Classes_Restaurants_IRestaurantsManage_m_changeTableNumberOfSeats, Classes_Restaurants_IRestaurantsManage_m_removeRestaurantTable, Classes_Restaurants_IRestaurantsManage_m_changeMenuName, Classes_Restaurants_IRestaurantsManage_m_addRestaurantTable, Classes_Restaurants_IRestaurantsManage_m_changeRestaurantName}

# IRestaurantsAccess class attributes and methods

# Classes_Restaurants_IRestaurantsAccess class attributes and methods
Classes_Restaurants_IRestaurantsAccess_m_getRestaurantReservations: Method = Method(name="getRestaurantReservations", parameters={Parameter(name='restaurantID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getRestaurantTables: Method = Method(name="getRestaurantTables", parameters={Parameter(name='restaurantID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getRestaurantTableNumberOfSeats: Method = Method(name="getRestaurantTableNumberOfSeats", parameters={Parameter(name='restaurantID'), Parameter(name='tableNbr')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getAvailableTables: Method = Method(name="getAvailableTables", parameters={Parameter(name='to'), Parameter(name='restaurantID'), Parameter(name='from')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getReservationGuest: Method = Method(name="getReservationGuest", parameters={Parameter(name='restaurantID'), Parameter(name='reservationID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getRestaurantMenuName: Method = Method(name="getRestaurantMenuName", parameters={Parameter(name='restaurantID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getAllRestaurantNames: Method = Method(name="getAllRestaurantNames", parameters={}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_searchRestaurants: Method = Method(name="searchRestaurants", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantReservations: Method = Method(name="searchRestaurantReservations", parameters={Parameter(name='keyword'), Parameter(name='restaurantID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantTables: Method = Method(name="searchRestaurantTables", parameters={Parameter(name='restaurantID'), Parameter(name='keyword')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_makeReservation: Method = Method(name="makeReservation", parameters={Parameter(name='from'), Parameter(name='guestID'), Parameter(name='restaurantID'), Parameter(name='to'), Parameter(name='tables')})
Classes_Restaurants_IRestaurantsAccess_m_cancelReservation: Method = Method(name="cancelReservation", parameters={Parameter(name='reservationID'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsAccess_m_changeReservedTables: Method = Method(name="changeReservedTables", parameters={Parameter(name='tables'), Parameter(name='reservationID'), Parameter(name='restaurantID')})
Classes_Restaurants_IRestaurantsAccess_m_getAvailableTablesByNbrGuests: Method = Method(name="getAvailableTablesByNbrGuests", parameters={Parameter(name='from'), Parameter(name='nbrGuests'), Parameter(name='restaurantID'), Parameter(name='to')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getRestaurantMenuItems: Method = Method(name="getRestaurantMenuItems", parameters={Parameter(name='restaurantID')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess_m_getReservationFromTime: Method = Method(name="getReservationFromTime", parameters={Parameter(name='restaurantID'), Parameter(name='reservationID')}, type=DateType)
Classes_Restaurants_IRestaurantsAccess_m_getReservationToTime: Method = Method(name="getReservationToTime", parameters={Parameter(name='restaurantID'), Parameter(name='reservationID')}, type=DateType)
Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantReservationsWithTime: Method = Method(name="searchRestaurantReservationsWithTime", parameters={Parameter(name='keyword'), Parameter(name='restaurantID'), Parameter(name='from'), Parameter(name='to')}, type=StringType)
Classes_Restaurants_IRestaurantsAccess.methods={Classes_Restaurants_IRestaurantsAccess_m_getRestaurantTables, Classes_Restaurants_IRestaurantsAccess_m_changeReservedTables, Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantTables, Classes_Restaurants_IRestaurantsAccess_m_getAvailableTables, Classes_Restaurants_IRestaurantsAccess_m_getRestaurantMenuItems, Classes_Restaurants_IRestaurantsAccess_m_getReservationGuest, Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantReservationsWithTime, Classes_Restaurants_IRestaurantsAccess_m_getReservationToTime, Classes_Restaurants_IRestaurantsAccess_m_getRestaurantReservations, Classes_Restaurants_IRestaurantsAccess_m_getAvailableTablesByNbrGuests, Classes_Restaurants_IRestaurantsAccess_m_cancelReservation, Classes_Restaurants_IRestaurantsAccess_m_makeReservation, Classes_Restaurants_IRestaurantsAccess_m_getAllRestaurantNames, Classes_Restaurants_IRestaurantsAccess_m_getRestaurantMenuName, Classes_Restaurants_IRestaurantsAccess_m_getRestaurantTableNumberOfSeats, Classes_Restaurants_IRestaurantsAccess_m_getReservationFromTime, Classes_Restaurants_IRestaurantsAccess_m_searchRestaurants, Classes_Restaurants_IRestaurantsAccess_m_searchRestaurantReservations}

# Classes_Restaurants_RestaurantsManager class attributes and methods

# IRestaurantsManage class attributes and methods

# Restaurant class attributes and methods

# Classes_Restaurants_Restaurant class attributes and methods
Classes_Restaurants_Restaurant_name: Property = Property(name="name", type=StringType)
Classes_Restaurants_Restaurant_m_addReservation: Method = Method(name="addReservation", parameters={})
Classes_Restaurants_Restaurant_m_getReservation: Method = Method(name="getReservation", parameters={Parameter(name='reservationID')})
Classes_Restaurants_Restaurant.attributes={Classes_Restaurants_Restaurant_name}
Classes_Restaurants_Restaurant.methods={Classes_Restaurants_Restaurant_m_addReservation, Classes_Restaurants_Restaurant_m_getReservation}

# Reservation class attributes and methods

# RestaurantTable class attributes and methods

# RestaurantMenu class attributes and methods

# Classes_Restaurants_Reservation class attributes and methods
Classes_Restaurants_Reservation_id: Property = Property(name="id", type=StringType)
Classes_Restaurants_Reservation_reservedBy: Property = Property(name="reservedBy", type=StringType)
Classes_Restaurants_Reservation_from: Property = Property(name="from", type=DateType)
Classes_Restaurants_Reservation_to: Property = Property(name="to", type=DateType)
Classes_Restaurants_Reservation.attributes={Classes_Restaurants_Reservation_id, Classes_Restaurants_Reservation_to, Classes_Restaurants_Reservation_from, Classes_Restaurants_Reservation_reservedBy}

# Classes_Restaurants_RestaurantMenu class attributes and methods
Classes_Restaurants_RestaurantMenu_name: Property = Property(name="name", type=StringType)
Classes_Restaurants_RestaurantMenu_items: Property = Property(name="items", type=StringType)
Classes_Restaurants_RestaurantMenu_m_addItem: Method = Method(name="addItem", parameters={Parameter(name='itemID')})
Classes_Restaurants_RestaurantMenu_m_removeItem: Method = Method(name="removeItem", parameters={Parameter(name='itemID')})
Classes_Restaurants_RestaurantMenu.attributes={Classes_Restaurants_RestaurantMenu_items, Classes_Restaurants_RestaurantMenu_name}
Classes_Restaurants_RestaurantMenu.methods={Classes_Restaurants_RestaurantMenu_m_addItem, Classes_Restaurants_RestaurantMenu_m_removeItem}

# Classes_Feedback_IFeedback class attributes and methods
Classes_Feedback_IFeedback_m_getAllFeedbackIDs: Method = Method(name="getAllFeedbackIDs", parameters={}, type=StringType)
Classes_Feedback_IFeedback_m_getFeedbackDescription: Method = Method(name="getFeedbackDescription", parameters={Parameter(name='id')}, type=StringType)
Classes_Feedback_IFeedback_m_getFeedbackIsResolved: Method = Method(name="getFeedbackIsResolved", parameters={Parameter(name='id')}, type=StringType)
Classes_Feedback_IFeedback_m_getFeedbackIsNoted: Method = Method(name="getFeedbackIsNoted", parameters={Parameter(name='id')}, type=StringType)
Classes_Feedback_IFeedback_m_setFeedbackDescription: Method = Method(name="setFeedbackDescription", parameters={Parameter(name='desc'), Parameter(name='id')})
Classes_Feedback_IFeedback_m_setFeedbackIsResolved: Method = Method(name="setFeedbackIsResolved", parameters={Parameter(name='id'), Parameter(name='status')})
Classes_Feedback_IFeedback_m_setFeedbackIsNoted: Method = Method(name="setFeedbackIsNoted", parameters={Parameter(name='id'), Parameter(name='status')})
Classes_Feedback_IFeedback_m_searchFeedback: Method = Method(name="searchFeedback", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Feedback_IFeedback_m_addFeedback: Method = Method(name="addFeedback", parameters={Parameter(name='desc')})
Classes_Feedback_IFeedback.methods={Classes_Feedback_IFeedback_m_setFeedbackDescription, Classes_Feedback_IFeedback_m_setFeedbackIsNoted, Classes_Feedback_IFeedback_m_getFeedbackIsResolved, Classes_Feedback_IFeedback_m_getFeedbackDescription, Classes_Feedback_IFeedback_m_setFeedbackIsResolved, Classes_Feedback_IFeedback_m_getFeedbackIsNoted, Classes_Feedback_IFeedback_m_searchFeedback, Classes_Feedback_IFeedback_m_getAllFeedbackIDs, Classes_Feedback_IFeedback_m_addFeedback}

# Classes_Restaurants_RestaurantTable class attributes and methods
Classes_Restaurants_RestaurantTable_tableNumber: Property = Property(name="tableNumber", type=StringType)
Classes_Restaurants_RestaurantTable_numberOfSeats: Property = Property(name="numberOfSeats", type=StringType)
Classes_Restaurants_RestaurantTable.attributes={Classes_Restaurants_RestaurantTable_numberOfSeats, Classes_Restaurants_RestaurantTable_tableNumber}

# Classes_Feedback_FeedbackManager class attributes and methods

# IFeedback class attributes and methods

# Feedback class attributes and methods

# Classes_Feedback_Feedback class attributes and methods
Classes_Feedback_Feedback_description: Property = Property(name="description", type=StringType)
Classes_Feedback_Feedback_isNoted: Property = Property(name="isNoted", type=StringType)
Classes_Feedback_Feedback_isResolved: Property = Property(name="isResolved", type=StringType)
Classes_Feedback_Feedback_id: Property = Property(name="id", type=StringType)
Classes_Feedback_Feedback.attributes={Classes_Feedback_Feedback_description, Classes_Feedback_Feedback_isResolved, Classes_Feedback_Feedback_id, Classes_Feedback_Feedback_isNoted}

# Classes_Requests_IRequests class attributes and methods
Classes_Requests_IRequests_m_getRequestDescription: Method = Method(name="getRequestDescription", parameters={Parameter(name='specialRequestId')}, type=StringType)
Classes_Requests_IRequests_m_hasRequestBeenResolved: Method = Method(name="hasRequestBeenResolved", parameters={Parameter(name='specialRequestId')}, type=StringType)
Classes_Requests_IRequests_m_setRequestResolved: Method = Method(name="setRequestResolved", parameters={Parameter(name='SpecialRequestId')})
Classes_Requests_IRequests_m_changeRequestDesc: Method = Method(name="changeRequestDesc", parameters={Parameter(name='specialRequestId'), Parameter(name='description')})
Classes_Requests_IRequests_m_searchRequests: Method = Method(name="searchRequests", parameters={Parameter(name='keyword')}, type=StringType)
Classes_Requests_IRequests_m_getAllRequestIDs: Method = Method(name="getAllRequestIDs", parameters={}, type=StringType)
Classes_Requests_IRequests_m_setRequestDescription: Method = Method(name="setRequestDescription", parameters={Parameter(name='description'), Parameter(name='specialRequestId')})
Classes_Requests_IRequests_m_addRequest: Method = Method(name="addRequest", parameters={Parameter(name='description'), Parameter(name='specialRequestId')})
Classes_Requests_IRequests_m_createRequest: Method = Method(name="createRequest", parameters={Parameter(name='description')})
Classes_Requests_IRequests_m_deleteRequest: Method = Method(name="deleteRequest", parameters={Parameter(name='specialRequestId')})
Classes_Requests_IRequests.methods={Classes_Requests_IRequests_m_createRequest, Classes_Requests_IRequests_m_addRequest, Classes_Requests_IRequests_m_setRequestDescription, Classes_Requests_IRequests_m_changeRequestDesc, Classes_Requests_IRequests_m_hasRequestBeenResolved, Classes_Requests_IRequests_m_getAllRequestIDs, Classes_Requests_IRequests_m_getRequestDescription, Classes_Requests_IRequests_m_searchRequests, Classes_Requests_IRequests_m_deleteRequest, Classes_Requests_IRequests_m_setRequestResolved}

# Classes_Requests_RequestsManager class attributes and methods

# IRequests class attributes and methods

# Request class attributes and methods

# Classes_Requests_Request class attributes and methods
Classes_Requests_Request_id: Property = Property(name="id", type=StringType)
Classes_Requests_Request_description: Property = Property(name="description", type=StringType)
Classes_Requests_Request_isResolved: Property = Property(name="isResolved", type=StringType)
Classes_Requests_Request.attributes={Classes_Requests_Request_isResolved, Classes_Requests_Request_description, Classes_Requests_Request_id}

# Relationships
location0: BinaryAssociation = BinaryAssociation(
    name="location0",
    ends={
        Property(name="RoomLocation", type=Classes_Bookables_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookables_Room", type=RoomLocation, multiplicity=Multiplicity(1, 1))
    }
)
room1: BinaryAssociation = BinaryAssociation(
    name="room1",
    ends={
        Property(name="HotelRoom", type=Classes_Bookables_HostelBed, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookables_HostelBed", type=HotelRoom, multiplicity=Multiplicity(1, 1))
    }
)
bookables2: BinaryAssociation = BinaryAssociation(
    name="bookables2",
    ends={
        Property(name="Bookable", type=Classes_Bookables_BookablesManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookables_BookablesManager", type=Bookable, multiplicity=Multiplicity(0, 9999))
    }
)
creditCard5: BinaryAssociation = BinaryAssociation(
    name="creditCard5",
    ends={
        Property(name="CreditCard", type=Classes_Stays_Stay, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Stays_Stay", type=CreditCard, multiplicity=Multiplicity(1, 1))
    }
)
iHotelStayManager3: BinaryAssociation = BinaryAssociation(
    name="iHotelStayManager3",
    ends={
        Property(name="IStays", type=Classes_Bookables_BookablesManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookables_BookablesManager4", type=IStays, multiplicity=Multiplicity(1, 1))
    }
)
iGuests11: BinaryAssociation = BinaryAssociation(
    name="iGuests11",
    ends={
        Property(name="IGuests", type=Classes_Stays_StaysManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Stays_StaysManager12", type=IGuests, multiplicity=Multiplicity(1, 1))
    }
)
stays6: BinaryAssociation = BinaryAssociation(
    name="stays6",
    ends={
        Property(name="Stay", type=Classes_Stays_StaysManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Stays_StaysManager", type=Stay, multiplicity=Multiplicity(0, 9999))
    }
)
customerProvides7: BinaryAssociation = BinaryAssociation(
    name="customerProvides7",
    ends={
        Property(name="CustomerProvides", type=Classes_Stays_StaysManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Stays_StaysManager8", type=CustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
iBills9: BinaryAssociation = BinaryAssociation(
    name="iBills9",
    ends={
        Property(name="IBills", type=Classes_Stays_StaysManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Stays_StaysManager10", type=IBills, multiplicity=Multiplicity(1, 1))
    }
)
bills13: BinaryAssociation = BinaryAssociation(
    name="bills13",
    ends={
        Property(name="Bill", type=Classes_Bills_BillsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bills_BillsManager", type=Bill, multiplicity=Multiplicity(0, 9999))
    }
)
customerProvides14: BinaryAssociation = BinaryAssociation(
    name="customerProvides14",
    ends={
        Property(name="CustomerProvides16", type=Classes_Bills_BillsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bills_BillsManager15", type=CustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
bookablesAccess17: BinaryAssociation = BinaryAssociation(
    name="bookablesAccess17",
    ends={
        Property(name="IBookablesAccess", type=Classes_Bills_BillsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bills_BillsManager18", type=IBookablesAccess, multiplicity=Multiplicity(1, 1))
    }
)
inventoryAccess19: BinaryAssociation = BinaryAssociation(
    name="inventoryAccess19",
    ends={
        Property(name="IInventoryAccess", type=Classes_Bills_BillsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bills_BillsManager20", type=IInventoryAccess, multiplicity=Multiplicity(1, 1))
    }
)
servicesAccess21: BinaryAssociation = BinaryAssociation(
    name="servicesAccess21",
    ends={
        Property(name="IServicesAccess", type=Classes_Bills_BillsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bills_BillsManager22", type=IServicesAccess, multiplicity=Multiplicity(1, 1))
    }
)
items23: BinaryAssociation = BinaryAssociation(
    name="items23",
    ends={
        Property(name="Item", type=Classes_Inventory_InventoryManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Inventory_InventoryManager", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
service24: BinaryAssociation = BinaryAssociation(
    name="service24",
    ends={
        Property(name="Service", type=Classes_Services_ServiceManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Services_ServiceManager", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
roomServiceOrder25: BinaryAssociation = BinaryAssociation(
    name="roomServiceOrder25",
    ends={
        Property(name="RoomServiceOrder", type=Classes_Services_ServiceManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Services_ServiceManager26", type=RoomServiceOrder, multiplicity=Multiplicity(0, 9999))
    }
)
roomServiceMenu27: BinaryAssociation = BinaryAssociation(
    name="roomServiceMenu27",
    ends={
        Property(name="RoomServiceMenu", type=Classes_Services_ServiceManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Services_ServiceManager28", type=RoomServiceMenu, multiplicity=Multiplicity(1, 1))
    }
)
service29: BinaryAssociation = BinaryAssociation(
    name="service29",
    ends={
        Property(name="Service30", type=Classes_Services_RoomServiceOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Services_RoomServiceOrder", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
guests31: BinaryAssociation = BinaryAssociation(
    name="guests31",
    ends={
        Property(name="Guest", type=Classes_Guests_GuestsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Guests_GuestsManager", type=Guest, multiplicity=Multiplicity(0, 9999))
    }
)
iManageAccounts32: BinaryAssociation = BinaryAssociation(
    name="iManageAccounts32",
    ends={
        Property(name="IManageAccounts", type=Classes_Guests_GuestsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Guests_GuestsManager33", type=IManageAccounts, multiplicity=Multiplicity(1, 1))
    }
)
accounts34: BinaryAssociation = BinaryAssociation(
    name="accounts34",
    ends={
        Property(name="Account", type=Classes_Accounts_AccountsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Accounts_AccountsManager", type=Account, multiplicity=Multiplicity(0, 9999))
    }
)
creditCard35: BinaryAssociation = BinaryAssociation(
    name="creditCard35",
    ends={
        Property(name="CreditCard36", type=Classes_Bookings_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_Booking", type=CreditCard, multiplicity=Multiplicity(1, 1))
    }
)
booking37: BinaryAssociation = BinaryAssociation(
    name="booking37",
    ends={
        Property(name="Booking", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager", type=Booking, multiplicity=Multiplicity(0, 9999))
    }
)
iBookableAccess38: BinaryAssociation = BinaryAssociation(
    name="iBookableAccess38",
    ends={
        Property(name="IBookablesAccess40", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager39", type=IBookablesAccess, multiplicity=Multiplicity(1, 1))
    }
)
iHotelStayManager41: BinaryAssociation = BinaryAssociation(
    name="iHotelStayManager41",
    ends={
        Property(name="IStays43", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager42", type=IStays, multiplicity=Multiplicity(1, 1))
    }
)
bank44: BinaryAssociation = BinaryAssociation(
    name="bank44",
    ends={
        Property(name="CustomerProvides46", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager45", type=CustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
iGuest47: BinaryAssociation = BinaryAssociation(
    name="iGuest47",
    ends={
        Property(name="IGuests49", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager48", type=IGuests, multiplicity=Multiplicity(1, 1))
    }
)
iCustomer50: BinaryAssociation = BinaryAssociation(
    name="iCustomer50",
    ends={
        Property(name="ICustomers", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager51", type=ICustomers, multiplicity=Multiplicity(1, 1))
    }
)
iBills52: BinaryAssociation = BinaryAssociation(
    name="iBills52",
    ends={
        Property(name="IBills54", type=Classes_Bookings_BookingsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Bookings_BookingsManager53", type=IBills, multiplicity=Multiplicity(1, 1))
    }
)
customer55: BinaryAssociation = BinaryAssociation(
    name="customer55",
    ends={
        Property(name="Customer", type=Classes_Customers_CustomersManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Customers_CustomersManager", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
statisticEntry56: BinaryAssociation = BinaryAssociation(
    name="statisticEntry56",
    ends={
        Property(name="StatisticEntry", type=Classes_Statistics_Statistic, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_Statistic", type=StatisticEntry, multiplicity=Multiplicity(0, 9999))
    }
)
fromDate57: BinaryAssociation = BinaryAssociation(
    name="fromDate57",
    ends={
        Property(name="Date", type=Classes_Statistics_Statistic, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_Statistic58", type=Date, multiplicity=Multiplicity(1, 1))
    }
)
toDate59: BinaryAssociation = BinaryAssociation(
    name="toDate59",
    ends={
        Property(name="Date61", type=Classes_Statistics_Statistic, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_Statistic60", type=Date, multiplicity=Multiplicity(1, 1))
    }
)
dateOfEntry62: BinaryAssociation = BinaryAssociation(
    name="dateOfEntry62",
    ends={
        Property(name="Date63", type=Classes_Statistics_StatisticEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_StatisticEntry", type=Date, multiplicity=Multiplicity(1, 1))
    }
)
iBillsAccess64: BinaryAssociation = BinaryAssociation(
    name="iBillsAccess64",
    ends={
        Property(name="IBills65", type=Classes_Statistics_StatisticsGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_StatisticsGenerator", type=IBills, multiplicity=Multiplicity(1, 1))
    }
)
iBooking66: BinaryAssociation = BinaryAssociation(
    name="iBooking66",
    ends={
        Property(name="IBookings", type=Classes_Statistics_StatisticsGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_StatisticsGenerator67", type=IBookings, multiplicity=Multiplicity(1, 1))
    }
)
iStaff68: BinaryAssociation = BinaryAssociation(
    name="iStaff68",
    ends={
        Property(name="IStaff", type=Classes_Statistics_StatisticsGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Statistics_StatisticsGenerator69", type=IStaff, multiplicity=Multiplicity(1, 1))
    }
)
employees70: BinaryAssociation = BinaryAssociation(
    name="employees70",
    ends={
        Property(name="Staff", type=Classes_Staff_StaffManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Staff_StaffManager", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
iStatisticsGenerator71: BinaryAssociation = BinaryAssociation(
    name="iStatisticsGenerator71",
    ends={
        Property(name="IStatisticsGenerator", type=Classes_Staff_StaffManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Staff_StaffManager72", type=IStatisticsGenerator, multiplicity=Multiplicity(1, 1))
    }
)
salaryContract73: BinaryAssociation = BinaryAssociation(
    name="salaryContract73",
    ends={
        Property(name="SalaryContract", type=Classes_Staff_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Staff_Staff", type=SalaryContract, multiplicity=Multiplicity(1, 1))
    }
)
restaurant74: BinaryAssociation = BinaryAssociation(
    name="restaurant74",
    ends={
        Property(name="Restaurant", type=Classes_Restaurants_RestaurantsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Restaurants_RestaurantsManager", type=Restaurant, multiplicity=Multiplicity(0, 9999))
    }
)
reservation75: BinaryAssociation = BinaryAssociation(
    name="reservation75",
    ends={
        Property(name="Reservation", type=Classes_Restaurants_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Restaurants_Restaurant", type=Reservation, multiplicity=Multiplicity(0, 9999))
    }
)
restaurantTable76: BinaryAssociation = BinaryAssociation(
    name="restaurantTable76",
    ends={
        Property(name="RestaurantTable", type=Classes_Restaurants_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Restaurants_Restaurant77", type=RestaurantTable, multiplicity=Multiplicity(0, 9999))
    }
)
menu78: BinaryAssociation = BinaryAssociation(
    name="menu78",
    ends={
        Property(name="RestaurantMenu", type=Classes_Restaurants_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Restaurants_Restaurant79", type=RestaurantMenu, multiplicity=Multiplicity(1, 1))
    }
)
restaurantTable80: BinaryAssociation = BinaryAssociation(
    name="restaurantTable80",
    ends={
        Property(name="RestaurantTable81", type=Classes_Restaurants_Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Restaurants_Reservation", type=RestaurantTable, multiplicity=Multiplicity(1, 9999))
    }
)
feedbacks82: BinaryAssociation = BinaryAssociation(
    name="feedbacks82",
    ends={
        Property(name="Feedback", type=Classes_Feedback_FeedbackManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Feedback_FeedbackManager", type=Feedback, multiplicity=Multiplicity(0, 9999))
    }
)
specialRequest83: BinaryAssociation = BinaryAssociation(
    name="specialRequest83",
    ends={
        Property(name="Request", type=Classes_Requests_RequestsManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Requests_RequestsManager", type=Request, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Classes_Bookables_Room_Bookable = Generalization(general=Bookable, specific=Classes_Bookables_Room)
gen_Classes_Bookables_ConferenceRoom_Room = Generalization(general=Room, specific=Classes_Bookables_ConferenceRoom)
gen_Classes_Bookables_HostelBed_Bookable = Generalization(general=Bookable, specific=Classes_Bookables_HostelBed)
gen_Classes_Bookables_HotelRoom_Room = Generalization(general=Room, specific=Classes_Bookables_HotelRoom)
gen_Classes_Bookables_IBookablesManage_IBookablesAccess = Generalization(general=IBookablesAccess, specific=Classes_Bookables_IBookablesManage)
gen_Classes_Bookables_BookablesManager_IBookablesManage = Generalization(general=IBookablesManage, specific=Classes_Bookables_BookablesManager)
gen_Classes_Stays_StaysManager_IStays = Generalization(general=IStays, specific=Classes_Stays_StaysManager)
gen_Classes_Bills_BillsManager_IBills = Generalization(general=IBills, specific=Classes_Bills_BillsManager)
gen_Classes_Inventory_IManageInventory_IInventoryAccess = Generalization(general=IInventoryAccess, specific=Classes_Inventory_IManageInventory)
gen_Classes_Inventory_InventoryManager_IManageInventory = Generalization(general=IManageInventory, specific=Classes_Inventory_InventoryManager)
gen_Classes_Services_ServiceManager_IServicesManage = Generalization(general=IServicesManage, specific=Classes_Services_ServiceManager)
gen_Classes_Services_IServicesManage_IServicesAccess = Generalization(general=IServicesAccess, specific=Classes_Services_IServicesManage)
gen_Classes_Guests_GuestsManager_IGuests = Generalization(general=IGuests, specific=Classes_Guests_GuestsManager)
gen_Classes_Accounts_AccountsManager_Accounts_IManageAccounts = Generalization(general=Accounts_IManageAccounts, specific=Classes_Accounts_AccountsManager)
gen_Classes_Accounts_AccountsManager_Accounts_IAccountsAccess = Generalization(general=Accounts_IAccountsAccess, specific=Classes_Accounts_AccountsManager)
gen_Classes_Bookings_BookingsManager_IBookings = Generalization(general=IBookings, specific=Classes_Bookings_BookingsManager)
gen_Classes_Customers_CustomersManager_ICustomers = Generalization(general=ICustomers, specific=Classes_Customers_CustomersManager)
gen_Classes_Statistics_StatisticsGenerator_IStatisticsGenerator = Generalization(general=IStatisticsGenerator, specific=Classes_Statistics_StatisticsGenerator)
gen_Classes_Staff_StaffManager_IStaff = Generalization(general=IStaff, specific=Classes_Staff_StaffManager)
gen_Classes_Staff_MonthlySalaryContract_SalaryContract = Generalization(general=SalaryContract, specific=Classes_Staff_MonthlySalaryContract)
gen_Classes_Staff_HourlySalaryContract_SalaryContract = Generalization(general=SalaryContract, specific=Classes_Staff_HourlySalaryContract)
gen_Classes_Restaurants_IRestaurantsManage_IRestaurantsAccess = Generalization(general=IRestaurantsAccess, specific=Classes_Restaurants_IRestaurantsManage)
gen_Classes_Restaurants_RestaurantsManager_IRestaurantsManage = Generalization(general=IRestaurantsManage, specific=Classes_Restaurants_RestaurantsManager)
gen_Classes_Feedback_FeedbackManager_IFeedback = Generalization(general=IFeedback, specific=Classes_Feedback_FeedbackManager)
gen_Classes_Requests_RequestsManager_IRequests = Generalization(general=IRequests, specific=Classes_Requests_RequestsManager)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Classes_Bookables_Bookable, Classes_Bookables_Room, Bookable, RoomLocation, Classes_Bookables_RoomLocation, Classes_Bookables_ConferenceRoom, Classes_Bookables_HostelBed, HotelRoom, Classes_Bookables_HotelRoom, Room, Classes_Bookables_IBookablesManage, IBookablesAccess, Classes_Bookables_IBookablesAccess, Classes_Bookables_BookablesManager, IBookablesManage, CreditCard, Classes_Stays_CreditCard, IStays, Classes_Stays_Stay, IGuests, Classes_Stays_IStays, Classes_Stays_StaysManager, Stay, CustomerProvides, IBills, Classes_Banking_AdministratorProvides, Classes_Banking_CustomerProvides, Classes_Bills_BillsManager, Bill, IInventoryAccess, IServicesAccess, Classes_Bills_Bill, Classes_Bills_IBills, Classes_Inventory_IManageInventory, Classes_Inventory_InventoryManager, IManageInventory, Item, Classes_Inventory_Item, Classes_Inventory_IInventoryAccess, Classes_Services_RoomServiceMenu, Classes_Services_ServiceManager, IServicesManage, Service, RoomServiceOrder, RoomServiceMenu, Classes_Services_Service, Classes_Services_RoomServiceOrder, Classes_Services_IServicesManage, Classes_Services_IServicesAccess, Classes_Guests_GuestsManager, Guest, IManageAccounts, Classes_Guests_Guest, Classes_Guests_IGuests, Classes_Accounts_Account, Classes_Accounts_AccountsManager, Accounts_IManageAccounts, Accounts_IAccountsAccess, Account, Classes_Accounts_IAccountsAccess, Classes_Accounts_IManageAccounts, Classes_Bookings_Booking, Classes_Bookings_BookingsManager, IBookings, Booking, ICustomers, Classes_Bookings_IBookings, Classes_Customers_CustomersManager, Customer, Classes_Customers_Customer, Classes_Customers_ICustomers, Classes_Statistics_Statistic, StatisticEntry, Date, Classes_Statistics_StatisticEntry, Classes_Statistics_Date, Classes_Statistics_IStatisticsGenerator, Classes_Staff_MonthlySalaryContract, Classes_Statistics_StatisticsGenerator, IStatisticsGenerator, IStaff, Classes_Staff_StaffManager, Staff, Classes_Staff_Staff, SalaryContract, Classes_Staff_SalaryContract, Classes_Staff_HourlySalaryContract, Classes_Staff_IStaff, Classes_Restaurants_IRestaurantsManage, IRestaurantsAccess, Classes_Restaurants_IRestaurantsAccess, Classes_Restaurants_RestaurantsManager, IRestaurantsManage, Restaurant, Classes_Restaurants_Restaurant, Reservation, RestaurantTable, RestaurantMenu, Classes_Restaurants_Reservation, Classes_Restaurants_RestaurantMenu, Classes_Feedback_IFeedback, Classes_Restaurants_RestaurantTable, Classes_Feedback_FeedbackManager, IFeedback, Feedback, Classes_Feedback_Feedback, Classes_Requests_IRequests, Classes_Requests_RequestsManager, IRequests, Request, Classes_Requests_Request, HotelRoomCategory, ConferenceRoomCategory, AccountType},
    associations={location0, room1, bookables2, creditCard5, iHotelStayManager3, iGuests11, stays6, customerProvides7, iBills9, bills13, customerProvides14, bookablesAccess17, inventoryAccess19, servicesAccess21, items23, service24, roomServiceOrder25, roomServiceMenu27, service29, guests31, iManageAccounts32, accounts34, creditCard35, booking37, iBookableAccess38, iHotelStayManager41, bank44, iGuest47, iCustomer50, iBills52, customer55, statisticEntry56, fromDate57, toDate59, dateOfEntry62, iBillsAccess64, iBooking66, iStaff68, employees70, iStatisticsGenerator71, salaryContract73, restaurant74, reservation75, restaurantTable76, menu78, restaurantTable80, feedbacks82, specialRequest83},
    generalizations={gen_Classes_Bookables_Room_Bookable, gen_Classes_Bookables_ConferenceRoom_Room, gen_Classes_Bookables_HostelBed_Bookable, gen_Classes_Bookables_HotelRoom_Room, gen_Classes_Bookables_IBookablesManage_IBookablesAccess, gen_Classes_Bookables_BookablesManager_IBookablesManage, gen_Classes_Stays_StaysManager_IStays, gen_Classes_Bills_BillsManager_IBills, gen_Classes_Inventory_IManageInventory_IInventoryAccess, gen_Classes_Inventory_InventoryManager_IManageInventory, gen_Classes_Services_ServiceManager_IServicesManage, gen_Classes_Services_IServicesManage_IServicesAccess, gen_Classes_Guests_GuestsManager_IGuests, gen_Classes_Accounts_AccountsManager_Accounts_IManageAccounts, gen_Classes_Accounts_AccountsManager_Accounts_IAccountsAccess, gen_Classes_Bookings_BookingsManager_IBookings, gen_Classes_Customers_CustomersManager_ICustomers, gen_Classes_Statistics_StatisticsGenerator_IStatisticsGenerator, gen_Classes_Staff_StaffManager_IStaff, gen_Classes_Staff_MonthlySalaryContract_SalaryContract, gen_Classes_Staff_HourlySalaryContract_SalaryContract, gen_Classes_Restaurants_IRestaurantsManage_IRestaurantsAccess, gen_Classes_Restaurants_RestaurantsManager_IRestaurantsManage, gen_Classes_Feedback_FeedbackManager_IFeedback, gen_Classes_Requests_RequestsManager_IRequests},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)