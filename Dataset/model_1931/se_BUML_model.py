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
se_hotelsystem_BookingHandler = Class(name="se::hotelsystem::BookingHandler")
hotelsystem_IHotelReceptionistProvides = Class(name="hotelsystem::IHotelReceptionistProvides")
hotelsystem_IHotelCustomerProvides = Class(name="hotelsystem::IHotelCustomerProvides")
hotelsystem_Booking = Class(name="hotelsystem::Booking")
hotelsystem_PaymentHandler = Class(name="hotelsystem::PaymentHandler")
hotelsystem_IRoomHandler = Class(name="hotelsystem::IRoomHandler")
se_hotelsystem_Booking = Class(name="se::hotelsystem::Booking")
hotelsystem_Bill = Class(name="hotelsystem::Bill")
hotelsystem_Customer = Class(name="hotelsystem::Customer")
hotelsystem_RoomReservation = Class(name="hotelsystem::RoomReservation")
se_hotelsystem_Customer = Class(name="se::hotelsystem::Customer")
se_hotelsystem_RoomReservation = Class(name="se::hotelsystem::RoomReservation")
hotelsystem_RoomType = Class(name="hotelsystem::RoomType")
hotelsystem_RoomExtra = Class(name="hotelsystem::RoomExtra")
hotelsystem_Room = Class(name="hotelsystem::Room")
se_hotelsystem_RoomType = Class(name="se::hotelsystem::RoomType")
se_hotelsystem_Bill = Class(name="se::hotelsystem::Bill")
se_hotelsystem_RoomExtra = Class(name="se::hotelsystem::RoomExtra")
se_hotelsystem_Room = Class(name="se::hotelsystem::Room")
se_hotelsystem_IRoomHandler = Class(name="se::hotelsystem::IRoomHandler", is_abstract=True)
se_hotelsystem_PaymentHandler = Class(name="se::hotelsystem::PaymentHandler")
bankcomponents_ICustomerProvides = Class(name="bankcomponents::ICustomerProvides")
se_hotelsystem_IHotelReceptionistProvides = Class(name="se::hotelsystem::IHotelReceptionistProvides", is_abstract=True)
se_hotelsystem_IHotelCustomerProvides = Class(name="se::hotelsystem::IHotelCustomerProvides", is_abstract=True)
se_hotelsystem_FreeRoomTypesDTO = Class(name="se::hotelsystem::FreeRoomTypesDTO")
se_hotelsystem_RoomHandler = Class(name="se::hotelsystem::RoomHandler")
hotelsystem_IHotelAdministratorProvides = Class(name="hotelsystem::IHotelAdministratorProvides")
se_hotelsystem_IHotelAdministratorProvides = Class(name="se::hotelsystem::IHotelAdministratorProvides", is_abstract=True)
se_hotelsystem_HotelInitializer = Class(name="se::hotelsystem::HotelInitializer")
IHotelStartupProvides = Class(name="IHotelStartupProvides")
hotelsystem_RoomHandler = Class(name="hotelsystem::RoomHandler")
se_bankcomponents_BankAdministrator = Class(name="se::bankcomponents::BankAdministrator")
IAdministratorProvides = Class(name="IAdministratorProvides")
se_bankcomponents_IAdministratorProvides = Class(name="se::bankcomponents::IAdministratorProvides", is_abstract=True)
se_hotelsystem_IHotelStartupProvides = Class(name="se::hotelsystem::IHotelStartupProvides", is_abstract=True)
se_bankcomponents_ICustomerProvides = Class(name="se::bankcomponents::ICustomerProvides", is_abstract=True)
se_actor_User = Class(name="se::actor::User")
se_actor_Receptionist = Class(name="se::actor::Receptionist")
User = Class(name="User")
hotelsystem_IHotelStartupProvides = Class(name="hotelsystem::IHotelStartupProvides")
se_actor_Administrator = Class(name="se::actor::Administrator")

