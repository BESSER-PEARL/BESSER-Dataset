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
model_BankComponent = Class(name="model_BankComponent")
model_HotelComponent = Class(name="model_HotelComponent")
model_Receptionist = Class(name="model_Receptionist")
model_Customers = Class(name="model_Customers")
model_Admin = Class(name="model_Admin")
model_BankInterface = Class(name="model_BankInterface", is_abstract=True)
model_CustomerInterface = Class(name="model_CustomerInterface", is_abstract=True)
model_Room = Class(name="model_Room")
model_Expense = Class(name="model_Expense")
model_Receipt = Class(name="model_Receipt")
model_Resident = Class(name="model_Resident")
model_Customer = Class(name="model_Customer")
model_ReceptionistInterface = Class(name="model_ReceptionistInterface", is_abstract=True)
model_Booking = Class(name="model_Booking")
model_AdminInterface = Class(name="model_AdminInterface", is_abstract=True)
model_User = Class(name="model_User")
model_Promotion = Class(name="model_Promotion")
model_RoomExpert = Class(name="model_RoomExpert")
model_DatabaseInterface = Class(name="model_DatabaseInterface", is_abstract=True)
model_ExpenseExpert = Class(name="model_ExpenseExpert")
model_PromotionExpert = Class(name="model_PromotionExpert")
model_BookingExpert = Class(name="model_BookingExpert")
model_UserExpert = Class(name="model_UserExpert")
model_EmailSender = Class(name="model_EmailSender")
model_Payment = Class(name="model_Payment")
model_BookingController = Class(name="model_BookingController")
CustomerInterface = Class(name="CustomerInterface")
model_ReceiptExpert = Class(name="model_ReceiptExpert")
model_ReceptionistController = Class(name="model_ReceptionistController")
BookingController = Class(name="BookingController")
ReceptionistInterface = Class(name="ReceptionistInterface")
model_MSAccessDB = Class(name="model_MSAccessDB")
DatabaseInterface = Class(name="DatabaseInterface")
model_AdminController = Class(name="model_AdminController")
AdminInterface = Class(name="AdminInterface")

# model_BankComponent class attributes and methods

# model_HotelComponent class attributes and methods

# model_Receptionist class attributes and methods

# model_Customers class attributes and methods

# model_Admin class attributes and methods

# model_BankInterface class attributes and methods

# model_CustomerInterface class attributes and methods
model_CustomerInterface_m_searchRooms: Method = Method(name="searchRooms", parameters={Parameter(name='model_dateTo', type=StringType), Parameter(name='model_numberOfRooms', type=StringType), Parameter(name='model_dateFrom', type=StringType), Parameter(name='model_numberOfGuests', type=StringType)}, type=StringType)
model_CustomerInterface_m_createCustomer: Method = Method(name="createCustomer", parameters={Parameter(name='model_ccv', type=StringType), Parameter(name='model_surname', type=StringType), Parameter(name='model_email', type=StringType), Parameter(name='model_expriningYear', type=StringType), Parameter(name='model_expiringMonth', type=StringType), Parameter(name='model_address', type=StringType), Parameter(name='model_ccNumber', type=StringType), Parameter(name='model_firstName', type=StringType)}, type=StringType)
model_CustomerInterface_m_pay: Method = Method(name="pay", parameters={Parameter(name='model_customer', type=StringType), Parameter(name='model_receipt', type=StringType)}, type=BooleanType)
model_CustomerInterface_m_validateCard: Method = Method(name="validateCard", parameters={Parameter(name='model_customer', type=StringType)}, type=BooleanType)
model_CustomerInterface_m_createBooking: Method = Method(name="createBooking", parameters={Parameter(name='model_toDate', type=StringType), Parameter(name='model_receipt', type=StringType), Parameter(name='model_roomTypes', type=StringType), Parameter(name='model_customer', type=StringType), Parameter(name='model_wishes', type=StringType), Parameter(name='model_promotion', type=StringType), Parameter(name='model_fromDate', type=StringType)}, type=BooleanType)
model_CustomerInterface.methods={model_CustomerInterface_m_createBooking, model_CustomerInterface_m_searchRooms, model_CustomerInterface_m_createCustomer, model_CustomerInterface_m_validateCard, model_CustomerInterface_m_pay}

# model_Room class attributes and methods
model_Room_number: Property = Property(name="number", type=StringType)
model_Room_description: Property = Property(name="description", type=StringType)
model_Room_clean: Property = Property(name="clean", type=StringType)
model_Room_type: Property = Property(name="type", type=StringType)
model_Room_beds: Property = Property(name="beds", type=StringType)
model_Room_status: Property = Property(name="status", type=StringType)
model_Room_m_Room: Method = Method(name="Room", parameters={Parameter(name='model_status', type=StringType), Parameter(name='model_price', type=StringType), Parameter(name='model_description', type=StringType), Parameter(name='model_beds', type=StringType), Parameter(name='model_type', type=StringType), Parameter(name='model_receipt', type=StringType), Parameter(name='model_number', type=StringType)})
model_Room.attributes={model_Room_type, model_Room_number, model_Room_status, model_Room_beds, model_Room_clean, model_Room_description}
model_Room.methods={model_Room_m_Room}

