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
RoomApproval: Enumeration = Enumeration(
    name="RoomApproval",
    literals={
            
    }
)

DisabilityApproval: Enumeration = Enumeration(
    name="DisabilityApproval",
    literals={
            
    }
)

# Classes
tda593_california_DataService = Class(name="tda593::california::DataService", is_abstract=True)
tda593_facilities_AdminKeyCardManager = Class(name="tda593::facilities::AdminKeyCardManager", is_abstract=True)
KeyCardManager = Class(name="KeyCardManager")
tda593_facilities_KeyCardManager = Class(name="tda593::facilities::KeyCardManager", is_abstract=True)
tda593_facilities_KeyCard = Class(name="tda593::facilities::KeyCard")
tda593_facilities_AdminRoomManager = Class(name="tda593::facilities::AdminRoomManager", is_abstract=True)
RoomManager = Class(name="RoomManager")
tda593_facilities_RoomManager = Class(name="tda593::facilities::RoomManager", is_abstract=True)
tda593_facilities_RoomType = Class(name="tda593::facilities::RoomType")
tda593_facilities_Room = Class(name="tda593::facilities::Room", is_abstract=True)
facilities_KeyCard = Class(name="facilities::KeyCard")
tda593_facilities_RoomManagerImpl = Class(name="tda593::facilities::RoomManagerImpl")
facilities_RoomDataService = Class(name="facilities::RoomDataService")
facilities_RoomTypeDataService = Class(name="facilities::RoomTypeDataService")
facilities_KeyCardManager = Class(name="facilities::KeyCardManager")
tda593_facilities_RoomDataService = Class(name="tda593::facilities::RoomDataService")
tda593_facilities_RoomTypeDataService = Class(name="tda593::facilities::RoomTypeDataService")
tda593_facilities_KeyCardManagerImpl = Class(name="tda593::facilities::KeyCardManagerImpl")
facilities_KeyCardDataService = Class(name="facilities::KeyCardDataService")
tda593_facilities_KeyCardDataService = Class(name="tda593::facilities::KeyCardDataService")
tda593_facilities_AdminRoomManagerImpl = Class(name="tda593::facilities::AdminRoomManagerImpl")
facilities_RoomManagerImpl = Class(name="facilities::RoomManagerImpl")
facilities_AdminRoomManager = Class(name="facilities::AdminRoomManager")
tda593_facilities_AdminKeyCardManagerImpl = Class(name="tda593::facilities::AdminKeyCardManagerImpl")
facilities_KeyCardManagerImpl = Class(name="facilities::KeyCardManagerImpl")
facilities_AdminKeyCardManager = Class(name="facilities::AdminKeyCardManager")
tda593_billing_DiscountManager = Class(name="tda593::billing::DiscountManager", is_abstract=True)
facilities_RoomType = Class(name="facilities::RoomType")
tda593_facilities_GuestRoom = Class(name="tda593::facilities::GuestRoom")
Room = Class(name="Room")
tda593_facilities_ConferenceRoom = Class(name="tda593::facilities::ConferenceRoom")
billing_DiscountLimit = Class(name="billing::DiscountLimit")
tda593_billing_DiscountLimit = Class(name="tda593::billing::DiscountLimit")
booking_LegalEntity = Class(name="booking::LegalEntity")
tda593_billing_SumDiscount = Class(name="tda593::billing::SumDiscount")
Discount = Class(name="Discount")
tda593_billing_PercentageDiscount = Class(name="tda593::billing::PercentageDiscount")
tda593_billing_DiscountDataService = Class(name="tda593::billing::DiscountDataService")
tda593_billing_DiscountManagerImpl = Class(name="tda593::billing::DiscountManagerImpl")
DiscountManager = Class(name="DiscountManager")
billing_DiscountDataService = Class(name="billing::DiscountDataService")
tda593_billing_Bill = Class(name="tda593::billing::Bill")
tda593_billing_Discount = Class(name="tda593::billing::Discount", is_abstract=True)
billing_Purchase = Class(name="billing::Purchase")
billing_Discount = Class(name="billing::Discount")
billing_Bill = Class(name="billing::Bill")
tda593_billing_Purchase = Class(name="tda593::billing::Purchase")
billing_Service = Class(name="billing::Service")
tda593_billing_Service = Class(name="tda593::billing::Service")
tda593_billing_BillManager = Class(name="tda593::billing::BillManager", is_abstract=True)
tda593_billing_BookingBill = Class(name="tda593::billing::BookingBill")
Bill = Class(name="Bill")
booking_Booking = Class(name="booking::Booking")
tda593_billing_CreditCardManager = Class(name="tda593::billing::CreditCardManager", is_abstract=True)
tda593_billing_CreditCardInformation = Class(name="tda593::billing::CreditCardInformation")
tda593_billing_BankingManager = Class(name="tda593::billing::BankingManager", is_abstract=True)
tda593_billing_BankingManagerImpl = Class(name="tda593::billing::BankingManagerImpl")
BankingManager = Class(name="BankingManager")
tda593_billing_CreditCardInformationDataService = Class(name="tda593::billing::CreditCardInformationDataService")
tda593_billing_CreditCardManagerImpl = Class(name="tda593::billing::CreditCardManagerImpl")
CreditCardManager = Class(name="CreditCardManager")
billing_CreditCardInformationDataService = Class(name="billing::CreditCardInformationDataService")
tda593_billing_ServiceManagerImpl = Class(name="tda593::billing::ServiceManagerImpl")
ServiceManager = Class(name="ServiceManager")
billing_ServiceDataService = Class(name="billing::ServiceDataService")
tda593_billing_ServiceManager = Class(name="tda593::billing::ServiceManager", is_abstract=True)
tda593_billing_ServiceDataService = Class(name="tda593::billing::ServiceDataService")
tda593_billing_AdminServiceManager = Class(name="tda593::billing::AdminServiceManager", is_abstract=True)
tda593_billing_AdminServiceManagerImpl = Class(name="tda593::billing::AdminServiceManagerImpl")
billing_ServiceManagerImpl = Class(name="billing::ServiceManagerImpl")
billing_AdminServiceManager = Class(name="billing::AdminServiceManager")
tda593_billing_AdminDiscountManager = Class(name="tda593::billing::AdminDiscountManager", is_abstract=True)
tda593_billing_BillManagerImpl = Class(name="tda593::billing::BillManagerImpl")
BillManager = Class(name="BillManager")
billing_BillDataService = Class(name="billing::BillDataService")
booking_BookingManager = Class(name="booking::BookingManager")
tda593_billing_BillDataService = Class(name="tda593::billing::BillDataService")
tda593_billing_AdminDiscountManagerImpl = Class(name="tda593::billing::AdminDiscountManagerImpl")
billing_DiscountManagerImpl = Class(name="billing::DiscountManagerImpl")
billing_AdminDiscountManager = Class(name="billing::AdminDiscountManager")
tda593_booking_Organization = Class(name="tda593::booking::Organization")
LegalEntity = Class(name="LegalEntity")
tda593_booking_Person = Class(name="tda593::booking::Person")
booking_TravelInformation = Class(name="booking::TravelInformation")
booking_RoomStay = Class(name="booking::RoomStay")
tda593_booking_TravelInformation = Class(name="tda593::booking::TravelInformation")
tda593_booking_RoomStay = Class(name="tda593::booking::RoomStay")
tda593_booking_Booking = Class(name="tda593::booking::Booking")
tda593_booking_BookingManager = Class(name="tda593::booking::BookingManager", is_abstract=True)
booking_StayRequest = Class(name="booking::StayRequest")
booking_Person = Class(name="booking::Person")
facilities_Room = Class(name="facilities::Room")
tda593_booking_StayRequest = Class(name="tda593::booking::StayRequest")
tda593_booking_BookingManagerImpl = Class(name="tda593::booking::BookingManagerImpl")
BookingManager = Class(name="BookingManager")
booking_BookingDataService = Class(name="booking::BookingDataService")
facilities_RoomManager = Class(name="facilities::RoomManager")
tda593_booking_BookingDataService = Class(name="tda593::booking::BookingDataService")
tda593_booking_LegalEntityManager = Class(name="tda593::booking::LegalEntityManager", is_abstract=True)
booking_LegalEntityDataService = Class(name="booking::LegalEntityDataService")
tda593_booking_LegalEntityDataService = Class(name="tda593::booking::LegalEntityDataService")
tda593_booking_LegalEntity = Class(name="tda593::booking::LegalEntity", is_abstract=True)
tda593_booking_LegalEntityManagerImpl = Class(name="tda593::booking::LegalEntityManagerImpl")
LegalEntityManager = Class(name="LegalEntityManager")

