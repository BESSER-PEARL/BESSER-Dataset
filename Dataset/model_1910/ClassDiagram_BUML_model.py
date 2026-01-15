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
StaffType: Enumeration = Enumeration(
    name="StaffType",
    literals={
            EnumerationLiteral(name="Manager"),
			EnumerationLiteral(name="Receptionist"),
			EnumerationLiteral(name="Janitor"),
			EnumerationLiteral(name="HouseKeeper")
    }
)

# Classes
ClassDiagram_Hotel_Facility = Class(name="ClassDiagram::Hotel::Facility")
ClassDiagram_Hotel_Staff = Class(name="ClassDiagram::Hotel::Staff")
ClassDiagram_Company = Class(name="ClassDiagram::Company")
ClassDiagram_Company_Hotel = Class(name="ClassDiagram::Company::Hotel")
ClassDiagram_Company_GuestRecord = Class(name="ClassDiagram::Company::GuestRecord")
ClassDiagram_Hotel_Booking = Class(name="ClassDiagram::Hotel::Booking")
ClassDiagram_Hotel_Room = Class(name="ClassDiagram::Hotel::Room")
ClassDiagram_Booking_PurchasedService = Class(name="ClassDiagram::Booking::PurchasedService")
ClassDiagram_Booking_BookedService = Class(name="ClassDiagram::Booking::BookedService")
ClassDiagram_Booking_Bill = Class(name="ClassDiagram::Booking::Bill")
ClassDiagram_ApplianceType_ApplianceService = Class(name="ClassDiagram::ApplianceType::ApplianceService")
ClassDiagram_Room_RoomAppliance = Class(name="ClassDiagram::Room::RoomAppliance")
ClassDiagram_Room_RoomType = Class(name="ClassDiagram::Room::RoomType")
ClassDiagram_Room_RoomKey = Class(name="ClassDiagram::Room::RoomKey")
ClassDiagram_RoomAppliance_ApplianceType = Class(name="ClassDiagram::RoomAppliance::ApplianceType")
ClassDiagram_Facility_FacilityType = Class(name="ClassDiagram::Facility::FacilityType")
ClassDiagram_Facility_FacilityService = Class(name="ClassDiagram::Facility::FacilityService")
ClassDiagram_BookingManager = Class(name="ClassDiagram::BookingManager", is_abstract=True)
ClassDiagram_IRoomManager = Class(name="ClassDiagram::IRoomManager", is_abstract=True)
ClassDiagram_IGuestManager = Class(name="ClassDiagram::IGuestManager", is_abstract=True)
ClassDiagram_IFacilityManager = Class(name="ClassDiagram::IFacilityManager", is_abstract=True)
ClassDiagram_IBillManager = Class(name="ClassDiagram::IBillManager", is_abstract=True)
ClassDiagram_IApplianceAdministration = Class(name="ClassDiagram::IApplianceAdministration", is_abstract=True)
ClassDiagram_IFacilityAdministration = Class(name="ClassDiagram::IFacilityAdministration", is_abstract=True)
ClassDiagram_IRoomAdministration = Class(name="ClassDiagram::IRoomAdministration", is_abstract=True)
ClassDiagram_IStaffAdministration = Class(name="ClassDiagram::IStaffAdministration", is_abstract=True)
ClassDiagram_IHotelAdministration = Class(name="ClassDiagram::IHotelAdministration", is_abstract=True)
ClassDiagram_IServiceBooking = Class(name="ClassDiagram::IServiceBooking", is_abstract=True)
ClassDiagram_IBooking = Class(name="ClassDiagram::IBooking", is_abstract=True)
ClassDiagram_FacilityAdministration = Class(name="ClassDiagram::FacilityAdministration")
IFacilityAdministration = Class(name="IFacilityAdministration")
ClassDiagram_ServiceBooking = Class(name="ClassDiagram::ServiceBooking")
IServiceBooking = Class(name="IServiceBooking")
ClassDiagram_FacilityManager = Class(name="ClassDiagram::FacilityManager")
IFacilityManager = Class(name="IFacilityManager")
ClassDiagram_GuestManager = Class(name="ClassDiagram::GuestManager")
IGuestManager = Class(name="IGuestManager")
ClassDiagram_BillManager = Class(name="ClassDiagram::BillManager")
IBillManager = Class(name="IBillManager")
ClassDiagram_GuestBooking = Class(name="ClassDiagram::GuestBooking")
IBooking = Class(name="IBooking")
ClassDiagram_StaffBooking = Class(name="ClassDiagram::StaffBooking")
BookingManager = Class(name="BookingManager")
ClassDiagram_HotelAdministration = Class(name="ClassDiagram::HotelAdministration")
IHotelAdministration = Class(name="IHotelAdministration")
ClassDiagram_StaffAdministration = Class(name="ClassDiagram::StaffAdministration")
IStaffAdministration = Class(name="IStaffAdministration")
ClassDiagram_RoomManager = Class(name="ClassDiagram::RoomManager")
IRoomManager = Class(name="IRoomManager")
ClassDiagram_RoomAdministration = Class(name="ClassDiagram::RoomAdministration")
IRoomAdministration = Class(name="IRoomAdministration")
ClassDiagram_ApplianceAdministration = Class(name="ClassDiagram::ApplianceAdministration")
IApplianceAdministration = Class(name="IApplianceAdministration")