# se_hotelsystem_BookingHandler class attributes and methods
se_hotelsystem_BookingHandler_bookingCurrentlyCheckingOut: Property = Property(name="bookingCurrentlyCheckingOut", type=IntegerType)
se_hotelsystem_BookingHandler_nextBookingId: Property = Property(name="nextBookingId", type=IntegerType)
se_hotelsystem_BookingHandler_m_getBookingById: Method = Method(name="getBookingById", parameters={Parameter(name='bookingId')}, type=StringType)
se_hotelsystem_BookingHandler_m_isFree: Method = Method(name="isFree", parameters={Parameter(name='startDate'), Parameter(name='roomId'), Parameter(name='endDate')}, type=BooleanType)
se_hotelsystem_BookingHandler.attributes={se_hotelsystem_BookingHandler_nextBookingId, se_hotelsystem_BookingHandler_bookingCurrentlyCheckingOut}
se_hotelsystem_BookingHandler.methods={se_hotelsystem_BookingHandler_m_isFree, se_hotelsystem_BookingHandler_m_getBookingById}

# hotelsystem_IHotelReceptionistProvides class attributes and methods

# hotelsystem_IHotelCustomerProvides class attributes and methods

# hotelsystem_Booking class attributes and methods

# hotelsystem_PaymentHandler class attributes and methods

# hotelsystem_IRoomHandler class attributes and methods

# se_hotelsystem_Booking class attributes and methods
se_hotelsystem_Booking_canceled: Property = Property(name="canceled", type=BooleanType)
se_hotelsystem_Booking_bookingId: Property = Property(name="bookingId", type=IntegerType)
se_hotelsystem_Booking_startDate: Property = Property(name="startDate", type=StringType)
se_hotelsystem_Booking_endDate: Property = Property(name="endDate", type=StringType)
se_hotelsystem_Booking_confirmed: Property = Property(name="confirmed", type=BooleanType)
se_hotelsystem_Booking_m_getOccupiedRooms: Method = Method(name="getOccupiedRooms", parameters={Parameter(name='date')}, type=StringType)
se_hotelsystem_Booking_m_checkOut: Method = Method(name="checkOut", parameters={}, type=FloatType)
se_hotelsystem_Booking_m_cancel: Method = Method(name="cancel", parameters={})
se_hotelsystem_Booking_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='extra'), Parameter(name='roomNbr')}, type=BooleanType)
se_hotelsystem_Booking_m_nrOfNights: Method = Method(name="nrOfNights", parameters={}, type=IntegerType)
se_hotelsystem_Booking_m_isCheckedIn: Method = Method(name="isCheckedIn", parameters={}, type=BooleanType)
se_hotelsystem_Booking_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='room')}, type=BooleanType)
se_hotelsystem_Booking_m_getBookingPrice: Method = Method(name="getBookingPrice", parameters={}, type=FloatType)
se_hotelsystem_Booking_m_getRoomPrice: Method = Method(name="getRoomPrice", parameters={Parameter(name='roomNumber')}, type=FloatType)
se_hotelsystem_Booking_m_isFree: Method = Method(name="isFree", parameters={Parameter(name='endDate'), Parameter(name='startDate'), Parameter(name='roomId')}, type=BooleanType)
se_hotelsystem_Booking_m_checkOutRoom: Method = Method(name="checkOutRoom", parameters={Parameter(name='roomNumber')}, type=FloatType)
se_hotelsystem_Booking.attributes={se_hotelsystem_Booking_canceled, se_hotelsystem_Booking_bookingId, se_hotelsystem_Booking_confirmed, se_hotelsystem_Booking_startDate, se_hotelsystem_Booking_endDate}
se_hotelsystem_Booking.methods={se_hotelsystem_Booking_m_isFree, se_hotelsystem_Booking_m_getRoomPrice, se_hotelsystem_Booking_m_checkOutRoom, se_hotelsystem_Booking_m_isCheckedIn, se_hotelsystem_Booking_m_checkOut, se_hotelsystem_Booking_m_nrOfNights, se_hotelsystem_Booking_m_getOccupiedRooms, se_hotelsystem_Booking_m_cancel, se_hotelsystem_Booking_m_checkIn, se_hotelsystem_Booking_m_addExtra, se_hotelsystem_Booking_m_getBookingPrice}

# hotelsystem_Bill class attributes and methods

# hotelsystem_Customer class attributes and methods

