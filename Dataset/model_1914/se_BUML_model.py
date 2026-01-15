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
EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="CHECK_IN"),
			EnumerationLiteral(name="CHECK_OUT")
    }
)

# Classes
se_bookingSystem_CheckInEvent = Class(name="se::bookingSystem::CheckInEvent")
AbstractEvent = Class(name="AbstractEvent")
se_bookingSystem_AbstractEvent = Class(name="se::bookingSystem::AbstractEvent", is_abstract=True)
IEvent = Class(name="IEvent")
se_bookingSystem_IEvent = Class(name="se::bookingSystem::IEvent", is_abstract=True)
se_bookingSystem_CheckOutEvent = Class(name="se::bookingSystem::CheckOutEvent")
se_bookingSystem_BookingSystem = Class(name="se::bookingSystem::BookingSystem")
bookingSystem_IHotelBookingManager = Class(name="bookingSystem::IHotelBookingManager")
bookingSystem_IHotelCustomerProvides = Class(name="bookingSystem::IHotelCustomerProvides")
bookingSystem_IEvent = Class(name="bookingSystem::IEvent")
bookingSystem_IBooking = Class(name="bookingSystem::IBooking")
roomManager_IHotelRoomProvider = Class(name="roomManager::IHotelRoomProvider")
roomManager_IRoom = Class(name="roomManager::IRoom")
se_bookingSystem_IBooking = Class(name="se::bookingSystem::IBooking", is_abstract=True)
se_bookingSystem_IHotelBookingManager = Class(name="se::bookingSystem::IHotelBookingManager", is_abstract=True)
IHotelCustomerProvides = Class(name="IHotelCustomerProvides")
se_bookingSystem_IHotelCustomerProvides = Class(name="se::bookingSystem::IHotelCustomerProvides", is_abstract=True)
se_bookingSystem_FreeRoomTypesDTO = Class(name="se::bookingSystem::FreeRoomTypesDTO")
se_bookingSystem_Booking = Class(name="se::bookingSystem::Booking")
IBooking = Class(name="IBooking")
se_roomManager_IRoomType = Class(name="se::roomManager::IRoomType", is_abstract=True)
se_roomManager_RoomType = Class(name="se::roomManager::RoomType")
IRoomType = Class(name="IRoomType")
se_roomManager_RoomManager = Class(name="se::roomManager::RoomManager")
roomManager_IHotelStartupProvies = Class(name="roomManager::IHotelStartupProvies")
roomManager_IHotelRoomManager = Class(name="roomManager::IHotelRoomManager")
roomManager_IRoomType = Class(name="roomManager::IRoomType")
se_roomManager_IHotelStartupProvies = Class(name="se::roomManager::IHotelStartupProvies", is_abstract=True)
se_roomManager_IHotelRoomProvider = Class(name="se::roomManager::IHotelRoomProvider", is_abstract=True)
se_roomManager_IHotelRoomManager = Class(name="se::roomManager::IHotelRoomManager", is_abstract=True)
IHotelRoomProvider = Class(name="IHotelRoomProvider")
se_roomManager_Room = Class(name="se::roomManager::Room")
IRoom = Class(name="IRoom")
se_roomManager_IRoom = Class(name="se::roomManager::IRoom", is_abstract=True)

# se_bookingSystem_CheckInEvent class attributes and methods

# AbstractEvent class attributes and methods

# se_bookingSystem_AbstractEvent class attributes and methods
se_bookingSystem_AbstractEvent_eventType: Property = Property(name="eventType", type=StringType)
se_bookingSystem_AbstractEvent_bookingID: Property = Property(name="bookingID", type=IntegerType)
se_bookingSystem_AbstractEvent_timestamp: Property = Property(name="timestamp", type=StringType)
se_bookingSystem_AbstractEvent.attributes={se_bookingSystem_AbstractEvent_bookingID, se_bookingSystem_AbstractEvent_timestamp, se_bookingSystem_AbstractEvent_eventType}

# IEvent class attributes and methods

