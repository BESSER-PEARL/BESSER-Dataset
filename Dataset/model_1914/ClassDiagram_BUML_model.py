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
ClassDiagram_Hotel_Room = Class(name="ClassDiagram_Hotel_Room")
ClassDiagram_Hotel_Staff = Class(name="ClassDiagram_Hotel_Staff")
ClassDiagram_Hotel_Booking = Class(name="ClassDiagram_Hotel_Booking")
ClassDiagram_Room_RoomType = Class(name="ClassDiagram_Room_RoomType")
ClassDiagram_Room_RoomKey = Class(name="ClassDiagram_Room_RoomKey")
ClassDiagram_Booking_BookedService = Class(name="ClassDiagram_Booking_BookedService")
ClassDiagram_Booking_Bill = Class(name="ClassDiagram_Booking_Bill")
ClassDiagram_Facility_FacilityService = Class(name="ClassDiagram_Facility_FacilityService")
ClassDiagram_RoomAppliance_ApplianceType = Class(name="ClassDiagram_RoomAppliance_ApplianceType")
ClassDiagram_ApplianceType_ApplianceService = Class(name="ClassDiagram_ApplianceType_ApplianceService")
ClassDiagram_Room_RoomAppliance = Class(name="ClassDiagram_Room_RoomAppliance")
ClassDiagram_Hotel_Facility = Class(name="ClassDiagram_Hotel_Facility")
ClassDiagram_Facility_FacilityType = Class(name="ClassDiagram_Facility_FacilityType")
ClassDiagram_IServiceBooking = Class(name="ClassDiagram_IServiceBooking", is_abstract=True)
ClassDiagram_BookingManager = Class(name="ClassDiagram_BookingManager")
ClassDiagram_Booking_PurchasedService = Class(name="ClassDiagram_Booking_PurchasedService")
ClassDiagram_RoomManager = Class(name="ClassDiagram_RoomManager")
ClassDiagram_GuestManager = Class(name="ClassDiagram_GuestManager")
ClassDiagram_BillManager = Class(name="ClassDiagram_BillManager")
ClassDiagram_RoomAdministration = Class(name="ClassDiagram_RoomAdministration")
ClassDiagram_ApplianceAdministration = Class(name="ClassDiagram_ApplianceAdministration")
ClassDiagram_StaffAdministration = Class(name="ClassDiagram_StaffAdministration")
ClassDiagram_FacilityAdministration = Class(name="ClassDiagram_FacilityAdministration")
ClassDiagram_HotelAdministration = Class(name="ClassDiagram_HotelAdministration")
ClassDiagram_FacilityManager = Class(name="ClassDiagram_FacilityManager")

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
ClassDiagram_Company_GuestRecord_paymentInformation: Property = Property(name="paymentInformation", type=StringType)
ClassDiagram_Company_GuestRecord.attributes={ClassDiagram_Company_GuestRecord_ssn, ClassDiagram_Company_GuestRecord_name, ClassDiagram_Company_GuestRecord_adress, ClassDiagram_Company_GuestRecord_paymentInformation, ClassDiagram_Company_GuestRecord_phoneNumber}

# ClassDiagram_Hotel_Room class attributes and methods
ClassDiagram_Hotel_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
ClassDiagram_Hotel_Room_cleaningStatus: Property = Property(name="cleaningStatus", type=BooleanType)
ClassDiagram_Hotel_Room_maintenceStatus: Property = Property(name="maintenceStatus", type=BooleanType)
ClassDiagram_Hotel_Room.attributes={ClassDiagram_Hotel_Room_maintenceStatus, ClassDiagram_Hotel_Room_cleaningStatus, ClassDiagram_Hotel_Room_roomNumber}

# ClassDiagram_Hotel_Staff class attributes and methods
ClassDiagram_Hotel_Staff_ssn: Property = Property(name="ssn", type=StringType)
ClassDiagram_Hotel_Staff_firstName: Property = Property(name="firstName", type=StringType)
ClassDiagram_Hotel_Staff_lastName: Property = Property(name="lastName", type=StringType)
ClassDiagram_Hotel_Staff_hasWorkTitel: Property = Property(name="hasWorkTitel", type=StringType)
ClassDiagram_Hotel_Staff.attributes={ClassDiagram_Hotel_Staff_lastName, ClassDiagram_Hotel_Staff_firstName, ClassDiagram_Hotel_Staff_hasWorkTitel, ClassDiagram_Hotel_Staff_ssn}