# tda593_california_DataService class attributes and methods
tda593_california_DataService_m_get: Method = Method(name="get", parameters={Parameter(name='id')})
tda593_california_DataService_m_getAll: Method = Method(name="getAll", parameters={})
tda593_california_DataService_m_count: Method = Method(name="count", parameters={}, type=IntegerType)
tda593_california_DataService_m_set: Method = Method(name="set", parameters={Parameter(name='object')})
tda593_california_DataService_m_setAll: Method = Method(name="setAll", parameters={Parameter(name='objects')})
tda593_california_DataService_m_delete: Method = Method(name="delete", parameters={Parameter(name='object')})
tda593_california_DataService_m_exist: Method = Method(name="exist", parameters={Parameter(name='object')}, type=BooleanType)
tda593_california_DataService.methods={tda593_california_DataService_m_count, tda593_california_DataService_m_delete, tda593_california_DataService_m_setAll, tda593_california_DataService_m_getAll, tda593_california_DataService_m_set, tda593_california_DataService_m_exist, tda593_california_DataService_m_get}

# tda593_facilities_AdminKeyCardManager class attributes and methods
tda593_facilities_AdminKeyCardManager_m_addKeyCard: Method = Method(name="addKeyCard", parameters={Parameter(name='cardNumber')})
tda593_facilities_AdminKeyCardManager_m_removeKeyCard: Method = Method(name="removeKeyCard", parameters={Parameter(name='cardNumber')})
tda593_facilities_AdminKeyCardManager.methods={tda593_facilities_AdminKeyCardManager_m_addKeyCard, tda593_facilities_AdminKeyCardManager_m_removeKeyCard}

# KeyCardManager class attributes and methods

# tda593_facilities_KeyCardManager class attributes and methods
tda593_facilities_KeyCardManager_m_getKeyCard: Method = Method(name="getKeyCard", parameters={Parameter(name='keyCardNbr')}, type=StringType)
tda593_facilities_KeyCardManager.methods={tda593_facilities_KeyCardManager_m_getKeyCard}

# tda593_facilities_KeyCard class attributes and methods
tda593_facilities_KeyCard_id: Property = Property(name="id", type=StringType)
tda593_facilities_KeyCard.attributes={tda593_facilities_KeyCard_id}

# tda593_facilities_AdminRoomManager class attributes and methods
tda593_facilities_AdminRoomManager_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='roomNumber')}, type=BooleanType)
tda593_facilities_AdminRoomManager_m_addRoomType: Method = Method(name="addRoomType", parameters={Parameter(name='description'), Parameter(name='roomApprovals'), Parameter(name='name'), Parameter(name='price')}, type=StringType)
tda593_facilities_AdminRoomManager_m_addConferenceRoom: Method = Method(name="addConferenceRoom", parameters={Parameter(name='photos'), Parameter(name='numberOfSeats'), Parameter(name='description'), Parameter(name='disabilityApprovals'), Parameter(name='number'), Parameter(name='equipment'), Parameter(name='floor'), Parameter(name='roomType')}, type=StringType)
tda593_facilities_AdminRoomManager_m_removeRoomType: Method = Method(name="removeRoomType", parameters={Parameter(name='roomType')}, type=BooleanType)
tda593_facilities_AdminRoomManager_m_addGuestRoom: Method = Method(name="addGuestRoom", parameters={Parameter(name='description'), Parameter(name='disabilityApprovals'), Parameter(name='numberOfExtraBeds'), Parameter(name='roomType'), Parameter(name='numberOfBeds'), Parameter(name='floor'), Parameter(name='photos'), Parameter(name='number')}, type=StringType)
tda593_facilities_AdminRoomManager.methods={tda593_facilities_AdminRoomManager_m_addRoomType, tda593_facilities_AdminRoomManager_m_removeRoomType, tda593_facilities_AdminRoomManager_m_addGuestRoom, tda593_facilities_AdminRoomManager_m_addConferenceRoom, tda593_facilities_AdminRoomManager_m_removeRoom}

# RoomManager class attributes and methods

# tda593_facilities_RoomManager class attributes and methods
tda593_facilities_RoomManager_m_getRoomTypes: Method = Method(name="getRoomTypes", parameters={}, type=StringType)
tda593_facilities_RoomManager_m_registerKeyCard: Method = Method(name="registerKeyCard", parameters={Parameter(name='keyCard'), Parameter(name='roomNumber')})
tda593_facilities_RoomManager_m_registerKeyCard: Method = Method(name="registerKeyCard", parameters={Parameter(name='roomNumber'), Parameter(name='keyCardNbr')})
tda593_facilities_RoomManager_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='roomNumber')}, type=StringType)
tda593_facilities_RoomManager_m_getRoomType: Method = Method(name="getRoomType", parameters={Parameter(name='name')}, type=StringType)
tda593_facilities_RoomManager_m_getGuestRooms: Method = Method(name="getGuestRooms", parameters={}, type=StringType)
tda593_facilities_RoomManager_m_getConferenceRooms: Method = Method(name="getConferenceRooms", parameters={}, type=StringType)
tda593_facilities_RoomManager_m_setIsBeingCleaned: Method = Method(name="setIsBeingCleaned", parameters={Parameter(name='value'), Parameter(name='room')})
tda593_facilities_RoomManager_m_getRooms: Method = Method(name="getRooms", parameters={}, type=StringType)
tda593_facilities_RoomManager_m_unregisterKeyCard: Method = Method(name="unregisterKeyCard", parameters={Parameter(name='roomNumber'), Parameter(name='keyCard')})
tda593_facilities_RoomManager_m_unregisterKeyCard: Method = Method(name="unregisterKeyCard", parameters={Parameter(name='keyCardNbr'), Parameter(name='roomNumber')})
tda593_facilities_RoomManager_m_unregisterAllKeyCards: Method = Method(name="unregisterAllKeyCards", parameters={Parameter(name='roomNumber')})
tda593_facilities_RoomManager_m_getRoomTypeAmounts: Method = Method(name="getRoomTypeAmounts", parameters={})
tda593_facilities_RoomManager_m_getRoomTypeAmount: Method = Method(name="getRoomTypeAmount", parameters={Parameter(name='roomType')}, type=IntegerType)
tda593_facilities_RoomManager.methods={tda593_facilities_RoomManager_m_getGuestRooms, tda593_facilities_RoomManager_m_getRooms, tda593_facilities_RoomManager_m_getConferenceRooms, tda593_facilities_RoomManager_m_unregisterKeyCard, tda593_facilities_RoomManager_m_getRoomType, tda593_facilities_RoomManager_m_setIsBeingCleaned, tda593_facilities_RoomManager_m_registerKeyCard, tda593_facilities_RoomManager_m_getRoomTypeAmount, tda593_facilities_RoomManager_m_getRoomTypeAmounts, tda593_facilities_RoomManager_m_getRoomTypes, tda593_facilities_RoomManager_m_getRoom, tda593_facilities_RoomManager_m_registerKeyCard, tda593_facilities_RoomManager_m_unregisterAllKeyCards, tda593_facilities_RoomManager_m_unregisterKeyCard}

# tda593_facilities_RoomType class attributes and methods
tda593_facilities_RoomType_name: Property = Property(name="name", type=StringType)
tda593_facilities_RoomType_description: Property = Property(name="description", type=StringType)
tda593_facilities_RoomType_roomApprovals: Property = Property(name="roomApprovals", type=StringType)
tda593_facilities_RoomType_price: Property = Property(name="price", type=FloatType)
tda593_facilities_RoomType.attributes={tda593_facilities_RoomType_name, tda593_facilities_RoomType_description, tda593_facilities_RoomType_roomApprovals, tda593_facilities_RoomType_price}

# tda593_facilities_Room class attributes and methods
tda593_facilities_Room_floor: Property = Property(name="floor", type=IntegerType)
tda593_facilities_Room_roomNumber: Property = Property(name="roomNumber", type=StringType)
tda593_facilities_Room_isOperational: Property = Property(name="isOperational", type=BooleanType)
tda593_facilities_Room_isBeingCleaned: Property = Property(name="isBeingCleaned", type=BooleanType)
tda593_facilities_Room_description: Property = Property(name="description", type=StringType)
tda593_facilities_Room_photos: Property = Property(name="photos", type=StringType)
tda593_facilities_Room_disabilityApprovals: Property = Property(name="disabilityApprovals", type=StringType)
tda593_facilities_Room_m_registerKeyCard: Method = Method(name="registerKeyCard", parameters={Parameter(name='keyCard')})
tda593_facilities_Room_m_unregisterKeyCard: Method = Method(name="unregisterKeyCard", parameters={Parameter(name='keyCard')})
tda593_facilities_Room_m_unregisterKeyCards: Method = Method(name="unregisterKeyCards", parameters={})
tda593_facilities_Room.attributes={tda593_facilities_Room_floor, tda593_facilities_Room_description, tda593_facilities_Room_isBeingCleaned, tda593_facilities_Room_disabilityApprovals, tda593_facilities_Room_isOperational, tda593_facilities_Room_roomNumber, tda593_facilities_Room_photos}
tda593_facilities_Room.methods={tda593_facilities_Room_m_unregisterKeyCard, tda593_facilities_Room_m_registerKeyCard, tda593_facilities_Room_m_unregisterKeyCards}

