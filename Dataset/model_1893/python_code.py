from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IManagement:

    pass
class CodePack_Backend_ManagementHandler(IManagement):

    pass
class IReceptionOperations_rename_required:

    pass
class CodePack_Backend_ReceptionHandler(IReceptionOperations_rename_required):

    pass
class Backend_CodePack_BankComponent:

    pass
class IUserAccount:

    pass
class CodePack_Backend_CustomerHandler(IUserAccount):

    pass
class CodePack_Shared_ContactData:

    def __init__(self, full_name: str, e_mail: str, phone_no: int):
        self.full_name = full_name
        self.e_mail = e_mail
        self.phone_no = phone_no
        
    @property
    def e_mail(self) -> str:
        return self.__e_mail

    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail

    @property
    def phone_no(self) -> int:
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name

class CodePack_DataModels_Booking:

    def __init__(self, customer_id: int, payment_id: int, bonus_points_used: int, id: int, date_check_in: date, date_check_out: date, isCheckedIn: bool, total_price: float, contact_name: str, contact_phone: int, contact_email: str, CodePack_DataModels_Booking: "Room" = None):
        self.customer_id = customer_id
        self.payment_id = payment_id
        self.bonus_points_used = bonus_points_used
        self.id = id
        self.date_check_in = date_check_in
        self.date_check_out = date_check_out
        self.isCheckedIn = isCheckedIn
        self.total_price = total_price
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.CodePack_DataModels_Booking = CodePack_DataModels_Booking
        
    @property
    def contact_phone(self) -> int:
        return self.__contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone: int):
        self.__contact_phone = contact_phone

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date_check_out(self) -> date:
        return self.__date_check_out

    @date_check_out.setter
    def date_check_out(self, date_check_out: date):
        self.__date_check_out = date_check_out

    @property
    def date_check_in(self) -> date:
        return self.__date_check_in

    @date_check_in.setter
    def date_check_in(self, date_check_in: date):
        self.__date_check_in = date_check_in

    @property
    def customer_id(self) -> int:
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id

    @property
    def isCheckedIn(self) -> bool:
        return self.__isCheckedIn

    @isCheckedIn.setter
    def isCheckedIn(self, isCheckedIn: bool):
        self.__isCheckedIn = isCheckedIn

    @property
    def bonus_points_used(self) -> int:
        return self.__bonus_points_used

    @bonus_points_used.setter
    def bonus_points_used(self, bonus_points_used: int):
        self.__bonus_points_used = bonus_points_used

    @property
    def total_price(self) -> float:
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price

    @property
    def contact_name(self) -> str:
        return self.__contact_name

    @contact_name.setter
    def contact_name(self, contact_name: str):
        self.__contact_name = contact_name

    @property
    def payment_id(self) -> int:
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id: int):
        self.__payment_id = payment_id

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    @contact_email.setter
    def contact_email(self, contact_email: str):
        self.__contact_email = contact_email

    @property
    def CodePack_DataModels_Booking(self):
        return self.__CodePack_DataModels_Booking

    @CodePack_DataModels_Booking.setter
    def CodePack_DataModels_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_DataModels_Booking__CodePack_DataModels_Booking", None)
        self.__CodePack_DataModels_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room34"):
                opp_val = getattr(old_value, "Room34", None)
                if opp_val == self:
                    setattr(old_value, "Room34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room34"):
                opp_val = getattr(value, "Room34", None)
                setattr(value, "Room34", self)