# ClassDiagram_Hotel_Booking class attributes and methods
ClassDiagram_Hotel_Booking_startDate: Property = Property(name="startDate", type=DateType)
ClassDiagram_Hotel_Booking_endDate: Property = Property(name="endDate", type=DateType)
ClassDiagram_Hotel_Booking_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Hotel_Booking_checkedIn: Property = Property(name="checkedIn", type=BooleanType)
ClassDiagram_Hotel_Booking_bookingID: Property = Property(name="bookingID", type=IntegerType)
ClassDiagram_Hotel_Booking.attributes={ClassDiagram_Hotel_Booking_endDate, ClassDiagram_Hotel_Booking_startDate, ClassDiagram_Hotel_Booking_bookingID, ClassDiagram_Hotel_Booking_price, ClassDiagram_Hotel_Booking_checkedIn}

# ClassDiagram_Room_RoomType class attributes and methods
ClassDiagram_Room_RoomType_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Room_RoomType_maxNumberOfGuests: Property = Property(name="maxNumberOfGuests", type=IntegerType)
ClassDiagram_Room_RoomType_area: Property = Property(name="area", type=FloatType)
ClassDiagram_Room_RoomType_name: Property = Property(name="name", type=StringType)
ClassDiagram_Room_RoomType.attributes={ClassDiagram_Room_RoomType_area, ClassDiagram_Room_RoomType_price, ClassDiagram_Room_RoomType_name, ClassDiagram_Room_RoomType_maxNumberOfGuests}

# ClassDiagram_Room_RoomKey class attributes and methods
ClassDiagram_Room_RoomKey_expirationDate: Property = Property(name="expirationDate", type=DateType)
ClassDiagram_Room_RoomKey.attributes={ClassDiagram_Room_RoomKey_expirationDate}

# ClassDiagram_Booking_BookedService class attributes and methods
ClassDiagram_Booking_BookedService_date: Property = Property(name="date", type=DateType)
ClassDiagram_Booking_BookedService.attributes={ClassDiagram_Booking_BookedService_date}

# ClassDiagram_Booking_Bill class attributes and methods
ClassDiagram_Booking_Bill_paidAmount: Property = Property(name="paidAmount", type=FloatType)
ClassDiagram_Booking_Bill.attributes={ClassDiagram_Booking_Bill_paidAmount}

# ClassDiagram_Facility_FacilityService class attributes and methods
ClassDiagram_Facility_FacilityService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Facility_FacilityService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Facility_FacilityService.attributes={ClassDiagram_Facility_FacilityService_price, ClassDiagram_Facility_FacilityService_name}

# ClassDiagram_RoomAppliance_ApplianceType class attributes and methods
ClassDiagram_RoomAppliance_ApplianceType_name: Property = Property(name="name", type=StringType)
ClassDiagram_RoomAppliance_ApplianceType.attributes={ClassDiagram_RoomAppliance_ApplianceType_name}

# ClassDiagram_ApplianceType_ApplianceService class attributes and methods
ClassDiagram_ApplianceType_ApplianceService_name: Property = Property(name="name", type=StringType)
ClassDiagram_ApplianceType_ApplianceService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_ApplianceType_ApplianceService.attributes={ClassDiagram_ApplianceType_ApplianceService_name, ClassDiagram_ApplianceType_ApplianceService_price}

# ClassDiagram_Room_RoomAppliance class attributes and methods
ClassDiagram_Room_RoomAppliance_name: Property = Property(name="name", type=StringType)
ClassDiagram_Room_RoomAppliance.attributes={ClassDiagram_Room_RoomAppliance_name}

# ClassDiagram_Hotel_Facility class attributes and methods
ClassDiagram_Hotel_Facility_name: Property = Property(name="name", type=StringType)
ClassDiagram_Hotel_Facility.attributes={ClassDiagram_Hotel_Facility_name}

# ClassDiagram_Facility_FacilityType class attributes and methods
ClassDiagram_Facility_FacilityType_name: Property = Property(name="name", type=StringType)
ClassDiagram_Facility_FacilityType.attributes={ClassDiagram_Facility_FacilityType_name}

