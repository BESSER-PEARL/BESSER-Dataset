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
CodePack_IBookings = Class(name="CodePack_IBookings", is_abstract=True)
CodePack_IUserAccount = Class(name="CodePack_IUserAccount", is_abstract=True)
IBookings = Class(name="IBookings")
CodePack_IStaffAdmin = Class(name="CodePack_IStaffAdmin", is_abstract=True)
CodePack_IManagement = Class(name="CodePack_IManagement", is_abstract=True)
IStaffAdmin = Class(name="IStaffAdmin")
IStaffAuthentication = Class(name="IStaffAuthentication")
CodePack_IStaffAuthentication = Class(name="CodePack_IStaffAuthentication", is_abstract=True)
CodePack_StaffGUI = Class(name="CodePack_StaffGUI")
ManagementHandler = Class(name="ManagementHandler")
ReceptionHandler = Class(name="ReceptionHandler")
CodePack_UserGUI = Class(name="CodePack_UserGUI")
CustomerHandler = Class(name="CustomerHandler")
CodePack_CheckInMachine = Class(name="CodePack_CheckInMachine")
CheckInHandler = Class(name="CheckInHandler")
CodePack_DataBank = Class(name="CodePack_DataBank")
Room = Class(name="Room")
Booking = Class(name="Booking")
CodePack_ICheckIn = Class(name="CodePack_ICheckIn", is_abstract=True)
CodePack_IReceptionOperations_rename_required = Class(name="CodePack_IReceptionOperations_rename_required", is_abstract=True)
ICheckIn = Class(name="ICheckIn")
CodePack_DataModels_Room = Class(name="CodePack_DataModels_Room")
CodePack_DataModels_RoomType = Class(name="CodePack_DataModels_RoomType")
CodePack_DataModels_Customer = Class(name="CodePack_DataModels_Customer")
CodePack_DataModels_PaymentData = Class(name="CodePack_DataModels_PaymentData")
Customer = Class(name="Customer")
RoomType = Class(name="RoomType")
PaymentData = Class(name="PaymentData")
RoomBooked = Class(name="RoomBooked")
ExtraService = Class(name="ExtraService")
ServiceType = Class(name="ServiceType")
Guest = Class(name="Guest")
StaffRole = Class(name="StaffRole")
StaffMember = Class(name="StaffMember")
CodePack_DataModels_StaffRole = Class(name="CodePack_DataModels_StaffRole")
CodePack_DataModels_StaffMember = Class(name="CodePack_DataModels_StaffMember")
CodePack_DataModels_Guest = Class(name="CodePack_DataModels_Guest")
CodePack_DataModels_Bill = Class(name="CodePack_DataModels_Bill")
CodePack_DataModels_RoomBooked = Class(name="CodePack_DataModels_RoomBooked")
CodePack_DataModels_ServiceType = Class(name="CodePack_DataModels_ServiceType")
CodePack_DataModels_ExtraService = Class(name="CodePack_DataModels_ExtraService")
CodePack_Backend_ReceptionHandler = Class(name="CodePack_Backend_ReceptionHandler")
IReceptionOperations_rename_required = Class(name="IReceptionOperations_rename_required")
CodePack_Backend_CheckInHandler = Class(name="CodePack_Backend_CheckInHandler")
CodePack_Backend_ManagementHandler = Class(name="CodePack_Backend_ManagementHandler")
IManagement = Class(name="IManagement")
CodePack_DataModels_Booking = Class(name="CodePack_DataModels_Booking")
CodePack_Shared_ContactData = Class(name="CodePack_Shared_ContactData")
CodePack_Backend_CustomerHandler = Class(name="CodePack_Backend_CustomerHandler")
IUserAccount = Class(name="IUserAccount")
Backend_CodePack_BankComponent = Class(name="Backend_CodePack_BankComponent")