class CodePack_DataModels_Bill:

    def __init__(self, booking_id: int, total_price: float, CodePack_DataModels_Bill: set["Room"] = None, CodePack_DataModels_Bill31: set["ExtraService"] = None):
        self.booking_id = booking_id
        self.total_price = total_price
        self.CodePack_DataModels_Bill = CodePack_DataModels_Bill if CodePack_DataModels_Bill is not None else set()
        self.CodePack_DataModels_Bill31 = CodePack_DataModels_Bill31 if CodePack_DataModels_Bill31 is not None else set()
        
    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def total_price(self) -> float:
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price

    @property
    def CodePack_DataModels_Bill(self):
        return self.__CodePack_DataModels_Bill

    @CodePack_DataModels_Bill.setter
    def CodePack_DataModels_Bill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_DataModels_Bill__CodePack_DataModels_Bill", None)
        self.__CodePack_DataModels_Bill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Room29"):
                    opp_val = getattr(item, "Room29", None)
                    
                    if opp_val == self:
                        setattr(item, "Room29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Room29"):
                    opp_val = getattr(item, "Room29", None)
                    
                    setattr(item, "Room29", self)
                    

    @property
    def CodePack_DataModels_Bill31(self):
        return self.__CodePack_DataModels_Bill31

    @CodePack_DataModels_Bill31.setter
    def CodePack_DataModels_Bill31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_DataModels_Bill__CodePack_DataModels_Bill31", None)
        self.__CodePack_DataModels_Bill31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtraService32"):
                    opp_val = getattr(item, "ExtraService32", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtraService32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtraService32"):
                    opp_val = getattr(item, "ExtraService32", None)
                    
                    setattr(item, "ExtraService32", self)
                    

class CodePack_DataModels_StaffMember:

    def __init__(self, phone_no: int, role_name: str, full_name: str, email: str, password: str, pers_no: str):
        self.phone_no = phone_no
        self.role_name = role_name
        self.full_name = full_name
        self.email = email
        self.password = password
        self.pers_no = pers_no
        
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def role_name(self) -> str:
        return self.__role_name

    @role_name.setter
    def role_name(self, role_name: str):
        self.__role_name = role_name

    @property
    def phone_no(self) -> int:
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no

    @property
    def pers_no(self) -> str:
        return self.__pers_no

    @pers_no.setter
    def pers_no(self, pers_no: str):
        self.__pers_no = pers_no

class CodePack_DataModels_StaffRole:

    def __init__(self, name: str, canManageBookings: bool, canManageRooms: bool, canManageServices: bool, canManageAccounts: bool):
        self.name = name
        self.canManageBookings = canManageBookings
        self.canManageRooms = canManageRooms
        self.canManageServices = canManageServices
        self.canManageAccounts = canManageAccounts
        
    @property
    def canManageRooms(self) -> bool:
        return self.__canManageRooms

    @canManageRooms.setter
    def canManageRooms(self, canManageRooms: bool):
        self.__canManageRooms = canManageRooms

    @property
    def canManageAccounts(self) -> bool:
        return self.__canManageAccounts

    @canManageAccounts.setter
    def canManageAccounts(self, canManageAccounts: bool):
        self.__canManageAccounts = canManageAccounts

    @property
    def canManageBookings(self) -> bool:
        return self.__canManageBookings

    @canManageBookings.setter
    def canManageBookings(self, canManageBookings: bool):
        self.__canManageBookings = canManageBookings

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def canManageServices(self) -> bool:
        return self.__canManageServices

    @canManageServices.setter
    def canManageServices(self, canManageServices: bool):
        self.__canManageServices = canManageServices

class CodePack_DataModels_ExtraService:

    def __init__(self, date_start: date, date_end: date, booking_id: int, total_price: float, type: str):
        self.date_start = date_start
        self.date_end = date_end
        self.booking_id = booking_id
        self.total_price = total_price
        self.type = type
        
    @property
    def date_start(self) -> date:
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start: date):
        self.__date_start = date_start

    @property
    def date_end(self) -> date:
        return self.__date_end

    @date_end.setter
    def date_end(self, date_end: date):
        self.__date_end = date_end

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def total_price(self) -> float:
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price

class CodePack_DataModels_Guest:

    def __init__(self, name: str, booking_id: int):
        self.name = name
        self.booking_id = booking_id
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