# hotelsystem_RoomReservation class attributes and methods

# se_hotelsystem_Customer class attributes and methods
se_hotelsystem_Customer_firstName: Property = Property(name="firstName", type=StringType)
se_hotelsystem_Customer_lastName: Property = Property(name="lastName", type=StringType)
se_hotelsystem_Customer.attributes={se_hotelsystem_Customer_firstName, se_hotelsystem_Customer_lastName}

# se_hotelsystem_RoomReservation class attributes and methods
se_hotelsystem_RoomReservation_startDate: Property = Property(name="startDate", type=StringType)
se_hotelsystem_RoomReservation_endDate: Property = Property(name="endDate", type=StringType)
se_hotelsystem_RoomReservation_checkInDate: Property = Property(name="checkInDate", type=StringType)
se_hotelsystem_RoomReservation_checkOuDate: Property = Property(name="checkOuDate", type=StringType)
se_hotelsystem_RoomReservation_m_getRoomId: Method = Method(name="getRoomId", parameters={}, type=IntegerType)
se_hotelsystem_RoomReservation_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='extra')})
se_hotelsystem_RoomReservation_m_checkIn: Method = Method(name="checkIn", parameters={})
se_hotelsystem_RoomReservation_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='nrOfNights')}, type=FloatType)
se_hotelsystem_RoomReservation_m_getRoomIfOccupied: Method = Method(name="getRoomIfOccupied", parameters={Parameter(name='date')}, type=StringType)
se_hotelsystem_RoomReservation.attributes={se_hotelsystem_RoomReservation_startDate, se_hotelsystem_RoomReservation_checkInDate, se_hotelsystem_RoomReservation_checkOuDate, se_hotelsystem_RoomReservation_endDate}
se_hotelsystem_RoomReservation.methods={se_hotelsystem_RoomReservation_m_addExtra, se_hotelsystem_RoomReservation_m_checkIn, se_hotelsystem_RoomReservation_m_getRoomId, se_hotelsystem_RoomReservation_m_checkOut, se_hotelsystem_RoomReservation_m_getRoomIfOccupied}

# hotelsystem_RoomType class attributes and methods

# hotelsystem_RoomExtra class attributes and methods

# hotelsystem_Room class attributes and methods

# se_hotelsystem_RoomType class attributes and methods
se_hotelsystem_RoomType_description: Property = Property(name="description", type=StringType)
se_hotelsystem_RoomType_numBeds: Property = Property(name="numBeds", type=IntegerType)
se_hotelsystem_RoomType_pricePerNight: Property = Property(name="pricePerNight", type=FloatType)
se_hotelsystem_RoomType_name: Property = Property(name="name", type=StringType)
se_hotelsystem_RoomType.attributes={se_hotelsystem_RoomType_description, se_hotelsystem_RoomType_pricePerNight, se_hotelsystem_RoomType_name, se_hotelsystem_RoomType_numBeds}

# se_hotelsystem_Bill class attributes and methods
se_hotelsystem_Bill_price: Property = Property(name="price", type=FloatType)
se_hotelsystem_Bill_billID: Property = Property(name="billID", type=IntegerType)
se_hotelsystem_Bill.attributes={se_hotelsystem_Bill_price, se_hotelsystem_Bill_billID}

# se_hotelsystem_RoomExtra class attributes and methods
se_hotelsystem_RoomExtra_price: Property = Property(name="price", type=FloatType)
se_hotelsystem_RoomExtra_description: Property = Property(name="description", type=StringType)
se_hotelsystem_RoomExtra.attributes={se_hotelsystem_RoomExtra_description, se_hotelsystem_RoomExtra_price}

# se_hotelsystem_Room class attributes and methods
se_hotelsystem_Room_occupied: Property = Property(name="occupied", type=BooleanType)
se_hotelsystem_Room_blocked: Property = Property(name="blocked", type=BooleanType)
se_hotelsystem_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
se_hotelsystem_Room.attributes={se_hotelsystem_Room_occupied, se_hotelsystem_Room_roomNumber, se_hotelsystem_Room_blocked}

