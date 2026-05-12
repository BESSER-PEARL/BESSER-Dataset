from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Web_Customer_Actor:

    pass


class New_customer_Actor:

    pass


class Registered_Customer_Actor:

    pass


class Cash_on_Delivery_Actor:

    pass


class Authentication_Actor:

    pass


class Client_Register_UseCase:

    pass


class Checkout_UseCase:

    pass


class Make_Purchase_UseCase:

    pass


class View_items_UseCase:

    pass





class Class:

    pass


class Account:

    def __init__(self, id: int, billing_address: Customer, shopping_cart24: "Shopping_cart" = None, customer27: "Customer" = None, order28: "Order" = None, bill33: "Bill" = None):
        self.id = id
        self.billing_address = billing_address
        self.shopping_cart24 = shopping_cart24
        self.customer27 = customer27
        self.order28 = order28
        self.bill33 = bill33
        
        pass
    @property
    def billing_address(self):
        return self.__billing_address
    @billing_address.setter
    def billing_address(self, billing_address: Customer):
        self.__billing_address = billing_address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def shopping_cart24(self):
        return self.__shopping_cart24
    @shopping_cart24.setter
    def shopping_cart24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__shopping_cart24", None)
        self.__shopping_cart24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account25"):
                opp_val = getattr(old_value, "account25", None)
                if opp_val == self:
                    setattr(old_value, "account25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account25"):
                opp_val = getattr(value, "account25", None)
                setattr(value, "account25", self)

    @property
    def customer27(self):
        return self.__customer27
    @customer27.setter
    def customer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer27", None)
        self.__customer27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account26"):
                opp_val = getattr(old_value, "account26", None)
                if opp_val == self:
                    setattr(old_value, "account26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account26"):
                opp_val = getattr(value, "account26", None)
                setattr(value, "account26", self)

    @property
    def order28(self):
        return self.__order28
    @order28.setter
    def order28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order28", None)
        self.__order28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account29"):
                opp_val = getattr(old_value, "account29", None)
                if opp_val == self:
                    setattr(old_value, "account29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account29"):
                opp_val = getattr(value, "account29", None)
                setattr(value, "account29", self)

    @property
    def bill33(self):
        return self.__bill33
    @bill33.setter
    def bill33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__bill33", None)
        self.__bill33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account32"):
                opp_val = getattr(old_value, "account32", None)
                if opp_val == self:
                    setattr(old_value, "account32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account32"):
                opp_val = getattr(value, "account32", None)
                setattr(value, "account32", self)



class Bill:

    def __init__(self, Customer_name: Customer, Billing_address: Account, Total_Price: Order, customer19: "Customer" = None, order31: "Order" = None, account32: "Account" = None):
        self.Customer_name = Customer_name
        self.Billing_address = Billing_address
        self.Total_Price = Total_Price
        self.customer19 = customer19
        self.order31 = order31
        self.account32 = account32
        
        pass
    @property
    def Total_Price(self):
        return self.__Total_Price
    @Total_Price.setter
    def Total_Price(self, Total_Price: Order):
        self.__Total_Price = Total_Price

    @property
    def Customer_name(self):
        return self.__Customer_name
    @Customer_name.setter
    def Customer_name(self, Customer_name: Customer):
        self.__Customer_name = Customer_name

    @property
    def Billing_address(self):
        return self.__Billing_address
    @Billing_address.setter
    def Billing_address(self, Billing_address: Account):
        self.__Billing_address = Billing_address

    @property
    def customer19(self):
        return self.__customer19
    @customer19.setter
    def customer19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__customer19", None)
        self.__customer19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill18"):
                opp_val = getattr(old_value, "bill18", None)
                if opp_val == self:
                    setattr(old_value, "bill18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill18"):
                opp_val = getattr(value, "bill18", None)
                setattr(value, "bill18", self)

    @property
    def account32(self):
        return self.__account32
    @account32.setter
    def account32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__account32", None)
        self.__account32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill33"):
                opp_val = getattr(old_value, "bill33", None)
                if opp_val == self:
                    setattr(old_value, "bill33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill33"):
                opp_val = getattr(value, "bill33", None)
                setattr(value, "bill33", self)

    @property
    def order31(self):
        return self.__order31
    @order31.setter
    def order31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__order31", None)
        self.__order31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill30"):
                opp_val = getattr(old_value, "bill30", None)
                if opp_val == self:
                    setattr(old_value, "bill30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill30"):
                opp_val = getattr(value, "bill30", None)
                setattr(value, "bill30", self)



class Order:

    def __init__(self, id: str, Total: int, account29: "Account" = None, bill30: "Bill" = None):
        self.id = id
        self.Total = Total
        self.account29 = account29
        self.bill30 = bill30
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: int):
        self.__Total = Total

    @property
    def bill30(self):
        return self.__bill30
    @bill30.setter
    def bill30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__bill30", None)
        self.__bill30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order31"):
                opp_val = getattr(old_value, "order31", None)
                if opp_val == self:
                    setattr(old_value, "order31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order31"):
                opp_val = getattr(value, "order31", None)
                setattr(value, "order31", self)

    @property
    def account29(self):
        return self.__account29
    @account29.setter
    def account29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account29", None)
        self.__account29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order28"):
                opp_val = getattr(old_value, "order28", None)
                if opp_val == self:
                    setattr(old_value, "order28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order28"):
                opp_val = getattr(value, "order28", None)
                setattr(value, "order28", self)