class CodePack_DataModels_RoomBooked:

    def __init__(self, room_number: int, booking_id: int, date_start: date, date_end: date, CodePack_DataModels_RoomBooked: "Booking" = None):
        self.room_number = room_number
        self.booking_id = booking_id
        self.date_start = date_start
        self.date_end = date_end
        self.CodePack_DataModels_RoomBooked = CodePack_DataModels_RoomBooked
        
    @property
    def room_number(self) -> int:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: int):
        self.__room_number = room_number

    @property
    def date_end(self) -> date:
        return self.__date_end

    @date_end.setter
    def date_end(self, date_end: date):
        self.__date_end = date_end

    @property
    def date_start(self) -> date:
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start: date):
        self.__date_start = date_start

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def CodePack_DataModels_RoomBooked(self):
        return self.__CodePack_DataModels_RoomBooked

    @CodePack_DataModels_RoomBooked.setter
    def CodePack_DataModels_RoomBooked(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_DataModels_RoomBooked__CodePack_DataModels_RoomBooked", None)
        self.__CodePack_DataModels_RoomBooked = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking27"):
                opp_val = getattr(old_value, "Booking27", None)
                if opp_val == self:
                    setattr(old_value, "Booking27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking27"):
                opp_val = getattr(value, "Booking27", None)
                setattr(value, "Booking27", self)

class CodePack_DataModels_PaymentData:

    def __init__(self, cc_number: str, cc_ccv: str, cc_month: int, cc_year: int, cc_first_name: str, cc_last_name: str, id: int):
        self.cc_number = cc_number
        self.cc_ccv = cc_ccv
        self.cc_month = cc_month
        self.cc_year = cc_year
        self.cc_first_name = cc_first_name
        self.cc_last_name = cc_last_name
        self.id = id
        
    @property
    def cc_first_name(self) -> str:
        return self.__cc_first_name

    @cc_first_name.setter
    def cc_first_name(self, cc_first_name: str):
        self.__cc_first_name = cc_first_name

    @property
    def cc_year(self) -> int:
        return self.__cc_year

    @cc_year.setter
    def cc_year(self, cc_year: int):
        self.__cc_year = cc_year

    @property
    def cc_number(self) -> str:
        return self.__cc_number

    @cc_number.setter
    def cc_number(self, cc_number: str):
        self.__cc_number = cc_number

    @property
    def cc_month(self) -> int:
        return self.__cc_month

    @cc_month.setter
    def cc_month(self, cc_month: int):
        self.__cc_month = cc_month

    @property
    def cc_ccv(self) -> str:
        return self.__cc_ccv

    @cc_ccv.setter
    def cc_ccv(self, cc_ccv: str):
        self.__cc_ccv = cc_ccv

    @property
    def cc_last_name(self) -> str:
        return self.__cc_last_name

    @cc_last_name.setter
    def cc_last_name(self, cc_last_name: str):
        self.__cc_last_name = cc_last_name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class CodePack_DataModels_ServiceType:

    def __init__(self, description: str, type_name: str, price: float):
        self.description = description
        self.type_name = type_name
        self.price = price
        
    @property
    def type_name(self) -> str:
        return self.__type_name

    @type_name.setter
    def type_name(self, type_name: str):
        self.__type_name = type_name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class CodePack_DataModels_Customer:

    def __init__(self, bonus_points: int, e_mail: str, password: str, date_of_birth: date, first_name: str, phone_no: int, customer_id: int, payment_id: int, last_name: str):
        self.bonus_points = bonus_points
        self.e_mail = e_mail
        self.password = password
        self.date_of_birth = date_of_birth
        self.first_name = first_name
        self.phone_no = phone_no
        self.customer_id = customer_id
        self.payment_id = payment_id
        self.last_name = last_name
        
    @property
    def bonus_points(self) -> int:
        return self.__bonus_points

    @bonus_points.setter
    def bonus_points(self, bonus_points: int):
        self.__bonus_points = bonus_points

    @property
    def e_mail(self) -> str:
        return self.__e_mail

    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail

    @property
    def customer_id(self) -> int:
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id

    @property
    def date_of_birth(self) -> date:
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def payment_id(self) -> int:
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id: int):
        self.__payment_id = payment_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phone_no(self) -> int:
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no