# se_bookingSystem_IEvent class attributes and methods
se_bookingSystem_IEvent_m_getTimestamp: Method = Method(name="getTimestamp", parameters={}, type=StringType)
se_bookingSystem_IEvent_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
se_bookingSystem_IEvent_m_getBookingId: Method = Method(name="getBookingId", parameters={}, type=IntegerType)
se_bookingSystem_IEvent.methods={se_bookingSystem_IEvent_m_getTimestamp, se_bookingSystem_IEvent_m_getBookingId, se_bookingSystem_IEvent_m_getType}

# se_bookingSystem_CheckOutEvent class attributes and methods

# se_bookingSystem_BookingSystem class attributes and methods
se_bookingSystem_BookingSystem_bookingId: Property = Property(name="bookingId", type=IntegerType)
se_bookingSystem_BookingSystem.attributes={se_bookingSystem_BookingSystem_bookingId}

# bookingSystem_IHotelBookingManager class attributes and methods

# bookingSystem_IHotelCustomerProvides class attributes and methods

# bookingSystem_IEvent class attributes and methods

# bookingSystem_IBooking class attributes and methods

# roomManager_IHotelRoomProvider class attributes and methods

# roomManager_IRoom class attributes and methods

# se_bookingSystem_IBooking class attributes and methods
se_bookingSystem_IBooking_m_getRooms: Method = Method(name="getRooms", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_getFirstName: Method = Method(name="getFirstName", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_getLastName: Method = Method(name="getLastName", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_getID: Method = Method(name="getID", parameters={}, type=IntegerType)
se_bookingSystem_IBooking_m_getStartDate: Method = Method(name="getStartDate", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_getEndDate: Method = Method(name="getEndDate", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_setRooms: Method = Method(name="setRooms", parameters={Parameter(name='rooms')})
se_bookingSystem_IBooking_m_setStartDate: Method = Method(name="setStartDate", parameters={Parameter(name='startDate')})
se_bookingSystem_IBooking_m_setEndDate: Method = Method(name="setEndDate", parameters={Parameter(name='endDate')})
se_bookingSystem_IBooking_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='room')}, type=BooleanType)
se_bookingSystem_IBooking_m_checkInRoom: Method = Method(name="checkInRoom", parameters={Parameter(name='roomToCheckIn')}, type=BooleanType)
se_bookingSystem_IBooking_m_getCheckedInRooms: Method = Method(name="getCheckedInRooms", parameters={}, type=StringType)
se_bookingSystem_IBooking_m_checkOutRoom: Method = Method(name="checkOutRoom", parameters={Parameter(name='roomToCheckOut')}, type=BooleanType)
se_bookingSystem_IBooking.methods={se_bookingSystem_IBooking_m_getRooms, se_bookingSystem_IBooking_m_getEndDate, se_bookingSystem_IBooking_m_setStartDate, se_bookingSystem_IBooking_m_getCheckedInRooms, se_bookingSystem_IBooking_m_setRooms, se_bookingSystem_IBooking_m_checkOutRoom, se_bookingSystem_IBooking_m_getLastName, se_bookingSystem_IBooking_m_checkInRoom, se_bookingSystem_IBooking_m_getStartDate, se_bookingSystem_IBooking_m_getID, se_bookingSystem_IBooking_m_setEndDate, se_bookingSystem_IBooking_m_addRoom, se_bookingSystem_IBooking_m_getFirstName}

# se_bookingSystem_IHotelBookingManager class attributes and methods
se_bookingSystem_IHotelBookingManager_m_initiateCheckin: Method = Method(name="initiateCheckin", parameters={Parameter(name='bookingId')}, type=StringType)
se_bookingSystem_IHotelBookingManager_m_editBookingPeriod: Method = Method(name="editBookingPeriod", parameters={Parameter(name='startDate'), Parameter(name='endDate'), Parameter(name='bookingId')}, type=BooleanType)
se_bookingSystem_IHotelBookingManager_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='bookingId')})
se_bookingSystem_IHotelBookingManager_m_listBooking: Method = Method(name="listBooking", parameters={}, type=StringType)
se_bookingSystem_IHotelBookingManager_m_listOccupiedRooms: Method = Method(name="listOccupiedRooms", parameters={Parameter(name='date')}, type=StringType)
se_bookingSystem_IHotelBookingManager_m_listCheckins: Method = Method(name="listCheckins", parameters={Parameter(name='startTime'), Parameter(name='endTime')}, type=StringType)
se_bookingSystem_IHotelBookingManager_m_listCheckouts: Method = Method(name="listCheckouts", parameters={Parameter(name='endTime'), Parameter(name='startTime')}, type=StringType)
se_bookingSystem_IHotelBookingManager_m_addExtraCostToRoom: Method = Method(name="addExtraCostToRoom", parameters={Parameter(name='priceOfCost'), Parameter(name='roomNumber'), Parameter(name='bookingId'), Parameter(name='descriptionOfCost')})
se_bookingSystem_IHotelBookingManager_m_editBookingRooms: Method = Method(name="editBookingRooms", parameters={Parameter(name='numOfRooms'), Parameter(name='bookingID'), Parameter(name='roomType')})
se_bookingSystem_IHotelBookingManager.methods={se_bookingSystem_IHotelBookingManager_m_listBooking, se_bookingSystem_IHotelBookingManager_m_listCheckouts, se_bookingSystem_IHotelBookingManager_m_editBookingRooms, se_bookingSystem_IHotelBookingManager_m_listCheckins, se_bookingSystem_IHotelBookingManager_m_addExtraCostToRoom, se_bookingSystem_IHotelBookingManager_m_editBookingPeriod, se_bookingSystem_IHotelBookingManager_m_cancelBooking, se_bookingSystem_IHotelBookingManager_m_listOccupiedRooms, se_bookingSystem_IHotelBookingManager_m_initiateCheckin}

