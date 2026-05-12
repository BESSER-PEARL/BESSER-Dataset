from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase2_UseCase:

    pass


class UseCase_UseCase:

    pass


class Product_Recommendation_UseCase:

    pass


class Product_search_UseCase:

    pass


class Display_Login_Error_UseCase:

    pass


class Verify_Password_UseCase:

    pass


class Registration_UseCase:

    pass


class Place_Order_UseCase:

    pass


class Browse_Categories_UseCase:

    pass


class Login_UseCase:

    pass


class New_Customer_Actor:

    pass


class Existing_Customer_Actor:

    pass





class OrderDetails:

    def __init__(self, OrderId: int, ProductId: int, Quantity: int, UnitCost: int, Order_OrderDetails_13: "Order" = None):
        self.OrderId = OrderId
        self.ProductId = ProductId
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.Order_OrderDetails_13 = Order_OrderDetails_13
        
        pass
    @property
    def UnitCost(self):
        return self.__UnitCost
    @UnitCost.setter
    def UnitCost(self, UnitCost: int):
        self.__UnitCost = UnitCost

    @property
    def ProductId(self):
        return self.__ProductId
    @ProductId.setter
    def ProductId(self, ProductId: int):
        self.__ProductId = ProductId

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: int):
        self.__OrderId = OrderId

    @property
    def Order_OrderDetails_13(self):
        return self.__Order_OrderDetails_13
    @Order_OrderDetails_13.setter
    def Order_OrderDetails_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__Order_OrderDetails_13", None)
        self.__Order_OrderDetails_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_OrderDetails_02"):
                opp_val = getattr(old_value, "Order_OrderDetails_02", None)
                if opp_val == self:
                    setattr(old_value, "Order_OrderDetails_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_OrderDetails_02"):
                opp_val = getattr(value, "Order_OrderDetails_02", None)
                setattr(value, "Order_OrderDetails_02", self)



class Order:

    def __init__(self, OrderId: int, CustomerId: int, OrderDate: str, ShipDate: str, Order_OrderDetails_02: "OrderDetails" = None, Product_Order_15: "Product" = None):
        self.OrderId = OrderId
        self.CustomerId = CustomerId
        self.OrderDate = OrderDate
        self.ShipDate = ShipDate
        self.Order_OrderDetails_02 = Order_OrderDetails_02
        self.Product_Order_15 = Product_Order_15
        
        pass
    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: int):
        self.__CustomerId = CustomerId

    @property
    def OrderDate(self):
        return self.__OrderDate
    @OrderDate.setter
    def OrderDate(self, OrderDate: str):
        self.__OrderDate = OrderDate

    @property
    def ShipDate(self):
        return self.__ShipDate
    @ShipDate.setter
    def ShipDate(self, ShipDate: str):
        self.__ShipDate = ShipDate

    @property
    def OrderId(self):
        return self.__OrderId
    @OrderId.setter
    def OrderId(self, OrderId: int):
        self.__OrderId = OrderId

    @property
    def Order_OrderDetails_02(self):
        return self.__Order_OrderDetails_02
    @Order_OrderDetails_02.setter
    def Order_OrderDetails_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Order_OrderDetails_02", None)
        self.__Order_OrderDetails_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_OrderDetails_13"):
                opp_val = getattr(old_value, "Order_OrderDetails_13", None)
                if opp_val == self:
                    setattr(old_value, "Order_OrderDetails_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_OrderDetails_13"):
                opp_val = getattr(value, "Order_OrderDetails_13", None)
                setattr(value, "Order_OrderDetails_13", self)

    @property
    def Product_Order_15(self):
        return self.__Product_Order_15
    @Product_Order_15.setter
    def Product_Order_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Product_Order_15", None)
        self.__Product_Order_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product_Order_04"):
                opp_val = getattr(old_value, "Product_Order_04", None)
                if opp_val == self:
                    setattr(old_value, "Product_Order_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product_Order_04"):
                opp_val = getattr(value, "Product_Order_04", None)
                setattr(value, "Product_Order_04", self)



class User:

    def __init__(self, UserId: int, Password: str):
        self.UserId = UserId
        self.Password = Password
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId



