from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User:

    def __init__(self, User_Name: str, Passowrd: str):
        self.User_Name = User_Name
        self.Passowrd = Passowrd
        
        pass
    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: str):
        self.__User_Name = User_Name

    @property
    def Passowrd(self):
        return self.__Passowrd
    @Passowrd.setter
    def Passowrd(self, Passowrd: str):
        self.__Passowrd = Passowrd



class Registration:

    def __init__(self, Password: str, Last_Name: str, Gender: str, First_Name: str, attribute5: str, UserName: str, Email: str, attribute: str):
        self.Password = Password
        self.Last_Name = Last_Name
        self.Gender = Gender
        self.First_Name = First_Name
        self.attribute5 = attribute5
        self.UserName = UserName
        self.Email = Email
        self.attribute = attribute
        
        pass
    @property
    def attribute5(self):
        return self.__attribute5
    @attribute5.setter
    def attribute5(self, attribute5: str):
        self.__attribute5 = attribute5

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def First_Name(self):
        return self.__First_Name
    @First_Name.setter
    def First_Name(self, First_Name: str):
        self.__First_Name = First_Name

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender



class Cart:

    def __init__(self, Product: Product, product11: set["Product"] = None):
        self.Product = Product
        self.product11 = product11 if product11 is not None else set()
        
        pass
    @property
    def Product(self):
        return self.__Product
    @Product.setter
    def Product(self, Product: Product):
        self.__Product = Product

    @property
    def product11(self):
        return self.__product11
    @product11.setter
    def product11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__product11", None)
        self.__product11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cart10"):
                    opp_val = getattr(item, "cart10", None)
                    
                    if opp_val == self:
                        setattr(item, "cart10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cart10"):
                    opp_val = getattr(item, "cart10", None)
                    
                    setattr(item, "cart10", self)
                    



class StaffUI:

    pass


class Chef:

    pass


