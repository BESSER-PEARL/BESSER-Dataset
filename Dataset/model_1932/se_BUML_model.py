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
hotelsystem_Booking = Class(name="hotelsystem_Booking")
hotelsystem_PaymentHandler = Class(name="hotelsystem_PaymentHandler")
hotelsystem_IRoomHandler = Class(name="hotelsystem_IRoomHandler")
se_hotelsystem_Booking = Class(name="se_hotelsystem_Booking")
hotelsystem_Customer = Class(name="hotelsystem_Customer")
hotelsystem_RoomReservation = Class(name="hotelsystem_RoomReservation")
se_hotelsystem_BookingHandler = Class(name="se_hotelsystem_BookingHandler")
hotelsystem_IHotelReceptionistProvides = Class(name="hotelsystem_IHotelReceptionistProvides")
hotelsystem_IHotelCustomerProvides = Class(name="hotelsystem_IHotelCustomerProvides")
hotelsystem_RoomType = Class(name="hotelsystem_RoomType")
hotelsystem_RoomExtra = Class(name="hotelsystem_RoomExtra")
hotelsystem_Room = Class(name="hotelsystem_Room")
se_hotelsystem_RoomType = Class(name="se_hotelsystem_RoomType")
se_hotelsystem_RoomExtra = Class(name="se_hotelsystem_RoomExtra")
se_hotelsystem_Room = Class(name="se_hotelsystem_Room")
hotelsystem_Bill = Class(name="hotelsystem_Bill")
se_hotelsystem_Customer = Class(name="se_hotelsystem_Customer")
se_hotelsystem_RoomReservation = Class(name="se_hotelsystem_RoomReservation")
bankcomponents_ICustomerProvides = Class(name="bankcomponents_ICustomerProvides")
se_hotelsystem_IRoomHandler = Class(name="se_hotelsystem_IRoomHandler", is_abstract=True)
se_hotelsystem_IHotelReceptionistProvides = Class(name="se_hotelsystem_IHotelReceptionistProvides", is_abstract=True)
se_hotelsystem_Bill = Class(name="se_hotelsystem_Bill")
se_hotelsystem_PaymentHandler = Class(name="se_hotelsystem_PaymentHandler")
se_hotelsystem_IHotelCustomerProvides = Class(name="se_hotelsystem_IHotelCustomerProvides", is_abstract=True)
se_hotelsystem_FreeRoomTypesDTO = Class(name="se_hotelsystem_FreeRoomTypesDTO")
se_hotelsystem_RoomHandler = Class(name="se_hotelsystem_RoomHandler")
hotelsystem_IHotelAdministratorProvides = Class(name="hotelsystem_IHotelAdministratorProvides")
se_hotelsystem_IHotelAdministratorProvides = Class(name="se_hotelsystem_IHotelAdministratorProvides", is_abstract=True)
se_hotelsystem_IHotelStartupProvides = Class(name="se_hotelsystem_IHotelStartupProvides", is_abstract=True)
se_hotelsystem_HotelInitializer = Class(name="se_hotelsystem_HotelInitializer")
IHotelStartupProvides = Class(name="IHotelStartupProvides")
hotelsystem_RoomHandler = Class(name="hotelsystem_RoomHandler")
se_bankcomponents_BankAdministrator = Class(name="se_bankcomponents_BankAdministrator")
IAdministratorProvides = Class(name="IAdministratorProvides")
se_bankcomponents_IAdministratorProvides = Class(name="se_bankcomponents_IAdministratorProvides", is_abstract=True)
se_actor_User = Class(name="se_actor_User")
se_actor_Receptionist = Class(name="se_actor_Receptionist")
User = Class(name="User")
se_actor_Administrator = Class(name="se_actor_Administrator")
hotelsystem_IHotelStartupProvides = Class(name="hotelsystem_IHotelStartupProvides")
se_bankcomponents_ICustomerProvides = Class(name="se_bankcomponents_ICustomerProvides", is_abstract=True)

# hotelsystem_Booking class attributes and methods

# hotelsystem_PaymentHandler class attributes and methods

# hotelsystem_IRoomHandler class attributes and methods

