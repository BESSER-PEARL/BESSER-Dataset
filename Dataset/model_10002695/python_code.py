from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Classes:

    def __init__(self, quantity: str, Name: str, sc5: "ShoppingCart" = None, product7: "Product" = None, order9: "Order" = None):
        self.quantity = quantity
        self.Name = Name
        self.sc5 = sc5
        self.product7 = product7
        self.order9 = order9
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def sc5(self):
        return self.__sc5
    @sc5.setter
    def sc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes__sc5", None)
        self.__sc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items4"):
                opp_val = getattr(old_value, "items4", None)
                if opp_val == self:
                    setattr(old_value, "items4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items4"):
                opp_val = getattr(value, "items4", None)
                setattr(value, "items4", self)

    @property
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes__order9", None)
        self.__order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items8"):
                opp_val = getattr(old_value, "items8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items8"):
                opp_val = getattr(value, "items8", None)
                if opp_val is None:
                    setattr(value, "items8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product7(self):
        return self.__product7
    @product7.setter
    def product7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes__product7", None)
        self.__product7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems6"):
                opp_val = getattr(old_value, "lineItems6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems6"):
                opp_val = getattr(value, "lineItems6", None)
                if opp_val is None:
                    setattr(value, "lineItems6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: str, Items: str, items8: set["Classes"] = None, account11: "Account" = None, payment13: "Payment" = None):
        self.number = number
        self.Items = Items
        self.items8 = items8 if items8 is not None else set()
        self.account11 = account11
        self.payment13 = payment13
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def Items(self):
        return self.__Items
    @Items.setter
    def Items(self, Items: str):
        self.__Items = Items

    @property
    def payment13(self):
        return self.__payment13
    @payment13.setter
    def payment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment13", None)
        self.__payment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order12"):
                opp_val = getattr(old_value, "order12", None)
                if opp_val == self:
                    setattr(old_value, "order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order12"):
                opp_val = getattr(value, "order12", None)
                setattr(value, "order12", self)

    @property
    def account11(self):
        return self.__account11
    @account11.setter
    def account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account11", None)
        self.__account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                if opp_val is None:
                    setattr(value, "order10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items8", None)
        self.__items8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order9"):
                    opp_val = getattr(item, "order9", None)
                    
                    if opp_val == self:
                        setattr(item, "order9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order9"):
                    opp_val = getattr(item, "order9", None)
                    
                    setattr(item, "order9", self)
                    



class User:

    def __init__(self, login: str, password: str, shoppingCart0: "ShoppingCart" = None):
        self.login = login
        self.password = password
        self.shoppingCart0 = shoppingCart0
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__shoppingCart0", None)
        self.__shoppingCart0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)



class Account:

    def __init__(self, open: date, Valid_invalid: str, cart2: "ShoppingCart" = None, order10: set["Order"] = None):
        self.open = open
        self.Valid_invalid = Valid_invalid
        self.cart2 = cart2
        self.order10 = order10 if order10 is not None else set()
        
        pass
    @property
    def Valid_invalid(self):
        return self.__Valid_invalid
    @Valid_invalid.setter
    def Valid_invalid(self, Valid_invalid: str):
        self.__Valid_invalid = Valid_invalid

    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order10", None)
        self.__order10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    if opp_val == self:
                        setattr(item, "account11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    setattr(item, "account11", self)
                    

    @property
    def cart2(self):
        return self.__cart2
    @cart2.setter
    def cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart2", None)
        self.__cart2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account3"):
                opp_val = getattr(old_value, "account3", None)
                if opp_val == self:
                    setattr(old_value, "account3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account3"):
                opp_val = getattr(value, "account3", None)
                setattr(value, "account3", self)



class ShoppingCart:

    def __init__(self, Update_cart: date, webUser1: "User" = None, account3: "Account" = None, items4: "Classes" = None):
        self.Update_cart = Update_cart
        self.webUser1 = webUser1
        self.account3 = account3
        self.items4 = items4
        
        pass
    @property
    def Update_cart(self):
        return self.__Update_cart
    @Update_cart.setter
    def Update_cart(self, Update_cart: date):
        self.__Update_cart = Update_cart

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                setattr(value, "shoppingCart0", self)

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart2"):
                opp_val = getattr(old_value, "cart2", None)
                if opp_val == self:
                    setattr(old_value, "cart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart2"):
                opp_val = getattr(value, "cart2", None)
                setattr(value, "cart2", self)

    @property
    def items4(self):
        return self.__items4
    @items4.setter
    def items4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items4", None)
        self.__items4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc5"):
                opp_val = getattr(old_value, "sc5", None)
                if opp_val == self:
                    setattr(old_value, "sc5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc5"):
                opp_val = getattr(value, "sc5", None)
                setattr(value, "sc5", self)



class Payment:

    def __init__(self, Paytment_type: str, order12: "Order" = None):
        self.Paytment_type = Paytment_type
        self.order12 = order12
        
        pass
    @property
    def Paytment_type(self):
        return self.__Paytment_type
    @Paytment_type.setter
    def Paytment_type(self, Paytment_type: str):
        self.__Paytment_type = Paytment_type

    @property
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment13"):
                opp_val = getattr(old_value, "payment13", None)
                if opp_val == self:
                    setattr(old_value, "payment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment13"):
                opp_val = getattr(value, "payment13", None)
                setattr(value, "payment13", self)



class Product:

    def __init__(self, name: str, description: str, lineItems6: set["Classes"] = None):
        self.name = name
        self.description = description
        self.lineItems6 = lineItems6 if lineItems6 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lineItems6(self):
        return self.__lineItems6
    @lineItems6.setter
    def lineItems6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__lineItems6", None)
        self.__lineItems6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product7"):
                    opp_val = getattr(item, "product7", None)
                    
                    if opp_val == self:
                        setattr(item, "product7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product7"):
                    opp_val = getattr(item, "product7", None)
                    
                    setattr(item, "product7", self)
                    

