from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
        
        pass
    @property
    def phone_no(self):
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no


    @property
    def e_mail(self):
        return self.__e_mail

    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail


    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name


class CodePack_DataModels_Booking:

    def __init__(self, id: int, date_check_in: date, date_check_out: date, isCheckedIn: bool, total_price: float, contact_name: str, contact_phone: int, contact_email: str, customer_id: int, payment_id: int, bonus_points_used: int, CodePack_DataModels_Booking: "Room" = None):
        self.id = id
        self.date_check_in = date_check_in
        self.date_check_out = date_check_out
        self.isCheckedIn = isCheckedIn
        self.total_price = total_price
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.customer_id = customer_id
        self.payment_id = payment_id
        self.bonus_points_used = bonus_points_used
        self.CodePack_DataModels_Booking = CodePack_DataModels_Booking
        
        pass
    @property
    def contact_name(self):
        return self.__contact_name

    @contact_name.setter
    def contact_name(self, contact_name: str):
        self.__contact_name = contact_name


    @property
    def isCheckedIn(self):
        return self.__isCheckedIn

    @isCheckedIn.setter
    def isCheckedIn(self, isCheckedIn: bool):
        self.__isCheckedIn = isCheckedIn


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id


    @property
    def contact_email(self):
        return self.__contact_email

    @contact_email.setter
    def contact_email(self, contact_email: str):
        self.__contact_email = contact_email


    @property
    def date_check_in(self):
        return self.__date_check_in

    @date_check_in.setter
    def date_check_in(self, date_check_in: date):
        self.__date_check_in = date_check_in


    @property
    def bonus_points_used(self):
        return self.__bonus_points_used

    @bonus_points_used.setter
    def bonus_points_used(self, bonus_points_used: int):
        self.__bonus_points_used = bonus_points_used


    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price


    @property
    def date_check_out(self):
        return self.__date_check_out

    @date_check_out.setter
    def date_check_out(self, date_check_out: date):
        self.__date_check_out = date_check_out


    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id: int):
        self.__payment_id = payment_id


    @property
    def contact_phone(self):
        return self.__contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone: int):
        self.__contact_phone = contact_phone


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

class IManagement:

    pass
class CodePack_Backend_ManagementHandler(IManagement):

    pass
class IReceptionOperations_rename_required:

    pass
class CodePack_Backend_ReceptionHandler(IReceptionOperations_rename_required):

    pass
class CodePack_DataModels_ExtraService:

    def __init__(self, date_start: date, date_end: date, booking_id: int, total_price: float, type: str):
        self.date_start = date_start
        self.date_end = date_end
        self.booking_id = booking_id
        self.total_price = total_price
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start: date):
        self.__date_start = date_start


    @property
    def booking_id(self):
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id


    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price


    @property
    def date_end(self):
        return self.__date_end

    @date_end.setter
    def date_end(self, date_end: date):
        self.__date_end = date_end


class CodePack_DataModels_ServiceType:

    def __init__(self, description: str, type_name: str, price: float):
        self.description = description
        self.type_name = type_name
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def type_name(self):
        return self.__type_name

    @type_name.setter
    def type_name(self, type_name: str):
        self.__type_name = type_name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class CodePack_DataModels_RoomBooked:

    def __init__(self, room_number: int, booking_id: int, date_start: date, date_end: date, CodePack_DataModels_RoomBooked: "Booking" = None):
        self.room_number = room_number
        self.booking_id = booking_id
        self.date_start = date_start
        self.date_end = date_end
        self.CodePack_DataModels_RoomBooked = CodePack_DataModels_RoomBooked
        
        pass
    @property
    def date_end(self):
        return self.__date_end

    @date_end.setter
    def date_end(self, date_end: date):
        self.__date_end = date_end


    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start: date):
        self.__date_start = date_start


    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: int):
        self.__room_number = room_number


    @property
    def booking_id(self):
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

class CodePack_DataModels_Bill:

    def __init__(self, booking_id: int, total_price: float, CodePack_DataModels_Bill: set["Room"] = None, CodePack_DataModels_Bill31: set["ExtraService"] = None):
        self.booking_id = booking_id
        self.total_price = total_price
        self.CodePack_DataModels_Bill = CodePack_DataModels_Bill if CodePack_DataModels_Bill is not None else set()
        self.CodePack_DataModels_Bill31 = CodePack_DataModels_Bill31 if CodePack_DataModels_Bill31 is not None else set()
        
        pass
    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float):
        self.__total_price = total_price


    @property
    def booking_id(self):
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id


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
                    