class Shopping_Cart:

    def __init__(self, RecordId: int, CartId: int, Quantity: int, ProductId: int, DateCreated: int, Customer_Shopping_Cart_11: "Customer" = None, Shopping_Cart_Product_06: "Product" = None):
        self.RecordId = RecordId
        self.CartId = CartId
        self.Quantity = Quantity
        self.ProductId = ProductId
        self.DateCreated = DateCreated
        self.Customer_Shopping_Cart_11 = Customer_Shopping_Cart_11
        self.Shopping_Cart_Product_06 = Shopping_Cart_Product_06
        
        pass
    @property
    def RecordId(self):
        return self.__RecordId
    @RecordId.setter
    def RecordId(self, RecordId: int):
        self.__RecordId = RecordId

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
    def DateCreated(self):
        return self.__DateCreated
    @DateCreated.setter
    def DateCreated(self, DateCreated: int):
        self.__DateCreated = DateCreated

    @property
    def ProductId(self):
        return self.__ProductId
    @ProductId.setter
    def ProductId(self, ProductId: int):
        self.__ProductId = ProductId

    @property
    def Customer_Shopping_Cart_11(self):
        return self.__Customer_Shopping_Cart_11
    @Customer_Shopping_Cart_11.setter
    def Customer_Shopping_Cart_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__Customer_Shopping_Cart_11", None)
        self.__Customer_Shopping_Cart_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Shopping_Cart_00"):
                opp_val = getattr(old_value, "Customer_Shopping_Cart_00", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Shopping_Cart_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Shopping_Cart_00"):
                opp_val = getattr(value, "Customer_Shopping_Cart_00", None)
                setattr(value, "Customer_Shopping_Cart_00", self)

    @property
    def Shopping_Cart_Product_06(self):
        return self.__Shopping_Cart_Product_06
    @Shopping_Cart_Product_06.setter
    def Shopping_Cart_Product_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__Shopping_Cart_Product_06", None)
        self.__Shopping_Cart_Product_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Cart_Product_17"):
                opp_val = getattr(old_value, "Shopping_Cart_Product_17", None)
                if opp_val == self:
                    setattr(old_value, "Shopping_Cart_Product_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Cart_Product_17"):
                opp_val = getattr(value, "Shopping_Cart_Product_17", None)
                setattr(value, "Shopping_Cart_Product_17", self)



class Product:

    def __init__(self, ModelNumber: int, ModelName: str, UnitCost: int, Description: str, ProductId: int, CategoryId: int, Product_Order_04: "Order" = None, Shopping_Cart_Product_17: "Shopping_Cart" = None):
        self.ModelNumber = ModelNumber
        self.ModelName = ModelName
        self.UnitCost = UnitCost
        self.Description = Description
        self.ProductId = ProductId
        self.CategoryId = CategoryId
        self.Product_Order_04 = Product_Order_04
        self.Shopping_Cart_Product_17 = Shopping_Cart_Product_17
        
        pass
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def UnitCost(self):
        return self.__UnitCost
    @UnitCost.setter
    def UnitCost(self, UnitCost: int):
        self.__UnitCost = UnitCost

    @property
    def ProductId(self):
        return self.__ProductId
    @ProductId.setter
    def ProductId(self, ProductId: int):
        self.__ProductId = ProductId

    @property
    def ModelName(self):
        return self.__ModelName
    @ModelName.setter
    def ModelName(self, ModelName: str):
        self.__ModelName = ModelName

    @property
    def ModelNumber(self):
        return self.__ModelNumber
    @ModelNumber.setter
    def ModelNumber(self, ModelNumber: int):
        self.__ModelNumber = ModelNumber

    @property
    def CategoryId(self):
        return self.__CategoryId
    @CategoryId.setter
    def CategoryId(self, CategoryId: int):
        self.__CategoryId = CategoryId

    @property
    def Shopping_Cart_Product_17(self):
        return self.__Shopping_Cart_Product_17
    @Shopping_Cart_Product_17.setter
    def Shopping_Cart_Product_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Shopping_Cart_Product_17", None)
        self.__Shopping_Cart_Product_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Cart_Product_06"):
                opp_val = getattr(old_value, "Shopping_Cart_Product_06", None)
                if opp_val == self:
                    setattr(old_value, "Shopping_Cart_Product_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Cart_Product_06"):
                opp_val = getattr(value, "Shopping_Cart_Product_06", None)
                setattr(value, "Shopping_Cart_Product_06", self)

    @property
    def Product_Order_04(self):
        return self.__Product_Order_04
    @Product_Order_04.setter
    def Product_Order_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Product_Order_04", None)
        self.__Product_Order_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product_Order_15"):
                opp_val = getattr(old_value, "Product_Order_15", None)
                if opp_val == self:
                    setattr(old_value, "Product_Order_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product_Order_15"):
                opp_val = getattr(value, "Product_Order_15", None)
                setattr(value, "Product_Order_15", self)



class Customer:

    def __init__(self, CustomerId: int, Full_Name: str, Email_Address: str, Password: str, Delivery_address: str, Customer_Shopping_Cart_00: "Shopping_Cart" = None):
        self.CustomerId = CustomerId
        self.Full_Name = Full_Name
        self.Email_Address = Email_Address
        self.Password = Password
        self.Delivery_address = Delivery_address
        self.Customer_Shopping_Cart_00 = Customer_Shopping_Cart_00
        
        pass
    @property
    def Email_Address(self):
        return self.__Email_Address
    @Email_Address.setter
    def Email_Address(self, Email_Address: str):
        self.__Email_Address = Email_Address

    @property
    def Delivery_address(self):
        return self.__Delivery_address
    @Delivery_address.setter
    def Delivery_address(self, Delivery_address: str):
        self.__Delivery_address = Delivery_address

    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: int):
        self.__CustomerId = CustomerId

    @property
    def Full_Name(self):
        return self.__Full_Name
    @Full_Name.setter
    def Full_Name(self, Full_Name: str):
        self.__Full_Name = Full_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Customer_Shopping_Cart_00(self):
        return self.__Customer_Shopping_Cart_00
    @Customer_Shopping_Cart_00.setter
    def Customer_Shopping_Cart_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Shopping_Cart_00", None)
        self.__Customer_Shopping_Cart_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Shopping_Cart_11"):
                opp_val = getattr(old_value, "Customer_Shopping_Cart_11", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Shopping_Cart_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Shopping_Cart_11"):
                opp_val = getattr(value, "Customer_Shopping_Cart_11", None)
                setattr(value, "Customer_Shopping_Cart_11", self)

