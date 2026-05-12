from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Identity_Provider_Actor:

    pass


class Authentication_Actor:

    pass


class New_Customer_Actor:

    pass


class Registered_customer__Actor:

    pass


class web_customer_Actor:

    pass





class Client_Register_external:

    pass


class Make_Purchase_external:

    pass


class View_Items_external:

    pass


class Online_grocery_shopping_Component:

    pass


class Cancellation:

    def __init__(self, customerID: str, productID: str, amount: str, product9: "Product" = None):
        self.customerID = customerID
        self.productID = productID
        self.amount = amount
        self.product9 = product9
        
        pass
    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: str):
        self.__customerID = customerID

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def productID(self):
        return self.__productID
    @productID.setter
    def productID(self, productID: str):
        self.__productID = productID

    @property
    def product9(self):
        return self.__product9
    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cancellation__product9", None)
        self.__product9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cancellation8"):
                opp_val = getattr(old_value, "cancellation8", None)
                if opp_val == self:
                    setattr(old_value, "cancellation8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cancellation8"):
                opp_val = getattr(value, "cancellation8", None)
                setattr(value, "cancellation8", self)



class Supplier:

    def __init__(self, suppName: str, suppID: str, address: str, product11: "Product" = None):
        self.suppName = suppName
        self.suppID = suppID
        self.address = address
        self.product11 = product11
        
        pass
    @property
    def suppID(self):
        return self.__suppID
    @suppID.setter
    def suppID(self, suppID: str):
        self.__suppID = suppID

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def suppName(self):
        return self.__suppName
    @suppName.setter
    def suppName(self, suppName: str):
        self.__suppName = suppName

    @property
    def product11(self):
        return self.__product11
    @product11.setter
    def product11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supplier__product11", None)
        self.__product11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier10"):
                opp_val = getattr(old_value, "supplier10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier10"):
                opp_val = getattr(value, "supplier10", None)
                if opp_val is None:
                    setattr(value, "supplier10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Product:

    def __init__(self, quantity: int, name: str, price: int, productID: str, shopping_Cart5: "Shopping_Cart" = None, cancellation8: "Cancellation" = None, supplier10: set["Supplier"] = None):
        self.quantity = quantity
        self.name = name
        self.price = price
        self.productID = productID
        self.shopping_Cart5 = shopping_Cart5
        self.cancellation8 = cancellation8
        self.supplier10 = supplier10 if supplier10 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def productID(self, productID: str):
        self.__productID = productID

    @property
    def shopping_Cart5(self):
        return self.__shopping_Cart5
    @shopping_Cart5.setter
    def shopping_Cart5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__shopping_Cart5", None)
        self.__shopping_Cart5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                if opp_val is None:
                    setattr(value, "product4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cancellation8(self):
        return self.__cancellation8
    @cancellation8.setter
    def cancellation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cancellation8", None)
        self.__cancellation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product9"):
                opp_val = getattr(old_value, "product9", None)
                if opp_val == self:
                    setattr(old_value, "product9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product9"):
                opp_val = getattr(value, "product9", None)
                setattr(value, "product9", self)

    @property
    def supplier10(self):
        return self.__supplier10
    @supplier10.setter
    def supplier10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__supplier10", None)
        self.__supplier10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product11"):
                    opp_val = getattr(item, "product11", None)
                    
                    if opp_val == self:
                        setattr(item, "product11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product11"):
                    opp_val = getattr(item, "product11", None)
                    
                    setattr(item, "product11", self)
                    



class Payment:

    def __init__(self, customerId: str, productID: str, amount: int, shopping_Cart7: "Shopping_Cart" = None):
        self.customerId = customerId
        self.productID = productID
        self.amount = amount
        self.shopping_Cart7 = shopping_Cart7
        
        pass
    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: str):
        self.__customerId = customerId

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def productID(self):
        return self.__productID
    @productID.setter
    def productID(self, productID: str):
        self.__productID = productID

    @property
    def shopping_Cart7(self):
        return self.__shopping_Cart7
    @shopping_Cart7.setter
    def shopping_Cart7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__shopping_Cart7", None)
        self.__shopping_Cart7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment6"):
                opp_val = getattr(old_value, "payment6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment6"):
                opp_val = getattr(value, "payment6", None)
                if opp_val is None:
                    setattr(value, "payment6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Shopping_Cart:

    def __init__(self, cartId: str, quantity: int, dateAdded: str, customer3: "Customer" = None, product4: set["Product"] = None, payment6: set["Payment"] = None):
        self.cartId = cartId
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.customer3 = customer3
        self.product4 = product4 if product4 is not None else set()
        self.payment6 = payment6 if payment6 is not None else set()
        
        pass
    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: str):
        self.__cartId = cartId

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: str):
        self.__dateAdded = dateAdded

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart2"):
                opp_val = getattr(old_value, "shopping_Cart2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart2"):
                opp_val = getattr(value, "shopping_Cart2", None)
                if opp_val is None:
                    setattr(value, "shopping_Cart2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__product4", None)
        self.__product4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_Cart5"):
                    opp_val = getattr(item, "shopping_Cart5", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_Cart5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_Cart5"):
                    opp_val = getattr(item, "shopping_Cart5", None)
                    
                    setattr(item, "shopping_Cart5", self)
                    

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__payment6", None)
        self.__payment6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_Cart7"):
                    opp_val = getattr(item, "shopping_Cart7", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_Cart7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_Cart7"):
                    opp_val = getattr(item, "shopping_Cart7", None)
                    
                    setattr(item, "shopping_Cart7", self)
                    



class Customer:

    def __init__(self, address: str, loginName: str, mobileNo: int, shopping_Cart2: set["Shopping_Cart"] = None):
        self.address = address
        self.loginName = loginName
        self.mobileNo = mobileNo
        self.shopping_Cart2 = shopping_Cart2 if shopping_Cart2 is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def mobileNo(self):
        return self.__mobileNo
    @mobileNo.setter
    def mobileNo(self, mobileNo: int):
        self.__mobileNo = mobileNo

    @property
    def loginName(self):
        return self.__loginName
    @loginName.setter
    def loginName(self, loginName: str):
        self.__loginName = loginName

    @property
    def shopping_Cart2(self):
        return self.__shopping_Cart2
    @shopping_Cart2.setter
    def shopping_Cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shopping_Cart2", None)
        self.__shopping_Cart2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    if opp_val == self:
                        setattr(item, "customer3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    setattr(item, "customer3", self)
                    



class administrator:

    def __init__(self, adminName: str, email: str):
        self.adminName = adminName
        self.email = email
        
        pass
    @property
    def adminName(self):
        return self.__adminName
    @adminName.setter
    def adminName(self, adminName: str):
        self.__adminName = adminName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class user:

    def __init__(self, userID: str, password: str, loginStatus: str, user0: "user" = None, user1: "user" = None):
        self.userID = userID
        self.password = password
        self.loginStatus = loginStatus
        self.user0 = user0
        self.user1 = user1
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user0"):
                opp_val = getattr(old_value, "user0", None)
                if opp_val == self:
                    setattr(old_value, "user0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user0"):
                opp_val = getattr(value, "user0", None)
                setattr(value, "user0", self)

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__user0", None)
        self.__user0 = value
        
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

