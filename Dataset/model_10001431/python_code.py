from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Print_Receipt(Enum):
    pass

############################################
# Definition of Classes
############################################










class bill:

    def __init__(self, tableno: int, orderid: int, menuid: str):
        self.tableno = tableno
        self.orderid = orderid
        self.menuid = menuid
        
        pass
    @property
    def orderid(self):
        return self.__orderid
    @orderid.setter
    def orderid(self, orderid: int):
        self.__orderid = orderid

    @property
    def tableno(self):
        return self.__tableno
    @tableno.setter
    def tableno(self, tableno: int):
        self.__tableno = tableno

    @property
    def menuid(self):
        return self.__menuid
    @menuid.setter
    def menuid(self, menuid: str):
        self.__menuid = menuid



class payment:

    def __init__(self, tableno: int, name: str, order1: "order" = None, customer10: "customer" = None):
        self.tableno = tableno
        self.name = name
        self.order1 = order1
        self.customer10 = customer10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tableno(self):
        return self.__tableno
    @tableno.setter
    def tableno(self, tableno: int):
        self.__tableno = tableno

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payment__order1", None)
        self.__order1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment0"):
                opp_val = getattr(old_value, "payment0", None)
                if opp_val == self:
                    setattr(old_value, "payment0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment0"):
                opp_val = getattr(value, "payment0", None)
                setattr(value, "payment0", self)

    @property
    def customer10(self):
        return self.__customer10
    @customer10.setter
    def customer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payment__customer10", None)
        self.__customer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment_customer_111"):
                opp_val = getattr(old_value, "payment_customer_111", None)
                if opp_val == self:
                    setattr(old_value, "payment_customer_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment_customer_111"):
                opp_val = getattr(value, "payment_customer_111", None)
                setattr(value, "payment_customer_111", self)



class order:

    def __init__(self, orderid: int, price: int, orderdate: str, menu5: "menu" = None, payment0: "payment" = None):
        self.orderid = orderid
        self.price = price
        self.orderdate = orderdate
        self.menu5 = menu5
        self.payment0 = payment0
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def orderid(self):
        return self.__orderid
    @orderid.setter
    def orderid(self, orderid: int):
        self.__orderid = orderid

    @property
    def orderdate(self):
        return self.__orderdate
    @orderdate.setter
    def orderdate(self, orderdate: str):
        self.__orderdate = orderdate

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__payment0", None)
        self.__payment0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order1"):
                opp_val = getattr(old_value, "order1", None)
                if opp_val == self:
                    setattr(old_value, "order1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order1"):
                opp_val = getattr(value, "order1", None)
                setattr(value, "order1", self)

    @property
    def menu5(self):
        return self.__menu5
    @menu5.setter
    def menu5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__menu5", None)
        self.__menu5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order4"):
                opp_val = getattr(old_value, "order4", None)
                if opp_val == self:
                    setattr(old_value, "order4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order4"):
                opp_val = getattr(value, "order4", None)
                setattr(value, "order4", self)



class waiter:

    def __init__(self, Staffid: int, name: str, menu6: "menu" = None, chef8: "chef" = None, staff14: "staff" = None):
        self.Staffid = Staffid
        self.name = name
        self.menu6 = menu6
        self.chef8 = chef8
        self.staff14 = staff14
        
        pass
    @property
    def Staffid(self):
        return self.__Staffid
    @Staffid.setter
    def Staffid(self, Staffid: int):
        self.__Staffid = Staffid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def menu6(self):
        return self.__menu6
    @menu6.setter
    def menu6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_waiter__menu6", None)
        self.__menu6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waiter7"):
                opp_val = getattr(old_value, "waiter7", None)
                if opp_val == self:
                    setattr(old_value, "waiter7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waiter7"):
                opp_val = getattr(value, "waiter7", None)
                setattr(value, "waiter7", self)

    @property
    def chef8(self):
        return self.__chef8
    @chef8.setter
    def chef8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_waiter__chef8", None)
        self.__chef8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waiter9"):
                opp_val = getattr(old_value, "waiter9", None)
                if opp_val == self:
                    setattr(old_value, "waiter9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waiter9"):
                opp_val = getattr(value, "waiter9", None)
                setattr(value, "waiter9", self)

    @property
    def staff14(self):
        return self.__staff14
    @staff14.setter
    def staff14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_waiter__staff14", None)
        self.__staff14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waiter15"):
                opp_val = getattr(old_value, "waiter15", None)
                if opp_val == self:
                    setattr(old_value, "waiter15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waiter15"):
                opp_val = getattr(value, "waiter15", None)
                setattr(value, "waiter15", self)