class CodePack_DataModels_RoomType:

    def __init__(self, description: str, max_guests: int, rate: float, typename: str):
        self.description = description
        self.max_guests = max_guests
        self.rate = rate
        self.typename = typename
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int):
        self.__max_guests = max_guests

    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

    @property
    def typename(self) -> str:
        return self.__typename

    @typename.setter
    def typename(self, typename: str):
        self.__typename = typename

class CodePack_DataModels_Room:

    def __init__(self, number: int, description: str, isAvailable: bool, room_type: str):
        self.number = number
        self.description = description
        self.isAvailable = isAvailable
        self.room_type = room_type
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def isAvailable(self) -> bool:
        return self.__isAvailable

    @isAvailable.setter
    def isAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def room_type(self) -> str:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: str):
        self.__room_type = room_type

class StaffMember:

    pass
class ServiceType:

    pass
class ExtraService:

    pass
class RoomBooked:

    pass
class PaymentData:

    pass
class RoomType:

    pass
class Customer:

    pass
class Booking:

    pass
class Room:

    pass
class StaffRole:

    pass
class CodePack_DataBank:

    pass
class Guest:

    pass
class CodePack_CheckInMachine:

    def __init__(self, CodePack_CheckInMachine: "CheckInHandler" = None):
        self.CodePack_CheckInMachine = CodePack_CheckInMachine
        
    @property
    def CodePack_CheckInMachine(self):
        return self.__CodePack_CheckInMachine

    @CodePack_CheckInMachine.setter
    def CodePack_CheckInMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_CheckInMachine__CodePack_CheckInMachine", None)
        self.__CodePack_CheckInMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CheckInHandler"):
                opp_val = getattr(old_value, "CheckInHandler", None)
                if opp_val == self:
                    setattr(old_value, "CheckInHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CheckInHandler"):
                opp_val = getattr(value, "CheckInHandler", None)
                setattr(value, "CheckInHandler", self)

    def startUI(self):
        # TODO: Implement startUI method
        pass

class CustomerHandler:

    pass
class CodePack_UserGUI:

    def __init__(self, CodePack_UserGUI: "CustomerHandler" = None):
        self.CodePack_UserGUI = CodePack_UserGUI
        
    @property
    def CodePack_UserGUI(self):
        return self.__CodePack_UserGUI

    @CodePack_UserGUI.setter
    def CodePack_UserGUI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_UserGUI__CodePack_UserGUI", None)
        self.__CodePack_UserGUI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CustomerHandler"):
                opp_val = getattr(old_value, "CustomerHandler", None)
                if opp_val == self:
                    setattr(old_value, "CustomerHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CustomerHandler"):
                opp_val = getattr(value, "CustomerHandler", None)
                setattr(value, "CustomerHandler", self)

    def startUI(self):
        # TODO: Implement startUI method
        pass

class ReceptionHandler:

    pass
class ManagementHandler:

    pass
class CodePack_StaffGUI:

    def __init__(self, CodePack_StaffGUI: "ManagementHandler" = None, CodePack_StaffGUI2: "ReceptionHandler" = None):
        self.CodePack_StaffGUI = CodePack_StaffGUI
        self.CodePack_StaffGUI2 = CodePack_StaffGUI2
        
    @property
    def CodePack_StaffGUI(self):
        return self.__CodePack_StaffGUI

    @CodePack_StaffGUI.setter
    def CodePack_StaffGUI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_StaffGUI__CodePack_StaffGUI", None)
        self.__CodePack_StaffGUI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ManagementHandler"):
                opp_val = getattr(old_value, "ManagementHandler", None)
                if opp_val == self:
                    setattr(old_value, "ManagementHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ManagementHandler"):
                opp_val = getattr(value, "ManagementHandler", None)
                setattr(value, "ManagementHandler", self)

    @property
    def CodePack_StaffGUI2(self):
        return self.__CodePack_StaffGUI2

    @CodePack_StaffGUI2.setter
    def CodePack_StaffGUI2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CodePack_StaffGUI__CodePack_StaffGUI2", None)
        self.__CodePack_StaffGUI2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReceptionHandler"):
                opp_val = getattr(old_value, "ReceptionHandler", None)
                if opp_val == self:
                    setattr(old_value, "ReceptionHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReceptionHandler"):
                opp_val = getattr(value, "ReceptionHandler", None)
                setattr(value, "ReceptionHandler", self)

    def startUI(self):
        # TODO: Implement startUI method
        pass

