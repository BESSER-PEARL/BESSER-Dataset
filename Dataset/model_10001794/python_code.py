from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, customer: str, address: str, email: str, credit_card_info: str, shipping_info: str, user0: "User" = None, shopping_Cart2: set["Shopping_Cart"] = None, orders4: set["Orders"] = None):
        self.customer = customer
        self.address = address
        self.email = email
        self.credit_card_info = credit_card_info
        self.shipping_info = shipping_info
        self.user0 = user0
        self.shopping_Cart2 = shopping_Cart2 if shopping_Cart2 is not None else set()
        self.orders4 = orders4 if orders4 is not None else set()
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def credit_card_info(self):
        return self.__credit_card_info
    @credit_card_info.setter
    def credit_card_info(self, credit_card_info: str):
        self.__credit_card_info = credit_card_info

    @property
    def shipping_info(self):
        return self.__shipping_info
    @shipping_info.setter
    def shipping_info(self, shipping_info: str):
        self.__shipping_info = shipping_info

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer: str):
        self.__customer = customer

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
                    

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__user0", None)
        self.__user0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if opp_val == self:
                    setattr(old_value, "customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                setattr(value, "customer1", self)

    @property
    def orders4(self):
        return self.__orders4
    @orders4.setter
    def orders4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders4", None)
        self.__orders4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    if opp_val == self:
                        setattr(item, "customer5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    setattr(item, "customer5", self)
                    



class Products:

    def __init__(self, totral: int, racknumber: int, item10: "Item" = None, Administrator_Products_113: "Administrator" = None):
        self.totral = totral
        self.racknumber = racknumber
        self.item10 = item10
        self.Administrator_Products_113 = Administrator_Products_113
        
        pass
    @property
    def totral(self):
        return self.__totral
    @totral.setter
    def totral(self, totral: int):
        self.__totral = totral

    @property
    def racknumber(self):
        return self.__racknumber
    @racknumber.setter
    def racknumber(self, racknumber: int):
        self.__racknumber = racknumber

    @property
    def item10(self):
        return self.__item10
    @item10.setter
    def item10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__item10", None)
        self.__item10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products11"):
                opp_val = getattr(old_value, "products11", None)
                if opp_val == self:
                    setattr(old_value, "products11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products11"):
                opp_val = getattr(value, "products11", None)
                setattr(value, "products11", self)

    @property
    def Administrator_Products_113(self):
        return self.__Administrator_Products_113
    @Administrator_Products_113.setter
    def Administrator_Products_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__Administrator_Products_113", None)
        self.__Administrator_Products_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products12"):
                opp_val = getattr(old_value, "products12", None)
                if opp_val == self:
                    setattr(old_value, "products12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products12"):
                opp_val = getattr(value, "products12", None)
                setattr(value, "products12", self)



class Item:

    def __init__(self, name: str, unitcost: int, pieceAvailable: int, products11: "Products" = None):
        self.name = name
        self.unitcost = unitcost
        self.pieceAvailable = pieceAvailable
        self.products11 = products11
        
        pass
    @property
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: int):
        self.__unitcost = unitcost

    @property
    def pieceAvailable(self):
        return self.__pieceAvailable
    @pieceAvailable.setter
    def pieceAvailable(self, pieceAvailable: int):
        self.__pieceAvailable = pieceAvailable

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def products11(self):
        return self.__products11
    @products11.setter
    def products11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__products11", None)
        self.__products11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item10"):
                opp_val = getattr(old_value, "item10", None)
                if opp_val == self:
                    setattr(old_value, "item10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item10"):
                opp_val = getattr(value, "item10", None)
                setattr(value, "item10", self)



class Administrator:

    def __init__(self, adminName: str, email: str, products12: "Products" = None, user15: "User" = None):
        self.adminName = adminName
        self.email = email
        self.products12 = products12
        self.user15 = user15
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def adminName(self):
        return self.__adminName
    @adminName.setter
    def adminName(self, adminName: str):
        self.__adminName = adminName

    @property
    def products12(self):
        return self.__products12
    @products12.setter
    def products12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__products12", None)
        self.__products12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Administrator_Products_113"):
                opp_val = getattr(old_value, "Administrator_Products_113", None)
                if opp_val == self:
                    setattr(old_value, "Administrator_Products_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Administrator_Products_113"):
                opp_val = getattr(value, "Administrator_Products_113", None)
                setattr(value, "Administrator_Products_113", self)

    @property
    def user15(self):
        return self.__user15
    @user15.setter
    def user15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__user15", None)
        self.__user15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator14"):
                opp_val = getattr(old_value, "administrator14", None)
                if opp_val == self:
                    setattr(old_value, "administrator14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator14"):
                opp_val = getattr(value, "administrator14", None)
                setattr(value, "administrator14", self)



class Order_Details:

    def __init__(self, orderId: int, productId: int, productName: str, quantity: int, unitcost: int, subtotal: int, orders9: "Orders" = None):
        self.orderId = orderId
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.unitcost = unitcost
        self.subtotal = subtotal
        self.orders9 = orders9
        
        pass
    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: int):
        self.__subtotal = subtotal

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def unitcost(self):
        return self.__unitcost
    @unitcost.setter
    def unitcost(self, unitcost: int):
        self.__unitcost = unitcost

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def orders9(self):
        return self.__orders9
    @orders9.setter
    def orders9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Details__orders9", None)
        self.__orders9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Details8"):
                opp_val = getattr(old_value, "order_Details8", None)
                if opp_val == self:
                    setattr(old_value, "order_Details8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Details8"):
                opp_val = getattr(value, "order_Details8", None)
                setattr(value, "order_Details8", self)



