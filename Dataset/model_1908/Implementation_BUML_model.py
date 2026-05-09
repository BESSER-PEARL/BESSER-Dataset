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
Implementation_DecisionSupportComponent = Class(name="Implementation_DecisionSupportComponent")
DecisionSupportComponent_IDecisionSupport = Class(name="DecisionSupportComponent_IDecisionSupport")
Implementation_DecisionSupportComponent_IDecisionSupport = Class(name="Implementation_DecisionSupportComponent_IDecisionSupport", is_abstract=True)
Implementation_OccupancyComponent_IOccupancyDecision = Class(name="Implementation_OccupancyComponent_IOccupancyDecision", is_abstract=True)
Implementation_BookingComponent_IBookingDecision = Class(name="Implementation_BookingComponent_IBookingDecision", is_abstract=True)
Implementation_DecisionSupportComponent_BookingDSSInfo = Class(name="Implementation_DecisionSupportComponent_BookingDSSInfo")
Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo = Class(name="Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo")
Implementation_DecisionSupportComponent_DSSController = Class(name="Implementation_DecisionSupportComponent_DSSController")
Implementation_OccupancyComponent_Occupancy = Class(name="Implementation_OccupancyComponent_Occupancy")
Implementation_DecisionSupportComponent_OccupancyDSSInfo = Class(name="Implementation_DecisionSupportComponent_OccupancyDSSInfo")
Implementation_OccupancyComponent = Class(name="Implementation_OccupancyComponent")
Implementation_OccupancyComponent_OccupancyHandler = Class(name="Implementation_OccupancyComponent_OccupancyHandler")
OccupancyComponent_IOccupancyDecision = Class(name="OccupancyComponent_IOccupancyDecision")
OccupancyComponent_IOccupancy = Class(name="OccupancyComponent_IOccupancy")
Implementation_RoomComponent_IRoomInformation = Class(name="Implementation_RoomComponent_IRoomInformation", is_abstract=True)
Implementation_OccupancyComponent_Guest = Class(name="Implementation_OccupancyComponent_Guest")
Implementation_OccupancyComponent_IOccupancy = Class(name="Implementation_OccupancyComponent_IOccupancy", is_abstract=True)
Implementation_PaymentComponent = Class(name="Implementation_PaymentComponent")
PaymentComponent_IPayment = Class(name="PaymentComponent_IPayment")
Implementation_PaymentComponent_IPayment = Class(name="Implementation_PaymentComponent_IPayment", is_abstract=True)
Implementation_BookingComponent_IBookingInformation = Class(name="Implementation_BookingComponent_IBookingInformation", is_abstract=True)
Implementation_Bank_CustomerProvides = Class(name="Implementation_Bank_CustomerProvides", is_abstract=True)
Implementation_Bank_AdministratorProvides = Class(name="Implementation_Bank_AdministratorProvides", is_abstract=True)
Implementation_PaymentComponent_PaymentHandler = Class(name="Implementation_PaymentComponent_PaymentHandler")
Implementation_PaymentComponent_Payment = Class(name="Implementation_PaymentComponent_Payment")
Implementation_AdditionalServiceComponent = Class(name="Implementation_AdditionalServiceComponent")
AdditionalServiceComponent_IAdditionalServiceAdministration = Class(name="AdditionalServiceComponent_IAdditionalServiceAdministration")
AdditionalServiceComponent_IEventManagement = Class(name="AdditionalServiceComponent_IEventManagement")
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration = Class(name="Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration", is_abstract=True)
Implementation_AdditionalServiceComponent_IEventManagement = Class(name="Implementation_AdditionalServiceComponent_IEventManagement", is_abstract=True)
Implementation_StaffComponent_IAuthentication = Class(name="Implementation_StaffComponent_IAuthentication", is_abstract=True)
Implementation_AdditionalServiceComponent_AdditionalService = Class(name="Implementation_AdditionalServiceComponent_AdditionalService")
Implementation_AdditionalServiceComponent_AdditionalServiceEvent = Class(name="Implementation_AdditionalServiceComponent_AdditionalServiceEvent")
Implementation_AdditionalServiceComponent_AdditionalServiceHandler = Class(name="Implementation_AdditionalServiceComponent_AdditionalServiceHandler")
Implementation_BookingComponent = Class(name="Implementation_BookingComponent")
Implementation_BookingComponent_PaymentDetails = Class(name="Implementation_BookingComponent_PaymentDetails")
Implementation_BookingComponent_Booking = Class(name="Implementation_BookingComponent_Booking")
Implementation_BookingComponent_AdditionalService = Class(name="Implementation_BookingComponent_AdditionalService")
Implementation_BookingComponent_BookingGuest = Class(name="Implementation_BookingComponent_BookingGuest")
Implementation_BookingComponent_RoomType = Class(name="Implementation_BookingComponent_RoomType")
Implementation_BookingComponent_BookingHandler = Class(name="Implementation_BookingComponent_BookingHandler")
BookingComponent_IBookingInformation = Class(name="BookingComponent_IBookingInformation")
BookingComponent_IBookingDecision = Class(name="BookingComponent_IBookingDecision")
BookingComponent_IBookingAdministration = Class(name="BookingComponent_IBookingAdministration")
Implementation_BookingComponent_IBookingAdministration = Class(name="Implementation_BookingComponent_IBookingAdministration", is_abstract=True)
Implementation_StaffComponent = Class(name="Implementation_StaffComponent")
StaffComponent_IAccountAdministration = Class(name="StaffComponent_IAccountAdministration")
StaffComponent_IAuthentication = Class(name="StaffComponent_IAuthentication")
Implementation_StaffComponent_IAccountAdministration = Class(name="Implementation_StaffComponent_IAccountAdministration", is_abstract=True)
Implementation_StaffComponent_AccountManager = Class(name="Implementation_StaffComponent_AccountManager")
Implementation_StaffComponent_Employee = Class(name="Implementation_StaffComponent_Employee")
Implementation_RoomComponent = Class(name="Implementation_RoomComponent")
RoomComponent_IRoomInformation = Class(name="RoomComponent_IRoomInformation")
RoomComponent_IRoomAdministration = Class(name="RoomComponent_IRoomAdministration")
Implementation_RoomComponent_IRoomAdministration = Class(name="Implementation_RoomComponent_IRoomAdministration", is_abstract=True)
Implementation_Bank = Class(name="Implementation_Bank")
Implementation_RoomComponent_Room = Class(name="Implementation_RoomComponent_Room")
Implementation_RoomComponent_Bedroom = Class(name="Implementation_RoomComponent_Bedroom")
RoomComponent_Room = Class(name="RoomComponent_Room")
Implementation_RoomComponent_ConferenceRoom = Class(name="Implementation_RoomComponent_ConferenceRoom")
Implementation_RoomComponent_RoomHandler = Class(name="Implementation_RoomComponent_RoomHandler")

# Implementation_DecisionSupportComponent class attributes and methods

# DecisionSupportComponent_IDecisionSupport class attributes and methods