# se_hotelsystem_IRoomHandler class attributes and methods
se_hotelsystem_IRoomHandler_m_getAllRoomTypes: Method = Method(name="getAllRoomTypes", parameters={Parameter(name='nrOfBeds')}, type=StringType)
se_hotelsystem_IRoomHandler_m_getFreeRooms: Method = Method(name="getFreeRooms", parameters={}, type=IntegerType)
se_hotelsystem_IRoomHandler_m_getAllRoomsByType: Method = Method(name="getAllRoomsByType", parameters={Parameter(name='roomType')}, type=StringType)
se_hotelsystem_IRoomHandler_m_getRoomType: Method = Method(name="getRoomType", parameters={Parameter(name='roomTypeName')}, type=StringType)
se_hotelsystem_IRoomHandler_m_getFreeRoomByType: Method = Method(name="getFreeRoomByType", parameters={Parameter(name='roomType')}, type=StringType)
se_hotelsystem_IRoomHandler_m_getAllRooms: Method = Method(name="getAllRooms", parameters={}, type=StringType)
se_hotelsystem_IRoomHandler.methods={se_hotelsystem_IRoomHandler_m_getFreeRoomByType, se_hotelsystem_IRoomHandler_m_getAllRooms, se_hotelsystem_IRoomHandler_m_getFreeRooms, se_hotelsystem_IRoomHandler_m_getAllRoomTypes, se_hotelsystem_IRoomHandler_m_getAllRoomsByType, se_hotelsystem_IRoomHandler_m_getRoomType}

# se_hotelsystem_PaymentHandler class attributes and methods
se_hotelsystem_PaymentHandler_m_payIfCardValid: Method = Method(name="payIfCardValid", parameters={Parameter(name='firstName'), Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='ccNumber'), Parameter(name='ccv'), Parameter(name='sum')}, type=BooleanType)
se_hotelsystem_PaymentHandler.methods={se_hotelsystem_PaymentHandler_m_payIfCardValid}

# bankcomponents_ICustomerProvides class attributes and methods

