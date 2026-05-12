from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, c_id: int, c_name: str, c_address: str, c_email: str, c_mobile: int):
        self.c_id = c_id
        self.c_name = c_name
        self.c_address = c_address
        self.c_email = c_email
        self.c_mobile = c_mobile
        
        pass
    @property
    def c_name(self):
        return self.__c_name
    @c_name.setter
    def c_name(self, c_name: str):
        self.__c_name = c_name

    @property
    def c_email(self):
        return self.__c_email
    @c_email.setter
    def c_email(self, c_email: str):
        self.__c_email = c_email

    @property
    def c_id(self):
        return self.__c_id
    @c_id.setter
    def c_id(self, c_id: int):
        self.__c_id = c_id

    @property
    def c_address(self):
        return self.__c_address
    @c_address.setter
    def c_address(self, c_address: str):
        self.__c_address = c_address

    @property
    def c_mobile(self):
        return self.__c_mobile
    @c_mobile.setter
    def c_mobile(self, c_mobile: int):
        self.__c_mobile = c_mobile



class Restaurants:

    def __init__(self, r_ID: int, r_name: str, r_address: str, r_contact: int, r_cuisine: str, reservedBy9: set["Table"] = None, booking12: "Booking" = None):
        self.r_ID = r_ID
        self.r_name = r_name
        self.r_address = r_address
        self.r_contact = r_contact
        self.r_cuisine = r_cuisine
        self.reservedBy9 = reservedBy9 if reservedBy9 is not None else set()
        self.booking12 = booking12
        
        pass
    @property
    def r_ID(self):
        return self.__r_ID
    @r_ID.setter
    def r_ID(self, r_ID: int):
        self.__r_ID = r_ID

    @property
    def r_address(self):
        return self.__r_address
    @r_address.setter
    def r_address(self, r_address: str):
        self.__r_address = r_address

    @property
    def r_name(self):
        return self.__r_name
    @r_name.setter
    def r_name(self, r_name: str):
        self.__r_name = r_name

    @property
    def r_cuisine(self):
        return self.__r_cuisine
    @r_cuisine.setter
    def r_cuisine(self, r_cuisine: str):
        self.__r_cuisine = r_cuisine

    @property
    def r_contact(self):
        return self.__r_contact
    @r_contact.setter
    def r_contact(self, r_contact: int):
        self.__r_contact = r_contact

    @property
    def reservedBy9(self):
        return self.__reservedBy9
    @reservedBy9.setter
    def reservedBy9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurants__reservedBy9", None)
        self.__reservedBy9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table_Booking_08"):
                    opp_val = getattr(item, "Table_Booking_08", None)
                    
                    if opp_val == self:
                        setattr(item, "Table_Booking_08", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table_Booking_08"):
                    opp_val = getattr(item, "Table_Booking_08", None)
                    
                    setattr(item, "Table_Booking_08", self)
                    

    @property
    def booking12(self):
        return self.__booking12
    @booking12.setter
    def booking12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurants__booking12", None)
        self.__booking12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restaurants13"):
                opp_val = getattr(old_value, "restaurants13", None)
                if opp_val == self:
                    setattr(old_value, "restaurants13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restaurants13"):
                opp_val = getattr(value, "restaurants13", None)
                setattr(value, "restaurants13", self)



class CustomerUI:

    pass


class Food:

    def __init__(self, food_id: str, name: str, price: float, prepared: bool, served: bool, has11: "Order" = None):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.prepared = prepared
        self.served = served
        self.has11 = has11
        
        pass
    @property
    def food_id(self):
        return self.__food_id
    @food_id.setter
    def food_id(self, food_id: str):
        self.__food_id = food_id

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def has11(self):
        return self.__has11
    @has11.setter
    def has11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__has11", None)
        self.__has11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orde10"):
                opp_val = getattr(old_value, "orde10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orde10"):
                opp_val = getattr(value, "orde10", None)
                if opp_val is None:
                    setattr(value, "orde10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, order_id: str, foodList: str, table7: "Table" = None, orde10: set["Food"] = None):
        self.order_id = order_id
        self.foodList = foodList
        self.table7 = table7
        self.orde10 = orde10 if orde10 is not None else set()
        
        pass
    @property
    def foodList(self):
        return self.__foodList
    @foodList.setter
    def foodList(self, foodList: str):
        self.__foodList = foodList

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def table7(self):
        return self.__table7
    @table7.setter
    def table7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__table7", None)
        self.__table7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has6"):
                opp_val = getattr(old_value, "has6", None)
                if opp_val == self:
                    setattr(old_value, "has6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has6"):
                opp_val = getattr(value, "has6", None)
                setattr(value, "has6", self)

    @property
    def orde10(self):
        return self.__orde10
    @orde10.setter
    def orde10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orde10", None)
        self.__orde10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has11"):
                    opp_val = getattr(item, "has11", None)
                    
                    if opp_val == self:
                        setattr(item, "has11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has11"):
                    opp_val = getattr(item, "has11", None)
                    
                    setattr(item, "has11", self)
                    



class Report:

    def __init__(self, report_id: str, orders: str, reservationManagementSystem5: "ReservationManagementSystem" = None):
        self.report_id = report_id
        self.orders = orders
        self.reservationManagementSystem5 = reservationManagementSystem5
        
        pass
    @property
    def report_id(self):
        return self.__report_id
    @report_id.setter
    def report_id(self, report_id: str):
        self.__report_id = report_id

    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

    @property
    def reservationManagementSystem5(self):
        return self.__reservationManagementSystem5
    @reservationManagementSystem5.setter
    def reservationManagementSystem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Report__reservationManagementSystem5", None)
        self.__reservationManagementSystem5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generates4"):
                opp_val = getattr(old_value, "generates4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generates4"):
                opp_val = getattr(value, "generates4", None)
                if opp_val is None:
                    setattr(value, "generates4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Table:

    def __init__(self, numSeats: int, table_id: str, avaliable: bool, has6: "Order" = None, Table_Booking_08: "Restaurants" = None):
        self.numSeats = numSeats
        self.table_id = table_id
        self.avaliable = avaliable
        self.has6 = has6
        self.Table_Booking_08 = Table_Booking_08
        
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
    def Table_Booking_08(self):
        return self.__Table_Booking_08
    @Table_Booking_08.setter
    def Table_Booking_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Table_Booking_08", None)
        self.__Table_Booking_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservedBy9"):
                opp_val = getattr(old_value, "reservedBy9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservedBy9"):
                opp_val = getattr(value, "reservedBy9", None)
                if opp_val is None:
                    setattr(value, "reservedBy9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has6(self):
        return self.__has6
    @has6.setter
    def has6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__has6", None)
        self.__has6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table7"):
                opp_val = getattr(old_value, "table7", None)
                if opp_val == self:
                    setattr(old_value, "table7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table7"):
                opp_val = getattr(value, "table7", None)
                setattr(value, "table7", self)



class Booking:

    def __init__(self, b_id: int, date: date, startTime: str, endTime: str, reservedTables: str, customer_name: str, contact_no: int, email_id: str, ReservationManagementSystem_Booking_13: "ReservationManagementSystem" = None, restaurants13: "Restaurants" = None):
        self.b_id = b_id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.reservedTables = reservedTables
        self.customer_name = customer_name
        self.contact_no = contact_no
        self.email_id = email_id
        self.ReservationManagementSystem_Booking_13 = ReservationManagementSystem_Booking_13
        self.restaurants13 = restaurants13
        
        pass
    @property
    def b_id(self):
        return self.__b_id
    @b_id.setter
    def b_id(self, b_id: int):
        self.__b_id = b_id

    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: str):
        self.__email_id = email_id

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
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

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

    @property
    def restaurants13(self):
        return self.__restaurants13
    @restaurants13.setter
    def restaurants13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__restaurants13", None)
        self.__restaurants13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking12"):
                opp_val = getattr(old_value, "booking12", None)
                if opp_val == self:
                    setattr(old_value, "booking12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking12"):
                opp_val = getattr(value, "booking12", None)
                setattr(value, "booking12", self)



class ReservationManagementSystem:

    def __init__(self, bookings: str, interacts1: set["CustomerUI"] = None, booking2: set["Booking"] = None, generates4: set["Report"] = None):
        self.bookings = bookings
        self.interacts1 = interacts1 if interacts1 is not None else set()
        self.booking2 = booking2 if booking2 is not None else set()
        self.generates4 = generates4 if generates4 is not None else set()
        
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
                    

    @property
    def generates4(self):
        return self.__generates4
    @generates4.setter
    def generates4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__generates4", None)
        self.__generates4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservationManagementSystem5"):
                    opp_val = getattr(item, "reservationManagementSystem5", None)
                    
                    if opp_val == self:
                        setattr(item, "reservationManagementSystem5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservationManagementSystem5"):
                    opp_val = getattr(item, "reservationManagementSystem5", None)
                    
                    setattr(item, "reservationManagementSystem5", self)
                    