# model_Expense class attributes and methods
model_Expense_price: Property = Property(name="price", type=FloatType)
model_Expense_name: Property = Property(name="name", type=StringType)
model_Expense_description: Property = Property(name="description", type=StringType)
model_Expense_date: Property = Property(name="date", type=DateType)
model_Expense_id: Property = Property(name="id", type=IntegerType)
model_Expense_fixed: Property = Property(name="fixed", type=BooleanType)
model_Expense_receiptId: Property = Property(name="receiptId", type=IntegerType)
model_Expense_m_Expense: Method = Method(name="Expense", parameters={Parameter(name='model_price', type=StringType), Parameter(name='model_name', type=StringType), Parameter(name='model_receiptID', type=StringType), Parameter(name='model_date', type=StringType), Parameter(name='model_id', type=StringType), Parameter(name='model_isFixed', type=StringType), Parameter(name='model_description', type=StringType)})
model_Expense.attributes={model_Expense_description, model_Expense_name, model_Expense_price, model_Expense_id, model_Expense_date, model_Expense_fixed, model_Expense_receiptId}
model_Expense.methods={model_Expense_m_Expense}

# model_Receipt class attributes and methods
model_Receipt_totalCost: Property = Property(name="totalCost", type=FloatType)
model_Receipt_Date: Property = Property(name="Date", type=DateType)
model_Receipt_id: Property = Property(name="id", type=IntegerType)
model_Receipt_m_getAllExpenses: Method = Method(name="getAllExpenses", parameters={}, type=StringType)
model_Receipt_m_Receipt: Method = Method(name="Receipt", parameters={Parameter(name='model_id', type=StringType), Parameter(name='model_expenses', type=StringType), Parameter(name='model_date', type=StringType)})
model_Receipt_m_addExpense: Method = Method(name="addExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=BooleanType)
model_Receipt_m_removeExpense: Method = Method(name="removeExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=BooleanType)
model_Receipt.attributes={model_Receipt_id, model_Receipt_Date, model_Receipt_totalCost}
model_Receipt.methods={model_Receipt_m_Receipt, model_Receipt_m_removeExpense, model_Receipt_m_getAllExpenses, model_Receipt_m_addExpense}

# model_Resident class attributes and methods
model_Resident_firstName: Property = Property(name="firstName", type=StringType)
model_Resident_surname: Property = Property(name="surname", type=StringType)
model_Resident_id: Property = Property(name="id", type=StringType)
model_Resident_m_Resident: Method = Method(name="Resident", parameters={Parameter(name='model_surname', type=StringType), Parameter(name='model_firstName', type=StringType), Parameter(name='model_id', type=StringType)})
model_Resident.attributes={model_Resident_firstName, model_Resident_id, model_Resident_surname}
model_Resident.methods={model_Resident_m_Resident}

# model_Customer class attributes and methods
model_Customer_firstName: Property = Property(name="firstName", type=StringType)
model_Customer_surname: Property = Property(name="surname", type=StringType)
model_Customer_email: Property = Property(name="email", type=StringType)
model_Customer_adress: Property = Property(name="adress", type=StringType)
model_Customer_ccNumber: Property = Property(name="ccNumber", type=StringType)
model_Customer_ccv: Property = Property(name="ccv", type=StringType)
model_Customer_expiringMonth: Property = Property(name="expiringMonth", type=StringType)
model_Customer_expiringYear: Property = Property(name="expiringYear", type=StringType)
model_Customer_m_Customer: Method = Method(name="Customer", parameters={Parameter(name='model_ccNumber', type=StringType), Parameter(name='model_ccv', type=StringType), Parameter(name='model_ccExpiringYear', type=StringType), Parameter(name='model_address', type=StringType), Parameter(name='model_email', type=StringType), Parameter(name='model_ccExpiringMonth', type=StringType), Parameter(name='model_surname', type=StringType), Parameter(name='model_firstName', type=StringType)})
model_Customer.attributes={model_Customer_surname, model_Customer_expiringYear, model_Customer_ccv, model_Customer_firstName, model_Customer_ccNumber, model_Customer_email, model_Customer_expiringMonth, model_Customer_adress}
model_Customer.methods={model_Customer_m_Customer}

# model_ReceptionistInterface class attributes and methods
model_ReceptionistInterface_m_createResident: Method = Method(name="createResident", parameters={Parameter(name='model_passportNumber', type=StringType), Parameter(name='model_firstName', type=StringType), Parameter(name='model_surname', type=StringType)}, type=StringType)
model_ReceptionistInterface_m_viewUnOccupiedRooms: Method = Method(name="viewUnOccupiedRooms", parameters={Parameter(name='model_roomType', type=StringType)}, type=StringType)
model_ReceptionistInterface_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='model_rooms', type=StringType), Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_ReceptionistInterface_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_ReceptionistInterface_m_login: Method = Method(name="login", parameters={Parameter(name='model_name', type=StringType), Parameter(name='model_password', type=StringType)}, type=BooleanType)
model_ReceptionistInterface_m_removeBooking: Method = Method(name="removeBooking", parameters={Parameter(name='model_booking', type=StringType)}, type=StringType)
model_ReceptionistInterface_m_viewAllBookings: Method = Method(name="viewAllBookings", parameters={Parameter(name='model_toDate', type=StringType), Parameter(name='model_fromDate', type=StringType)}, type=StringType)
model_ReceptionistInterface_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='model_bookingNumber', type=StringType)}, type=StringType)
model_ReceptionistInterface_m_viewUnOccupiedRooms: Method = Method(name="viewUnOccupiedRooms", parameters={}, type=StringType)
model_ReceptionistInterface_m_viewAllBookings: Method = Method(name="viewAllBookings", parameters={Parameter(name='model_dateTo', type=StringType), Parameter(name='model_surname', type=StringType), Parameter(name='model_dateFrom', type=StringType)}, type=StringType)
model_ReceptionistInterface.methods={model_ReceptionistInterface_m_checkIn, model_ReceptionistInterface_m_checkOut, model_ReceptionistInterface_m_login, model_ReceptionistInterface_m_getBooking, model_ReceptionistInterface_m_removeBooking, model_ReceptionistInterface_m_createResident, model_ReceptionistInterface_m_viewAllBookings, model_ReceptionistInterface_m_viewUnOccupiedRooms, model_ReceptionistInterface_m_viewAllBookings, model_ReceptionistInterface_m_viewUnOccupiedRooms}