# CodePack_IBookings class attributes and methods
CodePack_IBookings_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='CodePack_date_check_in', type=StringType), Parameter(name='CodePack_number_of_guests', type=StringType), Parameter(name='CodePack_services', type=StringType), Parameter(name='CodePack_contact_data', type=StringType), Parameter(name='CodePack_rooms', type=StringType), Parameter(name='CodePack_payment_data', type=StringType), Parameter(name='CodePack_date_check_out', type=StringType)}, type=StringType)
CodePack_IBookings_m_getBookingsForCustomer: Method = Method(name="getBookingsForCustomer", parameters={Parameter(name='CodePack_customer_id', type=StringType)}, type=StringType)
CodePack_IBookings_m_getBookingForId: Method = Method(name="getBookingForId", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=StringType)
CodePack_IBookings_m_updateTimeForBooking: Method = Method(name="updateTimeForBooking", parameters={Parameter(name='CodePack_new_check_in', type=StringType), Parameter(name='CodePack_booking_id', type=StringType), Parameter(name='CodePack_new_check_out', type=StringType)}, type=BooleanType)
CodePack_IBookings_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=BooleanType)
CodePack_IBookings_m_getPaymentForBooking: Method = Method(name="getPaymentForBooking", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=StringType)
CodePack_IBookings_m_sendComfimationMail: Method = Method(name="sendComfimationMail", parameters={Parameter(name='CodePack_booking', type=StringType)})
CodePack_IBookings_m_createBookingForCustomer: Method = Method(name="createBookingForCustomer", parameters={Parameter(name='CodePack_services', type=StringType), Parameter(name='CodePack_bonus_points_used', type=StringType), Parameter(name='CodePack_rooms', type=StringType), Parameter(name='CodePack_customer_id', type=StringType), Parameter(name='CodePack_date_check_in', type=StringType), Parameter(name='CodePack_number_of_guests', type=StringType), Parameter(name='CodePack_date_check_out', type=StringType)}, type=StringType)
CodePack_IBookings_m_updateRoomForBooking: Method = Method(name="updateRoomForBooking", parameters={Parameter(name='CodePack_booking_id', type=StringType), Parameter(name='CodePack_new_room', type=StringType), Parameter(name='CodePack_old_room', type=StringType)}, type=BooleanType)
CodePack_IBookings_m_updateServiceForBooking: Method = Method(name="updateServiceForBooking", parameters={Parameter(name='CodePack_old_service_id', type=StringType), Parameter(name='CodePack_new_service', type=StringType)}, type=BooleanType)
CodePack_IBookings_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='CodePack_date_start', type=StringType), Parameter(name='CodePack_date_end', type=StringType)}, type=StringType)
CodePack_IBookings_m_getAvailableServices: Method = Method(name="getAvailableServices", parameters={}, type=StringType)
CodePack_IBookings_m_isRoomAvailable: Method = Method(name="isRoomAvailable", parameters={Parameter(name='CodePack_room_number', type=StringType), Parameter(name='CodePack_date_end', type=StringType), Parameter(name='CodePack_date_start', type=StringType)}, type=BooleanType)
CodePack_IBookings.methods={CodePack_IBookings_m_getBookingsForCustomer, CodePack_IBookings_m_getPaymentForBooking, CodePack_IBookings_m_updateRoomForBooking, CodePack_IBookings_m_getBookingForId, CodePack_IBookings_m_updateServiceForBooking, CodePack_IBookings_m_createBookingForCustomer, CodePack_IBookings_m_getAvailableServices, CodePack_IBookings_m_isRoomAvailable, CodePack_IBookings_m_updateTimeForBooking, CodePack_IBookings_m_sendComfimationMail, CodePack_IBookings_m_cancelBooking, CodePack_IBookings_m_getAvailableRooms, CodePack_IBookings_m_createBooking}

# CodePack_IUserAccount class attributes and methods
CodePack_IUserAccount_m_updateCustomerPwd: Method = Method(name="updateCustomerPwd", parameters={Parameter(name='CodePack_customer_id', type=StringType), Parameter(name='CodePack_pwd_old', type=StringType), Parameter(name='CodePack_pwd_new', type=StringType)}, type=BooleanType)
CodePack_IUserAccount_m_updateCustomerInfo: Method = Method(name="updateCustomerInfo", parameters={Parameter(name='CodePack_phone_no', type=StringType), Parameter(name='CodePack_customer_id', type=StringType), Parameter(name='CodePack_e_mail', type=StringType)}, type=BooleanType)
CodePack_IUserAccount_m_registerCustomer: Method = Method(name="registerCustomer", parameters={Parameter(name='CodePack_password', type=StringType), Parameter(name='CodePack_date_of_birth', type=StringType), Parameter(name='CodePack_e_mail', type=StringType), Parameter(name='CodePack_first_name', type=StringType), Parameter(name='CodePack_phone_no', type=StringType), Parameter(name='CodePack_last_name', type=StringType)}, type=BooleanType)
CodePack_IUserAccount_m_getCustomerInfo: Method = Method(name="getCustomerInfo", parameters={Parameter(name='CodePack_customer_id', type=StringType)}, type=StringType)
CodePack_IUserAccount_m_isEmailAvailable: Method = Method(name="isEmailAvailable", parameters={Parameter(name='CodePack_e_mail', type=StringType)}, type=BooleanType)
CodePack_IUserAccount_m_login: Method = Method(name="login", parameters={Parameter(name='CodePack_password', type=StringType), Parameter(name='CodePack_e_mail', type=StringType)}, type=IntegerType)
CodePack_IUserAccount_m_updateCustomerCC: Method = Method(name="updateCustomerCC", parameters={Parameter(name='CodePack_cc_year', type=StringType), Parameter(name='CodePack_cc_month', type=StringType), Parameter(name='CodePack_name_first', type=StringType), Parameter(name='CodePack_customer_id', type=StringType), Parameter(name='CodePack_cc_ccv', type=StringType), Parameter(name='CodePack_cc_number', type=StringType), Parameter(name='CodePack_name_last', type=StringType)}, type=BooleanType)
CodePack_IUserAccount.methods={CodePack_IUserAccount_m_updateCustomerCC, CodePack_IUserAccount_m_isEmailAvailable, CodePack_IUserAccount_m_getCustomerInfo, CodePack_IUserAccount_m_login, CodePack_IUserAccount_m_updateCustomerInfo, CodePack_IUserAccount_m_registerCustomer, CodePack_IUserAccount_m_updateCustomerPwd}