# se_hotelsystem_IHotelReceptionistProvides class attributes and methods
se_hotelsystem_IHotelReceptionistProvides_m_editBookingTime: Method = Method(name="editBookingTime", parameters={Parameter(name='reservationId'), Parameter(name='startDate'), Parameter(name='endDate')}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='roomNumbers'), Parameter(name='bookingId')}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='bookingId')}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_addRoomTypeToBooking: Method = Method(name="addRoomTypeToBooking", parameters={Parameter(name='bookingId'), Parameter(name='numberOfRoomsForType'), Parameter(name='roomTypeName')}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_removeRoomTypeFromBooking: Method = Method(name="removeRoomTypeFromBooking", parameters={Parameter(name='bookingId'), Parameter(name='roomType'), Parameter(name='nbrToRemove')}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_listFreeRooms: Method = Method(name="listFreeRooms", parameters={Parameter(name='bookingId')}, type=IntegerType)
se_hotelsystem_IHotelReceptionistProvides_m_addExtraToRoom: Method = Method(name="addExtraToRoom", parameters={Parameter(name='extraDescription'), Parameter(name='bookingId'), Parameter(name='roomNumber'), Parameter(name='price')}, type=BooleanType)
se_hotelsystem_IHotelReceptionistProvides_m_listBookings: Method = Method(name="listBookings", parameters={}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listOccupiedRooms: Method = Method(name="listOccupiedRooms", parameters={Parameter(name='date')}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listCheckins: Method = Method(name="listCheckins", parameters={Parameter(name='startDate'), Parameter(name='endDate')}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_listCheckouts: Method = Method(name="listCheckouts", parameters={Parameter(name='endDate'), Parameter(name='startDate')}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides_m_getFreeRoom: Method = Method(name="getFreeRoom", parameters={Parameter(name='startDate'), Parameter(name='endDate'), Parameter(name='roomType')}, type=StringType)
se_hotelsystem_IHotelReceptionistProvides.methods={se_hotelsystem_IHotelReceptionistProvides_m_editBookingTime, se_hotelsystem_IHotelReceptionistProvides_m_listCheckouts, se_hotelsystem_IHotelReceptionistProvides_m_listOccupiedRooms, se_hotelsystem_IHotelReceptionistProvides_m_getFreeRoom, se_hotelsystem_IHotelReceptionistProvides_m_addExtraToRoom, se_hotelsystem_IHotelReceptionistProvides_m_removeRoomTypeFromBooking, se_hotelsystem_IHotelReceptionistProvides_m_addRoomTypeToBooking, se_hotelsystem_IHotelReceptionistProvides_m_listCheckins, se_hotelsystem_IHotelReceptionistProvides_m_checkIn, se_hotelsystem_IHotelReceptionistProvides_m_cancelBooking, se_hotelsystem_IHotelReceptionistProvides_m_listFreeRooms, se_hotelsystem_IHotelReceptionistProvides_m_listBookings}

# se_hotelsystem_IHotelCustomerProvides class attributes and methods
se_hotelsystem_IHotelCustomerProvides_m_initiateBooking: Method = Method(name="initiateBooking", parameters={Parameter(name='startDate'), Parameter(name='firstName'), Parameter(name='endDate'), Parameter(name='lastName')}, type=IntegerType)
se_hotelsystem_IHotelCustomerProvides_m_addRoomToBooking: Method = Method(name="addRoomToBooking", parameters={Parameter(name='roomTypeName'), Parameter(name='bookingID')}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_getFreeRooms: Method = Method(name="getFreeRooms", parameters={Parameter(name='startDate'), Parameter(name='numBeds'), Parameter(name='endDate')}, type=StringType)
se_hotelsystem_IHotelCustomerProvides_m_initiateRoomCheckout: Method = Method(name="initiateRoomCheckout", parameters={Parameter(name='bookingId'), Parameter(name='roomNumber')}, type=FloatType)
se_hotelsystem_IHotelCustomerProvides_m_payRoomDuringCheckout: Method = Method(name="payRoomDuringCheckout", parameters={Parameter(name='ccv'), Parameter(name='expiryMonth'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='roomNumber'), Parameter(name='expiryYear')}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='bookingID')}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_initiateCheckout: Method = Method(name="initiateCheckout", parameters={Parameter(name='bookingID')}, type=FloatType)
se_hotelsystem_IHotelCustomerProvides_m_payDuringCheckout: Method = Method(name="payDuringCheckout", parameters={Parameter(name='firstName'), Parameter(name='expiryMonth'), Parameter(name='lastName'), Parameter(name='ccNumber'), Parameter(name='expiryYear'), Parameter(name='ccv')}, type=BooleanType)
se_hotelsystem_IHotelCustomerProvides_m_checkInRoom: Method = Method(name="checkInRoom", parameters={Parameter(name='roomTypeName'), Parameter(name='bookindId')}, type=IntegerType)
se_hotelsystem_IHotelCustomerProvides.methods={se_hotelsystem_IHotelCustomerProvides_m_payDuringCheckout, se_hotelsystem_IHotelCustomerProvides_m_initiateRoomCheckout, se_hotelsystem_IHotelCustomerProvides_m_initiateBooking, se_hotelsystem_IHotelCustomerProvides_m_getFreeRooms, se_hotelsystem_IHotelCustomerProvides_m_checkInRoom, se_hotelsystem_IHotelCustomerProvides_m_initiateCheckout, se_hotelsystem_IHotelCustomerProvides_m_payRoomDuringCheckout, se_hotelsystem_IHotelCustomerProvides_m_addRoomToBooking, se_hotelsystem_IHotelCustomerProvides_m_confirmBooking}

# se_hotelsystem_FreeRoomTypesDTO class attributes and methods
se_hotelsystem_FreeRoomTypesDTO_roomTypeDescription: Property = Property(name="roomTypeDescription", type=StringType)
se_hotelsystem_FreeRoomTypesDTO_numBeds: Property = Property(name="numBeds", type=IntegerType)
se_hotelsystem_FreeRoomTypesDTO_pricePerNight: Property = Property(name="pricePerNight", type=FloatType)
se_hotelsystem_FreeRoomTypesDTO_numFreeRooms: Property = Property(name="numFreeRooms", type=IntegerType)
se_hotelsystem_FreeRoomTypesDTO.attributes={se_hotelsystem_FreeRoomTypesDTO_roomTypeDescription, se_hotelsystem_FreeRoomTypesDTO_pricePerNight, se_hotelsystem_FreeRoomTypesDTO_numFreeRooms, se_hotelsystem_FreeRoomTypesDTO_numBeds}

# se_hotelsystem_RoomHandler class attributes and methods
se_hotelsystem_RoomHandler_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='roomNumber')}, type=StringType)
se_hotelsystem_RoomHandler_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='numberOfRooms')})
se_hotelsystem_RoomHandler.methods={se_hotelsystem_RoomHandler_m_initialize, se_hotelsystem_RoomHandler_m_getRoom}