class CodePack_DataModels_Guest:

    def __init__(self, name: str, booking_id: int):
        self.name = name
        self.booking_id = booking_id
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def booking_id(self):
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id


class CodePack_DataModels_StaffMember:

    def __init__(self, full_name: str, email: str, password: str, pers_no: str, phone_no: int, role_name: str):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.pers_no = pers_no
        self.phone_no = phone_no
        self.role_name = role_name
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def pers_no(self):
        return self.__pers_no

    @pers_no.setter
    def pers_no(self, pers_no: str):
        self.__pers_no = pers_no


    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name


    @property
    def phone_no(self):
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def role_name(self):
        return self.__role_name

    @role_name.setter
    def role_name(self, role_name: str):
        self.__role_name = role_name


class CodePack_DataModels_StaffRole:

    def __init__(self, name: str, canManageBookings: bool, canManageRooms: bool, canManageServices: bool, canManageAccounts: bool):
        self.name = name
        self.canManageBookings = canManageBookings
        self.canManageRooms = canManageRooms
        self.canManageServices = canManageServices
        self.canManageAccounts = canManageAccounts
        
        pass
    @property
    def canManageAccounts(self):
        return self.__canManageAccounts

    @canManageAccounts.setter
    def canManageAccounts(self, canManageAccounts: bool):
        self.__canManageAccounts = canManageAccounts


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def canManageRooms(self):
        return self.__canManageRooms

    @canManageRooms.setter
    def canManageRooms(self, canManageRooms: bool):
        self.__canManageRooms = canManageRooms


    @property
    def canManageServices(self):
        return self.__canManageServices

    @canManageServices.setter
    def canManageServices(self, canManageServices: bool):
        self.__canManageServices = canManageServices


    @property
    def canManageBookings(self):
        return self.__canManageBookings

    @canManageBookings.setter
    def canManageBookings(self, canManageBookings: bool):
        self.__canManageBookings = canManageBookings


class StaffMember:

    pass
class StaffRole:

    pass
class Guest:

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
class CodePack_DataModels_PaymentData:

    def __init__(self, cc_number: str, cc_ccv: str, cc_month: int, cc_year: int, cc_first_name: str, cc_last_name: str, id: int):
        self.cc_number = cc_number
        self.cc_ccv = cc_ccv
        self.cc_month = cc_month
        self.cc_year = cc_year
        self.cc_first_name = cc_first_name
        self.cc_last_name = cc_last_name
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def cc_number(self):
        return self.__cc_number

    @cc_number.setter
    def cc_number(self, cc_number: str):
        self.__cc_number = cc_number


    @property
    def cc_month(self):
        return self.__cc_month

    @cc_month.setter
    def cc_month(self, cc_month: int):
        self.__cc_month = cc_month


    @property
    def cc_first_name(self):
        return self.__cc_first_name

    @cc_first_name.setter
    def cc_first_name(self, cc_first_name: str):
        self.__cc_first_name = cc_first_name


    @property
    def cc_last_name(self):
        return self.__cc_last_name

    @cc_last_name.setter
    def cc_last_name(self, cc_last_name: str):
        self.__cc_last_name = cc_last_name


    @property
    def cc_year(self):
        return self.__cc_year

    @cc_year.setter
    def cc_year(self, cc_year: int):
        self.__cc_year = cc_year


    @property
    def cc_ccv(self):
        return self.__cc_ccv

    @cc_ccv.setter
    def cc_ccv(self, cc_ccv: str):
        self.__cc_ccv = cc_ccv


class CodePack_DataModels_Customer:

    def __init__(self, password: str, date_of_birth: date, bonus_points: int, e_mail: str, first_name: str, phone_no: int, customer_id: int, payment_id: int, last_name: str):
        self.password = password
        self.date_of_birth = date_of_birth
        self.bonus_points = bonus_points
        self.e_mail = e_mail
        self.first_name = first_name
        self.phone_no = phone_no
        self.customer_id = customer_id
        self.payment_id = payment_id
        self.last_name = last_name
        
        pass
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name


    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name


    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id: int):
        self.__payment_id = payment_id


    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth


    @property
    def e_mail(self):
        return self.__e_mail

    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail


    @property
    def bonus_points(self):
        return self.__bonus_points

    @bonus_points.setter
    def bonus_points(self, bonus_points: int):
        self.__bonus_points = bonus_points


    @property
    def phone_no(self):
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, phone_no: int):
        self.__phone_no = phone_no


    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        self.__customer_id = customer_id


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


