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
BookingStatus: Enumeration = Enumeration(
    name="BookingStatus",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="BOOKED"),
			EnumerationLiteral(name="CHECKED_IN"),
			EnumerationLiteral(name="CHECKED_OUT")
    }
)

# Classes
RootElement_Guest = Class(name="RootElement::Guest")
SupportTicketWriter = Class(name="SupportTicketWriter")
FeedbackWriter = Class(name="FeedbackWriter")
MakeBooking = Class(name="MakeBooking")
RootElement_SupportTicketWriter = Class(name="RootElement::SupportTicketWriter", is_abstract=True)
RootElement_MakeBooking = Class(name="RootElement::MakeBooking", is_abstract=True)
RootElement_FeedbackWriter = Class(name="RootElement::FeedbackWriter", is_abstract=True)
RootElement_Booking = Class(name="RootElement::Booking")
RootElement_RoomBooking = Class(name="RootElement::RoomBooking", is_abstract=True)
RootElement_ServiceItem = Class(name="RootElement::ServiceItem")
RootElement_Room = Class(name="RootElement::Room")
RootElement_RoomType = Class(name="RootElement::RoomType")
RootElement_RoomAttribute = Class(name="RootElement::RoomAttribute")
SupportTicketReader = Class(name="SupportTicketReader")
RootElement_Feedback = Class(name="RootElement::Feedback")
RootElement_Staff = Class(name="RootElement::Staff")
Cleaning = Class(name="Cleaning")
RootElement_Cleaning = Class(name="RootElement::Cleaning", is_abstract=True)
RootElement_SupportTicketReader = Class(name="RootElement::SupportTicketReader", is_abstract=True)
RootElement_SupportTicket = Class(name="RootElement::SupportTicket")
Staff = Class(name="Staff")
ReceptionHandling = Class(name="ReceptionHandling")
ServiceItemHandling = Class(name="ServiceItemHandling")
Payment = Class(name="Payment")
RootElement_ReceptionHandling = Class(name="RootElement::ReceptionHandling", is_abstract=True)
RootElement_ServiceItemHandling = Class(name="RootElement::ServiceItemHandling", is_abstract=True)
RootElement_Clerk = Class(name="RootElement::Clerk")
RootElement_Payment = Class(name="RootElement::Payment", is_abstract=True)
RootElement_Manager = Class(name="RootElement::Manager")
Clerk = Class(name="Clerk")
SysAdmin = Class(name="SysAdmin")
FeedbackReader = Class(name="FeedbackReader")
RootElement_FeedbackReader = Class(name="RootElement::FeedbackReader", is_abstract=True)
RootElement_SysAdmin = Class(name="RootElement::SysAdmin")
RoomAttributeHandling = Class(name="RoomAttributeHandling")
RoomHandling = Class(name="RoomHandling")
RoomTypeHandling = Class(name="RoomTypeHandling")
RootElement_RoomAttributeHandling = Class(name="RootElement::RoomAttributeHandling", is_abstract=True)
RootElement_RoomHandling = Class(name="RootElement::RoomHandling", is_abstract=True)
RootElement_RoomTypeHandling = Class(name="RootElement::RoomTypeHandling", is_abstract=True)
RootElement_BookingHandler = Class(name="RootElement::BookingHandler")
RootElement_RoomFetcher = Class(name="RootElement::RoomFetcher", is_abstract=True)
RootElement_RoomStructure = Class(name="RootElement::RoomStructure")
RootElement_FeedbackHandler = Class(name="RootElement::FeedbackHandler")
RootElement_SupportTicketHandler = Class(name="RootElement::SupportTicketHandler")
RootElement_CleaningHandler = Class(name="RootElement::CleaningHandler")
RootElement_PaymentHandler = Class(name="RootElement::PaymentHandler")
RootElement_DailyRoomBooking = Class(name="RootElement::DailyRoomBooking")
RoomBooking = Class(name="RoomBooking")
RoomFetcher = Class(name="RoomFetcher")
RootElement_HourlyRoomBooking = Class(name="RootElement::HourlyRoomBooking")
RootElement_HotelSystem = Class(name="RootElement::HotelSystem", is_abstract=True)
RootElement_Hotel = Class(name="RootElement::Hotel")
HotelSystem = Class(name="HotelSystem")

# RootElement_Guest class attributes and methods
RootElement_Guest_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
RootElement_Guest_nextDestination: Property = Property(name="nextDestination", type=StringType)
RootElement_Guest_nationality: Property = Property(name="nationality", type=StringType)
RootElement_Guest_name: Property = Property(name="name", type=StringType)
RootElement_Guest_mail: Property = Property(name="mail", type=StringType)
RootElement_Guest_socialSecurityNumber: Property = Property(name="socialSecurityNumber", type=StringType)
RootElement_Guest.attributes={RootElement_Guest_name, RootElement_Guest_phoneNumber, RootElement_Guest_mail, RootElement_Guest_nextDestination, RootElement_Guest_nationality, RootElement_Guest_socialSecurityNumber}