# hotelsystem_IHotelAdministratorProvides class attributes and methods

# se_hotelsystem_IHotelAdministratorProvides class attributes and methods
se_hotelsystem_IHotelAdministratorProvides_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='price'), Parameter(name='roomTypeName'), Parameter(name='nbrOfBeds'), Parameter(name='featureDescription')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='nbrOfBeds'), Parameter(name='featuresDescription'), Parameter(name='roomTypeName'), Parameter(name='price')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='roomTypeName')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_changeRoomType: Method = Method(name="changeRoomType", parameters={Parameter(name='roomTypeName'), Parameter(name='roomNumber')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='roomNumber'), Parameter(name='roomTypeName')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='roomNumber')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_blockRoom: Method = Method(name="blockRoom", parameters={Parameter(name='roomNumber')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides_m_unblockRoom: Method = Method(name="unblockRoom", parameters={Parameter(name='roomNumber')}, type=BooleanType)
se_hotelsystem_IHotelAdministratorProvides.methods={se_hotelsystem_IHotelAdministratorProvides_m_changeRoomType, se_hotelsystem_IHotelAdministratorProvides_m_addRoom, se_hotelsystem_IHotelAdministratorProvides_m_blockRoom, se_hotelsystem_IHotelAdministratorProvides_m_addRoomType, se_hotelsystem_IHotelAdministratorProvides_m_removeRoom, se_hotelsystem_IHotelAdministratorProvides_m_editRoomType, se_hotelsystem_IHotelAdministratorProvides_m_unblockRoom, se_hotelsystem_IHotelAdministratorProvides_m_removeRoomType}

# se_hotelsystem_HotelInitializer class attributes and methods

# IHotelStartupProvides class attributes and methods

# hotelsystem_RoomHandler class attributes and methods

# se_bankcomponents_BankAdministrator class attributes and methods

# IAdministratorProvides class attributes and methods

# se_bankcomponents_IAdministratorProvides class attributes and methods
se_bankcomponents_IAdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='expiryMonth'), Parameter(name='ccv'), Parameter(name='lastName'), Parameter(name='firstName'), Parameter(name='expiryYear'), Parameter(name='sum'), Parameter(name='ccNumber')}, type=FloatType)
se_bankcomponents_IAdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='expiryYear'), Parameter(name='ccv'), Parameter(name='lastName'), Parameter(name='ccNumber'), Parameter(name='firstName'), Parameter(name='expiryMonth')}, type=BooleanType)
se_bankcomponents_IAdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='ccNumber'), Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='expiryMonth')}, type=BooleanType)
se_bankcomponents_IAdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='ccNumber'), Parameter(name='expiryMonth'), Parameter(name='firstName'), Parameter(name='lastName')}, type=FloatType)
se_bankcomponents_IAdministratorProvides.methods={se_bankcomponents_IAdministratorProvides_m_getBalance, se_bankcomponents_IAdministratorProvides_m_makeDeposit, se_bankcomponents_IAdministratorProvides_m_removeCreditCard, se_bankcomponents_IAdministratorProvides_m_addCreditCard}

# se_hotelsystem_IHotelStartupProvides class attributes and methods
se_hotelsystem_IHotelStartupProvides_m_startup: Method = Method(name="startup", parameters={Parameter(name='numRooms')})
se_hotelsystem_IHotelStartupProvides.methods={se_hotelsystem_IHotelStartupProvides_m_startup}