class chef:

    def __init__(self, Staffid: int, Name: str, waiter9: "waiter" = None):
        self.Staffid = Staffid
        self.Name = Name
        self.waiter9 = waiter9
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Staffid(self):
        return self.__Staffid
    @Staffid.setter
    def Staffid(self, Staffid: int):
        self.__Staffid = Staffid

    @property
    def waiter9(self):
        return self.__waiter9
    @waiter9.setter
    def waiter9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef__waiter9", None)
        self.__waiter9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chef8"):
                opp_val = getattr(old_value, "chef8", None)
                if opp_val == self:
                    setattr(old_value, "chef8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chef8"):
                opp_val = getattr(value, "chef8", None)
                setattr(value, "chef8", self)



class menu:

    def __init__(self, Menuid: str, Menuname: str, Price: int, browse_menu3: "customer" = None, order4: "order" = None, waiter7: "waiter" = None, staff12: "staff" = None):
        self.Menuid = Menuid
        self.Menuname = Menuname
        self.Price = Price
        self.browse_menu3 = browse_menu3
        self.order4 = order4
        self.waiter7 = waiter7
        self.staff12 = staff12
        
        pass
    @property
    def Menuname(self):
        return self.__Menuname
    @Menuname.setter
    def Menuname(self, Menuname: str):
        self.__Menuname = Menuname

    @property
    def Menuid(self):
        return self.__Menuid
    @Menuid.setter
    def Menuid(self, Menuid: str):
        self.__Menuid = Menuid

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def waiter7(self):
        return self.__waiter7
    @waiter7.setter
    def waiter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__waiter7", None)
        self.__waiter7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu6"):
                opp_val = getattr(old_value, "menu6", None)
                if opp_val == self:
                    setattr(old_value, "menu6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu6"):
                opp_val = getattr(value, "menu6", None)
                setattr(value, "menu6", self)

    @property
    def order4(self):
        return self.__order4
    @order4.setter
    def order4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__order4", None)
        self.__order4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu5"):
                opp_val = getattr(old_value, "menu5", None)
                if opp_val == self:
                    setattr(old_value, "menu5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu5"):
                opp_val = getattr(value, "menu5", None)
                setattr(value, "menu5", self)

    @property
    def browse_menu3(self):
        return self.__browse_menu3
    @browse_menu3.setter
    def browse_menu3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__browse_menu3", None)
        self.__browse_menu3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu2"):
                opp_val = getattr(old_value, "menu2", None)
                if opp_val == self:
                    setattr(old_value, "menu2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu2"):
                opp_val = getattr(value, "menu2", None)
                setattr(value, "menu2", self)

    @property
    def staff12(self):
        return self.__staff12
    @staff12.setter
    def staff12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__staff12", None)
        self.__staff12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu13"):
                opp_val = getattr(old_value, "menu13", None)
                if opp_val == self:
                    setattr(old_value, "menu13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu13"):
                opp_val = getattr(value, "menu13", None)
                setattr(value, "menu13", self)



