from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Order_Details:

    def __init__(self, Order_Id: int, Product_Id: int, Product_Name: str, Quantity: int, Sub_Total: str, Unicast: str, orders5: "Orders" = None):
        self.Order_Id = Order_Id
        self.Product_Id = Product_Id
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.Sub_Total = Sub_Total
        self.Unicast = Unicast
        self.orders5 = orders5
        
        pass
    @property
    def Product_Name(self):
        return self.__Product_Name
    @Product_Name.setter
    def Product_Name(self, Product_Name: str):
        self.__Product_Name = Product_Name

    @property
    def Product_Id(self):
        return self.__Product_Id
    @Product_Id.setter
    def Product_Id(self, Product_Id: int):
        self.__Product_Id = Product_Id

    @property
    def Order_Id(self):
        return self.__Order_Id
    @Order_Id.setter
    def Order_Id(self, Order_Id: int):
        self.__Order_Id = Order_Id

    @property
    def Unicast(self):
        return self.__Unicast
    @Unicast.setter
    def Unicast(self, Unicast: str):
        self.__Unicast = Unicast

    @property
    def Sub_Total(self):
        return self.__Sub_Total
    @Sub_Total.setter
    def Sub_Total(self, Sub_Total: str):
        self.__Sub_Total = Sub_Total

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def orders5(self):
        return self.__orders5
    @orders5.setter
    def orders5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Details__orders5", None)
        self.__orders5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Details4"):
                opp_val = getattr(old_value, "order_Details4", None)
                if opp_val == self:
                    setattr(old_value, "order_Details4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Details4"):
                opp_val = getattr(value, "order_Details4", None)
                setattr(value, "order_Details4", self)



class Shipping_Info:

    def __init__(self, Shipping_Id: int, Shipping_Type: str, orders3: "Orders" = None):
        self.Shipping_Id = Shipping_Id
        self.Shipping_Type = Shipping_Type
        self.orders3 = orders3
        
        pass
    @property
    def Shipping_Id(self):
        return self.__Shipping_Id
    @Shipping_Id.setter
    def Shipping_Id(self, Shipping_Id: int):
        self.__Shipping_Id = Shipping_Id

    @property
    def Shipping_Type(self):
        return self.__Shipping_Type
    @Shipping_Type.setter
    def Shipping_Type(self, Shipping_Type: str):
        self.__Shipping_Type = Shipping_Type

    @property
    def orders3(self):
        return self.__orders3
    @orders3.setter
    def orders3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shipping_Info__orders3", None)
        self.__orders3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shipping_Info2"):
                opp_val = getattr(old_value, "shipping_Info2", None)
                if opp_val == self:
                    setattr(old_value, "shipping_Info2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shipping_Info2"):
                opp_val = getattr(value, "shipping_Info2", None)
                setattr(value, "shipping_Info2", self)