# IHotelCustomerProvides class attributes and methods

# se_bookingSystem_IHotelCustomerProvides class attributes and methods
se_bookingSystem_IHotelCustomerProvides_m_getFreeRooms: Method = Method(name="getFreeRooms", parameters={Parameter(name='endDate'), Parameter(name='numBeds'), Parameter(name='startDate')}, type=StringType)
se_bookingSystem_IHotelCustomerProvides_m_initiateBooking: Method = Method(name="initiateBooking", parameters={Parameter(name='startDate'), Parameter(name='endDate'), Parameter(name='lastName'), Parameter(name='firstName')}, type=IntegerType)
se_bookingSystem_IHotelCustomerProvides_m_addRoomToBooking: Method = Method(name="addRoomToBooking", parameters={Parameter(name='roomTypeDescription'), Parameter(name='bookingID')}, type=BooleanType)
se_bookingSystem_IHotelCustomerProvides_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='bookingID')}, type=BooleanType)
se_bookingSystem_IHotelCustomerProvides_m_initiateCheckout: Method = Method(name="initiateCheckout", parameters={Parameter(name='bookingID')}, type=FloatType)
se_bookingSystem_IHotelCustomerProvides_m_payDuringCheckout: Method = Method(name="payDuringCheckout", parameters={Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='expiryYear'), Parameter(name='expiryMonth'), Parameter(name='ccv'), Parameter(name='ccNumber')}, type=BooleanType)
se_bookingSystem_IHotelCustomerProvides_m_initiateRoomCheckout: Method = Method(name="initiateRoomCheckout", parameters={Parameter(name='roomNumber'), Parameter(name='bookingId')}, type=FloatType)
se_bookingSystem_IHotelCustomerProvides_m_payRoomDuringCheckout: Method = Method(name="payRoomDuringCheckout", parameters={Parameter(name='lastName'), Parameter(name='ccv'), Parameter(name='expiryYear'), Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='roomNumber'), Parameter(name='expiryMonth')}, type=BooleanType)
se_bookingSystem_IHotelCustomerProvides_m_checkInRoom: Method = Method(name="checkInRoom", parameters={Parameter(name='bookingId'), Parameter(name='roomTypeDescription')}, type=IntegerType)
se_bookingSystem_IHotelCustomerProvides.methods={se_bookingSystem_IHotelCustomerProvides_m_checkInRoom, se_bookingSystem_IHotelCustomerProvides_m_getFreeRooms, se_bookingSystem_IHotelCustomerProvides_m_initiateCheckout, se_bookingSystem_IHotelCustomerProvides_m_confirmBooking, se_bookingSystem_IHotelCustomerProvides_m_initiateRoomCheckout, se_bookingSystem_IHotelCustomerProvides_m_initiateBooking, se_bookingSystem_IHotelCustomerProvides_m_addRoomToBooking, se_bookingSystem_IHotelCustomerProvides_m_payRoomDuringCheckout, se_bookingSystem_IHotelCustomerProvides_m_payDuringCheckout}