class ICheckIn:

    pass
class CodePack_Backend_CheckInHandler(ICheckIn):

    pass
class CheckInHandler:

    pass
class CodePack_ICheckIn(ABC):

    def __init__(self):
        
    def assignGuestToBooking(self, booking_id: int, guest_name: str) -> str:
        # TODO: Implement assignGuestToBooking method
        pass

    def validateBooking(self, booking_id: int) -> bool:
        # TODO: Implement validateBooking method
        pass

class IStaffAuthentication:

    pass
class IStaffAdmin:

    pass
class CodePack_IManagement(IStaffAdmin, IStaffAuthentication):

    def __init__(self):
        
    def addRoomType(self, name: str, max_guests: int, rate: float, description: str) -> bool:
        # TODO: Implement addRoomType method
        pass

    def getRoom(self, number: int) -> str:
        # TODO: Implement getRoom method
        pass

    def getAllRooms(self) -> str:
        # TODO: Implement getAllRooms method
        pass

    def getRoomTypes(self) -> str:
        # TODO: Implement getRoomTypes method
        pass

    def getServiceTypes(self) -> str:
        # TODO: Implement getServiceTypes method
        pass

    def removeServiceType(self, serviceType: str) -> bool:
        # TODO: Implement removeServiceType method
        pass

    def updateRoom(self, room: str) -> bool:
        # TODO: Implement updateRoom method
        pass

    def updateRoomType(self, roomType: str) -> bool:
        # TODO: Implement updateRoomType method
        pass

    def removeRoomType(self, type_name: str) -> bool:
        # TODO: Implement removeRoomType method
        pass

    def updateServiceType(self, serviceType: str) -> bool:
        # TODO: Implement updateServiceType method
        pass

    def removeRoom(self, number: int) -> bool:
        # TODO: Implement removeRoom method
        pass

    def addRoom(self, type: str, number: int, isAvailable: bool, description: str) -> bool:
        # TODO: Implement addRoom method
        pass

class CodePack_IStaffAuthentication(ABC):

    def __init__(self):
        
    def getRoleForStaff(self, pers_no: str) -> str:
        # TODO: Implement getRoleForStaff method
        pass

    def login(self, password: str, e_mail: str) -> str:
        # TODO: Implement login method
        pass

class CodePack_IStaffAdmin(ABC):

    def __init__(self):
        
    def updateStaffAccount(self, account: str) -> bool:
        # TODO: Implement updateStaffAccount method
        pass

    def removeStaffAccount(self, account: str) -> bool:
        # TODO: Implement removeStaffAccount method
        pass

    def getStaffAccount(self, pers_no: str) -> str:
        # TODO: Implement getStaffAccount method
        pass

    def registerStaffAccount(self, email: str, pers_no: str, role_name: str, name: str, phone_no: int) -> str:
        # TODO: Implement registerStaffAccount method
        pass

    def updateStaffRole(self, role: str) -> bool:
        # TODO: Implement updateStaffRole method
        pass

    def addStaffRole(self, canManageServices: bool, name: str, canManageAccounts: bool, canManageBookings: bool, canManageRooms: bool) -> str:
        # TODO: Implement addStaffRole method
        pass

    def removeStaffRole(self, role: str) -> bool:
        # TODO: Implement removeStaffRole method
        pass

    def getAllStaffAccounts(self) -> str:
        # TODO: Implement getAllStaffAccounts method
        pass

    def getStaffRoles(self) -> str:
        # TODO: Implement getStaffRoles method
        pass