# ClassDiagram_Hotel_Facility class attributes and methods
ClassDiagram_Hotel_Facility_name: Property = Property(name="name", type=StringType)
ClassDiagram_Hotel_Facility.attributes={ClassDiagram_Hotel_Facility_name}

# ClassDiagram_Hotel_Staff class attributes and methods
ClassDiagram_Hotel_Staff_ssn: Property = Property(name="ssn", type=StringType)
ClassDiagram_Hotel_Staff_firstName: Property = Property(name="firstName", type=StringType)
ClassDiagram_Hotel_Staff_lastName: Property = Property(name="lastName", type=StringType)
ClassDiagram_Hotel_Staff_stafftype: Property = Property(name="stafftype", type=StringType)
ClassDiagram_Hotel_Staff.attributes={ClassDiagram_Hotel_Staff_stafftype, ClassDiagram_Hotel_Staff_lastName, ClassDiagram_Hotel_Staff_ssn, ClassDiagram_Hotel_Staff_firstName}

# ClassDiagram_Company class attributes and methods
ClassDiagram_Company_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company.attributes={ClassDiagram_Company_name}

# ClassDiagram_Company_Hotel class attributes and methods
ClassDiagram_Company_Hotel_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company_Hotel.attributes={ClassDiagram_Company_Hotel_name}

# ClassDiagram_Company_GuestRecord class attributes and methods
ClassDiagram_Company_GuestRecord_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company_GuestRecord_adress: Property = Property(name="adress", type=StringType)
ClassDiagram_Company_GuestRecord_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
ClassDiagram_Company_GuestRecord_ssn: Property = Property(name="ssn", type=StringType)
ClassDiagram_Company_GuestRecord_payment: Property = Property(name="payment", type=StringType)
ClassDiagram_Company_GuestRecord.attributes={ClassDiagram_Company_GuestRecord_name, ClassDiagram_Company_GuestRecord_ssn, ClassDiagram_Company_GuestRecord_adress, ClassDiagram_Company_GuestRecord_payment, ClassDiagram_Company_GuestRecord_phoneNumber}

# ClassDiagram_Hotel_Booking class attributes and methods
ClassDiagram_Hotel_Booking_startDate: Property = Property(name="startDate", type=DateType)
ClassDiagram_Hotel_Booking_endDate: Property = Property(name="endDate", type=DateType)
ClassDiagram_Hotel_Booking_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Hotel_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
ClassDiagram_Hotel_Booking_bookingID: Property = Property(name="bookingID", type=IntegerType)
ClassDiagram_Hotel_Booking.attributes={ClassDiagram_Hotel_Booking_checkedIn, ClassDiagram_Hotel_Booking_startDate, ClassDiagram_Hotel_Booking_price, ClassDiagram_Hotel_Booking_endDate, ClassDiagram_Hotel_Booking_bookingID}

# ClassDiagram_Hotel_Room class attributes and methods
ClassDiagram_Hotel_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
ClassDiagram_Hotel_Room_cleaningStatus: Property = Property(name="cleaningStatus", type=BooleanType)
ClassDiagram_Hotel_Room_maintenceStatus: Property = Property(name="maintenceStatus", type=BooleanType)
ClassDiagram_Hotel_Room.attributes={ClassDiagram_Hotel_Room_maintenceStatus, ClassDiagram_Hotel_Room_cleaningStatus, ClassDiagram_Hotel_Room_roomNumber}

