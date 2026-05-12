from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Shopping_cart:

    def __init__(self, Checkout__: Shopping_cart, cartId: int, productId: int, quantity: int, date: int, Add_items_to_shopping_cart__: Shopping_cart, Delete_from_Shopping_Cart__: Shopping_cart, change_to_cart__: Shopping_cart, customer1: "Customer" = None):
        self.Checkout__ = Checkout__
        self.cartId = cartId
        self.productId = productId
        self.quantity = quantity
        self.date = date
        self.Add_items_to_shopping_cart__ = Add_items_to_shopping_cart__
        self.Delete_from_Shopping_Cart__ = Delete_from_Shopping_Cart__
        self.change_to_cart__ = change_to_cart__
        self.customer1 = customer1
        
        pass
    @property
    def change_to_cart__(self):
        return self.__change_to_cart__
    @change_to_cart__.setter
    def change_to_cart__(self, change_to_cart__: Shopping_cart):
        self.__change_to_cart__ = change_to_cart__

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def cartId(self):
        return self.__cartId
    @cartId.setter
    def cartId(self, cartId: int):
        self.__cartId = cartId

    @property
    def Checkout__(self):
        return self.__Checkout__
    @Checkout__.setter
    def Checkout__(self, Checkout__: Shopping_cart):
        self.__Checkout__ = Checkout__

    @property
    def Delete_from_Shopping_Cart__(self):
        return self.__Delete_from_Shopping_Cart__
    @Delete_from_Shopping_Cart__.setter
    def Delete_from_Shopping_Cart__(self, Delete_from_Shopping_Cart__: Shopping_cart):
        self.__Delete_from_Shopping_Cart__ = Delete_from_Shopping_Cart__

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def Add_items_to_shopping_cart__(self):
        return self.__Add_items_to_shopping_cart__
    @Add_items_to_shopping_cart__.setter
    def Add_items_to_shopping_cart__(self, Add_items_to_shopping_cart__: Shopping_cart):
        self.__Add_items_to_shopping_cart__ = Add_items_to_shopping_cart__

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart0"):
                opp_val = getattr(old_value, "shopping_cart0", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart0"):
                opp_val = getattr(value, "shopping_cart0", None)
                setattr(value, "shopping_cart0", self)



class Orders:

    def __init__(self, orderId: int, dateCreated: str, dateShipped: str, customerName: str, customerId: str, status: str, shippingId: str, customer3: "Customer" = None, shippingInfo4: "shippingInfo" = None, order_Details6: "Order_Details" = None):
        self.orderId = orderId
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.customerName = customerName
        self.customerId = customerId
        self.status = status
        self.shippingId = shippingId
        self.customer3 = customer3
        self.shippingInfo4 = shippingInfo4
        self.order_Details6 = order_Details6
        
        pass
    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: str):
        self.__customerId = customerId

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def dateShipped(self):
        return self.__dateShipped
    @dateShipped.setter
    def dateShipped(self, dateShipped: str):
        self.__dateShipped = dateShipped

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: str):
        self.__shippingId = shippingId

    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shippingInfo4(self):
        return self.__shippingInfo4
    @shippingInfo4.setter
    def shippingInfo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__shippingInfo4", None)
        self.__shippingInfo4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders5"):
                opp_val = getattr(old_value, "orders5", None)
                if opp_val == self:
                    setattr(old_value, "orders5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders5"):
                opp_val = getattr(value, "orders5", None)
                setattr(value, "orders5", self)

    @property
    def order_Details6(self):
        return self.__order_Details6
    @order_Details6.setter
    def order_Details6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__order_Details6", None)
        self.__order_Details6 = value
        
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
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders2"):
                opp_val = getattr(old_value, "orders2", None)
                if opp_val == self:
                    setattr(old_value, "orders2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders2"):
                opp_val = getattr(value, "orders2", None)
                setattr(value, "orders2", self)



class Order_Details:

    def __init__(self, productName: str, quantity: int, unitCost: int, subTotal: int, Payment__: Order_Details, Report_Generation: Order_Details, orderId: int, productId: int, orders7: "Orders" = None):
        self.productName = productName
        self.quantity = quantity
        self.unitCost = unitCost
        self.subTotal = subTotal
        self.Payment__ = Payment__
        self.Report_Generation = Report_Generation
        self.orderId = orderId
        self.productId = productId
        self.orders7 = orders7
        
        pass
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
    def unitCost(self):
        return self.__unitCost
    @unitCost.setter
    def unitCost(self, unitCost: int):
        self.__unitCost = unitCost

    @property
    def subTotal(self):
        return self.__subTotal
    @subTotal.setter
    def subTotal(self, subTotal: int):
        self.__subTotal = subTotal

    @property
    def Payment__(self):
        return self.__Payment__
    @Payment__.setter
    def Payment__(self, Payment__: Order_Details):
        self.__Payment__ = Payment__

    @property
    def Report_Generation(self):
        return self.__Report_Generation
    @Report_Generation.setter
    def Report_Generation(self, Report_Generation: Order_Details):
        self.__Report_Generation = Report_Generation

    @property
    def productName(self):
        return self.__productName
    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def productId(self):
        return self.__productId
    @productId.setter
    def productId(self, productId: int):
        self.__productId = productId

    @property
    def orders7(self):
        return self.__orders7
    @orders7.setter
    def orders7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Details__orders7", None)
        self.__orders7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Details6"):
                opp_val = getattr(old_value, "order_Details6", None)
                if opp_val == self:
                    setattr(old_value, "order_Details6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Details6"):
                opp_val = getattr(value, "order_Details6", None)
                setattr(value, "order_Details6", self)