# se_hotelsystem_Booking class attributes and methods
se_hotelsystem_Booking_startDate: Property = Property(name="startDate", type=StringType)
se_hotelsystem_Booking_endDate: Property = Property(name="endDate", type=StringType)
se_hotelsystem_Booking_canceled: Property = Property(name="canceled", type=BooleanType)
se_hotelsystem_Booking_bookingId: Property = Property(name="bookingId", type=IntegerType)
se_hotelsystem_Booking_confirmed: Property = Property(name="confirmed", type=BooleanType)
se_hotelsystem_Booking_m_cancel: Method = Method(name="cancel", parameters={})
se_hotelsystem_Booking_m_getOccupiedRooms: Method = Method(name="getOccupiedRooms", parameters={Parameter(name='se_date', type=StringType)}, type=StringType)
se_hotelsystem_Booking_m_checkOut: Method = Method(name="checkOut", parameters={}, type=FloatType)
se_hotelsystem_Booking_m_nrOfNights: Method = Method(name="nrOfNights", parameters={}, type=IntegerType)
se_hotelsystem_Booking_m_isCheckedIn: Method = Method(name="isCheckedIn", parameters={}, type=BooleanType)
se_hotelsystem_Booking_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='se_room', type=StringType)}, type=BooleanType)
se_hotelsystem_Booking_m_getBookingPrice: Method = Method(name="getBookingPrice", parameters={}, type=FloatType)
se_hotelsystem_Booking_m_getRoomPrice: Method = Method(name="getRoomPrice", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=FloatType)
se_hotelsystem_Booking_m_isFree: Method = Method(name="isFree", parameters={Parameter(name='se_roomId', type=StringType), Parameter(name='se_endDate', type=StringType), Parameter(name='se_startDate', type=StringType)}, type=BooleanType)
se_hotelsystem_Booking_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='se_extra', type=StringType), Parameter(name='se_roomNbr', type=StringType)}, type=BooleanType)
se_hotelsystem_Booking_m_checkOutRoom: Method = Method(name="checkOutRoom", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=FloatType)
se_hotelsystem_Booking.attributes={se_hotelsystem_Booking_startDate, se_hotelsystem_Booking_bookingId, se_hotelsystem_Booking_endDate, se_hotelsystem_Booking_confirmed, se_hotelsystem_Booking_canceled}
se_hotelsystem_Booking.methods={se_hotelsystem_Booking_m_cancel, se_hotelsystem_Booking_m_addExtra, se_hotelsystem_Booking_m_getBookingPrice, se_hotelsystem_Booking_m_getRoomPrice, se_hotelsystem_Booking_m_isFree, se_hotelsystem_Booking_m_checkOutRoom, se_hotelsystem_Booking_m_checkIn, se_hotelsystem_Booking_m_checkOut, se_hotelsystem_Booking_m_isCheckedIn, se_hotelsystem_Booking_m_getOccupiedRooms, se_hotelsystem_Booking_m_nrOfNights}

# hotelsystem_Customer class attributes and methods

# hotelsystem_RoomReservation class attributes and methods

# se_hotelsystem_BookingHandler class attributes and methods
se_hotelsystem_BookingHandler_bookingCurrentlyCheckingOut: Property = Property(name="bookingCurrentlyCheckingOut", type=IntegerType)
se_hotelsystem_BookingHandler_nextBookingId: Property = Property(name="nextBookingId", type=IntegerType)
se_hotelsystem_BookingHandler_m_getBookingById: Method = Method(name="getBookingById", parameters={Parameter(name='se_bookingId', type=StringType)}, type=StringType)
se_hotelsystem_BookingHandler_m_isFree: Method = Method(name="isFree", parameters={Parameter(name='se_startDate', type=StringType), Parameter(name='se_endDate', type=StringType), Parameter(name='se_roomId', type=StringType)}, type=BooleanType)
se_hotelsystem_BookingHandler.attributes={se_hotelsystem_BookingHandler_nextBookingId, se_hotelsystem_BookingHandler_bookingCurrentlyCheckingOut}
se_hotelsystem_BookingHandler.methods={se_hotelsystem_BookingHandler_m_isFree, se_hotelsystem_BookingHandler_m_getBookingById}

# hotelsystem_IHotelReceptionistProvides class attributes and methods

# hotelsystem_IHotelCustomerProvides class attributes and methods

# hotelsystem_RoomType class attributes and methods

# hotelsystem_RoomExtra class attributes and methods

# hotelsystem_Room class attributes and methods