# IBookings class attributes and methods

# CodePack_IStaffAdmin class attributes and methods
CodePack_IStaffAdmin_m_registerStaffAccount: Method = Method(name="registerStaffAccount", parameters={Parameter(name='CodePack_phone_no', type=StringType), Parameter(name='CodePack_name', type=StringType), Parameter(name='CodePack_pers_no', type=StringType), Parameter(name='CodePack_email', type=StringType), Parameter(name='CodePack_role_name', type=StringType)}, type=StringType)
CodePack_IStaffAdmin_m_updateStaffAccount: Method = Method(name="updateStaffAccount", parameters={Parameter(name='CodePack_account', type=StringType)}, type=BooleanType)
CodePack_IStaffAdmin_m_getStaffAccount: Method = Method(name="getStaffAccount", parameters={Parameter(name='CodePack_pers_no', type=StringType)}, type=StringType)
CodePack_IStaffAdmin_m_getAllStaffAccounts: Method = Method(name="getAllStaffAccounts", parameters={}, type=StringType)
CodePack_IStaffAdmin_m_removeStaffAccount: Method = Method(name="removeStaffAccount", parameters={Parameter(name='CodePack_account', type=StringType)}, type=BooleanType)
CodePack_IStaffAdmin_m_getStaffRoles: Method = Method(name="getStaffRoles", parameters={}, type=StringType)
CodePack_IStaffAdmin_m_addStaffRole: Method = Method(name="addStaffRole", parameters={Parameter(name='CodePack_canManageServices', type=StringType), Parameter(name='CodePack_canManageRooms', type=StringType), Parameter(name='CodePack_canManageBookings', type=StringType), Parameter(name='CodePack_canManageAccounts', type=StringType), Parameter(name='CodePack_name', type=StringType)}, type=StringType)
CodePack_IStaffAdmin_m_updateStaffRole: Method = Method(name="updateStaffRole", parameters={Parameter(name='CodePack_role', type=StringType)}, type=BooleanType)
CodePack_IStaffAdmin_m_removeStaffRole: Method = Method(name="removeStaffRole", parameters={Parameter(name='CodePack_role', type=StringType)}, type=BooleanType)
CodePack_IStaffAdmin.methods={CodePack_IStaffAdmin_m_updateStaffAccount, CodePack_IStaffAdmin_m_registerStaffAccount, CodePack_IStaffAdmin_m_removeStaffAccount, CodePack_IStaffAdmin_m_addStaffRole, CodePack_IStaffAdmin_m_getAllStaffAccounts, CodePack_IStaffAdmin_m_getStaffRoles, CodePack_IStaffAdmin_m_removeStaffRole, CodePack_IStaffAdmin_m_updateStaffRole, CodePack_IStaffAdmin_m_getStaffAccount}

