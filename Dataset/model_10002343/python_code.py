from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Item:

    def __init__(self, productId: str, price: float, colour: str, user5: "Account" = None, Shopping_Cart_Login_19: "Shopping_Cart" = None):
        self.productId = productId
        self.price = price
        self.colour = colour
        self.user5 = user5
        self.Shopping_Cart_Login_19 = Shopping_Cart_Login_19
        
        pass
    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)

    @property
    def Shopping_Cart_Login_19(self):
        return self.__Shopping_Cart_Login_19
    @Shopping_Cart_Login_19.setter
    def Shopping_Cart_Login_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__Shopping_Cart_Login_19", None)
        self.__Shopping_Cart_Login_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Cart_Login_08"):
                opp_val = getattr(old_value, "Shopping_Cart_Login_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Cart_Login_08"):
                opp_val = getattr(value, "Shopping_Cart_Login_08", None)
                if opp_val is None:
                    setattr(value, "Shopping_Cart_Login_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Shopping_Cart:

    def __init__(self, cartId: str, orders7: "Order" = None, Shopping_Cart_Login_08: set["Item"] = None):
        self.cartId = cartId
        self.orders7 = orders7
        self.Shopping_Cart_Login_08 = Shopping_Cart_Login_08 if Shopping_Cart_Login_08 is not None else set()
        
        pass
    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: str):
        self.__cartId = cartId

    @property
    def orders7(self):
        return self.__orders7
    @orders7.setter
    def orders7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__orders7", None)
        self.__orders7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "friend6"):
                opp_val = getattr(old_value, "friend6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "friend6"):
                opp_val = getattr(value, "friend6", None)
                if opp_val is None:
                    setattr(value, "friend6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Shopping_Cart_Login_08(self):
        return self.__Shopping_Cart_Login_08
    @Shopping_Cart_Login_08.setter
    def Shopping_Cart_Login_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__Shopping_Cart_Login_08", None)
        self.__Shopping_Cart_Login_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shopping_Cart_Login_19"):
                    opp_val = getattr(item, "Shopping_Cart_Login_19", None)
                    
                    if opp_val == self:
                        setattr(item, "Shopping_Cart_Login_19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shopping_Cart_Login_19"):
                    opp_val = getattr(item, "Shopping_Cart_Login_19", None)
                    
                    setattr(item, "Shopping_Cart_Login_19", self)
                    



class Order:

    def __init__(self, quantity: int, price: Item, friend6: set["Shopping_Cart"] = None, user3: "Account" = None):
        self.quantity = quantity
        self.price = price
        self.friend6 = friend6 if friend6 is not None else set()
        self.user3 = user3
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: Item):
        self.__price = price

    @property
    def friend6(self):
        return self.__friend6
    @friend6.setter
    def friend6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__friend6", None)
        self.__friend6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orders7"):
                    opp_val = getattr(item, "orders7", None)
                    
                    if opp_val == self:
                        setattr(item, "orders7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orders7"):
                    opp_val = getattr(item, "orders7", None)
                    
                    setattr(item, "orders7", self)
                    

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post2"):
                opp_val = getattr(old_value, "post2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post2"):
                opp_val = getattr(value, "post2", None)
                if opp_val is None:
                    setattr(value, "post2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer:

    def __init__(self, name: str, emailAddress: str, DOB: str, cellNo: float, Gender: str, user1: "Account" = None):
        self.name = name
        self.emailAddress = emailAddress
        self.DOB = DOB
        self.cellNo = cellNo
        self.Gender = Gender
        self.user1 = user1
        
        pass
    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def cellNo(self):
        return self.__cellNo
    @cellNo.setter
    def cellNo(self, cellNo: float):
        self.__cellNo = cellNo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myprofile0"):
                opp_val = getattr(old_value, "myprofile0", None)
                if opp_val == self:
                    setattr(old_value, "myprofile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myprofile0"):
                opp_val = getattr(value, "myprofile0", None)
                setattr(value, "myprofile0", self)



class Account:

    def __init__(self, Username: str, Password: int, login4: "Item" = None, myprofile0: "Customer" = None, post2: set["Order"] = None):
        self.Username = Username
        self.Password = Password
        self.login4 = login4
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        
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
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__myprofile0", None)
        self.__myprofile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def post2(self):
        return self.__post2
    @post2.setter
    def post2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__post2", None)
        self.__post2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user5"):
                opp_val = getattr(old_value, "user5", None)
                if opp_val == self:
                    setattr(old_value, "user5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user5"):
                opp_val = getattr(value, "user5", None)
                setattr(value, "user5", self)