# SupportTicketWriter class attributes and methods

# FeedbackWriter class attributes and methods

# MakeBooking class attributes and methods

# RootElement_SupportTicketWriter class attributes and methods
RootElement_SupportTicketWriter_m_newSupportTicket: Method = Method(name="newSupportTicket", parameters={Parameter(name='roomName'), Parameter(name='description')})
RootElement_SupportTicketWriter.methods={RootElement_SupportTicketWriter_m_newSupportTicket}

# RootElement_MakeBooking class attributes and methods
RootElement_MakeBooking_m_createBooking: Method = Method(name="createBooking", parameters={}, type=StringType)
RootElement_MakeBooking_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='endDate'), Parameter(name='nbrOfAdults'), Parameter(name='startDate'), Parameter(name='nbrOfChildren')}, type=StringType)
RootElement_MakeBooking_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='booking'), Parameter(name='nbrOfChildren'), Parameter(name='endDate'), Parameter(name='startDate'), Parameter(name='room'), Parameter(name='nbrOfAdults')}, type=StringType)
RootElement_MakeBooking_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='phone'), Parameter(name='nationality'), Parameter(name='mail'), Parameter(name='name'), Parameter(name='booking'), Parameter(name='passportNr'), Parameter(name='nextDestination')}, type=StringType)
RootElement_MakeBooking_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='booking')}, type=StringType)
RootElement_MakeBooking_m_lookupBooking: Method = Method(name="lookupBooking", parameters={Parameter(name='name'), Parameter(name='phoneNumber')}, type=StringType)
RootElement_MakeBooking.methods={RootElement_MakeBooking_m_getAvailableRooms, RootElement_MakeBooking_m_lookupBooking, RootElement_MakeBooking_m_confirmBooking, RootElement_MakeBooking_m_addRoom, RootElement_MakeBooking_m_cancelBooking, RootElement_MakeBooking_m_createBooking}

# RootElement_FeedbackWriter class attributes and methods
RootElement_FeedbackWriter_m_giveFeedback: Method = Method(name="giveFeedback", parameters={Parameter(name='rating'), Parameter(name='feedback')})
RootElement_FeedbackWriter.methods={RootElement_FeedbackWriter_m_giveFeedback}

# RootElement_Booking class attributes and methods
RootElement_Booking_bookingID: Property = Property(name="bookingID", type=StringType)
RootElement_Booking_m_calculateCost: Method = Method(name="calculateCost", parameters={}, type=StringType)
RootElement_Booking.attributes={RootElement_Booking_bookingID}
RootElement_Booking.methods={RootElement_Booking_m_calculateCost}

# RootElement_RoomBooking class attributes and methods
RootElement_RoomBooking_startDate: Property = Property(name="startDate", type=DateType)
RootElement_RoomBooking_endDate: Property = Property(name="endDate", type=DateType)
RootElement_RoomBooking_bookingStatus: Property = Property(name="bookingStatus", type=StringType)
RootElement_RoomBooking_m_calculateCost: Method = Method(name="calculateCost", parameters={}, type=StringType)
RootElement_RoomBooking.attributes={RootElement_RoomBooking_bookingStatus, RootElement_RoomBooking_endDate, RootElement_RoomBooking_startDate}
RootElement_RoomBooking.methods={RootElement_RoomBooking_m_calculateCost}

# RootElement_ServiceItem class attributes and methods
RootElement_ServiceItem_name: Property = Property(name="name", type=StringType)
RootElement_ServiceItem_description: Property = Property(name="description", type=StringType)
RootElement_ServiceItem_price: Property = Property(name="price", type=StringType)
RootElement_ServiceItem.attributes={RootElement_ServiceItem_price, RootElement_ServiceItem_description, RootElement_ServiceItem_name}

# RootElement_Room class attributes and methods
RootElement_Room_isOccupied: Property = Property(name="isOccupied", type=StringType)
RootElement_Room_name: Property = Property(name="name", type=StringType)
RootElement_Room_needCleaning: Property = Property(name="needCleaning", type=StringType)
RootElement_Room.attributes={RootElement_Room_isOccupied, RootElement_Room_needCleaning, RootElement_Room_name}