# facilities_KeyCard class attributes and methods

# tda593_facilities_RoomManagerImpl class attributes and methods

# facilities_RoomDataService class attributes and methods

# facilities_RoomTypeDataService class attributes and methods

# facilities_KeyCardManager class attributes and methods

# tda593_facilities_RoomDataService class attributes and methods
tda593_facilities_RoomDataService_m_getAllGuestRooms: Method = Method(name="getAllGuestRooms", parameters={}, type=StringType)
tda593_facilities_RoomDataService_m_getAllConferenceRooms: Method = Method(name="getAllConferenceRooms", parameters={}, type=StringType)
tda593_facilities_RoomDataService_m_getGuestRoom: Method = Method(name="getGuestRoom", parameters={Parameter(name='id')}, type=StringType)
tda593_facilities_RoomDataService_m_getConferenceRoom: Method = Method(name="getConferenceRoom", parameters={Parameter(name='id')}, type=StringType)
tda593_facilities_RoomDataService.methods={tda593_facilities_RoomDataService_m_getGuestRoom, tda593_facilities_RoomDataService_m_getAllConferenceRooms, tda593_facilities_RoomDataService_m_getAllGuestRooms, tda593_facilities_RoomDataService_m_getConferenceRoom}

# tda593_facilities_RoomTypeDataService class attributes and methods

# tda593_facilities_KeyCardManagerImpl class attributes and methods

# facilities_KeyCardDataService class attributes and methods

# tda593_facilities_KeyCardDataService class attributes and methods

# tda593_facilities_AdminRoomManagerImpl class attributes and methods

# facilities_RoomManagerImpl class attributes and methods

# facilities_AdminRoomManager class attributes and methods

# tda593_facilities_AdminKeyCardManagerImpl class attributes and methods

# facilities_KeyCardManagerImpl class attributes and methods

# facilities_AdminKeyCardManager class attributes and methods

# tda593_billing_DiscountManager class attributes and methods
tda593_billing_DiscountManager_m_getDiscount: Method = Method(name="getDiscount", parameters={Parameter(name='code')}, type=StringType)
tda593_billing_DiscountManager.methods={tda593_billing_DiscountManager_m_getDiscount}

# facilities_RoomType class attributes and methods

# tda593_facilities_GuestRoom class attributes and methods
tda593_facilities_GuestRoom_numberOfBeds: Property = Property(name="numberOfBeds", type=IntegerType)
tda593_facilities_GuestRoom_numberOfExtrabeds: Property = Property(name="numberOfExtrabeds", type=IntegerType)
tda593_facilities_GuestRoom.attributes={tda593_facilities_GuestRoom_numberOfExtrabeds, tda593_facilities_GuestRoom_numberOfBeds}

# Room class attributes and methods

# tda593_facilities_ConferenceRoom class attributes and methods
tda593_facilities_ConferenceRoom_equipment: Property = Property(name="equipment", type=StringType)
tda593_facilities_ConferenceRoom_numberOfSeats: Property = Property(name="numberOfSeats", type=IntegerType)
tda593_facilities_ConferenceRoom.attributes={tda593_facilities_ConferenceRoom_equipment, tda593_facilities_ConferenceRoom_numberOfSeats}

# billing_DiscountLimit class attributes and methods

# tda593_billing_DiscountLimit class attributes and methods
tda593_billing_DiscountLimit_id: Property = Property(name="id", type=IntegerType)
tda593_billing_DiscountLimit_startDate: Property = Property(name="startDate", type=DateType)
tda593_billing_DiscountLimit_endDate: Property = Property(name="endDate", type=DateType)
tda593_billing_DiscountLimit_timesLeftToUse: Property = Property(name="timesLeftToUse", type=IntegerType)
tda593_billing_DiscountLimit.attributes={tda593_billing_DiscountLimit_timesLeftToUse, tda593_billing_DiscountLimit_endDate, tda593_billing_DiscountLimit_id, tda593_billing_DiscountLimit_startDate}

# booking_LegalEntity class attributes and methods

# tda593_billing_SumDiscount class attributes and methods
tda593_billing_SumDiscount_discountSum: Property = Property(name="discountSum", type=FloatType)
tda593_billing_SumDiscount.attributes={tda593_billing_SumDiscount_discountSum}

# Discount class attributes and methods

# tda593_billing_PercentageDiscount class attributes and methods
tda593_billing_PercentageDiscount_percentage: Property = Property(name="percentage", type=FloatType)
tda593_billing_PercentageDiscount.attributes={tda593_billing_PercentageDiscount_percentage}

# tda593_billing_DiscountDataService class attributes and methods

# tda593_billing_DiscountManagerImpl class attributes and methods

# DiscountManager class attributes and methods

# billing_DiscountDataService class attributes and methods

# tda593_billing_Bill class attributes and methods
tda593_billing_Bill_id: Property = Property(name="id", type=IntegerType)
tda593_billing_Bill_date: Property = Property(name="date", type=DateType)
tda593_billing_Bill_isPublished: Property = Property(name="isPublished", type=BooleanType)
tda593_billing_Bill_isPaid: Property = Property(name="isPaid", type=BooleanType)
tda593_billing_Bill_m_applyDiscount: Method = Method(name="applyDiscount", parameters={Parameter(name='discount')})
tda593_billing_Bill_m_addSubBill: Method = Method(name="addSubBill", parameters={Parameter(name='subBill')})
tda593_billing_Bill_m_registerPurchase: Method = Method(name="registerPurchase", parameters={Parameter(name='purchase')})
tda593_billing_Bill_m_publishBill: Method = Method(name="publishBill", parameters={})
tda593_billing_Bill_m_unregisterPurchase: Method = Method(name="unregisterPurchase", parameters={Parameter(name='purchase')})
tda593_billing_Bill_m_removeSubBill: Method = Method(name="removeSubBill", parameters={Parameter(name='subBill')})
tda593_billing_Bill_m_unPublishBill: Method = Method(name="unPublishBill", parameters={})
tda593_billing_Bill_m_getPrice: Method = Method(name="getPrice", parameters={}, type=FloatType)
tda593_billing_Bill_m_removeDiscount: Method = Method(name="removeDiscount", parameters={Parameter(name='discount')})
tda593_billing_Bill.attributes={tda593_billing_Bill_date, tda593_billing_Bill_id, tda593_billing_Bill_isPublished, tda593_billing_Bill_isPaid}
tda593_billing_Bill.methods={tda593_billing_Bill_m_applyDiscount, tda593_billing_Bill_m_addSubBill, tda593_billing_Bill_m_getPrice, tda593_billing_Bill_m_unregisterPurchase, tda593_billing_Bill_m_removeDiscount, tda593_billing_Bill_m_unPublishBill, tda593_billing_Bill_m_registerPurchase, tda593_billing_Bill_m_removeSubBill, tda593_billing_Bill_m_publishBill}

# tda593_billing_Discount class attributes and methods
tda593_billing_Discount_code: Property = Property(name="code", type=StringType)
tda593_billing_Discount_name: Property = Property(name="name", type=StringType)
tda593_billing_Discount_m_getPriceWithDiscount: Method = Method(name="getPriceWithDiscount", parameters={Parameter(name='price')}, type=FloatType)
tda593_billing_Discount.attributes={tda593_billing_Discount_name, tda593_billing_Discount_code}
tda593_billing_Discount.methods={tda593_billing_Discount_m_getPriceWithDiscount}

# billing_Purchase class attributes and methods

# billing_Discount class attributes and methods

# billing_Bill class attributes and methods

# tda593_billing_Purchase class attributes and methods
tda593_billing_Purchase_id: Property = Property(name="id", type=IntegerType)
tda593_billing_Purchase_quantity: Property = Property(name="quantity", type=IntegerType)
tda593_billing_Purchase_price: Property = Property(name="price", type=FloatType)
tda593_billing_Purchase.attributes={tda593_billing_Purchase_quantity, tda593_billing_Purchase_price, tda593_billing_Purchase_id}

