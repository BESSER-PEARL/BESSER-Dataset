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
ClassDiagram_Company = Class(name="ClassDiagram_Company")
ClassDiagram_Company_Hotel = Class(name="ClassDiagram_Company_Hotel")
ClassDiagram_Company_GuestRecord = Class(name="ClassDiagram_Company_GuestRecord")
ClassDiagram_Hotel_Booking = Class(name="ClassDiagram_Hotel_Booking")
ClassDiagram_Hotel_Room = Class(name="ClassDiagram_Hotel_Room")
ClassDiagram_Hotel_Facility = Class(name="ClassDiagram_Hotel_Facility")
ClassDiagram_Hotel_Staff = Class(name="ClassDiagram_Hotel_Staff")
ClassDiagram_Booking_BookedService = Class(name="ClassDiagram_Booking_BookedService")
ClassDiagram_Booking_Bill = Class(name="ClassDiagram_Booking_Bill")
ClassDiagram_Room_RoomType = Class(name="ClassDiagram_Room_RoomType")
ClassDiagram_Room_RoomKey = Class(name="ClassDiagram_Room_RoomKey")
ClassDiagram_RoomAppliance_ApplianceType = Class(name="ClassDiagram_RoomAppliance_ApplianceType")
ClassDiagram_ApplianceType_ApplianceService = Class(name="ClassDiagram_ApplianceType_ApplianceService")
ClassDiagram_Facility_FacilityType = Class(name="ClassDiagram_Facility_FacilityType")
ClassDiagram_Facility_FacilityService = Class(name="ClassDiagram_Facility_FacilityService")
ClassDiagram_Booking_PurchasedService = Class(name="ClassDiagram_Booking_PurchasedService")
ClassDiagram_Room_RoomAppliance = Class(name="ClassDiagram_Room_RoomAppliance")
ClassDiagram_IRoomManager = Class(name="ClassDiagram_IRoomManager", is_abstract=True)
ClassDiagram_BookingManager = Class(name="ClassDiagram_BookingManager", is_abstract=True)
ClassDiagram_IGuestManager = Class(name="ClassDiagram_IGuestManager", is_abstract=True)
ClassDiagram_IBillManager = Class(name="ClassDiagram_IBillManager", is_abstract=True)
ClassDiagram_IFacilityManager = Class(name="ClassDiagram_IFacilityManager", is_abstract=True)
ClassDiagram_IApplianceAdministration = Class(name="ClassDiagram_IApplianceAdministration", is_abstract=True)
ClassDiagram_IRoomAdministration = Class(name="ClassDiagram_IRoomAdministration", is_abstract=True)
ClassDiagram_IFacilityAdministration = Class(name="ClassDiagram_IFacilityAdministration", is_abstract=True)
ClassDiagram_IBooking = Class(name="ClassDiagram_IBooking", is_abstract=True)
ClassDiagram_IServiceBooking = Class(name="ClassDiagram_IServiceBooking", is_abstract=True)
ClassDiagram_GuestBooking = Class(name="ClassDiagram_GuestBooking")
IBooking = Class(name="IBooking")
ClassDiagram_StaffBooking = Class(name="ClassDiagram_StaffBooking")
BookingManager = Class(name="BookingManager")
ClassDiagram_IStaffAdministration = Class(name="ClassDiagram_IStaffAdministration", is_abstract=True)
ClassDiagram_IHotelAdministration = Class(name="ClassDiagram_IHotelAdministration", is_abstract=True)
ClassDiagram_HotelAdministration = Class(name="ClassDiagram_HotelAdministration")
IHotelAdministration = Class(name="IHotelAdministration")
ClassDiagram_StaffAdministration = Class(name="ClassDiagram_StaffAdministration")
IStaffAdministration = Class(name="IStaffAdministration")
ClassDiagram_RoomManager = Class(name="ClassDiagram_RoomManager")
IRoomManager = Class(name="IRoomManager")
ClassDiagram_RoomAdministration = Class(name="ClassDiagram_RoomAdministration")
IRoomAdministration = Class(name="IRoomAdministration")
ClassDiagram_ApplianceAdministration = Class(name="ClassDiagram_ApplianceAdministration")
IApplianceAdministration = Class(name="IApplianceAdministration")
ClassDiagram_FacilityAdministration = Class(name="ClassDiagram_FacilityAdministration")
IFacilityAdministration = Class(name="IFacilityAdministration")
ClassDiagram_ServiceBooking = Class(name="ClassDiagram_ServiceBooking")
IServiceBooking = Class(name="IServiceBooking")
ClassDiagram_FacilityManager = Class(name="ClassDiagram_FacilityManager")
IFacilityManager = Class(name="IFacilityManager")
ClassDiagram_GuestManager = Class(name="ClassDiagram_GuestManager")
IGuestManager = Class(name="IGuestManager")
ClassDiagram_BillManager = Class(name="ClassDiagram_BillManager")
IBillManager = Class(name="IBillManager")

