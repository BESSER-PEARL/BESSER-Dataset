from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Product_Item_Specification:

    def __init__(self, quantity: int, price: float, id: int, ItemSpecs__: str, Brand__: str, Item_Specification_Item_016: "Product_Item" = None):
        self.quantity = quantity
        self.price = price
        self.id = id
        self.ItemSpecs__ = ItemSpecs__
        self.Brand__ = Brand__
        self.Item_Specification_Item_016 = Item_Specification_Item_016
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ItemSpecs__(self):
        return self.__ItemSpecs__
    @ItemSpecs__.setter
    def ItemSpecs__(self, ItemSpecs__: str):
        self.__ItemSpecs__ = ItemSpecs__

    @property
    def Brand__(self):
        return self.__Brand__
    @Brand__.setter
    def Brand__(self, Brand__: str):
        self.__Brand__ = Brand__

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def Item_Specification_Item_016(self):
        return self.__Item_Specification_Item_016
    @Item_Specification_Item_016.setter
    def Item_Specification_Item_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item_Specification__Item_Specification_Item_016", None)
        self.__Item_Specification_Item_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item_Specification_Item_117"):
                opp_val = getattr(old_value, "Item_Specification_Item_117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item_Specification_Item_117"):
                opp_val = getattr(value, "Item_Specification_Item_117", None)
                if opp_val is None:
                    setattr(value, "Item_Specification_Item_117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Product_Item_Type:

    def __init__(self, quantity: int, price: float, id: int, ItemType__: str, Avail__: str, Item_Type_Item_018: "Product_Item" = None):
        self.quantity = quantity
        self.price = price
        self.id = id
        self.ItemType__ = ItemType__
        self.Avail__ = Avail__
        self.Item_Type_Item_018 = Item_Type_Item_018
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ItemType__(self):
        return self.__ItemType__
    @ItemType__.setter
    def ItemType__(self, ItemType__: str):
        self.__ItemType__ = ItemType__

    @property
    def Avail__(self):
        return self.__Avail__
    @Avail__.setter
    def Avail__(self, Avail__: str):
        self.__Avail__ = Avail__

    @property
    def Item_Type_Item_018(self):
        return self.__Item_Type_Item_018
    @Item_Type_Item_018.setter
    def Item_Type_Item_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item_Type__Item_Type_Item_018", None)
        self.__Item_Type_Item_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item_Type_Item_119"):
                opp_val = getattr(old_value, "Item_Type_Item_119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item_Type_Item_119"):
                opp_val = getattr(value, "Item_Type_Item_119", None)
                if opp_val is None:
                    setattr(value, "Item_Type_Item_119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Product_Item:

    def __init__(self, quantity: int, list__: float, id: int, OutofStock__: str, totalcost__: str, Item_Specification_Item_117: set["Product_Item_Specification"] = None, Item_Type_Item_119: set["Product_Item_Type"] = None, Item_ShoppingCart_020: "Cart_ShoppingCart" = None, GUI_Screen_Item_127: "GUI_Screen" = None):
        self.quantity = quantity
        self.list__ = list__
        self.id = id
        self.OutofStock__ = OutofStock__
        self.totalcost__ = totalcost__
        self.Item_Specification_Item_117 = Item_Specification_Item_117 if Item_Specification_Item_117 is not None else set()
        self.Item_Type_Item_119 = Item_Type_Item_119 if Item_Type_Item_119 is not None else set()
        self.Item_ShoppingCart_020 = Item_ShoppingCart_020
        self.GUI_Screen_Item_127 = GUI_Screen_Item_127
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def list__(self):
        return self.__list__
    @list__.setter
    def list__(self, list__: float):
        self.__list__ = list__

    @property
    def totalcost__(self):
        return self.__totalcost__
    @totalcost__.setter
    def totalcost__(self, totalcost__: str):
        self.__totalcost__ = totalcost__

    @property
    def OutofStock__(self):
        return self.__OutofStock__
    @OutofStock__.setter
    def OutofStock__(self, OutofStock__: str):
        self.__OutofStock__ = OutofStock__

    @property
    def Item_ShoppingCart_020(self):
        return self.__Item_ShoppingCart_020
    @Item_ShoppingCart_020.setter
    def Item_ShoppingCart_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item__Item_ShoppingCart_020", None)
        self.__Item_ShoppingCart_020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item_ShoppingCart_121"):
                opp_val = getattr(old_value, "Item_ShoppingCart_121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item_ShoppingCart_121"):
                opp_val = getattr(value, "Item_ShoppingCart_121", None)
                if opp_val is None:
                    setattr(value, "Item_ShoppingCart_121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Item_Type_Item_119(self):
        return self.__Item_Type_Item_119
    @Item_Type_Item_119.setter
    def Item_Type_Item_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item__Item_Type_Item_119", None)
        self.__Item_Type_Item_119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item_Type_Item_018"):
                    opp_val = getattr(item, "Item_Type_Item_018", None)
                    
                    if opp_val == self:
                        setattr(item, "Item_Type_Item_018", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item_Type_Item_018"):
                    opp_val = getattr(item, "Item_Type_Item_018", None)
                    
                    setattr(item, "Item_Type_Item_018", self)
                    

    @property
    def GUI_Screen_Item_127(self):
        return self.__GUI_Screen_Item_127
    @GUI_Screen_Item_127.setter
    def GUI_Screen_Item_127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item__GUI_Screen_Item_127", None)
        self.__GUI_Screen_Item_127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_Item_026"):
                opp_val = getattr(old_value, "GUI_Screen_Item_026", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_Item_026", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_Item_026"):
                opp_val = getattr(value, "GUI_Screen_Item_026", None)
                setattr(value, "GUI_Screen_Item_026", self)

    @property
    def Item_Specification_Item_117(self):
        return self.__Item_Specification_Item_117
    @Item_Specification_Item_117.setter
    def Item_Specification_Item_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product_Item__Item_Specification_Item_117", None)
        self.__Item_Specification_Item_117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item_Specification_Item_016"):
                    opp_val = getattr(item, "Item_Specification_Item_016", None)
                    
                    if opp_val == self:
                        setattr(item, "Item_Specification_Item_016", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item_Specification_Item_016"):
                    opp_val = getattr(item, "Item_Specification_Item_016", None)
                    
                    setattr(item, "Item_Specification_Item_016", self)
                    



class Cart_Checkout:

    def __init__(self, Paymentid: int, CheckoutID: int, billingMethod: str, CustomerID: str, PayBill__: Customer_Account, ShoppingCart_Checkout_111: "Cart_ShoppingCart" = None, Checkout_Payment_014: set["Customer_Payment1"] = None):
        self.Paymentid = Paymentid
        self.CheckoutID = CheckoutID
        self.billingMethod = billingMethod
        self.CustomerID = CustomerID
        self.PayBill__ = PayBill__
        self.ShoppingCart_Checkout_111 = ShoppingCart_Checkout_111
        self.Checkout_Payment_014 = Checkout_Payment_014 if Checkout_Payment_014 is not None else set()
        
        pass
    @property
    def PayBill__(self):
        return self.__PayBill__
    @PayBill__.setter
    def PayBill__(self, PayBill__: Customer_Account):
        self.__PayBill__ = PayBill__

    @property
    def billingMethod(self):
        return self.__billingMethod
    @billingMethod.setter
    def billingMethod(self, billingMethod: str):
        self.__billingMethod = billingMethod

    @property
    def CheckoutID(self):
        return self.__CheckoutID
    @CheckoutID.setter
    def CheckoutID(self, CheckoutID: int):
        self.__CheckoutID = CheckoutID

    @property
    def Paymentid(self):
        return self.__Paymentid
    @Paymentid.setter
    def Paymentid(self, Paymentid: int):
        self.__Paymentid = Paymentid

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: str):
        self.__CustomerID = CustomerID

    @property
    def ShoppingCart_Checkout_111(self):
        return self.__ShoppingCart_Checkout_111
    @ShoppingCart_Checkout_111.setter
    def ShoppingCart_Checkout_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_Checkout__ShoppingCart_Checkout_111", None)
        self.__ShoppingCart_Checkout_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Checkout_010"):
                opp_val = getattr(old_value, "ShoppingCart_Checkout_010", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Checkout_010"):
                opp_val = getattr(value, "ShoppingCart_Checkout_010", None)
                if opp_val is None:
                    setattr(value, "ShoppingCart_Checkout_010", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Checkout_Payment_014(self):
        return self.__Checkout_Payment_014
    @Checkout_Payment_014.setter
    def Checkout_Payment_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_Checkout__Checkout_Payment_014", None)
        self.__Checkout_Payment_014 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Checkout_Payment_115"):
                    opp_val = getattr(item, "Checkout_Payment_115", None)
                    
                    if opp_val == self:
                        setattr(item, "Checkout_Payment_115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Checkout_Payment_115"):
                    opp_val = getattr(item, "Checkout_Payment_115", None)
                    
                    setattr(item, "Checkout_Payment_115", self)
                    



class Cart_ShoppingCart:

    def __init__(self, id: int, creationDate: date, CheckoutID: int, AddCart: int, RemoveOrder: int, UpdateOrder: int, GetTotal__: float, ShoppingCart_Checkout_010: set["Cart_Checkout"] = None, ShoppingCart_Customer_012: "Customer_Customer1" = None, Item_ShoppingCart_121: set["Product_Item"] = None, GUI_Screen_ShoppingCart_125: "GUI_Screen" = None):
        self.id = id
        self.creationDate = creationDate
        self.CheckoutID = CheckoutID
        self.AddCart = AddCart
        self.RemoveOrder = RemoveOrder
        self.UpdateOrder = UpdateOrder
        self.GetTotal__ = GetTotal__
        self.ShoppingCart_Checkout_010 = ShoppingCart_Checkout_010 if ShoppingCart_Checkout_010 is not None else set()
        self.ShoppingCart_Customer_012 = ShoppingCart_Customer_012
        self.Item_ShoppingCart_121 = Item_ShoppingCart_121 if Item_ShoppingCart_121 is not None else set()
        self.GUI_Screen_ShoppingCart_125 = GUI_Screen_ShoppingCart_125
        
        pass
    @property
    def UpdateOrder(self):
        return self.__UpdateOrder
    @UpdateOrder.setter
    def UpdateOrder(self, UpdateOrder: int):
        self.__UpdateOrder = UpdateOrder

    @property
    def RemoveOrder(self):
        return self.__RemoveOrder
    @RemoveOrder.setter
    def RemoveOrder(self, RemoveOrder: int):
        self.__RemoveOrder = RemoveOrder

    @property
    def AddCart(self):
        return self.__AddCart
    @AddCart.setter
    def AddCart(self, AddCart: int):
        self.__AddCart = AddCart

    @property
    def GetTotal__(self):
        return self.__GetTotal__
    @GetTotal__.setter
    def GetTotal__(self, GetTotal__: float):
        self.__GetTotal__ = GetTotal__

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def CheckoutID(self):
        return self.__CheckoutID
    @CheckoutID.setter
    def CheckoutID(self, CheckoutID: int):
        self.__CheckoutID = CheckoutID

    @property
    def ShoppingCart_Checkout_010(self):
        return self.__ShoppingCart_Checkout_010
    @ShoppingCart_Checkout_010.setter
    def ShoppingCart_Checkout_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_ShoppingCart__ShoppingCart_Checkout_010", None)
        self.__ShoppingCart_Checkout_010 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ShoppingCart_Checkout_111"):
                    opp_val = getattr(item, "ShoppingCart_Checkout_111", None)
                    
                    if opp_val == self:
                        setattr(item, "ShoppingCart_Checkout_111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ShoppingCart_Checkout_111"):
                    opp_val = getattr(item, "ShoppingCart_Checkout_111", None)
                    
                    setattr(item, "ShoppingCart_Checkout_111", self)
                    

    @property
    def ShoppingCart_Customer_012(self):
        return self.__ShoppingCart_Customer_012
    @ShoppingCart_Customer_012.setter
    def ShoppingCart_Customer_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_ShoppingCart__ShoppingCart_Customer_012", None)
        self.__ShoppingCart_Customer_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Customer_113"):
                opp_val = getattr(old_value, "ShoppingCart_Customer_113", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_Customer_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Customer_113"):
                opp_val = getattr(value, "ShoppingCart_Customer_113", None)
                setattr(value, "ShoppingCart_Customer_113", self)

    @property
    def Item_ShoppingCart_121(self):
        return self.__Item_ShoppingCart_121
    @Item_ShoppingCart_121.setter
    def Item_ShoppingCart_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_ShoppingCart__Item_ShoppingCart_121", None)
        self.__Item_ShoppingCart_121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item_ShoppingCart_020"):
                    opp_val = getattr(item, "Item_ShoppingCart_020", None)
                    
                    if opp_val == self:
                        setattr(item, "Item_ShoppingCart_020", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item_ShoppingCart_020"):
                    opp_val = getattr(item, "Item_ShoppingCart_020", None)
                    
                    setattr(item, "Item_ShoppingCart_020", self)
                    

    @property
    def GUI_Screen_ShoppingCart_125(self):
        return self.__GUI_Screen_ShoppingCart_125
    @GUI_Screen_ShoppingCart_125.setter
    def GUI_Screen_ShoppingCart_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart_ShoppingCart__GUI_Screen_ShoppingCart_125", None)
        self.__GUI_Screen_ShoppingCart_125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_ShoppingCart_024"):
                opp_val = getattr(old_value, "GUI_Screen_ShoppingCart_024", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_ShoppingCart_024", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_ShoppingCart_024"):
                opp_val = getattr(value, "GUI_Screen_ShoppingCart_024", None)
                setattr(value, "GUI_Screen_ShoppingCart_024", self)



class Customer_Payment1:

    def __init__(self, PayBill__: str, Auth__: bool, ID: Customer_Account, Payment_Customer_08: set["Customer_Customer1"] = None, Checkout_Payment_115: "Cart_Checkout" = None):
        self.PayBill__ = PayBill__
        self.Auth__ = Auth__
        self.ID = ID
        self.Payment_Customer_08 = Payment_Customer_08 if Payment_Customer_08 is not None else set()
        self.Checkout_Payment_115 = Checkout_Payment_115
        
        pass
    @property
    def Auth__(self):
        return self.__Auth__
    @Auth__.setter
    def Auth__(self, Auth__: bool):
        self.__Auth__ = Auth__

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: Customer_Account):
        self.__ID = ID

    @property
    def PayBill__(self):
        return self.__PayBill__
    @PayBill__.setter
    def PayBill__(self, PayBill__: str):
        self.__PayBill__ = PayBill__

    @property
    def Checkout_Payment_115(self):
        return self.__Checkout_Payment_115
    @Checkout_Payment_115.setter
    def Checkout_Payment_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Payment1__Checkout_Payment_115", None)
        self.__Checkout_Payment_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Checkout_Payment_014"):
                opp_val = getattr(old_value, "Checkout_Payment_014", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Checkout_Payment_014"):
                opp_val = getattr(value, "Checkout_Payment_014", None)
                if opp_val is None:
                    setattr(value, "Checkout_Payment_014", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Payment_Customer_08(self):
        return self.__Payment_Customer_08
    @Payment_Customer_08.setter
    def Payment_Customer_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Payment1__Payment_Customer_08", None)
        self.__Payment_Customer_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Payment_Customer_19"):
                    opp_val = getattr(item, "Payment_Customer_19", None)
                    
                    if opp_val == self:
                        setattr(item, "Payment_Customer_19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Payment_Customer_19"):
                    opp_val = getattr(item, "Payment_Customer_19", None)
                    
                    setattr(item, "Payment_Customer_19", self)
                    



class Customer_Account:

    def __init__(self, Login__: str, account__: str, GUI_Screen_Account_123: "GUI_Screen" = None):
        self.Login__ = Login__
        self.account__ = account__
        self.GUI_Screen_Account_123 = GUI_Screen_Account_123
        
        pass
    @property
    def account__(self):
        return self.__account__
    @account__.setter
    def account__(self, account__: str):
        self.__account__ = account__

    @property
    def Login__(self):
        return self.__Login__
    @Login__.setter
    def Login__(self, Login__: str):
        self.__Login__ = Login__

    @property
    def GUI_Screen_Account_123(self):
        return self.__GUI_Screen_Account_123
    @GUI_Screen_Account_123.setter
    def GUI_Screen_Account_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Account__GUI_Screen_Account_123", None)
        self.__GUI_Screen_Account_123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_Account_022"):
                opp_val = getattr(old_value, "GUI_Screen_Account_022", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_Account_022", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_Account_022"):
                opp_val = getattr(value, "GUI_Screen_Account_022", None)
                setattr(value, "GUI_Screen_Account_022", self)



class Customer_User:

    def __init__(self, Addresschange__: str, userid__: str):
        self.Addresschange__ = Addresschange__
        self.userid__ = userid__
        
        pass
    @property
    def Addresschange__(self):
        return self.__Addresschange__
    @Addresschange__.setter
    def Addresschange__(self, Addresschange__: str):
        self.__Addresschange__ = Addresschange__

    @property
    def userid__(self):
        return self.__userid__
    @userid__.setter
    def userid__(self, userid__: str):
        self.__userid__ = userid__



class Customer_Customer1:

    def __init__(self, userId: str, PaymentMet__: float, Account__: str, select__: str, Payment_Customer_19: "Customer_Payment1" = None, ShoppingCart_Customer_113: "Cart_ShoppingCart" = None):
        self.userId = userId
        self.PaymentMet__ = PaymentMet__
        self.Account__ = Account__
        self.select__ = select__
        self.Payment_Customer_19 = Payment_Customer_19
        self.ShoppingCart_Customer_113 = ShoppingCart_Customer_113
        
        pass
    @property
    def Account__(self):
        return self.__Account__
    @Account__.setter
    def Account__(self, Account__: str):
        self.__Account__ = Account__

    @property
    def PaymentMet__(self):
        return self.__PaymentMet__
    @PaymentMet__.setter
    def PaymentMet__(self, PaymentMet__: float):
        self.__PaymentMet__ = PaymentMet__

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def select__(self):
        return self.__select__
    @select__.setter
    def select__(self, select__: str):
        self.__select__ = select__

    @property
    def Payment_Customer_19(self):
        return self.__Payment_Customer_19
    @Payment_Customer_19.setter
    def Payment_Customer_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Customer1__Payment_Customer_19", None)
        self.__Payment_Customer_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment_Customer_08"):
                opp_val = getattr(old_value, "Payment_Customer_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment_Customer_08"):
                opp_val = getattr(value, "Payment_Customer_08", None)
                if opp_val is None:
                    setattr(value, "Payment_Customer_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ShoppingCart_Customer_113(self):
        return self.__ShoppingCart_Customer_113
    @ShoppingCart_Customer_113.setter
    def ShoppingCart_Customer_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Customer1__ShoppingCart_Customer_113", None)
        self.__ShoppingCart_Customer_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Customer_012"):
                opp_val = getattr(old_value, "ShoppingCart_Customer_012", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_Customer_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Customer_012"):
                opp_val = getattr(value, "ShoppingCart_Customer_012", None)
                setattr(value, "ShoppingCart_Customer_012", self)



class Shopping_Cart_Checkout:

    def __init__(self, Paymentid: int, CheckoutID: int, billingMethod: str, CustomerID: str, Checkout__: float, Payment_Checkout_15: set["Customer_Payment"] = None, ShoppingCart_Checkout_17: "Shopping_Cart_ShoppingCart" = None):
        self.Paymentid = Paymentid
        self.CheckoutID = CheckoutID
        self.billingMethod = billingMethod
        self.CustomerID = CustomerID
        self.Checkout__ = Checkout__
        self.Payment_Checkout_15 = Payment_Checkout_15 if Payment_Checkout_15 is not None else set()
        self.ShoppingCart_Checkout_17 = ShoppingCart_Checkout_17
        
        pass
    @property
    def CheckoutID(self):
        return self.__CheckoutID
    @CheckoutID.setter
    def CheckoutID(self, CheckoutID: int):
        self.__CheckoutID = CheckoutID

    @property
    def Checkout__(self):
        return self.__Checkout__
    @Checkout__.setter
    def Checkout__(self, Checkout__: float):
        self.__Checkout__ = Checkout__

    @property
    def billingMethod(self):
        return self.__billingMethod
    @billingMethod.setter
    def billingMethod(self, billingMethod: str):
        self.__billingMethod = billingMethod

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: str):
        self.__CustomerID = CustomerID

    @property
    def Paymentid(self):
        return self.__Paymentid
    @Paymentid.setter
    def Paymentid(self, Paymentid: int):
        self.__Paymentid = Paymentid

    @property
    def Payment_Checkout_15(self):
        return self.__Payment_Checkout_15
    @Payment_Checkout_15.setter
    def Payment_Checkout_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart_Checkout__Payment_Checkout_15", None)
        self.__Payment_Checkout_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Payment_Checkout_04"):
                    opp_val = getattr(item, "Payment_Checkout_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Payment_Checkout_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Payment_Checkout_04"):
                    opp_val = getattr(item, "Payment_Checkout_04", None)
                    
                    setattr(item, "Payment_Checkout_04", self)
                    

    @property
    def ShoppingCart_Checkout_17(self):
        return self.__ShoppingCart_Checkout_17
    @ShoppingCart_Checkout_17.setter
    def ShoppingCart_Checkout_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart_Checkout__ShoppingCart_Checkout_17", None)
        self.__ShoppingCart_Checkout_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Checkout_06"):
                opp_val = getattr(old_value, "ShoppingCart_Checkout_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Checkout_06"):
                opp_val = getattr(value, "ShoppingCart_Checkout_06", None)
                if opp_val is None:
                    setattr(value, "ShoppingCart_Checkout_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Shopping_Cart_ShoppingCart:

    def __init__(self, id: int, creationDate: date, CheckoutID: int, AddOrder: int, RemoveOrder: int, UpdateOrder: int, GetTotal__: float, Customer_ShoppingCart_13: "Customer_Customer" = None, ShoppingCart_Checkout_06: set["Shopping_Cart_Checkout"] = None):
        self.id = id
        self.creationDate = creationDate
        self.CheckoutID = CheckoutID
        self.AddOrder = AddOrder
        self.RemoveOrder = RemoveOrder
        self.UpdateOrder = UpdateOrder
        self.GetTotal__ = GetTotal__
        self.Customer_ShoppingCart_13 = Customer_ShoppingCart_13
        self.ShoppingCart_Checkout_06 = ShoppingCart_Checkout_06 if ShoppingCart_Checkout_06 is not None else set()
        
        pass
    @property
    def GetTotal__(self):
        return self.__GetTotal__
    @GetTotal__.setter
    def GetTotal__(self, GetTotal__: float):
        self.__GetTotal__ = GetTotal__

    @property
    def AddOrder(self):
        return self.__AddOrder
    @AddOrder.setter
    def AddOrder(self, AddOrder: int):
        self.__AddOrder = AddOrder

    @property
    def RemoveOrder(self):
        return self.__RemoveOrder
    @RemoveOrder.setter
    def RemoveOrder(self, RemoveOrder: int):
        self.__RemoveOrder = RemoveOrder

    @property
    def CheckoutID(self):
        return self.__CheckoutID
    @CheckoutID.setter
    def CheckoutID(self, CheckoutID: int):
        self.__CheckoutID = CheckoutID

    @property
    def UpdateOrder(self):
        return self.__UpdateOrder
    @UpdateOrder.setter
    def UpdateOrder(self, UpdateOrder: int):
        self.__UpdateOrder = UpdateOrder

    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ShoppingCart_Checkout_06(self):
        return self.__ShoppingCart_Checkout_06
    @ShoppingCart_Checkout_06.setter
    def ShoppingCart_Checkout_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart_ShoppingCart__ShoppingCart_Checkout_06", None)
        self.__ShoppingCart_Checkout_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ShoppingCart_Checkout_17"):
                    opp_val = getattr(item, "ShoppingCart_Checkout_17", None)
                    
                    if opp_val == self:
                        setattr(item, "ShoppingCart_Checkout_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ShoppingCart_Checkout_17"):
                    opp_val = getattr(item, "ShoppingCart_Checkout_17", None)
                    
                    setattr(item, "ShoppingCart_Checkout_17", self)
                    

    @property
    def Customer_ShoppingCart_13(self):
        return self.__Customer_ShoppingCart_13
    @Customer_ShoppingCart_13.setter
    def Customer_ShoppingCart_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart_ShoppingCart__Customer_ShoppingCart_13", None)
        self.__Customer_ShoppingCart_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_02"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_02", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_02"):
                opp_val = getattr(value, "Customer_ShoppingCart_02", None)
                setattr(value, "Customer_ShoppingCart_02", self)



class Customer_Payment:

    def __init__(self, Paymentid: int, login: str, ApplPay: int, CustomerId: str, PayPal: int, Payment__: float, Payment_Customer_00: "Customer_Customer" = None, Payment_Checkout_04: "Shopping_Cart_Checkout" = None):
        self.Paymentid = Paymentid
        self.login = login
        self.ApplPay = ApplPay
        self.CustomerId = CustomerId
        self.PayPal = PayPal
        self.Payment__ = Payment__
        self.Payment_Customer_00 = Payment_Customer_00
        self.Payment_Checkout_04 = Payment_Checkout_04
        
        pass
    @property
    def Paymentid(self):
        return self.__Paymentid
    @Paymentid.setter
    def Paymentid(self, Paymentid: int):
        self.__Paymentid = Paymentid

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def ApplPay(self):
        return self.__ApplPay
    @ApplPay.setter
    def ApplPay(self, ApplPay: int):
        self.__ApplPay = ApplPay

    @property
    def PayPal(self):
        return self.__PayPal
    @PayPal.setter
    def PayPal(self, PayPal: int):
        self.__PayPal = PayPal

    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: str):
        self.__CustomerId = CustomerId

    @property
    def Payment__(self):
        return self.__Payment__
    @Payment__.setter
    def Payment__(self, Payment__: float):
        self.__Payment__ = Payment__

    @property
    def Payment_Checkout_04(self):
        return self.__Payment_Checkout_04
    @Payment_Checkout_04.setter
    def Payment_Checkout_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Payment__Payment_Checkout_04", None)
        self.__Payment_Checkout_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment_Checkout_15"):
                opp_val = getattr(old_value, "Payment_Checkout_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment_Checkout_15"):
                opp_val = getattr(value, "Payment_Checkout_15", None)
                if opp_val is None:
                    setattr(value, "Payment_Checkout_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Payment_Customer_00(self):
        return self.__Payment_Customer_00
    @Payment_Customer_00.setter
    def Payment_Customer_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Payment__Payment_Customer_00", None)
        self.__Payment_Customer_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment_Customer_11"):
                opp_val = getattr(old_value, "Payment_Customer_11", None)
                if opp_val == self:
                    setattr(old_value, "Payment_Customer_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment_Customer_11"):
                opp_val = getattr(value, "Payment_Customer_11", None)
                setattr(value, "Payment_Customer_11", self)



class Customer_Customer:

    def __init__(self, firstname: str, lastname: str, emailAddress: str, id: int, login: str, password: str, Message: str, Payment_Customer_11: "Customer_Payment" = None, Customer_ShoppingCart_02: "Shopping_Cart_ShoppingCart" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.emailAddress = emailAddress
        self.id = id
        self.login = login
        self.password = password
        self.Message = Message
        self.Payment_Customer_11 = Payment_Customer_11
        self.Customer_ShoppingCart_02 = Customer_ShoppingCart_02
        
        pass
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def Message(self):
        return self.__Message
    @Message.setter
    def Message(self, Message: str):
        self.__Message = Message

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def Payment_Customer_11(self):
        return self.__Payment_Customer_11
    @Payment_Customer_11.setter
    def Payment_Customer_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Customer__Payment_Customer_11", None)
        self.__Payment_Customer_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment_Customer_00"):
                opp_val = getattr(old_value, "Payment_Customer_00", None)
                if opp_val == self:
                    setattr(old_value, "Payment_Customer_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment_Customer_00"):
                opp_val = getattr(value, "Payment_Customer_00", None)
                setattr(value, "Payment_Customer_00", self)

    @property
    def Customer_ShoppingCart_02(self):
        return self.__Customer_ShoppingCart_02
    @Customer_ShoppingCart_02.setter
    def Customer_ShoppingCart_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Customer__Customer_ShoppingCart_02", None)
        self.__Customer_ShoppingCart_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_13"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_13", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_13"):
                opp_val = getattr(value, "Customer_ShoppingCart_13", None)
                setattr(value, "Customer_ShoppingCart_13", self)



class GUI_Screen:

    def __init__(self, id: int, Message: str, Exit__: str, Error__: str, DisplayList__: int, GUI_Screen_Account_022: "Customer_Account" = None, GUI_Screen_ShoppingCart_024: "Cart_ShoppingCart" = None, GUI_Screen_Item_026: "Product_Item" = None):
        self.id = id
        self.Message = Message
        self.Exit__ = Exit__
        self.Error__ = Error__
        self.DisplayList__ = DisplayList__
        self.GUI_Screen_Account_022 = GUI_Screen_Account_022
        self.GUI_Screen_ShoppingCart_024 = GUI_Screen_ShoppingCart_024
        self.GUI_Screen_Item_026 = GUI_Screen_Item_026
        
        pass
    @property
    def DisplayList__(self):
        return self.__DisplayList__
    @DisplayList__.setter
    def DisplayList__(self, DisplayList__: int):
        self.__DisplayList__ = DisplayList__

    @property
    def Message(self):
        return self.__Message
    @Message.setter
    def Message(self, Message: str):
        self.__Message = Message

    @property
    def Exit__(self):
        return self.__Exit__
    @Exit__.setter
    def Exit__(self, Exit__: str):
        self.__Exit__ = Exit__

    @property
    def Error__(self):
        return self.__Error__
    @Error__.setter
    def Error__(self, Error__: str):
        self.__Error__ = Error__

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def GUI_Screen_Account_022(self):
        return self.__GUI_Screen_Account_022
    @GUI_Screen_Account_022.setter
    def GUI_Screen_Account_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI_Screen__GUI_Screen_Account_022", None)
        self.__GUI_Screen_Account_022 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_Account_123"):
                opp_val = getattr(old_value, "GUI_Screen_Account_123", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_Account_123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_Account_123"):
                opp_val = getattr(value, "GUI_Screen_Account_123", None)
                setattr(value, "GUI_Screen_Account_123", self)

    @property
    def GUI_Screen_Item_026(self):
        return self.__GUI_Screen_Item_026
    @GUI_Screen_Item_026.setter
    def GUI_Screen_Item_026(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI_Screen__GUI_Screen_Item_026", None)
        self.__GUI_Screen_Item_026 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_Item_127"):
                opp_val = getattr(old_value, "GUI_Screen_Item_127", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_Item_127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_Item_127"):
                opp_val = getattr(value, "GUI_Screen_Item_127", None)
                setattr(value, "GUI_Screen_Item_127", self)

    @property
    def GUI_Screen_ShoppingCart_024(self):
        return self.__GUI_Screen_ShoppingCart_024
    @GUI_Screen_ShoppingCart_024.setter
    def GUI_Screen_ShoppingCart_024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI_Screen__GUI_Screen_ShoppingCart_024", None)
        self.__GUI_Screen_ShoppingCart_024 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GUI_Screen_ShoppingCart_125"):
                opp_val = getattr(old_value, "GUI_Screen_ShoppingCart_125", None)
                if opp_val == self:
                    setattr(old_value, "GUI_Screen_ShoppingCart_125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GUI_Screen_ShoppingCart_125"):
                opp_val = getattr(value, "GUI_Screen_ShoppingCart_125", None)
                setattr(value, "GUI_Screen_ShoppingCart_125", self)

