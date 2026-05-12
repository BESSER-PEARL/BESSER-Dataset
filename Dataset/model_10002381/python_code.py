from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CustomerUI:

    pass


class Table:

    def __init__(self, numSeats: int, table_id: str, avaliable: bool, Table_Booking_04: "Booking" = None):
        self.numSeats = numSeats
        self.table_id = table_id
        self.avaliable = avaliable
        self.Table_Booking_04 = Table_Booking_04
        
        pass
    @property
    def avaliable(self):
        return self.__avaliable
    @avaliable.setter
    def avaliable(self, avaliable: bool):
        self.__avaliable = avaliable

    @property
    def numSeats(self):
        return self.__numSeats
    @numSeats.setter
    def numSeats(self, numSeats: int):
        self.__numSeats = numSeats

    @property
    def table_id(self):
        return self.__table_id
    @table_id.setter
    def table_id(self, table_id: str):
        self.__table_id = table_id

    @property
    def Table_Booking_04(self):
        return self.__Table_Booking_04
    @Table_Booking_04.setter
    def Table_Booking_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Table_Booking_04", None)
        self.__Table_Booking_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservedBy5"):
                opp_val = getattr(old_value, "reservedBy5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservedBy5"):
                opp_val = getattr(value, "reservedBy5", None)
                if opp_val is None:
                    setattr(value, "reservedBy5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking:

    def __init__(self, booking_id: int, date: date, startTime: str, endTime: str, reservedTables: str, customer_name: str, contact_no: int, email_id: str, ReservationManagementSystem_Booking_13: "ReservationManagementSystem" = None, reservedBy5: set["Table"] = None):
        self.booking_id = booking_id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.reservedTables = reservedTables
        self.customer_name = customer_name
        self.contact_no = contact_no
        self.email_id = email_id
        self.ReservationManagementSystem_Booking_13 = ReservationManagementSystem_Booking_13
        self.reservedBy5 = reservedBy5 if reservedBy5 is not None else set()
        
        pass
    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: str):
        self.__email_id = email_id

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def reservedBy5(self):
        return self.__reservedBy5
    @reservedBy5.setter
    def reservedBy5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__reservedBy5", None)
        self.__reservedBy5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table_Booking_04"):
                    opp_val = getattr(item, "Table_Booking_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Table_Booking_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table_Booking_04"):
                    opp_val = getattr(item, "Table_Booking_04", None)
                    
                    setattr(item, "Table_Booking_04", self)
                    

    @property
    def ReservationManagementSystem_Booking_13(self):
        return self.__ReservationManagementSystem_Booking_13
    @ReservationManagementSystem_Booking_13.setter
    def ReservationManagementSystem_Booking_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__ReservationManagementSystem_Booking_13", None)
        self.__ReservationManagementSystem_Booking_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking2"):
                opp_val = getattr(old_value, "booking2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking2"):
                opp_val = getattr(value, "booking2", None)
                if opp_val is None:
                    setattr(value, "booking2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ReservationManagementSystem:

    def __init__(self, bookings: str, interacts1: set["CustomerUI"] = None, booking2: set["Booking"] = None):
        self.bookings = bookings
        self.interacts1 = interacts1 if interacts1 is not None else set()
        self.booking2 = booking2 if booking2 is not None else set()
        
        pass
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def booking2(self):
        return self.__booking2
    @booking2.setter
    def booking2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__booking2", None)
        self.__booking2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReservationManagementSystem_Booking_13"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_13", None)
                    
                    if opp_val == self:
                        setattr(item, "ReservationManagementSystem_Booking_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReservationManagementSystem_Booking_13"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_13", None)
                    
                    setattr(item, "ReservationManagementSystem_Booking_13", self)
                    

    @property
    def interacts1(self):
        return self.__interacts1
    @interacts1.setter
    def interacts1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__interacts1", None)
        self.__interacts1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CustomerUI_ReservationManagementSystem_00"):
                    opp_val = getattr(item, "CustomerUI_ReservationManagementSystem_00", None)
                    
                    if opp_val == self:
                        setattr(item, "CustomerUI_ReservationManagementSystem_00", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CustomerUI_ReservationManagementSystem_00"):
                    opp_val = getattr(item, "CustomerUI_ReservationManagementSystem_00", None)
                    
                    setattr(item, "CustomerUI_ReservationManagementSystem_00", self)
                    

