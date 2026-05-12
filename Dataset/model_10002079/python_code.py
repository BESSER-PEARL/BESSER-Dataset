from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Shopping:

    def __init__(self, Name: str, Location: str, Identity: int):
        self.Name = Name
        self.Location = Location
        self.Identity = Identity
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Identity(self):
        return self.__Identity
    @Identity.setter
    def Identity(self, Identity: int):
        self.__Identity = Identity



class OrderDetails:

    def __init__(self, OrderID: int, ProductID: int, ProductName: str, Quantity: int, UnitCost: int, SubTotal: int, order7: "Order" = None):
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.SubTotal = SubTotal
        self.order7 = order7
        
        pass
    @property
    def ProductName(self):
        return self.__ProductName
    @ProductName.setter
    def ProductName(self, ProductName: str):
        self.__ProductName = ProductName

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def UnitCost(self):
        return self.__UnitCost
    @UnitCost.setter
    def UnitCost(self, UnitCost: int):
        self.__UnitCost = UnitCost

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def SubTotal(self):
        return self.__SubTotal
    @SubTotal.setter
    def SubTotal(self, SubTotal: int):
        self.__SubTotal = SubTotal

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_a6"):
                opp_val = getattr(old_value, "has_a6", None)
                if opp_val == self:
                    setattr(old_value, "has_a6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_a6"):
                opp_val = getattr(value, "has_a6", None)
                setattr(value, "has_a6", self)



class ShippingInfo:

    def __init__(self, ShippingID: int, ShippingType: str, ShippingCost: int, ShippingRegionID: int, order5: "Order" = None):
        self.ShippingID = ShippingID
        self.ShippingType = ShippingType
        self.ShippingCost = ShippingCost
        self.ShippingRegionID = ShippingRegionID
        self.order5 = order5
        
        pass
    @property
    def ShippingType(self):
        return self.__ShippingType
    @ShippingType.setter
    def ShippingType(self, ShippingType: str):
        self.__ShippingType = ShippingType

    @property
    def ShippingCost(self):
        return self.__ShippingCost
    @ShippingCost.setter
    def ShippingCost(self, ShippingCost: int):
        self.__ShippingCost = ShippingCost

    @property
    def ShippingID(self):
        return self.__ShippingID
    @ShippingID.setter
    def ShippingID(self, ShippingID: int):
        self.__ShippingID = ShippingID

    @property
    def ShippingRegionID(self):
        return self.__ShippingRegionID
    @ShippingRegionID.setter
    def ShippingRegionID(self, ShippingRegionID: int):
        self.__ShippingRegionID = ShippingRegionID

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShippingInfo__order5", None)
        self.__order5 = value
        
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



