from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Food:

    def __init__(self, food_Id: str, name: str, description: str, price: str, type: int, prepared: bool, served: bool, is_ordered_by1: set["Order"] = None):
        self.food_Id = food_Id
        self.name = name
        self.description = description
        self.price = price
        self.type = type
        self.prepared = prepared
        self.served = served
        self.is_ordered_by1 = is_ordered_by1 if is_ordered_by1 is not None else set()
        
        pass
    @property
    def prepared(self):
        return self.__prepared
    @prepared.setter
    def prepared(self, prepared: bool):
        self.__prepared = prepared

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def food_Id(self):
        return self.__food_Id
    @food_Id.setter
    def food_Id(self, food_Id: str):
        self.__food_Id = food_Id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def served(self):
        return self.__served
    @served.setter
    def served(self, served: bool):
        self.__served = served

    @property
    def is_ordered_by1(self):
        return self.__is_ordered_by1
    @is_ordered_by1.setter
    def is_ordered_by1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__is_ordered_by1", None)
        self.__is_ordered_by1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has0"):
                    opp_val = getattr(item, "has0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has0"):
                    opp_val = getattr(item, "has0", None)
                    
                    if opp_val is None:
                        setattr(item, "has0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Order:

    def __init__(self, order_Id: str, foodOrdered: Food, has0: set["Food"] = None, is_ordered_by2: "Table" = None):
        self.order_Id = order_Id
        self.foodOrdered = foodOrdered
        self.has0 = has0 if has0 is not None else set()
        self.is_ordered_by2 = is_ordered_by2
        
        pass
    @property
    def order_Id(self):
        return self.__order_Id
    @order_Id.setter
    def order_Id(self, order_Id: str):
        self.__order_Id = order_Id

    @property
    def foodOrdered(self):
        return self.__foodOrdered
    @foodOrdered.setter
    def foodOrdered(self, foodOrdered: Food):
        self.__foodOrdered = foodOrdered

    @property
    def has0(self):
        return self.__has0
    @has0.setter
    def has0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__has0", None)
        self.__has0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "is_ordered_by1"):
                    opp_val = getattr(item, "is_ordered_by1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "is_ordered_by1"):
                    opp_val = getattr(item, "is_ordered_by1", None)
                    
                    if opp_val is None:
                        setattr(item, "is_ordered_by1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def is_ordered_by2(self):
        return self.__is_ordered_by2
    @is_ordered_by2.setter
    def is_ordered_by2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__is_ordered_by2", None)
        self.__is_ordered_by2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has3"):
                opp_val = getattr(old_value, "has3", None)
                if opp_val == self:
                    setattr(old_value, "has3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has3"):
                opp_val = getattr(value, "has3", None)
                setattr(value, "has3", self)



class Table:

    def __init__(self, table_Id: str, numSeats: int, occupied: bool, specialRequest: str, order: str, has3: "Order" = None, reserved4: "Booking" = None):
        self.table_Id = table_Id
        self.numSeats = numSeats
        self.occupied = occupied
        self.specialRequest = specialRequest
        self.order = order
        self.has3 = has3
        self.reserved4 = reserved4
        
        pass
    @property
    def numSeats(self):
        return self.__numSeats
    @numSeats.setter
    def numSeats(self, numSeats: int):
        self.__numSeats = numSeats

    @property
    def specialRequest(self):
        return self.__specialRequest
    @specialRequest.setter
    def specialRequest(self, specialRequest: str):
        self.__specialRequest = specialRequest

    @property
    def table_Id(self):
        return self.__table_Id
    @table_Id.setter
    def table_Id(self, table_Id: str):
        self.__table_Id = table_Id

    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def occupied(self):
        return self.__occupied
    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied

    @property
    def has3(self):
        return self.__has3
    @has3.setter
    def has3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__has3", None)
        self.__has3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_ordered_by2"):
                opp_val = getattr(old_value, "is_ordered_by2", None)
                if opp_val == self:
                    setattr(old_value, "is_ordered_by2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_ordered_by2"):
                opp_val = getattr(value, "is_ordered_by2", None)
                setattr(value, "is_ordered_by2", self)

    @property
    def reserved4(self):
        return self.__reserved4
    @reserved4.setter
    def reserved4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__reserved4", None)
        self.__reserved4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_reserved_by5"):
                opp_val = getattr(old_value, "is_reserved_by5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_reserved_by5"):
                opp_val = getattr(value, "is_reserved_by5", None)
                if opp_val is None:
                    setattr(value, "is_reserved_by5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking:

    def __init__(self, booking_Id: str, type: int, name: str, contact: str, date: str, reservedTables: str, is_reserved_by5: set["Table"] = None, is_in7: "RMS" = None):
        self.booking_Id = booking_Id
        self.type = type
        self.name = name
        self.contact = contact
        self.date = date
        self.reservedTables = reservedTables
        self.is_reserved_by5 = is_reserved_by5 if is_reserved_by5 is not None else set()
        self.is_in7 = is_in7
        
        pass
    @property
    def booking_Id(self):
        return self.__booking_Id
    @booking_Id.setter
    def booking_Id(self, booking_Id: str):
        self.__booking_Id = booking_Id

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def is_in7(self):
        return self.__is_in7
    @is_in7.setter
    def is_in7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__is_in7", None)
        self.__is_in7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has6"):
                opp_val = getattr(old_value, "has6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has6"):
                opp_val = getattr(value, "has6", None)
                if opp_val is None:
                    setattr(value, "has6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def is_reserved_by5(self):
        return self.__is_reserved_by5
    @is_reserved_by5.setter
    def is_reserved_by5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__is_reserved_by5", None)
        self.__is_reserved_by5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reserved4"):
                    opp_val = getattr(item, "reserved4", None)
                    
                    if opp_val == self:
                        setattr(item, "reserved4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reserved4"):
                    opp_val = getattr(item, "reserved4", None)
                    
                    setattr(item, "reserved4", self)
                    



class Report:

    def __init__(self, orders: str, totalSales: str, profit: str, generates10: "RMS" = None):
        self.orders = orders
        self.totalSales = totalSales
        self.profit = profit
        self.generates10 = generates10
        
        pass
    @property
    def totalSales(self):
        return self.__totalSales
    @totalSales.setter
    def totalSales(self, totalSales: str):
        self.__totalSales = totalSales

    @property
    def profit(self):
        return self.__profit
    @profit.setter
    def profit(self, profit: str):
        self.__profit = profit

    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

    @property
    def generates10(self):
        return self.__generates10
    @generates10.setter
    def generates10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Report__generates10", None)
        self.__generates10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_generated_by11"):
                opp_val = getattr(old_value, "is_generated_by11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_generated_by11"):
                opp_val = getattr(value, "is_generated_by11", None)
                if opp_val is None:
                    setattr(value, "is_generated_by11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RMS:

    def __init__(self, bookings: str, has6: set["Booking"] = None, accesses9: set["Staff"] = None, is_generated_by11: set["Report"] = None):
        self.bookings = bookings
        self.has6 = has6 if has6 is not None else set()
        self.accesses9 = accesses9 if accesses9 is not None else set()
        self.is_generated_by11 = is_generated_by11 if is_generated_by11 is not None else set()
        
        pass
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def is_generated_by11(self):
        return self.__is_generated_by11
    @is_generated_by11.setter
    def is_generated_by11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RMS__is_generated_by11", None)
        self.__is_generated_by11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "generates10"):
                    opp_val = getattr(item, "generates10", None)
                    
                    if opp_val == self:
                        setattr(item, "generates10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "generates10"):
                    opp_val = getattr(item, "generates10", None)
                    
                    setattr(item, "generates10", self)
                    

    @property
    def accesses9(self):
        return self.__accesses9
    @accesses9.setter
    def accesses9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RMS__accesses9", None)
        self.__accesses9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Staff_RMS_08"):
                    opp_val = getattr(item, "Staff_RMS_08", None)
                    
                    if opp_val == self:
                        setattr(item, "Staff_RMS_08", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Staff_RMS_08"):
                    opp_val = getattr(item, "Staff_RMS_08", None)
                    
                    setattr(item, "Staff_RMS_08", self)
                    

    @property
    def has6(self):
        return self.__has6
    @has6.setter
    def has6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RMS__has6", None)
        self.__has6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "is_in7"):
                    opp_val = getattr(item, "is_in7", None)
                    
                    if opp_val == self:
                        setattr(item, "is_in7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "is_in7"):
                    opp_val = getattr(item, "is_in7", None)
                    
                    setattr(item, "is_in7", self)
                    



class Staff:

    def __init__(self, staff_Id: str, name: str, jobType: int, contact: str, Staff_RMS_08: "RMS" = None):
        self.staff_Id = staff_Id
        self.name = name
        self.jobType = jobType
        self.contact = contact
        self.Staff_RMS_08 = Staff_RMS_08
        
        pass
    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def staff_Id(self):
        return self.__staff_Id
    @staff_Id.setter
    def staff_Id(self, staff_Id: str):
        self.__staff_Id = staff_Id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jobType(self):
        return self.__jobType
    @jobType.setter
    def jobType(self, jobType: int):
        self.__jobType = jobType

    @property
    def Staff_RMS_08(self):
        return self.__Staff_RMS_08
    @Staff_RMS_08.setter
    def Staff_RMS_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__Staff_RMS_08", None)
        self.__Staff_RMS_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accesses9"):
                opp_val = getattr(old_value, "accesses9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses9"):
                opp_val = getattr(value, "accesses9", None)
                if opp_val is None:
                    setattr(value, "accesses9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Chef:

    pass


class Waiter:

    pass


class Manager:

    pass