# ClassDiagram_Booking_PurchasedService class attributes and methods
ClassDiagram_Booking_PurchasedService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Booking_PurchasedService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Booking_PurchasedService.attributes={ClassDiagram_Booking_PurchasedService_price, ClassDiagram_Booking_PurchasedService_name}

# ClassDiagram_Booking_BookedService class attributes and methods
ClassDiagram_Booking_BookedService_date: Property = Property(name="date", type=DateType)
ClassDiagram_Booking_BookedService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Booking_BookedService.attributes={ClassDiagram_Booking_BookedService_date, ClassDiagram_Booking_BookedService_price}

# ClassDiagram_Booking_Bill class attributes and methods
ClassDiagram_Booking_Bill_paidAmount: Property = Property(name="paidAmount", type=FloatType)
ClassDiagram_Booking_Bill.attributes={ClassDiagram_Booking_Bill_paidAmount}

# ClassDiagram_ApplianceType_ApplianceService class attributes and methods
ClassDiagram_ApplianceType_ApplianceService_name: Property = Property(name="name", type=StringType)
ClassDiagram_ApplianceType_ApplianceService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_ApplianceType_ApplianceService.attributes={ClassDiagram_ApplianceType_ApplianceService_name, ClassDiagram_ApplianceType_ApplianceService_price}

# ClassDiagram_Room_RoomAppliance class attributes and methods
ClassDiagram_Room_RoomAppliance_name: Property = Property(name="name", type=StringType)
ClassDiagram_Room_RoomAppliance.attributes={ClassDiagram_Room_RoomAppliance_name}

# ClassDiagram_Room_RoomType class attributes and methods
ClassDiagram_Room_RoomType_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Room_RoomType_maxNumberOfGuests: Property = Property(name="maxNumberOfGuests", type=IntegerType)
ClassDiagram_Room_RoomType_area: Property = Property(name="area", type=FloatType)
ClassDiagram_Room_RoomType.attributes={ClassDiagram_Room_RoomType_price, ClassDiagram_Room_RoomType_maxNumberOfGuests, ClassDiagram_Room_RoomType_area}

# ClassDiagram_Room_RoomKey class attributes and methods
ClassDiagram_Room_RoomKey_expirationDate: Property = Property(name="expirationDate", type=DateType)
ClassDiagram_Room_RoomKey.attributes={ClassDiagram_Room_RoomKey_expirationDate}

# ClassDiagram_RoomAppliance_ApplianceType class attributes and methods
ClassDiagram_RoomAppliance_ApplianceType_name: Property = Property(name="name", type=StringType)
ClassDiagram_RoomAppliance_ApplianceType.attributes={ClassDiagram_RoomAppliance_ApplianceType_name}

# ClassDiagram_Facility_FacilityType class attributes and methods
ClassDiagram_Facility_FacilityType_kind: Property = Property(name="kind", type=StringType)
ClassDiagram_Facility_FacilityType.attributes={ClassDiagram_Facility_FacilityType_kind}

# ClassDiagram_Facility_FacilityService class attributes and methods
ClassDiagram_Facility_FacilityService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Facility_FacilityService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Facility_FacilityService.attributes={ClassDiagram_Facility_FacilityService_name, ClassDiagram_Facility_FacilityService_price}

# ClassDiagram_BookingManager class attributes and methods
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='guestSSN'), Parameter(name='date')})
ClassDiagram_BookingManager_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='booking')})
ClassDiagram_BookingManager_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')})
ClassDiagram_BookingManager_m_assignKey: Method = Method(name="assignKey", parameters={Parameter(name='booking'), Parameter(name='rooms'), Parameter(name='expirationDate')})
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='roomNr'), Parameter(name='date')})
ClassDiagram_BookingManager.methods={ClassDiagram_BookingManager_m_checkIn, ClassDiagram_BookingManager_m_assignKey, ClassDiagram_BookingManager_m_checkOut, ClassDiagram_BookingManager_m_findBooking, ClassDiagram_BookingManager_m_findBooking}