class shippingInfo:

    def __init__(self, shippingId: int, shippingType: str, shippingCost: int, shippingRegionId: int, View_Shipping_Status__: shippingInfo, orders5: "Orders" = None):
        self.shippingId = shippingId
        self.shippingType = shippingType
        self.shippingCost = shippingCost
        self.shippingRegionId = shippingRegionId
        self.View_Shipping_Status__ = View_Shipping_Status__
        self.orders5 = orders5
        
        pass
    @property
    def shippingRegionId(self):
        return self.__shippingRegionId
    @shippingRegionId.setter
    def shippingRegionId(self, shippingRegionId: int):
        self.__shippingRegionId = shippingRegionId

    @property
    def shippingId(self):
        return self.__shippingId
    @shippingId.setter
    def shippingId(self, shippingId: int):
        self.__shippingId = shippingId

    @property
    def View_Shipping_Status__(self):
        return self.__View_Shipping_Status__
    @View_Shipping_Status__.setter
    def View_Shipping_Status__(self, View_Shipping_Status__: shippingInfo):
        self.__View_Shipping_Status__ = View_Shipping_Status__

    @property
    def shippingType(self):
        return self.__shippingType
    @shippingType.setter
    def shippingType(self, shippingType: str):
        self.__shippingType = shippingType

    @property
    def shippingCost(self):
        return self.__shippingCost
    @shippingCost.setter
    def shippingCost(self, shippingCost: int):
        self.__shippingCost = shippingCost

    @property
    def orders5(self):
        return self.__orders5
    @orders5.setter
    def orders5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shippingInfo__orders5", None)
        self.__orders5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shippingInfo4"):
                opp_val = getattr(old_value, "shippingInfo4", None)
                if opp_val == self:
                    setattr(old_value, "shippingInfo4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shippingInfo4"):
                opp_val = getattr(value, "shippingInfo4", None)
                setattr(value, "shippingInfo4", self)



class Admin:

    def __init__(self, adminName: str, email: str, attribute: str, Reverse__: Admin, Contact_Us__: Admin, Help__: Admin):
        self.adminName = adminName
        self.email = email
        self.attribute = attribute
        self.Reverse__ = Reverse__
        self.Contact_Us__ = Contact_Us__
        self.Help__ = Help__
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Help__(self):
        return self.__Help__
    @Help__.setter
    def Help__(self, Help__: Admin):
        self.__Help__ = Help__

    @property
    def Contact_Us__(self):
        return self.__Contact_Us__
    @Contact_Us__.setter
    def Contact_Us__(self, Contact_Us__: Admin):
        self.__Contact_Us__ = Contact_Us__

    @property
    def adminName(self):
        return self.__adminName
    @adminName.setter
    def adminName(self, adminName: str):
        self.__adminName = adminName

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Reverse__(self):
        return self.__Reverse__
    @Reverse__.setter
    def Reverse__(self, Reverse__: Admin):
        self.__Reverse__ = Reverse__



class User:

    def __init__(self, userId: str, password: str, loginStatus: str, Logout__: User, Update_Account_Information__: User, View_Account_Purchase_History__: User):
        self.userId = userId
        self.password = password
        self.loginStatus = loginStatus
        self.Logout__ = Logout__
        self.Update_Account_Information__ = Update_Account_Information__
        self.View_Account_Purchase_History__ = View_Account_Purchase_History__
        
        pass
    @property
    def Logout__(self):
        return self.__Logout__
    @Logout__.setter
    def Logout__(self, Logout__: User):
        self.__Logout__ = Logout__

    @property
    def View_Account_Purchase_History__(self):
        return self.__View_Account_Purchase_History__
    @View_Account_Purchase_History__.setter
    def View_Account_Purchase_History__(self, View_Account_Purchase_History__: User):
        self.__View_Account_Purchase_History__ = View_Account_Purchase_History__

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def Update_Account_Information__(self):
        return self.__Update_Account_Information__
    @Update_Account_Information__.setter
    def Update_Account_Information__(self, Update_Account_Information__: User):
        self.__Update_Account_Information__ = Update_Account_Information__

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



class Customer:

    def __init__(self, customerName: str, address: str, email: str, creditCardInfo: str, shippingInfo: str, registration__: Customer, login__: Customer, search__: Customer, shopping_cart0: "Shopping_cart" = None, orders2: "Orders" = None):
        self.customerName = customerName
        self.address = address
        self.email = email
        self.creditCardInfo = creditCardInfo
        self.shippingInfo = shippingInfo
        self.registration__ = registration__
        self.login__ = login__
        self.search__ = search__
        self.shopping_cart0 = shopping_cart0
        self.orders2 = orders2
        
        pass
    @property
    def registration__(self):
        return self.__registration__
    @registration__.setter
    def registration__(self, registration__: Customer):
        self.__registration__ = registration__

    @property
    def creditCardInfo(self):
        return self.__creditCardInfo
    @creditCardInfo.setter
    def creditCardInfo(self, creditCardInfo: str):
        self.__creditCardInfo = creditCardInfo

    @property
    def search__(self):
        return self.__search__
    @search__.setter
    def search__(self, search__: Customer):
        self.__search__ = search__

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def shippingInfo(self):
        return self.__shippingInfo
    @shippingInfo.setter
    def shippingInfo(self, shippingInfo: str):
        self.__shippingInfo = shippingInfo

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def login__(self):
        return self.__login__
    @login__.setter
    def login__(self, login__: Customer):
        self.__login__ = login__

    @property
    def shopping_cart0(self):
        return self.__shopping_cart0
    @shopping_cart0.setter
    def shopping_cart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shopping_cart0", None)
        self.__shopping_cart0 = value
        
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
    def orders2(self):
        return self.__orders2
    @orders2.setter
    def orders2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders2", None)
        self.__orders2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)