# se_bankcomponents_ICustomerProvides class attributes and methods
se_bankcomponents_ICustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='ccv'), Parameter(name='sum'), Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='lastName')}, type=BooleanType)
se_bankcomponents_ICustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='lastName'), Parameter(name='expiryMonth'), Parameter(name='ccNumber'), Parameter(name='expiryYear'), Parameter(name='firstName'), Parameter(name='ccv')}, type=BooleanType)
se_bankcomponents_ICustomerProvides.methods={se_bankcomponents_ICustomerProvides_m_isCreditCardValid, se_bankcomponents_ICustomerProvides_m_makePayment}

# se_actor_User class attributes and methods

# se_actor_Receptionist class attributes and methods

# User class attributes and methods

# hotelsystem_IHotelStartupProvides class attributes and methods

# se_actor_Administrator class attributes and methods

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
bills8: BinaryAssociation = BinaryAssociation(
    name="bills8",
    ends={
        Property(name="hotelsystem_Bill", type=se_hotelsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Booking9", type=hotelsystem_Bill, multiplicity=Multiplicity(0, 9999))
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
roomreservation17: BinaryAssociation = BinaryAssociation(
    name="roomreservation17",
    ends={
        Property(name="hotelsystem_RoomReservation18", type=se_hotelsystem_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Bill", type=hotelsystem_RoomReservation, multiplicity=Multiplicity(1, 1))
    }
)
roomtype15: BinaryAssociation = BinaryAssociation(
    name="roomtype15",
    ends={
        Property(name="hotelsystem_RoomType16", type=se_hotelsystem_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_Room", type=hotelsystem_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
bankingComponent19: BinaryAssociation = BinaryAssociation(
    name="bankingComponent19",
    ends={
        Property(name="bankcomponents_ICustomerProvides", type=se_hotelsystem_PaymentHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="se_hotelsystem_PaymentHandler", type=bankcomponents_ICustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
roomTypes20: BinaryAssociation = BinaryAssociation(
    name="roomTypes20",
    ends={
        Property(name="se_hotelsystem_RoomHandler", type=hotelsystem_RoomType, multiplicity=Multiplicity(0, 9999)),
        Property(name="hotelsystem_RoomType21", type=se_hotelsystem_RoomHandler, multiplicity=Multiplicity(1, 1))
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
    types={se_hotelsystem_BookingHandler, hotelsystem_IHotelReceptionistProvides, hotelsystem_IHotelCustomerProvides, hotelsystem_Booking, hotelsystem_PaymentHandler, hotelsystem_IRoomHandler, se_hotelsystem_Booking, hotelsystem_Bill, hotelsystem_Customer, hotelsystem_RoomReservation, se_hotelsystem_Customer, se_hotelsystem_RoomReservation, hotelsystem_RoomType, hotelsystem_RoomExtra, hotelsystem_Room, se_hotelsystem_RoomType, se_hotelsystem_Bill, se_hotelsystem_RoomExtra, se_hotelsystem_Room, se_hotelsystem_IRoomHandler, se_hotelsystem_PaymentHandler, bankcomponents_ICustomerProvides, se_hotelsystem_IHotelReceptionistProvides, se_hotelsystem_IHotelCustomerProvides, se_hotelsystem_FreeRoomTypesDTO, se_hotelsystem_RoomHandler, hotelsystem_IHotelAdministratorProvides, se_hotelsystem_IHotelAdministratorProvides, se_hotelsystem_HotelInitializer, IHotelStartupProvides, hotelsystem_RoomHandler, se_bankcomponents_BankAdministrator, IAdministratorProvides, se_bankcomponents_IAdministratorProvides, se_hotelsystem_IHotelStartupProvides, se_bankcomponents_ICustomerProvides, se_actor_User, se_actor_Receptionist, User, hotelsystem_IHotelStartupProvides, se_actor_Administrator},
    associations={bookings0, paymentHandler1, roomhandler3, customer5, roomReservations6, bills8, roomType10, roomExtras11, room13, roomreservation17, roomtype15, bankingComponent19, roomTypes20, rooms22, roomHandler25, ireceptionistprovides26, ihotelcustomerprovides27, iadministratorprovides29, ihotelstartupprovides30},
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