class CodePack_DataModels_RoomType:

    def __init__(self, description: str, max_guests: int, rate: float, typename: str):
        self.description = description
        self.max_guests = max_guests
        self.rate = rate
        self.typename = typename
        
        pass
    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int):
        self.__max_guests = max_guests


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate


    @property
    def typename(self):
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
        
        pass
    @property
    def isAvailable(self):
        return self.__isAvailable

    @isAvailable.setter
    def isAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable


    @property
    def room_type(self):
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: str):
        self.__room_type = room_type


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


class ICheckIn:

    pass
class CodePack_Backend_CheckInHandler(ICheckIn):

    pass
class CodePack_ICheckIn(ABC):

    def __init__(self):
        
        pass
    def validateBooking(self, CodePack_booking_id) :
        # TODO: Implement validateBooking method
        pass

    def assignGuestToBooking(self, CodePack_guest_name, CodePack_booking_id) :
        # TODO: Implement assignGuestToBooking method
        pass

class Booking:

    pass
class Room:

    pass
class CodePack_DataBank:

    pass
class CheckInHandler:

    pass
class CodePack_CheckInMachine:

    def __init__(self, CodePack_CheckInMachine: "CheckInHandler" = None):
        self.CodePack_CheckInMachine = CodePack_CheckInMachine
        
        pass
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
        
        pass
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
        
        pass
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

class CodePack_IStaffAuthentication(ABC):

    def __init__(self):
        
        pass
    def getRoleForStaff(self, CodePack_pers_no) :
        # TODO: Implement getRoleForStaff method
        pass

    def login(self, CodePack_password, CodePack_e_mail) :
        # TODO: Implement login method
        pass

class IStaffAuthentication:

    pass
class IStaffAdmin:

    pass
class CodePack_IManagement(IStaffAuthentication, IStaffAdmin):

    def __init__(self):
        
        pass
    def getServiceTypes(self) :
        # TODO: Implement getServiceTypes method
        pass

    def removeRoomType(self, CodePack_type_name) :
        # TODO: Implement removeRoomType method
        pass

    def removeServiceType(self, CodePack_serviceType) :
        # TODO: Implement removeServiceType method
        pass

    def removeRoom(self, CodePack_number) :
        # TODO: Implement removeRoom method
        pass

    def getRoom(self, CodePack_number) :
        # TODO: Implement getRoom method
        pass

    def getRoomTypes(self) :
        # TODO: Implement getRoomTypes method
        pass

    def updateServiceType(self, CodePack_serviceType) :
        # TODO: Implement updateServiceType method
        pass

    def addRoom(self, CodePack_number, CodePack_type, CodePack_description, CodePack_isAvailable) :
        # TODO: Implement addRoom method
        pass

    def getAllRooms(self) :
        # TODO: Implement getAllRooms method
        pass

    def addRoomType(self, CodePack_name, CodePack_description, CodePack_rate, CodePack_max_guests) :
        # TODO: Implement addRoomType method
        pass

    def updateRoom(self, CodePack_room) :
        # TODO: Implement updateRoom method
        pass

    def updateRoomType(self, CodePack_roomType) :
        # TODO: Implement updateRoomType method
        pass

class CodePack_IStaffAdmin(ABC):

    def __init__(self):
        
        pass
    def getStaffRoles(self) :
        # TODO: Implement getStaffRoles method
        pass

    def removeStaffRole(self, CodePack_role) :
        # TODO: Implement removeStaffRole method
        pass

    def updateStaffRole(self, CodePack_role) :
        # TODO: Implement updateStaffRole method
        pass

    def updateStaffAccount(self, CodePack_account) :
        # TODO: Implement updateStaffAccount method
        pass

    def getStaffAccount(self, CodePack_pers_no) :
        # TODO: Implement getStaffAccount method
        pass

    def removeStaffAccount(self, CodePack_account) :
        # TODO: Implement removeStaffAccount method
        pass

    def getAllStaffAccounts(self) :
        # TODO: Implement getAllStaffAccounts method
        pass

    def registerStaffAccount(self, CodePack_pers_no, CodePack_email, CodePack_phone_no, CodePack_name, CodePack_role_name) :
        # TODO: Implement registerStaffAccount method
        pass

    def addStaffRole(self, CodePack_canManageAccounts, CodePack_canManageRooms, CodePack_canManageServices, CodePack_canManageBookings, CodePack_name) :
        # TODO: Implement addStaffRole method
        pass