class Product:

    def __init__(self, food_id: str, name: str, price: float, Note: str, cart10: "Cart" = None, has9: "Order" = None):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.Note = Note
        self.cart10 = cart10
        self.has9 = has9
        
        pass
    @property
    def Note(self):
        return self.__Note
    @Note.setter
    def Note(self, Note: str):
        self.__Note = Note

    @property
    def food_id(self):
        return self.__food_id
    @food_id.setter
    def food_id(self, food_id: str):
        self.__food_id = food_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def has9(self):
        return self.__has9
    @has9.setter
    def has9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__has9", None)
        self.__has9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orde8"):
                opp_val = getattr(old_value, "orde8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orde8"):
                opp_val = getattr(value, "orde8", None)
                if opp_val is None:
                    setattr(value, "orde8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cart10(self):
        return self.__cart10
    @cart10.setter
    def cart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cart10", None)
        self.__cart10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product11"):
                opp_val = getattr(old_value, "product11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product11"):
                opp_val = getattr(value, "product11", None)
                if opp_val is None:
                    setattr(value, "product11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, order_id: str, foodList: str, table5: "Table" = None, orde8: set["Product"] = None):
        self.order_id = order_id
        self.foodList = foodList
        self.table5 = table5
        self.orde8 = orde8 if orde8 is not None else set()
        
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
    def table5(self):
        return self.__table5
    @table5.setter
    def table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__table5", None)
        self.__table5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has4"):
                opp_val = getattr(old_value, "has4", None)
                if opp_val == self:
                    setattr(old_value, "has4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has4"):
                opp_val = getattr(value, "has4", None)
                setattr(value, "has4", self)

    @property
    def orde8(self):
        return self.__orde8
    @orde8.setter
    def orde8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orde8", None)
        self.__orde8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has9"):
                    opp_val = getattr(item, "has9", None)
                    
                    if opp_val == self:
                        setattr(item, "has9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has9"):
                    opp_val = getattr(item, "has9", None)
                    
                    setattr(item, "has9", self)
                    



class Invoice:

    def __init__(self, invoice_id: str, orders: str, reservationManagementSystem3: "ReservationManagementSystem" = None):
        self.invoice_id = invoice_id
        self.orders = orders
        self.reservationManagementSystem3 = reservationManagementSystem3
        
        pass
    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

    @property
    def invoice_id(self):
        return self.__invoice_id
    @invoice_id.setter
    def invoice_id(self, invoice_id: str):
        self.__invoice_id = invoice_id

    @property
    def reservationManagementSystem3(self):
        return self.__reservationManagementSystem3
    @reservationManagementSystem3.setter
    def reservationManagementSystem3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Invoice__reservationManagementSystem3", None)
        self.__reservationManagementSystem3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generates2"):
                opp_val = getattr(old_value, "generates2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generates2"):
                opp_val = getattr(value, "generates2", None)
                if opp_val is None:
                    setattr(value, "generates2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Table:

    def __init__(self, numSeats: int, table_id: str, avaliable: bool, has4: "Order" = None, Table_Booking_06: "Booking" = None):
        self.numSeats = numSeats
        self.table_id = table_id
        self.avaliable = avaliable
        self.has4 = has4
        self.Table_Booking_06 = Table_Booking_06
        
        pass
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
    def numSeats(self):
        return self.__numSeats
    @numSeats.setter
    def numSeats(self, numSeats: int):
        self.__numSeats = numSeats

    @property
    def has4(self):
        return self.__has4
    @has4.setter
    def has4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__has4", None)
        self.__has4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if opp_val == self:
                    setattr(old_value, "table5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                setattr(value, "table5", self)

    @property
    def Table_Booking_06(self):
        return self.__Table_Booking_06
    @Table_Booking_06.setter
    def Table_Booking_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__Table_Booking_06", None)
        self.__Table_Booking_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservedBy7"):
                opp_val = getattr(old_value, "reservedBy7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservedBy7"):
                opp_val = getattr(value, "reservedBy7", None)
                if opp_val is None:
                    setattr(value, "reservedBy7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking:

    def __init__(self, booking_id: int, date: date, startTime: str, endTime: str, reservedTables: str, customer_name: str, ReservationManagementSystem_Booking_11: "ReservationManagementSystem" = None, reservedBy7: set["Table"] = None):
        self.booking_id = booking_id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.reservedTables = reservedTables
        self.customer_name = customer_name
        self.ReservationManagementSystem_Booking_11 = ReservationManagementSystem_Booking_11
        self.reservedBy7 = reservedBy7 if reservedBy7 is not None else set()
        
        pass
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
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def booking_id(self):
        return self.__booking_id
    @booking_id.setter
    def booking_id(self, booking_id: int):
        self.__booking_id = booking_id

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def ReservationManagementSystem_Booking_11(self):
        return self.__ReservationManagementSystem_Booking_11
    @ReservationManagementSystem_Booking_11.setter
    def ReservationManagementSystem_Booking_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__ReservationManagementSystem_Booking_11", None)
        self.__ReservationManagementSystem_Booking_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking0"):
                opp_val = getattr(old_value, "booking0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking0"):
                opp_val = getattr(value, "booking0", None)
                if opp_val is None:
                    setattr(value, "booking0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reservedBy7(self):
        return self.__reservedBy7
    @reservedBy7.setter
    def reservedBy7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__reservedBy7", None)
        self.__reservedBy7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table_Booking_06"):
                    opp_val = getattr(item, "Table_Booking_06", None)
                    
                    if opp_val == self:
                        setattr(item, "Table_Booking_06", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table_Booking_06"):
                    opp_val = getattr(item, "Table_Booking_06", None)
                    
                    setattr(item, "Table_Booking_06", self)
                    



class ReservationManagementSystem:

    def __init__(self, bookings: str, booking0: set["Booking"] = None, generates2: set["Invoice"] = None):
        self.bookings = bookings
        self.booking0 = booking0 if booking0 is not None else set()
        self.generates2 = generates2 if generates2 is not None else set()
        
        pass
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def booking0(self):
        return self.__booking0
    @booking0.setter
    def booking0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__booking0", None)
        self.__booking0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReservationManagementSystem_Booking_11"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_11", None)
                    
                    if opp_val == self:
                        setattr(item, "ReservationManagementSystem_Booking_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReservationManagementSystem_Booking_11"):
                    opp_val = getattr(item, "ReservationManagementSystem_Booking_11", None)
                    
                    setattr(item, "ReservationManagementSystem_Booking_11", self)
                    

    @property
    def generates2(self):
        return self.__generates2
    @generates2.setter
    def generates2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservationManagementSystem__generates2", None)
        self.__generates2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservationManagementSystem3"):
                    opp_val = getattr(item, "reservationManagementSystem3", None)
                    
                    if opp_val == self:
                        setattr(item, "reservationManagementSystem3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservationManagementSystem3"):
                    opp_val = getattr(item, "reservationManagementSystem3", None)
                    
                    setattr(item, "reservationManagementSystem3", self)
                    

