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
GuestTypes: Enumeration = Enumeration(
    name="GuestTypes",
    literals={
            EnumerationLiteral(name="Regular"),
			EnumerationLiteral(name="BlackListed"),
			EnumerationLiteral(name="VIP")
    }
)

PaymentMethod: Enumeration = Enumeration(
    name="PaymentMethod",
    literals={
            EnumerationLiteral(name="bankcard"),
			EnumerationLiteral(name="cash"),
			EnumerationLiteral(name="voucher")
    }
)

# Classes
bookingmodel_Booking = Class(name="bookingmodel::Booking")
bookingmodel_RoomToGuestIDEntry = Class(name="bookingmodel::RoomToGuestIDEntry")
bookingmodel_RoomIDToRoomTypeEntry = Class(name="bookingmodel::RoomIDToRoomTypeEntry")
bookingmodel_BookingRefToBookingEntry = Class(name="bookingmodel::BookingRefToBookingEntry")
bookingmodel_Customer = Class(name="bookingmodel::Customer")
bookingmodel_PaymentDetails = Class(name="bookingmodel::PaymentDetails")
bookingmodel_Person = Class(name="bookingmodel::Person", is_abstract=True)
bookingmodel_Guest = Class(name="bookingmodel::Guest")
bookingmodel_ExtraToIsPayedEntry = Class(name="bookingmodel::ExtraToIsPayedEntry")
Person = Class(name="Person")
bookingmodel_BookingHandler = Class(name="bookingmodel::BookingHandler")
bookingmodel_CustomerEmailToBookingRefEntry = Class(name="bookingmodel::CustomerEmailToBookingRefEntry")
bookingmodel_GuestEmailToRoomIDEntry = Class(name="bookingmodel::GuestEmailToRoomIDEntry")
bookingmodel_RoomIDToBookingRefEntry = Class(name="bookingmodel::RoomIDToBookingRefEntry")
bookingmodel_IBookingProvidesForHost = Class(name="bookingmodel::IBookingProvidesForHost", is_abstract=True)
bookingmodel_IBookingProvidesForCustomer = Class(name="bookingmodel::IBookingProvidesForCustomer", is_abstract=True)
BookingInfo = Class(name="BookingInfo")
CustomerInfo = Class(name="CustomerInfo")
bookingmodel_BookingInfo = Class(name="bookingmodel::BookingInfo", is_abstract=True)
bookingmodel_CustomerInfo = Class(name="bookingmodel::CustomerInfo", is_abstract=True)
bookingmodel_IBookingProvidesForGuest = Class(name="bookingmodel::IBookingProvidesForGuest", is_abstract=True)
bookingmodel_BookingProvides = Class(name="bookingmodel::BookingProvides")
IBookingProvidesForCustomer = Class(name="IBookingProvidesForCustomer")
IBookingProvidesForGuest = Class(name="IBookingProvidesForGuest")
IBookingProvidesForHost = Class(name="IBookingProvidesForHost")