class Orders:

    def __init__(self, OrderId: int, dateCreated: str, Date: str, customerName: str, CustomerId: str, ShippingId: str, status: str, customer5: "Customer" = None, shipping_Info6: "Shipping_Info" = None, order_Details8: "Order_Details" = None):
        self.OrderId = OrderId
        self.dateCreated = dateCreated
        self.Date = Date
        self.customerName = customerName
        self.CustomerId = CustomerId
        self.ShippingId = ShippingId
        self.status = status
        self.customer5 = customer5
        self.shipping_Info6 = shipping_Info6
        self.order_Details8 = order_Details8
        
        pass
    @property
    def ShippingId(self):
        return self.__ShippingId
    @ShippingId.setter
    def ShippingId(self, ShippingId: str):
        self.__ShippingId = ShippingId

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: int):
        self.__OrderId = OrderId

    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: str):
        self.__CustomerId = CustomerId

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def order_Details8(self):
        return self.__order_Details8
    @order_Details8.setter
    def order_Details8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__order_Details8", None)
        self.__order_Details8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders9"):
                opp_val = getattr(old_value, "orders9", None)
                if opp_val == self:
                    setattr(old_value, "orders9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders9"):
                opp_val = getattr(value, "orders9", None)
                setattr(value, "orders9", self)

    @property
    def shipping_Info6(self):
        return self.__shipping_Info6
    @shipping_Info6.setter
    def shipping_Info6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__shipping_Info6", None)
        self.__shipping_Info6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders7"):
                opp_val = getattr(old_value, "orders7", None)
                if opp_val == self:
                    setattr(old_value, "orders7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders7"):
                opp_val = getattr(value, "orders7", None)
                setattr(value, "orders7", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders4"):
                opp_val = getattr(old_value, "orders4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders4"):
                opp_val = getattr(value, "orders4", None)
                if opp_val is None:
                    setattr(value, "orders4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Shopping_Cart:

    def __init__(self, CartId: int, productId: int, Quantity: int, dateAdded: int, customer3: "Customer" = None):
        self.CartId = CartId
        self.productId = productId
        self.Quantity = Quantity
        self.dateAdded = dateAdded
        self.customer3 = customer3
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def CartId(self):
        return self.__CartId
    @CartId.setter
    def CartId(self, CartId: int):
        self.__CartId = CartId

    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: int):
        self.__dateAdded = dateAdded

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

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



class Shipping_Info:

    def __init__(self, Shipping_Id: int, Shipping_Type: str, Shipping_Cost: int, ShippingRegionId: int, orders7: "Orders" = None):
        self.Shipping_Id = Shipping_Id
        self.Shipping_Type = Shipping_Type
        self.Shipping_Cost = Shipping_Cost
        self.ShippingRegionId = ShippingRegionId
        self.orders7 = orders7
        
        pass
    @property
    def Shipping_Cost(self):
        return self.__Shipping_Cost
    @Shipping_Cost.setter
    def Shipping_Cost(self, Shipping_Cost: int):
        self.__Shipping_Cost = Shipping_Cost

    @property
    def Shipping_Type(self):
        return self.__Shipping_Type
    @Shipping_Type.setter
    def Shipping_Type(self, Shipping_Type: str):
        self.__Shipping_Type = Shipping_Type

    @property
    def Shipping_Id(self):
        return self.__Shipping_Id
    @Shipping_Id.setter
    def Shipping_Id(self, Shipping_Id: int):
        self.__Shipping_Id = Shipping_Id

    @property
    def ShippingRegionId(self):
        return self.__ShippingRegionId
    @ShippingRegionId.setter
    def ShippingRegionId(self, ShippingRegionId: int):
        self.__ShippingRegionId = ShippingRegionId

    @property
    def orders7(self):
        return self.__orders7
    @orders7.setter
    def orders7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipping_Info__orders7", None)
        self.__orders7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shipping_Info6"):
                opp_val = getattr(old_value, "shipping_Info6", None)
                if opp_val == self:
                    setattr(old_value, "shipping_Info6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shipping_Info6"):
                opp_val = getattr(value, "shipping_Info6", None)
                setattr(value, "shipping_Info6", self)



class User:

    def __init__(self, User_Id: str, Password: str, loginStatus: str, customer1: "Customer" = None, administrator14: "Administrator" = None):
        self.User_Id = User_Id
        self.Password = Password
        self.loginStatus = loginStatus
        self.customer1 = customer1
        self.administrator14 = administrator14
        
        pass
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def User_Id(self):
        return self.__User_Id
    @User_Id.setter
    def User_Id(self, User_Id: str):
        self.__User_Id = User_Id

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__customer1", None)
        self.__customer1 = value
        
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
    def administrator14(self):
        return self.__administrator14
    @administrator14.setter
    def administrator14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__administrator14", None)
        self.__administrator14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user15"):
                opp_val = getattr(old_value, "user15", None)
                if opp_val == self:
                    setattr(old_value, "user15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user15"):
                opp_val = getattr(value, "user15", None)
                setattr(value, "user15", self)

