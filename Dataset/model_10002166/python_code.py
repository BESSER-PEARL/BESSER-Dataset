from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Estring_Interface:

    pass


class online_shopping_Order_Detail:

    def __init__(self, Order_ID: str, Product_ID: str, Product_Name: Estring_Interface, unit_Cost: str, Quantity: str, Subtotal: str, product15: "online_shopping_Product" = None, Orders_Order_Detail_117: "online_shopping_Orders" = None):
        self.Order_ID = Order_ID
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.unit_Cost = unit_Cost
        self.Quantity = Quantity
        self.Subtotal = Subtotal
        self.product15 = product15
        self.Orders_Order_Detail_117 = Orders_Order_Detail_117
        
        pass
    @property
    def Order_ID(self):
        return self.__Order_ID
    @Order_ID.setter
    def Order_ID(self, Order_ID: str):
        self.__Order_ID = Order_ID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def Product_ID(self):
        return self.__Product_ID
    @Product_ID.setter
    def Product_ID(self, Product_ID: str):
        self.__Product_ID = Product_ID

    @property
    def unit_Cost(self):
        return self.__unit_Cost
    @unit_Cost.setter
    def unit_Cost(self, unit_Cost: str):
        self.__unit_Cost = unit_Cost

    @property
    def Subtotal(self):
        return self.__Subtotal
    @Subtotal.setter
    def Subtotal(self, Subtotal: str):
        self.__Subtotal = Subtotal

    @property
    def Product_Name(self):
        return self.__Product_Name
    @Product_Name.setter
    def Product_Name(self, Product_Name: Estring_Interface):
        self.__Product_Name = Product_Name

    @property
    def Orders_Order_Detail_117(self):
        return self.__Orders_Order_Detail_117
    @Orders_Order_Detail_117.setter
    def Orders_Order_Detail_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Order_Detail__Orders_Order_Detail_117", None)
        self.__Orders_Order_Detail_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orders_Order_Detail_016"):
                opp_val = getattr(old_value, "Orders_Order_Detail_016", None)
                if opp_val == self:
                    setattr(old_value, "Orders_Order_Detail_016", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orders_Order_Detail_016"):
                opp_val = getattr(value, "Orders_Order_Detail_016", None)
                setattr(value, "Orders_Order_Detail_016", self)

    @property
    def product15(self):
        return self.__product15
    @product15.setter
    def product15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Order_Detail__product15", None)
        self.__product15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Detail14"):
                opp_val = getattr(old_value, "order_Detail14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Detail14"):
                opp_val = getattr(value, "order_Detail14", None)
                if opp_val is None:
                    setattr(value, "order_Detail14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class online_shopping_Delivertiony_Informa:

    def __init__(self, Delivery_Address: Estring_Interface, Other_Delivery_Address: Estring_Interface, Delivery_Phone: str, Receiver_Name: Estring_Interface, Orders_Delivertiony_Informa_119: "online_shopping_Orders" = None):
        self.Delivery_Address = Delivery_Address
        self.Other_Delivery_Address = Other_Delivery_Address
        self.Delivery_Phone = Delivery_Phone
        self.Receiver_Name = Receiver_Name
        self.Orders_Delivertiony_Informa_119 = Orders_Delivertiony_Informa_119
        
        pass
    @property
    def Delivery_Address(self):
        return self.__Delivery_Address
    @Delivery_Address.setter
    def Delivery_Address(self, Delivery_Address: Estring_Interface):
        self.__Delivery_Address = Delivery_Address

    @property
    def Receiver_Name(self):
        return self.__Receiver_Name
    @Receiver_Name.setter
    def Receiver_Name(self, Receiver_Name: Estring_Interface):
        self.__Receiver_Name = Receiver_Name

    @property
    def Delivery_Phone(self):
        return self.__Delivery_Phone
    @Delivery_Phone.setter
    def Delivery_Phone(self, Delivery_Phone: str):
        self.__Delivery_Phone = Delivery_Phone

    @property
    def Other_Delivery_Address(self):
        return self.__Other_Delivery_Address
    @Other_Delivery_Address.setter
    def Other_Delivery_Address(self, Other_Delivery_Address: Estring_Interface):
        self.__Other_Delivery_Address = Other_Delivery_Address

    @property
    def Orders_Delivertiony_Informa_119(self):
        return self.__Orders_Delivertiony_Informa_119
    @Orders_Delivertiony_Informa_119.setter
    def Orders_Delivertiony_Informa_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Delivertiony_Informa__Orders_Delivertiony_Informa_119", None)
        self.__Orders_Delivertiony_Informa_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orders_Delivertiony_Informa_018"):
                opp_val = getattr(old_value, "Orders_Delivertiony_Informa_018", None)
                if opp_val == self:
                    setattr(old_value, "Orders_Delivertiony_Informa_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orders_Delivertiony_Informa_018"):
                opp_val = getattr(value, "Orders_Delivertiony_Informa_018", None)
                setattr(value, "Orders_Delivertiony_Informa_018", self)



class online_shopping_Payment:

    def __init__(self, Catch_Pay: str, Online_Pay: str, Shopping_Card_Payment_121: "online_shopping_Shopping_Card" = None):
        self.Catch_Pay = Catch_Pay
        self.Online_Pay = Online_Pay
        self.Shopping_Card_Payment_121 = Shopping_Card_Payment_121
        
        pass
    @property
    def Online_Pay(self):
        return self.__Online_Pay
    @Online_Pay.setter
    def Online_Pay(self, Online_Pay: str):
        self.__Online_Pay = Online_Pay

    @property
    def Catch_Pay(self):
        return self.__Catch_Pay
    @Catch_Pay.setter
    def Catch_Pay(self, Catch_Pay: str):
        self.__Catch_Pay = Catch_Pay

    @property
    def Shopping_Card_Payment_121(self):
        return self.__Shopping_Card_Payment_121
    @Shopping_Card_Payment_121.setter
    def Shopping_Card_Payment_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Payment__Shopping_Card_Payment_121", None)
        self.__Shopping_Card_Payment_121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Card_Payment_020"):
                opp_val = getattr(old_value, "Shopping_Card_Payment_020", None)
                if opp_val == self:
                    setattr(old_value, "Shopping_Card_Payment_020", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Card_Payment_020"):
                opp_val = getattr(value, "Shopping_Card_Payment_020", None)
                setattr(value, "Shopping_Card_Payment_020", self)



class online_shopping_Product:

    def __init__(self, Price: str, Image_File_Name: Estring_Interface, Product_ID: str, Name: Estring_Interface, Description: Estring_Interface, Category_Product_19: "online_shopping_Category" = None, Shopping_Card_Product_113: set["online_shopping_Shopping_Card"] = None, order_Detail14: set["online_shopping_Order_Detail"] = None):
        self.Price = Price
        self.Image_File_Name = Image_File_Name
        self.Product_ID = Product_ID
        self.Name = Name
        self.Description = Description
        self.Category_Product_19 = Category_Product_19
        self.Shopping_Card_Product_113 = Shopping_Card_Product_113 if Shopping_Card_Product_113 is not None else set()
        self.order_Detail14 = order_Detail14 if order_Detail14 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: Estring_Interface):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: Estring_Interface):
        self.__Description = Description

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Image_File_Name(self):
        return self.__Image_File_Name
    @Image_File_Name.setter
    def Image_File_Name(self, Image_File_Name: Estring_Interface):
        self.__Image_File_Name = Image_File_Name

    @property
    def Product_ID(self):
        return self.__Product_ID
    @Product_ID.setter
    def Product_ID(self, Product_ID: str):
        self.__Product_ID = Product_ID

    @property
    def Category_Product_19(self):
        return self.__Category_Product_19
    @Category_Product_19.setter
    def Category_Product_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Product__Category_Product_19", None)
        self.__Category_Product_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category_Product_08"):
                opp_val = getattr(old_value, "Category_Product_08", None)
                if opp_val == self:
                    setattr(old_value, "Category_Product_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category_Product_08"):
                opp_val = getattr(value, "Category_Product_08", None)
                setattr(value, "Category_Product_08", self)

    @property
    def order_Detail14(self):
        return self.__order_Detail14
    @order_Detail14.setter
    def order_Detail14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Product__order_Detail14", None)
        self.__order_Detail14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product15"):
                    opp_val = getattr(item, "product15", None)
                    
                    if opp_val == self:
                        setattr(item, "product15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product15"):
                    opp_val = getattr(item, "product15", None)
                    
                    setattr(item, "product15", self)
                    

    @property
    def Shopping_Card_Product_113(self):
        return self.__Shopping_Card_Product_113
    @Shopping_Card_Product_113.setter
    def Shopping_Card_Product_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Product__Shopping_Card_Product_113", None)
        self.__Shopping_Card_Product_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shopping_Card_Product_012"):
                    opp_val = getattr(item, "Shopping_Card_Product_012", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shopping_Card_Product_012"):
                    opp_val = getattr(item, "Shopping_Card_Product_012", None)
                    
                    if opp_val is None:
                        setattr(item, "Shopping_Card_Product_012", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class online_shopping_Category:

    def __init__(self, Category_ID: str, Department_ID: str, Catemegory_Name: Estring_Interface, Description: Estring_Interface, Deoartment_Category_17: "online_shopping_Deoartment" = None, Category_Product_08: "online_shopping_Product" = None):
        self.Category_ID = Category_ID
        self.Department_ID = Department_ID
        self.Catemegory_Name = Catemegory_Name
        self.Description = Description
        self.Deoartment_Category_17 = Deoartment_Category_17
        self.Category_Product_08 = Category_Product_08
        
        pass
    @property
    def Catemegory_Name(self):
        return self.__Catemegory_Name
    @Catemegory_Name.setter
    def Catemegory_Name(self, Catemegory_Name: Estring_Interface):
        self.__Catemegory_Name = Catemegory_Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: Estring_Interface):
        self.__Description = Description

    @property
    def Category_ID(self):
        return self.__Category_ID
    @Category_ID.setter
    def Category_ID(self, Category_ID: str):
        self.__Category_ID = Category_ID

    @property
    def Department_ID(self):
        return self.__Department_ID
    @Department_ID.setter
    def Department_ID(self, Department_ID: str):
        self.__Department_ID = Department_ID

    @property
    def Deoartment_Category_17(self):
        return self.__Deoartment_Category_17
    @Deoartment_Category_17.setter
    def Deoartment_Category_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Category__Deoartment_Category_17", None)
        self.__Deoartment_Category_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Deoartment_Category_06"):
                opp_val = getattr(old_value, "Deoartment_Category_06", None)
                if opp_val == self:
                    setattr(old_value, "Deoartment_Category_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Deoartment_Category_06"):
                opp_val = getattr(value, "Deoartment_Category_06", None)
                setattr(value, "Deoartment_Category_06", self)

    @property
    def Category_Product_08(self):
        return self.__Category_Product_08
    @Category_Product_08.setter
    def Category_Product_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Category__Category_Product_08", None)
        self.__Category_Product_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category_Product_19"):
                opp_val = getattr(old_value, "Category_Product_19", None)
                if opp_val == self:
                    setattr(old_value, "Category_Product_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category_Product_19"):
                opp_val = getattr(value, "Category_Product_19", None)
                setattr(value, "Category_Product_19", self)



class online_shopping_Shopping_Card:

    def __init__(self, Produced_Id: str, Cart_ID: str, Date_Added: str, Quantity: str, Shopping_Card_Customer_00: "online_shopping_Customer" = None, Customer_Shopping_Card_13: "online_shopping_Customer" = None, Shopping_Card_Product_012: set["online_shopping_Product"] = None, Shopping_Card_Payment_020: "online_shopping_Payment" = None):
        self.Produced_Id = Produced_Id
        self.Cart_ID = Cart_ID
        self.Date_Added = Date_Added
        self.Quantity = Quantity
        self.Shopping_Card_Customer_00 = Shopping_Card_Customer_00
        self.Customer_Shopping_Card_13 = Customer_Shopping_Card_13
        self.Shopping_Card_Product_012 = Shopping_Card_Product_012 if Shopping_Card_Product_012 is not None else set()
        self.Shopping_Card_Payment_020 = Shopping_Card_Payment_020
        
        pass
    @property
    def Cart_ID(self):
        return self.__Cart_ID
    @Cart_ID.setter
    def Cart_ID(self, Cart_ID: str):
        self.__Cart_ID = Cart_ID

    @property
    def Produced_Id(self):
        return self.__Produced_Id
    @Produced_Id.setter
    def Produced_Id(self, Produced_Id: str):
        self.__Produced_Id = Produced_Id

    @property
    def Date_Added(self):
        return self.__Date_Added
    @Date_Added.setter
    def Date_Added(self, Date_Added: str):
        self.__Date_Added = Date_Added

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def Shopping_Card_Product_012(self):
        return self.__Shopping_Card_Product_012
    @Shopping_Card_Product_012.setter
    def Shopping_Card_Product_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Shopping_Card__Shopping_Card_Product_012", None)
        self.__Shopping_Card_Product_012 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shopping_Card_Product_113"):
                    opp_val = getattr(item, "Shopping_Card_Product_113", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shopping_Card_Product_113"):
                    opp_val = getattr(item, "Shopping_Card_Product_113", None)
                    
                    if opp_val is None:
                        setattr(item, "Shopping_Card_Product_113", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Customer_Shopping_Card_13(self):
        return self.__Customer_Shopping_Card_13
    @Customer_Shopping_Card_13.setter
    def Customer_Shopping_Card_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Shopping_Card__Customer_Shopping_Card_13", None)
        self.__Customer_Shopping_Card_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Shopping_Card_02"):
                opp_val = getattr(old_value, "Customer_Shopping_Card_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Shopping_Card_02"):
                opp_val = getattr(value, "Customer_Shopping_Card_02", None)
                if opp_val is None:
                    setattr(value, "Customer_Shopping_Card_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Shopping_Card_Payment_020(self):
        return self.__Shopping_Card_Payment_020
    @Shopping_Card_Payment_020.setter
    def Shopping_Card_Payment_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Shopping_Card__Shopping_Card_Payment_020", None)
        self.__Shopping_Card_Payment_020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Card_Payment_121"):
                opp_val = getattr(old_value, "Shopping_Card_Payment_121", None)
                if opp_val == self:
                    setattr(old_value, "Shopping_Card_Payment_121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Card_Payment_121"):
                opp_val = getattr(value, "Shopping_Card_Payment_121", None)
                setattr(value, "Shopping_Card_Payment_121", self)

    @property
    def Shopping_Card_Customer_00(self):
        return self.__Shopping_Card_Customer_00
    @Shopping_Card_Customer_00.setter
    def Shopping_Card_Customer_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Shopping_Card__Shopping_Card_Customer_00", None)
        self.__Shopping_Card_Customer_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Card1"):
                opp_val = getattr(old_value, "shopping_Card1", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Card1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Card1"):
                opp_val = getattr(value, "shopping_Card1", None)
                setattr(value, "shopping_Card1", self)



class online_shopping_Customer:

    def __init__(self, Name: Estring_Interface, Address: Estring_Interface, E_mail: Estring_Interface, Phone: str, Shippinginfo: Estring_Interface, shopping_Card1: "online_shopping_Shopping_Card" = None, Customer_Shopping_Card_02: set["online_shopping_Shopping_Card"] = None, Customer_Orders_022: set["online_shopping_Orders"] = None):
        self.Name = Name
        self.Address = Address
        self.E_mail = E_mail
        self.Phone = Phone
        self.Shippinginfo = Shippinginfo
        self.shopping_Card1 = shopping_Card1
        self.Customer_Shopping_Card_02 = Customer_Shopping_Card_02 if Customer_Shopping_Card_02 is not None else set()
        self.Customer_Orders_022 = Customer_Orders_022 if Customer_Orders_022 is not None else set()
        
        pass
    @property
    def Shippinginfo(self):
        return self.__Shippinginfo
    @Shippinginfo.setter
    def Shippinginfo(self, Shippinginfo: Estring_Interface):
        self.__Shippinginfo = Shippinginfo

    @property
    def E_mail(self):
        return self.__E_mail
    @E_mail.setter
    def E_mail(self, E_mail: Estring_Interface):
        self.__E_mail = E_mail

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: Estring_Interface):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: Estring_Interface):
        self.__Address = Address

    @property
    def shopping_Card1(self):
        return self.__shopping_Card1
    @shopping_Card1.setter
    def shopping_Card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Customer__shopping_Card1", None)
        self.__shopping_Card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shopping_Card_Customer_00"):
                opp_val = getattr(old_value, "Shopping_Card_Customer_00", None)
                if opp_val == self:
                    setattr(old_value, "Shopping_Card_Customer_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shopping_Card_Customer_00"):
                opp_val = getattr(value, "Shopping_Card_Customer_00", None)
                setattr(value, "Shopping_Card_Customer_00", self)

    @property
    def Customer_Shopping_Card_02(self):
        return self.__Customer_Shopping_Card_02
    @Customer_Shopping_Card_02.setter
    def Customer_Shopping_Card_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Customer__Customer_Shopping_Card_02", None)
        self.__Customer_Shopping_Card_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Shopping_Card_13"):
                    opp_val = getattr(item, "Customer_Shopping_Card_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Shopping_Card_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Shopping_Card_13"):
                    opp_val = getattr(item, "Customer_Shopping_Card_13", None)
                    
                    setattr(item, "Customer_Shopping_Card_13", self)
                    

    @property
    def Customer_Orders_022(self):
        return self.__Customer_Orders_022
    @Customer_Orders_022.setter
    def Customer_Orders_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Customer__Customer_Orders_022", None)
        self.__Customer_Orders_022 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Orders_123"):
                    opp_val = getattr(item, "Customer_Orders_123", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Orders_123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Orders_123"):
                    opp_val = getattr(item, "Customer_Orders_123", None)
                    
                    setattr(item, "Customer_Orders_123", self)
                    



class online_shopping_Orders:

    def __init__(self, Order_ID: int, Date_Created: Estring_Interface, Datw_Shipping: Estring_Interface, Customer_Name: Estring_Interface, Customer_ID: Estring_Interface, Orders_Order_Detail_016: "online_shopping_Order_Detail" = None, Orders_Delivertiony_Informa_018: "online_shopping_Delivertiony_Informa" = None, Customer_Orders_123: "online_shopping_Customer" = None):
        self.Order_ID = Order_ID
        self.Date_Created = Date_Created
        self.Datw_Shipping = Datw_Shipping
        self.Customer_Name = Customer_Name
        self.Customer_ID = Customer_ID
        self.Orders_Order_Detail_016 = Orders_Order_Detail_016
        self.Orders_Delivertiony_Informa_018 = Orders_Delivertiony_Informa_018
        self.Customer_Orders_123 = Customer_Orders_123
        
        pass
    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: Estring_Interface):
        self.__Customer_Name = Customer_Name

    @property
    def Order_ID(self):
        return self.__Order_ID
    @Order_ID.setter
    def Order_ID(self, Order_ID: int):
        self.__Order_ID = Order_ID

    @property
    def Date_Created(self):
        return self.__Date_Created
    @Date_Created.setter
    def Date_Created(self, Date_Created: Estring_Interface):
        self.__Date_Created = Date_Created

    @property
    def Customer_ID(self):
        return self.__Customer_ID
    @Customer_ID.setter
    def Customer_ID(self, Customer_ID: Estring_Interface):
        self.__Customer_ID = Customer_ID

    @property
    def Datw_Shipping(self):
        return self.__Datw_Shipping
    @Datw_Shipping.setter
    def Datw_Shipping(self, Datw_Shipping: Estring_Interface):
        self.__Datw_Shipping = Datw_Shipping

    @property
    def Orders_Order_Detail_016(self):
        return self.__Orders_Order_Detail_016
    @Orders_Order_Detail_016.setter
    def Orders_Order_Detail_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Orders__Orders_Order_Detail_016", None)
        self.__Orders_Order_Detail_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orders_Order_Detail_117"):
                opp_val = getattr(old_value, "Orders_Order_Detail_117", None)
                if opp_val == self:
                    setattr(old_value, "Orders_Order_Detail_117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orders_Order_Detail_117"):
                opp_val = getattr(value, "Orders_Order_Detail_117", None)
                setattr(value, "Orders_Order_Detail_117", self)

    @property
    def Customer_Orders_123(self):
        return self.__Customer_Orders_123
    @Customer_Orders_123.setter
    def Customer_Orders_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Orders__Customer_Orders_123", None)
        self.__Customer_Orders_123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Orders_022"):
                opp_val = getattr(old_value, "Customer_Orders_022", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Orders_022"):
                opp_val = getattr(value, "Customer_Orders_022", None)
                if opp_val is None:
                    setattr(value, "Customer_Orders_022", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Orders_Delivertiony_Informa_018(self):
        return self.__Orders_Delivertiony_Informa_018
    @Orders_Delivertiony_Informa_018.setter
    def Orders_Delivertiony_Informa_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Orders__Orders_Delivertiony_Informa_018", None)
        self.__Orders_Delivertiony_Informa_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orders_Delivertiony_Informa_119"):
                opp_val = getattr(old_value, "Orders_Delivertiony_Informa_119", None)
                if opp_val == self:
                    setattr(old_value, "Orders_Delivertiony_Informa_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orders_Delivertiony_Informa_119"):
                opp_val = getattr(value, "Orders_Delivertiony_Informa_119", None)
                setattr(value, "Orders_Delivertiony_Informa_119", self)



class online_shopping_Session_manager:

    def __init__(self, Person_ID: Estring_Interface, Department_Name: Estring_Interface, Session_manager_Deoartment_04: "online_shopping_Deoartment" = None, Session_manager_Person_010: "online_shopping_Person" = None):
        self.Person_ID = Person_ID
        self.Department_Name = Department_Name
        self.Session_manager_Deoartment_04 = Session_manager_Deoartment_04
        self.Session_manager_Person_010 = Session_manager_Person_010
        
        pass
    @property
    def Department_Name(self):
        return self.__Department_Name
    @Department_Name.setter
    def Department_Name(self, Department_Name: Estring_Interface):
        self.__Department_Name = Department_Name

    @property
    def Person_ID(self):
        return self.__Person_ID
    @Person_ID.setter
    def Person_ID(self, Person_ID: Estring_Interface):
        self.__Person_ID = Person_ID

    @property
    def Session_manager_Person_010(self):
        return self.__Session_manager_Person_010
    @Session_manager_Person_010.setter
    def Session_manager_Person_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Session_manager__Session_manager_Person_010", None)
        self.__Session_manager_Person_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Session_manager_Person_111"):
                opp_val = getattr(old_value, "Session_manager_Person_111", None)
                if opp_val == self:
                    setattr(old_value, "Session_manager_Person_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Session_manager_Person_111"):
                opp_val = getattr(value, "Session_manager_Person_111", None)
                setattr(value, "Session_manager_Person_111", self)

    @property
    def Session_manager_Deoartment_04(self):
        return self.__Session_manager_Deoartment_04
    @Session_manager_Deoartment_04.setter
    def Session_manager_Deoartment_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Session_manager__Session_manager_Deoartment_04", None)
        self.__Session_manager_Deoartment_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Session_manager_Deoartment_15"):
                opp_val = getattr(old_value, "Session_manager_Deoartment_15", None)
                if opp_val == self:
                    setattr(old_value, "Session_manager_Deoartment_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Session_manager_Deoartment_15"):
                opp_val = getattr(value, "Session_manager_Deoartment_15", None)
                setattr(value, "Session_manager_Deoartment_15", self)



class online_shopping_Deoartment:

    def __init__(self, Department_ID: str, Name: str, Description: str, Session_manager_Deoartment_15: "online_shopping_Session_manager" = None, Deoartment_Category_06: "online_shopping_Category" = None):
        self.Department_ID = Department_ID
        self.Name = Name
        self.Description = Description
        self.Session_manager_Deoartment_15 = Session_manager_Deoartment_15
        self.Deoartment_Category_06 = Deoartment_Category_06
        
        pass
    @property
    def Department_ID(self):
        return self.__Department_ID
    @Department_ID.setter
    def Department_ID(self, Department_ID: str):
        self.__Department_ID = Department_ID

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Session_manager_Deoartment_15(self):
        return self.__Session_manager_Deoartment_15
    @Session_manager_Deoartment_15.setter
    def Session_manager_Deoartment_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Deoartment__Session_manager_Deoartment_15", None)
        self.__Session_manager_Deoartment_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Session_manager_Deoartment_04"):
                opp_val = getattr(old_value, "Session_manager_Deoartment_04", None)
                if opp_val == self:
                    setattr(old_value, "Session_manager_Deoartment_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Session_manager_Deoartment_04"):
                opp_val = getattr(value, "Session_manager_Deoartment_04", None)
                setattr(value, "Session_manager_Deoartment_04", self)

    @property
    def Deoartment_Category_06(self):
        return self.__Deoartment_Category_06
    @Deoartment_Category_06.setter
    def Deoartment_Category_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Deoartment__Deoartment_Category_06", None)
        self.__Deoartment_Category_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Deoartment_Category_17"):
                opp_val = getattr(old_value, "Deoartment_Category_17", None)
                if opp_val == self:
                    setattr(old_value, "Deoartment_Category_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Deoartment_Category_17"):
                opp_val = getattr(value, "Deoartment_Category_17", None)
                setattr(value, "Deoartment_Category_17", self)



class online_shopping_Administrator:

    def __init__(self, Name: Estring_Interface, Email: Estring_Interface):
        self.Name = Name
        self.Email = Email
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: Estring_Interface):
        self.__Email = Email

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: Estring_Interface):
        self.__Name = Name



class online_shopping_Person:

    def __init__(self, Person_ID: Estring_Interface, Person_Password: Estring_Interface, Login_Status: Estring_Interface, Session_manager_Person_111: "online_shopping_Session_manager" = None):
        self.Person_ID = Person_ID
        self.Person_Password = Person_Password
        self.Login_Status = Login_Status
        self.Session_manager_Person_111 = Session_manager_Person_111
        
        pass
    @property
    def Login_Status(self):
        return self.__Login_Status
    @Login_Status.setter
    def Login_Status(self, Login_Status: Estring_Interface):
        self.__Login_Status = Login_Status

    @property
    def Person_Password(self):
        return self.__Person_Password
    @Person_Password.setter
    def Person_Password(self, Person_Password: Estring_Interface):
        self.__Person_Password = Person_Password

    @property
    def Person_ID(self):
        return self.__Person_ID
    @Person_ID.setter
    def Person_ID(self, Person_ID: Estring_Interface):
        self.__Person_ID = Person_ID

    @property
    def Session_manager_Person_111(self):
        return self.__Session_manager_Person_111
    @Session_manager_Person_111.setter
    def Session_manager_Person_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_online_shopping_Person__Session_manager_Person_111", None)
        self.__Session_manager_Person_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Session_manager_Person_010"):
                opp_val = getattr(old_value, "Session_manager_Person_010", None)
                if opp_val == self:
                    setattr(old_value, "Session_manager_Person_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Session_manager_Person_010"):
                opp_val = getattr(value, "Session_manager_Person_010", None)
                setattr(value, "Session_manager_Person_010", self)