# ClassDiagram_Company class attributes and methods
ClassDiagram_Company_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company.attributes={ClassDiagram_Company_name}

# ClassDiagram_Company_Hotel class attributes and methods
ClassDiagram_Company_Hotel_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company_Hotel.attributes={ClassDiagram_Company_Hotel_name}

# ClassDiagram_Company_GuestRecord class attributes and methods
ClassDiagram_Company_GuestRecord_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
ClassDiagram_Company_GuestRecord_ssn: Property = Property(name="ssn", type=StringType)
ClassDiagram_Company_GuestRecord_payment: Property = Property(name="payment", type=StringType)
ClassDiagram_Company_GuestRecord_name: Property = Property(name="name", type=StringType)
ClassDiagram_Company_GuestRecord_adress: Property = Property(name="adress", type=StringType)
ClassDiagram_Company_GuestRecord.attributes={ClassDiagram_Company_GuestRecord_ssn, ClassDiagram_Company_GuestRecord_adress, ClassDiagram_Company_GuestRecord_name, ClassDiagram_Company_GuestRecord_payment, ClassDiagram_Company_GuestRecord_phoneNumber}

# ClassDiagram_Hotel_Booking class attributes and methods
ClassDiagram_Hotel_Booking_startDate: Property = Property(name="startDate", type=DateType)
ClassDiagram_Hotel_Booking_endDate: Property = Property(name="endDate", type=DateType)
ClassDiagram_Hotel_Booking_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Hotel_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
ClassDiagram_Hotel_Booking_bookingID: Property = Property(name="bookingID", type=IntegerType)
ClassDiagram_Hotel_Booking.attributes={ClassDiagram_Hotel_Booking_startDate, ClassDiagram_Hotel_Booking_endDate, ClassDiagram_Hotel_Booking_checkedIn, ClassDiagram_Hotel_Booking_bookingID, ClassDiagram_Hotel_Booking_price}

# ClassDiagram_Hotel_Room class attributes and methods
ClassDiagram_Hotel_Room_cleaningStatus: Property = Property(name="cleaningStatus", type=BooleanType)
ClassDiagram_Hotel_Room_maintenceStatus: Property = Property(name="maintenceStatus", type=BooleanType)
ClassDiagram_Hotel_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
ClassDiagram_Hotel_Room.attributes={ClassDiagram_Hotel_Room_roomNumber, ClassDiagram_Hotel_Room_cleaningStatus, ClassDiagram_Hotel_Room_maintenceStatus}

# ClassDiagram_Hotel_Facility class attributes and methods
ClassDiagram_Hotel_Facility_name: Property = Property(name="name", type=StringType)
ClassDiagram_Hotel_Facility.attributes={ClassDiagram_Hotel_Facility_name}

# ClassDiagram_Hotel_Staff class attributes and methods
ClassDiagram_Hotel_Staff_ssn: Property = Property(name="ssn", type=StringType)
ClassDiagram_Hotel_Staff_firstName: Property = Property(name="firstName", type=StringType)
ClassDiagram_Hotel_Staff_lastName: Property = Property(name="lastName", type=StringType)
ClassDiagram_Hotel_Staff_stafftype: Property = Property(name="stafftype", type=StringType)
ClassDiagram_Hotel_Staff.attributes={ClassDiagram_Hotel_Staff_ssn, ClassDiagram_Hotel_Staff_lastName, ClassDiagram_Hotel_Staff_firstName, ClassDiagram_Hotel_Staff_stafftype}