# RootElement_RoomType class attributes and methods
RootElement_RoomType_name: Property = Property(name="name", type=StringType)
RootElement_RoomType_price: Property = Property(name="price", type=StringType)
RootElement_RoomType_capacity: Property = Property(name="capacity", type=StringType)
RootElement_RoomType_m_addRoomAttribute: Method = Method(name="addRoomAttribute", parameters={Parameter(name='roomAttribute')}, type=BooleanType)
RootElement_RoomType_m_removeRoomAttribute: Method = Method(name="removeRoomAttribute", parameters={Parameter(name='roomAttribute')}, type=BooleanType)
RootElement_RoomType.attributes={RootElement_RoomType_price, RootElement_RoomType_capacity, RootElement_RoomType_name}
RootElement_RoomType.methods={RootElement_RoomType_m_removeRoomAttribute, RootElement_RoomType_m_addRoomAttribute}

# RootElement_RoomAttribute class attributes and methods
RootElement_RoomAttribute_id: Property = Property(name="id", type=StringType)
RootElement_RoomAttribute_name: Property = Property(name="name", type=StringType)
RootElement_RoomAttribute_description: Property = Property(name="description", type=StringType)
RootElement_RoomAttribute.attributes={RootElement_RoomAttribute_name, RootElement_RoomAttribute_id, RootElement_RoomAttribute_description}

# SupportTicketReader class attributes and methods

# RootElement_Feedback class attributes and methods
RootElement_Feedback_feedbackDescription: Property = Property(name="feedbackDescription", type=StringType)
RootElement_Feedback_rating: Property = Property(name="rating", type=StringType)
RootElement_Feedback_read: Property = Property(name="read", type=StringType)
RootElement_Feedback.attributes={RootElement_Feedback_feedbackDescription, RootElement_Feedback_read, RootElement_Feedback_rating}

# RootElement_Staff class attributes and methods
RootElement_Staff_staffID: Property = Property(name="staffID", type=StringType)
RootElement_Staff_name: Property = Property(name="name", type=StringType)
RootElement_Staff.attributes={RootElement_Staff_name, RootElement_Staff_staffID}

# Cleaning class attributes and methods

# RootElement_Cleaning class attributes and methods
RootElement_Cleaning_m_checkIfRoomCleaned: Method = Method(name="checkIfRoomCleaned", parameters={Parameter(name='roomName')}, type=StringType)
RootElement_Cleaning_m_getListOfUncleanRooms: Method = Method(name="getListOfUncleanRooms", parameters={}, type=StringType)
RootElement_Cleaning_m_markRoomAsCleaned: Method = Method(name="markRoomAsCleaned", parameters={Parameter(name='room')})
RootElement_Cleaning.methods={RootElement_Cleaning_m_markRoomAsCleaned, RootElement_Cleaning_m_getListOfUncleanRooms, RootElement_Cleaning_m_checkIfRoomCleaned}

# RootElement_SupportTicketReader class attributes and methods
RootElement_SupportTicketReader_m_getUnfixedTickets: Method = Method(name="getUnfixedTickets", parameters={}, type=StringType)
RootElement_SupportTicketReader_m_getSupportTicketsForRoom: Method = Method(name="getSupportTicketsForRoom", parameters={Parameter(name='roomName')}, type=StringType)
RootElement_SupportTicketReader_m_markAsCompleted: Method = Method(name="markAsCompleted", parameters={Parameter(name='supportTicket')})
RootElement_SupportTicketReader.methods={RootElement_SupportTicketReader_m_getUnfixedTickets, RootElement_SupportTicketReader_m_getSupportTicketsForRoom, RootElement_SupportTicketReader_m_markAsCompleted}

# RootElement_SupportTicket class attributes and methods
RootElement_SupportTicket_problemDescription: Property = Property(name="problemDescription", type=StringType)
RootElement_SupportTicket_roomName: Property = Property(name="roomName", type=StringType)
RootElement_SupportTicket_fixed: Property = Property(name="fixed", type=StringType)
RootElement_SupportTicket.attributes={RootElement_SupportTicket_fixed, RootElement_SupportTicket_roomName, RootElement_SupportTicket_problemDescription}

# Staff class attributes and methods

# ReceptionHandling class attributes and methods

# ServiceItemHandling class attributes and methods

# Payment class attributes and methods

# RootElement_ReceptionHandling class attributes and methods
RootElement_ReceptionHandling_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='booking')}, type=StringType)
RootElement_ReceptionHandling_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')}, type=StringType)
RootElement_ReceptionHandling_m_findBookings: Method = Method(name="findBookings", parameters={Parameter(name='name')}, type=StringType)
RootElement_ReceptionHandling_m_findActiveBooking: Method = Method(name="findActiveBooking", parameters={Parameter(name='roomName')}, type=StringType)
RootElement_ReceptionHandling.methods={RootElement_ReceptionHandling_m_findActiveBooking, RootElement_ReceptionHandling_m_checkOut, RootElement_ReceptionHandling_m_checkIn, RootElement_ReceptionHandling_m_findBookings}