# se_bookingSystem_FreeRoomTypesDTO class attributes and methods
se_bookingSystem_FreeRoomTypesDTO_roomTypeDescription: Property = Property(name="roomTypeDescription", type=StringType)
se_bookingSystem_FreeRoomTypesDTO_numBeds: Property = Property(name="numBeds", type=IntegerType)
se_bookingSystem_FreeRoomTypesDTO_pricePerNight: Property = Property(name="pricePerNight", type=FloatType)
se_bookingSystem_FreeRoomTypesDTO_numFreeRooms: Property = Property(name="numFreeRooms", type=IntegerType)
se_bookingSystem_FreeRoomTypesDTO.attributes={se_bookingSystem_FreeRoomTypesDTO_pricePerNight, se_bookingSystem_FreeRoomTypesDTO_numFreeRooms, se_bookingSystem_FreeRoomTypesDTO_roomTypeDescription, se_bookingSystem_FreeRoomTypesDTO_numBeds}

# se_bookingSystem_Booking class attributes and methods
se_bookingSystem_Booking_lastName: Property = Property(name="lastName", type=StringType)
se_bookingSystem_Booking_id: Property = Property(name="id", type=IntegerType)
se_bookingSystem_Booking_firstName: Property = Property(name="firstName", type=StringType)
se_bookingSystem_Booking_startDate: Property = Property(name="startDate", type=StringType)
se_bookingSystem_Booking_endDate: Property = Property(name="endDate", type=StringType)
se_bookingSystem_Booking.attributes={se_bookingSystem_Booking_lastName, se_bookingSystem_Booking_firstName, se_bookingSystem_Booking_id, se_bookingSystem_Booking_startDate, se_bookingSystem_Booking_endDate}

# IBooking class attributes and methods

# se_roomManager_IRoomType class attributes and methods
se_roomManager_IRoomType_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
se_roomManager_IRoomType_m_getPrice: Method = Method(name="getPrice", parameters={}, type=FloatType)
se_roomManager_IRoomType_m_getNumberOfBeds: Method = Method(name="getNumberOfBeds", parameters={}, type=IntegerType)
se_roomManager_IRoomType_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
se_roomManager_IRoomType_m_setName: Method = Method(name="setName", parameters={Parameter(name='name')})
se_roomManager_IRoomType_m_setPrice: Method = Method(name="setPrice", parameters={Parameter(name='price')})
se_roomManager_IRoomType_m_setNumberOfBeds: Method = Method(name="setNumberOfBeds", parameters={Parameter(name='beds')})
se_roomManager_IRoomType_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
se_roomManager_IRoomType.methods={se_roomManager_IRoomType_m_getName, se_roomManager_IRoomType_m_getPrice, se_roomManager_IRoomType_m_setPrice, se_roomManager_IRoomType_m_getDescription, se_roomManager_IRoomType_m_setDescription, se_roomManager_IRoomType_m_setName, se_roomManager_IRoomType_m_setNumberOfBeds, se_roomManager_IRoomType_m_getNumberOfBeds}

# se_roomManager_RoomType class attributes and methods
se_roomManager_RoomType_price: Property = Property(name="price", type=FloatType)
se_roomManager_RoomType_name: Property = Property(name="name", type=StringType)
se_roomManager_RoomType_numberOfBeds: Property = Property(name="numberOfBeds", type=IntegerType)
se_roomManager_RoomType_description: Property = Property(name="description", type=StringType)
se_roomManager_RoomType.attributes={se_roomManager_RoomType_description, se_roomManager_RoomType_numberOfBeds, se_roomManager_RoomType_price, se_roomManager_RoomType_name}

# IRoomType class attributes and methods

# se_roomManager_RoomManager class attributes and methods

# roomManager_IHotelStartupProvies class attributes and methods

# roomManager_IHotelRoomManager class attributes and methods

# roomManager_IRoomType class attributes and methods