# ClassDiagram_IRoomManager class attributes and methods
ClassDiagram_IRoomManager_m_maintenanceStatus: Method = Method(name="maintenanceStatus", parameters={Parameter(name='room')})
ClassDiagram_IRoomManager_m_getRoomsToClean: Method = Method(name="getRoomsToClean", parameters={})
ClassDiagram_IRoomManager_m_getRoomsToMaintain: Method = Method(name="getRoomsToMaintain", parameters={})
ClassDiagram_IRoomManager_m_findRoom: Method = Method(name="findRoom", parameters={Parameter(name='roomNumber')})
ClassDiagram_IRoomManager_m_cleaningStatus: Method = Method(name="cleaningStatus", parameters={Parameter(name='room')})
ClassDiagram_IRoomManager.methods={ClassDiagram_IRoomManager_m_maintenanceStatus, ClassDiagram_IRoomManager_m_getRoomsToClean, ClassDiagram_IRoomManager_m_getRoomsToMaintain, ClassDiagram_IRoomManager_m_cleaningStatus, ClassDiagram_IRoomManager_m_findRoom}

# ClassDiagram_IGuestManager class attributes and methods
ClassDiagram_IGuestManager_m_editGuestRecord: Method = Method(name="editGuestRecord", parameters={Parameter(name='guest')})
ClassDiagram_IGuestManager_m_removeGuestRecord: Method = Method(name="removeGuestRecord", parameters={Parameter(name='guest')})
ClassDiagram_IGuestManager_m_createGuestRecord: Method = Method(name="createGuestRecord", parameters={Parameter(name='lastName'), Parameter(name='phoneNumber'), Parameter(name='firstName'), Parameter(name='adress'), Parameter(name='ssn')})
ClassDiagram_IGuestManager_m_findGuest: Method = Method(name="findGuest", parameters={Parameter(name='ssn')})
ClassDiagram_IGuestManager_m_findGuests: Method = Method(name="findGuests", parameters={Parameter(name='firstName'), Parameter(name='lastName')})
ClassDiagram_IGuestManager.methods={ClassDiagram_IGuestManager_m_removeGuestRecord, ClassDiagram_IGuestManager_m_createGuestRecord, ClassDiagram_IGuestManager_m_findGuests, ClassDiagram_IGuestManager_m_editGuestRecord, ClassDiagram_IGuestManager_m_findGuest}

# ClassDiagram_IFacilityManager class attributes and methods
ClassDiagram_IFacilityManager_m_findBookedService: Method = Method(name="findBookedService", parameters={Parameter(name='date'), Parameter(name='facilityService')})
ClassDiagram_IFacilityManager_m_findBookedServices: Method = Method(name="findBookedServices", parameters={Parameter(name='guest')})
ClassDiagram_IFacilityManager.methods={ClassDiagram_IFacilityManager_m_findBookedServices, ClassDiagram_IFacilityManager_m_findBookedService}

# ClassDiagram_IBillManager class attributes and methods
ClassDiagram_IBillManager_m_getAmount: Method = Method(name="getAmount", parameters={Parameter(name='bill')})
ClassDiagram_IBillManager_m_pay: Method = Method(name="pay", parameters={Parameter(name='bill'), Parameter(name='amount')})
ClassDiagram_IBillManager_m_addPurchesedService: Method = Method(name="addPurchesedService", parameters={Parameter(name='item'), Parameter(name='bill'), Parameter(name='amount')})
ClassDiagram_IBillManager_m_findBill: Method = Method(name="findBill", parameters={Parameter(name='booking')})
ClassDiagram_IBillManager_m_createReceipt: Method = Method(name="createReceipt", parameters={Parameter(name='bill')})
ClassDiagram_IBillManager.methods={ClassDiagram_IBillManager_m_findBill, ClassDiagram_IBillManager_m_addPurchesedService, ClassDiagram_IBillManager_m_pay, ClassDiagram_IBillManager_m_createReceipt, ClassDiagram_IBillManager_m_getAmount}

