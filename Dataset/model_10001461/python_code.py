from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ShoppingCart:

    def __init__(self, cartID: int, productID: int, quantity: int, dateAdded: str, Customer_ShoppingCart_11: "Customer" = None):
        self.cartID = cartID
        self.productID = productID
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.Customer_ShoppingCart_11 = Customer_ShoppingCart_11
        
        pass
    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: str):
        self.__dateAdded = dateAdded

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def productID(self):
        return self.__productID
    @productID.setter
    def productID(self, productID: int):
        self.__productID = productID

    @property
    def cartID(self):
        return self.__cartID
    @cartID.setter
    def cartID(self, cartID: int):
        self.__cartID = cartID

    @property
    def Customer_ShoppingCart_11(self):
        return self.__Customer_ShoppingCart_11
    @Customer_ShoppingCart_11.setter
    def Customer_ShoppingCart_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__Customer_ShoppingCart_11", None)
        self.__Customer_ShoppingCart_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_00"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_00", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_00"):
                opp_val = getattr(value, "Customer_ShoppingCart_00", None)
                setattr(value, "Customer_ShoppingCart_00", self)



class Admin:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class Customer:

    def __init__(self, branch: str, password: str, phone: int, name: str, email: str, sem: str, Customer_ShoppingCart_00: "ShoppingCart" = None):
        self.branch = branch
        self.password = password
        self.phone = phone
        self.name = name
        self.email = email
        self.sem = sem
        self.Customer_ShoppingCart_00 = Customer_ShoppingCart_00
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def sem(self):
        return self.__sem
    @sem.setter
    def sem(self, sem: str):
        self.__sem = sem

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Customer_ShoppingCart_00(self):
        return self.__Customer_ShoppingCart_00
    @Customer_ShoppingCart_00.setter
    def Customer_ShoppingCart_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_ShoppingCart_00", None)
        self.__Customer_ShoppingCart_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_11"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_11", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_11"):
                opp_val = getattr(value, "Customer_ShoppingCart_11", None)
                setattr(value, "Customer_ShoppingCart_11", self)



class Login:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