class CodePack_IBookings(ABC):

    def __init__(self):
        
    def getPaymentForBooking(self, booking_id: int) -> str:
        # TODO: Implement getPaymentForBooking method
        pass

    def updateTimeForBooking(self, new_check_out: date, booking_id: int, new_check_in: date) -> bool:
        # TODO: Implement updateTimeForBooking method
        pass

    def createBooking(self, payment_data: str, services: str, rooms: str, number_of_guests: int, date_check_in: date, date_check_out: date, contact_data: str) -> str:
        # TODO: Implement createBooking method
        pass

    def sendComfimationMail(self, booking: str):
        # TODO: Implement sendComfimationMail method
        pass

    def createBookingForCustomer(self, rooms: str, bonus_points_used: int, number_of_guests: int, date_check_out: date, customer_id: int, services: str, date_check_in: date) -> str:
        # TODO: Implement createBookingForCustomer method
        pass

    def getAvailableServices(self) -> str:
        # TODO: Implement getAvailableServices method
        pass

    def getAvailableRooms(self, date_start: date, date_end: date) -> str:
        # TODO: Implement getAvailableRooms method
        pass

    def updateRoomForBooking(self, old_room: int, booking_id: int, new_room: int) -> bool:
        # TODO: Implement updateRoomForBooking method
        pass

    def cancelBooking(self, booking_id: int) -> bool:
        # TODO: Implement cancelBooking method
        pass

    def updateServiceForBooking(self, new_service: str, old_service_id: int) -> bool:
        # TODO: Implement updateServiceForBooking method
        pass

    def isRoomAvailable(self, room_number: int, date_start: date, date_end: date) -> bool:
        # TODO: Implement isRoomAvailable method
        pass

    def getBookingForId(self, booking_id: int) -> str:
        # TODO: Implement getBookingForId method
        pass

    def getBookingsForCustomer(self, customer_id: int) -> str:
        # TODO: Implement getBookingsForCustomer method
        pass

class IBookings:

    pass
class CodePack_IReceptionOperations_rename_required(IBookings, ICheckIn, IStaffAuthentication):

    def __init__(self):
        
    def isCheckedIn(self, booking_id: int) -> bool:
        # TODO: Implement isCheckedIn method
        pass

    def generateBill(self, booking_id: int) -> str:
        # TODO: Implement generateBill method
        pass

    def generateReceipt(self, bill: str) -> str:
        # TODO: Implement generateReceipt method
        pass

class CodePack_IUserAccount(IBookings):

    def __init__(self):
        
    def registerCustomer(self, last_name: str, phone_no: int, e_mail: str, password: str, first_name: str, date_of_birth: date) -> bool:
        # TODO: Implement registerCustomer method
        pass

    def updateCustomerPwd(self, customer_id: int, pwd_old: str, pwd_new: str) -> bool:
        # TODO: Implement updateCustomerPwd method
        pass

    def isEmailAvailable(self, e_mail: str) -> bool:
        # TODO: Implement isEmailAvailable method
        pass

    def updateCustomerInfo(self, customer_id: int, phone_no: str, e_mail: str) -> bool:
        # TODO: Implement updateCustomerInfo method
        pass

    def getCustomerInfo(self, customer_id: int) -> str:
        # TODO: Implement getCustomerInfo method
        pass

    def updateCustomerCC(self, cc_year: int, name_last: str, cc_number: str, cc_month: int, cc_ccv: str, name_first: str, customer_id: int) -> bool:
        # TODO: Implement updateCustomerCC method
        pass

    def login(self, password: str, e_mail: str) -> int:
        # TODO: Implement login method
        pass