# ClassDiagram_Booking_BookedService class attributes and methods
ClassDiagram_Booking_BookedService_date: Property = Property(name="date", type=DateType)
ClassDiagram_Booking_BookedService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Booking_BookedService.attributes={ClassDiagram_Booking_BookedService_date, ClassDiagram_Booking_BookedService_price}

# ClassDiagram_Booking_Bill class attributes and methods
ClassDiagram_Booking_Bill_paidAmount: Property = Property(name="paidAmount", type=FloatType)
ClassDiagram_Booking_Bill.attributes={ClassDiagram_Booking_Bill_paidAmount}

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

# ClassDiagram_ApplianceType_ApplianceService class attributes and methods
ClassDiagram_ApplianceType_ApplianceService_name: Property = Property(name="name", type=StringType)
ClassDiagram_ApplianceType_ApplianceService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_ApplianceType_ApplianceService.attributes={ClassDiagram_ApplianceType_ApplianceService_name, ClassDiagram_ApplianceType_ApplianceService_price}

# ClassDiagram_Facility_FacilityType class attributes and methods
ClassDiagram_Facility_FacilityType_kind: Property = Property(name="kind", type=StringType)
ClassDiagram_Facility_FacilityType.attributes={ClassDiagram_Facility_FacilityType_kind}

# ClassDiagram_Facility_FacilityService class attributes and methods
ClassDiagram_Facility_FacilityService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Facility_FacilityService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Facility_FacilityService.attributes={ClassDiagram_Facility_FacilityService_price, ClassDiagram_Facility_FacilityService_name}

# ClassDiagram_Booking_PurchasedService class attributes and methods
ClassDiagram_Booking_PurchasedService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Booking_PurchasedService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Booking_PurchasedService.attributes={ClassDiagram_Booking_PurchasedService_name, ClassDiagram_Booking_PurchasedService_price}

# ClassDiagram_Room_RoomAppliance class attributes and methods
ClassDiagram_Room_RoomAppliance_name: Property = Property(name="name", type=StringType)
ClassDiagram_Room_RoomAppliance.attributes={ClassDiagram_Room_RoomAppliance_name}