# billing_Service class attributes and methods

# tda593_billing_Service class attributes and methods
tda593_billing_Service_id: Property = Property(name="id", type=IntegerType)
tda593_billing_Service_price: Property = Property(name="price", type=FloatType)
tda593_billing_Service_name: Property = Property(name="name", type=StringType)
tda593_billing_Service.attributes={tda593_billing_Service_price, tda593_billing_Service_id, tda593_billing_Service_name}

# tda593_billing_BillManager class attributes and methods
tda593_billing_BillManager_m_getBill: Method = Method(name="getBill", parameters={Parameter(name='id')}, type=StringType)
tda593_billing_BillManager_m_getBookingBill: Method = Method(name="getBookingBill", parameters={Parameter(name='booking')}, type=StringType)
tda593_billing_BillManager_m_billItem: Method = Method(name="billItem", parameters={Parameter(name='quantity'), Parameter(name='bill'), Parameter(name='service')})
tda593_billing_BillManager_m_addSubBill: Method = Method(name="addSubBill", parameters={Parameter(name='toBill'), Parameter(name='subBill')})
tda593_billing_BillManager_m_applyDiscount: Method = Method(name="applyDiscount", parameters={Parameter(name='discount'), Parameter(name='bill')})
tda593_billing_BillManager_m_publishBill: Method = Method(name="publishBill", parameters={Parameter(name='bill')})
tda593_billing_BillManager_m_markBillAsPaid: Method = Method(name="markBillAsPaid", parameters={Parameter(name='bill'), Parameter(name='isPaid'), Parameter(name='creditCardManager'), Parameter(name='bankingManager')}, type=BooleanType)
tda593_billing_BillManager_m_createBill: Method = Method(name="createBill", parameters={Parameter(name='customer')}, type=StringType)
tda593_billing_BillManager_m_createBookingBill: Method = Method(name="createBookingBill", parameters={Parameter(name='booking'), Parameter(name='customer')}, type=StringType)
tda593_billing_BillManager_m_getBills: Method = Method(name="getBills", parameters={Parameter(name='customer')}, type=StringType)
tda593_billing_BillManager_m_getUnpaidBills: Method = Method(name="getUnpaidBills", parameters={Parameter(name='customer')}, type=StringType)
tda593_billing_BillManager.methods={tda593_billing_BillManager_m_getBookingBill, tda593_billing_BillManager_m_getBills, tda593_billing_BillManager_m_getUnpaidBills, tda593_billing_BillManager_m_billItem, tda593_billing_BillManager_m_getBill, tda593_billing_BillManager_m_markBillAsPaid, tda593_billing_BillManager_m_applyDiscount, tda593_billing_BillManager_m_createBill, tda593_billing_BillManager_m_publishBill, tda593_billing_BillManager_m_createBookingBill, tda593_billing_BillManager_m_addSubBill}

# tda593_billing_BookingBill class attributes and methods

# Bill class attributes and methods

# booking_Booking class attributes and methods

# tda593_billing_CreditCardManager class attributes and methods
tda593_billing_CreditCardManager_m_setCreditCardInformation: Method = Method(name="setCreditCardInformation", parameters={Parameter(name='cardNumber'), Parameter(name='legalEntity'), Parameter(name='lastname'), Parameter(name='expirationDate'), Parameter(name='firstname'), Parameter(name='validator'), Parameter(name='ccv')}, type=BooleanType)
tda593_billing_CreditCardManager_m_getCreditCardInformation: Method = Method(name="getCreditCardInformation", parameters={Parameter(name='legalEntity')}, type=StringType)
tda593_billing_CreditCardManager_m_getCreditCardInformation: Method = Method(name="getCreditCardInformation", parameters={Parameter(name='legalEntityId')}, type=StringType)
tda593_billing_CreditCardManager_m_revalidateCreditCardInformation: Method = Method(name="revalidateCreditCardInformation", parameters={Parameter(name='legalEntity'), Parameter(name='bankingManager')}, type=BooleanType)
tda593_billing_CreditCardManager.methods={tda593_billing_CreditCardManager_m_getCreditCardInformation, tda593_billing_CreditCardManager_m_setCreditCardInformation, tda593_billing_CreditCardManager_m_revalidateCreditCardInformation, tda593_billing_CreditCardManager_m_getCreditCardInformation}

# tda593_billing_CreditCardInformation class attributes and methods
tda593_billing_CreditCardInformation_cardNumber: Property = Property(name="cardNumber", type=StringType)
tda593_billing_CreditCardInformation_expirationDate: Property = Property(name="expirationDate", type=DateType)
tda593_billing_CreditCardInformation_ccv: Property = Property(name="ccv", type=StringType)
tda593_billing_CreditCardInformation_firstName: Property = Property(name="firstName", type=StringType)
tda593_billing_CreditCardInformation_lastName: Property = Property(name="lastName", type=StringType)
tda593_billing_CreditCardInformation.attributes={tda593_billing_CreditCardInformation_firstName, tda593_billing_CreditCardInformation_ccv, tda593_billing_CreditCardInformation_expirationDate, tda593_billing_CreditCardInformation_cardNumber, tda593_billing_CreditCardInformation_lastName}

# tda593_billing_BankingManager class attributes and methods
tda593_billing_BankingManager_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='expiryMonth'), Parameter(name='sum'), Parameter(name='lastName'), Parameter(name='ccv'), Parameter(name='firstName'), Parameter(name='ccNumber'), Parameter(name='expiryYear')}, type=BooleanType)
tda593_billing_BankingManager_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='lastName'), Parameter(name='expiryYear'), Parameter(name='firstName'), Parameter(name='expiryMonth'), Parameter(name='ccv'), Parameter(name='ccNumber')}, type=BooleanType)
tda593_billing_BankingManager.methods={tda593_billing_BankingManager_m_isCreditCardValid, tda593_billing_BankingManager_m_makePayment}

# tda593_billing_BankingManagerImpl class attributes and methods

# BankingManager class attributes and methods

# tda593_billing_CreditCardInformationDataService class attributes and methods
tda593_billing_CreditCardInformationDataService_m_getByLegalEntity: Method = Method(name="getByLegalEntity", parameters={Parameter(name='legalEntityId')}, type=StringType)
tda593_billing_CreditCardInformationDataService.methods={tda593_billing_CreditCardInformationDataService_m_getByLegalEntity}

# tda593_billing_CreditCardManagerImpl class attributes and methods

# CreditCardManager class attributes and methods

# billing_CreditCardInformationDataService class attributes and methods

# tda593_billing_ServiceManagerImpl class attributes and methods

# ServiceManager class attributes and methods

# billing_ServiceDataService class attributes and methods

# tda593_billing_ServiceManager class attributes and methods
tda593_billing_ServiceManager_m_getAllServices: Method = Method(name="getAllServices", parameters={}, type=StringType)
tda593_billing_ServiceManager_m_getService: Method = Method(name="getService", parameters={Parameter(name='id')}, type=StringType)
tda593_billing_ServiceManager.methods={tda593_billing_ServiceManager_m_getService, tda593_billing_ServiceManager_m_getAllServices}

# tda593_billing_ServiceDataService class attributes and methods

# tda593_billing_AdminServiceManager class attributes and methods
tda593_billing_AdminServiceManager_m_createService: Method = Method(name="createService", parameters={Parameter(name='price'), Parameter(name='name')}, type=StringType)
tda593_billing_AdminServiceManager_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='service')})
tda593_billing_AdminServiceManager.methods={tda593_billing_AdminServiceManager_m_createService, tda593_billing_AdminServiceManager_m_removeService}

# tda593_billing_AdminServiceManagerImpl class attributes and methods

# billing_ServiceManagerImpl class attributes and methods

# billing_AdminServiceManager class attributes and methods