# RootElement_ServiceItemHandling class attributes and methods
RootElement_ServiceItemHandling_m_addServiceItem: Method = Method(name="addServiceItem", parameters={Parameter(name='description'), Parameter(name='booking'), Parameter(name='price'), Parameter(name='name')})
RootElement_ServiceItemHandling_m_findAllServiceItems: Method = Method(name="findAllServiceItems", parameters={Parameter(name='booking')}, type=StringType)
RootElement_ServiceItemHandling_m_removeServiceItem: Method = Method(name="removeServiceItem", parameters={Parameter(name='booking'), Parameter(name='serviceItem')})
RootElement_ServiceItemHandling.methods={RootElement_ServiceItemHandling_m_findAllServiceItems, RootElement_ServiceItemHandling_m_addServiceItem, RootElement_ServiceItemHandling_m_removeServiceItem}

# RootElement_Clerk class attributes and methods

# RootElement_Payment class attributes and methods
RootElement_Payment_m_verifyCreditCard: Method = Method(name="verifyCreditCard", parameters={Parameter(name='creditCard')}, type=StringType)
RootElement_Payment_m_debitCard: Method = Method(name="debitCard", parameters={Parameter(name='creditCard'), Parameter(name='amount')}, type=StringType)
RootElement_Payment.methods={RootElement_Payment_m_debitCard, RootElement_Payment_m_verifyCreditCard}

# RootElement_Manager class attributes and methods

# Clerk class attributes and methods

# SysAdmin class attributes and methods

# FeedbackReader class attributes and methods

# RootElement_FeedbackReader class attributes and methods
RootElement_FeedbackReader_m_getAllFeedback: Method = Method(name="getAllFeedback", parameters={}, type=StringType)
RootElement_FeedbackReader_m_getUnreadFeedback: Method = Method(name="getUnreadFeedback", parameters={}, type=StringType)
RootElement_FeedbackReader.methods={RootElement_FeedbackReader_m_getAllFeedback, RootElement_FeedbackReader_m_getUnreadFeedback}

# RootElement_SysAdmin class attributes and methods

# RoomAttributeHandling class attributes and methods

# RoomHandling class attributes and methods

# RoomTypeHandling class attributes and methods

# RootElement_RoomAttributeHandling class attributes and methods
RootElement_RoomAttributeHandling_m_addRoomAttribute: Method = Method(name="addRoomAttribute", parameters={Parameter(name='description'), Parameter(name='name')}, type=StringType)
RootElement_RoomAttributeHandling_m_editRoomAttribute: Method = Method(name="editRoomAttribute", parameters={Parameter(name='roomAttribute'), Parameter(name='newName'), Parameter(name='newDescription')}, type=StringType)
RootElement_RoomAttributeHandling_m_removeRoomAttribute: Method = Method(name="removeRoomAttribute", parameters={Parameter(name='roomAttribute')}, type=StringType)
RootElement_RoomAttributeHandling_m_getAllRoomAttributes: Method = Method(name="getAllRoomAttributes", parameters={}, type=StringType)
RootElement_RoomAttributeHandling_m_findRoomAttribute: Method = Method(name="findRoomAttribute", parameters={Parameter(name='name')}, type=StringType)
RootElement_RoomAttributeHandling.methods={RootElement_RoomAttributeHandling_m_findRoomAttribute, RootElement_RoomAttributeHandling_m_getAllRoomAttributes, RootElement_RoomAttributeHandling_m_addRoomAttribute, RootElement_RoomAttributeHandling_m_removeRoomAttribute, RootElement_RoomAttributeHandling_m_editRoomAttribute}

# RootElement_RoomHandling class attributes and methods
RootElement_RoomHandling_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='roomType'), Parameter(name='roomName')}, type=StringType)
RootElement_RoomHandling_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='room')}, type=StringType)
RootElement_RoomHandling_m_editRoom: Method = Method(name="editRoom", parameters={Parameter(name='newRoomName'), Parameter(name='room'), Parameter(name='newRoomType')}, type=StringType)
RootElement_RoomHandling_m_findRoom: Method = Method(name="findRoom", parameters={Parameter(name='roomName')}, type=StringType)
RootElement_RoomHandling_m_getAllRooms: Method = Method(name="getAllRooms", parameters={}, type=StringType)
RootElement_RoomHandling.methods={RootElement_RoomHandling_m_removeRoom, RootElement_RoomHandling_m_findRoom, RootElement_RoomHandling_m_addRoom, RootElement_RoomHandling_m_getAllRooms, RootElement_RoomHandling_m_editRoom}