# model_Booking class attributes and methods
model_Booking_fromDate: Property = Property(name="fromDate", type=DateType)
model_Booking_toDate: Property = Property(name="toDate", type=DateType)
model_Booking_wishes: Property = Property(name="wishes", type=StringType)
model_Booking_promotion: Property = Property(name="promotion", type=StringType)
model_Booking_roomTypes: Property = Property(name="roomTypes", type=StringType)
model_Booking_checkedIn: Property = Property(name="checkedIn", type=StringType)
model_Booking_id: Property = Property(name="id", type=IntegerType)
model_Booking_m_Booking: Method = Method(name="Booking", parameters={Parameter(name='model_rooms', type=StringType), Parameter(name='model_roomTypes', type=StringType), Parameter(name='model_fromDate', type=StringType), Parameter(name='model_wishes', type=StringType), Parameter(name='model_receipt', type=StringType), Parameter(name='model_id', type=StringType), Parameter(name='model_customer', type=StringType), Parameter(name='model_toDate', type=StringType), Parameter(name='model_promotionCode', type=StringType)})
model_Booking.attributes={model_Booking_promotion, model_Booking_checkedIn, model_Booking_toDate, model_Booking_roomTypes, model_Booking_id, model_Booking_wishes, model_Booking_fromDate}
model_Booking.methods={model_Booking_m_Booking}

