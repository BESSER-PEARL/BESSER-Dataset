from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Category:

    def __init__(self, ID: int, Type: str, Food_Items_Category_15: set["Food_Items"] = None):
        self.ID = ID
        self.Type = Type
        self.Food_Items_Category_15 = Food_Items_Category_15 if Food_Items_Category_15 is not None else set()
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Food_Items_Category_15(self):
        return self.__Food_Items_Category_15
    @Food_Items_Category_15.setter
    def Food_Items_Category_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__Food_Items_Category_15", None)
        self.__Food_Items_Category_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Food_Items_Category_04"):
                    opp_val = getattr(item, "Food_Items_Category_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Food_Items_Category_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Food_Items_Category_04"):
                    opp_val = getattr(item, "Food_Items_Category_04", None)
                    
                    setattr(item, "Food_Items_Category_04", self)
                    



class Food_Items:

    def __init__(self, Items_ID: int, Item_Name: str, Items_Manage: Admin, item_photo: str, Items_Price: int, Items_Detail: str, Food_Items_Category_04: "Category" = None, Admin_Food_Items_17: "Admin" = None, customer9: set["Customer"] = None):
        self.Items_ID = Items_ID
        self.Item_Name = Item_Name
        self.Items_Manage = Items_Manage
        self.item_photo = item_photo
        self.Items_Price = Items_Price
        self.Items_Detail = Items_Detail
        self.Food_Items_Category_04 = Food_Items_Category_04
        self.Admin_Food_Items_17 = Admin_Food_Items_17
        self.customer9 = customer9 if customer9 is not None else set()
        
        pass
    @property
    def Items_Manage(self):
        return self.__Items_Manage
    @Items_Manage.setter
    def Items_Manage(self, Items_Manage: Admin):
        self.__Items_Manage = Items_Manage

    @property
    def Items_ID(self):
        return self.__Items_ID
    @Items_ID.setter
    def Items_ID(self, Items_ID: int):
        self.__Items_ID = Items_ID

    @property
    def Item_Name(self):
        return self.__Item_Name
    @Item_Name.setter
    def Item_Name(self, Item_Name: str):
        self.__Item_Name = Item_Name

    @property
    def item_photo(self):
        return self.__item_photo
    @item_photo.setter
    def item_photo(self, item_photo: str):
        self.__item_photo = item_photo

    @property
    def Items_Price(self):
        return self.__Items_Price
    @Items_Price.setter
    def Items_Price(self, Items_Price: int):
        self.__Items_Price = Items_Price

    @property
    def Items_Detail(self):
        return self.__Items_Detail
    @Items_Detail.setter
    def Items_Detail(self, Items_Detail: str):
        self.__Items_Detail = Items_Detail

    @property
    def Food_Items_Category_04(self):
        return self.__Food_Items_Category_04
    @Food_Items_Category_04.setter
    def Food_Items_Category_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food_Items__Food_Items_Category_04", None)
        self.__Food_Items_Category_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Food_Items_Category_15"):
                opp_val = getattr(old_value, "Food_Items_Category_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Food_Items_Category_15"):
                opp_val = getattr(value, "Food_Items_Category_15", None)
                if opp_val is None:
                    setattr(value, "Food_Items_Category_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Admin_Food_Items_17(self):
        return self.__Admin_Food_Items_17
    @Admin_Food_Items_17.setter
    def Admin_Food_Items_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food_Items__Admin_Food_Items_17", None)
        self.__Admin_Food_Items_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_Food_Items_06"):
                opp_val = getattr(old_value, "Admin_Food_Items_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_Food_Items_06"):
                opp_val = getattr(value, "Admin_Food_Items_06", None)
                if opp_val is None:
                    setattr(value, "Admin_Food_Items_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food_Items__customer9", None)
        self.__customer9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food_Items8"):
                    opp_val = getattr(item, "food_Items8", None)
                    
                    if opp_val == self:
                        setattr(item, "food_Items8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food_Items8"):
                    opp_val = getattr(item, "food_Items8", None)
                    
                    setattr(item, "food_Items8", self)
                    



class Cash_on_delievery:

    def __init__(self, Customer_Name: str, Address: str, Phone_number: int, Amount: str):
        self.Customer_Name = Customer_Name
        self.Address = Address
        self.Phone_number = Phone_number
        self.Amount = Amount
        
        pass
    @property
    def Phone_number(self):
        return self.__Phone_number
    @Phone_number.setter
    def Phone_number(self, Phone_number: int):
        self.__Phone_number = Phone_number

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: str):
        self.__Customer_Name = Customer_Name

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount



class Bank:

    def __init__(self, Account_no: int, Account_type: str, Online_payment_ID_and_password: str):
        self.Account_no = Account_no
        self.Account_type = Account_type
        self.Online_payment_ID_and_password = Online_payment_ID_and_password
        
        pass
    @property
    def Online_payment_ID_and_password(self):
        return self.__Online_payment_ID_and_password
    @Online_payment_ID_and_password.setter
    def Online_payment_ID_and_password(self, Online_payment_ID_and_password: str):
        self.__Online_payment_ID_and_password = Online_payment_ID_and_password

    @property
    def Account_type(self):
        return self.__Account_type
    @Account_type.setter
    def Account_type(self, Account_type: str):
        self.__Account_type = Account_type

    @property
    def Account_no(self):
        return self.__Account_no
    @Account_no.setter
    def Account_no(self, Account_no: int):
        self.__Account_no = Account_no



class Payment:

    def __init__(self, Payment_Option: str, Amount: int, System_order_Payment_11: set["System_order"] = None):
        self.Payment_Option = Payment_Option
        self.Amount = Amount
        self.System_order_Payment_11 = System_order_Payment_11 if System_order_Payment_11 is not None else set()
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def Payment_Option(self):
        return self.__Payment_Option
    @Payment_Option.setter
    def Payment_Option(self, Payment_Option: str):
        self.__Payment_Option = Payment_Option

    @property
    def System_order_Payment_11(self):
        return self.__System_order_Payment_11
    @System_order_Payment_11.setter
    def System_order_Payment_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__System_order_Payment_11", None)
        self.__System_order_Payment_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "System_order_Payment_00"):
                    opp_val = getattr(item, "System_order_Payment_00", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "System_order_Payment_00"):
                    opp_val = getattr(item, "System_order_Payment_00", None)
                    
                    if opp_val is None:
                        setattr(item, "System_order_Payment_00", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class System_order:

    def __init__(self, Customer_ID: int, Customer_Name: str, Order_ID: int, Date: int, Time: int, Delivery_Charges: int, Total: int, Payment_Option: str, System_order_Customer_02: "Customer" = None, System_order_Payment_00: set["Payment"] = None):
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.Order_ID = Order_ID
        self.Date = Date
        self.Time = Time
        self.Delivery_Charges = Delivery_Charges
        self.Total = Total
        self.Payment_Option = Payment_Option
        self.System_order_Customer_02 = System_order_Customer_02
        self.System_order_Payment_00 = System_order_Payment_00 if System_order_Payment_00 is not None else set()
        
        pass
    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: int):
        self.__Total = Total

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: int):
        self.__Date = Date

    @property
    def Payment_Option(self):
        return self.__Payment_Option
    @Payment_Option.setter
    def Payment_Option(self, Payment_Option: str):
        self.__Payment_Option = Payment_Option

    @property
    def Delivery_Charges(self):
        return self.__Delivery_Charges
    @Delivery_Charges.setter
    def Delivery_Charges(self, Delivery_Charges: int):
        self.__Delivery_Charges = Delivery_Charges

    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: str):
        self.__Customer_Name = Customer_Name

    @property
    def Order_ID(self):
        return self.__Order_ID
    @Order_ID.setter
    def Order_ID(self, Order_ID: int):
        self.__Order_ID = Order_ID

    @property
    def Customer_ID(self):
        return self.__Customer_ID
    @Customer_ID.setter
    def Customer_ID(self, Customer_ID: int):
        self.__Customer_ID = Customer_ID

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time

    @property
    def System_order_Payment_00(self):
        return self.__System_order_Payment_00
    @System_order_Payment_00.setter
    def System_order_Payment_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_order__System_order_Payment_00", None)
        self.__System_order_Payment_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "System_order_Payment_11"):
                    opp_val = getattr(item, "System_order_Payment_11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "System_order_Payment_11"):
                    opp_val = getattr(item, "System_order_Payment_11", None)
                    
                    if opp_val is None:
                        setattr(item, "System_order_Payment_11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def System_order_Customer_02(self):
        return self.__System_order_Customer_02
    @System_order_Customer_02.setter
    def System_order_Customer_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_order__System_order_Customer_02", None)
        self.__System_order_Customer_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System_order_Customer_13"):
                opp_val = getattr(old_value, "System_order_Customer_13", None)
                if opp_val == self:
                    setattr(old_value, "System_order_Customer_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System_order_Customer_13"):
                opp_val = getattr(value, "System_order_Customer_13", None)
                setattr(value, "System_order_Customer_13", self)



class Customer:

    pass


class Admin:

    pass


class User:

    def __init__(self, User_ID: int, User_Type: str, User_Name: str, User_Password: str):
        self.User_ID = User_ID
        self.User_Type = User_Type
        self.User_Name = User_Name
        self.User_Password = User_Password
        
        pass
    @property
    def User_ID(self):
        return self.__User_ID
    @User_ID.setter
    def User_ID(self, User_ID: int):
        self.__User_ID = User_ID

    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: str):
        self.__User_Name = User_Name

    @property
    def User_Type(self):
        return self.__User_Type
    @User_Type.setter
    def User_Type(self, User_Type: str):
        self.__User_Type = User_Type

    @property
    def User_Password(self):
        return self.__User_Password
    @User_Password.setter
    def User_Password(self, User_Password: str):
        self.__User_Password = User_Password

