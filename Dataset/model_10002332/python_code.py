from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CustomerUI:

    pass


class StaffUI:

    pass


class Chef:

    pass


class Waiter:

    pass


class Staff:

    def __init__(self, staffId: str, name: str, type: str, Staff_StaffUI_00: set["StaffUI"] = None, reservationManagementSystem2: "ReservationManagementSystem" = None):
        self.staffId = staffId
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
    def staffId(self):
        return self.__staffId
    @staffId.setter
    def staffId(self, staffId: str):
        self.__staffId = staffId

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

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



class Food:

    def __init__(self, food_id: str, name: str, price: float, prepared: bool, served: bool, has15: "Order" = None):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.prepared = prepared
        self.served = served
        self.has15 = has15
        
        pass
    @property
    def food_id(self):
        return self.__food_id
    @food_id.setter
    def food_id(self, food_id: str):
        self.__food_id = food_id

    @property
    def served(self):
        return self.__served
    @served.setter
    def served(self, served: bool):
        self.__served = served

    @property
    def prepared(self):
        return self.__prepared
    @prepared.setter
    def prepared(self, prepared: bool):
        self.__prepared = prepared

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def has15(self):
        return self.__has15
    @has15.setter
    def has15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__has15", None)
        self.__has15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orde14"):
                opp_val = getattr(old_value, "orde14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orde14"):
                opp_val = getattr(value, "orde14", None)
                if opp_val is None:
                    setattr(value, "orde14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, order_id: str, foodList: str, table11: "Table" = None, orde14: set["Food"] = None):
        self.order_id = order_id
        self.foodList = foodList
        self.table11 = table11
        self.orde14 = orde14 if orde14 is not None else set()
        
        pass
    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def foodList(self):
        return self.__foodList
    @foodList.setter
    def foodList(self, foodList: str):
        self.__foodList = foodList

    @property
    def orde14(self):
        return self.__orde14
    @orde14.setter
    def orde14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orde14", None)
        self.__orde14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has15"):
                    opp_val = getattr(item, "has15", None)
                    
                    if opp_val == self:
                        setattr(item, "has15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has15"):
                    opp_val = getattr(item, "has15", None)
                    
                    setattr(item, "has15", self)
                    

    @property
    def table11(self):
        return self.__table11
    @table11.setter
    def table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__table11", None)
        self.__table11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has10"):
                opp_val = getattr(old_value, "has10", None)
                if opp_val == self:
                    setattr(old_value, "has10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has10"):
                opp_val = getattr(value, "has10", None)
                setattr(value, "has10", self)



class Report:

    def __init__(self, report_id: str, orders: str, reservationManagementSystem9: "ReservationManagementSystem" = None):
        self.report_id = report_id
        self.orders = orders
        self.reservationManagementSystem9 = reservationManagementSystem9
        
        pass
    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

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
        old_value = getattr(self, f"_Report__reservationManagementSystem9", None)
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

    def __init__(self, numSeats: int, table_id: str, avaliable: bool, has10: "Order" = None, Table_Booking_012: "Booking" = None):
        self.numSeats = numSeats
        self.table_id = table_id
        self.avaliable = avaliable
        self.has10 = has10
        self.Table_Booking_012 = Table_Booking_012
        
        pass
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
    def avaliable(self):
        return self.__avaliable
    @avaliable.setter
    def avaliable(self, avaliable: bool):
        self.__avaliable = avaliable

    @property
    def Table_Booking_012(self):
        return self.__Table_Booking_012
    @Table_Booking_012.setter
    def Table_Booking_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Table_Booking_012", None)
        self.__Table_Booking_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservedBy13"):
                opp_val = getattr(old_value, "reservedBy13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservedBy13"):
                opp_val = getattr(value, "reservedBy13", None)
                if opp_val is None:
                    setattr(value, "reservedBy13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has10(self):
        return self.__has10
    @has10.setter
    def has10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__has10", None)
        self.__has10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table11"):
                opp_val = getattr(old_value, "table11", None)
                if opp_val == self:
                    setattr(old_value, "table11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table11"):
                opp_val = getattr(value, "table11", None)
                setattr(value, "table11", self)



class Booking:

    def __init__(self, booking_id: int, date: date, startTime: str, endTime: str, reservedTables: str, customer_name: str, contact_no: int, email_id: str, ReservationManagementSystem_Booking_17: "ReservationManagementSystem" = None, reservedBy13: set["Table"] = None):
        self.booking_id = booking_id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.reservedTables = reservedTables
        self.customer_name = customer_name
        self.contact_no = contact_no
        self.email_id = email_id
        self.ReservationManagementSystem_Booking_17 = ReservationManagementSystem_Booking_17
        self.reservedBy13 = reservedBy13 if reservedBy13 is not None else set()
        
        pass
    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: str):
        self.__email_id = email_id

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
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

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
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

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
    def reservedBy13(self):
        return self.__reservedBy13
    @reservedBy13.setter
    def reservedBy13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__reservedBy13", None)
        self.__reservedBy13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table_Booking_012"):
                    opp_val = getattr(item, "Table_Booking_012", None)
                    
                    if opp_val == self:
                        setattr(item, "Table_Booking_012", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table_Booking_012"):
                    opp_val = getattr(item, "Table_Booking_012", None)
                    
                    setattr(item, "Table_Booking_012", self)
                    



class ReservationManagementSystem:

    def __init__(self, bookings: str, interacts3: set["Staff"] = None, interacts5: set["CustomerUI"] = None, booking6: set["Booking"] = None, generates8: set["Report"] = None):
        self.bookings = bookings
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
    def interacts5(self):
        return self.__interacts5
    @interacts5.setter
    def interacts5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__interacts5", None)
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
                    

    @property
    def interacts3(self):
        return self.__interacts3
    @interacts3.setter
    def interacts3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__interacts3", None)
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
    def generates8(self):
        return self.__generates8
    @generates8.setter
    def generates8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__generates8", None)
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
    def booking6(self):
        return self.__booking6
    @booking6.setter
    def booking6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__booking6", None)
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
                    