# CodePack_IManagement class attributes and methods
CodePack_IManagement_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='CodePack_type', type=StringType), Parameter(name='CodePack_description', type=StringType), Parameter(name='CodePack_number', type=StringType), Parameter(name='CodePack_isAvailable', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_updateRoom: Method = Method(name="updateRoom", parameters={Parameter(name='CodePack_room', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='CodePack_number', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='CodePack_max_guests', type=StringType), Parameter(name='CodePack_description', type=StringType), Parameter(name='CodePack_rate', type=StringType), Parameter(name='CodePack_name', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_updateRoomType: Method = Method(name="updateRoomType", parameters={Parameter(name='CodePack_roomType', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='CodePack_type_name', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='CodePack_number', type=StringType)}, type=StringType)
CodePack_IManagement_m_getAllRooms: Method = Method(name="getAllRooms", parameters={}, type=StringType)
CodePack_IManagement_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={}, type=StringType)
CodePack_IManagement_m_getServiceTypes: Method = Method(name="getServiceTypes", parameters={}, type=StringType)
CodePack_IManagement_m_updateServiceType: Method = Method(name="updateServiceType", parameters={Parameter(name='CodePack_serviceType', type=StringType)}, type=BooleanType)
CodePack_IManagement_m_removeServiceType: Method = Method(name="removeServiceType", parameters={Parameter(name='CodePack_serviceType', type=StringType)}, type=BooleanType)
CodePack_IManagement.methods={CodePack_IManagement_m_getServiceTypes, CodePack_IManagement_m_updateRoom, CodePack_IManagement_m_removeRoomType, CodePack_IManagement_m_getAllRooms, CodePack_IManagement_m_removeServiceType, CodePack_IManagement_m_addRoom, CodePack_IManagement_m_removeRoom, CodePack_IManagement_m_updateServiceType, CodePack_IManagement_m_getRoom, CodePack_IManagement_m_getRoomTypes, CodePack_IManagement_m_addRoomType, CodePack_IManagement_m_updateRoomType}

# IStaffAdmin class attributes and methods

# IStaffAuthentication class attributes and methods

# CodePack_IStaffAuthentication class attributes and methods
CodePack_IStaffAuthentication_m_login: Method = Method(name="login", parameters={Parameter(name='CodePack_e_mail', type=StringType), Parameter(name='CodePack_password', type=StringType)}, type=StringType)
CodePack_IStaffAuthentication_m_getRoleForStaff: Method = Method(name="getRoleForStaff", parameters={Parameter(name='CodePack_pers_no', type=StringType)}, type=StringType)
CodePack_IStaffAuthentication.methods={CodePack_IStaffAuthentication_m_getRoleForStaff, CodePack_IStaffAuthentication_m_login}

# CodePack_StaffGUI class attributes and methods
CodePack_StaffGUI_m_startUI: Method = Method(name="startUI", parameters={})
CodePack_StaffGUI.methods={CodePack_StaffGUI_m_startUI}

# ManagementHandler class attributes and methods

# ReceptionHandler class attributes and methods

# CodePack_UserGUI class attributes and methods
CodePack_UserGUI_m_startUI: Method = Method(name="startUI", parameters={})
CodePack_UserGUI.methods={CodePack_UserGUI_m_startUI}

# CustomerHandler class attributes and methods

# CodePack_CheckInMachine class attributes and methods
CodePack_CheckInMachine_m_startUI: Method = Method(name="startUI", parameters={})
CodePack_CheckInMachine.methods={CodePack_CheckInMachine_m_startUI}

# CheckInHandler class attributes and methods

# CodePack_DataBank class attributes and methods

# Room class attributes and methods

# Booking class attributes and methods

# CodePack_ICheckIn class attributes and methods
CodePack_ICheckIn_m_validateBooking: Method = Method(name="validateBooking", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=BooleanType)
CodePack_ICheckIn_m_assignGuestToBooking: Method = Method(name="assignGuestToBooking", parameters={Parameter(name='CodePack_booking_id', type=StringType), Parameter(name='CodePack_guest_name', type=StringType)}, type=StringType)
CodePack_ICheckIn.methods={CodePack_ICheckIn_m_assignGuestToBooking, CodePack_ICheckIn_m_validateBooking}

# CodePack_IReceptionOperations_rename_required class attributes and methods
CodePack_IReceptionOperations_rename_required_m_generateReceipt: Method = Method(name="generateReceipt", parameters={Parameter(name='CodePack_bill', type=StringType)}, type=StringType)
CodePack_IReceptionOperations_rename_required_m_generateBill: Method = Method(name="generateBill", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=StringType)
CodePack_IReceptionOperations_rename_required_m_isCheckedIn: Method = Method(name="isCheckedIn", parameters={Parameter(name='CodePack_booking_id', type=StringType)}, type=BooleanType)
CodePack_IReceptionOperations_rename_required.methods={CodePack_IReceptionOperations_rename_required_m_isCheckedIn, CodePack_IReceptionOperations_rename_required_m_generateBill, CodePack_IReceptionOperations_rename_required_m_generateReceipt}

# ICheckIn class attributes and methods

# CodePack_DataModels_Room class attributes and methods
CodePack_DataModels_Room_number: Property = Property(name="number", type=IntegerType)
CodePack_DataModels_Room_description: Property = Property(name="description", type=StringType)
CodePack_DataModels_Room_isAvailable: Property = Property(name="isAvailable", type=BooleanType)
CodePack_DataModels_Room_room_type: Property = Property(name="room_type", type=StringType)
CodePack_DataModels_Room.attributes={CodePack_DataModels_Room_isAvailable, CodePack_DataModels_Room_room_type, CodePack_DataModels_Room_description, CodePack_DataModels_Room_number}

# CodePack_DataModels_RoomType class attributes and methods
CodePack_DataModels_RoomType_description: Property = Property(name="description", type=StringType)
CodePack_DataModels_RoomType_max_guests: Property = Property(name="max_guests", type=IntegerType)
CodePack_DataModels_RoomType_rate: Property = Property(name="rate", type=FloatType)
CodePack_DataModels_RoomType_typename: Property = Property(name="typename", type=StringType)
CodePack_DataModels_RoomType.attributes={CodePack_DataModels_RoomType_rate, CodePack_DataModels_RoomType_description, CodePack_DataModels_RoomType_typename, CodePack_DataModels_RoomType_max_guests}

# CodePack_DataModels_Customer class attributes and methods
CodePack_DataModels_Customer_password: Property = Property(name="password", type=StringType)
CodePack_DataModels_Customer_date_of_birth: Property = Property(name="date_of_birth", type=DateType)
CodePack_DataModels_Customer_bonus_points: Property = Property(name="bonus_points", type=IntegerType)
CodePack_DataModels_Customer_e_mail: Property = Property(name="e_mail", type=StringType)
CodePack_DataModels_Customer_first_name: Property = Property(name="first_name", type=StringType)
CodePack_DataModels_Customer_phone_no: Property = Property(name="phone_no", type=IntegerType)
CodePack_DataModels_Customer_customer_id: Property = Property(name="customer_id", type=IntegerType)
CodePack_DataModels_Customer_payment_id: Property = Property(name="payment_id", type=IntegerType)
CodePack_DataModels_Customer_last_name: Property = Property(name="last_name", type=StringType)
CodePack_DataModels_Customer.attributes={CodePack_DataModels_Customer_first_name, CodePack_DataModels_Customer_phone_no, CodePack_DataModels_Customer_date_of_birth, CodePack_DataModels_Customer_last_name, CodePack_DataModels_Customer_bonus_points, CodePack_DataModels_Customer_customer_id, CodePack_DataModels_Customer_payment_id, CodePack_DataModels_Customer_password, CodePack_DataModels_Customer_e_mail}

# CodePack_DataModels_PaymentData class attributes and methods
CodePack_DataModels_PaymentData_cc_number: Property = Property(name="cc_number", type=StringType)
CodePack_DataModels_PaymentData_cc_ccv: Property = Property(name="cc_ccv", type=StringType)
CodePack_DataModels_PaymentData_cc_month: Property = Property(name="cc_month", type=IntegerType)
CodePack_DataModels_PaymentData_cc_year: Property = Property(name="cc_year", type=IntegerType)
CodePack_DataModels_PaymentData_cc_first_name: Property = Property(name="cc_first_name", type=StringType)
CodePack_DataModels_PaymentData_cc_last_name: Property = Property(name="cc_last_name", type=StringType)
CodePack_DataModels_PaymentData_id: Property = Property(name="id", type=IntegerType)
CodePack_DataModels_PaymentData.attributes={CodePack_DataModels_PaymentData_id, CodePack_DataModels_PaymentData_cc_year, CodePack_DataModels_PaymentData_cc_first_name, CodePack_DataModels_PaymentData_cc_last_name, CodePack_DataModels_PaymentData_cc_ccv, CodePack_DataModels_PaymentData_cc_number, CodePack_DataModels_PaymentData_cc_month}

# Customer class attributes and methods

# RoomType class attributes and methods

# PaymentData class attributes and methods

# RoomBooked class attributes and methods

# ExtraService class attributes and methods

# ServiceType class attributes and methods

# Guest class attributes and methods

# StaffRole class attributes and methods

# StaffMember class attributes and methods

# CodePack_DataModels_StaffRole class attributes and methods
CodePack_DataModels_StaffRole_name: Property = Property(name="name", type=StringType)
CodePack_DataModels_StaffRole_canManageBookings: Property = Property(name="canManageBookings", type=BooleanType)
CodePack_DataModels_StaffRole_canManageRooms: Property = Property(name="canManageRooms", type=BooleanType)
CodePack_DataModels_StaffRole_canManageServices: Property = Property(name="canManageServices", type=BooleanType)
CodePack_DataModels_StaffRole_canManageAccounts: Property = Property(name="canManageAccounts", type=BooleanType)
CodePack_DataModels_StaffRole.attributes={CodePack_DataModels_StaffRole_name, CodePack_DataModels_StaffRole_canManageRooms, CodePack_DataModels_StaffRole_canManageAccounts, CodePack_DataModels_StaffRole_canManageServices, CodePack_DataModels_StaffRole_canManageBookings}

# CodePack_DataModels_StaffMember class attributes and methods
CodePack_DataModels_StaffMember_full_name: Property = Property(name="full_name", type=StringType)
CodePack_DataModels_StaffMember_email: Property = Property(name="email", type=StringType)
CodePack_DataModels_StaffMember_password: Property = Property(name="password", type=StringType)
CodePack_DataModels_StaffMember_pers_no: Property = Property(name="pers_no", type=StringType)
CodePack_DataModels_StaffMember_phone_no: Property = Property(name="phone_no", type=IntegerType)
CodePack_DataModels_StaffMember_role_name: Property = Property(name="role_name", type=StringType)
CodePack_DataModels_StaffMember.attributes={CodePack_DataModels_StaffMember_email, CodePack_DataModels_StaffMember_password, CodePack_DataModels_StaffMember_phone_no, CodePack_DataModels_StaffMember_full_name, CodePack_DataModels_StaffMember_role_name, CodePack_DataModels_StaffMember_pers_no}

# CodePack_DataModels_Guest class attributes and methods
CodePack_DataModels_Guest_name: Property = Property(name="name", type=StringType)
CodePack_DataModels_Guest_booking_id: Property = Property(name="booking_id", type=IntegerType)
CodePack_DataModels_Guest.attributes={CodePack_DataModels_Guest_booking_id, CodePack_DataModels_Guest_name}

# CodePack_DataModels_Bill class attributes and methods
CodePack_DataModels_Bill_booking_id: Property = Property(name="booking_id", type=IntegerType)
CodePack_DataModels_Bill_total_price: Property = Property(name="total_price", type=FloatType)
CodePack_DataModels_Bill.attributes={CodePack_DataModels_Bill_total_price, CodePack_DataModels_Bill_booking_id}

# CodePack_DataModels_RoomBooked class attributes and methods
CodePack_DataModels_RoomBooked_room_number: Property = Property(name="room_number", type=IntegerType)
CodePack_DataModels_RoomBooked_booking_id: Property = Property(name="booking_id", type=IntegerType)
CodePack_DataModels_RoomBooked_date_start: Property = Property(name="date_start", type=DateType)
CodePack_DataModels_RoomBooked_date_end: Property = Property(name="date_end", type=DateType)
CodePack_DataModels_RoomBooked.attributes={CodePack_DataModels_RoomBooked_room_number, CodePack_DataModels_RoomBooked_date_end, CodePack_DataModels_RoomBooked_booking_id, CodePack_DataModels_RoomBooked_date_start}

# CodePack_DataModels_ServiceType class attributes and methods
CodePack_DataModels_ServiceType_description: Property = Property(name="description", type=StringType)
CodePack_DataModels_ServiceType_type_name: Property = Property(name="type_name", type=StringType)
CodePack_DataModels_ServiceType_price: Property = Property(name="price", type=FloatType)
CodePack_DataModels_ServiceType.attributes={CodePack_DataModels_ServiceType_description, CodePack_DataModels_ServiceType_type_name, CodePack_DataModels_ServiceType_price}

# CodePack_DataModels_ExtraService class attributes and methods
CodePack_DataModels_ExtraService_date_start: Property = Property(name="date_start", type=DateType)
CodePack_DataModels_ExtraService_date_end: Property = Property(name="date_end", type=DateType)
CodePack_DataModels_ExtraService_booking_id: Property = Property(name="booking_id", type=IntegerType)
CodePack_DataModels_ExtraService_total_price: Property = Property(name="total_price", type=FloatType)
CodePack_DataModels_ExtraService_type: Property = Property(name="type", type=StringType)
CodePack_DataModels_ExtraService.attributes={CodePack_DataModels_ExtraService_total_price, CodePack_DataModels_ExtraService_booking_id, CodePack_DataModels_ExtraService_date_start, CodePack_DataModels_ExtraService_date_end, CodePack_DataModels_ExtraService_type}

# CodePack_Backend_ReceptionHandler class attributes and methods

# IReceptionOperations_rename_required class attributes and methods

# CodePack_Backend_CheckInHandler class attributes and methods

# CodePack_Backend_ManagementHandler class attributes and methods

# IManagement class attributes and methods

# CodePack_DataModels_Booking class attributes and methods
CodePack_DataModels_Booking_id: Property = Property(name="id", type=IntegerType)
CodePack_DataModels_Booking_date_check_in: Property = Property(name="date_check_in", type=DateType)
CodePack_DataModels_Booking_date_check_out: Property = Property(name="date_check_out", type=DateType)
CodePack_DataModels_Booking_isCheckedIn: Property = Property(name="isCheckedIn", type=BooleanType)
CodePack_DataModels_Booking_total_price: Property = Property(name="total_price", type=FloatType)
CodePack_DataModels_Booking_contact_name: Property = Property(name="contact_name", type=StringType)
CodePack_DataModels_Booking_contact_phone: Property = Property(name="contact_phone", type=IntegerType)
CodePack_DataModels_Booking_contact_email: Property = Property(name="contact_email", type=StringType)
CodePack_DataModels_Booking_customer_id: Property = Property(name="customer_id", type=IntegerType)
CodePack_DataModels_Booking_payment_id: Property = Property(name="payment_id", type=IntegerType)
CodePack_DataModels_Booking_bonus_points_used: Property = Property(name="bonus_points_used", type=IntegerType)
CodePack_DataModels_Booking.attributes={CodePack_DataModels_Booking_contact_name, CodePack_DataModels_Booking_date_check_in, CodePack_DataModels_Booking_bonus_points_used, CodePack_DataModels_Booking_customer_id, CodePack_DataModels_Booking_isCheckedIn, CodePack_DataModels_Booking_total_price, CodePack_DataModels_Booking_id, CodePack_DataModels_Booking_contact_email, CodePack_DataModels_Booking_contact_phone, CodePack_DataModels_Booking_date_check_out, CodePack_DataModels_Booking_payment_id}

# CodePack_Shared_ContactData class attributes and methods
CodePack_Shared_ContactData_full_name: Property = Property(name="full_name", type=StringType)
CodePack_Shared_ContactData_e_mail: Property = Property(name="e_mail", type=StringType)
CodePack_Shared_ContactData_phone_no: Property = Property(name="phone_no", type=IntegerType)
CodePack_Shared_ContactData.attributes={CodePack_Shared_ContactData_full_name, CodePack_Shared_ContactData_e_mail, CodePack_Shared_ContactData_phone_no}

# CodePack_Backend_CustomerHandler class attributes and methods

# IUserAccount class attributes and methods

# Backend_CodePack_BankComponent class attributes and methods

# Relationships
managementHandler0: BinaryAssociation = BinaryAssociation(
    name="managementHandler0",
    ends={
        Property(name="ManagementHandler", type=CodePack_StaffGUI, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_StaffGUI", type=ManagementHandler, multiplicity=Multiplicity(0, 1))
    }
)
receptionHandler1: BinaryAssociation = BinaryAssociation(
    name="receptionHandler1",
    ends={
        Property(name="ReceptionHandler", type=CodePack_StaffGUI, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_StaffGUI2", type=ReceptionHandler, multiplicity=Multiplicity(0, 1))
    }
)
customerHandler3: BinaryAssociation = BinaryAssociation(
    name="customerHandler3",
    ends={
        Property(name="CustomerHandler", type=CodePack_UserGUI, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_UserGUI", type=CustomerHandler, multiplicity=Multiplicity(0, 1))
    }
)
checkInHandler4: BinaryAssociation = BinaryAssociation(
    name="checkInHandler4",
    ends={
        Property(name="CheckInHandler", type=CodePack_CheckInMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_CheckInMachine", type=CheckInHandler, multiplicity=Multiplicity(0, 1))
    }
)
roomList5: BinaryAssociation = BinaryAssociation(
    name="roomList5",
    ends={
        Property(name="Room", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank", type=Room, multiplicity=Multiplicity(1, 9999))
    }
)
bookingList6: BinaryAssociation = BinaryAssociation(
    name="bookingList6",
    ends={
        Property(name="Booking", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank7", type=Booking, multiplicity=Multiplicity(1, 9999))
    }
)
customerList8: BinaryAssociation = BinaryAssociation(
    name="customerList8",
    ends={
        Property(name="Customer", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank9", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
roomTypeList10: BinaryAssociation = BinaryAssociation(
    name="roomTypeList10",
    ends={
        Property(name="RoomType", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank11", type=RoomType, multiplicity=Multiplicity(1, 9999))
    }
)
paymentDataList12: BinaryAssociation = BinaryAssociation(
    name="paymentDataList12",
    ends={
        Property(name="PaymentData", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank13", type=PaymentData, multiplicity=Multiplicity(1, 9999))
    }
)
roomBookedList14: BinaryAssociation = BinaryAssociation(
    name="roomBookedList14",
    ends={
        Property(name="RoomBooked", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank15", type=RoomBooked, multiplicity=Multiplicity(1, 9999))
    }
)
extraServiceList16: BinaryAssociation = BinaryAssociation(
    name="extraServiceList16",
    ends={
        Property(name="ExtraService", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank17", type=ExtraService, multiplicity=Multiplicity(1, 9999))
    }
)
serviceTypeList18: BinaryAssociation = BinaryAssociation(
    name="serviceTypeList18",
    ends={
        Property(name="ServiceType", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank19", type=ServiceType, multiplicity=Multiplicity(1, 9999))
    }
)
GuestList20: BinaryAssociation = BinaryAssociation(
    name="GuestList20",
    ends={
        Property(name="Guest", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank21", type=Guest, multiplicity=Multiplicity(1, 9999))
    }
)
staffRoleList22: BinaryAssociation = BinaryAssociation(
    name="staffRoleList22",
    ends={
        Property(name="StaffRole", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank23", type=StaffRole, multiplicity=Multiplicity(1, 9999))
    }
)
staffMemberList24: BinaryAssociation = BinaryAssociation(
    name="staffMemberList24",
    ends={
        Property(name="StaffMember", type=CodePack_DataBank, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataBank25", type=StaffMember, multiplicity=Multiplicity(1, 9999))
    }
)
rooms_booked28: BinaryAssociation = BinaryAssociation(
    name="rooms_booked28",
    ends={
        Property(name="Room29", type=CodePack_DataModels_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataModels_Bill", type=Room, multiplicity=Multiplicity(1, 9999))
    }
)
services_ordered30: BinaryAssociation = BinaryAssociation(
    name="services_ordered30",
    ends={
        Property(name="ExtraService32", type=CodePack_DataModels_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataModels_Bill31", type=ExtraService, multiplicity=Multiplicity(1, 9999))
    }
)
booking26: BinaryAssociation = BinaryAssociation(
    name="booking26",
    ends={
        Property(name="Booking27", type=CodePack_DataModels_RoomBooked, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataModels_RoomBooked", type=Booking, multiplicity=Multiplicity(1, 1))
    }
)
bankComponent35: BinaryAssociation = BinaryAssociation(
    name="bankComponent35",
    ends={
        Property(name="CodePack_Backend_CustomerHandler", type=Backend_CodePack_BankComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Backend_CodePack_BankComponent", type=CodePack_Backend_CustomerHandler, multiplicity=Multiplicity(1, 1))
    }
)
bankComponent36: BinaryAssociation = BinaryAssociation(
    name="bankComponent36",
    ends={
        Property(name="Backend_CodePack_BankComponent37", type=CodePack_Backend_ReceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_Backend_ReceptionHandler", type=Backend_CodePack_BankComponent, multiplicity=Multiplicity(1, 1))
    }
)
room33: BinaryAssociation = BinaryAssociation(
    name="room33",
    ends={
        Property(name="Room34", type=CodePack_DataModels_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="CodePack_DataModels_Booking", type=Room, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CodePack_IUserAccount_IBookings = Generalization(general=IBookings, specific=CodePack_IUserAccount)
gen_CodePack_IManagement_IStaffAdmin = Generalization(general=IStaffAdmin, specific=CodePack_IManagement)
gen_CodePack_IManagement_IStaffAuthentication = Generalization(general=IStaffAuthentication, specific=CodePack_IManagement)
gen_CodePack_IReceptionOperations_rename_required_IBookings = Generalization(general=IBookings, specific=CodePack_IReceptionOperations_rename_required)
gen_CodePack_IReceptionOperations_rename_required_ICheckIn = Generalization(general=ICheckIn, specific=CodePack_IReceptionOperations_rename_required)
gen_CodePack_IReceptionOperations_rename_required_IStaffAuthentication = Generalization(general=IStaffAuthentication, specific=CodePack_IReceptionOperations_rename_required)
gen_CodePack_Backend_ReceptionHandler_IReceptionOperations_rename_required = Generalization(general=IReceptionOperations_rename_required, specific=CodePack_Backend_ReceptionHandler)
gen_CodePack_Backend_CheckInHandler_ICheckIn = Generalization(general=ICheckIn, specific=CodePack_Backend_CheckInHandler)
gen_CodePack_Backend_ManagementHandler_IManagement = Generalization(general=IManagement, specific=CodePack_Backend_ManagementHandler)
gen_CodePack_Backend_CustomerHandler_IUserAccount = Generalization(general=IUserAccount, specific=CodePack_Backend_CustomerHandler)

# Domain Model
domain_model = DomainModel(
    name="CodePack",
    types={CodePack_IBookings, CodePack_IUserAccount, IBookings, CodePack_IStaffAdmin, CodePack_IManagement, IStaffAdmin, IStaffAuthentication, CodePack_IStaffAuthentication, CodePack_StaffGUI, ManagementHandler, ReceptionHandler, CodePack_UserGUI, CustomerHandler, CodePack_CheckInMachine, CheckInHandler, CodePack_DataBank, Room, Booking, CodePack_ICheckIn, CodePack_IReceptionOperations_rename_required, ICheckIn, CodePack_DataModels_Room, CodePack_DataModels_RoomType, CodePack_DataModels_Customer, CodePack_DataModels_PaymentData, Customer, RoomType, PaymentData, RoomBooked, ExtraService, ServiceType, Guest, StaffRole, StaffMember, CodePack_DataModels_StaffRole, CodePack_DataModels_StaffMember, CodePack_DataModels_Guest, CodePack_DataModels_Bill, CodePack_DataModels_RoomBooked, CodePack_DataModels_ServiceType, CodePack_DataModels_ExtraService, CodePack_Backend_ReceptionHandler, IReceptionOperations_rename_required, CodePack_Backend_CheckInHandler, CodePack_Backend_ManagementHandler, IManagement, CodePack_DataModels_Booking, CodePack_Shared_ContactData, CodePack_Backend_CustomerHandler, IUserAccount, Backend_CodePack_BankComponent},
    associations={managementHandler0, receptionHandler1, customerHandler3, checkInHandler4, roomList5, bookingList6, customerList8, roomTypeList10, paymentDataList12, roomBookedList14, extraServiceList16, serviceTypeList18, GuestList20, staffRoleList22, staffMemberList24, rooms_booked28, services_ordered30, booking26, bankComponent35, bankComponent36, room33},
    generalizations={gen_CodePack_IUserAccount_IBookings, gen_CodePack_IManagement_IStaffAdmin, gen_CodePack_IManagement_IStaffAuthentication, gen_CodePack_IReceptionOperations_rename_required_IBookings, gen_CodePack_IReceptionOperations_rename_required_ICheckIn, gen_CodePack_IReceptionOperations_rename_required_IStaffAuthentication, gen_CodePack_Backend_ReceptionHandler_IReceptionOperations_rename_required, gen_CodePack_Backend_CheckInHandler_ICheckIn, gen_CodePack_Backend_ManagementHandler_IManagement, gen_CodePack_Backend_CustomerHandler_IUserAccount},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)