# se_hotelsystem_RoomType class attributes and methods
se_hotelsystem_RoomType_description: Property = Property(name="description", type=StringType)
se_hotelsystem_RoomType_numBeds: Property = Property(name="numBeds", type=IntegerType)
se_hotelsystem_RoomType_pricePerNight: Property = Property(name="pricePerNight", type=FloatType)
se_hotelsystem_RoomType_name: Property = Property(name="name", type=StringType)
se_hotelsystem_RoomType.attributes={se_hotelsystem_RoomType_description, se_hotelsystem_RoomType_name, se_hotelsystem_RoomType_numBeds, se_hotelsystem_RoomType_pricePerNight}

# se_hotelsystem_RoomExtra class attributes and methods
se_hotelsystem_RoomExtra_price: Property = Property(name="price", type=FloatType)
se_hotelsystem_RoomExtra_description: Property = Property(name="description", type=StringType)
se_hotelsystem_RoomExtra.attributes={se_hotelsystem_RoomExtra_description, se_hotelsystem_RoomExtra_price}

# se_hotelsystem_Room class attributes and methods
se_hotelsystem_Room_occupied: Property = Property(name="occupied", type=BooleanType)
se_hotelsystem_Room_blocked: Property = Property(name="blocked", type=BooleanType)
se_hotelsystem_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
se_hotelsystem_Room.attributes={se_hotelsystem_Room_blocked, se_hotelsystem_Room_occupied, se_hotelsystem_Room_roomNumber}

# hotelsystem_Bill class attributes and methods

# se_hotelsystem_Customer class attributes and methods
se_hotelsystem_Customer_firstName: Property = Property(name="firstName", type=StringType)
se_hotelsystem_Customer_lastName: Property = Property(name="lastName", type=StringType)
se_hotelsystem_Customer.attributes={se_hotelsystem_Customer_firstName, se_hotelsystem_Customer_lastName}

# se_hotelsystem_RoomReservation class attributes and methods
se_hotelsystem_RoomReservation_startDate: Property = Property(name="startDate", type=StringType)
se_hotelsystem_RoomReservation_endDate: Property = Property(name="endDate", type=StringType)
se_hotelsystem_RoomReservation_checkInDate: Property = Property(name="checkInDate", type=StringType)
se_hotelsystem_RoomReservation_checkOuDate: Property = Property(name="checkOuDate", type=StringType)
se_hotelsystem_RoomReservation_m_getRoomIfOccupied: Method = Method(name="getRoomIfOccupied", parameters={Parameter(name='se_date', type=StringType)}, type=StringType)
se_hotelsystem_RoomReservation_m_getRoomId: Method = Method(name="getRoomId", parameters={}, type=IntegerType)
se_hotelsystem_RoomReservation_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='se_extra', type=StringType)})
se_hotelsystem_RoomReservation_m_checkIn: Method = Method(name="checkIn", parameters={})
se_hotelsystem_RoomReservation_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='se_nrOfNights', type=StringType)}, type=FloatType)
se_hotelsystem_RoomReservation.attributes={se_hotelsystem_RoomReservation_endDate, se_hotelsystem_RoomReservation_startDate, se_hotelsystem_RoomReservation_checkInDate, se_hotelsystem_RoomReservation_checkOuDate}
se_hotelsystem_RoomReservation.methods={se_hotelsystem_RoomReservation_m_checkOut, se_hotelsystem_RoomReservation_m_checkIn, se_hotelsystem_RoomReservation_m_getRoomId, se_hotelsystem_RoomReservation_m_addExtra, se_hotelsystem_RoomReservation_m_getRoomIfOccupied}

# bankcomponents_ICustomerProvides class attributes and methods

# se_hotelsystem_IRoomHandler class attributes and methods
se_hotelsystem_IRoomHandler_m_getAllRoomTypes: Method = Method(name="getAllRoomTypes", parameters={Parameter(name='se_nrOfBeds', type=StringType)}, type=StringType)
se_hotelsystem_IRoomHandler_m_getFreeRooms: Method = Method(name="getFreeRooms", parameters={}, type=IntegerType)
se_hotelsystem_IRoomHandler_m_getAllRoomsByType: Method = Method(name="getAllRoomsByType", parameters={Parameter(name='se_roomType', type=StringType)}, type=StringType)
se_hotelsystem_IRoomHandler_m_getRoomType: Method = Method(name="getRoomType", parameters={Parameter(name='se_roomTypeName', type=StringType)}, type=StringType)
se_hotelsystem_IRoomHandler_m_getFreeRoomByType: Method = Method(name="getFreeRoomByType", parameters={Parameter(name='se_roomType', type=StringType)}, type=StringType)
se_hotelsystem_IRoomHandler_m_getAllRooms: Method = Method(name="getAllRooms", parameters={}, type=StringType)
se_hotelsystem_IRoomHandler.methods={se_hotelsystem_IRoomHandler_m_getAllRooms, se_hotelsystem_IRoomHandler_m_getFreeRoomByType, se_hotelsystem_IRoomHandler_m_getAllRoomTypes, se_hotelsystem_IRoomHandler_m_getAllRoomsByType, se_hotelsystem_IRoomHandler_m_getRoomType, se_hotelsystem_IRoomHandler_m_getFreeRooms}