# bookingmodel_Booking class attributes and methods
bookingmodel_Booking_startDate: Property = Property(name="startDate", type=StringType)
bookingmodel_Booking_endDate: Property = Property(name="endDate", type=StringType)
bookingmodel_Booking_serviceNotes: Property = Property(name="serviceNotes", type=StringType)
bookingmodel_Booking_nrOfGuests: Property = Property(name="nrOfGuests", type=StringType)
bookingmodel_Booking_bookingRef: Property = Property(name="bookingRef", type=StringType)
bookingmodel_Booking_isPayed: Property = Property(name="isPayed", type=StringType)
bookingmodel_Booking_paymentMethod: Property = Property(name="paymentMethod", type=StringType)
bookingmodel_Booking_m_checkedInAllRooms: Method = Method(name="checkedInAllRooms", parameters={}, type=StringType)
bookingmodel_Booking_m_checkedInRoom: Method = Method(name="checkedInRoom", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_Booking_m_getExtras: Method = Method(name="getExtras", parameters={}, type=StringType)
bookingmodel_Booking_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={}, type=StringType)
bookingmodel_Booking_m_getRoomIDs: Method = Method(name="getRoomIDs", parameters={}, type=StringType)
bookingmodel_Booking_m_removeResponsibleGuestToAllRooms: Method = Method(name="removeResponsibleGuestToAllRooms", parameters={Parameter(name='guestEmail')}, type=StringType)
bookingmodel_Booking_m_removeResponsibleGuest: Method = Method(name="removeResponsibleGuest", parameters={Parameter(name='roomID'), Parameter(name='guestEmail')}, type=StringType)
bookingmodel_Booking_m_setResponsibleGuest: Method = Method(name="setResponsibleGuest", parameters={Parameter(name='guestEmail'), Parameter(name='roomID')}, type=StringType)
bookingmodel_Booking_m_setResponsibleGuestToAllRooms: Method = Method(name="setResponsibleGuestToAllRooms", parameters={Parameter(name='guestEmail')}, type=StringType)
bookingmodel_Booking_m_getNrOfRooms: Method = Method(name="getNrOfRooms", parameters={}, type=StringType)
bookingmodel_Booking_m_setExtras: Method = Method(name="setExtras", parameters={Parameter(name='extras')}, type=StringType)
bookingmodel_Booking_m_setRoomTypes: Method = Method(name="setRoomTypes", parameters={Parameter(name='roomTypes')}, type=StringType)
bookingmodel_Booking_m_setRoomIDs: Method = Method(name="setRoomIDs", parameters={Parameter(name='roomIDs')}, type=StringType)
bookingmodel_Booking_m_setServiceNotes: Method = Method(name="setServiceNotes", parameters={Parameter(name='services')}, type=StringType)
bookingmodel_Booking_m_checkedOutRoom: Method = Method(name="checkedOutRoom", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_Booking_m_checkedOutAllRooms: Method = Method(name="checkedOutAllRooms", parameters={}, type=StringType)
bookingmodel_Booking_m_allExtrasPayed: Method = Method(name="allExtrasPayed", parameters={}, type=StringType)
bookingmodel_Booking_m_isExtraPayed: Method = Method(name="isExtraPayed", parameters={Parameter(name='extra')}, type=StringType)
bookingmodel_Booking_m_getUnPayedExtras: Method = Method(name="getUnPayedExtras", parameters={}, type=StringType)
bookingmodel_Booking_m_setExtrasAsPayed: Method = Method(name="setExtrasAsPayed", parameters={Parameter(name='extras')}, type=StringType)
bookingmodel_Booking_m_removeServiceNotes: Method = Method(name="removeServiceNotes", parameters={Parameter(name='serviceNotes')}, type=StringType)
bookingmodel_Booking.attributes={bookingmodel_Booking_startDate, bookingmodel_Booking_serviceNotes, bookingmodel_Booking_isPayed, bookingmodel_Booking_nrOfGuests, bookingmodel_Booking_endDate, bookingmodel_Booking_paymentMethod, bookingmodel_Booking_bookingRef}
bookingmodel_Booking.methods={bookingmodel_Booking_m_checkedOutAllRooms, bookingmodel_Booking_m_checkedInRoom, bookingmodel_Booking_m_getExtras, bookingmodel_Booking_m_checkedOutRoom, bookingmodel_Booking_m_getRoomIDs, bookingmodel_Booking_m_removeResponsibleGuest, bookingmodel_Booking_m_setExtras, bookingmodel_Booking_m_removeServiceNotes, bookingmodel_Booking_m_allExtrasPayed, bookingmodel_Booking_m_getRoomTypes, bookingmodel_Booking_m_setServiceNotes, bookingmodel_Booking_m_setRoomIDs, bookingmodel_Booking_m_setExtrasAsPayed, bookingmodel_Booking_m_checkedInAllRooms, bookingmodel_Booking_m_setRoomTypes, bookingmodel_Booking_m_isExtraPayed, bookingmodel_Booking_m_getUnPayedExtras, bookingmodel_Booking_m_removeResponsibleGuestToAllRooms, bookingmodel_Booking_m_setResponsibleGuestToAllRooms, bookingmodel_Booking_m_setResponsibleGuest, bookingmodel_Booking_m_getNrOfRooms}

# bookingmodel_RoomToGuestIDEntry class attributes and methods
bookingmodel_RoomToGuestIDEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_RoomToGuestIDEntry_value: Property = Property(name="value", type=StringType)
bookingmodel_RoomToGuestIDEntry.attributes={bookingmodel_RoomToGuestIDEntry_key, bookingmodel_RoomToGuestIDEntry_value}

# bookingmodel_RoomIDToRoomTypeEntry class attributes and methods
bookingmodel_RoomIDToRoomTypeEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_RoomIDToRoomTypeEntry_value: Property = Property(name="value", type=StringType)
bookingmodel_RoomIDToRoomTypeEntry.attributes={bookingmodel_RoomIDToRoomTypeEntry_value, bookingmodel_RoomIDToRoomTypeEntry_key}

# bookingmodel_BookingRefToBookingEntry class attributes and methods
bookingmodel_BookingRefToBookingEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_BookingRefToBookingEntry.attributes={bookingmodel_BookingRefToBookingEntry_key}

# bookingmodel_Customer class attributes and methods

# bookingmodel_PaymentDetails class attributes and methods
bookingmodel_PaymentDetails_ccNr: Property = Property(name="ccNr", type=StringType)
bookingmodel_PaymentDetails_ccV: Property = Property(name="ccV", type=StringType)
bookingmodel_PaymentDetails_expMonth: Property = Property(name="expMonth", type=StringType)
bookingmodel_PaymentDetails_expYear: Property = Property(name="expYear", type=StringType)
bookingmodel_PaymentDetails_firstName: Property = Property(name="firstName", type=StringType)
bookingmodel_PaymentDetails_lastName: Property = Property(name="lastName", type=StringType)
bookingmodel_PaymentDetails.attributes={bookingmodel_PaymentDetails_lastName, bookingmodel_PaymentDetails_expMonth, bookingmodel_PaymentDetails_expYear, bookingmodel_PaymentDetails_firstName, bookingmodel_PaymentDetails_ccV, bookingmodel_PaymentDetails_ccNr}

# bookingmodel_Person class attributes and methods
bookingmodel_Person_firstName: Property = Property(name="firstName", type=StringType)
bookingmodel_Person_lastName: Property = Property(name="lastName", type=StringType)
bookingmodel_Person_email: Property = Property(name="email", type=StringType)
bookingmodel_Person_telephoneNr: Property = Property(name="telephoneNr", type=StringType)
bookingmodel_Person_Address: Property = Property(name="Address", type=StringType)
bookingmodel_Person_age: Property = Property(name="age", type=StringType)
bookingmodel_Person.attributes={bookingmodel_Person_email, bookingmodel_Person_telephoneNr, bookingmodel_Person_firstName, bookingmodel_Person_lastName, bookingmodel_Person_Address, bookingmodel_Person_age}

# bookingmodel_Guest class attributes and methods
bookingmodel_Guest_guestTypes: Property = Property(name="guestTypes", type=StringType)
bookingmodel_Guest_roomNr: Property = Property(name="roomNr", type=StringType)
bookingmodel_Guest.attributes={bookingmodel_Guest_guestTypes, bookingmodel_Guest_roomNr}

# bookingmodel_ExtraToIsPayedEntry class attributes and methods
bookingmodel_ExtraToIsPayedEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_ExtraToIsPayedEntry_value: Property = Property(name="value", type=StringType)
bookingmodel_ExtraToIsPayedEntry.attributes={bookingmodel_ExtraToIsPayedEntry_value, bookingmodel_ExtraToIsPayedEntry_key}

# Person class attributes and methods

# bookingmodel_BookingHandler class attributes and methods
bookingmodel_BookingHandler_m_removeBooking: Method = Method(name="removeBooking", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingHandler_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingHandler_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='bookingRef'), Parameter(name='startDate'), Parameter(name='roomTypes'), Parameter(name='nrOfGuests'), Parameter(name='extras'), Parameter(name='services'), Parameter(name='endDate')}, type=StringType)
bookingmodel_BookingHandler_m_exists: Method = Method(name="exists", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingHandler_m_addBooking: Method = Method(name="addBooking", parameters={Parameter(name='services'), Parameter(name='roomTypes'), Parameter(name='extras'), Parameter(name='startDate'), Parameter(name='nrOfGuests'), Parameter(name='endDate')}, type=StringType)
bookingmodel_BookingHandler_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_BookingHandler_m_isActive: Method = Method(name="isActive", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingHandler.methods={bookingmodel_BookingHandler_m_exists, bookingmodel_BookingHandler_m_removeBooking, bookingmodel_BookingHandler_m_getBooking, bookingmodel_BookingHandler_m_addBooking, bookingmodel_BookingHandler_m_isActive, bookingmodel_BookingHandler_m_editBooking, bookingmodel_BookingHandler_m_getBooking}

# bookingmodel_CustomerEmailToBookingRefEntry class attributes and methods
bookingmodel_CustomerEmailToBookingRefEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_CustomerEmailToBookingRefEntry_value: Property = Property(name="value", type=StringType)
bookingmodel_CustomerEmailToBookingRefEntry.attributes={bookingmodel_CustomerEmailToBookingRefEntry_key, bookingmodel_CustomerEmailToBookingRefEntry_value}

# bookingmodel_GuestEmailToRoomIDEntry class attributes and methods
bookingmodel_GuestEmailToRoomIDEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_GuestEmailToRoomIDEntry_value: Property = Property(name="value", type=IntegerType)
bookingmodel_GuestEmailToRoomIDEntry.attributes={bookingmodel_GuestEmailToRoomIDEntry_value, bookingmodel_GuestEmailToRoomIDEntry_key}

# bookingmodel_RoomIDToBookingRefEntry class attributes and methods
bookingmodel_RoomIDToBookingRefEntry_key: Property = Property(name="key", type=StringType)
bookingmodel_RoomIDToBookingRefEntry_value: Property = Property(name="value", type=StringType)
bookingmodel_RoomIDToBookingRefEntry.attributes={bookingmodel_RoomIDToBookingRefEntry_value, bookingmodel_RoomIDToBookingRefEntry_key}

# bookingmodel_IBookingProvidesForHost class attributes and methods
bookingmodel_IBookingProvidesForHost_m_isExtraPayed: Method = Method(name="isExtraPayed", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_isRoomPayed: Method = Method(name="isRoomPayed", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_existBooking: Method = Method(name="existBooking", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_getExistingBookings: Method = Method(name="getExistingBookings", parameters={}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_isBookingPayed: Method = Method(name="isBookingPayed", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_isCheckedOut: Method = Method(name="isCheckedOut", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_isCheckedIn: Method = Method(name="isCheckedIn", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_getResponsibleGuest: Method = Method(name="getResponsibleGuest", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_getRoomID: Method = Method(name="getRoomID", parameters={Parameter(name='guestEmail')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_addServiceNotes: Method = Method(name="addServiceNotes", parameters={Parameter(name='serviceNote'), Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForHost_m_removeServiceNotes: Method = Method(name="removeServiceNotes", parameters={Parameter(name='roomID'), Parameter(name='serviceNote')}, type=StringType)
bookingmodel_IBookingProvidesForHost.methods={bookingmodel_IBookingProvidesForHost_m_isCheckedIn, bookingmodel_IBookingProvidesForHost_m_removeServiceNotes, bookingmodel_IBookingProvidesForHost_m_isRoomPayed, bookingmodel_IBookingProvidesForHost_m_getExistingBookings, bookingmodel_IBookingProvidesForHost_m_getRoomID, bookingmodel_IBookingProvidesForHost_m_isExtraPayed, bookingmodel_IBookingProvidesForHost_m_isBookingPayed, bookingmodel_IBookingProvidesForHost_m_isCheckedOut, bookingmodel_IBookingProvidesForHost_m_addServiceNotes, bookingmodel_IBookingProvidesForHost_m_getResponsibleGuest, bookingmodel_IBookingProvidesForHost_m_existBooking}

# bookingmodel_IBookingProvidesForCustomer class attributes and methods
bookingmodel_IBookingProvidesForCustomer_m_payBooking: Method = Method(name="payBooking", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_getPrice: Method = Method(name="getPrice", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_setPaymentDetails: Method = Method(name="setPaymentDetails", parameters={Parameter(name='expiryMonth'), Parameter(name='expiryYear'), Parameter(name='lastName'), Parameter(name='bookingRef'), Parameter(name='customerEmail'), Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='ccNumber')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_removeBooking: Method = Method(name="removeBooking", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='extras'), Parameter(name='bookingRef'), Parameter(name='services'), Parameter(name='startDate'), Parameter(name='nrOfGuests'), Parameter(name='endDate'), Parameter(name='roomTypes')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_setPaymentMethod: Method = Method(name="setPaymentMethod", parameters={Parameter(name='bookingRef'), Parameter(name='method')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_editPaymentDetails: Method = Method(name="editPaymentDetails", parameters={Parameter(name='ccv'), Parameter(name='bookingRef'), Parameter(name='firstName'), Parameter(name='expiryYear'), Parameter(name='customerEmail'), Parameter(name='ccNumber'), Parameter(name='lastName'), Parameter(name='expiryMonth')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_setPersonalDetails: Method = Method(name="setPersonalDetails", parameters={Parameter(name='bookingRef'), Parameter(name='email'), Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='age')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_book: Method = Method(name="book", parameters={Parameter(name='roomTypes'), Parameter(name='nrOfGuests'), Parameter(name='startDate'), Parameter(name='extras'), Parameter(name='endDate'), Parameter(name='services')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_removeExtra: Method = Method(name="removeExtra", parameters={Parameter(name='roomID'), Parameter(name='extraID')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='extraID'), Parameter(name='bookingRef')}, type=StringType)
bookingmodel_IBookingProvidesForCustomer.methods={bookingmodel_IBookingProvidesForCustomer_m_removeBooking, bookingmodel_IBookingProvidesForCustomer_m_book, bookingmodel_IBookingProvidesForCustomer_m_addExtra, bookingmodel_IBookingProvidesForCustomer_m_editBooking, bookingmodel_IBookingProvidesForCustomer_m_getPrice, bookingmodel_IBookingProvidesForCustomer_m_setPaymentMethod, bookingmodel_IBookingProvidesForCustomer_m_editPaymentDetails, bookingmodel_IBookingProvidesForCustomer_m_payBooking, bookingmodel_IBookingProvidesForCustomer_m_setPaymentDetails, bookingmodel_IBookingProvidesForCustomer_m_removeExtra, bookingmodel_IBookingProvidesForCustomer_m_setPersonalDetails}

# BookingInfo class attributes and methods

# CustomerInfo class attributes and methods

# bookingmodel_BookingInfo class attributes and methods
bookingmodel_BookingInfo_m_getStartDate: Method = Method(name="getStartDate", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getEndDate: Method = Method(name="getEndDate", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getNrOfGuests: Method = Method(name="getNrOfGuests", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getServiceNotes: Method = Method(name="getServiceNotes", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getBookingRef: Method = Method(name="getBookingRef", parameters={Parameter(name='customerEmail')}, type=StringType)
bookingmodel_BookingInfo_m_getExtras: Method = Method(name="getExtras", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getRooms: Method = Method(name="getRooms", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getPaymentMethod: Method = Method(name="getPaymentMethod", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_BookingInfo.methods={bookingmodel_BookingInfo_m_getBookingRef, bookingmodel_BookingInfo_m_getRooms, bookingmodel_BookingInfo_m_getRoomTypes, bookingmodel_BookingInfo_m_getServiceNotes, bookingmodel_BookingInfo_m_getNrOfGuests, bookingmodel_BookingInfo_m_getExtras, bookingmodel_BookingInfo_m_getStartDate, bookingmodel_BookingInfo_m_getPaymentMethod, bookingmodel_BookingInfo_m_getEndDate}

# bookingmodel_CustomerInfo class attributes and methods
bookingmodel_CustomerInfo_m_getExpMonth: Method = Method(name="getExpMonth", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getExpYear: Method = Method(name="getExpYear", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCardFirstName: Method = Method(name="getCardFirstName", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCardLastName: Method = Method(name="getCardLastName", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCustomerName: Method = Method(name="getCustomerName", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCustomerLastName: Method = Method(name="getCustomerLastName", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCustomerAge: Method = Method(name="getCustomerAge", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCustomerEmail: Method = Method(name="getCustomerEmail", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCcNr: Method = Method(name="getCcNr", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo_m_getCcV: Method = Method(name="getCcV", parameters={Parameter(name='bookingRef')}, type=StringType)
bookingmodel_CustomerInfo.methods={bookingmodel_CustomerInfo_m_getExpYear, bookingmodel_CustomerInfo_m_getCardFirstName, bookingmodel_CustomerInfo_m_getCcNr, bookingmodel_CustomerInfo_m_getCustomerAge, bookingmodel_CustomerInfo_m_getCcV, bookingmodel_CustomerInfo_m_getCardLastName, bookingmodel_CustomerInfo_m_getExpMonth, bookingmodel_CustomerInfo_m_getCustomerLastName, bookingmodel_CustomerInfo_m_getCustomerName, bookingmodel_CustomerInfo_m_getCustomerEmail}

# bookingmodel_IBookingProvidesForGuest class attributes and methods
bookingmodel_IBookingProvidesForGuest_m_payRoom: Method = Method(name="payRoom", parameters={Parameter(name='firstName'), Parameter(name='lastName'), Parameter(name='roomID'), Parameter(name='ccNumber'), Parameter(name='expYear'), Parameter(name='expMonth'), Parameter(name='ccv')}, type=StringType)
bookingmodel_IBookingProvidesForGuest_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='bookingRef'), Parameter(name='guestEmail'), Parameter(name='roomType')}, type=StringType)
bookingmodel_IBookingProvidesForGuest_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForGuest_m_payExtra: Method = Method(name="payExtra", parameters={Parameter(name='lastName'), Parameter(name='extra'), Parameter(name='expYear'), Parameter(name='ccNumber'), Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='roomID'), Parameter(name='expMonth')}, type=StringType)
bookingmodel_IBookingProvidesForGuest_m_removeExtra: Method = Method(name="removeExtra", parameters={Parameter(name='extraIDs'), Parameter(name='roomID')}, type=StringType)
bookingmodel_IBookingProvidesForGuest_m_addExtra: Method = Method(name="addExtra", parameters={Parameter(name='roomID'), Parameter(name='extraIDs')}, type=StringType)
bookingmodel_IBookingProvidesForGuest.methods={bookingmodel_IBookingProvidesForGuest_m_checkOut, bookingmodel_IBookingProvidesForGuest_m_removeExtra, bookingmodel_IBookingProvidesForGuest_m_payExtra, bookingmodel_IBookingProvidesForGuest_m_payRoom, bookingmodel_IBookingProvidesForGuest_m_checkIn, bookingmodel_IBookingProvidesForGuest_m_addExtra}

# bookingmodel_BookingProvides class attributes and methods
bookingmodel_BookingProvides_m_stringToList: Method = Method(name="stringToList", parameters={Parameter(name='text')}, type=StringType)
bookingmodel_BookingProvides.methods={bookingmodel_BookingProvides_m_stringToList}

# IBookingProvidesForCustomer class attributes and methods

# IBookingProvidesForGuest class attributes and methods

# IBookingProvidesForHost class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="bookingmodel_Booking", type=bookingmodel_BookingRefToBookingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingRefToBookingEntry", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1))
    }
)
paymentDetails11: BinaryAssociation = BinaryAssociation(
    name="paymentDetails11",
    ends={
        Property(name="bookingmodel_PaymentDetails", type=bookingmodel_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Customer12", type=bookingmodel_PaymentDetails, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
customer1: BinaryAssociation = BinaryAssociation(
    name="customer1",
    ends={
        Property(name="bookingmodel_Customer", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Booking2", type=bookingmodel_Customer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guestList3: BinaryAssociation = BinaryAssociation(
    name="guestList3",
    ends={
        Property(name="bookingmodel_Guest", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Booking4", type=bookingmodel_Guest, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
roomIDToGuestMap5: BinaryAssociation = BinaryAssociation(
    name="roomIDToGuestMap5",
    ends={
        Property(name="bookingmodel_RoomToGuestIDEntry", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Booking6", type=bookingmodel_RoomToGuestIDEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roomIDToRoomTypeMap7: BinaryAssociation = BinaryAssociation(
    name="roomIDToRoomTypeMap7",
    ends={
        Property(name="bookingmodel_RoomIDToRoomTypeEntry", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Booking8", type=bookingmodel_RoomIDToRoomTypeEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extraToIsPayedMap9: BinaryAssociation = BinaryAssociation(
    name="extraToIsPayedMap9",
    ends={
        Property(name="bookingmodel_ExtraToIsPayedEntry", type=bookingmodel_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_Booking10", type=bookingmodel_ExtraToIsPayedEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customerEmailToBookingRefEntry17: BinaryAssociation = BinaryAssociation(
    name="customerEmailToBookingRefEntry17",
    ends={
        Property(name="bookingmodel_CustomerEmailToBookingRefEntry", type=bookingmodel_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingHandler18", type=bookingmodel_CustomerEmailToBookingRefEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guestEmailToRoomIDEntry19: BinaryAssociation = BinaryAssociation(
    name="guestEmailToRoomIDEntry19",
    ends={
        Property(name="bookingmodel_GuestEmailToRoomIDEntry", type=bookingmodel_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingHandler20", type=bookingmodel_GuestEmailToRoomIDEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookingsMap13: BinaryAssociation = BinaryAssociation(
    name="bookingsMap13",
    ends={
        Property(name="bookingmodel_BookingRefToBookingEntry14", type=bookingmodel_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingHandler", type=bookingmodel_BookingRefToBookingEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roomIDToBookingRefMap15: BinaryAssociation = BinaryAssociation(
    name="roomIDToBookingRefMap15",
    ends={
        Property(name="bookingmodel_RoomIDToBookingRefEntry", type=bookingmodel_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingHandler16", type=bookingmodel_RoomIDToBookingRefEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookingHandler21: BinaryAssociation = BinaryAssociation(
    name="bookingHandler21",
    ends={
        Property(name="bookingmodel_BookingHandler22", type=bookingmodel_BookingProvides, multiplicity=Multiplicity(1, 1)),
        Property(name="bookingmodel_BookingProvides", type=bookingmodel_BookingHandler, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_bookingmodel_Customer_Person = Generalization(general=Person, specific=bookingmodel_Customer)
gen_bookingmodel_Guest_Person = Generalization(general=Person, specific=bookingmodel_Guest)
gen_bookingmodel_IBookingProvidesForCustomer_BookingInfo = Generalization(general=BookingInfo, specific=bookingmodel_IBookingProvidesForCustomer)
gen_bookingmodel_IBookingProvidesForCustomer_CustomerInfo = Generalization(general=CustomerInfo, specific=bookingmodel_IBookingProvidesForCustomer)
gen_bookingmodel_BookingProvides_IBookingProvidesForCustomer = Generalization(general=IBookingProvidesForCustomer, specific=bookingmodel_BookingProvides)
gen_bookingmodel_BookingProvides_IBookingProvidesForGuest = Generalization(general=IBookingProvidesForGuest, specific=bookingmodel_BookingProvides)
gen_bookingmodel_BookingProvides_IBookingProvidesForHost = Generalization(general=IBookingProvidesForHost, specific=bookingmodel_BookingProvides)

# Domain Model
domain_model = DomainModel(
    name="bookingmodel",
    types={bookingmodel_Booking, bookingmodel_RoomToGuestIDEntry, bookingmodel_RoomIDToRoomTypeEntry, bookingmodel_BookingRefToBookingEntry, bookingmodel_Customer, bookingmodel_PaymentDetails, bookingmodel_Person, bookingmodel_Guest, bookingmodel_ExtraToIsPayedEntry, Person, bookingmodel_BookingHandler, bookingmodel_CustomerEmailToBookingRefEntry, bookingmodel_GuestEmailToRoomIDEntry, bookingmodel_RoomIDToBookingRefEntry, bookingmodel_IBookingProvidesForHost, bookingmodel_IBookingProvidesForCustomer, BookingInfo, CustomerInfo, bookingmodel_BookingInfo, bookingmodel_CustomerInfo, bookingmodel_IBookingProvidesForGuest, bookingmodel_BookingProvides, IBookingProvidesForCustomer, IBookingProvidesForGuest, IBookingProvidesForHost, GuestTypes, PaymentMethod},
    associations={value0, paymentDetails11, customer1, guestList3, roomIDToGuestMap5, roomIDToRoomTypeMap7, extraToIsPayedMap9, customerEmailToBookingRefEntry17, guestEmailToRoomIDEntry19, bookingsMap13, roomIDToBookingRefMap15, bookingHandler21},
    generalizations={gen_bookingmodel_Customer_Person, gen_bookingmodel_Guest_Person, gen_bookingmodel_IBookingProvidesForCustomer_BookingInfo, gen_bookingmodel_IBookingProvidesForCustomer_CustomerInfo, gen_bookingmodel_BookingProvides_IBookingProvidesForCustomer, gen_bookingmodel_BookingProvides_IBookingProvidesForGuest, gen_bookingmodel_BookingProvides_IBookingProvidesForHost},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)