class staff:

    def __init__(self, staffID: int, name: str, jobtype: str, menu13: "menu" = None, waiter15: "waiter" = None, restaurant19: "restaurant" = None):
        self.staffID = staffID
        self.name = name
        self.jobtype = jobtype
        self.menu13 = menu13
        self.waiter15 = waiter15
        self.restaurant19 = restaurant19
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jobtype(self):
        return self.__jobtype
    @jobtype.setter
    def jobtype(self, jobtype: str):
        self.__jobtype = jobtype

    @property
    def staffID(self):
        return self.__staffID
    @staffID.setter
    def staffID(self, staffID: int):
        self.__staffID = staffID

    @property
    def waiter15(self):
        return self.__waiter15
    @waiter15.setter
    def waiter15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff__waiter15", None)
        self.__waiter15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff14"):
                opp_val = getattr(old_value, "staff14", None)
                if opp_val == self:
                    setattr(old_value, "staff14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff14"):
                opp_val = getattr(value, "staff14", None)
                setattr(value, "staff14", self)

    @property
    def restaurant19(self):
        return self.__restaurant19
    @restaurant19.setter
    def restaurant19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff__restaurant19", None)
        self.__restaurant19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff18"):
                opp_val = getattr(old_value, "staff18", None)
                if opp_val == self:
                    setattr(old_value, "staff18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff18"):
                opp_val = getattr(value, "staff18", None)
                setattr(value, "staff18", self)

    @property
    def menu13(self):
        return self.__menu13
    @menu13.setter
    def menu13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff__menu13", None)
        self.__menu13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff12"):
                opp_val = getattr(old_value, "staff12", None)
                if opp_val == self:
                    setattr(old_value, "staff12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff12"):
                opp_val = getattr(value, "staff12", None)
                setattr(value, "staff12", self)



class customer:

    def __init__(self, Tableno: int, Name: str, Order: str, menu2: "menu" = None, payment_customer_111: "payment" = None, restaurant17: "restaurant" = None):
        self.Tableno = Tableno
        self.Name = Name
        self.Order = Order
        self.menu2 = menu2
        self.payment_customer_111 = payment_customer_111
        self.restaurant17 = restaurant17
        
        pass
    @property
    def Order(self):
        return self.__Order
    @Order.setter
    def Order(self, Order: str):
        self.__Order = Order

    @property
    def Tableno(self):
        return self.__Tableno
    @Tableno.setter
    def Tableno(self, Tableno: int):
        self.__Tableno = Tableno

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def restaurant17(self):
        return self.__restaurant17
    @restaurant17.setter
    def restaurant17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__restaurant17", None)
        self.__restaurant17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer16"):
                opp_val = getattr(old_value, "customer16", None)
                if opp_val == self:
                    setattr(old_value, "customer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer16"):
                opp_val = getattr(value, "customer16", None)
                setattr(value, "customer16", self)

    @property
    def payment_customer_111(self):
        return self.__payment_customer_111
    @payment_customer_111.setter
    def payment_customer_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__payment_customer_111", None)
        self.__payment_customer_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer10"):
                opp_val = getattr(old_value, "customer10", None)
                if opp_val == self:
                    setattr(old_value, "customer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer10"):
                opp_val = getattr(value, "customer10", None)
                setattr(value, "customer10", self)

    @property
    def menu2(self):
        return self.__menu2
    @menu2.setter
    def menu2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__menu2", None)
        self.__menu2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "browse_menu3"):
                opp_val = getattr(old_value, "browse_menu3", None)
                if opp_val == self:
                    setattr(old_value, "browse_menu3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "browse_menu3"):
                opp_val = getattr(value, "browse_menu3", None)
                setattr(value, "browse_menu3", self)



class restaurant:

    def __init__(self, tableid: int, Menuid: str, customer16: "customer" = None, staff18: "staff" = None):
        self.tableid = tableid
        self.Menuid = Menuid
        self.customer16 = customer16
        self.staff18 = staff18
        
        pass
    @property
    def tableid(self):
        return self.__tableid
    @tableid.setter
    def tableid(self, tableid: int):
        self.__tableid = tableid

    @property
    def Menuid(self):
        return self.__Menuid
    @Menuid.setter
    def Menuid(self, Menuid: str):
        self.__Menuid = Menuid

    @property
    def staff18(self):
        return self.__staff18
    @staff18.setter
    def staff18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restaurant__staff18", None)
        self.__staff18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restaurant19"):
                opp_val = getattr(old_value, "restaurant19", None)
                if opp_val == self:
                    setattr(old_value, "restaurant19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restaurant19"):
                opp_val = getattr(value, "restaurant19", None)
                setattr(value, "restaurant19", self)

    @property
    def customer16(self):
        return self.__customer16
    @customer16.setter
    def customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restaurant__customer16", None)
        self.__customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restaurant17"):
                opp_val = getattr(old_value, "restaurant17", None)
                if opp_val == self:
                    setattr(old_value, "restaurant17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restaurant17"):
                opp_val = getattr(value, "restaurant17", None)
                setattr(value, "restaurant17", self)