# ClassDiagram_IRoomManager class attributes and methods
ClassDiagram_IRoomManager_m_findRoom: Method = Method(name="findRoom", parameters={Parameter(name='ClassDiagram_roomNumber', type=StringType)})
ClassDiagram_IRoomManager_m_cleaningStatus: Method = Method(name="cleaningStatus", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_IRoomManager_m_maintenanceStatus: Method = Method(name="maintenanceStatus", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_IRoomManager_m_getRoomsToClean: Method = Method(name="getRoomsToClean", parameters={})
ClassDiagram_IRoomManager_m_getRoomsToMaintain: Method = Method(name="getRoomsToMaintain", parameters={})
ClassDiagram_IRoomManager.methods={ClassDiagram_IRoomManager_m_cleaningStatus, ClassDiagram_IRoomManager_m_findRoom, ClassDiagram_IRoomManager_m_getRoomsToMaintain, ClassDiagram_IRoomManager_m_maintenanceStatus, ClassDiagram_IRoomManager_m_getRoomsToClean}

# ClassDiagram_BookingManager class attributes and methods
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_guestSSN', type=StringType)})
ClassDiagram_BookingManager_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_BookingManager_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_BookingManager_m_assignKey: Method = Method(name="assignKey", parameters={Parameter(name='ClassDiagram_rooms', type=StringType), Parameter(name='ClassDiagram_expirationDate', type=StringType), Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='ClassDiagram_roomNr', type=StringType), Parameter(name='ClassDiagram_date', type=StringType)})
ClassDiagram_BookingManager.methods={ClassDiagram_BookingManager_m_findBooking, ClassDiagram_BookingManager_m_assignKey, ClassDiagram_BookingManager_m_checkOut, ClassDiagram_BookingManager_m_findBooking, ClassDiagram_BookingManager_m_checkIn}

# ClassDiagram_IGuestManager class attributes and methods
ClassDiagram_IGuestManager_m_createGuestRecord: Method = Method(name="createGuestRecord", parameters={Parameter(name='ClassDiagram_adress', type=StringType), Parameter(name='ClassDiagram_phoneNumber', type=StringType), Parameter(name='ClassDiagram_firstName', type=StringType), Parameter(name='ClassDiagram_lastName', type=StringType), Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_IGuestManager_m_removeGuestRecord: Method = Method(name="removeGuestRecord", parameters={Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_IGuestManager_m_findGuest: Method = Method(name="findGuest", parameters={Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_IGuestManager_m_findGuests: Method = Method(name="findGuests", parameters={Parameter(name='ClassDiagram_lastName', type=StringType), Parameter(name='ClassDiagram_firstName', type=StringType)})
ClassDiagram_IGuestManager_m_editGuestRecord: Method = Method(name="editGuestRecord", parameters={Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_IGuestManager.methods={ClassDiagram_IGuestManager_m_findGuests, ClassDiagram_IGuestManager_m_removeGuestRecord, ClassDiagram_IGuestManager_m_findGuest, ClassDiagram_IGuestManager_m_editGuestRecord, ClassDiagram_IGuestManager_m_createGuestRecord}

# ClassDiagram_IBillManager class attributes and methods
ClassDiagram_IBillManager_m_addPurchesedService: Method = Method(name="addPurchesedService", parameters={Parameter(name='ClassDiagram_amount', type=StringType), Parameter(name='ClassDiagram_item', type=StringType), Parameter(name='ClassDiagram_bill', type=StringType)})
ClassDiagram_IBillManager_m_findBill: Method = Method(name="findBill", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IBillManager_m_createReceipt: Method = Method(name="createReceipt", parameters={Parameter(name='ClassDiagram_bill', type=StringType)})
ClassDiagram_IBillManager_m_getAmount: Method = Method(name="getAmount", parameters={Parameter(name='ClassDiagram_bill', type=StringType)})
ClassDiagram_IBillManager_m_pay: Method = Method(name="pay", parameters={Parameter(name='ClassDiagram_amount', type=StringType), Parameter(name='ClassDiagram_bill', type=StringType)})
ClassDiagram_IBillManager.methods={ClassDiagram_IBillManager_m_pay, ClassDiagram_IBillManager_m_getAmount, ClassDiagram_IBillManager_m_findBill, ClassDiagram_IBillManager_m_addPurchesedService, ClassDiagram_IBillManager_m_createReceipt}

# ClassDiagram_IFacilityManager class attributes and methods
ClassDiagram_IFacilityManager_m_findBookedService: Method = Method(name="findBookedService", parameters={Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_facilityService', type=StringType)})
ClassDiagram_IFacilityManager_m_findBookedServices: Method = Method(name="findBookedServices", parameters={Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_IFacilityManager.methods={ClassDiagram_IFacilityManager_m_findBookedServices, ClassDiagram_IFacilityManager_m_findBookedService}

# ClassDiagram_IApplianceAdministration class attributes and methods
ClassDiagram_IApplianceAdministration_m_addAppliance: Method = Method(name="addAppliance", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_IApplianceAdministration_m_removeAppliance: Method = Method(name="removeAppliance", parameters={Parameter(name='ClassDiagram_appliance', type=StringType)})
ClassDiagram_IApplianceAdministration_m_addApplianceType: Method = Method(name="addApplianceType", parameters={Parameter(name='ClassDiagram_name', type=StringType)})
ClassDiagram_IApplianceAdministration_m_editApplianceService: Method = Method(name="editApplianceService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IApplianceAdministration_m_removeApplianceService: Method = Method(name="removeApplianceService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IApplianceAdministration_m_editApplianceType: Method = Method(name="editApplianceType", parameters={Parameter(name='ClassDiagram_applianceType', type=StringType)})
ClassDiagram_IApplianceAdministration_m_removeApplianceType: Method = Method(name="removeApplianceType", parameters={Parameter(name='ClassDiagram_applianceType', type=StringType)})
ClassDiagram_IApplianceAdministration_m_editAppliance: Method = Method(name="editAppliance", parameters={Parameter(name='ClassDiagram_appliance', type=StringType)})
ClassDiagram_IApplianceAdministration_m_addApplianceService: Method = Method(name="addApplianceService", parameters={Parameter(name='ClassDiagram_name', type=StringType), Parameter(name='ClassDiagram_price', type=StringType)})
ClassDiagram_IApplianceAdministration.methods={ClassDiagram_IApplianceAdministration_m_addApplianceType, ClassDiagram_IApplianceAdministration_m_removeAppliance, ClassDiagram_IApplianceAdministration_m_editApplianceType, ClassDiagram_IApplianceAdministration_m_addApplianceService, ClassDiagram_IApplianceAdministration_m_addAppliance, ClassDiagram_IApplianceAdministration_m_removeApplianceService, ClassDiagram_IApplianceAdministration_m_editAppliance, ClassDiagram_IApplianceAdministration_m_editApplianceService, ClassDiagram_IApplianceAdministration_m_removeApplianceType}

# ClassDiagram_IRoomAdministration class attributes and methods
ClassDiagram_IRoomAdministration_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='ClassDiagram_roomType', type=StringType), Parameter(name='ClassDiagram_roomNumber', type=StringType)})
ClassDiagram_IRoomAdministration_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_IRoomAdministration_m_editRoom: Method = Method(name="editRoom", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_IRoomAdministration_m_createRoomType: Method = Method(name="createRoomType", parameters={})
ClassDiagram_IRoomAdministration_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='ClassDiagram_roomType', type=StringType)})
ClassDiagram_IRoomAdministration_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='ClassDiagram_roomType', type=StringType)})
ClassDiagram_IRoomAdministration.methods={ClassDiagram_IRoomAdministration_m_addRoom, ClassDiagram_IRoomAdministration_m_editRoomType, ClassDiagram_IRoomAdministration_m_editRoom, ClassDiagram_IRoomAdministration_m_removeRoomType, ClassDiagram_IRoomAdministration_m_createRoomType, ClassDiagram_IRoomAdministration_m_removeRoom}

# ClassDiagram_IFacilityAdministration class attributes and methods
ClassDiagram_IFacilityAdministration_m_addFacility: Method = Method(name="addFacility", parameters={Parameter(name='ClassDiagram_name', type=StringType), Parameter(name='ClassDiagram_facilityType', type=StringType)})
ClassDiagram_IFacilityAdministration_m_editFacility: Method = Method(name="editFacility", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_IFacilityAdministration_m_removeFacility: Method = Method(name="removeFacility", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_IFacilityAdministration_m_addFacilityType: Method = Method(name="addFacilityType", parameters={Parameter(name='ClassDiagram_kind', type=StringType)})
ClassDiagram_IFacilityAdministration_m_editFacilityType: Method = Method(name="editFacilityType", parameters={Parameter(name='ClassDiagram_facilityType', type=StringType)})
ClassDiagram_IFacilityAdministration_m_removeFacilityType: Method = Method(name="removeFacilityType", parameters={Parameter(name='ClassDiagram_facilityType', type=StringType)})
ClassDiagram_IFacilityAdministration_m_addService: Method = Method(name="addService", parameters={Parameter(name='ClassDiagram_name', type=StringType), Parameter(name='ClassDiagram_facility', type=StringType), Parameter(name='ClassDiagram_price', type=StringType)})
ClassDiagram_IFacilityAdministration_m_editService: Method = Method(name="editService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IFacilityAdministration_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IFacilityAdministration.methods={ClassDiagram_IFacilityAdministration_m_addService, ClassDiagram_IFacilityAdministration_m_editFacility, ClassDiagram_IFacilityAdministration_m_removeFacilityType, ClassDiagram_IFacilityAdministration_m_editService, ClassDiagram_IFacilityAdministration_m_removeFacility, ClassDiagram_IFacilityAdministration_m_removeService, ClassDiagram_IFacilityAdministration_m_addFacility, ClassDiagram_IFacilityAdministration_m_editFacilityType, ClassDiagram_IFacilityAdministration_m_addFacilityType}

# ClassDiagram_IBooking class attributes and methods
ClassDiagram_IBooking_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='ClassDiagram_rooms', type=StringType), Parameter(name='ClassDiagram_end', type=StringType), Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_IBooking_m_findAvailableRooms: Method = Method(name="findAvailableRooms", parameters={Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_roomType', type=StringType), Parameter(name='ClassDiagram_end', type=StringType)})
ClassDiagram_IBooking_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IBooking_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IBooking_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='ClassDiagram_bookingNumber', type=StringType)})
ClassDiagram_IBooking_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_IBooking.methods={ClassDiagram_IBooking_m_createBooking, ClassDiagram_IBooking_m_cancelBooking, ClassDiagram_IBooking_m_findAvailableRooms, ClassDiagram_IBooking_m_editBooking, ClassDiagram_IBooking_m_getBookings, ClassDiagram_IBooking_m_findBooking}

# ClassDiagram_IServiceBooking class attributes and methods
ClassDiagram_IServiceBooking_m_bookFacilityService: Method = Method(name="bookFacilityService", parameters={Parameter(name='ClassDiagram_booking', type=StringType), Parameter(name='ClassDiagram_guest', type=StringType), Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_service', type=StringType), Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_IServiceBooking_m_findAvailableServices: Method = Method(name="findAvailableServices", parameters={Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_IServiceBooking_m_getBookedServices: Method = Method(name="getBookedServices", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IServiceBooking_m_findBookedService: Method = Method(name="findBookedService", parameters={Parameter(name='ClassDiagram_bookedServiceID', type=StringType)})
ClassDiagram_IServiceBooking_m_cancelBookedService: Method = Method(name="cancelBookedService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IServiceBooking.methods={ClassDiagram_IServiceBooking_m_findAvailableServices, ClassDiagram_IServiceBooking_m_getBookedServices, ClassDiagram_IServiceBooking_m_cancelBookedService, ClassDiagram_IServiceBooking_m_findBookedService, ClassDiagram_IServiceBooking_m_bookFacilityService}

# ClassDiagram_GuestBooking class attributes and methods

# IBooking class attributes and methods

# ClassDiagram_StaffBooking class attributes and methods

# BookingManager class attributes and methods

# ClassDiagram_IStaffAdministration class attributes and methods
ClassDiagram_IStaffAdministration_m_addStaff: Method = Method(name="addStaff", parameters={})
ClassDiagram_IStaffAdministration_m_editStaff: Method = Method(name="editStaff", parameters={})
ClassDiagram_IStaffAdministration_m_removeStaff: Method = Method(name="removeStaff", parameters={})
ClassDiagram_IStaffAdministration.methods={ClassDiagram_IStaffAdministration_m_editStaff, ClassDiagram_IStaffAdministration_m_removeStaff, ClassDiagram_IStaffAdministration_m_addStaff}

# ClassDiagram_IHotelAdministration class attributes and methods
ClassDiagram_IHotelAdministration_m_removeHotel: Method = Method(name="removeHotel", parameters={})
ClassDiagram_IHotelAdministration_m_addHotel: Method = Method(name="addHotel", parameters={})
ClassDiagram_IHotelAdministration_m_editHotel: Method = Method(name="editHotel", parameters={})
ClassDiagram_IHotelAdministration.methods={ClassDiagram_IHotelAdministration_m_removeHotel, ClassDiagram_IHotelAdministration_m_addHotel, ClassDiagram_IHotelAdministration_m_editHotel}

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

# Relationships
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
hasRoom5: BinaryAssociation = BinaryAssociation(
    name="hasRoom5",
    ends={
        Property(name="ClassDiagram_Hotel_Room", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel6", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(0, 9999))
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
hasPurchaseditem13: BinaryAssociation = BinaryAssociation(
    name="hasPurchaseditem13",
    ends={
        Property(name="ClassDiagram_Booking_PurchasedService", type=ClassDiagram_Booking_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Booking_Bill", type=ClassDiagram_Booking_PurchasedService, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ClassDiagram_GuestBooking_IBooking = Generalization(general=IBooking, specific=ClassDiagram_GuestBooking)
gen_ClassDiagram_StaffBooking_BookingManager = Generalization(general=BookingManager, specific=ClassDiagram_StaffBooking)
gen_ClassDiagram_HotelAdministration_IHotelAdministration = Generalization(general=IHotelAdministration, specific=ClassDiagram_HotelAdministration)
gen_ClassDiagram_StaffAdministration_IStaffAdministration = Generalization(general=IStaffAdministration, specific=ClassDiagram_StaffAdministration)
gen_ClassDiagram_RoomManager_IRoomManager = Generalization(general=IRoomManager, specific=ClassDiagram_RoomManager)
gen_ClassDiagram_RoomAdministration_IRoomAdministration = Generalization(general=IRoomAdministration, specific=ClassDiagram_RoomAdministration)
gen_ClassDiagram_ApplianceAdministration_IApplianceAdministration = Generalization(general=IApplianceAdministration, specific=ClassDiagram_ApplianceAdministration)
gen_ClassDiagram_FacilityAdministration_IFacilityAdministration = Generalization(general=IFacilityAdministration, specific=ClassDiagram_FacilityAdministration)
gen_ClassDiagram_ServiceBooking_IServiceBooking = Generalization(general=IServiceBooking, specific=ClassDiagram_ServiceBooking)
gen_ClassDiagram_FacilityManager_IFacilityManager = Generalization(general=IFacilityManager, specific=ClassDiagram_FacilityManager)
gen_ClassDiagram_GuestManager_IGuestManager = Generalization(general=IGuestManager, specific=ClassDiagram_GuestManager)
gen_ClassDiagram_BillManager_IBillManager = Generalization(general=IBillManager, specific=ClassDiagram_BillManager)

# Domain Model
domain_model = DomainModel(
    name="ClassDiagram",
    types={ClassDiagram_Company, ClassDiagram_Company_Hotel, ClassDiagram_Company_GuestRecord, ClassDiagram_Hotel_Booking, ClassDiagram_Hotel_Room, ClassDiagram_Hotel_Facility, ClassDiagram_Hotel_Staff, ClassDiagram_Booking_BookedService, ClassDiagram_Booking_Bill, ClassDiagram_Room_RoomType, ClassDiagram_Room_RoomKey, ClassDiagram_RoomAppliance_ApplianceType, ClassDiagram_ApplianceType_ApplianceService, ClassDiagram_Facility_FacilityType, ClassDiagram_Facility_FacilityService, ClassDiagram_Booking_PurchasedService, ClassDiagram_Room_RoomAppliance, ClassDiagram_IRoomManager, ClassDiagram_BookingManager, ClassDiagram_IGuestManager, ClassDiagram_IBillManager, ClassDiagram_IFacilityManager, ClassDiagram_IApplianceAdministration, ClassDiagram_IRoomAdministration, ClassDiagram_IFacilityAdministration, ClassDiagram_IBooking, ClassDiagram_IServiceBooking, ClassDiagram_GuestBooking, IBooking, ClassDiagram_StaffBooking, BookingManager, ClassDiagram_IStaffAdministration, ClassDiagram_IHotelAdministration, ClassDiagram_HotelAdministration, IHotelAdministration, ClassDiagram_StaffAdministration, IStaffAdministration, ClassDiagram_RoomManager, IRoomManager, ClassDiagram_RoomAdministration, IRoomAdministration, ClassDiagram_ApplianceAdministration, IApplianceAdministration, ClassDiagram_FacilityAdministration, IFacilityAdministration, ClassDiagram_ServiceBooking, IServiceBooking, ClassDiagram_FacilityManager, IFacilityManager, ClassDiagram_GuestManager, IGuestManager, ClassDiagram_BillManager, IBillManager, StaffType},
    associations={hasHotel0, hasGuest1, hasBooking3, hasRoom5, hasFacility7, employee9, bookedservice11, roomAppliances14, hasType16, hasKey18, hasApplianceType20, hasAppliance22, hasType25, hasPurchaseditem13},
    generalizations={gen_ClassDiagram_GuestBooking_IBooking, gen_ClassDiagram_StaffBooking_BookingManager, gen_ClassDiagram_HotelAdministration_IHotelAdministration, gen_ClassDiagram_StaffAdministration_IStaffAdministration, gen_ClassDiagram_RoomManager_IRoomManager, gen_ClassDiagram_RoomAdministration_IRoomAdministration, gen_ClassDiagram_ApplianceAdministration_IApplianceAdministration, gen_ClassDiagram_FacilityAdministration_IFacilityAdministration, gen_ClassDiagram_ServiceBooking_IServiceBooking, gen_ClassDiagram_FacilityManager_IFacilityManager, gen_ClassDiagram_GuestManager_IGuestManager, gen_ClassDiagram_BillManager_IBillManager},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)