# ClassDiagram_IApplianceAdministration class attributes and methods
ClassDiagram_IApplianceAdministration_m_editAppliance: Method = Method(name="editAppliance", parameters={Parameter(name='appliance')})
ClassDiagram_IApplianceAdministration_m_addApplianceService: Method = Method(name="addApplianceService", parameters={Parameter(name='price'), Parameter(name='name')})
ClassDiagram_IApplianceAdministration_m_editApplianceService: Method = Method(name="editApplianceService", parameters={Parameter(name='service')})
ClassDiagram_IApplianceAdministration_m_removeApplianceService: Method = Method(name="removeApplianceService", parameters={Parameter(name='service')})
ClassDiagram_IApplianceAdministration_m_addAppliance: Method = Method(name="addAppliance", parameters={Parameter(name='room')})
ClassDiagram_IApplianceAdministration_m_removeAppliance: Method = Method(name="removeAppliance", parameters={Parameter(name='appliance')})
ClassDiagram_IApplianceAdministration_m_addApplianceType: Method = Method(name="addApplianceType", parameters={Parameter(name='name')})
ClassDiagram_IApplianceAdministration_m_editApplianceType: Method = Method(name="editApplianceType", parameters={Parameter(name='applianceType')})
ClassDiagram_IApplianceAdministration_m_removeApplianceType: Method = Method(name="removeApplianceType", parameters={Parameter(name='applianceType')})
ClassDiagram_IApplianceAdministration.methods={ClassDiagram_IApplianceAdministration_m_addAppliance, ClassDiagram_IApplianceAdministration_m_addApplianceType, ClassDiagram_IApplianceAdministration_m_removeAppliance, ClassDiagram_IApplianceAdministration_m_editApplianceService, ClassDiagram_IApplianceAdministration_m_editApplianceType, ClassDiagram_IApplianceAdministration_m_removeApplianceService, ClassDiagram_IApplianceAdministration_m_removeApplianceType, ClassDiagram_IApplianceAdministration_m_addApplianceService, ClassDiagram_IApplianceAdministration_m_editAppliance}

# ClassDiagram_IFacilityAdministration class attributes and methods
ClassDiagram_IFacilityAdministration_m_addFacility: Method = Method(name="addFacility", parameters={Parameter(name='facilityType'), Parameter(name='name')})
ClassDiagram_IFacilityAdministration_m_editFacility: Method = Method(name="editFacility", parameters={Parameter(name='facility')})
ClassDiagram_IFacilityAdministration_m_removeFacility: Method = Method(name="removeFacility", parameters={Parameter(name='facility')})
ClassDiagram_IFacilityAdministration_m_addFacilityType: Method = Method(name="addFacilityType", parameters={Parameter(name='kind')})
ClassDiagram_IFacilityAdministration_m_editFacilityType: Method = Method(name="editFacilityType", parameters={Parameter(name='facilityType')})
ClassDiagram_IFacilityAdministration_m_removeFacilityType: Method = Method(name="removeFacilityType", parameters={Parameter(name='facilityType')})
ClassDiagram_IFacilityAdministration_m_addService: Method = Method(name="addService", parameters={Parameter(name='price'), Parameter(name='facility'), Parameter(name='name')})
ClassDiagram_IFacilityAdministration_m_editService: Method = Method(name="editService", parameters={Parameter(name='service')})
ClassDiagram_IFacilityAdministration_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='service')})
ClassDiagram_IFacilityAdministration.methods={ClassDiagram_IFacilityAdministration_m_addFacility, ClassDiagram_IFacilityAdministration_m_editFacility, ClassDiagram_IFacilityAdministration_m_addFacilityType, ClassDiagram_IFacilityAdministration_m_editService, ClassDiagram_IFacilityAdministration_m_editFacilityType, ClassDiagram_IFacilityAdministration_m_removeFacility, ClassDiagram_IFacilityAdministration_m_removeFacilityType, ClassDiagram_IFacilityAdministration_m_addService, ClassDiagram_IFacilityAdministration_m_removeService}

# ClassDiagram_IRoomAdministration class attributes and methods
ClassDiagram_IRoomAdministration_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='roomNumber'), Parameter(name='roomType')})
ClassDiagram_IRoomAdministration_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='room')})
ClassDiagram_IRoomAdministration_m_editRoom: Method = Method(name="editRoom", parameters={Parameter(name='room')})
ClassDiagram_IRoomAdministration_m_createRoomType: Method = Method(name="createRoomType", parameters={})
ClassDiagram_IRoomAdministration_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='roomType')})
ClassDiagram_IRoomAdministration_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='roomType')})
ClassDiagram_IRoomAdministration.methods={ClassDiagram_IRoomAdministration_m_removeRoom, ClassDiagram_IRoomAdministration_m_addRoom, ClassDiagram_IRoomAdministration_m_editRoomType, ClassDiagram_IRoomAdministration_m_editRoom, ClassDiagram_IRoomAdministration_m_removeRoomType, ClassDiagram_IRoomAdministration_m_createRoomType}