# tda593_billing_AdminDiscountManager class attributes and methods
tda593_billing_AdminDiscountManager_m_createDiscountLimitForDiscount: Method = Method(name="createDiscountLimitForDiscount", parameters={Parameter(name='users'), Parameter(name='usesAmount'), Parameter(name='to'), Parameter(name='from'), Parameter(name='discount')})
tda593_billing_AdminDiscountManager_m_setAmountLimit: Method = Method(name="setAmountLimit", parameters={Parameter(name='usesAmount'), Parameter(name='discount')})
tda593_billing_AdminDiscountManager_m_setDateRangeLimit: Method = Method(name="setDateRangeLimit", parameters={Parameter(name='discount'), Parameter(name='validTo'), Parameter(name='validFrom')})
tda593_billing_AdminDiscountManager_m_addAllowedUsers: Method = Method(name="addAllowedUsers", parameters={Parameter(name='legalEntities'), Parameter(name='discount')})
tda593_billing_AdminDiscountManager_m_addPercentageDiscount: Method = Method(name="addPercentageDiscount", parameters={Parameter(name='percentage'), Parameter(name='code'), Parameter(name='name')}, type=StringType)
tda593_billing_AdminDiscountManager_m_addSumDiscount: Method = Method(name="addSumDiscount", parameters={Parameter(name='code'), Parameter(name='name'), Parameter(name='sum')}, type=StringType)
tda593_billing_AdminDiscountManager.methods={tda593_billing_AdminDiscountManager_m_setAmountLimit, tda593_billing_AdminDiscountManager_m_addPercentageDiscount, tda593_billing_AdminDiscountManager_m_createDiscountLimitForDiscount, tda593_billing_AdminDiscountManager_m_addSumDiscount, tda593_billing_AdminDiscountManager_m_addAllowedUsers, tda593_billing_AdminDiscountManager_m_setDateRangeLimit}

# tda593_billing_BillManagerImpl class attributes and methods

# BillManager class attributes and methods

# billing_BillDataService class attributes and methods

# booking_BookingManager class attributes and methods

# tda593_billing_BillDataService class attributes and methods
tda593_billing_BillDataService_m_getAll: Method = Method(name="getAll", parameters={Parameter(name='customer')}, type=StringType)
tda593_billing_BillDataService_m_getBookingBill: Method = Method(name="getBookingBill", parameters={Parameter(name='booking')}, type=StringType)
tda593_billing_BillDataService.methods={tda593_billing_BillDataService_m_getAll, tda593_billing_BillDataService_m_getBookingBill}

# tda593_billing_AdminDiscountManagerImpl class attributes and methods

# billing_DiscountManagerImpl class attributes and methods

# billing_AdminDiscountManager class attributes and methods

# tda593_booking_Organization class attributes and methods
tda593_booking_Organization_name: Property = Property(name="name", type=StringType)
tda593_booking_Organization_organizationNumber: Property = Property(name="organizationNumber", type=StringType)
tda593_booking_Organization.attributes={tda593_booking_Organization_name, tda593_booking_Organization_organizationNumber}

# LegalEntity class attributes and methods

# tda593_booking_Person class attributes and methods
tda593_booking_Person_firstname: Property = Property(name="firstname", type=StringType)
tda593_booking_Person_lastname: Property = Property(name="lastname", type=StringType)
tda593_booking_Person_socialSecurityNumber: Property = Property(name="socialSecurityNumber", type=StringType)
tda593_booking_Person.attributes={tda593_booking_Person_socialSecurityNumber, tda593_booking_Person_firstname, tda593_booking_Person_lastname}

# booking_TravelInformation class attributes and methods

# booking_RoomStay class attributes and methods

# tda593_booking_TravelInformation class attributes and methods
tda593_booking_TravelInformation_id: Property = Property(name="id", type=IntegerType)
tda593_booking_TravelInformation_trackingId: Property = Property(name="trackingId", type=StringType)
tda593_booking_TravelInformation_comment: Property = Property(name="comment", type=StringType)
tda593_booking_TravelInformation.attributes={tda593_booking_TravelInformation_id, tda593_booking_TravelInformation_trackingId, tda593_booking_TravelInformation_comment}

# tda593_booking_RoomStay class attributes and methods
tda593_booking_RoomStay_active: Property = Property(name="active", type=BooleanType)
tda593_booking_RoomStay_id: Property = Property(name="id", type=IntegerType)
tda593_booking_RoomStay.attributes={tda593_booking_RoomStay_active, tda593_booking_RoomStay_id}

# tda593_booking_Booking class attributes and methods
tda593_booking_Booking_endDate: Property = Property(name="endDate", type=DateType)
tda593_booking_Booking_specialRequest: Property = Property(name="specialRequest", type=StringType)
tda593_booking_Booking_price: Property = Property(name="price", type=FloatType)
tda593_booking_Booking_isCanceled: Property = Property(name="isCanceled", type=BooleanType)
tda593_booking_Booking_id: Property = Property(name="id", type=IntegerType)
tda593_booking_Booking_startDate: Property = Property(name="startDate", type=DateType)
tda593_booking_Booking_m_registerTravelInformation: Method = Method(name="registerTravelInformation", parameters={Parameter(name='travelInformation')})
tda593_booking_Booking_m_unregisterTravelInformation: Method = Method(name="unregisterTravelInformation", parameters={Parameter(name='travelInformation')})
tda593_booking_Booking_m_getStayRequests: Method = Method(name="getStayRequests", parameters={}, type=StringType)
tda593_booking_Booking_m_getGuests: Method = Method(name="getGuests", parameters={}, type=StringType)
tda593_booking_Booking.attributes={tda593_booking_Booking_startDate, tda593_booking_Booking_specialRequest, tda593_booking_Booking_id, tda593_booking_Booking_price, tda593_booking_Booking_endDate, tda593_booking_Booking_isCanceled}
tda593_booking_Booking.methods={tda593_booking_Booking_m_registerTravelInformation, tda593_booking_Booking_m_getGuests, tda593_booking_Booking_m_unregisterTravelInformation, tda593_booking_Booking_m_getStayRequests}

# tda593_booking_BookingManager class attributes and methods
tda593_booking_BookingManager_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
tda593_booking_BookingManager_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='customer'), Parameter(name='to'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingManager_m_getBookings: Method = Method(name="getBookings", parameters={Parameter(name='customer')}, type=StringType)
tda593_booking_BookingManager_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingManager_m_getAvailableRooms: Method = Method(name="getAvailableRooms", parameters={Parameter(name='roomType'), Parameter(name='from'), Parameter(name='to')}, type=StringType)
tda593_booking_BookingManager_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='customer'), Parameter(name='to'), Parameter(name='roomType'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingManager_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='room'), Parameter(name='to'), Parameter(name='customer'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingManager_m_isRoomAvailable: Method = Method(name="isRoomAvailable", parameters={Parameter(name='roomNumber'), Parameter(name='to'), Parameter(name='from')}, type=BooleanType)
tda593_booking_BookingManager_m_registerRoom: Method = Method(name="registerRoom", parameters={Parameter(name='room'), Parameter(name='booking')})
tda593_booking_BookingManager_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='guests'), Parameter(name='booking')})
tda593_booking_BookingManager_m_isRoomTypeAvailable: Method = Method(name="isRoomTypeAvailable", parameters={Parameter(name='roomType'), Parameter(name='to'), Parameter(name='from')}, type=BooleanType)
tda593_booking_BookingManager_m_getActiveBooking: Method = Method(name="getActiveBooking", parameters={Parameter(name='roomNumber')}, type=StringType)
tda593_booking_BookingManager_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='booking')})
tda593_booking_BookingManager_m_getAvailableRoomTypeAmounts: Method = Method(name="getAvailableRoomTypeAmounts", parameters={Parameter(name='from'), Parameter(name='to')})
tda593_booking_BookingManager_m_getAvailableRoomTypeAmount: Method = Method(name="getAvailableRoomTypeAmount", parameters={Parameter(name='from'), Parameter(name='roomType'), Parameter(name='to')}, type=IntegerType)
tda593_booking_BookingManager_m_addStayRequest: Method = Method(name="addStayRequest", parameters={Parameter(name='booking'), Parameter(name='stayRequest')}, type=StringType)
tda593_booking_BookingManager_m_removeStayRequest: Method = Method(name="removeStayRequest", parameters={Parameter(name='booking'), Parameter(name='stayRequest')})
tda593_booking_BookingManager_m_getStayRequests: Method = Method(name="getStayRequests", parameters={})
tda593_booking_BookingManager_m_setSpecialRequest: Method = Method(name="setSpecialRequest", parameters={Parameter(name='specialRequest'), Parameter(name='booking')})
tda593_booking_BookingManager_m_cancelBooking: Method = Method(name="cancelBooking", parameters={Parameter(name='booking')})
tda593_booking_BookingManager_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='bookingId')}, type=StringType)
tda593_booking_BookingManager_m_changeBookingDates: Method = Method(name="changeBookingDates", parameters={Parameter(name='newEnd'), Parameter(name='booking'), Parameter(name='newStart')}, type=BooleanType)
tda593_booking_BookingManager.methods={tda593_booking_BookingManager_m_isRoomTypeAvailable, tda593_booking_BookingManager_m_addStayRequest, tda593_booking_BookingManager_m_getBookings, tda593_booking_BookingManager_m_cancelBooking, tda593_booking_BookingManager_m_registerRoom, tda593_booking_BookingManager_m_checkIn, tda593_booking_BookingManager_m_getBookings, tda593_booking_BookingManager_m_changeBookingDates, tda593_booking_BookingManager_m_getBooking, tda593_booking_BookingManager_m_isRoomAvailable, tda593_booking_BookingManager_m_getBookings, tda593_booking_BookingManager_m_removeStayRequest, tda593_booking_BookingManager_m_createBooking, tda593_booking_BookingManager_m_getStayRequests, tda593_booking_BookingManager_m_getAvailableRooms, tda593_booking_BookingManager_m_getAvailableRooms, tda593_booking_BookingManager_m_getAvailableRoomTypeAmount, tda593_booking_BookingManager_m_createBooking, tda593_booking_BookingManager_m_getActiveBooking, tda593_booking_BookingManager_m_setSpecialRequest, tda593_booking_BookingManager_m_checkOut, tda593_booking_BookingManager_m_getAvailableRoomTypeAmounts}