class IBookings:

    pass
class CodePack_IReceptionOperations_rename_required(IBookings, IStaffAuthentication, ICheckIn):

    def __init__(self):
        
        pass
    def isCheckedIn(self, CodePack_booking_id) :
        # TODO: Implement isCheckedIn method
        pass

    def generateReceipt(self, CodePack_bill) :
        # TODO: Implement generateReceipt method
        pass

    def generateBill(self, CodePack_booking_id) :
        # TODO: Implement generateBill method
        pass

class CodePack_IUserAccount(IBookings):

    def __init__(self):
        
        pass
    def updateCustomerInfo(self, CodePack_phone_no, CodePack_customer_id, CodePack_e_mail) :
        # TODO: Implement updateCustomerInfo method
        pass

    def updateCustomerPwd(self, CodePack_customer_id, CodePack_pwd_old, CodePack_pwd_new) :
        # TODO: Implement updateCustomerPwd method
        pass

    def getCustomerInfo(self, CodePack_customer_id) :
        # TODO: Implement getCustomerInfo method
        pass

    def isEmailAvailable(self, CodePack_e_mail) :
        # TODO: Implement isEmailAvailable method
        pass

    def updateCustomerCC(self, CodePack_cc_month, CodePack_name_last, CodePack_customer_id, CodePack_cc_year, CodePack_cc_ccv, CodePack_name_first, CodePack_cc_number) :
        # TODO: Implement updateCustomerCC method
        pass

    def login(self, CodePack_e_mail, CodePack_password) :
        # TODO: Implement login method
        pass

    def registerCustomer(self, CodePack_date_of_birth, CodePack_password, CodePack_phone_no, CodePack_last_name, CodePack_e_mail, CodePack_first_name) :
        # TODO: Implement registerCustomer method
        pass

class CodePack_IBookings(ABC):

    def __init__(self):
        
        pass
    def getBookingForId(self, CodePack_booking_id) :
        # TODO: Implement getBookingForId method
        pass

    def isRoomAvailable(self, CodePack_date_end, CodePack_room_number, CodePack_date_start) :
        # TODO: Implement isRoomAvailable method
        pass

    def sendComfimationMail(self, CodePack_booking):
        # TODO: Implement sendComfimationMail method
        pass

    def getAvailableServices(self) :
        # TODO: Implement getAvailableServices method
        pass

    def getAvailableRooms(self, CodePack_date_end, CodePack_date_start) :
        # TODO: Implement getAvailableRooms method
        pass

    def updateTimeForBooking(self, CodePack_booking_id, CodePack_new_check_in, CodePack_new_check_out) :
        # TODO: Implement updateTimeForBooking method
        pass

    def updateRoomForBooking(self, CodePack_booking_id, CodePack_old_room, CodePack_new_room) :
        # TODO: Implement updateRoomForBooking method
        pass

    def updateServiceForBooking(self, CodePack_old_service_id, CodePack_new_service) :
        # TODO: Implement updateServiceForBooking method
        pass

    def createBookingForCustomer(self, CodePack_date_check_out, CodePack_number_of_guests, CodePack_date_check_in, CodePack_bonus_points_used, CodePack_customer_id, CodePack_rooms, CodePack_services) :
        # TODO: Implement createBookingForCustomer method
        pass

    def createBooking(self, CodePack_number_of_guests, CodePack_payment_data, CodePack_date_check_out, CodePack_contact_data, CodePack_date_check_in, CodePack_services, CodePack_rooms) :
        # TODO: Implement createBooking method
        pass

    def getBookingsForCustomer(self, CodePack_customer_id) :
        # TODO: Implement getBookingsForCustomer method
        pass

    def cancelBooking(self, CodePack_booking_id) :
        # TODO: Implement cancelBooking method
        pass

    def getPaymentForBooking(self, CodePack_booking_id) :
        # TODO: Implement getPaymentForBooking method
        pass