# model_AdminInterface class attributes and methods
model_AdminInterface_m_login: Method = Method(name="login", parameters={Parameter(name='model_name', type=StringType), Parameter(name='model_password', type=StringType)}, type=StringType)
model_AdminInterface_m_removePromotion: Method = Method(name="removePromotion", parameters={Parameter(name='model_promotion', type=StringType)}, type=StringType)
model_AdminInterface_m_updatePromotion: Method = Method(name="updatePromotion", parameters={Parameter(name='model_promotion', type=StringType)}, type=StringType)
model_AdminInterface_m_createExpense: Method = Method(name="createExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=StringType)
model_AdminInterface_m_removeExpense: Method = Method(name="removeExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=StringType)
model_AdminInterface_m_updateExpense: Method = Method(name="updateExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=StringType)
model_AdminInterface_m_viewRooms: Method = Method(name="viewRooms", parameters={}, type=StringType)
model_AdminInterface_m_viewPromotions: Method = Method(name="viewPromotions", parameters={}, type=StringType)
model_AdminInterface_m_viewUsers: Method = Method(name="viewUsers", parameters={}, type=StringType)
model_AdminInterface_m_viewExpenses: Method = Method(name="viewExpenses", parameters={}, type=StringType)
model_AdminInterface_m_AdminController: Method = Method(name="AdminController", parameters={Parameter(name='model_promotionExpert', type=StringType), Parameter(name='model_expenseExpert', type=StringType), Parameter(name='model_userExpert', type=StringType), Parameter(name='model_roomExpert', type=StringType)})
model_AdminInterface_m_createRoom: Method = Method(name="createRoom", parameters={Parameter(name='model_room', type=StringType)}, type=StringType)
model_AdminInterface_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='model_room', type=StringType)}, type=StringType)
model_AdminInterface_m_updateRoom: Method = Method(name="updateRoom", parameters={Parameter(name='model_room', type=StringType)}, type=BooleanType)
model_AdminInterface_m_createUser: Method = Method(name="createUser", parameters={Parameter(name='model_user', type=StringType)}, type=StringType)
model_AdminInterface_m_removeUser: Method = Method(name="removeUser", parameters={Parameter(name='model_user', type=StringType)}, type=StringType)
model_AdminInterface_m_updateUser: Method = Method(name="updateUser", parameters={Parameter(name='model_user', type=StringType)}, type=StringType)
model_AdminInterface_m_createPromotion: Method = Method(name="createPromotion", parameters={Parameter(name='model_promotion', type=StringType)}, type=StringType)
model_AdminInterface.methods={model_AdminInterface_m_login, model_AdminInterface_m_viewExpenses, model_AdminInterface_m_createUser, model_AdminInterface_m_createExpense, model_AdminInterface_m_updateUser, model_AdminInterface_m_removePromotion, model_AdminInterface_m_updateExpense, model_AdminInterface_m_removeExpense, model_AdminInterface_m_removeRoom, model_AdminInterface_m_viewUsers, model_AdminInterface_m_viewPromotions, model_AdminInterface_m_updatePromotion, model_AdminInterface_m_viewRooms, model_AdminInterface_m_AdminController, model_AdminInterface_m_updateRoom, model_AdminInterface_m_createRoom, model_AdminInterface_m_removeUser, model_AdminInterface_m_createPromotion}

# model_User class attributes and methods
model_User_firstName: Property = Property(name="firstName", type=StringType)
model_User_surname: Property = Property(name="surname", type=StringType)
model_User_password: Property = Property(name="password", type=StringType)
model_User_id: Property = Property(name="id", type=StringType)
model_User_receptionist: Property = Property(name="receptionist", type=StringType)
model_User_administrator: Property = Property(name="administrator", type=StringType)
model_User_m_User: Method = Method(name="User", parameters={Parameter(name='model_firstName', type=StringType), Parameter(name='model_receptionist', type=StringType), Parameter(name='model_id', type=StringType), Parameter(name='model_administrator', type=StringType), Parameter(name='model_surname', type=StringType), Parameter(name='model_password', type=StringType)})
model_User.attributes={model_User_administrator, model_User_firstName, model_User_surname, model_User_receptionist, model_User_password, model_User_id}
model_User.methods={model_User_m_User}

# model_Promotion class attributes and methods
model_Promotion_code: Property = Property(name="code", type=StringType)
model_Promotion_description: Property = Property(name="description", type=StringType)
model_Promotion_percentage: Property = Property(name="percentage", type=StringType)
model_Promotion_validFrom: Property = Property(name="validFrom", type=DateType)
model_Promotion_validTo: Property = Property(name="validTo", type=DateType)
model_Promotion_roomType: Property = Property(name="roomType", type=StringType)
model_Promotion_expirationDate: Property = Property(name="expirationDate", type=DateType)
model_Promotion_m_calculateDiscount: Method = Method(name="calculateDiscount", parameters={Parameter(name='model_room', type=StringType)}, type=FloatType)
model_Promotion_m_Promotion: Method = Method(name="Promotion", parameters={Parameter(name='model_description', type=StringType), Parameter(name='model_expirationDate', type=StringType), Parameter(name='model_roomType', type=StringType), Parameter(name='model_vaildTo', type=StringType), Parameter(name='model_vaildFrom', type=StringType), Parameter(name='model_code', type=StringType), Parameter(name='model_percentage', type=StringType)})
model_Promotion.attributes={model_Promotion_expirationDate, model_Promotion_description, model_Promotion_validFrom, model_Promotion_validTo, model_Promotion_roomType, model_Promotion_code, model_Promotion_percentage}
model_Promotion.methods={model_Promotion_m_Promotion, model_Promotion_m_calculateDiscount}

