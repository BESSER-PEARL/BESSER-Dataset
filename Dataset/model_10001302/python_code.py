from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class List_reservation_:

    pass


class List_re_:

    pass


class List__:

    pass


class CustomerUI:

    pass


class Management_UI:

    pass


class Restaurant_owner:

    def __init__(self, user_id: str, email: str, username: str):
        self.user_id = user_id
        self.email = email
        self.username = username
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class Administrator:

    def __init__(self, user_id: int, email: str, user_name: str):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id



class Staff:

    def __init__(self, user_id: str, name: str, type: str, Staff_StaffUI_00: set["Management_UI"] = None, reservationManagementSystem2: "Restaurant_Reservation_System" = None):
        self.user_id = user_id
        self.name = name
        self.type = type
        self.Staff_StaffUI_00 = Staff_StaffUI_00 if Staff_StaffUI_00 is not None else set()
        self.reservationManagementSystem2 = reservationManagementSystem2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def reservationManagementSystem2(self):
        return self.__reservationManagementSystem2
    @reservationManagementSystem2.setter
    def reservationManagementSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__reservationManagementSystem2", None)
        self.__reservationManagementSystem2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interacts3"):
                opp_val = getattr(old_value, "interacts3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interacts3"):
                opp_val = getattr(value, "interacts3", None)
                if opp_val is None:
                    setattr(value, "interacts3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Staff_StaffUI_00(self):
        return self.__Staff_StaffUI_00
    @Staff_StaffUI_00.setter
    def Staff_StaffUI_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__Staff_StaffUI_00", None)
        self.__Staff_StaffUI_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accesses1"):
                    opp_val = getattr(item, "accesses1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accesses1"):
                    opp_val = getattr(item, "accesses1", None)
                    
                    if opp_val is None:
                        setattr(item, "accesses1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Reservation_status:

    def __init__(self, report_id: str, reservation: List_reservation_, reservationManagementSystem9: "Restaurant_Reservation_System" = None):
        self.report_id = report_id
        self.reservation = reservation
        self.reservationManagementSystem9 = reservationManagementSystem9
        
        pass
    @property
    def reservation(self):
        return self.__reservation
    @reservation.setter
    def reservation(self, reservation: List_reservation_):
        self.__reservation = reservation

    @property
    def report_id(self):
        return self.__report_id
    @report_id.setter
    def report_id(self, report_id: str):
        self.__report_id = report_id

    @property
    def reservationManagementSystem9(self):
        return self.__reservationManagementSystem9
    @reservationManagementSystem9.setter
    def reservationManagementSystem9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation_status__reservationManagementSystem9", None)
        self.__reservationManagementSystem9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generates8"):
                opp_val = getattr(old_value, "generates8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generates8"):
                opp_val = getattr(value, "generates8", None)
                if opp_val is None:
                    setattr(value, "generates8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Table:

    def __init__(self, quantity: int, numSeats: int, table_id: str, Table_Booking_010: "Booking" = None):
        self.quantity = quantity
        self.numSeats = numSeats
        self.table_id = table_id
        self.Table_Booking_010 = Table_Booking_010
        
        pass
    @property
    def table_id(self):
        return self.__table_id
    @table_id.setter
    def table_id(self, table_id: str):
        self.__table_id = table_id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def numSeats(self):
        return self.__numSeats
    @numSeats.setter
    def numSeats(self, numSeats: int):
        self.__numSeats = numSeats

    @property
    def Table_Booking_010(self):
        return self.__Table_Booking_010
    @Table_Booking_010.setter
    def Table_Booking_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Table_Booking_010", None)
        self.__Table_Booking_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservedBy11"):
                opp_val = getattr(old_value, "reservedBy11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservedBy11"):
                opp_val = getattr(value, "reservedBy11", None)
                if opp_val is None:
                    setattr(value, "reservedBy11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking:

    def __init__(self, booking_id: int, date: date, startTime: str, endTime: str, reservedTables: str, customer_id: str, Restaurant_id: str, person: int, ReservationManagementSystem_Booking_17: "Restaurant_Reservation_System" = None, reservedBy11: set["Table"] = None):
        self.booking_id = booking_id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.reservedTables = reservedTables
        self.customer_id = customer_id
        self.Restaurant_id = Restaurant_id
        self.person = person
        self.ReservationManagementSystem_Booking_17 = ReservationManagementSystem_Booking_17
        self.reservedBy11 = reservedBy11 if reservedBy11 is not None else set()
        
        pass
    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def person(self):
        return self.__person
    @person.setter
    def person(self, person: int):
        self.__person = person

    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, customer_id: str):
        self.__customer_id = customer_id

    @property
    def Restaurant_id(self):
        return self.__Restaurant_id
    @Restaurant_id.setter
    def Restaurant_id(self, Restaurant_id: str):
        self.__Restaurant_id = Restaurant_id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def ReservationManagementSystem_Booking_17(self):
        return self.__ReservationManagementSystem_Booking_17
    @ReservationManagementSystem_Booking_17.setter
    def ReservationManagementSystem_Booking_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__ReservationManagementSystem_Booking_17", None)
        self.__ReservationManagementSystem_Booking_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking6"):
                opp_val = getattr(old_value, "booking6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking6"):
                opp_val = getattr(value, "booking6", None)
                if opp_val is None:
                    setattr(value, "booking6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reservedBy11(self):
        return self.__reservedBy11
    @reservedBy11.setter
    def reservedBy11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__reservedBy11", None)
        self.__reservedBy11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table_Booking_010"):
                    opp_val = getattr(item, "Table_Booking_010", None)
                    
                    if opp_val == self:
                        setattr(item, "Table_Booking_010", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table_Booking_010"):
                    opp_val = getattr(item, "Table_Booking_010", None)
                    
                    setattr(item, "Table_Booking_010", self)
                    



class Restaurant_Reservation_System:

    def __init__(self, bookings: str, Menu: str, interacts3: set["Staff"] = None, interacts5: set["CustomerUI"] = None, booking6: set["Booking"] = None, generates8: set["Reservation_status"] = None):
        self.bookings = bookings
        self.Menu = Menu
        self.interacts3 = interacts3 if interacts3 is not None else set()
        self.interacts5 = interacts5 if interacts5 is not None else set()
        self.booking6 = booking6 if booking6 is not None else set()
        self.generates8 = generates8 if generates8 is not None else set()
        
        pass
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def Menu(self):
        return self.__Menu
    @Menu.setter
    def Menu(self, Menu: str):
        self.__Menu = Menu

    @property
    def generates8(self):
        return self.__generates8
    @generates8.setter
    def generates8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant_Reservation_System__generates8", None)
        self.__generates8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservationManagementSystem9"):
                    opp_val = getattr(item, "reservationManagementSystem9", None)
                    
                    if opp_val == self:
                        setattr(item, "reservationManagementSystem9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservationManagementSystem9"):
                    opp_val = getattr(item, "reservationManagementSystem9", None)
                    
                    setattr(item, "reservationManagementSystem9", self)
                    

    @property
    def interacts3(self):
        return self.__interacts3
    @interacts3.setter
    def interacts3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant_Reservation_System__interacts3", None)
        self.__interacts3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservationManagementSystem2"):
                    opp_val = getattr(item, "reservationManagementSystem2", None)
                    
                    if opp_val == self:
                        setattr(item, "reservationManagementSystem2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservationManagementSystem2"):
                    opp_val = getattr(item, "reservationManagementSystem2", None)
                    
                    setattr(item, "reservationManagementSystem2", self)
                    

    @property
    def booking6(self):
        return self.__booking6
    @booking6.setter
    def booking6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant_Reservation_System__booking6", None)
        self.__booking6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReservationManagementSystem_Booking_17"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_17", None)
                    
                    if opp_val == self:
                        setattr(item, "ReservationManagementSystem_Booking_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReservationManagementSystem_Booking_17"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_17", None)
                    
                    setattr(item, "ReservationManagementSystem_Booking_17", self)
                    

    @property
    def interacts5(self):
        return self.__interacts5
    @interacts5.setter
    def interacts5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant_Reservation_System__interacts5", None)
        self.__interacts5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CustomerUI_ReservationManagementSystem_04"):
                    opp_val = getattr(item, "CustomerUI_ReservationManagementSystem_04", None)
                    
                    if opp_val == self:
                        setattr(item, "CustomerUI_ReservationManagementSystem_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CustomerUI_ReservationManagementSystem_04"):
                    opp_val = getattr(item, "CustomerUI_ReservationManagementSystem_04", None)
                    
                    setattr(item, "CustomerUI_ReservationManagementSystem_04", self)
                    