# booking_StayRequest class attributes and methods

# booking_Person class attributes and methods

# facilities_Room class attributes and methods

# tda593_booking_StayRequest class attributes and methods
tda593_booking_StayRequest_text: Property = Property(name="text", type=StringType)
tda593_booking_StayRequest_timeStamp: Property = Property(name="timeStamp", type=DateType)
tda593_booking_StayRequest_id: Property = Property(name="id", type=IntegerType)
tda593_booking_StayRequest.attributes={tda593_booking_StayRequest_id, tda593_booking_StayRequest_text, tda593_booking_StayRequest_timeStamp}

# tda593_booking_BookingManagerImpl class attributes and methods

# BookingManager class attributes and methods

# booking_BookingDataService class attributes and methods

# facilities_RoomManager class attributes and methods

# tda593_booking_BookingDataService class attributes and methods
tda593_booking_BookingDataService_m_getAll: Method = Method(name="getAll", parameters={Parameter(name='customer')}, type=StringType)
tda593_booking_BookingDataService_m_getAll: Method = Method(name="getAll", parameters={Parameter(name='to'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingDataService_m_beginTransaction: Method = Method(name="beginTransaction", parameters={})
tda593_booking_BookingDataService_m_commitTransaction: Method = Method(name="commitTransaction", parameters={})
tda593_booking_BookingDataService_m_rollbackTransaction: Method = Method(name="rollbackTransaction", parameters={})
tda593_booking_BookingDataService_m_getAll: Method = Method(name="getAll", parameters={Parameter(name='to'), Parameter(name='roomNumber'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingDataService_m_getAll: Method = Method(name="getAll", parameters={Parameter(name='to'), Parameter(name='legal'), Parameter(name='from')}, type=StringType)
tda593_booking_BookingDataService.methods={tda593_booking_BookingDataService_m_getAll, tda593_booking_BookingDataService_m_commitTransaction, tda593_booking_BookingDataService_m_beginTransaction, tda593_booking_BookingDataService_m_rollbackTransaction, tda593_booking_BookingDataService_m_getAll, tda593_booking_BookingDataService_m_getAll, tda593_booking_BookingDataService_m_getAll}

# tda593_booking_LegalEntityManager class attributes and methods
tda593_booking_LegalEntityManager_m_findPerson: Method = Method(name="findPerson", parameters={Parameter(name='firstname'), Parameter(name='lastname')}, type=StringType)
tda593_booking_LegalEntityManager_m_findOrganization: Method = Method(name="findOrganization", parameters={Parameter(name='name')}, type=StringType)
tda593_booking_LegalEntityManager_m_getOrganization: Method = Method(name="getOrganization", parameters={Parameter(name='organizationNumber')}, type=StringType)
tda593_booking_LegalEntityManager_m_getPerson: Method = Method(name="getPerson", parameters={Parameter(name='SSN')}, type=StringType)
tda593_booking_LegalEntityManager_m_createPerson: Method = Method(name="createPerson", parameters={Parameter(name='SSN'), Parameter(name='firstname'), Parameter(name='lastname'), Parameter(name='email'), Parameter(name='phone')}, type=StringType)
tda593_booking_LegalEntityManager_m_createOrganization: Method = Method(name="createOrganization", parameters={Parameter(name='phone'), Parameter(name='organizationNumber'), Parameter(name='name'), Parameter(name='email')}, type=StringType)
tda593_booking_LegalEntityManager_m_getLegalEntity: Method = Method(name="getLegalEntity", parameters={Parameter(name='id')}, type=StringType)
tda593_booking_LegalEntityManager.methods={tda593_booking_LegalEntityManager_m_createOrganization, tda593_booking_LegalEntityManager_m_findPerson, tda593_booking_LegalEntityManager_m_createPerson, tda593_booking_LegalEntityManager_m_getOrganization, tda593_booking_LegalEntityManager_m_getLegalEntity, tda593_booking_LegalEntityManager_m_findOrganization, tda593_booking_LegalEntityManager_m_getPerson}

# booking_LegalEntityDataService class attributes and methods

# tda593_booking_LegalEntityDataService class attributes and methods
tda593_booking_LegalEntityDataService_m_findPerson: Method = Method(name="findPerson", parameters={Parameter(name='firstname'), Parameter(name='lastname')}, type=StringType)
tda593_booking_LegalEntityDataService_m_findOrganization: Method = Method(name="findOrganization", parameters={Parameter(name='name')}, type=StringType)
tda593_booking_LegalEntityDataService_m_getOrganization: Method = Method(name="getOrganization", parameters={Parameter(name='organizationNumber')}, type=StringType)
tda593_booking_LegalEntityDataService_m_getPerson: Method = Method(name="getPerson", parameters={Parameter(name='SSN')}, type=StringType)
tda593_booking_LegalEntityDataService.methods={tda593_booking_LegalEntityDataService_m_getPerson, tda593_booking_LegalEntityDataService_m_findPerson, tda593_booking_LegalEntityDataService_m_findOrganization, tda593_booking_LegalEntityDataService_m_getOrganization}

# tda593_booking_LegalEntity class attributes and methods
tda593_booking_LegalEntity_phone: Property = Property(name="phone", type=StringType)
tda593_booking_LegalEntity_email: Property = Property(name="email", type=StringType)
tda593_booking_LegalEntity_id: Property = Property(name="id", type=IntegerType)
tda593_booking_LegalEntity_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
tda593_booking_LegalEntity.attributes={tda593_booking_LegalEntity_phone, tda593_booking_LegalEntity_id, tda593_booking_LegalEntity_email}
tda593_booking_LegalEntity.methods={tda593_booking_LegalEntity_m_getName}

# tda593_booking_LegalEntityManagerImpl class attributes and methods

# LegalEntityManager class attributes and methods

# Relationships
roomDataService3: BinaryAssociation = BinaryAssociation(
    name="roomDataService3",
    ends={
        Property(name="facilities_RoomDataService", type=tda593_facilities_RoomManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_RoomManagerImpl", type=facilities_RoomDataService, multiplicity=Multiplicity(1, 1))
    }
)
roomTypeDataService4: BinaryAssociation = BinaryAssociation(
    name="roomTypeDataService4",
    ends={
        Property(name="facilities_RoomTypeDataService", type=tda593_facilities_RoomManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_RoomManagerImpl5", type=facilities_RoomTypeDataService, multiplicity=Multiplicity(1, 1))
    }
)
keyCardManager6: BinaryAssociation = BinaryAssociation(
    name="keyCardManager6",
    ends={
        Property(name="facilities_KeyCardManager", type=tda593_facilities_RoomManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_RoomManagerImpl7", type=facilities_KeyCardManager, multiplicity=Multiplicity(1, 1))
    }
)
keyCardDataService8: BinaryAssociation = BinaryAssociation(
    name="keyCardDataService8",
    ends={
        Property(name="facilities_KeyCardDataService", type=tda593_facilities_KeyCardManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_KeyCardManagerImpl", type=facilities_KeyCardDataService, multiplicity=Multiplicity(1, 1))
    }
)
allowedKeyCards0: BinaryAssociation = BinaryAssociation(
    name="allowedKeyCards0",
    ends={
        Property(name="facilities_KeyCard", type=tda593_facilities_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_Room", type=facilities_KeyCard, multiplicity=Multiplicity(0, 9999))
    }
)
roomType1: BinaryAssociation = BinaryAssociation(
    name="roomType1",
    ends={
        Property(name="facilities_RoomType", type=tda593_facilities_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_facilities_Room2", type=facilities_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
discountLimit9: BinaryAssociation = BinaryAssociation(
    name="discountLimit9",
    ends={
        Property(name="billing_DiscountLimit", type=tda593_billing_Discount, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Discount", type=billing_DiscountLimit, multiplicity=Multiplicity(0, 1))
    }
)
allowedUsers10: BinaryAssociation = BinaryAssociation(
    name="allowedUsers10",
    ends={
        Property(name="booking_LegalEntity", type=tda593_billing_DiscountLimit, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_DiscountLimit", type=booking_LegalEntity, multiplicity=Multiplicity(0, 9999))
    }
)
discountDataService11: BinaryAssociation = BinaryAssociation(
    name="discountDataService11",
    ends={
        Property(name="billing_DiscountDataService", type=tda593_billing_DiscountManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_DiscountManagerImpl", type=billing_DiscountDataService, multiplicity=Multiplicity(1, 1))
    }
)
purchases12: BinaryAssociation = BinaryAssociation(
    name="purchases12",
    ends={
        Property(name="billing_Purchase", type=tda593_billing_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Bill", type=billing_Purchase, multiplicity=Multiplicity(0, 9999))
    }
)
usedDiscounts13: BinaryAssociation = BinaryAssociation(
    name="usedDiscounts13",
    ends={
        Property(name="billing_Discount", type=tda593_billing_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Bill14", type=billing_Discount, multiplicity=Multiplicity(0, 9999))
    }
)
customer15: BinaryAssociation = BinaryAssociation(
    name="customer15",
    ends={
        Property(name="booking_LegalEntity17", type=tda593_billing_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Bill16", type=booking_LegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
subBills18: BinaryAssociation = BinaryAssociation(
    name="subBills18",
    ends={
        Property(name="billing_Bill", type=tda593_billing_Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Bill19", type=billing_Bill, multiplicity=Multiplicity(0, 9999))
    }
)
service20: BinaryAssociation = BinaryAssociation(
    name="service20",
    ends={
        Property(name="billing_Service", type=tda593_billing_Purchase, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_Purchase", type=billing_Service, multiplicity=Multiplicity(1, 1))
    }
)
booking21: BinaryAssociation = BinaryAssociation(
    name="booking21",
    ends={
        Property(name="booking_Booking", type=tda593_billing_BookingBill, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_BookingBill", type=booking_Booking, multiplicity=Multiplicity(1, 1))
    }
)
creditCardInformationDataService27: BinaryAssociation = BinaryAssociation(
    name="creditCardInformationDataService27",
    ends={
        Property(name="billing_CreditCardInformationDataService", type=tda593_billing_CreditCardManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_CreditCardManagerImpl", type=billing_CreditCardInformationDataService, multiplicity=Multiplicity(1, 1))
    }
)
serviceDataService28: BinaryAssociation = BinaryAssociation(
    name="serviceDataService28",
    ends={
        Property(name="billing_ServiceDataService", type=tda593_billing_ServiceManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_ServiceManagerImpl", type=billing_ServiceDataService, multiplicity=Multiplicity(1, 1))
    }
)
legalEntity22: BinaryAssociation = BinaryAssociation(
    name="legalEntity22",
    ends={
        Property(name="booking_LegalEntity23", type=tda593_billing_CreditCardInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_CreditCardInformation", type=booking_LegalEntity, multiplicity=Multiplicity(0, 1))
    }
)
billDataService24: BinaryAssociation = BinaryAssociation(
    name="billDataService24",
    ends={
        Property(name="billing_BillDataService", type=tda593_billing_BillManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_BillManagerImpl", type=billing_BillDataService, multiplicity=Multiplicity(1, 1))
    }
)
bookingManager25: BinaryAssociation = BinaryAssociation(
    name="bookingManager25",
    ends={
        Property(name="booking_BookingManager", type=tda593_billing_BillManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_billing_BillManagerImpl26", type=booking_BookingManager, multiplicity=Multiplicity(1, 1))
    }
)
roomType29: BinaryAssociation = BinaryAssociation(
    name="roomType29",
    ends={
        Property(name="facilities_RoomType30", type=tda593_booking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_Booking", type=facilities_RoomType, multiplicity=Multiplicity(1, 1))
    }
)
travelInformation31: BinaryAssociation = BinaryAssociation(
    name="travelInformation31",
    ends={
        Property(name="booking_TravelInformation", type=tda593_booking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_Booking32", type=booking_TravelInformation, multiplicity=Multiplicity(0, 1))
    }
)
responsible33: BinaryAssociation = BinaryAssociation(
    name="responsible33",
    ends={
        Property(name="booking_LegalEntity35", type=tda593_booking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_Booking34", type=booking_LegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
roomStay36: BinaryAssociation = BinaryAssociation(
    name="roomStay36",
    ends={
        Property(name="booking_RoomStay", type=tda593_booking_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_Booking37", type=booking_RoomStay, multiplicity=Multiplicity(0, 1))
    }
)
predecessor38: BinaryAssociation = BinaryAssociation(
    name="predecessor38",
    ends={
        Property(name="booking_TravelInformation39", type=tda593_booking_TravelInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_TravelInformation", type=booking_TravelInformation, multiplicity=Multiplicity(0, 1))
    }
)
stayRequest40: BinaryAssociation = BinaryAssociation(
    name="stayRequest40",
    ends={
        Property(name="booking_StayRequest", type=tda593_booking_RoomStay, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_RoomStay", type=booking_StayRequest, multiplicity=Multiplicity(0, 9999))
    }
)
registeredPersons41: BinaryAssociation = BinaryAssociation(
    name="registeredPersons41",
    ends={
        Property(name="booking_Person", type=tda593_booking_RoomStay, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_RoomStay42", type=booking_Person, multiplicity=Multiplicity(0, 9999))
    }
)
room43: BinaryAssociation = BinaryAssociation(
    name="room43",
    ends={
        Property(name="facilities_Room", type=tda593_booking_RoomStay, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_RoomStay44", type=facilities_Room, multiplicity=Multiplicity(1, 1))
    }
)
bookingDataService45: BinaryAssociation = BinaryAssociation(
    name="bookingDataService45",
    ends={
        Property(name="booking_BookingDataService", type=tda593_booking_BookingManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_BookingManagerImpl", type=booking_BookingDataService, multiplicity=Multiplicity(1, 1))
    }
)
roomManager46: BinaryAssociation = BinaryAssociation(
    name="roomManager46",
    ends={
        Property(name="facilities_RoomManager", type=tda593_booking_BookingManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_BookingManagerImpl47", type=facilities_RoomManager, multiplicity=Multiplicity(1, 1))
    }
)
legalEntityDataService48: BinaryAssociation = BinaryAssociation(
    name="legalEntityDataService48",
    ends={
        Property(name="booking_LegalEntityDataService", type=tda593_booking_LegalEntityManagerImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="tda593_booking_LegalEntityManagerImpl", type=booking_LegalEntityDataService, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_tda593_facilities_AdminRoomManager_RoomManager = Generalization(general=RoomManager, specific=tda593_facilities_AdminRoomManager)
gen_tda593_facilities_AdminKeyCardManager_KeyCardManager = Generalization(general=KeyCardManager, specific=tda593_facilities_AdminKeyCardManager)
gen_tda593_facilities_RoomManagerImpl_RoomManager = Generalization(general=RoomManager, specific=tda593_facilities_RoomManagerImpl)
gen_tda593_facilities_KeyCardManagerImpl_KeyCardManager = Generalization(general=KeyCardManager, specific=tda593_facilities_KeyCardManagerImpl)
gen_tda593_facilities_AdminRoomManagerImpl_facilities_RoomManagerImpl = Generalization(general=facilities_RoomManagerImpl, specific=tda593_facilities_AdminRoomManagerImpl)
gen_tda593_facilities_AdminRoomManagerImpl_facilities_AdminRoomManager = Generalization(general=facilities_AdminRoomManager, specific=tda593_facilities_AdminRoomManagerImpl)
gen_tda593_facilities_AdminKeyCardManagerImpl_facilities_KeyCardManagerImpl = Generalization(general=facilities_KeyCardManagerImpl, specific=tda593_facilities_AdminKeyCardManagerImpl)
gen_tda593_facilities_AdminKeyCardManagerImpl_facilities_AdminKeyCardManager = Generalization(general=facilities_AdminKeyCardManager, specific=tda593_facilities_AdminKeyCardManagerImpl)
gen_tda593_facilities_GuestRoom_Room = Generalization(general=Room, specific=tda593_facilities_GuestRoom)
gen_tda593_facilities_ConferenceRoom_Room = Generalization(general=Room, specific=tda593_facilities_ConferenceRoom)
gen_tda593_billing_SumDiscount_Discount = Generalization(general=Discount, specific=tda593_billing_SumDiscount)
gen_tda593_billing_PercentageDiscount_Discount = Generalization(general=Discount, specific=tda593_billing_PercentageDiscount)
gen_tda593_billing_DiscountManagerImpl_DiscountManager = Generalization(general=DiscountManager, specific=tda593_billing_DiscountManagerImpl)
gen_tda593_billing_BookingBill_Bill = Generalization(general=Bill, specific=tda593_billing_BookingBill)
gen_tda593_billing_BankingManagerImpl_BankingManager = Generalization(general=BankingManager, specific=tda593_billing_BankingManagerImpl)
gen_tda593_billing_CreditCardManagerImpl_CreditCardManager = Generalization(general=CreditCardManager, specific=tda593_billing_CreditCardManagerImpl)
gen_tda593_billing_ServiceManagerImpl_ServiceManager = Generalization(general=ServiceManager, specific=tda593_billing_ServiceManagerImpl)
gen_tda593_billing_AdminServiceManager_ServiceManager = Generalization(general=ServiceManager, specific=tda593_billing_AdminServiceManager)
gen_tda593_billing_AdminServiceManagerImpl_billing_ServiceManagerImpl = Generalization(general=billing_ServiceManagerImpl, specific=tda593_billing_AdminServiceManagerImpl)
gen_tda593_billing_AdminServiceManagerImpl_billing_AdminServiceManager = Generalization(general=billing_AdminServiceManager, specific=tda593_billing_AdminServiceManagerImpl)
gen_tda593_billing_AdminDiscountManager_DiscountManager = Generalization(general=DiscountManager, specific=tda593_billing_AdminDiscountManager)
gen_tda593_billing_BillManagerImpl_BillManager = Generalization(general=BillManager, specific=tda593_billing_BillManagerImpl)
gen_tda593_billing_AdminDiscountManagerImpl_billing_DiscountManagerImpl = Generalization(general=billing_DiscountManagerImpl, specific=tda593_billing_AdminDiscountManagerImpl)
gen_tda593_billing_AdminDiscountManagerImpl_billing_AdminDiscountManager = Generalization(general=billing_AdminDiscountManager, specific=tda593_billing_AdminDiscountManagerImpl)
gen_tda593_booking_Organization_LegalEntity = Generalization(general=LegalEntity, specific=tda593_booking_Organization)
gen_tda593_booking_Person_LegalEntity = Generalization(general=LegalEntity, specific=tda593_booking_Person)
gen_tda593_booking_BookingManagerImpl_BookingManager = Generalization(general=BookingManager, specific=tda593_booking_BookingManagerImpl)
gen_tda593_booking_LegalEntityManagerImpl_LegalEntityManager = Generalization(general=LegalEntityManager, specific=tda593_booking_LegalEntityManagerImpl)

# Domain Model
domain_model = DomainModel(
    name="tda593",
    types={tda593_california_DataService, tda593_facilities_AdminKeyCardManager, KeyCardManager, tda593_facilities_KeyCardManager, tda593_facilities_KeyCard, tda593_facilities_AdminRoomManager, RoomManager, tda593_facilities_RoomManager, tda593_facilities_RoomType, tda593_facilities_Room, facilities_KeyCard, tda593_facilities_RoomManagerImpl, facilities_RoomDataService, facilities_RoomTypeDataService, facilities_KeyCardManager, tda593_facilities_RoomDataService, tda593_facilities_RoomTypeDataService, tda593_facilities_KeyCardManagerImpl, facilities_KeyCardDataService, tda593_facilities_KeyCardDataService, tda593_facilities_AdminRoomManagerImpl, facilities_RoomManagerImpl, facilities_AdminRoomManager, tda593_facilities_AdminKeyCardManagerImpl, facilities_KeyCardManagerImpl, facilities_AdminKeyCardManager, tda593_billing_DiscountManager, facilities_RoomType, tda593_facilities_GuestRoom, Room, tda593_facilities_ConferenceRoom, billing_DiscountLimit, tda593_billing_DiscountLimit, booking_LegalEntity, tda593_billing_SumDiscount, Discount, tda593_billing_PercentageDiscount, tda593_billing_DiscountDataService, tda593_billing_DiscountManagerImpl, DiscountManager, billing_DiscountDataService, tda593_billing_Bill, tda593_billing_Discount, billing_Purchase, billing_Discount, billing_Bill, tda593_billing_Purchase, billing_Service, tda593_billing_Service, tda593_billing_BillManager, tda593_billing_BookingBill, Bill, booking_Booking, tda593_billing_CreditCardManager, tda593_billing_CreditCardInformation, tda593_billing_BankingManager, tda593_billing_BankingManagerImpl, BankingManager, tda593_billing_CreditCardInformationDataService, tda593_billing_CreditCardManagerImpl, CreditCardManager, billing_CreditCardInformationDataService, tda593_billing_ServiceManagerImpl, ServiceManager, billing_ServiceDataService, tda593_billing_ServiceManager, tda593_billing_ServiceDataService, tda593_billing_AdminServiceManager, tda593_billing_AdminServiceManagerImpl, billing_ServiceManagerImpl, billing_AdminServiceManager, tda593_billing_AdminDiscountManager, tda593_billing_BillManagerImpl, BillManager, billing_BillDataService, booking_BookingManager, tda593_billing_BillDataService, tda593_billing_AdminDiscountManagerImpl, billing_DiscountManagerImpl, billing_AdminDiscountManager, tda593_booking_Organization, LegalEntity, tda593_booking_Person, booking_TravelInformation, booking_RoomStay, tda593_booking_TravelInformation, tda593_booking_RoomStay, tda593_booking_Booking, tda593_booking_BookingManager, booking_StayRequest, booking_Person, facilities_Room, tda593_booking_StayRequest, tda593_booking_BookingManagerImpl, BookingManager, booking_BookingDataService, facilities_RoomManager, tda593_booking_BookingDataService, tda593_booking_LegalEntityManager, booking_LegalEntityDataService, tda593_booking_LegalEntityDataService, tda593_booking_LegalEntity, tda593_booking_LegalEntityManagerImpl, LegalEntityManager, RoomApproval, DisabilityApproval},
    associations={roomDataService3, roomTypeDataService4, keyCardManager6, keyCardDataService8, allowedKeyCards0, roomType1, discountLimit9, allowedUsers10, discountDataService11, purchases12, usedDiscounts13, customer15, subBills18, service20, booking21, creditCardInformationDataService27, serviceDataService28, legalEntity22, billDataService24, bookingManager25, roomType29, travelInformation31, responsible33, roomStay36, predecessor38, stayRequest40, registeredPersons41, room43, bookingDataService45, roomManager46, legalEntityDataService48},
    generalizations={gen_tda593_facilities_AdminRoomManager_RoomManager, gen_tda593_facilities_AdminKeyCardManager_KeyCardManager, gen_tda593_facilities_RoomManagerImpl_RoomManager, gen_tda593_facilities_KeyCardManagerImpl_KeyCardManager, gen_tda593_facilities_AdminRoomManagerImpl_facilities_RoomManagerImpl, gen_tda593_facilities_AdminRoomManagerImpl_facilities_AdminRoomManager, gen_tda593_facilities_AdminKeyCardManagerImpl_facilities_KeyCardManagerImpl, gen_tda593_facilities_AdminKeyCardManagerImpl_facilities_AdminKeyCardManager, gen_tda593_facilities_GuestRoom_Room, gen_tda593_facilities_ConferenceRoom_Room, gen_tda593_billing_SumDiscount_Discount, gen_tda593_billing_PercentageDiscount_Discount, gen_tda593_billing_DiscountManagerImpl_DiscountManager, gen_tda593_billing_BookingBill_Bill, gen_tda593_billing_BankingManagerImpl_BankingManager, gen_tda593_billing_CreditCardManagerImpl_CreditCardManager, gen_tda593_billing_ServiceManagerImpl_ServiceManager, gen_tda593_billing_AdminServiceManager_ServiceManager, gen_tda593_billing_AdminServiceManagerImpl_billing_ServiceManagerImpl, gen_tda593_billing_AdminServiceManagerImpl_billing_AdminServiceManager, gen_tda593_billing_AdminDiscountManager_DiscountManager, gen_tda593_billing_BillManagerImpl_BillManager, gen_tda593_billing_AdminDiscountManagerImpl_billing_DiscountManagerImpl, gen_tda593_billing_AdminDiscountManagerImpl_billing_AdminDiscountManager, gen_tda593_booking_Organization_LegalEntity, gen_tda593_booking_Person_LegalEntity, gen_tda593_booking_BookingManagerImpl_BookingManager, gen_tda593_booking_LegalEntityManagerImpl_LegalEntityManager},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)