# RootElement_RoomTypeHandling class attributes and methods
RootElement_RoomTypeHandling_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='name'), Parameter(name='capacity'), Parameter(name='cost')}, type=StringType)
RootElement_RoomTypeHandling_m_editRoomType: Method = Method(name="editRoomType", parameters={Parameter(name='newName'), Parameter(name='roomType'), Parameter(name='newCapacity'), Parameter(name='newCost')}, type=StringType)
RootElement_RoomTypeHandling_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='roomType')}, type=StringType)
RootElement_RoomTypeHandling_m_getAllRoomTypes: Method = Method(name="getAllRoomTypes", parameters={}, type=StringType)
RootElement_RoomTypeHandling_m_addAttributeToRoomType: Method = Method(name="addAttributeToRoomType", parameters={Parameter(name='roomAttribute'), Parameter(name='roomType')}, type=StringType)
RootElement_RoomTypeHandling_m_removeAttributeFromRoomType: Method = Method(name="removeAttributeFromRoomType", parameters={Parameter(name='roomType'), Parameter(name='roomAttribute')}, type=StringType)
RootElement_RoomTypeHandling_m_findRoomType: Method = Method(name="findRoomType", parameters={Parameter(name='name')}, type=StringType)
RootElement_RoomTypeHandling.methods={RootElement_RoomTypeHandling_m_removeAttributeFromRoomType, RootElement_RoomTypeHandling_m_addAttributeToRoomType, RootElement_RoomTypeHandling_m_addRoomType, RootElement_RoomTypeHandling_m_findRoomType, RootElement_RoomTypeHandling_m_removeRoomType, RootElement_RoomTypeHandling_m_editRoomType, RootElement_RoomTypeHandling_m_getAllRoomTypes}

# RootElement_BookingHandler class attributes and methods

# RootElement_RoomFetcher class attributes and methods
RootElement_RoomFetcher_m_getBookableRooms: Method = Method(name="getBookableRooms", parameters={}, type=StringType)
RootElement_RoomFetcher_m_getAllCleanableRooms: Method = Method(name="getAllCleanableRooms", parameters={}, type=StringType)
RootElement_RoomFetcher_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={}, type=StringType)
RootElement_RoomFetcher.methods={RootElement_RoomFetcher_m_getAllCleanableRooms, RootElement_RoomFetcher_m_getAvailableRooms, RootElement_RoomFetcher_m_getBookableRooms}

# RootElement_RoomStructure class attributes and methods

# RootElement_FeedbackHandler class attributes and methods

# RootElement_SupportTicketHandler class attributes and methods

# RootElement_CleaningHandler class attributes and methods

# RootElement_PaymentHandler class attributes and methods

# RootElement_DailyRoomBooking class attributes and methods
RootElement_DailyRoomBooking_nbrOfGuests: Property = Property(name="nbrOfGuests", type=StringType)
RootElement_DailyRoomBooking.attributes={RootElement_DailyRoomBooking_nbrOfGuests}

# RoomBooking class attributes and methods

# RoomFetcher class attributes and methods

# RootElement_HourlyRoomBooking class attributes and methods

# RootElement_HotelSystem class attributes and methods
RootElement_HotelSystem_m_getStaff: Method = Method(name="getStaff", parameters={Parameter(name='staffID')}, type=Staff)
RootElement_HotelSystem_m_getClerk: Method = Method(name="getClerk", parameters={Parameter(name='staffID')}, type=Clerk)
RootElement_HotelSystem_m_getManager: Method = Method(name="getManager", parameters={Parameter(name='staffID')}, type=StringType)
RootElement_HotelSystem_m_getSystemAdministrator: Method = Method(name="getSystemAdministrator", parameters={}, type=SysAdmin)
RootElement_HotelSystem_m_getGuest: Method = Method(name="getGuest", parameters={}, type=StringType)
RootElement_HotelSystem_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
RootElement_HotelSystem_m_getNationality: Method = Method(name="getNationality", parameters={}, type=StringType)
RootElement_HotelSystem.methods={RootElement_HotelSystem_m_getNationality, RootElement_HotelSystem_m_getName, RootElement_HotelSystem_m_getSystemAdministrator, RootElement_HotelSystem_m_getClerk, RootElement_HotelSystem_m_getManager, RootElement_HotelSystem_m_getGuest, RootElement_HotelSystem_m_getStaff}

# RootElement_Hotel class attributes and methods

# HotelSystem class attributes and methods

