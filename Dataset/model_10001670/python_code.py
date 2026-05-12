from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Custom_Login:

    def __init__(self, Login: str, Password: str):
        self.Login = Login
        self.Password = Password
        
        pass
    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self, Login: str):
        self.__Login = Login

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Social_Login:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Corporate_Order:

    def __init__(self, Date: str, Corporate_Order_Items_024: set["Items"] = None, Corporate_Order_Customer_028: "Customer" = None):
        self.Date = Date
        self.Corporate_Order_Items_024 = Corporate_Order_Items_024 if Corporate_Order_Items_024 is not None else set()
        self.Corporate_Order_Customer_028 = Corporate_Order_Customer_028
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Corporate_Order_Customer_028(self):
        return self.__Corporate_Order_Customer_028
    @Corporate_Order_Customer_028.setter
    def Corporate_Order_Customer_028(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Corporate_Order__Corporate_Order_Customer_028", None)
        self.__Corporate_Order_Customer_028 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Corporate_Order_Customer_129"):
                opp_val = getattr(old_value, "Corporate_Order_Customer_129", None)
                if opp_val == self:
                    setattr(old_value, "Corporate_Order_Customer_129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Corporate_Order_Customer_129"):
                opp_val = getattr(value, "Corporate_Order_Customer_129", None)
                setattr(value, "Corporate_Order_Customer_129", self)

    @property
    def Corporate_Order_Items_024(self):
        return self.__Corporate_Order_Items_024
    @Corporate_Order_Items_024.setter
    def Corporate_Order_Items_024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Corporate_Order__Corporate_Order_Items_024", None)
        self.__Corporate_Order_Items_024 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Corporate_Order_Items_125"):
                    opp_val = getattr(item, "Corporate_Order_Items_125", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Corporate_Order_Items_125"):
                    opp_val = getattr(item, "Corporate_Order_Items_125", None)
                    
                    if opp_val is None:
                        setattr(item, "Corporate_Order_Items_125", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Phone_Order:

    def __init__(self, Date: str, Phone_Order_Items_022: set["Items"] = None, Phone_Order_Customer_026: "Customer" = None):
        self.Date = Date
        self.Phone_Order_Items_022 = Phone_Order_Items_022 if Phone_Order_Items_022 is not None else set()
        self.Phone_Order_Customer_026 = Phone_Order_Customer_026
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Phone_Order_Items_022(self):
        return self.__Phone_Order_Items_022
    @Phone_Order_Items_022.setter
    def Phone_Order_Items_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Phone_Order__Phone_Order_Items_022", None)
        self.__Phone_Order_Items_022 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Phone_Order_Items_123"):
                    opp_val = getattr(item, "Phone_Order_Items_123", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Phone_Order_Items_123"):
                    opp_val = getattr(item, "Phone_Order_Items_123", None)
                    
                    if opp_val is None:
                        setattr(item, "Phone_Order_Items_123", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Phone_Order_Customer_026(self):
        return self.__Phone_Order_Customer_026
    @Phone_Order_Customer_026.setter
    def Phone_Order_Customer_026(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Phone_Order__Phone_Order_Customer_026", None)
        self.__Phone_Order_Customer_026 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Phone_Order_Customer_127"):
                opp_val = getattr(old_value, "Phone_Order_Customer_127", None)
                if opp_val == self:
                    setattr(old_value, "Phone_Order_Customer_127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Phone_Order_Customer_127"):
                opp_val = getattr(value, "Phone_Order_Customer_127", None)
                setattr(value, "Phone_Order_Customer_127", self)



class Items:

    def __init__(self, SKUCode: str, Quantity: str, Shopping_Cart_Items_115: set["Shopping_Cart"] = None, Phone_Order_Items_123: set["Phone_Order"] = None, Corporate_Order_Items_125: set["Corporate_Order"] = None):
        self.SKUCode = SKUCode
        self.Quantity = Quantity
        self.Shopping_Cart_Items_115 = Shopping_Cart_Items_115 if Shopping_Cart_Items_115 is not None else set()
        self.Phone_Order_Items_123 = Phone_Order_Items_123 if Phone_Order_Items_123 is not None else set()
        self.Corporate_Order_Items_125 = Corporate_Order_Items_125 if Corporate_Order_Items_125 is not None else set()
        
        pass
    @property
    def SKUCode(self):
        return self.__SKUCode
    @SKUCode.setter
    def SKUCode(self, SKUCode: str):
        self.__SKUCode = SKUCode

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def Corporate_Order_Items_125(self):
        return self.__Corporate_Order_Items_125
    @Corporate_Order_Items_125.setter
    def Corporate_Order_Items_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__Corporate_Order_Items_125", None)
        self.__Corporate_Order_Items_125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Corporate_Order_Items_024"):
                    opp_val = getattr(item, "Corporate_Order_Items_024", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Corporate_Order_Items_024"):
                    opp_val = getattr(item, "Corporate_Order_Items_024", None)
                    
                    if opp_val is None:
                        setattr(item, "Corporate_Order_Items_024", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Phone_Order_Items_123(self):
        return self.__Phone_Order_Items_123
    @Phone_Order_Items_123.setter
    def Phone_Order_Items_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__Phone_Order_Items_123", None)
        self.__Phone_Order_Items_123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Phone_Order_Items_022"):
                    opp_val = getattr(item, "Phone_Order_Items_022", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Phone_Order_Items_022"):
                    opp_val = getattr(item, "Phone_Order_Items_022", None)
                    
                    if opp_val is None:
                        setattr(item, "Phone_Order_Items_022", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Shopping_Cart_Items_115(self):
        return self.__Shopping_Cart_Items_115
    @Shopping_Cart_Items_115.setter
    def Shopping_Cart_Items_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__Shopping_Cart_Items_115", None)
        self.__Shopping_Cart_Items_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shopping_Cart_Items_014"):
                    opp_val = getattr(item, "Shopping_Cart_Items_014", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shopping_Cart_Items_014"):
                    opp_val = getattr(item, "Shopping_Cart_Items_014", None)
                    
                    if opp_val is None:
                        setattr(item, "Shopping_Cart_Items_014", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Account:

    def __init__(self, Address: str, ContactNo: str, Email: str, customer8: "Customer" = None, Customer_Account_111: "Customer" = None, order17: "Order" = None, order19: "Order" = None, Account_Order_020: "Order" = None):
        self.Address = Address
        self.ContactNo = ContactNo
        self.Email = Email
        self.customer8 = customer8
        self.Customer_Account_111 = Customer_Account_111
        self.order17 = order17
        self.order19 = order19
        self.Account_Order_020 = Account_Order_020
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def ContactNo(self):
        return self.__ContactNo
    @ContactNo.setter
    def ContactNo(self, ContactNo: str):
        self.__ContactNo = ContactNo

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Customer_Account_111(self):
        return self.__Customer_Account_111
    @Customer_Account_111.setter
    def Customer_Account_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__Customer_Account_111", None)
        self.__Customer_Account_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Account_010"):
                opp_val = getattr(old_value, "Customer_Account_010", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Account_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Account_010"):
                opp_val = getattr(value, "Customer_Account_010", None)
                setattr(value, "Customer_Account_010", self)

    @property
    def order19(self):
        return self.__order19
    @order19.setter
    def order19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order19", None)
        self.__order19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account18"):
                opp_val = getattr(old_value, "account18", None)
                if opp_val == self:
                    setattr(old_value, "account18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account18"):
                opp_val = getattr(value, "account18", None)
                setattr(value, "account18", self)

    @property
    def customer8(self):
        return self.__customer8
    @customer8.setter
    def customer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer8", None)
        self.__customer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account9"):
                opp_val = getattr(old_value, "account9", None)
                if opp_val == self:
                    setattr(old_value, "account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account9"):
                opp_val = getattr(value, "account9", None)
                setattr(value, "account9", self)

    @property
    def order17(self):
        return self.__order17
    @order17.setter
    def order17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order17", None)
        self.__order17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account16"):
                opp_val = getattr(old_value, "account16", None)
                if opp_val == self:
                    setattr(old_value, "account16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account16"):
                opp_val = getattr(value, "account16", None)
                setattr(value, "account16", self)

    @property
    def Account_Order_020(self):
        return self.__Account_Order_020
    @Account_Order_020.setter
    def Account_Order_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__Account_Order_020", None)
        self.__Account_Order_020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Account_Order_121"):
                opp_val = getattr(old_value, "Account_Order_121", None)
                if opp_val == self:
                    setattr(old_value, "Account_Order_121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Account_Order_121"):
                opp_val = getattr(value, "Account_Order_121", None)
                setattr(value, "Account_Order_121", self)



class Order:

    def __init__(self, Order_ID: str, ReceipientName: str, ReceipientAddress: str, ReceipientContactNo: str, ReceipientEmail: str, GiftMessage: str, Customer_Order_13: "Customer" = None, Payment__Order_113: "Payment" = None, account16: "Account" = None, account18: "Account" = None, Account_Order_121: "Account" = None):
        self.Order_ID = Order_ID
        self.ReceipientName = ReceipientName
        self.ReceipientAddress = ReceipientAddress
        self.ReceipientContactNo = ReceipientContactNo
        self.ReceipientEmail = ReceipientEmail
        self.GiftMessage = GiftMessage
        self.Customer_Order_13 = Customer_Order_13
        self.Payment__Order_113 = Payment__Order_113
        self.account16 = account16
        self.account18 = account18
        self.Account_Order_121 = Account_Order_121
        
        pass
    @property
    def ReceipientContactNo(self):
        return self.__ReceipientContactNo
    @ReceipientContactNo.setter
    def ReceipientContactNo(self, ReceipientContactNo: str):
        self.__ReceipientContactNo = ReceipientContactNo

    @property
    def ReceipientAddress(self):
        return self.__ReceipientAddress
    @ReceipientAddress.setter
    def ReceipientAddress(self, ReceipientAddress: str):
        self.__ReceipientAddress = ReceipientAddress

    @property
    def ReceipientName(self):
        return self.__ReceipientName
    @ReceipientName.setter
    def ReceipientName(self, ReceipientName: str):
        self.__ReceipientName = ReceipientName

    @property
    def GiftMessage(self):
        return self.__GiftMessage
    @GiftMessage.setter
    def GiftMessage(self, GiftMessage: str):
        self.__GiftMessage = GiftMessage

    @property
    def Order_ID(self):
        return self.__Order_ID
    @Order_ID.setter
    def Order_ID(self, Order_ID: str):
        self.__Order_ID = Order_ID

    @property
    def ReceipientEmail(self):
        return self.__ReceipientEmail
    @ReceipientEmail.setter
    def ReceipientEmail(self, ReceipientEmail: str):
        self.__ReceipientEmail = ReceipientEmail

    @property
    def Account_Order_121(self):
        return self.__Account_Order_121
    @Account_Order_121.setter
    def Account_Order_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Account_Order_121", None)
        self.__Account_Order_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Account_Order_020"):
                opp_val = getattr(old_value, "Account_Order_020", None)
                if opp_val == self:
                    setattr(old_value, "Account_Order_020", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Account_Order_020"):
                opp_val = getattr(value, "Account_Order_020", None)
                setattr(value, "Account_Order_020", self)

    @property
    def Customer_Order_13(self):
        return self.__Customer_Order_13
    @Customer_Order_13.setter
    def Customer_Order_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Customer_Order_13", None)
        self.__Customer_Order_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Order_02"):
                opp_val = getattr(old_value, "Customer_Order_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Order_02"):
                opp_val = getattr(value, "Customer_Order_02", None)
                if opp_val is None:
                    setattr(value, "Customer_Order_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Payment__Order_113(self):
        return self.__Payment__Order_113
    @Payment__Order_113.setter
    def Payment__Order_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Payment__Order_113", None)
        self.__Payment__Order_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment__Order_012"):
                opp_val = getattr(old_value, "Payment__Order_012", None)
                if opp_val == self:
                    setattr(old_value, "Payment__Order_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment__Order_012"):
                opp_val = getattr(value, "Payment__Order_012", None)
                setattr(value, "Payment__Order_012", self)

    @property
    def account18(self):
        return self.__account18
    @account18.setter
    def account18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account18", None)
        self.__account18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order19"):
                opp_val = getattr(old_value, "order19", None)
                if opp_val == self:
                    setattr(old_value, "order19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order19"):
                opp_val = getattr(value, "order19", None)
                setattr(value, "order19", self)

    @property
    def account16(self):
        return self.__account16
    @account16.setter
    def account16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account16", None)
        self.__account16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order17"):
                opp_val = getattr(old_value, "order17", None)
                if opp_val == self:
                    setattr(old_value, "order17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order17"):
                opp_val = getattr(value, "order17", None)
                setattr(value, "order17", self)



class Payment:

    def __init__(self, Payment_ID: str, Date: int, Customer_Payment_17: "Customer" = None, Payment__Order_012: "Order" = None):
        self.Payment_ID = Payment_ID
        self.Date = Date
        self.Customer_Payment_17 = Customer_Payment_17
        self.Payment__Order_012 = Payment__Order_012
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: int):
        self.__Date = Date

    @property
    def Payment_ID(self):
        return self.__Payment_ID
    @Payment_ID.setter
    def Payment_ID(self, Payment_ID: str):
        self.__Payment_ID = Payment_ID

    @property
    def Customer_Payment_17(self):
        return self.__Customer_Payment_17
    @Customer_Payment_17.setter
    def Customer_Payment_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__Customer_Payment_17", None)
        self.__Customer_Payment_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Payment_06"):
                opp_val = getattr(old_value, "Customer_Payment_06", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Payment_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Payment_06"):
                opp_val = getattr(value, "Customer_Payment_06", None)
                setattr(value, "Customer_Payment_06", self)

    @property
    def Payment__Order_012(self):
        return self.__Payment__Order_012
    @Payment__Order_012.setter
    def Payment__Order_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__Payment__Order_012", None)
        self.__Payment__Order_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment__Order_113"):
                opp_val = getattr(old_value, "Payment__Order_113", None)
                if opp_val == self:
                    setattr(old_value, "Payment__Order_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment__Order_113"):
                opp_val = getattr(value, "Payment__Order_113", None)
                setattr(value, "Payment__Order_113", self)



class Shopping_Cart:

    def __init__(self, Date: str, Customer_Shopping_Cart_15: "Customer" = None, Shopping_Cart_Items_014: set["Items"] = None):
        self.Date = Date
        self.Customer_Shopping_Cart_15 = Customer_Shopping_Cart_15
        self.Shopping_Cart_Items_014 = Shopping_Cart_Items_014 if Shopping_Cart_Items_014 is not None else set()
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Customer_Shopping_Cart_15(self):
        return self.__Customer_Shopping_Cart_15
    @Customer_Shopping_Cart_15.setter
    def Customer_Shopping_Cart_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__Customer_Shopping_Cart_15", None)
        self.__Customer_Shopping_Cart_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Shopping_Cart_04"):
                opp_val = getattr(old_value, "Customer_Shopping_Cart_04", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Shopping_Cart_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Shopping_Cart_04"):
                opp_val = getattr(value, "Customer_Shopping_Cart_04", None)
                setattr(value, "Customer_Shopping_Cart_04", self)

    @property
    def Shopping_Cart_Items_014(self):
        return self.__Shopping_Cart_Items_014
    @Shopping_Cart_Items_014.setter
    def Shopping_Cart_Items_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__Shopping_Cart_Items_014", None)
        self.__Shopping_Cart_Items_014 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shopping_Cart_Items_115"):
                    opp_val = getattr(item, "Shopping_Cart_Items_115", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shopping_Cart_Items_115"):
                    opp_val = getattr(item, "Shopping_Cart_Items_115", None)
                    
                    if opp_val is None:
                        setattr(item, "Shopping_Cart_Items_115", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Products:

    def __init__(self, SKU_Code: str, Product_Name: str, Customer_Products_11: set["Customer"] = None):
        self.SKU_Code = SKU_Code
        self.Product_Name = Product_Name
        self.Customer_Products_11 = Customer_Products_11 if Customer_Products_11 is not None else set()
        
        pass
    @property
    def SKU_Code(self):
        return self.__SKU_Code
    @SKU_Code.setter
    def SKU_Code(self, SKU_Code: str):
        self.__SKU_Code = SKU_Code

    @property
    def Product_Name(self):
        return self.__Product_Name
    @Product_Name.setter
    def Product_Name(self, Product_Name: str):
        self.__Product_Name = Product_Name

    @property
    def Customer_Products_11(self):
        return self.__Customer_Products_11
    @Customer_Products_11.setter
    def Customer_Products_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__Customer_Products_11", None)
        self.__Customer_Products_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Products_00"):
                    opp_val = getattr(item, "Customer_Products_00", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Products_00"):
                    opp_val = getattr(item, "Customer_Products_00", None)
                    
                    if opp_val is None:
                        setattr(item, "Customer_Products_00", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, Customer_ID: str, Name: str, Customer_Products_00: set["Products"] = None, Customer_Order_02: set["Order"] = None, Customer_Shopping_Cart_04: "Shopping_Cart" = None, Customer_Payment_06: "Payment" = None, account9: "Account" = None, Customer_Account_010: "Account" = None, Phone_Order_Customer_127: "Phone_Order" = None, Corporate_Order_Customer_129: "Corporate_Order" = None):
        self.Customer_ID = Customer_ID
        self.Name = Name
        self.Customer_Products_00 = Customer_Products_00 if Customer_Products_00 is not None else set()
        self.Customer_Order_02 = Customer_Order_02 if Customer_Order_02 is not None else set()
        self.Customer_Shopping_Cart_04 = Customer_Shopping_Cart_04
        self.Customer_Payment_06 = Customer_Payment_06
        self.account9 = account9
        self.Customer_Account_010 = Customer_Account_010
        self.Phone_Order_Customer_127 = Phone_Order_Customer_127
        self.Corporate_Order_Customer_129 = Corporate_Order_Customer_129
        
        pass
    @property
    def Customer_ID(self):
        return self.__Customer_ID
    @Customer_ID.setter
    def Customer_ID(self, Customer_ID: str):
        self.__Customer_ID = Customer_ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Customer_Products_00(self):
        return self.__Customer_Products_00
    @Customer_Products_00.setter
    def Customer_Products_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Products_00", None)
        self.__Customer_Products_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Products_11"):
                    opp_val = getattr(item, "Customer_Products_11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Products_11"):
                    opp_val = getattr(item, "Customer_Products_11", None)
                    
                    if opp_val is None:
                        setattr(item, "Customer_Products_11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account9", None)
        self.__account9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer8"):
                opp_val = getattr(old_value, "customer8", None)
                if opp_val == self:
                    setattr(old_value, "customer8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer8"):
                opp_val = getattr(value, "customer8", None)
                setattr(value, "customer8", self)

    @property
    def Customer_Order_02(self):
        return self.__Customer_Order_02
    @Customer_Order_02.setter
    def Customer_Order_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Order_02", None)
        self.__Customer_Order_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Order_13"):
                    opp_val = getattr(item, "Customer_Order_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Order_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Order_13"):
                    opp_val = getattr(item, "Customer_Order_13", None)
                    
                    setattr(item, "Customer_Order_13", self)
                    

    @property
    def Customer_Shopping_Cart_04(self):
        return self.__Customer_Shopping_Cart_04
    @Customer_Shopping_Cart_04.setter
    def Customer_Shopping_Cart_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Shopping_Cart_04", None)
        self.__Customer_Shopping_Cart_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Shopping_Cart_15"):
                opp_val = getattr(old_value, "Customer_Shopping_Cart_15", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Shopping_Cart_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Shopping_Cart_15"):
                opp_val = getattr(value, "Customer_Shopping_Cart_15", None)
                setattr(value, "Customer_Shopping_Cart_15", self)

    @property
    def Corporate_Order_Customer_129(self):
        return self.__Corporate_Order_Customer_129
    @Corporate_Order_Customer_129.setter
    def Corporate_Order_Customer_129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Corporate_Order_Customer_129", None)
        self.__Corporate_Order_Customer_129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Corporate_Order_Customer_028"):
                opp_val = getattr(old_value, "Corporate_Order_Customer_028", None)
                if opp_val == self:
                    setattr(old_value, "Corporate_Order_Customer_028", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Corporate_Order_Customer_028"):
                opp_val = getattr(value, "Corporate_Order_Customer_028", None)
                setattr(value, "Corporate_Order_Customer_028", self)

    @property
    def Customer_Payment_06(self):
        return self.__Customer_Payment_06
    @Customer_Payment_06.setter
    def Customer_Payment_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Payment_06", None)
        self.__Customer_Payment_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Payment_17"):
                opp_val = getattr(old_value, "Customer_Payment_17", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Payment_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Payment_17"):
                opp_val = getattr(value, "Customer_Payment_17", None)
                setattr(value, "Customer_Payment_17", self)

    @property
    def Customer_Account_010(self):
        return self.__Customer_Account_010
    @Customer_Account_010.setter
    def Customer_Account_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Account_010", None)
        self.__Customer_Account_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Account_111"):
                opp_val = getattr(old_value, "Customer_Account_111", None)
                if opp_val == self:
                    setattr(old_value, "Customer_Account_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Account_111"):
                opp_val = getattr(value, "Customer_Account_111", None)
                setattr(value, "Customer_Account_111", self)

    @property
    def Phone_Order_Customer_127(self):
        return self.__Phone_Order_Customer_127
    @Phone_Order_Customer_127.setter
    def Phone_Order_Customer_127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Phone_Order_Customer_127", None)
        self.__Phone_Order_Customer_127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Phone_Order_Customer_026"):
                opp_val = getattr(old_value, "Phone_Order_Customer_026", None)
                if opp_val == self:
                    setattr(old_value, "Phone_Order_Customer_026", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Phone_Order_Customer_026"):
                opp_val = getattr(value, "Phone_Order_Customer_026", None)
                setattr(value, "Phone_Order_Customer_026", self)