# se_roomManager_IHotelStartupProvies class attributes and methods
se_roomManager_IHotelStartupProvies_m_startup: Method = Method(name="startup", parameters={Parameter(name='numRoom')})
se_roomManager_IHotelStartupProvies.methods={se_roomManager_IHotelStartupProvies_m_startup}

# se_roomManager_IHotelRoomProvider class attributes and methods
se_roomManager_IHotelRoomProvider_m_getRooms: Method = Method(name="getRooms", parameters={}, type=StringType)
se_roomManager_IHotelRoomProvider.methods={se_roomManager_IHotelRoomProvider_m_getRooms}

# se_roomManager_IHotelRoomManager class attributes and methods
se_roomManager_IHotelRoomManager_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='name'), Parameter(name='price'), Parameter(name='description'), Parameter(name='numberOfBeds')}, type=BooleanType)
se_roomManager_IHotelRoomManager_m_updateRoomType: Method = Method(name="updateRoomType", parameters={Parameter(name='name'), Parameter(name='price'), Parameter(name='numberOfBeds'), Parameter(name='roomType'), Parameter(name='description')})
se_roomManager_IHotelRoomManager_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={}, type=StringType)
se_roomManager_IHotelRoomManager_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='roomType')}, type=StringType)
se_roomManager_IHotelRoomManager_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='roomNumber'), Parameter(name='roomType')}, type=BooleanType)
se_roomManager_IHotelRoomManager_m_changeRoomType: Method = Method(name="changeRoomType", parameters={Parameter(name='roomNumber'), Parameter(name='roomType')}, type=BooleanType)
se_roomManager_IHotelRoomManager_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='roomNumber')}, type=StringType)
se_roomManager_IHotelRoomManager_m_blockRoom: Method = Method(name="blockRoom", parameters={Parameter(name='roomNumber')})
se_roomManager_IHotelRoomManager_m_unblockRoom: Method = Method(name="unblockRoom", parameters={Parameter(name='roomNumber')})
se_roomManager_IHotelRoomManager.methods={se_roomManager_IHotelRoomManager_m_changeRoomType, se_roomManager_IHotelRoomManager_m_removeRoom, se_roomManager_IHotelRoomManager_m_getRoomTypes, se_roomManager_IHotelRoomManager_m_addRoom, se_roomManager_IHotelRoomManager_m_removeRoomType, se_roomManager_IHotelRoomManager_m_blockRoom, se_roomManager_IHotelRoomManager_m_unblockRoom, se_roomManager_IHotelRoomManager_m_addRoomType, se_roomManager_IHotelRoomManager_m_updateRoomType}

# IHotelRoomProvider class attributes and methods

# se_roomManager_Room class attributes and methods
se_roomManager_Room_roomNumber: Property = Property(name="roomNumber", type=IntegerType)
se_roomManager_Room_blocked: Property = Property(name="blocked", type=BooleanType)
se_roomManager_Room_extraCostDescriptions: Property = Property(name="extraCostDescriptions", type=StringType)
se_roomManager_Room_extraCostPrice: Property = Property(name="extraCostPrice", type=FloatType)
se_roomManager_Room_occupied: Property = Property(name="occupied", type=BooleanType)
se_roomManager_Room.attributes={se_roomManager_Room_blocked, se_roomManager_Room_extraCostDescriptions, se_roomManager_Room_occupied, se_roomManager_Room_extraCostPrice, se_roomManager_Room_roomNumber}

# IRoom class attributes and methods