# Implementation_DecisionSupportComponent_IDecisionSupport class attributes and methods
Implementation_DecisionSupportComponent_IDecisionSupport_m_getDSSData: Method = Method(name="getDSSData", parameters={})
Implementation_DecisionSupportComponent_IDecisionSupport_m_getAllRoomTypeFrequency: Method = Method(name="getAllRoomTypeFrequency", parameters={}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport_m_getRoomTypeFrequency: Method = Method(name="getRoomTypeFrequency", parameters={Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport_m_countRoomType: Method = Method(name="countRoomType", parameters={Parameter(name='Implementation_bookingDSSInfo', type=StringType), Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport_m_getAllCustomerBookingFrequency: Method = Method(name="getAllCustomerBookingFrequency", parameters={}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport_m_getCustomerBookingFrequency: Method = Method(name="getCustomerBookingFrequency", parameters={Parameter(name='Implementation_customerSSN', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport_m_getDSSOccupancyInfo: Method = Method(name="getDSSOccupancyInfo", parameters={})
Implementation_DecisionSupportComponent_IDecisionSupport_m_getNumberOfOccupanciesOfRoom: Method = Method(name="getNumberOfOccupanciesOfRoom", parameters={Parameter(name='Implementation_roomNumber', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_IDecisionSupport.methods={Implementation_DecisionSupportComponent_IDecisionSupport_m_getAllRoomTypeFrequency, Implementation_DecisionSupportComponent_IDecisionSupport_m_getRoomTypeFrequency, Implementation_DecisionSupportComponent_IDecisionSupport_m_getNumberOfOccupanciesOfRoom, Implementation_DecisionSupportComponent_IDecisionSupport_m_getAllCustomerBookingFrequency, Implementation_DecisionSupportComponent_IDecisionSupport_m_countRoomType, Implementation_DecisionSupportComponent_IDecisionSupport_m_getDSSOccupancyInfo, Implementation_DecisionSupportComponent_IDecisionSupport_m_getCustomerBookingFrequency, Implementation_DecisionSupportComponent_IDecisionSupport_m_getDSSData}

# Implementation_OccupancyComponent_IOccupancyDecision class attributes and methods
Implementation_OccupancyComponent_IOccupancyDecision_m_getDSSOccupancyInfo: Method = Method(name="getDSSOccupancyInfo", parameters={}, type=StringType)
Implementation_OccupancyComponent_IOccupancyDecision.methods={Implementation_OccupancyComponent_IOccupancyDecision_m_getDSSOccupancyInfo}

# Implementation_BookingComponent_IBookingDecision class attributes and methods
Implementation_BookingComponent_IBookingDecision_m_getDSSInfo: Method = Method(name="getDSSInfo", parameters={}, type=StringType)
Implementation_BookingComponent_IBookingDecision.methods={Implementation_BookingComponent_IBookingDecision_m_getDSSInfo}

# Implementation_DecisionSupportComponent_BookingDSSInfo class attributes and methods
Implementation_DecisionSupportComponent_BookingDSSInfo_numberOfGuests: Property = Property(name="numberOfGuests", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_roomType: Property = Property(name="roomType", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_arrivalDate: Property = Property(name="arrivalDate", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_departureDate: Property = Property(name="departureDate", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_customerFirstName: Property = Property(name="customerFirstName", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_customerLastName: Property = Property(name="customerLastName", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_address: Property = Property(name="address", type=StringType)
Implementation_DecisionSupportComponent_BookingDSSInfo_m_addAdditionalService: Method = Method(name="addAdditionalService", parameters={Parameter(name='Implementation_additionalServicePrice', type=StringType), Parameter(name='Implementation_additionalServiceName', type=StringType)})
Implementation_DecisionSupportComponent_BookingDSSInfo.attributes={Implementation_DecisionSupportComponent_BookingDSSInfo_roomType, Implementation_DecisionSupportComponent_BookingDSSInfo_arrivalDate, Implementation_DecisionSupportComponent_BookingDSSInfo_customerLastName, Implementation_DecisionSupportComponent_BookingDSSInfo_numberOfGuests, Implementation_DecisionSupportComponent_BookingDSSInfo_departureDate, Implementation_DecisionSupportComponent_BookingDSSInfo_address, Implementation_DecisionSupportComponent_BookingDSSInfo_customerFirstName}
Implementation_DecisionSupportComponent_BookingDSSInfo.methods={Implementation_DecisionSupportComponent_BookingDSSInfo_m_addAdditionalService}

# Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo class attributes and methods
Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo_additionalServiceName: Property = Property(name="additionalServiceName", type=StringType)
Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo_additionalServicePrice: Property = Property(name="additionalServicePrice", type=StringType)
Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo.attributes={Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo_additionalServiceName, Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo_additionalServicePrice}

# Implementation_DecisionSupportComponent_DSSController class attributes and methods
Implementation_DecisionSupportComponent_DSSController_m_countCustomerBooking: Method = Method(name="countCustomerBooking", parameters={Parameter(name='Implementation_bookingDSSInfo', type=StringType), Parameter(name='Implementation_customerSSN', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_DSSController_m_getPositionInList: Method = Method(name="getPositionInList", parameters={Parameter(name='Implementation_element', type=StringType), Parameter(name='Implementation_listToCheck', type=StringType)}, type=StringType)
Implementation_DecisionSupportComponent_DSSController.methods={Implementation_DecisionSupportComponent_DSSController_m_getPositionInList, Implementation_DecisionSupportComponent_DSSController_m_countCustomerBooking}

# Implementation_OccupancyComponent_Occupancy class attributes and methods
Implementation_OccupancyComponent_Occupancy_roomNumber: Property = Property(name="roomNumber", type=StringType)
Implementation_OccupancyComponent_Occupancy_checkInDateTime: Property = Property(name="checkInDateTime", type=StringType)
Implementation_OccupancyComponent_Occupancy_checkOutDateTime: Property = Property(name="checkOutDateTime", type=StringType)
Implementation_OccupancyComponent_Occupancy_bookingReference: Property = Property(name="bookingReference", type=StringType)
Implementation_OccupancyComponent_Occupancy_m_getPartner: Method = Method(name="getPartner", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_Occupancy_m_addGuestToOccupancy: Method = Method(name="addGuestToOccupancy", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_Occupancy_m_listGuests: Method = Method(name="listGuests", parameters={}, type=StringType)
Implementation_OccupancyComponent_Occupancy.attributes={Implementation_OccupancyComponent_Occupancy_roomNumber, Implementation_OccupancyComponent_Occupancy_checkOutDateTime, Implementation_OccupancyComponent_Occupancy_checkInDateTime, Implementation_OccupancyComponent_Occupancy_bookingReference}
Implementation_OccupancyComponent_Occupancy.methods={Implementation_OccupancyComponent_Occupancy_m_getPartner, Implementation_OccupancyComponent_Occupancy_m_addGuestToOccupancy, Implementation_OccupancyComponent_Occupancy_m_listGuests}

# Implementation_DecisionSupportComponent_OccupancyDSSInfo class attributes and methods
Implementation_DecisionSupportComponent_OccupancyDSSInfo_roomNumber: Property = Property(name="roomNumber", type=StringType)
Implementation_DecisionSupportComponent_OccupancyDSSInfo_checkInDateTime: Property = Property(name="checkInDateTime", type=StringType)
Implementation_DecisionSupportComponent_OccupancyDSSInfo_checkOutDateTime: Property = Property(name="checkOutDateTime", type=StringType)
Implementation_DecisionSupportComponent_OccupancyDSSInfo_numberOfGuests: Property = Property(name="numberOfGuests", type=StringType)
Implementation_DecisionSupportComponent_OccupancyDSSInfo.attributes={Implementation_DecisionSupportComponent_OccupancyDSSInfo_checkOutDateTime, Implementation_DecisionSupportComponent_OccupancyDSSInfo_roomNumber, Implementation_DecisionSupportComponent_OccupancyDSSInfo_checkInDateTime, Implementation_DecisionSupportComponent_OccupancyDSSInfo_numberOfGuests}

# Implementation_OccupancyComponent class attributes and methods

# Implementation_OccupancyComponent_OccupancyHandler class attributes and methods
Implementation_OccupancyComponent_OccupancyHandler_m_findOccupancy: Method = Method(name="findOccupancy", parameters={Parameter(name='Implementation_partnerLastName', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_partnerFirstName', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_OccupancyHandler_m_isInRoomTypes: Method = Method(name="isInRoomTypes", parameters={Parameter(name='Implementation_roomTypes', type=StringType), Parameter(name='Implementation_guestInRoomType', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_OccupancyHandler.methods={Implementation_OccupancyComponent_OccupancyHandler_m_isInRoomTypes, Implementation_OccupancyComponent_OccupancyHandler_m_findOccupancy}

# OccupancyComponent_IOccupancyDecision class attributes and methods

# OccupancyComponent_IOccupancy class attributes and methods

# Implementation_RoomComponent_IRoomInformation class attributes and methods
Implementation_RoomComponent_IRoomInformation_m_getRoomInfo: Method = Method(name="getRoomInfo", parameters={Parameter(name='Implementation_roomNumber', type=StringType)}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_searchRoom: Method = Method(name="searchRoom", parameters={Parameter(name='Implementation_roomTypeName', type=StringType)}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_getAllRoomNumbers: Method = Method(name="getAllRoomNumbers", parameters={}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_countNumberOfTotalRooms: Method = Method(name="countNumberOfTotalRooms", parameters={}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_getCountOfRoomType: Method = Method(name="getCountOfRoomType", parameters={Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_getPriceOfRoomType: Method = Method(name="getPriceOfRoomType", parameters={Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_RoomComponent_IRoomInformation_m_getBedCountOfRoomType: Method = Method(name="getBedCountOfRoomType", parameters={Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_RoomComponent_IRoomInformation.methods={Implementation_RoomComponent_IRoomInformation_m_getBedCountOfRoomType, Implementation_RoomComponent_IRoomInformation_m_getCountOfRoomType, Implementation_RoomComponent_IRoomInformation_m_searchRoom, Implementation_RoomComponent_IRoomInformation_m_getAllRoomNumbers, Implementation_RoomComponent_IRoomInformation_m_countNumberOfTotalRooms, Implementation_RoomComponent_IRoomInformation_m_getRoomInfo, Implementation_RoomComponent_IRoomInformation_m_getRoomTypes, Implementation_RoomComponent_IRoomInformation_m_getPriceOfRoomType}

# Implementation_OccupancyComponent_Guest class attributes and methods
Implementation_OccupancyComponent_Guest_firstName: Property = Property(name="firstName", type=StringType)
Implementation_OccupancyComponent_Guest_lastName: Property = Property(name="lastName", type=StringType)
Implementation_OccupancyComponent_Guest.attributes={Implementation_OccupancyComponent_Guest_firstName, Implementation_OccupancyComponent_Guest_lastName}

# Implementation_OccupancyComponent_IOccupancy class attributes and methods
Implementation_OccupancyComponent_IOccupancy_m_checkInGuest: Method = Method(name="checkInGuest", parameters={Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_partnerFirstName', type=StringType), Parameter(name='Implementation_partnerLastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_lastName', type=StringType)})
Implementation_OccupancyComponent_IOccupancy_m_checkOutGuest: Method = Method(name="checkOutGuest", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_roomNumber', type=StringType), Parameter(name='Implementation_firstName', type=StringType)})
Implementation_OccupancyComponent_IOccupancy_m_listGuestsInRoom: Method = Method(name="listGuestsInRoom", parameters={Parameter(name='Implementation_roomNumber', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_IOccupancy_m_numberOfGuestsInHotel: Method = Method(name="numberOfGuestsInHotel", parameters={}, type=StringType)
Implementation_OccupancyComponent_IOccupancy_m_isOccupied: Method = Method(name="isOccupied", parameters={Parameter(name='Implementation_roomNumber', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_IOccupancy_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_OccupancyComponent_IOccupancy.methods={Implementation_OccupancyComponent_IOccupancy_m_getAvailableRooms, Implementation_OccupancyComponent_IOccupancy_m_checkOutGuest, Implementation_OccupancyComponent_IOccupancy_m_isOccupied, Implementation_OccupancyComponent_IOccupancy_m_numberOfGuestsInHotel, Implementation_OccupancyComponent_IOccupancy_m_listGuestsInRoom, Implementation_OccupancyComponent_IOccupancy_m_checkInGuest}

# Implementation_PaymentComponent class attributes and methods

# PaymentComponent_IPayment class attributes and methods

# Implementation_PaymentComponent_IPayment class attributes and methods
Implementation_PaymentComponent_IPayment_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_amount', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType)}, type=StringType)
Implementation_PaymentComponent_IPayment_m_validateCC: Method = Method(name="validateCC", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType)}, type=StringType)
Implementation_PaymentComponent_IPayment_m_addCC: Method = Method(name="addCC", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=StringType)
Implementation_PaymentComponent_IPayment_m_checkBalance: Method = Method(name="checkBalance", parameters={Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType)}, type=FloatType)
Implementation_PaymentComponent_IPayment_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_amount', type=StringType)}, type=FloatType)
Implementation_PaymentComponent_IPayment_m_removeCC: Method = Method(name="removeCC", parameters={Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_lastName', type=StringType)}, type=StringType)
Implementation_PaymentComponent_IPayment.methods={Implementation_PaymentComponent_IPayment_m_makePayment, Implementation_PaymentComponent_IPayment_m_checkBalance, Implementation_PaymentComponent_IPayment_m_validateCC, Implementation_PaymentComponent_IPayment_m_makeDeposit, Implementation_PaymentComponent_IPayment_m_removeCC, Implementation_PaymentComponent_IPayment_m_addCC}

# Implementation_BookingComponent_IBookingInformation class attributes and methods
Implementation_BookingComponent_IBookingInformation_m_getGuestsInBooking: Method = Method(name="getGuestsInBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_getRoomTypesInBooking: Method = Method(name="getRoomTypesInBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_searchForBooking: Method = Method(name="searchForBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_isPaidFor: Method = Method(name="isPaidFor", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_searchAvailableRoomTypes: Method = Method(name="searchAvailableRoomTypes", parameters={Parameter(name='Implementation_arrivalDate', type=StringType), Parameter(name='Implementation_departureDate', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingInformation_m_findBookingsByDateAndType: Method = Method(name="findBookingsByDateAndType", parameters={Parameter(name='Implementation_departureDate', type=StringType), Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_arrivalDate', type=StringType)}, type=IntegerType)
Implementation_BookingComponent_IBookingInformation.methods={Implementation_BookingComponent_IBookingInformation_m_getRoomTypesInBooking, Implementation_BookingComponent_IBookingInformation_m_searchAvailableRoomTypes, Implementation_BookingComponent_IBookingInformation_m_searchForBooking, Implementation_BookingComponent_IBookingInformation_m_makePayment, Implementation_BookingComponent_IBookingInformation_m_getGuestsInBooking, Implementation_BookingComponent_IBookingInformation_m_isPaidFor, Implementation_BookingComponent_IBookingInformation_m_findBookingsByDateAndType}

# Implementation_Bank_CustomerProvides class attributes and methods
Implementation_Bank_CustomerProvides_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_sum', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType)}, type=BooleanType)
Implementation_Bank_CustomerProvides_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType)}, type=BooleanType)
Implementation_Bank_CustomerProvides.methods={Implementation_Bank_CustomerProvides_m_isCreditCardValid, Implementation_Bank_CustomerProvides_m_makePayment}

# Implementation_Bank_AdministratorProvides class attributes and methods
Implementation_Bank_AdministratorProvides_m_getBalance: Method = Method(name="getBalance", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccv', type=StringType)}, type=FloatType)
Implementation_Bank_AdministratorProvides_m_makeDeposit: Method = Method(name="makeDeposit", parameters={Parameter(name='Implementation_sum', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccv', type=StringType)}, type=FloatType)
Implementation_Bank_AdministratorProvides_m_addCreditCard: Method = Method(name="addCreditCard", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=BooleanType)
Implementation_Bank_AdministratorProvides_m_removeCreditCard: Method = Method(name="removeCreditCard", parameters={Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=BooleanType)
Implementation_Bank_AdministratorProvides.methods={Implementation_Bank_AdministratorProvides_m_makeDeposit, Implementation_Bank_AdministratorProvides_m_removeCreditCard, Implementation_Bank_AdministratorProvides_m_getBalance, Implementation_Bank_AdministratorProvides_m_addCreditCard}

# Implementation_PaymentComponent_PaymentHandler class attributes and methods

# Implementation_PaymentComponent_Payment class attributes and methods
Implementation_PaymentComponent_Payment_ccNumber: Property = Property(name="ccNumber", type=StringType)
Implementation_PaymentComponent_Payment_ccv: Property = Property(name="ccv", type=StringType)
Implementation_PaymentComponent_Payment_firstName: Property = Property(name="firstName", type=StringType)
Implementation_PaymentComponent_Payment_lastName: Property = Property(name="lastName", type=StringType)
Implementation_PaymentComponent_Payment_expiryMonth: Property = Property(name="expiryMonth", type=StringType)
Implementation_PaymentComponent_Payment_expiryYear: Property = Property(name="expiryYear", type=StringType)
Implementation_PaymentComponent_Payment_amount: Property = Property(name="amount", type=FloatType)
Implementation_PaymentComponent_Payment.attributes={Implementation_PaymentComponent_Payment_ccNumber, Implementation_PaymentComponent_Payment_lastName, Implementation_PaymentComponent_Payment_ccv, Implementation_PaymentComponent_Payment_amount, Implementation_PaymentComponent_Payment_expiryYear, Implementation_PaymentComponent_Payment_firstName, Implementation_PaymentComponent_Payment_expiryMonth}

# Implementation_AdditionalServiceComponent class attributes and methods

# AdditionalServiceComponent_IAdditionalServiceAdministration class attributes and methods

# AdditionalServiceComponent_IEventManagement class attributes and methods

# Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration class attributes and methods
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_createAdditionalService: Method = Method(name="createAdditionalService", parameters={Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_description', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_editAdditionalService: Method = Method(name="editAdditionalService", parameters={Parameter(name='Implementation_description', type=StringType), Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_oldName', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeAdditionalService: Method = Method(name="removeAdditionalService", parameters={Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_createEvent: Method = Method(name="createEvent", parameters={Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_maxAttendants', type=StringType), Parameter(name='Implementation_currentAttendants', type=StringType), Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_editEvent: Method = Method(name="editEvent", parameters={Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_currentAttendants', type=StringType), Parameter(name='Implementation_maxAttendants', type=StringType), Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeEvent: Method = Method(name="removeEvent", parameters={Parameter(name='Implementation_dateTime', type=StringType), Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeEvents: Method = Method(name="removeEvents", parameters={Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration.methods={Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeAdditionalService, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeEvents, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_createEvent, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_createAdditionalService, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_editAdditionalService, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_editEvent, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration_m_removeEvent}

# Implementation_AdditionalServiceComponent_IEventManagement class attributes and methods
Implementation_AdditionalServiceComponent_IEventManagement_m_getServicePrice: Method = Method(name="getServicePrice", parameters={Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_getEventMaxAttendants: Method = Method(name="getEventMaxAttendants", parameters={Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_getEventCurrentAttendants: Method = Method(name="getEventCurrentAttendants", parameters={Parameter(name='Implementation_dateTime', type=StringType), Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_getServices: Method = Method(name="getServices", parameters={}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_getEvents: Method = Method(name="getEvents", parameters={Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_addGuestToEvent: Method = Method(name="addGuestToEvent", parameters={Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_guests', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement_m_removeGuestsFromEvent: Method = Method(name="removeGuestsFromEvent", parameters={Parameter(name='Implementation_guests', type=StringType), Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_IEventManagement.methods={Implementation_AdditionalServiceComponent_IEventManagement_m_getEvents, Implementation_AdditionalServiceComponent_IEventManagement_m_removeGuestsFromEvent, Implementation_AdditionalServiceComponent_IEventManagement_m_addGuestToEvent, Implementation_AdditionalServiceComponent_IEventManagement_m_getServicePrice, Implementation_AdditionalServiceComponent_IEventManagement_m_getEventCurrentAttendants, Implementation_AdditionalServiceComponent_IEventManagement_m_getServices, Implementation_AdditionalServiceComponent_IEventManagement_m_getEventMaxAttendants}

# Implementation_StaffComponent_IAuthentication class attributes and methods
Implementation_StaffComponent_IAuthentication_m_logIn: Method = Method(name="logIn", parameters={Parameter(name='Implementation_password', type=StringType), Parameter(name='Implementation_ssn', type=StringType)}, type=BooleanType)
Implementation_StaffComponent_IAuthentication_m_logOut: Method = Method(name="logOut", parameters={Parameter(name='Implementation_ssn', type=StringType)}, type=BooleanType)
Implementation_StaffComponent_IAuthentication_m_isLoggedIn: Method = Method(name="isLoggedIn", parameters={Parameter(name='Implementation_ssn', type=StringType)}, type=StringType)
Implementation_StaffComponent_IAuthentication.methods={Implementation_StaffComponent_IAuthentication_m_logIn, Implementation_StaffComponent_IAuthentication_m_isLoggedIn, Implementation_StaffComponent_IAuthentication_m_logOut}

# Implementation_AdditionalServiceComponent_AdditionalService class attributes and methods
Implementation_AdditionalServiceComponent_AdditionalService_name: Property = Property(name="name", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_usable: Property = Property(name="usable", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_price: Property = Property(name="price", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_description: Property = Property(name="description", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_findEvent: Method = Method(name="findEvent", parameters={Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_findEvents: Method = Method(name="findEvents", parameters={Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_createEvent: Method = Method(name="createEvent", parameters={Parameter(name='Implementation_maxAttendants', type=StringType), Parameter(name='Implementation_dateTime', type=StringType), Parameter(name='Implementation_currentAttendants', type=StringType), Parameter(name='Implementation_location', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_editEvent: Method = Method(name="editEvent", parameters={Parameter(name='Implementation_currentAttendants', type=StringType), Parameter(name='Implementation_maxAttendants', type=StringType), Parameter(name='Implementation_dateTime', type=StringType), Parameter(name='Implementation_location', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_removeEvent: Method = Method(name="removeEvent", parameters={Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService_m_removeEvents: Method = Method(name="removeEvents", parameters={Parameter(name='Implementation_dateTime', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalService.attributes={Implementation_AdditionalServiceComponent_AdditionalService_usable, Implementation_AdditionalServiceComponent_AdditionalService_name, Implementation_AdditionalServiceComponent_AdditionalService_price, Implementation_AdditionalServiceComponent_AdditionalService_description}
Implementation_AdditionalServiceComponent_AdditionalService.methods={Implementation_AdditionalServiceComponent_AdditionalService_m_removeEvents, Implementation_AdditionalServiceComponent_AdditionalService_m_createEvent, Implementation_AdditionalServiceComponent_AdditionalService_m_findEvents, Implementation_AdditionalServiceComponent_AdditionalService_m_editEvent, Implementation_AdditionalServiceComponent_AdditionalService_m_removeEvent, Implementation_AdditionalServiceComponent_AdditionalService_m_findEvent}

# Implementation_AdditionalServiceComponent_AdditionalServiceEvent class attributes and methods
Implementation_AdditionalServiceComponent_AdditionalServiceEvent_dateTime: Property = Property(name="dateTime", type=DateType)
Implementation_AdditionalServiceComponent_AdditionalServiceEvent_location: Property = Property(name="location", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalServiceEvent_maxAttendant: Property = Property(name="maxAttendant", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalServiceEvent_currentAttendants: Property = Property(name="currentAttendants", type=StringType)
Implementation_AdditionalServiceComponent_AdditionalServiceEvent.attributes={Implementation_AdditionalServiceComponent_AdditionalServiceEvent_location, Implementation_AdditionalServiceComponent_AdditionalServiceEvent_maxAttendant, Implementation_AdditionalServiceComponent_AdditionalServiceEvent_dateTime, Implementation_AdditionalServiceComponent_AdditionalServiceEvent_currentAttendants}

# Implementation_AdditionalServiceComponent_AdditionalServiceHandler class attributes and methods
Implementation_AdditionalServiceComponent_AdditionalServiceHandler_m_findService: Method = Method(name="findService", parameters={Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_AdditionalServiceComponent_AdditionalServiceHandler.methods={Implementation_AdditionalServiceComponent_AdditionalServiceHandler_m_findService}

# Implementation_BookingComponent class attributes and methods

# Implementation_BookingComponent_PaymentDetails class attributes and methods
Implementation_BookingComponent_PaymentDetails_firstName: Property = Property(name="firstName", type=StringType)
Implementation_BookingComponent_PaymentDetails_lastName: Property = Property(name="lastName", type=StringType)
Implementation_BookingComponent_PaymentDetails_address: Property = Property(name="address", type=StringType)
Implementation_BookingComponent_PaymentDetails_ccNumber: Property = Property(name="ccNumber", type=StringType)
Implementation_BookingComponent_PaymentDetails_ccv: Property = Property(name="ccv", type=StringType)
Implementation_BookingComponent_PaymentDetails_expiryMonth: Property = Property(name="expiryMonth", type=StringType)
Implementation_BookingComponent_PaymentDetails_expiryYear: Property = Property(name="expiryYear", type=StringType)
Implementation_BookingComponent_PaymentDetails_m_generateID: Method = Method(name="generateID", parameters={}, type=StringType)
Implementation_BookingComponent_PaymentDetails.attributes={Implementation_BookingComponent_PaymentDetails_address, Implementation_BookingComponent_PaymentDetails_expiryYear, Implementation_BookingComponent_PaymentDetails_lastName, Implementation_BookingComponent_PaymentDetails_ccNumber, Implementation_BookingComponent_PaymentDetails_expiryMonth, Implementation_BookingComponent_PaymentDetails_firstName, Implementation_BookingComponent_PaymentDetails_ccv}
Implementation_BookingComponent_PaymentDetails.methods={Implementation_BookingComponent_PaymentDetails_m_generateID}

# Implementation_BookingComponent_Booking class attributes and methods
Implementation_BookingComponent_Booking_arrivalDate: Property = Property(name="arrivalDate", type=DateType)
Implementation_BookingComponent_Booking_departureDate: Property = Property(name="departureDate", type=DateType)
Implementation_BookingComponent_Booking_bookingReference: Property = Property(name="bookingReference", type=StringType)
Implementation_BookingComponent_Booking_currentCost: Property = Property(name="currentCost", type=StringType)
Implementation_BookingComponent_Booking_isPaid: Property = Property(name="isPaid", type=StringType)
Implementation_BookingComponent_Booking_isActive: Property = Property(name="isActive", type=StringType)
Implementation_BookingComponent_Booking_m_removeGuestFromBooking: Method = Method(name="removeGuestFromBooking", parameters={Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_address', type=StringType)})
Implementation_BookingComponent_Booking_m_getGuestsInBooking: Method = Method(name="getGuestsInBooking", parameters={}, type=StringType)
Implementation_BookingComponent_Booking_m_getRoomTypesInBooking: Method = Method(name="getRoomTypesInBooking", parameters={}, type=StringType)
Implementation_BookingComponent_Booking_m_addPaymentDetails: Method = Method(name="addPaymentDetails", parameters={Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_address', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccv', type=StringType)})
Implementation_BookingComponent_Booking_m_addAdditionalServiceToBooking: Method = Method(name="addAdditionalServiceToBooking", parameters={Parameter(name='Implementation_location', type=StringType), Parameter(name='Implementation_guestCount', type=StringType), Parameter(name='Implementation_newService', type=StringType), Parameter(name='Implementation_dateTime', type=StringType)})
Implementation_BookingComponent_Booking_m_addRoomToBooking: Method = Method(name="addRoomToBooking", parameters={Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_roomPrice', type=StringType)})
Implementation_BookingComponent_Booking_m_removeRoomFromBooking: Method = Method(name="removeRoomFromBooking", parameters={Parameter(name='Implementation_roomType', type=StringType)})
Implementation_BookingComponent_Booking_m_updateBooking: Method = Method(name="updateBooking", parameters={Parameter(name='Implementation_arrivalDate', type=StringType), Parameter(name='Implementation_departureDate', type=StringType)})
Implementation_BookingComponent_Booking_m_removeAdditionalServiceFromBooking: Method = Method(name="removeAdditionalServiceFromBooking", parameters={Parameter(name='Implementation_additionalServiceName', type=StringType)})
Implementation_BookingComponent_Booking_m_currentCost: Method = Method(name="currentCost", parameters={}, type=StringType)
Implementation_BookingComponent_Booking_m_updatePaymentDetails: Method = Method(name="updatePaymentDetails", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_address', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType)})
Implementation_BookingComponent_Booking_m_generateReferenceNumber: Method = Method(name="generateReferenceNumber", parameters={}, type=StringType)
Implementation_BookingComponent_Booking_m_addGuestToBooking: Method = Method(name="addGuestToBooking", parameters={Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_address', type=StringType), Parameter(name='Implementation_phoneNumber', type=StringType)})
Implementation_BookingComponent_Booking.attributes={Implementation_BookingComponent_Booking_bookingReference, Implementation_BookingComponent_Booking_arrivalDate, Implementation_BookingComponent_Booking_isActive, Implementation_BookingComponent_Booking_currentCost, Implementation_BookingComponent_Booking_isPaid, Implementation_BookingComponent_Booking_departureDate}
Implementation_BookingComponent_Booking.methods={Implementation_BookingComponent_Booking_m_currentCost, Implementation_BookingComponent_Booking_m_updatePaymentDetails, Implementation_BookingComponent_Booking_m_updateBooking, Implementation_BookingComponent_Booking_m_getRoomTypesInBooking, Implementation_BookingComponent_Booking_m_removeAdditionalServiceFromBooking, Implementation_BookingComponent_Booking_m_addPaymentDetails, Implementation_BookingComponent_Booking_m_removeGuestFromBooking, Implementation_BookingComponent_Booking_m_addRoomToBooking, Implementation_BookingComponent_Booking_m_generateReferenceNumber, Implementation_BookingComponent_Booking_m_getGuestsInBooking, Implementation_BookingComponent_Booking_m_addAdditionalServiceToBooking, Implementation_BookingComponent_Booking_m_removeRoomFromBooking, Implementation_BookingComponent_Booking_m_addGuestToBooking}

# Implementation_BookingComponent_AdditionalService class attributes and methods
Implementation_BookingComponent_AdditionalService_name: Property = Property(name="name", type=StringType)
Implementation_BookingComponent_AdditionalService_guestCount: Property = Property(name="guestCount", type=StringType)
Implementation_BookingComponent_AdditionalService_location: Property = Property(name="location", type=StringType)
Implementation_BookingComponent_AdditionalService_dateTime: Property = Property(name="dateTime", type=DateType)
Implementation_BookingComponent_AdditionalService_price: Property = Property(name="price", type=IntegerType)
Implementation_BookingComponent_AdditionalService.attributes={Implementation_BookingComponent_AdditionalService_price, Implementation_BookingComponent_AdditionalService_guestCount, Implementation_BookingComponent_AdditionalService_location, Implementation_BookingComponent_AdditionalService_name, Implementation_BookingComponent_AdditionalService_dateTime}

# Implementation_BookingComponent_BookingGuest class attributes and methods
Implementation_BookingComponent_BookingGuest_firstName: Property = Property(name="firstName", type=StringType)
Implementation_BookingComponent_BookingGuest_lastName: Property = Property(name="lastName", type=StringType)
Implementation_BookingComponent_BookingGuest_address: Property = Property(name="address", type=StringType)
Implementation_BookingComponent_BookingGuest_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Implementation_BookingComponent_BookingGuest.attributes={Implementation_BookingComponent_BookingGuest_firstName, Implementation_BookingComponent_BookingGuest_lastName, Implementation_BookingComponent_BookingGuest_phoneNumber, Implementation_BookingComponent_BookingGuest_address}

# Implementation_BookingComponent_RoomType class attributes and methods
Implementation_BookingComponent_RoomType_roomType: Property = Property(name="roomType", type=StringType)
Implementation_BookingComponent_RoomType_cost: Property = Property(name="cost", type=StringType)
Implementation_BookingComponent_RoomType.attributes={Implementation_BookingComponent_RoomType_cost, Implementation_BookingComponent_RoomType_roomType}

# Implementation_BookingComponent_BookingHandler class attributes and methods
Implementation_BookingComponent_BookingHandler_m_bookingAvailable: Method = Method(name="bookingAvailable", parameters={Parameter(name='Implementation_startDate', type=StringType), Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_endDate', type=StringType)}, type=BooleanType)
Implementation_BookingComponent_BookingHandler_m_findBookingsByDate: Method = Method(name="findBookingsByDate", parameters={Parameter(name='Implementation_endDate', type=StringType), Parameter(name='Implementation_startDate', type=StringType)}, type=StringType)
Implementation_BookingComponent_BookingHandler_m_findBooking: Method = Method(name="findBooking", parameters={Parameter(name='Implementation_referenceNumber', type=StringType)}, type=StringType)
Implementation_BookingComponent_BookingHandler.methods={Implementation_BookingComponent_BookingHandler_m_bookingAvailable, Implementation_BookingComponent_BookingHandler_m_findBookingsByDate, Implementation_BookingComponent_BookingHandler_m_findBooking}

# BookingComponent_IBookingInformation class attributes and methods

# BookingComponent_IBookingDecision class attributes and methods

# BookingComponent_IBookingAdministration class attributes and methods

# Implementation_BookingComponent_IBookingAdministration class attributes and methods
Implementation_BookingComponent_IBookingAdministration_m_removeGuest: Method = Method(name="removeGuest", parameters={Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_address', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_firstName', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_confirmBooking: Method = Method(name="confirmBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_addPaymentDetails: Method = Method(name="addPaymentDetails", parameters={Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_expiryMonth', type=StringType), Parameter(name='Implementation_ccNumber', type=StringType), Parameter(name='Implementation_ccv', type=StringType), Parameter(name='Implementation_customerLastName', type=StringType), Parameter(name='Implementation_customerFirstName', type=StringType), Parameter(name='Implementation_expiryYear', type=StringType), Parameter(name='Implementation_customerAddress', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_makeBooking: Method = Method(name="makeBooking", parameters={Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_arrivalDate', type=StringType), Parameter(name='Implementation_customerSSN', type=StringType), Parameter(name='Implementation_departureDate', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_roomType', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_editBooking: Method = Method(name="editBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_departureDate', type=StringType), Parameter(name='Implementation_arrivalDate', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_addAdditionalService: Method = Method(name="addAdditionalService", parameters={Parameter(name='Implementation_additionalServiceName', type=StringType), Parameter(name='Implementation_cost', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='Implementation_roomType', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_removeAdditionalService: Method = Method(name="removeAdditionalService", parameters={Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_additionalServiceName', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration_m_addGuestToBooking: Method = Method(name="addGuestToBooking", parameters={Parameter(name='Implementation_firstName', type=StringType), Parameter(name='Implementation_phoneNumber', type=StringType), Parameter(name='Implementation_lastName', type=StringType), Parameter(name='Implementation_bookingReference', type=StringType), Parameter(name='Implementation_address', type=StringType)}, type=StringType)
Implementation_BookingComponent_IBookingAdministration.methods={Implementation_BookingComponent_IBookingAdministration_m_addRoom, Implementation_BookingComponent_IBookingAdministration_m_cancelBooking, Implementation_BookingComponent_IBookingAdministration_m_addAdditionalService, Implementation_BookingComponent_IBookingAdministration_m_removeAdditionalService, Implementation_BookingComponent_IBookingAdministration_m_addPaymentDetails, Implementation_BookingComponent_IBookingAdministration_m_makeBooking, Implementation_BookingComponent_IBookingAdministration_m_editBooking, Implementation_BookingComponent_IBookingAdministration_m_removeGuest, Implementation_BookingComponent_IBookingAdministration_m_confirmBooking, Implementation_BookingComponent_IBookingAdministration_m_addGuestToBooking, Implementation_BookingComponent_IBookingAdministration_m_removeRoom}

# Implementation_StaffComponent class attributes and methods

# StaffComponent_IAccountAdministration class attributes and methods

# StaffComponent_IAuthentication class attributes and methods

# Implementation_StaffComponent_IAccountAdministration class attributes and methods
Implementation_StaffComponent_IAccountAdministration_m_createAccount: Method = Method(name="createAccount", parameters={Parameter(name='Implementation_name', type=StringType), Parameter(name='Implementation_email', type=StringType), Parameter(name='Implementation_password', type=StringType), Parameter(name='Implementation_phone', type=StringType), Parameter(name='Implementation_ssn', type=StringType)}, type=StringType)
Implementation_StaffComponent_IAccountAdministration_m_editAccountDetails: Method = Method(name="editAccountDetails", parameters={Parameter(name='Implementation_ssn', type=StringType), Parameter(name='Implementation_password', type=StringType), Parameter(name='Implementation_email', type=StringType), Parameter(name='Implementation_phone', type=StringType), Parameter(name='Implementation_name', type=StringType)}, type=StringType)
Implementation_StaffComponent_IAccountAdministration_m_removeAccount: Method = Method(name="removeAccount", parameters={Parameter(name='Implementation_ssn', type=StringType)}, type=StringType)
Implementation_StaffComponent_IAccountAdministration.methods={Implementation_StaffComponent_IAccountAdministration_m_removeAccount, Implementation_StaffComponent_IAccountAdministration_m_editAccountDetails, Implementation_StaffComponent_IAccountAdministration_m_createAccount}

# Implementation_StaffComponent_AccountManager class attributes and methods
Implementation_StaffComponent_AccountManager_m_findAccount: Method = Method(name="findAccount", parameters={Parameter(name='Implementation_ssn', type=StringType)}, type=StringType)
Implementation_StaffComponent_AccountManager.methods={Implementation_StaffComponent_AccountManager_m_findAccount}

# Implementation_StaffComponent_Employee class attributes and methods
Implementation_StaffComponent_Employee_id: Property = Property(name="id", type=StringType)
Implementation_StaffComponent_Employee_ssn: Property = Property(name="ssn", type=StringType)
Implementation_StaffComponent_Employee_name: Property = Property(name="name", type=StringType)
Implementation_StaffComponent_Employee_email: Property = Property(name="email", type=StringType)
Implementation_StaffComponent_Employee_phone: Property = Property(name="phone", type=StringType)
Implementation_StaffComponent_Employee_password: Property = Property(name="password", type=StringType)
Implementation_StaffComponent_Employee_m_getEmployeeInfo: Method = Method(name="getEmployeeInfo", parameters={}, type=StringType)
Implementation_StaffComponent_Employee.attributes={Implementation_StaffComponent_Employee_ssn, Implementation_StaffComponent_Employee_phone, Implementation_StaffComponent_Employee_email, Implementation_StaffComponent_Employee_name, Implementation_StaffComponent_Employee_id, Implementation_StaffComponent_Employee_password}
Implementation_StaffComponent_Employee.methods={Implementation_StaffComponent_Employee_m_getEmployeeInfo}

# Implementation_RoomComponent class attributes and methods

# RoomComponent_IRoomInformation class attributes and methods

# RoomComponent_IRoomAdministration class attributes and methods

# Implementation_RoomComponent_IRoomAdministration class attributes and methods
Implementation_RoomComponent_IRoomAdministration_m_createBedRoom: Method = Method(name="createBedRoom", parameters={Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_bedCount', type=StringType), Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_roomTypeName', type=StringType), Parameter(name='Implementation_roomNumber', type=StringType), Parameter(name='Implementation_description', type=StringType)})
Implementation_RoomComponent_IRoomAdministration_m_editBedRoom: Method = Method(name="editBedRoom", parameters={Parameter(name='Implementation_currentRoomNumber', type=StringType), Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_roomNumber', type=StringType), Parameter(name='Implementation_roomTypeName', type=StringType), Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_description', type=StringType), Parameter(name='Implementation_bedCount', type=StringType)})
Implementation_RoomComponent_IRoomAdministration_m_remove: Method = Method(name="remove", parameters={Parameter(name='Implementation_roomNumber', type=StringType)})
Implementation_RoomComponent_IRoomAdministration_m_createConferenceRoom: Method = Method(name="createConferenceRoom", parameters={Parameter(name='Implementation_description', type=StringType), Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_projector', type=StringType), Parameter(name='Implementation_numberOfSeats', type=StringType), Parameter(name='Implementation_price', type=StringType), Parameter(name='Implementation_roomNumber', type=StringType), Parameter(name='Implementation_roomTypeName', type=StringType), Parameter(name='Implementation_conferencePhone', type=StringType)})
Implementation_RoomComponent_IRoomAdministration_m_editConferenceRoom: Method = Method(name="editConferenceRoom", parameters={Parameter(name='Implementation_roomTypeName', type=StringType), Parameter(name='Implementation_projector', type=StringType), Parameter(name='Implementation_roomNumber', type=StringType), Parameter(name='Implementation_usable', type=StringType), Parameter(name='Implementation_currentRoomNumber', type=StringType), Parameter(name='Implementation_numberOfSeats', type=StringType), Parameter(name='Implementation_conferencePhone', type=StringType), Parameter(name='Implementation_description', type=StringType), Parameter(name='Implementation_price', type=StringType)})
Implementation_RoomComponent_IRoomAdministration.methods={Implementation_RoomComponent_IRoomAdministration_m_createBedRoom, Implementation_RoomComponent_IRoomAdministration_m_editBedRoom, Implementation_RoomComponent_IRoomAdministration_m_createConferenceRoom, Implementation_RoomComponent_IRoomAdministration_m_editConferenceRoom, Implementation_RoomComponent_IRoomAdministration_m_remove}

# Implementation_Bank class attributes and methods

# Implementation_RoomComponent_Room class attributes and methods
Implementation_RoomComponent_Room_roomNumber: Property = Property(name="roomNumber", type=StringType)
Implementation_RoomComponent_Room_usable: Property = Property(name="usable", type=StringType)
Implementation_RoomComponent_Room_price: Property = Property(name="price", type=StringType)
Implementation_RoomComponent_Room_roomTypeName: Property = Property(name="roomTypeName", type=StringType)
Implementation_RoomComponent_Room_description: Property = Property(name="description", type=StringType)
Implementation_RoomComponent_Room.attributes={Implementation_RoomComponent_Room_roomNumber, Implementation_RoomComponent_Room_price, Implementation_RoomComponent_Room_roomTypeName, Implementation_RoomComponent_Room_description, Implementation_RoomComponent_Room_usable}

# Implementation_RoomComponent_Bedroom class attributes and methods
Implementation_RoomComponent_Bedroom_bedCount: Property = Property(name="bedCount", type=StringType)
Implementation_RoomComponent_Bedroom.attributes={Implementation_RoomComponent_Bedroom_bedCount}

# RoomComponent_Room class attributes and methods

# Implementation_RoomComponent_ConferenceRoom class attributes and methods
Implementation_RoomComponent_ConferenceRoom_numberOfSeats: Property = Property(name="numberOfSeats", type=IntegerType)
Implementation_RoomComponent_ConferenceRoom_projector: Property = Property(name="projector", type=BooleanType)
Implementation_RoomComponent_ConferenceRoom_conferencePhone: Property = Property(name="conferencePhone", type=BooleanType)
Implementation_RoomComponent_ConferenceRoom.attributes={Implementation_RoomComponent_ConferenceRoom_conferencePhone, Implementation_RoomComponent_ConferenceRoom_numberOfSeats, Implementation_RoomComponent_ConferenceRoom_projector}

# Implementation_RoomComponent_RoomHandler class attributes and methods

# Relationships
iOccupancyDecision1: BinaryAssociation = BinaryAssociation(
    name="iOccupancyDecision1",
    ends={
        Property(name="Implementation_OccupancyComponent_IOccupancyDecision", type=Implementation_DecisionSupportComponent_DSSController, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_DSSController", type=Implementation_OccupancyComponent_IOccupancyDecision, multiplicity=Multiplicity(1, 1))
    }
)
iBookingDecision2: BinaryAssociation = BinaryAssociation(
    name="iBookingDecision2",
    ends={
        Property(name="Implementation_BookingComponent_IBookingDecision", type=Implementation_DecisionSupportComponent_DSSController, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_DSSController3", type=Implementation_BookingComponent_IBookingDecision, multiplicity=Multiplicity(1, 1))
    }
)
additionalServices0: BinaryAssociation = BinaryAssociation(
    name="additionalServices0",
    ends={
        Property(name="Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo", type=Implementation_DecisionSupportComponent_BookingDSSInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_BookingDSSInfo", type=Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo, multiplicity=Multiplicity(0, 9999))
    }
)
occupancyDSSInfo4: BinaryAssociation = BinaryAssociation(
    name="occupancyDSSInfo4",
    ends={
        Property(name="Implementation_DecisionSupportComponent_OccupancyDSSInfo", type=Implementation_DecisionSupportComponent_DSSController, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_DSSController5", type=Implementation_DecisionSupportComponent_OccupancyDSSInfo, multiplicity=Multiplicity(0, 9999))
    }
)
additionalServiceDSSInfo6: BinaryAssociation = BinaryAssociation(
    name="additionalServiceDSSInfo6",
    ends={
        Property(name="Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo8", type=Implementation_DecisionSupportComponent_DSSController, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_DSSController7", type=Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo, multiplicity=Multiplicity(0, 9999))
    }
)
bookingDSSInfo9: BinaryAssociation = BinaryAssociation(
    name="bookingDSSInfo9",
    ends={
        Property(name="Implementation_DecisionSupportComponent_BookingDSSInfo11", type=Implementation_DecisionSupportComponent_DSSController, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_DecisionSupportComponent_DSSController10", type=Implementation_DecisionSupportComponent_BookingDSSInfo, multiplicity=Multiplicity(0, 9999))
    }
)
iRoomInformation13: BinaryAssociation = BinaryAssociation(
    name="iRoomInformation13",
    ends={
        Property(name="Implementation_RoomComponent_IRoomInformation", type=Implementation_OccupancyComponent_OccupancyHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_OccupancyComponent_OccupancyHandler", type=Implementation_RoomComponent_IRoomInformation, multiplicity=Multiplicity(1, 1))
    }
)
guests12: BinaryAssociation = BinaryAssociation(
    name="guests12",
    ends={
        Property(name="Implementation_OccupancyComponent_Guest", type=Implementation_OccupancyComponent_Occupancy, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_OccupancyComponent_Occupancy", type=Implementation_OccupancyComponent_Guest, multiplicity=Multiplicity(1, 9999))
    }
)
iBooking14: BinaryAssociation = BinaryAssociation(
    name="iBooking14",
    ends={
        Property(name="Implementation_BookingComponent_IBookingInformation", type=Implementation_OccupancyComponent_OccupancyHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_OccupancyComponent_OccupancyHandler15", type=Implementation_BookingComponent_IBookingInformation, multiplicity=Multiplicity(1, 1))
    }
)
occupancy16: BinaryAssociation = BinaryAssociation(
    name="occupancy16",
    ends={
        Property(name="Implementation_OccupancyComponent_Occupancy18", type=Implementation_OccupancyComponent_OccupancyHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_OccupancyComponent_OccupancyHandler17", type=Implementation_OccupancyComponent_Occupancy, multiplicity=Multiplicity(0, 9999))
    }
)
customerProvides20: BinaryAssociation = BinaryAssociation(
    name="customerProvides20",
    ends={
        Property(name="Implementation_Bank_CustomerProvides", type=Implementation_PaymentComponent_PaymentHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_PaymentComponent_PaymentHandler21", type=Implementation_Bank_CustomerProvides, multiplicity=Multiplicity(1, 1))
    }
)
administratorProvides22: BinaryAssociation = BinaryAssociation(
    name="administratorProvides22",
    ends={
        Property(name="Implementation_Bank_AdministratorProvides", type=Implementation_PaymentComponent_PaymentHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_PaymentComponent_PaymentHandler23", type=Implementation_Bank_AdministratorProvides, multiplicity=Multiplicity(1, 1))
    }
)
payment19: BinaryAssociation = BinaryAssociation(
    name="payment19",
    ends={
        Property(name="Implementation_PaymentComponent_Payment", type=Implementation_PaymentComponent_PaymentHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_PaymentComponent_PaymentHandler", type=Implementation_PaymentComponent_Payment, multiplicity=Multiplicity(0, 9999))
    }
)
additionalService28: BinaryAssociation = BinaryAssociation(
    name="additionalService28",
    ends={
        Property(name="Implementation_AdditionalServiceComponent_AdditionalService29", type=Implementation_AdditionalServiceComponent_AdditionalServiceHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_AdditionalServiceComponent_AdditionalServiceHandler", type=Implementation_AdditionalServiceComponent_AdditionalService, multiplicity=Multiplicity(0, 9999))
    }
)
iAuthentication30: BinaryAssociation = BinaryAssociation(
    name="iAuthentication30",
    ends={
        Property(name="Implementation_StaffComponent_IAuthentication", type=Implementation_AdditionalServiceComponent_AdditionalServiceHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_AdditionalServiceComponent_AdditionalServiceHandler31", type=Implementation_StaffComponent_IAuthentication, multiplicity=Multiplicity(1, 1))
    }
)
additionalServiceEvent24: BinaryAssociation = BinaryAssociation(
    name="additionalServiceEvent24",
    ends={
        Property(name="Implementation_AdditionalServiceComponent_AdditionalServiceEvent", type=Implementation_AdditionalServiceComponent_AdditionalService, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_AdditionalServiceComponent_AdditionalService", type=Implementation_AdditionalServiceComponent_AdditionalServiceEvent, multiplicity=Multiplicity(0, 9999))
    }
)
tempEvents25: BinaryAssociation = BinaryAssociation(
    name="tempEvents25",
    ends={
        Property(name="Implementation_AdditionalServiceComponent_AdditionalServiceEvent27", type=Implementation_AdditionalServiceComponent_AdditionalService, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_AdditionalServiceComponent_AdditionalService26", type=Implementation_AdditionalServiceComponent_AdditionalServiceEvent, multiplicity=Multiplicity(0, 9999))
    }
)
bookings39: BinaryAssociation = BinaryAssociation(
    name="bookings39",
    ends={
        Property(name="Implementation_BookingComponent_Booking40", type=Implementation_BookingComponent_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_BookingHandler", type=Implementation_BookingComponent_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
authentication41: BinaryAssociation = BinaryAssociation(
    name="authentication41",
    ends={
        Property(name="Implementation_StaffComponent_IAuthentication43", type=Implementation_BookingComponent_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_BookingHandler42", type=Implementation_StaffComponent_IAuthentication, multiplicity=Multiplicity(1, 1))
    }
)
additionalServices32: BinaryAssociation = BinaryAssociation(
    name="additionalServices32",
    ends={
        Property(name="Implementation_BookingComponent_AdditionalService", type=Implementation_BookingComponent_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_Booking", type=Implementation_BookingComponent_AdditionalService, multiplicity=Multiplicity(0, 9999))
    }
)
guests33: BinaryAssociation = BinaryAssociation(
    name="guests33",
    ends={
        Property(name="Implementation_BookingComponent_BookingGuest", type=Implementation_BookingComponent_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_Booking34", type=Implementation_BookingComponent_BookingGuest, multiplicity=Multiplicity(1, 9999))
    }
)
paymentDetails35: BinaryAssociation = BinaryAssociation(
    name="paymentDetails35",
    ends={
        Property(name="Implementation_BookingComponent_PaymentDetails", type=Implementation_BookingComponent_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_Booking36", type=Implementation_BookingComponent_PaymentDetails, multiplicity=Multiplicity(1, 1))
    }
)
rooms37: BinaryAssociation = BinaryAssociation(
    name="rooms37",
    ends={
        Property(name="Implementation_BookingComponent_RoomType", type=Implementation_BookingComponent_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_Booking38", type=Implementation_BookingComponent_RoomType, multiplicity=Multiplicity(1, 9999))
    }
)
iRoomInformation44: BinaryAssociation = BinaryAssociation(
    name="iRoomInformation44",
    ends={
        Property(name="Implementation_RoomComponent_IRoomInformation46", type=Implementation_BookingComponent_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_BookingHandler45", type=Implementation_RoomComponent_IRoomInformation, multiplicity=Multiplicity(1, 1))
    }
)
iAdditionalServiceInformation47: BinaryAssociation = BinaryAssociation(
    name="iAdditionalServiceInformation47",
    ends={
        Property(name="Implementation_AdditionalServiceComponent_IEventManagement", type=Implementation_BookingComponent_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_BookingHandler48", type=Implementation_AdditionalServiceComponent_IEventManagement, multiplicity=Multiplicity(1, 1))
    }
)
iPayment49: BinaryAssociation = BinaryAssociation(
    name="iPayment49",
    ends={
        Property(name="Implementation_PaymentComponent_IPayment", type=Implementation_BookingComponent_BookingHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_BookingComponent_BookingHandler50", type=Implementation_PaymentComponent_IPayment, multiplicity=Multiplicity(1, 1))
    }
)
loggedIn51: BinaryAssociation = BinaryAssociation(
    name="loggedIn51",
    ends={
        Property(name="Implementation_StaffComponent_Employee", type=Implementation_StaffComponent_AccountManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_StaffComponent_AccountManager", type=Implementation_StaffComponent_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
employees52: BinaryAssociation = BinaryAssociation(
    name="employees52",
    ends={
        Property(name="Implementation_StaffComponent_Employee54", type=Implementation_StaffComponent_AccountManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_StaffComponent_AccountManager53", type=Implementation_StaffComponent_Employee, multiplicity=Multiplicity(1, 9999))
    }
)
iAuthentication55: BinaryAssociation = BinaryAssociation(
    name="iAuthentication55",
    ends={
        Property(name="Implementation_StaffComponent_IAuthentication57", type=Implementation_StaffComponent_AccountManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_StaffComponent_AccountManager56", type=Implementation_StaffComponent_IAuthentication, multiplicity=Multiplicity(1, 1))
    }
)
bedRooms60: BinaryAssociation = BinaryAssociation(
    name="bedRooms60",
    ends={
        Property(name="Implementation_RoomComponent_Bedroom", type=Implementation_RoomComponent_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_RoomComponent_RoomHandler61", type=Implementation_RoomComponent_Bedroom, multiplicity=Multiplicity(0, 9999))
    }
)
conferenceRooms62: BinaryAssociation = BinaryAssociation(
    name="conferenceRooms62",
    ends={
        Property(name="Implementation_RoomComponent_ConferenceRoom", type=Implementation_RoomComponent_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_RoomComponent_RoomHandler63", type=Implementation_RoomComponent_ConferenceRoom, multiplicity=Multiplicity(0, 9999))
    }
)
authenticator58: BinaryAssociation = BinaryAssociation(
    name="authenticator58",
    ends={
        Property(name="Implementation_StaffComponent_IAuthentication59", type=Implementation_RoomComponent_RoomHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Implementation_RoomComponent_RoomHandler", type=Implementation_StaffComponent_IAuthentication, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Implementation_DecisionSupportComponent_DecisionSupportComponent_IDecisionSupport = Generalization(general=DecisionSupportComponent_IDecisionSupport, specific=Implementation_DecisionSupportComponent)
gen_Implementation_DecisionSupportComponent_DSSController_DecisionSupportComponent_IDecisionSupport = Generalization(general=DecisionSupportComponent_IDecisionSupport, specific=Implementation_DecisionSupportComponent_DSSController)
gen_Implementation_OccupancyComponent_OccupancyHandler_OccupancyComponent_IOccupancyDecision = Generalization(general=OccupancyComponent_IOccupancyDecision, specific=Implementation_OccupancyComponent_OccupancyHandler)
gen_Implementation_OccupancyComponent_OccupancyHandler_OccupancyComponent_IOccupancy = Generalization(general=OccupancyComponent_IOccupancy, specific=Implementation_OccupancyComponent_OccupancyHandler)
gen_Implementation_PaymentComponent_PaymentComponent_IPayment = Generalization(general=PaymentComponent_IPayment, specific=Implementation_PaymentComponent)
gen_Implementation_PaymentComponent_PaymentHandler_PaymentComponent_IPayment = Generalization(general=PaymentComponent_IPayment, specific=Implementation_PaymentComponent_PaymentHandler)
gen_Implementation_AdditionalServiceComponent_AdditionalServiceComponent_IAdditionalServiceAdministration = Generalization(general=AdditionalServiceComponent_IAdditionalServiceAdministration, specific=Implementation_AdditionalServiceComponent)
gen_Implementation_AdditionalServiceComponent_AdditionalServiceComponent_IEventManagement = Generalization(general=AdditionalServiceComponent_IEventManagement, specific=Implementation_AdditionalServiceComponent)
gen_Implementation_AdditionalServiceComponent_AdditionalServiceHandler_AdditionalServiceComponent_IEventManagement = Generalization(general=AdditionalServiceComponent_IEventManagement, specific=Implementation_AdditionalServiceComponent_AdditionalServiceHandler)
gen_Implementation_AdditionalServiceComponent_AdditionalServiceHandler_AdditionalServiceComponent_IAdditionalServiceAdministration = Generalization(general=AdditionalServiceComponent_IAdditionalServiceAdministration, specific=Implementation_AdditionalServiceComponent_AdditionalServiceHandler)
gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingInformation = Generalization(general=BookingComponent_IBookingInformation, specific=Implementation_BookingComponent_BookingHandler)
gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingDecision = Generalization(general=BookingComponent_IBookingDecision, specific=Implementation_BookingComponent_BookingHandler)
gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingAdministration = Generalization(general=BookingComponent_IBookingAdministration, specific=Implementation_BookingComponent_BookingHandler)
gen_Implementation_StaffComponent_StaffComponent_IAccountAdministration = Generalization(general=StaffComponent_IAccountAdministration, specific=Implementation_StaffComponent)
gen_Implementation_StaffComponent_StaffComponent_IAuthentication = Generalization(general=StaffComponent_IAuthentication, specific=Implementation_StaffComponent)
gen_Implementation_StaffComponent_AccountManager_StaffComponent_IAuthentication = Generalization(general=StaffComponent_IAuthentication, specific=Implementation_StaffComponent_AccountManager)
gen_Implementation_StaffComponent_AccountManager_StaffComponent_IAccountAdministration = Generalization(general=StaffComponent_IAccountAdministration, specific=Implementation_StaffComponent_AccountManager)
gen_Implementation_RoomComponent_RoomComponent_IRoomInformation = Generalization(general=RoomComponent_IRoomInformation, specific=Implementation_RoomComponent)
gen_Implementation_RoomComponent_RoomComponent_IRoomAdministration = Generalization(general=RoomComponent_IRoomAdministration, specific=Implementation_RoomComponent)
gen_Implementation_Bank_BookingComponent_IBookingDecision = Generalization(general=BookingComponent_IBookingDecision, specific=Implementation_Bank)
gen_Implementation_Bank_BookingComponent_IBookingAdministration = Generalization(general=BookingComponent_IBookingAdministration, specific=Implementation_Bank)
gen_Implementation_Bank_BookingComponent_IBookingInformation = Generalization(general=BookingComponent_IBookingInformation, specific=Implementation_Bank)
gen_Implementation_RoomComponent_Bedroom_RoomComponent_Room = Generalization(general=RoomComponent_Room, specific=Implementation_RoomComponent_Bedroom)
gen_Implementation_RoomComponent_ConferenceRoom_RoomComponent_Room = Generalization(general=RoomComponent_Room, specific=Implementation_RoomComponent_ConferenceRoom)
gen_Implementation_RoomComponent_RoomHandler_RoomComponent_IRoomInformation = Generalization(general=RoomComponent_IRoomInformation, specific=Implementation_RoomComponent_RoomHandler)
gen_Implementation_RoomComponent_RoomHandler_RoomComponent_IRoomAdministration = Generalization(general=RoomComponent_IRoomAdministration, specific=Implementation_RoomComponent_RoomHandler)

# Domain Model
domain_model = DomainModel(
    name="Implementation",
    types={Implementation_DecisionSupportComponent, DecisionSupportComponent_IDecisionSupport, Implementation_DecisionSupportComponent_IDecisionSupport, Implementation_OccupancyComponent_IOccupancyDecision, Implementation_BookingComponent_IBookingDecision, Implementation_DecisionSupportComponent_BookingDSSInfo, Implementation_DecisionSupportComponent_AdditionalServiceDSSInfo, Implementation_DecisionSupportComponent_DSSController, Implementation_OccupancyComponent_Occupancy, Implementation_DecisionSupportComponent_OccupancyDSSInfo, Implementation_OccupancyComponent, Implementation_OccupancyComponent_OccupancyHandler, OccupancyComponent_IOccupancyDecision, OccupancyComponent_IOccupancy, Implementation_RoomComponent_IRoomInformation, Implementation_OccupancyComponent_Guest, Implementation_OccupancyComponent_IOccupancy, Implementation_PaymentComponent, PaymentComponent_IPayment, Implementation_PaymentComponent_IPayment, Implementation_BookingComponent_IBookingInformation, Implementation_Bank_CustomerProvides, Implementation_Bank_AdministratorProvides, Implementation_PaymentComponent_PaymentHandler, Implementation_PaymentComponent_Payment, Implementation_AdditionalServiceComponent, AdditionalServiceComponent_IAdditionalServiceAdministration, AdditionalServiceComponent_IEventManagement, Implementation_AdditionalServiceComponent_IAdditionalServiceAdministration, Implementation_AdditionalServiceComponent_IEventManagement, Implementation_StaffComponent_IAuthentication, Implementation_AdditionalServiceComponent_AdditionalService, Implementation_AdditionalServiceComponent_AdditionalServiceEvent, Implementation_AdditionalServiceComponent_AdditionalServiceHandler, Implementation_BookingComponent, Implementation_BookingComponent_PaymentDetails, Implementation_BookingComponent_Booking, Implementation_BookingComponent_AdditionalService, Implementation_BookingComponent_BookingGuest, Implementation_BookingComponent_RoomType, Implementation_BookingComponent_BookingHandler, BookingComponent_IBookingInformation, BookingComponent_IBookingDecision, BookingComponent_IBookingAdministration, Implementation_BookingComponent_IBookingAdministration, Implementation_StaffComponent, StaffComponent_IAccountAdministration, StaffComponent_IAuthentication, Implementation_StaffComponent_IAccountAdministration, Implementation_StaffComponent_AccountManager, Implementation_StaffComponent_Employee, Implementation_RoomComponent, RoomComponent_IRoomInformation, RoomComponent_IRoomAdministration, Implementation_RoomComponent_IRoomAdministration, Implementation_Bank, Implementation_RoomComponent_Room, Implementation_RoomComponent_Bedroom, RoomComponent_Room, Implementation_RoomComponent_ConferenceRoom, Implementation_RoomComponent_RoomHandler},
    associations={iOccupancyDecision1, iBookingDecision2, additionalServices0, occupancyDSSInfo4, additionalServiceDSSInfo6, bookingDSSInfo9, iRoomInformation13, guests12, iBooking14, occupancy16, customerProvides20, administratorProvides22, payment19, additionalService28, iAuthentication30, additionalServiceEvent24, tempEvents25, bookings39, authentication41, additionalServices32, guests33, paymentDetails35, rooms37, iRoomInformation44, iAdditionalServiceInformation47, iPayment49, loggedIn51, employees52, iAuthentication55, bedRooms60, conferenceRooms62, authenticator58},
    generalizations={gen_Implementation_DecisionSupportComponent_DecisionSupportComponent_IDecisionSupport, gen_Implementation_DecisionSupportComponent_DSSController_DecisionSupportComponent_IDecisionSupport, gen_Implementation_OccupancyComponent_OccupancyHandler_OccupancyComponent_IOccupancyDecision, gen_Implementation_OccupancyComponent_OccupancyHandler_OccupancyComponent_IOccupancy, gen_Implementation_PaymentComponent_PaymentComponent_IPayment, gen_Implementation_PaymentComponent_PaymentHandler_PaymentComponent_IPayment, gen_Implementation_AdditionalServiceComponent_AdditionalServiceComponent_IAdditionalServiceAdministration, gen_Implementation_AdditionalServiceComponent_AdditionalServiceComponent_IEventManagement, gen_Implementation_AdditionalServiceComponent_AdditionalServiceHandler_AdditionalServiceComponent_IEventManagement, gen_Implementation_AdditionalServiceComponent_AdditionalServiceHandler_AdditionalServiceComponent_IAdditionalServiceAdministration, gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingInformation, gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingDecision, gen_Implementation_BookingComponent_BookingHandler_BookingComponent_IBookingAdministration, gen_Implementation_StaffComponent_StaffComponent_IAccountAdministration, gen_Implementation_StaffComponent_StaffComponent_IAuthentication, gen_Implementation_StaffComponent_AccountManager_StaffComponent_IAuthentication, gen_Implementation_StaffComponent_AccountManager_StaffComponent_IAccountAdministration, gen_Implementation_RoomComponent_RoomComponent_IRoomInformation, gen_Implementation_RoomComponent_RoomComponent_IRoomAdministration, gen_Implementation_Bank_BookingComponent_IBookingDecision, gen_Implementation_Bank_BookingComponent_IBookingAdministration, gen_Implementation_Bank_BookingComponent_IBookingInformation, gen_Implementation_RoomComponent_Bedroom_RoomComponent_Room, gen_Implementation_RoomComponent_ConferenceRoom_RoomComponent_Room, gen_Implementation_RoomComponent_RoomHandler_RoomComponent_IRoomInformation, gen_Implementation_RoomComponent_RoomHandler_RoomComponent_IRoomAdministration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)