# ClassDiagram_IStaffAdministration class attributes and methods
ClassDiagram_IStaffAdministration_m_addStaff: Method = Method(name="addStaff", parameters={})
ClassDiagram_IStaffAdministration_m_editStaff: Method = Method(name="editStaff", parameters={})
ClassDiagram_IStaffAdministration_m_removeStaff: Method = Method(name="removeStaff", parameters={})
ClassDiagram_IStaffAdministration.methods={ClassDiagram_IStaffAdministration_m_addStaff, ClassDiagram_IStaffAdministration_m_editStaff, ClassDiagram_IStaffAdministration_m_removeStaff}

# ClassDiagram_IHotelAdministration class attributes and methods
ClassDiagram_IHotelAdministration_m_addHotel: Method = Method(name="addHotel", parameters={})
ClassDiagram_IHotelAdministration_m_editHotel: Method = Method(name="editHotel", parameters={})
ClassDiagram_IHotelAdministration_m_removeHotel: Method = Method(name="removeHotel", parameters={})
ClassDiagram_IHotelAdministration.methods={ClassDiagram_IHotelAdministration_m_addHotel, ClassDiagram_IHotelAdministration_m_removeHotel, ClassDiagram_IHotelAdministration_m_editHotel}

# ClassDiagram_IServiceBooking class attributes and methods
ClassDiagram_IServiceBooking_m_bookFacilityService: Method = Method(name="bookFacilityService", parameters={Parameter(name='facility'), Parameter(name='service'), Parameter(name='booking'), Parameter(name='guest'), Parameter(name='date')})
ClassDiagram_IServiceBooking_m_findAvailableServices: Method = Method(name="findAvailableServices", parameters={Parameter(name='facility'), Parameter(name='date')})
ClassDiagram_IServiceBooking_m_getBookedServices: Method = Method(name="getBookedServices", parameters={Parameter(name='booking')})
ClassDiagram_IServiceBooking_m_findBookedService: Method = Method(name="findBookedService", parameters={Parameter(name='bookedServiceID')})
ClassDiagram_IServiceBooking_m_cancelBookedService: Method = Method(name="cancelBookedService", parameters={Parameter(name='service')})
ClassDiagram_IServiceBooking.methods={ClassDiagram_IServiceBooking_m_bookFacilityService, ClassDiagram_IServiceBooking_m_findBookedService, ClassDiagram_IServiceBooking_m_getBookedServices, ClassDiagram_IServiceBooking_m_findAvailableServices, ClassDiagram_IServiceBooking_m_cancelBookedService}

# ClassDiagram_IBooking class attributes and methods
ClassDiagram_IBooking_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='bookingNumber')})
ClassDiagram_IBooking_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='guest')})
ClassDiagram_IBooking_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='end'), Parameter(name='guest'), Parameter(name='rooms'), Parameter(name='start')})
ClassDiagram_IBooking_m_findAvailableRooms: Method = Method(name="findAvailableRooms", parameters={Parameter(name='end'), Parameter(name='roomType'), Parameter(name='start')})
ClassDiagram_IBooking_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='booking')})
ClassDiagram_IBooking_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='booking')})
ClassDiagram_IBooking.methods={ClassDiagram_IBooking_m_cancelBooking, ClassDiagram_IBooking_m_findBooking, ClassDiagram_IBooking_m_editBooking, ClassDiagram_IBooking_m_createBooking, ClassDiagram_IBooking_m_getBookings, ClassDiagram_IBooking_m_findAvailableRooms}

# ClassDiagram_FacilityAdministration class attributes and methods

# IFacilityAdministration class attributes and methods

# ClassDiagram_ServiceBooking class attributes and methods

# IServiceBooking class attributes and methods

# ClassDiagram_FacilityManager class attributes and methods

# IFacilityManager class attributes and methods

# ClassDiagram_GuestManager class attributes and methods

# IGuestManager class attributes and methods

# ClassDiagram_BillManager class attributes and methods

# IBillManager class attributes and methods

# ClassDiagram_GuestBooking class attributes and methods

# IBooking class attributes and methods

# ClassDiagram_StaffBooking class attributes and methods

# BookingManager class attributes and methods

# ClassDiagram_HotelAdministration class attributes and methods

# IHotelAdministration class attributes and methods

# ClassDiagram_StaffAdministration class attributes and methods

# IStaffAdministration class attributes and methods

# ClassDiagram_RoomManager class attributes and methods

# IRoomManager class attributes and methods

# ClassDiagram_RoomAdministration class attributes and methods

# IRoomAdministration class attributes and methods

# ClassDiagram_ApplianceAdministration class attributes and methods

# IApplianceAdministration class attributes and methods