# ClassDiagram_IServiceBooking class attributes and methods
ClassDiagram_IServiceBooking_m_bookFacilityService: Method = Method(name="bookFacilityService", parameters={Parameter(name='ClassDiagram_facility', type=StringType), Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_guest', type=StringType), Parameter(name='ClassDiagram_service', type=StringType), Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IServiceBooking_m_findAvailableServices: Method = Method(name="findAvailableServices", parameters={Parameter(name='ClassDiagram_facility', type=StringType), Parameter(name='ClassDiagram_date', type=StringType)})
ClassDiagram_IServiceBooking_m_getBookedServices: Method = Method(name="getBookedServices", parameters={Parameter(name='ClassDiagram_booking', type=StringType)})
ClassDiagram_IServiceBooking_m_findBookedService: Method = Method(name="findBookedService", parameters={Parameter(name='ClassDiagram_bookedServiceID', type=StringType)})
ClassDiagram_IServiceBooking_m_cancelBookedService: Method = Method(name="cancelBookedService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_IServiceBooking.methods={ClassDiagram_IServiceBooking_m_cancelBookedService, ClassDiagram_IServiceBooking_m_getBookedServices, ClassDiagram_IServiceBooking_m_findBookedService, ClassDiagram_IServiceBooking_m_bookFacilityService, ClassDiagram_IServiceBooking_m_findAvailableServices}

# ClassDiagram_BookingManager class attributes and methods
ClassDiagram_BookingManager_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_numberOfPeople', type=StringType), Parameter(name='ClassDiagram_rooms', type=StringType), Parameter(name='ClassDiagram_guest', type=StringType), Parameter(name='ClassDiagram_end', type=StringType)})
ClassDiagram_BookingManager_m_findAvailableRooms: Method = Method(name="findAvailableRooms", parameters={Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_roomType', type=StringType), Parameter(name='ClassDiagram_end', type=StringType), Parameter(name='ClassDiagram__people', type=StringType)})
ClassDiagram_BookingManager_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='ClassDiagram_date', type=StringType), Parameter(name='ClassDiagram_roomNr', type=StringType)})
ClassDiagram_BookingManager_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='ClassDiagram_bookingId', type=StringType)})
ClassDiagram_BookingManager_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='ClassDiagram_bookingId', type=StringType)})
ClassDiagram_BookingManager_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_BookingManager_m_initBooking: Method = Method(name="initBooking", parameters={})
ClassDiagram_BookingManager_m_findAvailableRoomTypes: Method = Method(name="findAvailableRoomTypes", parameters={Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_end', type=StringType)})
ClassDiagram_BookingManager_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BookingManager_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BookingManager_m_assignKey: Method = Method(name="assignKey", parameters={Parameter(name='ClassDiagram_booking', type=StringType), Parameter(name='ClassDiagram_room', type=StringType), Parameter(name='ClassDiagram_expirationDate', type=StringType)})
ClassDiagram_BookingManager.methods={ClassDiagram_BookingManager_m_editBooking, ClassDiagram_BookingManager_m_assignKey, ClassDiagram_BookingManager_m_cancelBooking, ClassDiagram_BookingManager_m_findBooking, ClassDiagram_BookingManager_m_checkOut, ClassDiagram_BookingManager_m_initBooking, ClassDiagram_BookingManager_m_getBookings, ClassDiagram_BookingManager_m_findAvailableRoomTypes, ClassDiagram_BookingManager_m_createBooking, ClassDiagram_BookingManager_m_findAvailableRooms, ClassDiagram_BookingManager_m_checkIn, ClassDiagram_BookingManager_m_findBooking}

# ClassDiagram_Booking_PurchasedService class attributes and methods
ClassDiagram_Booking_PurchasedService_name: Property = Property(name="name", type=StringType)
ClassDiagram_Booking_PurchasedService_price: Property = Property(name="price", type=FloatType)
ClassDiagram_Booking_PurchasedService.attributes={ClassDiagram_Booking_PurchasedService_price, ClassDiagram_Booking_PurchasedService_name}

# ClassDiagram_RoomManager class attributes and methods
ClassDiagram_RoomManager_m_findRoom: Method = Method(name="findRoom", parameters={Parameter(name='ClassDiagram_roomNumber', type=StringType)})
ClassDiagram_RoomManager_m_cleaningStatus: Method = Method(name="cleaningStatus", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_RoomManager_m_maintenanceStatus: Method = Method(name="maintenanceStatus", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_RoomManager_m_getRoomsToClean: Method = Method(name="getRoomsToClean", parameters={})
ClassDiagram_RoomManager_m_getRoomsToMaintain: Method = Method(name="getRoomsToMaintain", parameters={})
ClassDiagram_RoomManager_m_roomExists: Method = Method(name="roomExists", parameters={Parameter(name='ClassDiagram_rooms', type=StringType), Parameter(name='ClassDiagram_roomNumber', type=StringType)})
ClassDiagram_RoomManager.methods={ClassDiagram_RoomManager_m_cleaningStatus, ClassDiagram_RoomManager_m_roomExists, ClassDiagram_RoomManager_m_maintenanceStatus, ClassDiagram_RoomManager_m_findRoom, ClassDiagram_RoomManager_m_getRoomsToMaintain, ClassDiagram_RoomManager_m_getRoomsToClean}

# ClassDiagram_GuestManager class attributes and methods
ClassDiagram_GuestManager_m_createGuestRecord: Method = Method(name="createGuestRecord", parameters={Parameter(name='ClassDiagram_phoneNumber', type=StringType), Parameter(name='ClassDiagram_adress', type=StringType), Parameter(name='ClassDiagram_paymentInformation', type=StringType), Parameter(name='ClassDiagram_ssn', type=StringType), Parameter(name='ClassDiagram_lastName', type=StringType), Parameter(name='ClassDiagram_firstName', type=StringType)})
ClassDiagram_GuestManager_m_editGuestRecord: Method = Method(name="editGuestRecord", parameters={Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_GuestManager_m_removeGuestRecord: Method = Method(name="removeGuestRecord", parameters={Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_GuestManager_m_findGuestRecord: Method = Method(name="findGuestRecord", parameters={Parameter(name='ClassDiagram_ssn', type=StringType)})
ClassDiagram_GuestManager_m_findGuestRecords: Method = Method(name="findGuestRecords", parameters={Parameter(name='ClassDiagram_firstName', type=StringType), Parameter(name='ClassDiagram_lastName', type=StringType)})
ClassDiagram_GuestManager.methods={ClassDiagram_GuestManager_m_editGuestRecord, ClassDiagram_GuestManager_m_findGuestRecord, ClassDiagram_GuestManager_m_findGuestRecords, ClassDiagram_GuestManager_m_removeGuestRecord, ClassDiagram_GuestManager_m_createGuestRecord}

# ClassDiagram_BillManager class attributes and methods
ClassDiagram_BillManager_m_addPurchasedService: Method = Method(name="addPurchasedService", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType), Parameter(name='ClassDiagram_amount', type=StringType), Parameter(name='ClassDiagram_item', type=StringType)})
ClassDiagram_BillManager_m_findBill: Method = Method(name="findBill", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BillManager_m_createReceipt: Method = Method(name="createReceipt", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BillManager_m_getAmount: Method = Method(name="getAmount", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BillManager_m_pay: Method = Method(name="pay", parameters={Parameter(name='ClassDiagram_bookingID', type=StringType)})
ClassDiagram_BillManager.methods={ClassDiagram_BillManager_m_createReceipt, ClassDiagram_BillManager_m_pay, ClassDiagram_BillManager_m_findBill, ClassDiagram_BillManager_m_addPurchasedService, ClassDiagram_BillManager_m_getAmount}

# ClassDiagram_RoomAdministration class attributes and methods
ClassDiagram_RoomAdministration_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='ClassDiagram_roomNumber', type=StringType), Parameter(name='ClassDiagram_roomType', type=StringType), Parameter(name='ClassDiagram_appliances', type=StringType)})
ClassDiagram_RoomAdministration_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_RoomAdministration_m_editRoom: Method = Method(name="editRoom", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_RoomAdministration_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='ClassDiagram_roomType', type=StringType)})
ClassDiagram_RoomAdministration_m_createRoomType: Method = Method(name="createRoomType", parameters={Parameter(name='ClassDiagram_maxNumberOfGuests', type=StringType), Parameter(name='ClassDiagram_price', type=StringType), Parameter(name='ClassDiagram_applianceTypes', type=StringType), Parameter(name='ClassDiagram_area', type=StringType)})
ClassDiagram_RoomAdministration_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='ClassDiagram_roomType', type=StringType)})
ClassDiagram_RoomAdministration.methods={ClassDiagram_RoomAdministration_m_createRoomType, ClassDiagram_RoomAdministration_m_addRoom, ClassDiagram_RoomAdministration_m_removeRoomType, ClassDiagram_RoomAdministration_m_removeRoom, ClassDiagram_RoomAdministration_m_editRoom, ClassDiagram_RoomAdministration_m_editRoomType}

# ClassDiagram_ApplianceAdministration class attributes and methods
ClassDiagram_ApplianceAdministration_m_addAppliance: Method = Method(name="addAppliance", parameters={Parameter(name='ClassDiagram_room', type=StringType)})
ClassDiagram_ApplianceAdministration_m_editApplianceService: Method = Method(name="editApplianceService", parameters={Parameter(name='ClassDiagram_applianceService', type=StringType)})
ClassDiagram_ApplianceAdministration_m_removeApplianceServer: Method = Method(name="removeApplianceServer", parameters={Parameter(name='ClassDiagram_applianceService', type=StringType)})
ClassDiagram_ApplianceAdministration_m_removeAppliance: Method = Method(name="removeAppliance", parameters={Parameter(name='ClassDiagram_appliance', type=StringType)})
ClassDiagram_ApplianceAdministration_m_addApplianceType: Method = Method(name="addApplianceType", parameters={Parameter(name='ClassDiagram_name', type=StringType)})
ClassDiagram_ApplianceAdministration_m_editApplianceType: Method = Method(name="editApplianceType", parameters={Parameter(name='ClassDiagram_applianceType', type=StringType)})
ClassDiagram_ApplianceAdministration_m_removeApplianceType: Method = Method(name="removeApplianceType", parameters={Parameter(name='ClassDiagram_applianceType', type=StringType)})
ClassDiagram_ApplianceAdministration_m_editAppliance: Method = Method(name="editAppliance", parameters={Parameter(name='ClassDiagram_appliance', type=StringType)})
ClassDiagram_ApplianceAdministration_m_addApplianceService: Method = Method(name="addApplianceService", parameters={Parameter(name='ClassDiagram_applianceService', type=StringType)})
ClassDiagram_ApplianceAdministration.methods={ClassDiagram_ApplianceAdministration_m_editApplianceType, ClassDiagram_ApplianceAdministration_m_addAppliance, ClassDiagram_ApplianceAdministration_m_addApplianceService, ClassDiagram_ApplianceAdministration_m_removeAppliance, ClassDiagram_ApplianceAdministration_m_removeApplianceType, ClassDiagram_ApplianceAdministration_m_editApplianceService, ClassDiagram_ApplianceAdministration_m_removeApplianceServer, ClassDiagram_ApplianceAdministration_m_editAppliance, ClassDiagram_ApplianceAdministration_m_addApplianceType}

# ClassDiagram_StaffAdministration class attributes and methods
ClassDiagram_StaffAdministration_m_editStaff: Method = Method(name="editStaff", parameters={Parameter(name='ClassDiagram_staff', type=StringType)})
ClassDiagram_StaffAdministration_m_removeStaff: Method = Method(name="removeStaff", parameters={Parameter(name='ClassDiagram_staff', type=StringType)})
ClassDiagram_StaffAdministration_m_addStaff: Method = Method(name="addStaff", parameters={Parameter(name='ClassDiagram_lastName', type=StringType), Parameter(name='ClassDiagram_firstName', type=StringType), Parameter(name='ClassDiagram_ssn', type=StringType), Parameter(name='ClassDiagram_workTitel', type=StringType)})
ClassDiagram_StaffAdministration.methods={ClassDiagram_StaffAdministration_m_editStaff, ClassDiagram_StaffAdministration_m_removeStaff, ClassDiagram_StaffAdministration_m_addStaff}

# ClassDiagram_FacilityAdministration class attributes and methods
ClassDiagram_FacilityAdministration_m_addFacility: Method = Method(name="addFacility", parameters={Parameter(name='ClassDiagram_name', type=StringType), Parameter(name='ClassDiagram_facilityType', type=StringType)})
ClassDiagram_FacilityAdministration_m_editFacility: Method = Method(name="editFacility", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityAdministration_m_addFacilityType: Method = Method(name="addFacilityType", parameters={Parameter(name='ClassDiagram_name', type=StringType)})
ClassDiagram_FacilityAdministration_m_editFacilityType: Method = Method(name="editFacilityType", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityAdministration_m_removeFacility: Method = Method(name="removeFacility", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityAdministration_m_removeFacilityType: Method = Method(name="removeFacilityType", parameters={Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityAdministration_m_addService: Method = Method(name="addService", parameters={Parameter(name='ClassDiagram_price', type=StringType), Parameter(name='ClassDiagram_name', type=StringType), Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityAdministration_m_editService: Method = Method(name="editService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_FacilityAdministration_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='ClassDiagram_service', type=StringType)})
ClassDiagram_FacilityAdministration.methods={ClassDiagram_FacilityAdministration_m_addService, ClassDiagram_FacilityAdministration_m_addFacility, ClassDiagram_FacilityAdministration_m_removeFacilityType, ClassDiagram_FacilityAdministration_m_editFacilityType, ClassDiagram_FacilityAdministration_m_removeService, ClassDiagram_FacilityAdministration_m_removeFacility, ClassDiagram_FacilityAdministration_m_editFacility, ClassDiagram_FacilityAdministration_m_editService, ClassDiagram_FacilityAdministration_m_addFacilityType}

# ClassDiagram_HotelAdministration class attributes and methods
ClassDiagram_HotelAdministration_m_addHotel: Method = Method(name="addHotel", parameters={Parameter(name='ClassDiagram_name', type=StringType)})
ClassDiagram_HotelAdministration_m_editHotel: Method = Method(name="editHotel", parameters={Parameter(name='ClassDiagram_hotel', type=StringType)})
ClassDiagram_HotelAdministration_m_removeHotel: Method = Method(name="removeHotel", parameters={Parameter(name='ClassDiagram_hotel', type=StringType)})
ClassDiagram_HotelAdministration.methods={ClassDiagram_HotelAdministration_m_editHotel, ClassDiagram_HotelAdministration_m_addHotel, ClassDiagram_HotelAdministration_m_removeHotel}

# ClassDiagram_FacilityManager class attributes and methods
ClassDiagram_FacilityManager_m_findServices: Method = Method(name="findServices", parameters={Parameter(name='ClassDiagram_date', type=StringType)})
ClassDiagram_FacilityManager_m_findBookedServices: Method = Method(name="findBookedServices", parameters={Parameter(name='ClassDiagram_guest', type=StringType)})
ClassDiagram_FacilityManager_m_findServices: Method = Method(name="findServices", parameters={Parameter(name='ClassDiagram_end', type=StringType), Parameter(name='ClassDiagram_start', type=StringType), Parameter(name='ClassDiagram_facility', type=StringType)})
ClassDiagram_FacilityManager.methods={ClassDiagram_FacilityManager_m_findServices, ClassDiagram_FacilityManager_m_findBookedServices, ClassDiagram_FacilityManager_m_findServices}

# Relationships
recordsOf1: BinaryAssociation = BinaryAssociation(
    name="recordsOf1",
    ends={
        Property(name="ClassDiagram_Company_GuestRecord", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company2", type=ClassDiagram_Company_GuestRecord, multiplicity=Multiplicity(0, 9999))
    }
)
listOfRooms3: BinaryAssociation = BinaryAssociation(
    name="listOfRooms3",
    ends={
        Property(name="ClassDiagram_Hotel_Room", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel4", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(0, 9999))
    }
)
employees5: BinaryAssociation = BinaryAssociation(
    name="employees5",
    ends={
        Property(name="ClassDiagram_Hotel_Staff", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel6", type=ClassDiagram_Hotel_Staff, multiplicity=Multiplicity(0, 9999))
    }
)
listOfBookings7: BinaryAssociation = BinaryAssociation(
    name="listOfBookings7",
    ends={
        Property(name="ClassDiagram_Hotel_Booking", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel8", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
listOfRoomTypes9: BinaryAssociation = BinaryAssociation(
    name="listOfRoomTypes9",
    ends={
        Property(name="ClassDiagram_Room_RoomType", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company_Hotel10", type=ClassDiagram_Room_RoomType, multiplicity=Multiplicity(0, 9999))
    }
)
accessedBy11: BinaryAssociation = BinaryAssociation(
    name="accessedBy11",
    ends={
        Property(name="ClassDiagram_Room_RoomKey", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Room12", type=ClassDiagram_Room_RoomKey, multiplicity=Multiplicity(0, 9999))
    }
)
roomType13: BinaryAssociation = BinaryAssociation(
    name="roomType13",
    ends={
        Property(name="ClassDiagram_Room_RoomType15", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Room14", type=ClassDiagram_Room_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
applianceType18: BinaryAssociation = BinaryAssociation(
    name="applianceType18",
    ends={
        Property(name="ClassDiagram_RoomAppliance_ApplianceType19", type=ClassDiagram_Room_RoomAppliance, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Room_RoomAppliance", type=ClassDiagram_RoomAppliance_ApplianceType, multiplicity=Multiplicity(1, 1))
    }
)
owns0: BinaryAssociation = BinaryAssociation(
    name="owns0",
    ends={
        Property(name="ClassDiagram_Company_Hotel", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Company", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 9999))
    }
)
includes20: BinaryAssociation = BinaryAssociation(
    name="includes20",
    ends={
        Property(name="ClassDiagram_Booking_BookedService", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Booking21", type=ClassDiagram_Booking_BookedService, multiplicity=Multiplicity(0, 9999))
    }
)
rooms22: BinaryAssociation = BinaryAssociation(
    name="rooms22",
    ends={
        Property(name="ClassDiagram_Hotel_Room24", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Booking23", type=ClassDiagram_Hotel_Room, multiplicity=Multiplicity(1, 9999))
    }
)
responsibleGuest25: BinaryAssociation = BinaryAssociation(
    name="responsibleGuest25",
    ends={
        Property(name="ClassDiagram_Company_GuestRecord27", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Booking26", type=ClassDiagram_Company_GuestRecord, multiplicity=Multiplicity(1, 1))
    }
)
bill28: BinaryAssociation = BinaryAssociation(
    name="bill28",
    ends={
        Property(name="ClassDiagram_Booking_Bill", type=ClassDiagram_Hotel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Booking29", type=ClassDiagram_Booking_Bill, multiplicity=Multiplicity(1, 1))
    }
)
facilityService30: BinaryAssociation = BinaryAssociation(
    name="facilityService30",
    ends={
        Property(name="ClassDiagram_Facility_FacilityService", type=ClassDiagram_Booking_BookedService, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Booking_BookedService31", type=ClassDiagram_Facility_FacilityService, multiplicity=Multiplicity(1, 1))
    }
)
applianceType16: BinaryAssociation = BinaryAssociation(
    name="applianceType16",
    ends={
        Property(name="ClassDiagram_RoomAppliance_ApplianceType", type=ClassDiagram_Room_RoomType, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Room_RoomType17", type=ClassDiagram_RoomAppliance_ApplianceType, multiplicity=Multiplicity(0, 9999))
    }
)
facilityType34: BinaryAssociation = BinaryAssociation(
    name="facilityType34",
    ends={
        Property(name="ClassDiagram_Facility_FacilityType", type=ClassDiagram_Hotel_Facility, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Hotel_Facility", type=ClassDiagram_Facility_FacilityType, multiplicity=Multiplicity(1, 1))
    }
)
contains32: BinaryAssociation = BinaryAssociation(
    name="contains32",
    ends={
        Property(name="ClassDiagram_Booking_PurchasedService", type=ClassDiagram_Booking_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Booking_Bill33", type=ClassDiagram_Booking_PurchasedService, multiplicity=Multiplicity(0, 9999))
    }
)
hotel35: BinaryAssociation = BinaryAssociation(
    name="hotel35",
    ends={
        Property(name="ClassDiagram_Company_Hotel36", type=ClassDiagram_BookingManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_BookingManager", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
roomManager37: BinaryAssociation = BinaryAssociation(
    name="roomManager37",
    ends={
        Property(name="ClassDiagram_RoomManager", type=ClassDiagram_BookingManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_BookingManager38", type=ClassDiagram_RoomManager, multiplicity=Multiplicity(1, 1))
    }
)
guestManager39: BinaryAssociation = BinaryAssociation(
    name="guestManager39",
    ends={
        Property(name="ClassDiagram_GuestManager", type=ClassDiagram_BookingManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_BookingManager40", type=ClassDiagram_GuestManager, multiplicity=Multiplicity(1, 1))
    }
)
billManager41: BinaryAssociation = BinaryAssociation(
    name="billManager41",
    ends={
        Property(name="ClassDiagram_BillManager", type=ClassDiagram_BookingManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_BookingManager42", type=ClassDiagram_BillManager, multiplicity=Multiplicity(1, 1))
    }
)
company46: BinaryAssociation = BinaryAssociation(
    name="company46",
    ends={
        Property(name="ClassDiagram_Company48", type=ClassDiagram_GuestManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_GuestManager47", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1))
    }
)
hotel43: BinaryAssociation = BinaryAssociation(
    name="hotel43",
    ends={
        Property(name="ClassDiagram_Company_Hotel45", type=ClassDiagram_RoomManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_RoomManager44", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel52: BinaryAssociation = BinaryAssociation(
    name="hotel52",
    ends={
        Property(name="ClassDiagram_Company_Hotel53", type=ClassDiagram_StaffAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_StaffAdministration", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel54: BinaryAssociation = BinaryAssociation(
    name="hotel54",
    ends={
        Property(name="ClassDiagram_Company_Hotel55", type=ClassDiagram_RoomAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_RoomAdministration", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel49: BinaryAssociation = BinaryAssociation(
    name="hotel49",
    ends={
        Property(name="ClassDiagram_Company_Hotel51", type=ClassDiagram_BillManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_BillManager50", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel56: BinaryAssociation = BinaryAssociation(
    name="hotel56",
    ends={
        Property(name="ClassDiagram_Company_Hotel57", type=ClassDiagram_ApplianceAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_ApplianceAdministration", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel58: BinaryAssociation = BinaryAssociation(
    name="hotel58",
    ends={
        Property(name="ClassDiagram_Company_Hotel59", type=ClassDiagram_FacilityAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_FacilityAdministration", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
hotel62: BinaryAssociation = BinaryAssociation(
    name="hotel62",
    ends={
        Property(name="ClassDiagram_Company_Hotel63", type=ClassDiagram_FacilityManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_FacilityManager", type=ClassDiagram_Company_Hotel, multiplicity=Multiplicity(1, 1))
    }
)
company60: BinaryAssociation = BinaryAssociation(
    name="company60",
    ends={
        Property(name="ClassDiagram_Company61", type=ClassDiagram_HotelAdministration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_HotelAdministration", type=ClassDiagram_Company, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ClassDiagram",
    types={ClassDiagram_Company, ClassDiagram_Company_Hotel, ClassDiagram_Company_GuestRecord, ClassDiagram_Hotel_Room, ClassDiagram_Hotel_Staff, ClassDiagram_Hotel_Booking, ClassDiagram_Room_RoomType, ClassDiagram_Room_RoomKey, ClassDiagram_Booking_BookedService, ClassDiagram_Booking_Bill, ClassDiagram_Facility_FacilityService, ClassDiagram_RoomAppliance_ApplianceType, ClassDiagram_ApplianceType_ApplianceService, ClassDiagram_Room_RoomAppliance, ClassDiagram_Hotel_Facility, ClassDiagram_Facility_FacilityType, ClassDiagram_IServiceBooking, ClassDiagram_BookingManager, ClassDiagram_Booking_PurchasedService, ClassDiagram_RoomManager, ClassDiagram_GuestManager, ClassDiagram_BillManager, ClassDiagram_RoomAdministration, ClassDiagram_ApplianceAdministration, ClassDiagram_StaffAdministration, ClassDiagram_FacilityAdministration, ClassDiagram_HotelAdministration, ClassDiagram_FacilityManager, StaffType},
    associations={recordsOf1, listOfRooms3, employees5, listOfBookings7, listOfRoomTypes9, accessedBy11, roomType13, applianceType18, owns0, includes20, rooms22, responsibleGuest25, bill28, facilityService30, applianceType16, facilityType34, contains32, hotel35, roomManager37, guestManager39, billManager41, company46, hotel43, hotel52, hotel54, hotel49, hotel56, hotel58, hotel62, company60},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)