# se_roomManager_IRoom class attributes and methods
se_roomManager_IRoom_m_getRoomType: Method = Method(name="getRoomType", parameters={}, type=StringType)
se_roomManager_IRoom_m_getRoomNumber: Method = Method(name="getRoomNumber", parameters={}, type=IntegerType)
se_roomManager_IRoom_m_setRoomType: Method = Method(name="setRoomType", parameters={Parameter(name='roomType')})
se_roomManager_IRoom_m_setIsBlocked: Method = Method(name="setIsBlocked", parameters={Parameter(name='blocked')})
se_roomManager_IRoom_m_isBlocked: Method = Method(name="isBlocked", parameters={}, type=BooleanType)
se_roomManager_IRoom_m_getExtraCostDescription: Method = Method(name="getExtraCostDescription", parameters={}, type=StringType)
se_roomManager_IRoom_m_setExtraCostDescription: Method = Method(name="setExtraCostDescription", parameters={Parameter(name='extraCostDescription')})
se_roomManager_IRoom_m_getExtraCostPrice: Method = Method(name="getExtraCostPrice", parameters={}, type=FloatType)
se_roomManager_IRoom_m_addExtraCost: Method = Method(name="addExtraCost", parameters={Parameter(name='extraCostPrice')})
se_roomManager_IRoom_m_isOccupied: Method = Method(name="isOccupied", parameters={}, type=BooleanType)
se_roomManager_IRoom_m_setOccupied: Method = Method(name="setOccupied", parameters={Parameter(name='status')})
se_roomManager_IRoom.methods={se_roomManager_IRoom_m_getRoomType, se_roomManager_IRoom_m_setExtraCostDescription, se_roomManager_IRoom_m_getExtraCostDescription, se_roomManager_IRoom_m_setRoomType, se_roomManager_IRoom_m_setOccupied, se_roomManager_IRoom_m_addExtraCost, se_roomManager_IRoom_m_getExtraCostPrice, se_roomManager_IRoom_m_setIsBlocked, se_roomManager_IRoom_m_getRoomNumber, se_roomManager_IRoom_m_isBlocked, se_roomManager_IRoom_m_isOccupied}

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="bookingSystem_IEvent", type=se_bookingSystem_BookingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_BookingSystem", type=bookingSystem_IEvent, multiplicity=Multiplicity(0, 9999))
    }
)
bookings1: BinaryAssociation = BinaryAssociation(
    name="bookings1",
    ends={
        Property(name="bookingSystem_IBooking", type=se_bookingSystem_BookingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_BookingSystem2", type=bookingSystem_IBooking, multiplicity=Multiplicity(0, 9999))
    }
)
rooms5: BinaryAssociation = BinaryAssociation(
    name="rooms5",
    ends={
        Property(name="roomManager_IRoom", type=se_bookingSystem_BookingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_BookingSystem6", type=roomManager_IRoom, multiplicity=Multiplicity(0, 9999))
    }
)
roomProvider3: BinaryAssociation = BinaryAssociation(
    name="roomProvider3",
    ends={
        Property(name="roomManager_IHotelRoomProvider", type=se_bookingSystem_BookingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_BookingSystem4", type=roomManager_IHotelRoomProvider, multiplicity=Multiplicity(1, 1))
    }
)
roomList7: BinaryAssociation = BinaryAssociation(
    name="roomList7",
    ends={
        Property(name="roomManager_IRoom8", type=se_bookingSystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_Booking", type=roomManager_IRoom, multiplicity=Multiplicity(0, 9999))
    }
)
checkedInRooms9: BinaryAssociation = BinaryAssociation(
    name="checkedInRooms9",
    ends={
        Property(name="roomManager_IRoom11", type=se_bookingSystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="se_bookingSystem_Booking10", type=roomManager_IRoom, multiplicity=Multiplicity(0, 9999))
    }
)
roomTypes12: BinaryAssociation = BinaryAssociation(
    name="roomTypes12",
    ends={
        Property(name="roomManager_IRoomType", type=se_roomManager_RoomManager, multiplicity=Multiplicity(1, 1)),
        Property(name="se_roomManager_RoomManager", type=roomManager_IRoomType, multiplicity=Multiplicity(0, 9999))
    }
)
rooms13: BinaryAssociation = BinaryAssociation(
    name="rooms13",
    ends={
        Property(name="roomManager_IRoom15", type=se_roomManager_RoomManager, multiplicity=Multiplicity(1, 1)),
        Property(name="se_roomManager_RoomManager14", type=roomManager_IRoom, multiplicity=Multiplicity(0, 9999))
    }
)
roomType16: BinaryAssociation = BinaryAssociation(
    name="roomType16",
    ends={
        Property(name="roomManager_IRoomType17", type=se_roomManager_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="se_roomManager_Room", type=roomManager_IRoomType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_se_bookingSystem_CheckInEvent_AbstractEvent = Generalization(general=AbstractEvent, specific=se_bookingSystem_CheckInEvent)
gen_se_bookingSystem_AbstractEvent_IEvent = Generalization(general=IEvent, specific=se_bookingSystem_AbstractEvent)
gen_se_bookingSystem_CheckOutEvent_AbstractEvent = Generalization(general=AbstractEvent, specific=se_bookingSystem_CheckOutEvent)
gen_se_bookingSystem_BookingSystem_bookingSystem_IHotelBookingManager = Generalization(general=bookingSystem_IHotelBookingManager, specific=se_bookingSystem_BookingSystem)
gen_se_bookingSystem_BookingSystem_bookingSystem_IHotelCustomerProvides = Generalization(general=bookingSystem_IHotelCustomerProvides, specific=se_bookingSystem_BookingSystem)
gen_se_bookingSystem_IHotelBookingManager_IHotelCustomerProvides = Generalization(general=IHotelCustomerProvides, specific=se_bookingSystem_IHotelBookingManager)
gen_se_bookingSystem_Booking_IBooking = Generalization(general=IBooking, specific=se_bookingSystem_Booking)
gen_se_roomManager_RoomType_IRoomType = Generalization(general=IRoomType, specific=se_roomManager_RoomType)
gen_se_roomManager_RoomManager_roomManager_IHotelStartupProvies = Generalization(general=roomManager_IHotelStartupProvies, specific=se_roomManager_RoomManager)
gen_se_roomManager_RoomManager_roomManager_IHotelRoomProvider = Generalization(general=roomManager_IHotelRoomProvider, specific=se_roomManager_RoomManager)
gen_se_roomManager_RoomManager_roomManager_IHotelRoomManager = Generalization(general=roomManager_IHotelRoomManager, specific=se_roomManager_RoomManager)
gen_se_roomManager_IHotelRoomManager_IHotelRoomProvider = Generalization(general=IHotelRoomProvider, specific=se_roomManager_IHotelRoomManager)
gen_se_roomManager_Room_IRoom = Generalization(general=IRoom, specific=se_roomManager_Room)

# Domain Model
domain_model = DomainModel(
    name="se",
    types={se_bookingSystem_CheckInEvent, AbstractEvent, se_bookingSystem_AbstractEvent, IEvent, se_bookingSystem_IEvent, se_bookingSystem_CheckOutEvent, se_bookingSystem_BookingSystem, bookingSystem_IHotelBookingManager, bookingSystem_IHotelCustomerProvides, bookingSystem_IEvent, bookingSystem_IBooking, roomManager_IHotelRoomProvider, roomManager_IRoom, se_bookingSystem_IBooking, se_bookingSystem_IHotelBookingManager, IHotelCustomerProvides, se_bookingSystem_IHotelCustomerProvides, se_bookingSystem_FreeRoomTypesDTO, se_bookingSystem_Booking, IBooking, se_roomManager_IRoomType, se_roomManager_RoomType, IRoomType, se_roomManager_RoomManager, roomManager_IHotelStartupProvies, roomManager_IHotelRoomManager, roomManager_IRoomType, se_roomManager_IHotelStartupProvies, se_roomManager_IHotelRoomProvider, se_roomManager_IHotelRoomManager, IHotelRoomProvider, se_roomManager_Room, IRoom, se_roomManager_IRoom, EventType},
    associations={events0, bookings1, rooms5, roomProvider3, roomList7, checkedInRooms9, roomTypes12, rooms13, roomType16},
    generalizations={gen_se_bookingSystem_CheckInEvent_AbstractEvent, gen_se_bookingSystem_AbstractEvent_IEvent, gen_se_bookingSystem_CheckOutEvent_AbstractEvent, gen_se_bookingSystem_BookingSystem_bookingSystem_IHotelBookingManager, gen_se_bookingSystem_BookingSystem_bookingSystem_IHotelCustomerProvides, gen_se_bookingSystem_IHotelBookingManager_IHotelCustomerProvides, gen_se_bookingSystem_Booking_IBooking, gen_se_roomManager_RoomType_IRoomType, gen_se_roomManager_RoomManager_roomManager_IHotelStartupProvies, gen_se_roomManager_RoomManager_roomManager_IHotelRoomProvider, gen_se_roomManager_RoomManager_roomManager_IHotelRoomManager, gen_se_roomManager_IHotelRoomManager_IHotelRoomProvider, gen_se_roomManager_Room_IRoom},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)