# Relationships
hasRoom5: BinaryAssociation = BinaryAssociation(
    name="hasRoom5",
    ends={
        Property(name="ClassDiagram_Company_Hotel6", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(0, 9999)),
        Property(name="ClassDiagram_Hotel_Room", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hasFacility7: BinaryAssociation = BinaryAssociation(
    name="hasFacility7",
    ends={
        Property(name="ClassDiagram_Hotel_Facility", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel8", type=ClassDiagram_Hotel_Facility, multiplicity=Multiplicity(0, 9999))
    }
)
employee9: BinaryAssociation = BinaryAssociation(
    name="employee9",
    ends={
        Property(name="ClassDiagram_Hotel_Staff", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel10", type=ClassDiagram_Hotel_Staff, multiplicity=Multiplicity(0, 9999))
    }
)
hasHotel0: BinaryAssociation = BinaryAssociation(
    name="hasHotel0",
    ends={
        Property(name="ClassDiagram_Company_Hotel", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 9999))
    }
)
hasGuest1: BinaryAssociation = BinaryAssociation(
    name="hasGuest1",
    ends={
        Property(name="ClassDiagram_Company_GuestRecord", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company2", type=ClassDiagram_Company_GuestRecord, multiplicity=Multiplicity(0, 9999))
    }
)
hasBooking3: BinaryAssociation = BinaryAssociation(
    name="hasBooking3",
    ends={
        Property(name="ClassDiagram_Hotel_Booking", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel4", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
hasPurchaseditem13: BinaryAssociation = BinaryAssociation(
    name="hasPurchaseditem13",
    ends={
        Property(name="ClassDiagram_Booking_PurchasedService", type=ClassDiagram_Booking_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Booking_Bill", type=ClassDiagram_Booking_PurchasedService, multiplicity=Multiplicity(0, 9999))
    }
)
bookedservice11: BinaryAssociation = BinaryAssociation(
    name="bookedservice11",
    ends={
        Property(name="ClassDiagram_Booking_BookedService", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Booking12", type=ClassDiagram_Booking_BookedService, multiplicity=Multiplicity(0, 9999))
    }
)
roomAppliances14: BinaryAssociation = BinaryAssociation(
    name="roomAppliances14",
    ends={
        Property(name="ClassDiagram_Room_RoomAppliance", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Room15", type=ClassDiagram_Room_RoomAppliance, multiplicity=Multiplicity(0, 9999))
    }
)
hasType16: BinaryAssociation = BinaryAssociation(
    name="hasType16",
    ends={
        Property(name="ClassDiagram_Room_RoomType", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Room17", type=ClassDiagram_Room_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
hasKey18: BinaryAssociation = BinaryAssociation(
    name="hasKey18",
    ends={
        Property(name="ClassDiagram_Room_RoomKey", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Room19", type=ClassDiagram_Room_RoomKey, multiplicity=Multiplicity(0, 9999))
    }
)
hasApplianceType20: BinaryAssociation = BinaryAssociation(
    name="hasApplianceType20",
    ends={
        Property(name="ClassDiagram_RoomAppliance_ApplianceType", type=ClassDiagram_Room_RoomAppliance, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Room_RoomAppliance21", type=ClassDiagram_RoomAppliance_ApplianceType, multiplicity=Multiplicity(1, 1))
    }
)
hasAppliance22: BinaryAssociation = BinaryAssociation(
    name="hasAppliance22",
    ends={
        Property(name="ClassDiagram_Room_RoomAppliance24", type=ClassDiagram_Room_RoomType, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Room_RoomType23", type=ClassDiagram_Room_RoomAppliance, multiplicity=Multiplicity(0, 9999))
    }
)
hasType25: BinaryAssociation = BinaryAssociation(
    name="hasType25",
    ends={
        Property(name="ClassDiagram_Facility_FacilityType", type=ClassDiagram_Hotel_Facility, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Facility26", type=ClassDiagram_Facility_FacilityType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ClassDiagram_StaffBooking_BookingManager = Generalization(general=BookingManager, specific=ClassDiagram_StaffBooking)
gen_ClassDiagram_FacilityAdministration_IFacilityAdministration = Generalization(general=IFacilityAdministration, specific=ClassDiagram_FacilityAdministration)
gen_ClassDiagram_ServiceBooking_IServiceBooking = Generalization(general=IServiceBooking, specific=ClassDiagram_ServiceBooking)
gen_ClassDiagram_FacilityManager_IFacilityManager = Generalization(general=IFacilityManager, specific=ClassDiagram_FacilityManager)
gen_ClassDiagram_GuestManager_IGuestManager = Generalization(general=IGuestManager, specific=ClassDiagram_GuestManager)
gen_ClassDiagram_BillManager_IBillManager = Generalization(general=IBillManager, specific=ClassDiagram_BillManager)
gen_ClassDiagram_GuestBooking_IBooking = Generalization(general=IBooking, specific=ClassDiagram_GuestBooking)
gen_ClassDiagram_HotelAdministration_IHotelAdministration = Generalization(general=IHotelAdministration, specific=ClassDiagram_HotelAdministration)
gen_ClassDiagram_StaffAdministration_IStaffAdministration = Generalization(general=IStaffAdministration, specific=ClassDiagram_StaffAdministration)
gen_ClassDiagram_RoomManager_IRoomManager = Generalization(general=IRoomManager, specific=ClassDiagram_RoomManager)
gen_ClassDiagram_RoomAdministration_IRoomAdministration = Generalization(general=IRoomAdministration, specific=ClassDiagram_RoomAdministration)
gen_ClassDiagram_ApplianceAdministration_IApplianceAdministration = Generalization(general=IApplianceAdministration, specific=ClassDiagram_ApplianceAdministration)

# Domain Model
domain_model = DomainModel(
    name="ClassDiagram",
    types={ClassDiagram_Hotel_Facility, ClassDiagram_Hotel_Staff, ClassDiagram_Company, ClassDiagram_Company_Hotel, ClassDiagram_Company_GuestRecord, ClassDiagram_Hotel_Booking, ClassDiagram_Hotel_Room, ClassDiagram_Booking_PurchasedService, ClassDiagram_Booking_BookedService, ClassDiagram_Booking_Bill, ClassDiagram_ApplianceType_ApplianceService, ClassDiagram_Room_RoomAppliance, ClassDiagram_Room_RoomType, ClassDiagram_Room_RoomKey, ClassDiagram_RoomAppliance_ApplianceType, ClassDiagram_Facility_FacilityType, ClassDiagram_Facility_FacilityService, ClassDiagram_BookingManager, ClassDiagram_IRoomManager, ClassDiagram_IGuestManager, ClassDiagram_IFacilityManager, ClassDiagram_IBillManager, ClassDiagram_IApplianceAdministration, ClassDiagram_IFacilityAdministration, ClassDiagram_IRoomAdministration, ClassDiagram_IStaffAdministration, ClassDiagram_IHotelAdministration, ClassDiagram_IServiceBooking, ClassDiagram_IBooking, ClassDiagram_FacilityAdministration, IFacilityAdministration, ClassDiagram_ServiceBooking, IServiceBooking, ClassDiagram_FacilityManager, IFacilityManager, ClassDiagram_GuestManager, IGuestManager, ClassDiagram_BillManager, IBillManager, ClassDiagram_GuestBooking, IBooking, ClassDiagram_StaffBooking, BookingManager, ClassDiagram_HotelAdministration, IHotelAdministration, ClassDiagram_StaffAdministration, IStaffAdministration, ClassDiagram_RoomManager, IRoomManager, ClassDiagram_RoomAdministration, IRoomAdministration, ClassDiagram_ApplianceAdministration, IApplianceAdministration, StaffType},
    associations={hasRoom5, hasFacility7, employee9, hasHotel0, hasGuest1, hasBooking3, hasPurchaseditem13, bookedservice11, roomAppliances14, hasType16, hasKey18, hasApplianceType20, hasAppliance22, hasType25},
    generalizations={gen_ClassDiagram_StaffBooking_BookingManager, gen_ClassDiagram_FacilityAdministration_IFacilityAdministration, gen_ClassDiagram_ServiceBooking_IServiceBooking, gen_ClassDiagram_FacilityManager_IFacilityManager, gen_ClassDiagram_GuestManager_IGuestManager, gen_ClassDiagram_BillManager_IBillManager, gen_ClassDiagram_GuestBooking_IBooking, gen_ClassDiagram_HotelAdministration_IHotelAdministration, gen_ClassDiagram_StaffAdministration_IStaffAdministration, gen_ClassDiagram_RoomManager_IRoomManager, gen_ClassDiagram_RoomAdministration_IRoomAdministration, gen_ClassDiagram_ApplianceAdministration_IApplianceAdministration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)