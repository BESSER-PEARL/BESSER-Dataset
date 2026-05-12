from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class cheque_UseCase:

    pass


class credit_card_UseCase:

    pass


class Shipping_UseCase:

    pass


class cart_UseCase:

    pass


class Registration_UseCase:

    pass


class Password_UseCase:

    pass


class Order_Details_UseCase:

    pass


class Payment_UseCase:

    pass


class Login_UseCase:

    pass


class customer_Actor:

    pass


class Admin_Actor:

    pass





class Cash:

    def __init__(self, cashTendered: int):
        self.cashTendered = cashTendered
        
        pass
    @property
    def cashTendered(self):
        return self.__cashTendered
    @cashTendered.setter
    def cashTendered(self, cashTendered: int):
        self.__cashTendered = cashTendered



class Credit_Card:

    def __init__(self, number: int):
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number



class Payment:

    def __init__(self, Amount: str, order23: "Order" = None):
        self.Amount = Amount
        self.order23 = order23
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def order23(self):
        return self.__order23
    @order23.setter
    def order23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order23", None)
        self.__order23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment22"):
                opp_val = getattr(old_value, "Payment22", None)
                if opp_val == self:
                    setattr(old_value, "Payment22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment22"):
                opp_val = getattr(value, "Payment22", None)
                setattr(value, "Payment22", self)



class OrderDetails:

    def __init__(self, qty: int, order21: "Order" = None):
        self.qty = qty
        self.order21 = order21
        
        pass
    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def qty(self, qty: int):
        self.__qty = qty

    @property
    def order21(self):
        return self.__order21
    @order21.setter
    def order21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__order21", None)
        self.__order21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails20"):
                opp_val = getattr(old_value, "orderDetails20", None)
                if opp_val == self:
                    setattr(old_value, "orderDetails20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails20"):
                opp_val = getattr(value, "orderDetails20", None)
                setattr(value, "orderDetails20", self)



class Order:

    def __init__(self, Date: str, customer17: "Customer" = None, order_Status19: "Order_Status" = None, orderDetails20: "OrderDetails" = None, Payment22: "Payment" = None):
        self.Date = Date
        self.customer17 = customer17
        self.order_Status19 = order_Status19
        self.orderDetails20 = orderDetails20
        self.Payment22 = Payment22
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def customer17(self):
        return self.__customer17
    @customer17.setter
    def customer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer17", None)
        self.__customer17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                if opp_val is None:
                    setattr(value, "order16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Payment22(self):
        return self.__Payment22
    @Payment22.setter
    def Payment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Payment22", None)
        self.__Payment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order23"):
                opp_val = getattr(old_value, "order23", None)
                if opp_val == self:
                    setattr(old_value, "order23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order23"):
                opp_val = getattr(value, "order23", None)
                setattr(value, "order23", self)

    @property
    def order_Status19(self):
        return self.__order_Status19
    @order_Status19.setter
    def order_Status19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__order_Status19", None)
        self.__order_Status19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order18"):
                opp_val = getattr(old_value, "order18", None)
                if opp_val == self:
                    setattr(old_value, "order18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order18"):
                opp_val = getattr(value, "order18", None)
                setattr(value, "order18", self)

    @property
    def orderDetails20(self):
        return self.__orderDetails20
    @orderDetails20.setter
    def orderDetails20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderDetails20", None)
        self.__orderDetails20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order21"):
                opp_val = getattr(old_value, "order21", None)
                if opp_val == self:
                    setattr(old_value, "order21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order21"):
                opp_val = getattr(value, "order21", None)
                setattr(value, "order21", self)



class Customer:

    def __init__(self, Name: str, Address: str, Contact: str, order16: set["Order"] = None):
        self.Name = Name
        self.Address = Address
        self.Contact = Contact
        self.order16 = order16 if order16 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Contact(self):
        return self.__Contact
    @Contact.setter
    def Contact(self, Contact: str):
        self.__Contact = Contact

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order16", None)
        self.__order16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer17"):
                    opp_val = getattr(item, "customer17", None)
                    
                    if opp_val == self:
                        setattr(item, "customer17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer17"):
                    opp_val = getattr(item, "customer17", None)
                    
                    setattr(item, "customer17", self)
                    



class Order_Status:

    def __init__(self, Create: int, Deliveried: int, Paid: int, order18: "Order" = None):
        self.Create = Create
        self.Deliveried = Deliveried
        self.Paid = Paid
        self.order18 = order18
        
        pass
    @property
    def Deliveried(self):
        return self.__Deliveried
    @Deliveried.setter
    def Deliveried(self, Deliveried: int):
        self.__Deliveried = Deliveried

    @property
    def Paid(self):
        return self.__Paid
    @Paid.setter
    def Paid(self, Paid: int):
        self.__Paid = Paid

    @property
    def Create(self):
        return self.__Create
    @Create.setter
    def Create(self, Create: int):
        self.__Create = Create

    @property
    def order18(self):
        return self.__order18
    @order18.setter
    def order18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Status__order18", None)
        self.__order18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Status19"):
                opp_val = getattr(old_value, "order_Status19", None)
                if opp_val == self:
                    setattr(old_value, "order_Status19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Status19"):
                opp_val = getattr(value, "order_Status19", None)
                setattr(value, "order_Status19", self)