class Product:

    def __init__(self, id: int, Product_Name: str, Price: int, suppliers21: "Suppliers" = None, shopping_cart22: "Shopping_cart" = None):
        self.id = id
        self.Product_Name = Product_Name
        self.Price = Price
        self.suppliers21 = suppliers21
        self.shopping_cart22 = shopping_cart22
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Product_Name(self):
        return self.__Product_Name
    @Product_Name.setter
    def Product_Name(self, Product_Name: str):
        self.__Product_Name = Product_Name

    @property
    def shopping_cart22(self):
        return self.__shopping_cart22
    @shopping_cart22.setter
    def shopping_cart22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__shopping_cart22", None)
        self.__shopping_cart22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product23"):
                opp_val = getattr(old_value, "product23", None)
                if opp_val == self:
                    setattr(old_value, "product23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product23"):
                opp_val = getattr(value, "product23", None)
                setattr(value, "product23", self)

    @property
    def suppliers21(self):
        return self.__suppliers21
    @suppliers21.setter
    def suppliers21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__suppliers21", None)
        self.__suppliers21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product20"):
                opp_val = getattr(old_value, "product20", None)
                if opp_val == self:
                    setattr(old_value, "product20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product20"):
                opp_val = getattr(value, "product20", None)
                setattr(value, "product20", self)



class Shopping_cart:

    def __init__(self, Cart_id: int, Customer_id: Customer, Product_Name: Product, Quantity: int, product23: "Product" = None, account25: "Account" = None):
        self.Cart_id = Cart_id
        self.Customer_id = Customer_id
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.product23 = product23
        self.account25 = account25
        
        pass
    @property
    def Customer_id(self):
        return self.__Customer_id
    @Customer_id.setter
    def Customer_id(self, Customer_id: Customer):
        self.__Customer_id = Customer_id

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def Cart_id(self):
        return self.__Cart_id
    @Cart_id.setter
    def Cart_id(self, Cart_id: int):
        self.__Cart_id = Cart_id

    @property
    def Product_Name(self):
        return self.__Product_Name
    @Product_Name.setter
    def Product_Name(self, Product_Name: Product):
        self.__Product_Name = Product_Name

    @property
    def account25(self):
        return self.__account25
    @account25.setter
    def account25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart__account25", None)
        self.__account25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart24"):
                opp_val = getattr(old_value, "shopping_cart24", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart24"):
                opp_val = getattr(value, "shopping_cart24", None)
                setattr(value, "shopping_cart24", self)

    @property
    def product23(self):
        return self.__product23
    @product23.setter
    def product23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart__product23", None)
        self.__product23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart22"):
                opp_val = getattr(old_value, "shopping_cart22", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart22"):
                opp_val = getattr(value, "shopping_cart22", None)
                setattr(value, "shopping_cart22", self)



class Suppliers:

    def __init__(self, id: int, Name: str, product20: "Product" = None):
        self.id = id
        self.Name = Name
        self.product20 = product20
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def product20(self):
        return self.__product20
    @product20.setter
    def product20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Suppliers__product20", None)
        self.__product20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "suppliers21"):
                opp_val = getattr(old_value, "suppliers21", None)
                if opp_val == self:
                    setattr(old_value, "suppliers21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "suppliers21"):
                opp_val = getattr(value, "suppliers21", None)
                setattr(value, "suppliers21", self)



class Customer:

    def __init__(self, Name: str, Address: str, Contact: str, Username: str, Password: str, web_User17: "Web_User" = None, bill18: "Bill" = None, account26: "Account" = None):
        self.Name = Name
        self.Address = Address
        self.Contact = Contact
        self.Username = Username
        self.Password = Password
        self.web_User17 = web_User17
        self.bill18 = bill18
        self.account26 = account26
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Contact(self):
        return self.__Contact
    @Contact.setter
    def Contact(self, Contact: str):
        self.__Contact = Contact

    @property
    def web_User17(self):
        return self.__web_User17
    @web_User17.setter
    def web_User17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__web_User17", None)
        self.__web_User17 = value
        
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
    def account26(self):
        return self.__account26
    @account26.setter
    def account26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account26", None)
        self.__account26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer27"):
                opp_val = getattr(old_value, "customer27", None)
                if opp_val == self:
                    setattr(old_value, "customer27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer27"):
                opp_val = getattr(value, "customer27", None)
                setattr(value, "customer27", self)

    @property
    def bill18(self):
        return self.__bill18
    @bill18.setter
    def bill18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__bill18", None)
        self.__bill18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer19"):
                opp_val = getattr(old_value, "customer19", None)
                if opp_val == self:
                    setattr(old_value, "customer19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer19"):
                opp_val = getattr(value, "customer19", None)
                setattr(value, "customer19", self)



class Web_User:

    def __init__(self, Username: str, Password: int, customer16: "Customer" = None):
        self.Username = Username
        self.Password = Password
        self.customer16 = customer16
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: int):
        self.__Password = Password

    @property
    def customer16(self):
        return self.__customer16
    @customer16.setter
    def customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Web_User__customer16", None)
        self.__customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_User17"):
                opp_val = getattr(old_value, "web_User17", None)
                if opp_val == self:
                    setattr(old_value, "web_User17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_User17"):
                opp_val = getattr(value, "web_User17", None)
                setattr(value, "web_User17", self)