# model_RoomExpert class attributes and methods
model_RoomExpert_m_getAllRooms: Method = Method(name="getAllRooms", parameters={}, type=StringType)
model_RoomExpert_m_getAvailableRoomTypes: Method = Method(name="getAvailableRoomTypes", parameters={Parameter(name='model_to', type=StringType), Parameter(name='model_numberOfGuests', type=StringType), Parameter(name='model_from_', type=StringType), Parameter(name='model_numberOfRooms', type=StringType)}, type=StringType)
model_RoomExpert_m_getUnoccupiedRooms: Method = Method(name="getUnoccupiedRooms", parameters={}, type=StringType)
model_RoomExpert_m_addRoom: Method = Method(name="addRoom", parameters={Parameter(name='model_room', type=StringType)}, type=StringType)
model_RoomExpert_m_removeRoom: Method = Method(name="removeRoom", parameters={Parameter(name='model_room', type=StringType)}, type=BooleanType)
model_RoomExpert_m_updateRoom: Method = Method(name="updateRoom", parameters={Parameter(name='model_room', type=StringType)}, type=BooleanType)
model_RoomExpert_m_getRoom: Method = Method(name="getRoom", parameters={Parameter(name='model_roomNumber', type=StringType)}, type=StringType)
model_RoomExpert_m_RoomExpert: Method = Method(name="RoomExpert", parameters={Parameter(name='model_database', type=StringType)})
model_RoomExpert.methods={model_RoomExpert_m_addRoom, model_RoomExpert_m_removeRoom, model_RoomExpert_m_getUnoccupiedRooms, model_RoomExpert_m_RoomExpert, model_RoomExpert_m_getAvailableRoomTypes, model_RoomExpert_m_getRoom, model_RoomExpert_m_updateRoom, model_RoomExpert_m_getAllRooms}

# model_DatabaseInterface class attributes and methods
model_DatabaseInterface_m_query: Method = Method(name="query", parameters={Parameter(name='model_query', type=StringType)}, type=StringType)
model_DatabaseInterface_m_send: Method = Method(name="send", parameters={Parameter(name='model_query', type=StringType)}, type=BooleanType)
model_DatabaseInterface.methods={model_DatabaseInterface_m_send, model_DatabaseInterface_m_query}