# Relationships
supportTicketWriter0: BinaryAssociation = BinaryAssociation(
    name="supportTicketWriter0",
    ends={
        Property(name="RootElement_SupportTicketWriter", type=RootElement_Guest, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Guest", type=RootElement_SupportTicketWriter, multiplicity=Multiplicity(1, 1))
    }
)
makeBooking1: BinaryAssociation = BinaryAssociation(
    name="makeBooking1",
    ends={
        Property(name="RootElement_MakeBooking", type=RootElement_Guest, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Guest2", type=RootElement_MakeBooking, multiplicity=Multiplicity(1, 1))
    }
)
feedbackWriter3: BinaryAssociation = BinaryAssociation(
    name="feedbackWriter3",
    ends={
        Property(name="RootElement_FeedbackWriter", type=RootElement_Guest, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Guest4", type=RootElement_FeedbackWriter, multiplicity=Multiplicity(1, 1))
    }
)
roombooking5: BinaryAssociation = BinaryAssociation(
    name="roombooking5",
    ends={
        Property(name="RootElement_RoomBooking", type=RootElement_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Booking", type=RootElement_RoomBooking, multiplicity=Multiplicity(0, 9999))
    }
)
guest6: BinaryAssociation = BinaryAssociation(
    name="guest6",
    ends={
        Property(name="RootElement_Guest8", type=RootElement_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Booking7", type=RootElement_Guest, multiplicity=Multiplicity(1, 1))
    }
)
serviceitem9: BinaryAssociation = BinaryAssociation(
    name="serviceitem9",
    ends={
        Property(name="RootElement_ServiceItem", type=RootElement_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Booking10", type=RootElement_ServiceItem, multiplicity=Multiplicity(0, 9999))
    }
)
room11: BinaryAssociation = BinaryAssociation(
    name="room11",
    ends={
        Property(name="RootElement_Room", type=RootElement_RoomBooking, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_RoomBooking12", type=RootElement_Room, multiplicity=Multiplicity(1, 1))
    }
)
roomType13: BinaryAssociation = BinaryAssociation(
    name="roomType13",
    ends={
        Property(name="RootElement_RoomType", type=RootElement_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Room14", type=RootElement_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
roomAttributes15: BinaryAssociation = BinaryAssociation(
    name="roomAttributes15",
    ends={
        Property(name="RootElement_RoomAttribute", type=RootElement_RoomType, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_RoomType16", type=RootElement_RoomAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
cleaning17: BinaryAssociation = BinaryAssociation(
    name="cleaning17",
    ends={
        Property(name="RootElement_Cleaning", type=RootElement_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Staff", type=RootElement_Cleaning, multiplicity=Multiplicity(1, 1))
    }
)
supportTicketReader18: BinaryAssociation = BinaryAssociation(
    name="supportTicketReader18",
    ends={
        Property(name="RootElement_SupportTicketReader", type=RootElement_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Staff19", type=RootElement_SupportTicketReader, multiplicity=Multiplicity(1, 1))
    }
)
supportTicketWriter20: BinaryAssociation = BinaryAssociation(
    name="supportTicketWriter20",
    ends={
        Property(name="RootElement_SupportTicketWriter22", type=RootElement_Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Staff21", type=RootElement_SupportTicketWriter, multiplicity=Multiplicity(1, 1))
    }
)
receptionHandling23: BinaryAssociation = BinaryAssociation(
    name="receptionHandling23",
    ends={
        Property(name="RootElement_ReceptionHandling", type=RootElement_Clerk, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Clerk", type=RootElement_ReceptionHandling, multiplicity=Multiplicity(1, 1))
    }
)
serviceItemHandling24: BinaryAssociation = BinaryAssociation(
    name="serviceItemHandling24",
    ends={
        Property(name="RootElement_ServiceItemHandling", type=RootElement_Clerk, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Clerk25", type=RootElement_ServiceItemHandling, multiplicity=Multiplicity(1, 1))
    }
)
payment29: BinaryAssociation = BinaryAssociation(
    name="payment29",
    ends={
        Property(name="RootElement_Payment", type=RootElement_Clerk, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Clerk30", type=RootElement_Payment, multiplicity=Multiplicity(1, 1))
    }
)
makeBooking26: BinaryAssociation = BinaryAssociation(
    name="makeBooking26",
    ends={
        Property(name="RootElement_MakeBooking28", type=RootElement_Clerk, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Clerk27", type=RootElement_MakeBooking, multiplicity=Multiplicity(1, 1))
    }
)
feedbackReader31: BinaryAssociation = BinaryAssociation(
    name="feedbackReader31",
    ends={
        Property(name="RootElement_FeedbackReader", type=RootElement_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_Manager", type=RootElement_FeedbackReader, multiplicity=Multiplicity(1, 1))
    }
)
booking32: BinaryAssociation = BinaryAssociation(
    name="booking32",
    ends={
        Property(name="RootElement_Booking33", type=RootElement_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_BookingHandler", type=RootElement_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
roomFetcher34: BinaryAssociation = BinaryAssociation(
    name="roomFetcher34",
    ends={
        Property(name="RootElement_RoomFetcher", type=RootElement_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_BookingHandler35", type=RootElement_RoomFetcher, multiplicity=Multiplicity(1, 1))
    }
)
rooms36: BinaryAssociation = BinaryAssociation(
    name="rooms36",
    ends={
        Property(name="RootElement_Room37", type=RootElement_RoomStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_RoomStructure", type=RootElement_Room, multiplicity=Multiplicity(0, 9999))
    }
)
roomTypes38: BinaryAssociation = BinaryAssociation(
    name="roomTypes38",
    ends={
        Property(name="RootElement_RoomType40", type=RootElement_RoomStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_RoomStructure39", type=RootElement_RoomType, multiplicity=Multiplicity(0, 9999))
    }
)
roomAttributes41: BinaryAssociation = BinaryAssociation(
    name="roomAttributes41",
    ends={
        Property(name="RootElement_RoomAttribute43", type=RootElement_RoomStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_RoomStructure42", type=RootElement_RoomAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
feedback44: BinaryAssociation = BinaryAssociation(
    name="feedback44",
    ends={
        Property(name="RootElement_Feedback", type=RootElement_FeedbackHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_FeedbackHandler", type=RootElement_Feedback, multiplicity=Multiplicity(0, 9999))
    }
)
supportticket45: BinaryAssociation = BinaryAssociation(
    name="supportticket45",
    ends={
        Property(name="RootElement_SupportTicket", type=RootElement_SupportTicketHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_SupportTicketHandler", type=RootElement_SupportTicket, multiplicity=Multiplicity(0, 9999))
    }
)
roomFetcher46: BinaryAssociation = BinaryAssociation(
    name="roomFetcher46",
    ends={
        Property(name="RootElement_RoomFetcher47", type=RootElement_CleaningHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="RootElement_CleaningHandler", type=RootElement_RoomFetcher, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RootElement_Guest_SupportTicketWriter = Generalization(general=SupportTicketWriter, specific=RootElement_Guest)
gen_RootElement_Guest_FeedbackWriter = Generalization(general=FeedbackWriter, specific=RootElement_Guest)
gen_RootElement_Guest_MakeBooking = Generalization(general=MakeBooking, specific=RootElement_Guest)
gen_RootElement_Staff_SupportTicketWriter = Generalization(general=SupportTicketWriter, specific=RootElement_Staff)
gen_RootElement_Staff_SupportTicketReader = Generalization(general=SupportTicketReader, specific=RootElement_Staff)
gen_RootElement_Staff_Cleaning = Generalization(general=Cleaning, specific=RootElement_Staff)
gen_RootElement_Clerk_Staff = Generalization(general=Staff, specific=RootElement_Clerk)
gen_RootElement_Clerk_ReceptionHandling = Generalization(general=ReceptionHandling, specific=RootElement_Clerk)
gen_RootElement_Clerk_ServiceItemHandling = Generalization(general=ServiceItemHandling, specific=RootElement_Clerk)
gen_RootElement_Clerk_MakeBooking = Generalization(general=MakeBooking, specific=RootElement_Clerk)
gen_RootElement_Clerk_Payment = Generalization(general=Payment, specific=RootElement_Clerk)
gen_RootElement_Manager_Clerk = Generalization(general=Clerk, specific=RootElement_Manager)
gen_RootElement_Manager_SysAdmin = Generalization(general=SysAdmin, specific=RootElement_Manager)
gen_RootElement_Manager_FeedbackReader = Generalization(general=FeedbackReader, specific=RootElement_Manager)
gen_RootElement_SysAdmin_RoomAttributeHandling = Generalization(general=RoomAttributeHandling, specific=RootElement_SysAdmin)
gen_RootElement_SysAdmin_RoomHandling = Generalization(general=RoomHandling, specific=RootElement_SysAdmin)
gen_RootElement_SysAdmin_RoomTypeHandling = Generalization(general=RoomTypeHandling, specific=RootElement_SysAdmin)
gen_RootElement_BookingHandler_ReceptionHandling = Generalization(general=ReceptionHandling, specific=RootElement_BookingHandler)
gen_RootElement_BookingHandler_MakeBooking = Generalization(general=MakeBooking, specific=RootElement_BookingHandler)
gen_RootElement_BookingHandler_ServiceItemHandling = Generalization(general=ServiceItemHandling, specific=RootElement_BookingHandler)
gen_RootElement_RoomStructure_RoomHandling = Generalization(general=RoomHandling, specific=RootElement_RoomStructure)
gen_RootElement_FeedbackHandler_FeedbackReader = Generalization(general=FeedbackReader, specific=RootElement_FeedbackHandler)
gen_RootElement_FeedbackHandler_FeedbackWriter = Generalization(general=FeedbackWriter, specific=RootElement_FeedbackHandler)
gen_RootElement_SupportTicketHandler_SupportTicketReader = Generalization(general=SupportTicketReader, specific=RootElement_SupportTicketHandler)
gen_RootElement_SupportTicketHandler_SupportTicketWriter = Generalization(general=SupportTicketWriter, specific=RootElement_SupportTicketHandler)
gen_RootElement_CleaningHandler_Cleaning = Generalization(general=Cleaning, specific=RootElement_CleaningHandler)
gen_RootElement_PaymentHandler_Payment = Generalization(general=Payment, specific=RootElement_PaymentHandler)
gen_RootElement_RoomStructure_RoomTypeHandling = Generalization(general=RoomTypeHandling, specific=RootElement_RoomStructure)
gen_RootElement_RoomStructure_RoomAttributeHandling = Generalization(general=RoomAttributeHandling, specific=RootElement_RoomStructure)
gen_RootElement_RoomStructure_RoomFetcher = Generalization(general=RoomFetcher, specific=RootElement_RoomStructure)
gen_RootElement_HourlyRoomBooking_RoomBooking = Generalization(general=RoomBooking, specific=RootElement_HourlyRoomBooking)
gen_RootElement_Hotel_HotelSystem = Generalization(general=HotelSystem, specific=RootElement_Hotel)
gen_RootElement_DailyRoomBooking_RoomBooking = Generalization(general=RoomBooking, specific=RootElement_DailyRoomBooking)

# Domain Model
domain_model = DomainModel(
    name="RootElement",
    types={RootElement_Guest, SupportTicketWriter, FeedbackWriter, MakeBooking, RootElement_SupportTicketWriter, RootElement_MakeBooking, RootElement_FeedbackWriter, RootElement_Booking, RootElement_RoomBooking, RootElement_ServiceItem, RootElement_Room, RootElement_RoomType, RootElement_RoomAttribute, SupportTicketReader, RootElement_Feedback, RootElement_Staff, Cleaning, RootElement_Cleaning, RootElement_SupportTicketReader, RootElement_SupportTicket, Staff, ReceptionHandling, ServiceItemHandling, Payment, RootElement_ReceptionHandling, RootElement_ServiceItemHandling, RootElement_Clerk, RootElement_Payment, RootElement_Manager, Clerk, SysAdmin, FeedbackReader, RootElement_FeedbackReader, RootElement_SysAdmin, RoomAttributeHandling, RoomHandling, RoomTypeHandling, RootElement_RoomAttributeHandling, RootElement_RoomHandling, RootElement_RoomTypeHandling, RootElement_BookingHandler, RootElement_RoomFetcher, RootElement_RoomStructure, RootElement_FeedbackHandler, RootElement_SupportTicketHandler, RootElement_CleaningHandler, RootElement_PaymentHandler, RootElement_DailyRoomBooking, RoomBooking, RoomFetcher, RootElement_HourlyRoomBooking, RootElement_HotelSystem, RootElement_Hotel, HotelSystem, BookingStatus},
    associations={supportTicketWriter0, makeBooking1, feedbackWriter3, roombooking5, guest6, serviceitem9, room11, roomType13, roomAttributes15, cleaning17, supportTicketReader18, supportTicketWriter20, receptionHandling23, serviceItemHandling24, payment29, makeBooking26, feedbackReader31, booking32, roomFetcher34, rooms36, roomTypes38, roomAttributes41, feedback44, supportticket45, roomFetcher46},
    generalizations={gen_RootElement_Guest_SupportTicketWriter, gen_RootElement_Guest_FeedbackWriter, gen_RootElement_Guest_MakeBooking, gen_RootElement_Staff_SupportTicketWriter, gen_RootElement_Staff_SupportTicketReader, gen_RootElement_Staff_Cleaning, gen_RootElement_Clerk_Staff, gen_RootElement_Clerk_ReceptionHandling, gen_RootElement_Clerk_ServiceItemHandling, gen_RootElement_Clerk_MakeBooking, gen_RootElement_Clerk_Payment, gen_RootElement_Manager_Clerk, gen_RootElement_Manager_SysAdmin, gen_RootElement_Manager_FeedbackReader, gen_RootElement_SysAdmin_RoomAttributeHandling, gen_RootElement_SysAdmin_RoomHandling, gen_RootElement_SysAdmin_RoomTypeHandling, gen_RootElement_BookingHandler_ReceptionHandling, gen_RootElement_BookingHandler_MakeBooking, gen_RootElement_BookingHandler_ServiceItemHandling, gen_RootElement_RoomStructure_RoomHandling, gen_RootElement_FeedbackHandler_FeedbackReader, gen_RootElement_FeedbackHandler_FeedbackWriter, gen_RootElement_SupportTicketHandler_SupportTicketReader, gen_RootElement_SupportTicketHandler_SupportTicketWriter, gen_RootElement_CleaningHandler_Cleaning, gen_RootElement_PaymentHandler_Payment, gen_RootElement_RoomStructure_RoomTypeHandling, gen_RootElement_RoomStructure_RoomAttributeHandling, gen_RootElement_RoomStructure_RoomFetcher, gen_RootElement_HourlyRoomBooking_RoomBooking, gen_RootElement_Hotel_HotelSystem, gen_RootElement_DailyRoomBooking_RoomBooking},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)