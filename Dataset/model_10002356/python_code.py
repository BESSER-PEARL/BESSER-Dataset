from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class credit_card:

    pass


class cash:

    pass


class flights:

    def __init__(self, number: int, time: int, name: str, dest: str, depart: str, customer7: set["customer"] = None, admin9: "admin" = None):
        self.number = number
        self.time = time
        self.name = name
        self.dest = dest
        self.depart = depart
        self.customer7 = customer7 if customer7 is not None else set()
        self.admin9 = admin9
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def depart(self):
        return self.__depart
    @depart.setter
    def depart(self, depart: str):
        self.__depart = depart

    @property
    def dest(self):
        return self.__dest
    @dest.setter
    def dest(self, dest: str):
        self.__dest = dest

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flights__customer7", None)
        self.__customer7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flights6"):
                    opp_val = getattr(item, "flights6", None)
                    
                    if opp_val == self:
                        setattr(item, "flights6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flights6"):
                    opp_val = getattr(item, "flights6", None)
                    
                    setattr(item, "flights6", self)
                    

    @property
    def admin9(self):
        return self.__admin9
    @admin9.setter
    def admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flights__admin9", None)
        self.__admin9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flights8"):
                opp_val = getattr(old_value, "flights8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flights8"):
                opp_val = getattr(value, "flights8", None)
                if opp_val is None:
                    setattr(value, "flights8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class admin:

    def __init__(self, username: str, pwd: str, name_of_flight: str, type: str, seats: int, cost: int, customer5: set["customer"] = None, flights8: set["flights"] = None):
        self.username = username
        self.pwd = pwd
        self.name_of_flight = name_of_flight
        self.type = type
        self.seats = seats
        self.cost = cost
        self.customer5 = customer5 if customer5 is not None else set()
        self.flights8 = flights8 if flights8 is not None else set()
        
        pass
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name_of_flight(self):
        return self.__name_of_flight
    @name_of_flight.setter
    def name_of_flight(self, name_of_flight: str):
        self.__name_of_flight = name_of_flight

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def seats(self, seats: int):
        self.__seats = seats

    @property
    def pwd(self):
        return self.__pwd
    @pwd.setter
    def pwd(self, pwd: str):
        self.__pwd = pwd

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__customer5", None)
        self.__customer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin4"):
                    opp_val = getattr(item, "admin4", None)
                    
                    if opp_val == self:
                        setattr(item, "admin4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin4"):
                    opp_val = getattr(item, "admin4", None)
                    
                    setattr(item, "admin4", self)
                    

    @property
    def flights8(self):
        return self.__flights8
    @flights8.setter
    def flights8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__flights8", None)
        self.__flights8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    if opp_val == self:
                        setattr(item, "admin9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    setattr(item, "admin9", self)
                    



class ticket:

    def __init__(self, tiketno_: int, source: str, dest: str, custid: int, attribute: str, customer3: set["customer"] = None):
        self.tiketno_ = tiketno_
        self.source = source
        self.dest = dest
        self.custid = custid
        self.attribute = attribute
        self.customer3 = customer3 if customer3 is not None else set()
        
        pass
    @property
    def custid(self):
        return self.__custid
    @custid.setter
    def custid(self, custid: int):
        self.__custid = custid

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def tiketno_(self):
        return self.__tiketno_
    @tiketno_.setter
    def tiketno_(self, tiketno_: int):
        self.__tiketno_ = tiketno_

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def dest(self):
        return self.__dest
    @dest.setter
    def dest(self, dest: str):
        self.__dest = dest

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ticket__customer3", None)
        self.__customer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ticket2"):
                    opp_val = getattr(item, "ticket2", None)
                    
                    if opp_val == self:
                        setattr(item, "ticket2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ticket2"):
                    opp_val = getattr(item, "ticket2", None)
                    
                    setattr(item, "ticket2", self)
                    



class payement:

    def __init__(self, customer_info: str, pay_amt: int, transc_id: int, pay_date: int, paymethod: str, customer0: "customer" = None):
        self.customer_info = customer_info
        self.pay_amt = pay_amt
        self.transc_id = transc_id
        self.pay_date = pay_date
        self.paymethod = paymethod
        self.customer0 = customer0
        
        pass
    @property
    def customer_info(self):
        return self.__customer_info
    @customer_info.setter
    def customer_info(self, customer_info: str):
        self.__customer_info = customer_info

    @property
    def transc_id(self):
        return self.__transc_id
    @transc_id.setter
    def transc_id(self, transc_id: int):
        self.__transc_id = transc_id

    @property
    def paymethod(self):
        return self.__paymethod
    @paymethod.setter
    def paymethod(self, paymethod: str):
        self.__paymethod = paymethod

    @property
    def pay_amt(self):
        return self.__pay_amt
    @pay_amt.setter
    def pay_amt(self, pay_amt: int):
        self.__pay_amt = pay_amt

    @property
    def pay_date(self):
        return self.__pay_date
    @pay_date.setter
    def pay_date(self, pay_date: int):
        self.__pay_date = pay_date

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payement__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payement1"):
                opp_val = getattr(old_value, "payement1", None)
                if opp_val == self:
                    setattr(old_value, "payement1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payement1"):
                opp_val = getattr(value, "payement1", None)
                setattr(value, "payement1", self)



class customer:

    def __init__(self, name: str, address: str, age: int, source: str, payement1: "payement" = None, ticket2: "ticket" = None, admin4: "admin" = None, flights6: "flights" = None):
        self.name = name
        self.address = address
        self.age = age
        self.source = source
        self.payement1 = payement1
        self.ticket2 = ticket2
        self.admin4 = admin4
        self.flights6 = flights6
        
        pass
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def flights6(self):
        return self.__flights6
    @flights6.setter
    def flights6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__flights6", None)
        self.__flights6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                if opp_val is None:
                    setattr(value, "customer7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ticket2(self):
        return self.__ticket2
    @ticket2.setter
    def ticket2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__ticket2", None)
        self.__ticket2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                if opp_val is None:
                    setattr(value, "customer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payement1(self):
        return self.__payement1
    @payement1.setter
    def payement1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__payement1", None)
        self.__payement1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)

    @property
    def admin4(self):
        return self.__admin4
    @admin4.setter
    def admin4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__admin4", None)
        self.__admin4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                if opp_val is None:
                    setattr(value, "customer5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