# model_ExpenseExpert class attributes and methods
model_ExpenseExpert_m_getExpense: Method = Method(name="getExpense", parameters={Parameter(name='model_ID', type=StringType)}, type=StringType)
model_ExpenseExpert_m_getAllExpense: Method = Method(name="getAllExpense", parameters={}, type=StringType)
model_ExpenseExpert_m_getAllExpense: Method = Method(name="getAllExpense", parameters={Parameter(name='model_receiptID', type=StringType)}, type=StringType)
model_ExpenseExpert_m_addExpense: Method = Method(name="addExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=StringType)
model_ExpenseExpert_m_removeExpense: Method = Method(name="removeExpense", parameters={Parameter(name='model_ID', type=StringType)}, type=BooleanType)
model_ExpenseExpert_m_updateExpense: Method = Method(name="updateExpense", parameters={Parameter(name='model_expense', type=StringType)}, type=BooleanType)
model_ExpenseExpert_m_ExpenseExpert: Method = Method(name="ExpenseExpert", parameters={Parameter(name='model_database', type=StringType)})
model_ExpenseExpert.methods={model_ExpenseExpert_m_getExpense, model_ExpenseExpert_m_getAllExpense, model_ExpenseExpert_m_removeExpense, model_ExpenseExpert_m_ExpenseExpert, model_ExpenseExpert_m_getAllExpense, model_ExpenseExpert_m_addExpense, model_ExpenseExpert_m_updateExpense}

# model_PromotionExpert class attributes and methods
model_PromotionExpert_m_getPromotion: Method = Method(name="getPromotion", parameters={Parameter(name='model_promotionCode', type=StringType)}, type=StringType)
model_PromotionExpert_m_getAllPromotions: Method = Method(name="getAllPromotions", parameters={}, type=StringType)
model_PromotionExpert_m_removePromotion: Method = Method(name="removePromotion", parameters={Parameter(name='model_code', type=StringType)}, type=BooleanType)
model_PromotionExpert_m_updatePromotion: Method = Method(name="updatePromotion", parameters={Parameter(name='model_promotion', type=StringType)}, type=BooleanType)
model_PromotionExpert_m_PromotionExpert: Method = Method(name="PromotionExpert", parameters={Parameter(name='model_database', type=StringType)})
model_PromotionExpert_m_addPromotion: Method = Method(name="addPromotion", parameters={Parameter(name='model_promotion', type=StringType)}, type=StringType)
model_PromotionExpert.methods={model_PromotionExpert_m_updatePromotion, model_PromotionExpert_m_PromotionExpert, model_PromotionExpert_m_addPromotion, model_PromotionExpert_m_getPromotion, model_PromotionExpert_m_getAllPromotions, model_PromotionExpert_m_removePromotion}

# model_BookingExpert class attributes and methods
model_BookingExpert_m_getBooking: Method = Method(name="getBooking", parameters={Parameter(name='model_ID', type=StringType)}, type=StringType)
model_BookingExpert_m_getAllBookings: Method = Method(name="getAllBookings", parameters={Parameter(name='model_dateFrom', type=StringType), Parameter(name='model_dateTo', type=StringType)}, type=StringType)
model_BookingExpert_m_addBooking: Method = Method(name="addBooking", parameters={Parameter(name='model_booking', type=StringType)}, type=StringType)
model_BookingExpert_m_removeBooking: Method = Method(name="removeBooking", parameters={Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_BookingExpert_m_updateBooking: Method = Method(name="updateBooking", parameters={Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_BookingExpert_m_getAllBookings: Method = Method(name="getAllBookings", parameters={Parameter(name='model_dateFrom', type=StringType), Parameter(name='model_dateTo', type=StringType), Parameter(name='model_surname', type=StringType)}, type=StringType)
model_BookingExpert_m_BookingExpert: Method = Method(name="BookingExpert", parameters={Parameter(name='model_database', type=StringType)})
model_BookingExpert_m_checkIn: Method = Method(name="checkIn", parameters={Parameter(name='model_booking', type=StringType), Parameter(name='model_rooms', type=StringType)}, type=BooleanType)
model_BookingExpert_m_checkOut: Method = Method(name="checkOut", parameters={Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_BookingExpert.methods={model_BookingExpert_m_BookingExpert, model_BookingExpert_m_getBooking, model_BookingExpert_m_getAllBookings, model_BookingExpert_m_checkOut, model_BookingExpert_m_removeBooking, model_BookingExpert_m_getAllBookings, model_BookingExpert_m_addBooking, model_BookingExpert_m_checkIn, model_BookingExpert_m_updateBooking}

# model_UserExpert class attributes and methods
model_UserExpert_m_UserExpert: Method = Method(name="UserExpert", parameters={Parameter(name='model_database', type=StringType)})
model_UserExpert_m_getUser: Method = Method(name="getUser", parameters={Parameter(name='model_ID', type=StringType)}, type=StringType)
model_UserExpert_m_getAllUsers: Method = Method(name="getAllUsers", parameters={}, type=StringType)
model_UserExpert_m_addUser: Method = Method(name="addUser", parameters={Parameter(name='model_user', type=StringType)}, type=StringType)
model_UserExpert_m_removeUser: Method = Method(name="removeUser", parameters={Parameter(name='model_ID', type=StringType)}, type=BooleanType)
model_UserExpert_m_updateUser: Method = Method(name="updateUser", parameters={Parameter(name='model_user', type=StringType)}, type=BooleanType)
model_UserExpert_m_login: Method = Method(name="login", parameters={Parameter(name='model_name', type=StringType), Parameter(name='model_password', type=StringType)}, type=BooleanType)
model_UserExpert.methods={model_UserExpert_m_login, model_UserExpert_m_updateUser, model_UserExpert_m_removeUser, model_UserExpert_m_getUser, model_UserExpert_m_UserExpert, model_UserExpert_m_getAllUsers, model_UserExpert_m_addUser}

# model_EmailSender class attributes and methods
model_EmailSender_m_send: Method = Method(name="send", parameters={Parameter(name='model_booking', type=StringType)}, type=BooleanType)
model_EmailSender.methods={model_EmailSender_m_send}

# model_Payment class attributes and methods
model_Payment_m_makePayment: Method = Method(name="makePayment", parameters={Parameter(name='model_customer', type=StringType), Parameter(name='model_amount', type=StringType)}, type=BooleanType)
model_Payment_m_isCreditCardValid: Method = Method(name="isCreditCardValid", parameters={Parameter(name='model_customer', type=StringType)}, type=BooleanType)
model_Payment.methods={model_Payment_m_makePayment, model_Payment_m_isCreditCardValid}

# model_BookingController class attributes and methods
model_BookingController_m_BookingController: Method = Method(name="BookingController", parameters={Parameter(name='model_bookingExpert', type=StringType), Parameter(name='model_promotionExpert', type=StringType), Parameter(name='model_expenseExpert', type=StringType), Parameter(name='model_receiptExpert', type=StringType), Parameter(name='model_roomExpert', type=StringType)})
model_BookingController.methods={model_BookingController_m_BookingController}

# CustomerInterface class attributes and methods

# model_ReceiptExpert class attributes and methods
model_ReceiptExpert_m_updateReceipt: Method = Method(name="updateReceipt", parameters={Parameter(name='model_receipt', type=StringType)}, type=BooleanType)
model_ReceiptExpert_m_ReceiptExpert: Method = Method(name="ReceiptExpert", parameters={Parameter(name='model_database', type=StringType)})
model_ReceiptExpert_m_getReceipt: Method = Method(name="getReceipt", parameters={Parameter(name='model_ID', type=StringType)}, type=StringType)
model_ReceiptExpert_m_getAllReceipt: Method = Method(name="getAllReceipt", parameters={}, type=StringType)
model_ReceiptExpert_m_combine: Method = Method(name="combine", parameters={Parameter(name='model_receiptList', type=StringType)}, type=StringType)
model_ReceiptExpert_m_addReceipt: Method = Method(name="addReceipt", parameters={Parameter(name='model_receipt', type=StringType)}, type=StringType)
model_ReceiptExpert_m_removeReceipt: Method = Method(name="removeReceipt", parameters={Parameter(name='model_receipt', type=StringType)}, type=BooleanType)
model_ReceiptExpert.methods={model_ReceiptExpert_m_getReceipt, model_ReceiptExpert_m_combine, model_ReceiptExpert_m_removeReceipt, model_ReceiptExpert_m_getAllReceipt, model_ReceiptExpert_m_addReceipt, model_ReceiptExpert_m_updateReceipt, model_ReceiptExpert_m_ReceiptExpert}

# model_ReceptionistController class attributes and methods
model_ReceptionistController_m_ReceptionistController: Method = Method(name="ReceptionistController", parameters={Parameter(name='model_roomExpert', type=StringType), Parameter(name='model_bookingExpert', type=StringType), Parameter(name='model_promotionExpert', type=StringType), Parameter(name='model_receiptExpert', type=StringType), Parameter(name='model_userExpert', type=StringType), Parameter(name='model_expenseExpert', type=StringType)})
model_ReceptionistController.methods={model_ReceptionistController_m_ReceptionistController}

# BookingController class attributes and methods

# ReceptionistInterface class attributes and methods

# model_MSAccessDB class attributes and methods
model_MSAccessDB_m_openConnection: Method = Method(name="openConnection", parameters={}, type=BooleanType)
model_MSAccessDB_m_closeConnection: Method = Method(name="closeConnection", parameters={})
model_MSAccessDB.methods={model_MSAccessDB_m_closeConnection, model_MSAccessDB_m_openConnection}

# DatabaseInterface class attributes and methods

# model_AdminController class attributes and methods
model_AdminController_m_AdminController: Method = Method(name="AdminController", parameters={Parameter(name='model_roomExpert', type=StringType), Parameter(name='model_expenseExpert', type=StringType), Parameter(name='model_userExpert', type=StringType), Parameter(name='model_promotionExpert', type=StringType)})
model_AdminController.methods={model_AdminController_m_AdminController}

# AdminInterface class attributes and methods

# Relationships
price0: BinaryAssociation = BinaryAssociation(
    name="price0",
    ends={
        Property(name="model_Expense", type=model_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Room", type=model_Expense, multiplicity=Multiplicity(1, 1))
    }
)
receipt1: BinaryAssociation = BinaryAssociation(
    name="receipt1",
    ends={
        Property(name="model_Receipt", type=model_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Room2", type=model_Receipt, multiplicity=Multiplicity(1, 1))
    }
)
residents3: BinaryAssociation = BinaryAssociation(
    name="residents3",
    ends={
        Property(name="model_Resident", type=model_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Room4", type=model_Resident, multiplicity=Multiplicity(0, 9999))
    }
)
expenses5: BinaryAssociation = BinaryAssociation(
    name="expenses5",
    ends={
        Property(name="model_Expense7", type=model_Receipt, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Receipt6", type=model_Expense, multiplicity=Multiplicity(0, 9999))
    }
)
customer8: BinaryAssociation = BinaryAssociation(
    name="customer8",
    ends={
        Property(name="model_Customer", type=model_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Booking", type=model_Customer, multiplicity=Multiplicity(1, 1))
    }
)
receipt9: BinaryAssociation = BinaryAssociation(
    name="receipt9",
    ends={
        Property(name="model_Receipt11", type=model_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Booking10", type=model_Receipt, multiplicity=Multiplicity(1, 1))
    }
)
room12: BinaryAssociation = BinaryAssociation(
    name="room12",
    ends={
        Property(name="model_Room14", type=model_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Booking13", type=model_Room, multiplicity=Multiplicity(0, 9999))
    }
)
database15: BinaryAssociation = BinaryAssociation(
    name="database15",
    ends={
        Property(name="model_DatabaseInterface", type=model_RoomExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoomExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
database18: BinaryAssociation = BinaryAssociation(
    name="database18",
    ends={
        Property(name="model_DatabaseInterface19", type=model_UserExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_UserExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
database20: BinaryAssociation = BinaryAssociation(
    name="database20",
    ends={
        Property(name="model_DatabaseInterface21", type=model_PromotionExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PromotionExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
database16: BinaryAssociation = BinaryAssociation(
    name="database16",
    ends={
        Property(name="model_DatabaseInterface17", type=model_ExpenseExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExpenseExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
database24: BinaryAssociation = BinaryAssociation(
    name="database24",
    ends={
        Property(name="model_DatabaseInterface25", type=model_ReceiptExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ReceiptExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
room26: BinaryAssociation = BinaryAssociation(
    name="room26",
    ends={
        Property(name="model_RoomExpert27", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController", type=model_RoomExpert, multiplicity=Multiplicity(1, 1))
    }
)
bookingExpert28: BinaryAssociation = BinaryAssociation(
    name="bookingExpert28",
    ends={
        Property(name="model_BookingExpert30", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController29", type=model_BookingExpert, multiplicity=Multiplicity(1, 1))
    }
)
promotionExpert31: BinaryAssociation = BinaryAssociation(
    name="promotionExpert31",
    ends={
        Property(name="model_PromotionExpert33", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController32", type=model_PromotionExpert, multiplicity=Multiplicity(1, 1))
    }
)
databaseInterface34: BinaryAssociation = BinaryAssociation(
    name="databaseInterface34",
    ends={
        Property(name="model_DatabaseInterface36", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController35", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
expenseExpert37: BinaryAssociation = BinaryAssociation(
    name="expenseExpert37",
    ends={
        Property(name="model_ExpenseExpert39", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController38", type=model_ExpenseExpert, multiplicity=Multiplicity(1, 1))
    }
)
receiptExpert40: BinaryAssociation = BinaryAssociation(
    name="receiptExpert40",
    ends={
        Property(name="model_ReceiptExpert42", type=model_BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingController41", type=model_ReceiptExpert, multiplicity=Multiplicity(1, 1))
    }
)
database22: BinaryAssociation = BinaryAssociation(
    name="database22",
    ends={
        Property(name="model_DatabaseInterface23", type=model_BookingExpert, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookingExpert", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
databaseInterface51: BinaryAssociation = BinaryAssociation(
    name="databaseInterface51",
    ends={
        Property(name="model_DatabaseInterface53", type=model_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AdminController52", type=model_DatabaseInterface, multiplicity=Multiplicity(1, 1))
    }
)
roomExpert54: BinaryAssociation = BinaryAssociation(
    name="roomExpert54",
    ends={
        Property(name="model_RoomExpert56", type=model_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AdminController55", type=model_RoomExpert, multiplicity=Multiplicity(1, 1))
    }
)
userExpert57: BinaryAssociation = BinaryAssociation(
    name="userExpert57",
    ends={
        Property(name="model_UserExpert58", type=model_ReceptionistController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ReceptionistController", type=model_UserExpert, multiplicity=Multiplicity(1, 1))
    }
)
userExpert43: BinaryAssociation = BinaryAssociation(
    name="userExpert43",
    ends={
        Property(name="model_UserExpert44", type=model_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AdminController", type=model_UserExpert, multiplicity=Multiplicity(1, 1))
    }
)
expenseExpert45: BinaryAssociation = BinaryAssociation(
    name="expenseExpert45",
    ends={
        Property(name="model_ExpenseExpert47", type=model_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AdminController46", type=model_ExpenseExpert, multiplicity=Multiplicity(1, 1))
    }
)
promoExpert48: BinaryAssociation = BinaryAssociation(
    name="promoExpert48",
    ends={
        Property(name="model_PromotionExpert50", type=model_AdminController, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AdminController49", type=model_PromotionExpert, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_BookingController_CustomerInterface = Generalization(general=CustomerInterface, specific=model_BookingController)
gen_model_ReceptionistController_BookingController = Generalization(general=BookingController, specific=model_ReceptionistController)
gen_model_ReceptionistController_ReceptionistInterface = Generalization(general=ReceptionistInterface, specific=model_ReceptionistController)
gen_model_MSAccessDB_DatabaseInterface = Generalization(general=DatabaseInterface, specific=model_MSAccessDB)
gen_model_AdminController_AdminInterface = Generalization(general=AdminInterface, specific=model_AdminController)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_BankComponent, model_HotelComponent, model_Receptionist, model_Customers, model_Admin, model_BankInterface, model_CustomerInterface, model_Room, model_Expense, model_Receipt, model_Resident, model_Customer, model_ReceptionistInterface, model_Booking, model_AdminInterface, model_User, model_Promotion, model_RoomExpert, model_DatabaseInterface, model_ExpenseExpert, model_PromotionExpert, model_BookingExpert, model_UserExpert, model_EmailSender, model_Payment, model_BookingController, CustomerInterface, model_ReceiptExpert, model_ReceptionistController, BookingController, ReceptionistInterface, model_MSAccessDB, DatabaseInterface, model_AdminController, AdminInterface},
    associations={price0, receipt1, residents3, expenses5, customer8, receipt9, room12, database15, database18, database20, database16, database24, room26, bookingExpert28, promotionExpert31, databaseInterface34, expenseExpert37, receiptExpert40, database22, databaseInterface51, roomExpert54, userExpert57, userExpert43, expenseExpert45, promoExpert48},
    generalizations={gen_model_BookingController_CustomerInterface, gen_model_ReceptionistController_BookingController, gen_model_ReceptionistController_ReceptionistInterface, gen_model_MSAccessDB_DatabaseInterface, gen_model_AdminController_AdminInterface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)