class Orders:

    def __init__(self, Order_id: int, Date_Created: str, Date_Shipped: str, Customer_Id: str, Status: str, customer1: "Customer" = None, shipping_Info2: "Shipping_Info" = None, order_Details4: "Order_Details" = None):
        self.Order_id = Order_id
        self.Date_Created = Date_Created
        self.Date_Shipped = Date_Shipped
        self.Customer_Id = Customer_Id
        self.Status = Status
        self.customer1 = customer1
        self.shipping_Info2 = shipping_Info2
        self.order_Details4 = order_Details4
        
        pass
    @property
    def Date_Created(self):
        return self.__Date_Created
    @Date_Created.setter
    def Date_Created(self, Date_Created: str):
        self.__Date_Created = Date_Created

    @property
    def Date_Shipped(self):
        return self.__Date_Shipped
    @Date_Shipped.setter
    def Date_Shipped(self, Date_Shipped: str):
        self.__Date_Shipped = Date_Shipped

    @property
    def Order_id(self):
        return self.__Order_id
    @Order_id.setter
    def Order_id(self, Order_id: int):
        self.__Order_id = Order_id

    @property
    def Customer_Id(self):
        return self.__Customer_Id
    @Customer_Id.setter
    def Customer_Id(self, Customer_Id: str):
        self.__Customer_Id = Customer_Id

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def order_Details4(self):
        return self.__order_Details4
    @order_Details4.setter
    def order_Details4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__order_Details4", None)
        self.__order_Details4 = value
        
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
    def shipping_Info2(self):
        return self.__shipping_Info2
    @shipping_Info2.setter
    def shipping_Info2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__shipping_Info2", None)
        self.__shipping_Info2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders3"):
                opp_val = getattr(old_value, "orders3", None)
                if opp_val == self:
                    setattr(old_value, "orders3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders3"):
                opp_val = getattr(value, "orders3", None)
                setattr(value, "orders3", self)

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders0"):
                opp_val = getattr(old_value, "orders0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders0"):
                opp_val = getattr(value, "orders0", None)
                if opp_val is None:
                    setattr(value, "orders0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Shopping_Cart:

    def __init__(self, Cart_id: int, Product_id: int, Quantity: int, customer7: "Customer" = None):
        self.Cart_id = Cart_id
        self.Product_id = Product_id
        self.Quantity = Quantity
        self.customer7 = customer7
        
        pass
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
    def Product_id(self):
        return self.__Product_id
    @Product_id.setter
    def Product_id(self, Product_id: int):
        self.__Product_id = Product_id

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart6"):
                opp_val = getattr(old_value, "shopping_Cart6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart6"):
                opp_val = getattr(value, "shopping_Cart6", None)
                if opp_val is None:
                    setattr(value, "shopping_Cart6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    def __init__(self, AdminName: str, email: str):
        self.AdminName = AdminName
        self.email = email
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def AdminName(self):
        return self.__AdminName
    @AdminName.setter
    def AdminName(self, AdminName: str):
        self.__AdminName = AdminName



class User:

    def __init__(self, User_Id: int, Password: int, Login_Status: str):
        self.User_Id = User_Id
        self.Password = Password
        self.Login_Status = Login_Status
        
        pass
    @property
    def User_Id(self):
        return self.__User_Id
    @User_Id.setter
    def User_Id(self, User_Id: int):
        self.__User_Id = User_Id

    @property
    def Login_Status(self):
        return self.__Login_Status
    @Login_Status.setter
    def Login_Status(self, Login_Status: str):
        self.__Login_Status = Login_Status

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: int):
        self.__Password = Password



class Customer:

    def __init__(self, Customer_Name: str, Address: str, email: str, Credit_Card_Info: int, orders0: set["Orders"] = None, shopping_Cart6: set["Shopping_Cart"] = None):
        self.Customer_Name = Customer_Name
        self.Address = Address
        self.email = email
        self.Credit_Card_Info = Credit_Card_Info
        self.orders0 = orders0 if orders0 is not None else set()
        self.shopping_Cart6 = shopping_Cart6 if shopping_Cart6 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: str):
        self.__Customer_Name = Customer_Name

    @property
    def Credit_Card_Info(self):
        return self.__Credit_Card_Info
    @Credit_Card_Info.setter
    def Credit_Card_Info(self, Credit_Card_Info: int):
        self.__Credit_Card_Info = Credit_Card_Info

    @property
    def orders0(self):
        return self.__orders0
    @orders0.setter
    def orders0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders0", None)
        self.__orders0 = value if value is not None else set()
        
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
                    

    @property
    def shopping_Cart6(self):
        return self.__shopping_Cart6
    @shopping_Cart6.setter
    def shopping_Cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shopping_Cart6", None)
        self.__shopping_Cart6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer7"):
                    opp_val = getattr(item, "customer7", None)
                    
                    if opp_val == self:
                        setattr(item, "customer7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer7"):
                    opp_val = getattr(item, "customer7", None)
                    
                    setattr(item, "customer7", self)
                    

