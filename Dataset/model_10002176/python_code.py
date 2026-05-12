from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Staff:

    def __init__(self, staffid: Class, name: Class, Staff_Order_management_System_00: "Order_management_System" = None):
        self.staffid = staffid
        self.name = name
        self.Staff_Order_management_System_00 = Staff_Order_management_System_00
        
        pass
    @property
    def staffid(self):
        return self.__staffid
    @staffid.setter
    def staffid(self, staffid: Class):
        self.__staffid = staffid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: Class):
        self.__name = name

    @property
    def Staff_Order_management_System_00(self):
        return self.__Staff_Order_management_System_00
    @Staff_Order_management_System_00.setter
    def Staff_Order_management_System_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__Staff_Order_management_System_00", None)
        self.__Staff_Order_management_System_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff1"):
                opp_val = getattr(old_value, "staff1", None)
                if opp_val == self:
                    setattr(old_value, "staff1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff1"):
                opp_val = getattr(value, "staff1", None)
                setattr(value, "staff1", self)



class Foods:

    def __init__(self, Foodname: Class, Catogory: Class, price: Class, Ready: bool, order7: "Order" = None):
        self.Foodname = Foodname
        self.Catogory = Catogory
        self.price = price
        self.Ready = Ready
        self.order7 = order7
        
        pass
    @property
    def Catogory(self):
        return self.__Catogory
    @Catogory.setter
    def Catogory(self, Catogory: Class):
        self.__Catogory = Catogory

    @property
    def Foodname(self):
        return self.__Foodname
    @Foodname.setter
    def Foodname(self, Foodname: Class):
        self.__Foodname = Foodname

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: Class):
        self.__price = price

    @property
    def Ready(self):
        return self.__Ready
    @Ready.setter
    def Ready(self, Ready: bool):
        self.__Ready = Ready

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Foods__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foods6"):
                opp_val = getattr(old_value, "foods6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foods6"):
                opp_val = getattr(value, "foods6", None)
                if opp_val is None:
                    setattr(value, "foods6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Reservation:

    def __init__(self, seats: Class, table: Class, order5: set["Order"] = None):
        self.seats = seats
        self.table = table
        self.order5 = order5 if order5 is not None else set()
        
        pass
    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def seats(self, seats: Class):
        self.__seats = seats

    @property
    def table(self):
        return self.__table
    @table.setter
    def table(self, table: Class):
        self.__table = table

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation__order5", None)
        self.__order5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservation4"):
                    opp_val = getattr(item, "reservation4", None)
                    
                    if opp_val == self:
                        setattr(item, "reservation4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservation4"):
                    opp_val = getattr(item, "reservation4", None)
                    
                    setattr(item, "reservation4", self)
                    



class Order:

    def __init__(self, Orderlist: Class, Amount: Class, customername: Class, customer_address: Class, customerphone: Class, customer_email: Class, Order_management_System_Order_13: "Order_management_System" = None, reservation4: "Reservation" = None, foods6: set["Foods"] = None):
        self.Orderlist = Orderlist
        self.Amount = Amount
        self.customername = customername
        self.customer_address = customer_address
        self.customerphone = customerphone
        self.customer_email = customer_email
        self.Order_management_System_Order_13 = Order_management_System_Order_13
        self.reservation4 = reservation4
        self.foods6 = foods6 if foods6 is not None else set()
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: Class):
        self.__Amount = Amount

    @property
    def Orderlist(self):
        return self.__Orderlist
    @Orderlist.setter
    def Orderlist(self, Orderlist: Class):
        self.__Orderlist = Orderlist

    @property
    def customername(self):
        return self.__customername
    @customername.setter
    def customername(self, customername: Class):
        self.__customername = customername

    @property
    def customerphone(self):
        return self.__customerphone
    @customerphone.setter
    def customerphone(self, customerphone: Class):
        self.__customerphone = customerphone

    @property
    def customer_email(self):
        return self.__customer_email
    @customer_email.setter
    def customer_email(self, customer_email: Class):
        self.__customer_email = customer_email

    @property
    def customer_address(self):
        return self.__customer_address
    @customer_address.setter
    def customer_address(self, customer_address: Class):
        self.__customer_address = customer_address

    @property
    def reservation4(self):
        return self.__reservation4
    @reservation4.setter
    def reservation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__reservation4", None)
        self.__reservation4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                if opp_val is None:
                    setattr(value, "order5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Order_management_System_Order_13(self):
        return self.__Order_management_System_Order_13
    @Order_management_System_Order_13.setter
    def Order_management_System_Order_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_management_System_Order_13", None)
        self.__Order_management_System_Order_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_management_System_Order_02"):
                opp_val = getattr(old_value, "Order_management_System_Order_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_management_System_Order_02"):
                opp_val = getattr(value, "Order_management_System_Order_02", None)
                if opp_val is None:
                    setattr(value, "Order_management_System_Order_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def foods6(self):
        return self.__foods6
    @foods6.setter
    def foods6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__foods6", None)
        self.__foods6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order7"):
                    opp_val = getattr(item, "order7", None)
                    
                    if opp_val == self:
                        setattr(item, "order7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order7"):
                    opp_val = getattr(item, "order7", None)
                    
                    setattr(item, "order7", self)
                    



class Class:

    pass


class Order_management_System:

    def __init__(self, Orderlist: Class, staff1: "Staff" = None, Order_management_System_Order_02: set["Order"] = None):
        self.Orderlist = Orderlist
        self.staff1 = staff1
        self.Order_management_System_Order_02 = Order_management_System_Order_02 if Order_management_System_Order_02 is not None else set()
        
        pass
    @property
    def Orderlist(self):
        return self.__Orderlist
    @Orderlist.setter
    def Orderlist(self, Orderlist: Class):
        self.__Orderlist = Orderlist

    @property
    def staff1(self):
        return self.__staff1
    @staff1.setter
    def staff1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_management_System__staff1", None)
        self.__staff1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Staff_Order_management_System_00"):
                opp_val = getattr(old_value, "Staff_Order_management_System_00", None)
                if opp_val == self:
                    setattr(old_value, "Staff_Order_management_System_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Staff_Order_management_System_00"):
                opp_val = getattr(value, "Staff_Order_management_System_00", None)
                setattr(value, "Staff_Order_management_System_00", self)

    @property
    def Order_management_System_Order_02(self):
        return self.__Order_management_System_Order_02
    @Order_management_System_Order_02.setter
    def Order_management_System_Order_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_management_System__Order_management_System_Order_02", None)
        self.__Order_management_System_Order_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_management_System_Order_13"):
                    opp_val = getattr(item, "Order_management_System_Order_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Order_management_System_Order_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_management_System_Order_13"):
                    opp_val = getattr(item, "Order_management_System_Order_13", None)
                    
                    setattr(item, "Order_management_System_Order_13", self)
                    

