from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Shopping_Cart:

    def __init__(self, id: str, number: str, total: float, order8: "Order" = None, payment12: "Payment" = None):
        self.id = id
        self.number = number
        self.total = total
        self.order8 = order8
        self.payment12 = payment12
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart9"):
                opp_val = getattr(old_value, "shopping_Cart9", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart9"):
                opp_val = getattr(value, "shopping_Cart9", None)
                setattr(value, "shopping_Cart9", self)

    @property
    def payment12(self):
        return self.__payment12
    @payment12.setter
    def payment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__payment12", None)
        self.__payment12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart13"):
                opp_val = getattr(old_value, "shopping_Cart13", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart13"):
                opp_val = getattr(value, "shopping_Cart13", None)
                setattr(value, "shopping_Cart13", self)



class Order:

    def __init__(self, number: str, ordered: date, shipped: date, ship_to: str, shopping_Cart9: "Shopping_Cart" = None, customer11: "Customer" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.ship_to = ship_to
        self.shopping_Cart9 = shopping_Cart9
        self.customer11 = customer11
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def ship_to(self):
        return self.__ship_to
    @ship_to.setter
    def ship_to(self, ship_to: str):
        self.__ship_to = ship_to

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: date):
        self.__shipped = shipped

    @property
    def customer11(self):
        return self.__customer11
    @customer11.setter
    def customer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer11", None)
        self.__customer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if opp_val == self:
                    setattr(old_value, "order10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                setattr(value, "order10", self)

    @property
    def shopping_Cart9(self):
        return self.__shopping_Cart9
    @shopping_Cart9.setter
    def shopping_Cart9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shopping_Cart9", None)
        self.__shopping_Cart9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order8"):
                opp_val = getattr(old_value, "order8", None)
                if opp_val == self:
                    setattr(old_value, "order8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order8"):
                opp_val = getattr(value, "order8", None)
                setattr(value, "order8", self)



class Payment:

    def __init__(self, id: str, paid: date, details: str, total: float, shopping_Cart13: "Shopping_Cart" = None):
        self.id = id
        self.paid = paid
        self.details = details
        self.total = total
        self.shopping_Cart13 = shopping_Cart13
        
        pass
    @property
    def paid(self):
        return self.__paid
    @paid.setter
    def paid(self, paid: date):
        self.__paid = paid

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def shopping_Cart13(self):
        return self.__shopping_Cart13
    @shopping_Cart13.setter
    def shopping_Cart13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__shopping_Cart13", None)
        self.__shopping_Cart13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment12"):
                opp_val = getattr(old_value, "payment12", None)
                if opp_val == self:
                    setattr(old_value, "payment12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment12"):
                opp_val = getattr(value, "payment12", None)
                setattr(value, "payment12", self)



class Content:

    def __init__(self, quantity: int, price: float, customer7: "Customer" = None):
        self.quantity = quantity
        self.price = price
        self.customer7 = customer7
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Content__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "content6"):
                opp_val = getattr(old_value, "content6", None)
                if opp_val == self:
                    setattr(old_value, "content6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "content6"):
                opp_val = getattr(value, "content6", None)
                setattr(value, "content6", self)



class __enumeration___OderStatus:

    def __init__(self, new: str, hold: str, shipped: str, delivery: str, closed: str, return1: str):
        self.new = new
        self.hold = hold
        self.shipped = shipped
        self.delivery = delivery
        self.closed = closed
        self.return1 = return1
        
        pass
    @property
    def return1(self):
        return self.__return1
    @return1.setter
    def return1(self, return1: str):
        self.__return1 = return1

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: str):
        self.__shipped = shipped

    @property
    def delivery(self):
        return self.__delivery
    @delivery.setter
    def delivery(self, delivery: str):
        self.__delivery = delivery

    @property
    def new(self):
        return self.__new
    @new.setter
    def new(self, new: str):
        self.__new = new

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: str):
        self.__closed = closed

    @property
    def hold(self):
        return self.__hold
    @hold.setter
    def hold(self, hold: str):
        self.__hold = hold



class Customer:

    def __init__(self, name: str, address: str, phone: str, email: str, new_Customer1: "New_Customer" = None, registered_Customer3: "Registered_Customer" = None, product4: "Product" = None, content6: "Content" = None, order10: "Order" = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.new_Customer1 = new_Customer1
        self.registered_Customer3 = registered_Customer3
        self.product4 = product4
        self.content6 = content6
        self.order10 = order10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def new_Customer1(self):
        return self.__new_Customer1
    @new_Customer1.setter
    def new_Customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__new_Customer1", None)
        self.__new_Customer1 = value
        
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
    def registered_Customer3(self):
        return self.__registered_Customer3
    @registered_Customer3.setter
    def registered_Customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__registered_Customer3", None)
        self.__registered_Customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__product4", None)
        self.__product4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order10", None)
        self.__order10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer11"):
                opp_val = getattr(old_value, "customer11", None)
                if opp_val == self:
                    setattr(old_value, "customer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer11"):
                opp_val = getattr(value, "customer11", None)
                setattr(value, "customer11", self)

    @property
    def content6(self):
        return self.__content6
    @content6.setter
    def content6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__content6", None)
        self.__content6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)



class Product:

    def __init__(self, id: str, name: str, supplier: str, customer5: "Customer" = None):
        self.id = id
        self.name = name
        self.supplier = supplier
        self.customer5 = customer5
        
        pass
    @property
    def supplier(self):
        return self.__supplier
    @supplier.setter
    def supplier(self, supplier: str):
        self.__supplier = supplier

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if opp_val == self:
                    setattr(old_value, "product4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                setattr(value, "product4", self)



class New_Customer:

    def __init__(self, Name: str, address: str, phone: str, email: str, password: str, customer0: "Customer" = None):
        self.Name = Name
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.customer0 = customer0
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_Customer__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_Customer1"):
                opp_val = getattr(old_value, "new_Customer1", None)
                if opp_val == self:
                    setattr(old_value, "new_Customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_Customer1"):
                opp_val = getattr(value, "new_Customer1", None)
                setattr(value, "new_Customer1", self)



class __enumeration___UserState:

    def __init__(self, new: str, active: str, blocked: str, banned: str):
        self.new = new
        self.active = active
        self.blocked = blocked
        self.banned = banned
        
        pass
    @property
    def blocked(self):
        return self.__blocked
    @blocked.setter
    def blocked(self, blocked: str):
        self.__blocked = blocked

    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def banned(self):
        return self.__banned
    @banned.setter
    def banned(self, banned: str):
        self.__banned = banned

    @property
    def new(self):
        return self.__new
    @new.setter
    def new(self, new: str):
        self.__new = new



class Registered_Customer:

    def __init__(self, Email: str, password: str, customer2: "Customer" = None):
        self.Email = Email
        self.password = password
        self.customer2 = customer2
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registered_Customer__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registered_Customer3"):
                opp_val = getattr(old_value, "registered_Customer3", None)
                if opp_val == self:
                    setattr(old_value, "registered_Customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registered_Customer3"):
                opp_val = getattr(value, "registered_Customer3", None)
                setattr(value, "registered_Customer3", self)