# se_hotelsystem_IHotelReceptionistProvides class attributes and methods
se_hotelsystem_IHotelReceptionistProvides_m_editBookingTime: Method = Method(name="editBookingTime", parameters={Parameter(name='se_startDate', type=StringType), Parameter(name='se_endDate', type=StringType), Parameter(name='se_reservationId', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_addRoomTypeToBooking: Method = Method(name="addRoomTypeToBooking", parameters={Parameter(name='se_numberOfRoomsForType', type=StringType), Parameter(name='se_roomTypeName', type=StringType), Parameter(name='se_bookingId', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='se_bookingId', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_listBookings: Method = Method(name="listBookings", parameters={}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listOccupiedRooms: Method = Method(name="listOccupiedRooms", parameters={Parameter(name='se_date', type=StringType)}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listCheckins: Method = Method(name="listCheckins", parameters={Parameter(name='se_startDate', type=StringType), Parameter(name='se_endDate', type=StringType)}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listCheckouts: Method = Method(name="listCheckouts", parameters={Parameter(name='se_startDate', type=StringType), Parameter(name='se_endDate', type=StringType)}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_addExtraToRoom: Method = Method(name="addExtraToRoom", parameters={Parameter(name='se_extraDescription', type=StringType), Parameter(name='se_roomNumber', type=StringType), Parameter(name='se_bookingId', type=StringType), Parameter(name='se_price', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_getFreeRoom: Method = Method(name="getFreeRoom", parameters={Parameter(name='se_endDate', type=StringType), Parameter(name='se_roomType', type=StringType), Parameter(name='se_startDate', type=StringType)}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_removeRoomTypeFromBooking: Method = Method(name="removeRoomTypeFromBooking", parameters={Parameter(name='se_roomType', type=StringType), Parameter(name='se_bookingId', type=StringType), Parameter(name='se_nbrToRemove', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_listFreeRooms: Method = Method(name="listFreeRooms", parameters={Parameter(name='se_bookingId', type=StringType)}, type=IntegerType)
se_hotelsystem_IHotelReceptionistProvides_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='se_roomNumbers', type=StringType), Parameter(name='se_bookingId', type=StringType)}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides.methods={se_hotelsystem_IHotelReceptionistProvides_m_listFreeRooms, se_hotelsystem_IHotelReceptionistProvides_m_removeRoomTypeFromBooking, se_hotelsystem_IHotelReceptionistProvides_m_checkIn, se_hotelsystem_IHotelReceptionistProvides_m_listBookings, se_hotelsystem_IHotelReceptionistProvides_m_getFreeRoom, se_hotelsystem_IHotelReceptionistProvides_m_editBookingTime, se_hotelsystem_IHotelReceptionistProvides_m_addRoomTypeToBooking, se_hotelsystem_IHotelReceptionistProvides_m_listCheckins, se_hotelsystem_IHotelReceptionistProvides_m_addExtraToRoom, se_hotelsystem_IHotelReceptionistProvides_m_listOccupiedRooms, se_hotelsystem_IHotelReceptionistProvides_m_cancelBooking, se_hotelsystem_IHotelReceptionistProvides_m_listCheckouts}

# se_hotelsystem_Bill class attributes and methods
se_hotelsystem_Bill_price: Property = Property(name="price", type=FloatType)
se_hotelsystem_Bill_billID: Property = Property(name="billID", type=IntegerType)
se_hotelsystem_Bill.attributes={se_hotelsystem_Bill_billID, se_hotelsystem_Bill_price}

# se_hotelsystem_PaymentHandler class attributes and methods
se_hotelsystem_PaymentHandler_m_payIfCardValid: Method = Method(name="payIfCardValid", parameters={Parameter(name='se_sum', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_expiryYear', type=StringType)}, type=BooleanType)
se_hotelsystem_PaymentHandler.methods={se_hotelsystem_PaymentHandler_m_payIfCardValid}

# se_hotelsystem_IHotelCustomerProvides class attributes and methods
se_hotelsystem_IHotelCustomerProvides_m_getFreeRooms: Method = Method(name="getFreeRooms", parameters={Parameter(name='se_endDate', type=StringType), Parameter(name='se_startDate', type=StringType), Parameter(name='se_numBeds', type=StringType)}, type=StringType)
se_hotelsystem_IHotelCustomerProvides_m_initiateBooking: Method = Method(name="initiateBooking", parameters={Parameter(name='se_firstName', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_startDate', type=StringType), Parameter(name='se_endDate', type=StringType)}, type=IntegerType)
se_hotelsystem_IHotelCustomerProvides_m_initiateRoomCheckout: Method = Method(name="initiateRoomCheckout", parameters={Parameter(name='se_bookingId', type=StringType), Parameter(name='se_roomNumber', type=StringType)}, type=FloatType)
se_hotelsystem_IHotelCustomerProvides_m_payRoomDuringCheckout: Method = Method(name="payRoomDuringCheckout", parameters={Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_roomNumber', type=StringType), Parameter(name='se_expiryYear', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_firstName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_checkInRoom: Method = Method(name="checkInRoom", parameters={Parameter(name='se_bookindId', type=StringType), Parameter(name='se_roomTypeName', type=StringType)}, type=IntegerType)
se_hotelsystem_IHotelCustomerProvides_m_addRoomToBooking: Method = Method(name="addRoomToBooking", parameters={Parameter(name='se_bookingID', type=StringType), Parameter(name='se_roomTypeName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='se_bookingID', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_initiateCheckout: Method = Method(name="initiateCheckout", parameters={Parameter(name='se_bookingID', type=StringType)}, type=FloatType)
se_hotelsystem_IHotelCustomerProvides_m_payDuringCheckout: Method = Method(name="payDuringCheckout", parameters={Parameter(name='se_ccv', type=StringType), Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_expiryYear', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides.methods={se_hotelsystem_IHotelCustomerProvides_m_initiateRoomCheckout, se_hotelsystem_IHotelCustomerProvides_m_addRoomToBooking, se_hotelsystem_IHotelCustomerProvides_m_payRoomDuringCheckout, se_hotelsystem_IHotelCustomerProvides_m_getFreeRooms, se_hotelsystem_IHotelCustomerProvides_m_checkInRoom, se_hotelsystem_IHotelCustomerProvides_m_payDuringCheckout, se_hotelsystem_IHotelCustomerProvides_m_confirmBooking, se_hotelsystem_IHotelCustomerProvides_m_initiateCheckout, se_hotelsystem_IHotelCustomerProvides_m_initiateBooking}

# se_hotelsystem_FreeRoomTypesDTO class attributes and methods
se_hotelsystem_FreeRoomTypesDTO_roomTypeDescription: Property = Property(name="roomTypeDescription", type=StringType)
se_hotelsystem_FreeRoomTypesDTO_numBeds: Property = Property(name="numBeds", type=IntegerType)
se_hotelsystem_FreeRoomTypesDTO_pricePerNight: Property = Property(name="pricePerNight", type=FloatType)
se_hotelsystem_FreeRoomTypesDTO_numFreeRooms: Property = Property(name="numFreeRooms", type=IntegerType)
se_hotelsystem_FreeRoomTypesDTO.attributes={se_hotelsystem_FreeRoomTypesDTO_numBeds, se_hotelsystem_FreeRoomTypesDTO_roomTypeDescription, se_hotelsystem_FreeRoomTypesDTO_pricePerNight, se_hotelsystem_FreeRoomTypesDTO_numFreeRooms}

# se_hotelsystem_RoomHandler class attributes and methods
se_hotelsystem_RoomHandler_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=StringType)
se_hotelsystem_RoomHandler_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='se_numberOfRooms', type=StringType)})
se_hotelsystem_RoomHandler.methods={se_hotelsystem_RoomHandler_m_initialize, se_hotelsystem_RoomHandler_m_getRoom}

# hotelsystem_IHotelAdministratorProvides class attributes and methods

# se_hotelsystem_IHotelAdministratorProvides class attributes and methods
se_hotelsystem_IHotelAdministratorProvides_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_blockRoom: Method = Method(name="blockRoom", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_unblockRoom: Method = Method(name="unblockRoom", parameters={Parameter(name='se_roomNumber', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='se_featureDescription', type=StringType), Parameter(name='se_price', type=StringType), Parameter(name='se_roomTypeName', type=StringType), Parameter(name='se_nbrOfBeds', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='se_price', type=StringType), Parameter(name='se_nbrOfBeds', type=StringType), Parameter(name='se_featuresDescription', type=StringType), Parameter(name='se_roomTypeName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='se_roomTypeName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_changeRoomType: Method = Method(name="changeRoomType", parameters={Parameter(name='se_roomNumber', type=StringType), Parameter(name='se_roomTypeName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='se_roomNumber', type=StringType), Parameter(name='se_roomTypeName', type=StringType)}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides.methods={se_hotelsystem_IHotelAdministratorProvides_m_unblockRoom, se_hotelsystem_IHotelAdministratorProvides_m_editRoomType, se_hotelsystem_IHotelAdministratorProvides_m_changeRoomType, se_hotelsystem_IHotelAdministratorProvides_m_addRoom, se_hotelsystem_IHotelAdministratorProvides_m_removeRoom, se_hotelsystem_IHotelAdministratorProvides_m_blockRoom, se_hotelsystem_IHotelAdministratorProvides_m_removeRoomType, se_hotelsystem_IHotelAdministratorProvides_m_addRoomType}

# se_hotelsystem_IHotelStartupProvides class attributes and methods
se_hotelsystem_IHotelStartupProvides_m_startup: Method = Method(name="startup", parameters={Parameter(name='se_numRooms', type=StringType)})
se_hotelsystem_IHotelStartupProvides.methods={se_hotelsystem_IHotelStartupProvides_m_startup}

# se_hotelsystem_HotelInitializer class attributes and methods

# IHotelStartupProvides class attributes and methods

# hotelsystem_RoomHandler class attributes and methods

# se_bankcomponents_BankAdministrator class attributes and methods

# IAdministratorProvides class attributes and methods

# se_bankcomponents_IAdministratorProvides class attributes and methods
se_bankcomponents_IAdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='se_lastName', type=StringType), Parameter(name='se_sum', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_expiryYear', type=StringType)}, type=FloatType)
se_bankcomponents_IAdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='se_expiryYear', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_ccNumber', type=StringType)}, type=BooleanType)
se_bankcomponents_IAdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='se_lastName', type=StringType), Parameter(name='se_expiryYear', type=StringType), Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_firstName', type=StringType)}, type=BooleanType)
se_bankcomponents_IAdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_expiryYear', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_expiryMonth', type=StringType)}, type=FloatType)
se_bankcomponents_IAdministratorProvides.methods={se_bankcomponents_IAdministratorProvides_m_removeCreditCard, se_bankcomponents_IAdministratorProvides_m_makeDeposit, se_bankcomponents_IAdministratorProvides_m_addCreditCard, se_bankcomponents_IAdministratorProvides_m_getBalance}

# se_actor_User class attributes and methods

# se_actor_Receptionist class attributes and methods

# User class attributes and methods

# se_actor_Administrator class attributes and methods

# hotelsystem_IHotelStartupProvides class attributes and methods

# se_bankcomponents_ICustomerProvides class attributes and methods
se_bankcomponents_ICustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_ccNumber', type=StringType), Parameter(name='se_expiryYear', type=StringType)}, type=BooleanType)
se_bankcomponents_ICustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='se_expiryYear', type=StringType), Parameter(name='se_ccv', type=StringType), Parameter(name='se_sum', type=StringType), Parameter(name='se_expiryMonth', type=StringType), Parameter(name='se_lastName', type=StringType), Parameter(name='se_firstName', type=StringType), Parameter(name='se_ccNumber', type=StringType)}, type=BooleanType)
se_bankcomponents_ICustomerProvides.methods={se_bankcomponents_ICustomerProvides_m_makePayment, se_bankcomponents_ICustomerProvides_m_isCreditCardValid}

# Relationships
bookings0: BinaryAssociation = BinaryAssociation(
    name="bookings0",
    ends={
        Property(name="hotelsystem_Booking", type=se_hotelsystem_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_BookingHandler", type=hotelsystem_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
paymentHandler1: BinaryAssociation = BinaryAssociation(
    name="paymentHandler1",
    ends={
        Property(name="hotelsystem_PaymentHandler", type=se_hotelsystem_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_BookingHandler2", type=hotelsystem_PaymentHandler, multiplicity=Multiplicity(1, 1))
    }
)
roomhandler3: BinaryAssociation = BinaryAssociation(
    name="roomhandler3",
    ends={
        Property(name="hotelsystem_IRoomHandler", type=se_hotelsystem_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_BookingHandler4", type=hotelsystem_IRoomHandler, multiplicity=Multiplicity(1, 1))
    }
)
customer5: BinaryAssociation = BinaryAssociation(
    name="customer5",
    ends={
        Property(name="hotelsystem_Customer", type=se_hotelsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Booking", type=hotelsystem_Customer, multiplicity=Multiplicity(1, 1))
    }
)
roomReservations6: BinaryAssociation = BinaryAssociation(
    name="roomReservations6",
    ends={
        Property(name="hotelsystem_RoomReservation", type=se_hotelsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Booking7", type=hotelsystem_RoomReservation, multiplicity=Multiplicity(0, 9999))
    }
)
roomType10: BinaryAssociation = BinaryAssociation(
    name="roomType10",
    ends={
        Property(name="hotelsystem_RoomType", type=se_hotelsystem_RoomReservation, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_RoomReservation", type=hotelsystem_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
roomExtras11: BinaryAssociation = BinaryAssociation(
    name="roomExtras11",
    ends={
        Property(name="hotelsystem_RoomExtra", type=se_hotelsystem_RoomReservation, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_RoomReservation12", type=hotelsystem_RoomExtra, multiplicity=Multiplicity(0, 9999))
    }
)
room13: BinaryAssociation = BinaryAssociation(
    name="room13",
    ends={
        Property(name="hotelsystem_Room", type=se_hotelsystem_RoomReservation, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_RoomReservation14", type=hotelsystem_Room, multiplicity=Multiplicity(0, 1))
    }
)
roomtype15: BinaryAssociation = BinaryAssociation(
    name="roomtype15",
    ends={
        Property(name="hotelsystem_RoomType16", type=se_hotelsystem_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Room", type=hotelsystem_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
bills8: BinaryAssociation = BinaryAssociation(
    name="bills8",
    ends={
        Property(name="hotelsystem_Bill", type=se_hotelsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Booking9", type=hotelsystem_Bill, multiplicity=Multiplicity(0, 9999))
    }
)
bankingComponent19: BinaryAssociation = BinaryAssociation(
    name="bankingComponent19",
    ends={
        Property(name="bankcomponents_ICustomerProvides", type=se_hotelsystem_PaymentHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_PaymentHandler", type=bankcomponents_ICustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
roomreservation17: BinaryAssociation = BinaryAssociation(
    name="roomreservation17",
    ends={
        Property(name="hotelsystem_RoomReservation18", type=se_hotelsystem_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Bill", type=hotelsystem_RoomReservation, multiplicity=Multiplicity(1, 1))
    }
)
roomTypes20: BinaryAssociation = BinaryAssociation(
    name="roomTypes20",
    ends={
        Property(name="hotelsystem_RoomType21", type=se_hotelsystem_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_RoomHandler", type=hotelsystem_RoomType, multiplicity=Multiplicity(0, 9999))
    }
)
rooms22: BinaryAssociation = BinaryAssociation(
    name="rooms22",
    ends={
        Property(name="hotelsystem_Room24", type=se_hotelsystem_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_RoomHandler23", type=hotelsystem_Room, multiplicity=Multiplicity(0, 9999))
    }
)
roomHandler25: BinaryAssociation = BinaryAssociation(
    name="roomHandler25",
    ends={
        Property(name="hotelsystem_RoomHandler", type=se_hotelsystem_HotelInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_HotelInitializer", type=hotelsystem_RoomHandler, multiplicity=Multiplicity(1, 1))
    }
)
ireceptionistprovides26: BinaryAssociation = BinaryAssociation(
    name="ireceptionistprovides26",
    ends={
        Property(name="hotelsystem_IHotelReceptionistProvides", type=se_actor_Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="se_actor_Receptionist", type=hotelsystem_IHotelReceptionistProvides, multiplicity=Multiplicity(1, 1))
    }
)
ihotelcustomerprovides27: BinaryAssociation = BinaryAssociation(
    name="ihotelcustomerprovides27",
    ends={
        Property(name="hotelsystem_IHotelCustomerProvides", type=se_actor_Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="se_actor_Receptionist28", type=hotelsystem_IHotelCustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
iadministratorprovides29: BinaryAssociation = BinaryAssociation(
    name="iadministratorprovides29",
    ends={
        Property(name="hotelsystem_IHotelAdministratorProvides", type=se_actor_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="se_actor_Administrator", type=hotelsystem_IHotelAdministratorProvides, multiplicity=Multiplicity(1, 1))
    }
)
ihotelstartupprovides30: BinaryAssociation = BinaryAssociation(
    name="ihotelstartupprovides30",
    ends={
        Property(name="hotelsystem_IHotelStartupProvides", type=se_actor_Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="se_actor_Administrator31", type=hotelsystem_IHotelStartupProvides, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_se_hotelsystem_BookingHandler_hotelsystem_IHotelReceptionistProvides = Generalization(general=hotelsystem_IHotelReceptionistProvides, specific=se_hotelsystem_BookingHandler)
gen_se_hotelsystem_BookingHandler_hotelsystem_IHotelCustomerProvides = Generalization(general=hotelsystem_IHotelCustomerProvides, specific=se_hotelsystem_BookingHandler)
gen_se_hotelsystem_RoomHandler_hotelsystem_IRoomHandler = Generalization(general=hotelsystem_IRoomHandler, specific=se_hotelsystem_RoomHandler)
gen_se_hotelsystem_RoomHandler_hotelsystem_IHotelAdministratorProvides = Generalization(general=hotelsystem_IHotelAdministratorProvides, specific=se_hotelsystem_RoomHandler)
gen_se_hotelsystem_HotelInitializer_IHotelStartupProvides = Generalization(general=IHotelStartupProvides, specific=se_hotelsystem_HotelInitializer)
gen_se_bankcomponents_BankAdministrator_IAdministratorProvides = Generalization(general=IAdministratorProvides, specific=se_bankcomponents_BankAdministrator)
gen_se_actor_Receptionist_User = Generalization(general=User, specific=se_actor_Receptionist)
gen_se_actor_Administrator_User = Generalization(general=User, specific=se_actor_Administrator)

# Domain Model
domain_model = DomainModel(
    name="se",
    types={hotelsystem_Booking, hotelsystem_PaymentHandler, hotelsystem_IRoomHandler, se_hotelsystem_Booking, hotelsystem_Customer, hotelsystem_RoomReservation, se_hotelsystem_BookingHandler, hotelsystem_IHotelReceptionistProvides, hotelsystem_IHotelCustomerProvides, hotelsystem_RoomType, hotelsystem_RoomExtra, hotelsystem_Room, se_hotelsystem_RoomType, se_hotelsystem_RoomExtra, se_hotelsystem_Room, hotelsystem_Bill, se_hotelsystem_Customer, se_hotelsystem_RoomReservation, bankcomponents_ICustomerProvides, se_hotelsystem_IRoomHandler, se_hotelsystem_IHotelReceptionistProvides, se_hotelsystem_Bill, se_hotelsystem_PaymentHandler, se_hotelsystem_IHotelCustomerProvides, se_hotelsystem_FreeRoomTypesDTO, se_hotelsystem_RoomHandler, hotelsystem_IHotelAdministratorProvides, se_hotelsystem_IHotelAdministratorProvides, se_hotelsystem_IHotelStartupProvides, se_hotelsystem_HotelInitializer, IHotelStartupProvides, hotelsystem_RoomHandler, se_bankcomponents_BankAdministrator, IAdministratorProvides, se_bankcomponents_IAdministratorProvides, se_actor_User, se_actor_Receptionist, User, se_actor_Administrator, hotelsystem_IHotelStartupProvides, se_bankcomponents_ICustomerProvides},
    associations={bookings0, paymentHandler1, roomhandler3, customer5, roomReservations6, roomType10, roomExtras11, room13, roomtype15, bills8, bankingComponent19, roomreservation17, roomTypes20, rooms22, roomHandler25, ireceptionistprovides26, ihotelcustomerprovides27, iadministratorprovides29, ihotelstartupprovides30},
    generalizations={gen_se_hotelsystem_BookingHandler_hotelsystem_IHotelReceptionistProvides, gen_se_hotelsystem_BookingHandler_hotelsystem_IHotelCustomerProvides, gen_se_hotelsystem_RoomHandler_hotelsystem_IRoomHandler, gen_se_hotelsystem_RoomHandler_hotelsystem_IHotelAdministratorProvides, gen_se_hotelsystem_HotelInitializer_IHotelStartupProvides, gen_se_bankcomponents_BankAdministrator_IAdministratorProvides, gen_se_actor_Receptionist_User, gen_se_actor_Administrator_User},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)