class Order:

    def __init__(self, OrderID: int, DateCreated: str, DateShipped: str, CustomerName: str, CustomerID: str, Status: str, ShippingID: str, customer3: "Customer" = None, shippingInfo4: "ShippingInfo" = None, has_a6: "OrderDetails" = None):
        self.OrderID = OrderID
        self.DateCreated = DateCreated
        self.DateShipped = DateShipped
        self.CustomerName = CustomerName
        self.CustomerID = CustomerID
        self.Status = Status
        self.ShippingID = ShippingID
        self.customer3 = customer3
        self.shippingInfo4 = shippingInfo4
        self.has_a6 = has_a6
        
        pass
    @property
    def DateCreated(self):
        return self.__DateCreated
    @DateCreated.setter
    def DateCreated(self, DateCreated: str):
        self.__DateCreated = DateCreated

    @property
    def ShippingID(self):
        return self.__ShippingID
    @ShippingID.setter
    def ShippingID(self, ShippingID: str):
        self.__ShippingID = ShippingID

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: str):
        self.__CustomerID = CustomerID

    @property
    def DateShipped(self):
        return self.__DateShipped
    @DateShipped.setter
    def DateShipped(self, DateShipped: str):
        self.__DateShipped = DateShipped

    @property
    def shippingInfo4(self):
        return self.__shippingInfo4
    @shippingInfo4.setter
    def shippingInfo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shippingInfo4", None)
        self.__shippingInfo4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if opp_val == self:
                    setattr(old_value, "order5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                setattr(value, "order5", self)

    @property
    def has_a6(self):
        return self.__has_a6
    @has_a6.setter
    def has_a6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__has_a6", None)
        self.__has_a6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order7"):
                opp_val = getattr(old_value, "order7", None)
                if opp_val == self:
                    setattr(old_value, "order7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order7"):
                opp_val = getattr(value, "order7", None)
                setattr(value, "order7", self)

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                if opp_val is None:
                    setattr(value, "order2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ShoppingCart:

    def __init__(self, CartID: int, ProductID: int, Quantity: int, DateAdded: int, customer1: "Customer" = None):
        self.CartID = CartID
        self.ProductID = ProductID
        self.Quantity = Quantity
        self.DateAdded = DateAdded
        self.customer1 = customer1
        
        pass
    @property
    def CartID(self):
        return self.__CartID
    @CartID.setter
    def CartID(self, CartID: int):
        self.__CartID = CartID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def DateAdded(self):
        return self.__DateAdded
    @DateAdded.setter
    def DateAdded(self, DateAdded: int):
        self.__DateAdded = DateAdded

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                if opp_val is None:
                    setattr(value, "shoppingCart0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Administrator:

    def __init__(self, AdminName: str, Email: str):
        self.AdminName = AdminName
        self.Email = Email
        
        pass
    @property
    def AdminName(self):
        return self.__AdminName
    @AdminName.setter
    def AdminName(self, AdminName: str):
        self.__AdminName = AdminName

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class Customer:

    def __init__(self, CustomerName: str, Address: str, Email: str, CreditCartInfo: str, ShippingInfo: str, AccountBalance: int, shoppingCart0: set["ShoppingCart"] = None, order2: set["Order"] = None):
        self.CustomerName = CustomerName
        self.Address = Address
        self.Email = Email
        self.CreditCartInfo = CreditCartInfo
        self.ShippingInfo = ShippingInfo
        self.AccountBalance = AccountBalance
        self.shoppingCart0 = shoppingCart0 if shoppingCart0 is not None else set()
        self.order2 = order2 if order2 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def AccountBalance(self):
        return self.__AccountBalance
    @AccountBalance.setter
    def AccountBalance(self, AccountBalance: int):
        self.__AccountBalance = AccountBalance

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def ShippingInfo(self):
        return self.__ShippingInfo
    @ShippingInfo.setter
    def ShippingInfo(self, ShippingInfo: str):
        self.__ShippingInfo = ShippingInfo

    @property
    def CreditCartInfo(self):
        return self.__CreditCartInfo
    @CreditCartInfo.setter
    def CreditCartInfo(self, CreditCartInfo: str):
        self.__CreditCartInfo = CreditCartInfo

    @property
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order2", None)
        self.__order2 = value if value is not None else set()
        
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
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shoppingCart0", None)
        self.__shoppingCart0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    if opp_val == self:
                        setattr(item, "customer1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    setattr(item, "customer1", self)
                    



class Users:

    def __init__(self, UserID: str, Password: str, LoginStatus: str, RegisterDate: int):
        self.UserID = UserID
        self.Password = Password
        self.LoginStatus = LoginStatus
        self.RegisterDate = RegisterDate
        
        pass
    @property
    def LoginStatus(self):
        return self.__LoginStatus
    @LoginStatus.setter
    def LoginStatus(self, LoginStatus: str):
        self.__LoginStatus = LoginStatus

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def RegisterDate(self):
        return self.__RegisterDate
    @RegisterDate.setter
    def RegisterDate(self, RegisterDate: int):
        self.__RegisterDate = RegisterDate

