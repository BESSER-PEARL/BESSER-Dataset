from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Special_order_UseCase:

    pass


class Register_UseCase:

    pass


class Update_Order_UseCase:

    pass


class Generate_Reports_UseCase:

    pass


class Manage_Orders_UseCase:

    pass


class Place_Order_UseCase:

    pass


class Update_Stock_UseCase:

    pass


class Manage_customer_accounts_UseCase:

    pass


class Login_UseCase:

    pass


class Manager_Actor:

    pass


class Customer_Actor:

    pass





class Manager1:

    def __init__(self, id: str, name: str, stock33: set["Stock1"] = None, order35: set["Order1"] = None):
        self.id = id
        self.name = name
        self.stock33 = stock33 if stock33 is not None else set()
        self.order35 = order35 if order35 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stock33(self):
        return self.__stock33
    @stock33.setter
    def stock33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager1__stock33", None)
        self.__stock33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager32"):
                    opp_val = getattr(item, "manager32", None)
                    
                    if opp_val == self:
                        setattr(item, "manager32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager32"):
                    opp_val = getattr(item, "manager32", None)
                    
                    setattr(item, "manager32", self)
                    

    @property
    def order35(self):
        return self.__order35
    @order35.setter
    def order35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager1__order35", None)
        self.__order35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager34"):
                    opp_val = getattr(item, "manager34", None)
                    
                    if opp_val == self:
                        setattr(item, "manager34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager34"):
                    opp_val = getattr(item, "manager34", None)
                    
                    setattr(item, "manager34", self)
                    



class SpecialOrder:

    def __init__(self, orderRange: int, offerCode: int):
        self.orderRange = orderRange
        self.offerCode = offerCode
        
        pass
    @property
    def orderRange(self):
        return self.__orderRange
    @orderRange.setter
    def orderRange(self, orderRange: int):
        self.__orderRange = orderRange

    @property
    def offerCode(self):
        return self.__offerCode
    @offerCode.setter
    def offerCode(self, offerCode: int):
        self.__offerCode = offerCode



class Stock1:

    def __init__(self, items__: Item, item29: set["Item1"] = None, manager32: "Manager1" = None):
        self.items__ = items__
        self.item29 = item29 if item29 is not None else set()
        self.manager32 = manager32
        
        pass
    @property
    def items__(self):
        return self.__items__
    @items__.setter
    def items__(self, items__: Item):
        self.__items__ = items__

    @property
    def item29(self):
        return self.__item29
    @item29.setter
    def item29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock1__item29", None)
        self.__item29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stock28"):
                    opp_val = getattr(item, "stock28", None)
                    
                    if opp_val == self:
                        setattr(item, "stock28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stock28"):
                    opp_val = getattr(item, "stock28", None)
                    
                    setattr(item, "stock28", self)
                    

    @property
    def manager32(self):
        return self.__manager32
    @manager32.setter
    def manager32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock1__manager32", None)
        self.__manager32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stock33"):
                opp_val = getattr(old_value, "stock33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stock33"):
                opp_val = getattr(value, "stock33", None)
                if opp_val is None:
                    setattr(value, "stock33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Item1:

    def __init__(self, itemCode: int, itemName: str, itemCost: float, itemCount: str, stock28: "Stock1" = None):
        self.itemCode = itemCode
        self.itemName = itemName
        self.itemCost = itemCost
        self.itemCount = itemCount
        self.stock28 = stock28
        
        pass
    @property
    def itemName(self):
        return self.__itemName
    @itemName.setter
    def itemName(self, itemName: str):
        self.__itemName = itemName

    @property
    def itemCount(self):
        return self.__itemCount
    @itemCount.setter
    def itemCount(self, itemCount: str):
        self.__itemCount = itemCount

    @property
    def itemCode(self):
        return self.__itemCode
    @itemCode.setter
    def itemCode(self, itemCode: int):
        self.__itemCode = itemCode

    @property
    def itemCost(self):
        return self.__itemCost
    @itemCost.setter
    def itemCost(self, itemCost: float):
        self.__itemCost = itemCost

    @property
    def stock28(self):
        return self.__stock28
    @stock28.setter
    def stock28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item1__stock28", None)
        self.__stock28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item29"):
                opp_val = getattr(old_value, "item29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item29"):
                opp_val = getattr(value, "item29", None)
                if opp_val is None:
                    setattr(value, "item29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order1:

    def __init__(self, orderId: int, cust: Customer_Actor, orderDate: str, deliveryDate: str, totalAmount: float, conformationNo: int, customer27: "Customer1" = None, manager34: "Manager1" = None):
        self.orderId = orderId
        self.cust = cust
        self.orderDate = orderDate
        self.deliveryDate = deliveryDate
        self.totalAmount = totalAmount
        self.conformationNo = conformationNo
        self.customer27 = customer27
        self.manager34 = manager34
        
        pass
    @property
    def orderId(self):
        return self.__orderId
    @orderId.setter
    def orderId(self, orderId: int):
        self.__orderId = orderId

    @property
    def conformationNo(self):
        return self.__conformationNo
    @conformationNo.setter
    def conformationNo(self, conformationNo: int):
        self.__conformationNo = conformationNo

    @property
    def cust(self):
        return self.__cust
    @cust.setter
    def cust(self, cust: Customer_Actor):
        self.__cust = cust

    @property
    def totalAmount(self):
        return self.__totalAmount
    @totalAmount.setter
    def totalAmount(self, totalAmount: float):
        self.__totalAmount = totalAmount

    @property
    def orderDate(self):
        return self.__orderDate
    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def deliveryDate(self):
        return self.__deliveryDate
    @deliveryDate.setter
    def deliveryDate(self, deliveryDate: str):
        self.__deliveryDate = deliveryDate

    @property
    def manager34(self):
        return self.__manager34
    @manager34.setter
    def manager34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order1__manager34", None)
        self.__manager34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order35"):
                opp_val = getattr(old_value, "order35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order35"):
                opp_val = getattr(value, "order35", None)
                if opp_val is None:
                    setattr(value, "order35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer27(self):
        return self.__customer27
    @customer27.setter
    def customer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order1__customer27", None)
        self.__customer27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order26"):
                opp_val = getattr(old_value, "order26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order26"):
                opp_val = getattr(value, "order26", None)
                if opp_val is None:
                    setattr(value, "order26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer1:

    def __init__(self, name: str, customerId: int, address: str, phone: int, order26: set["Order1"] = None):
        self.name = name
        self.customerId = customerId
        self.address = address
        self.phone = phone
        self.order26 = order26 if order26 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def customerId(self):
        return self.__customerId
    @customerId.setter
    def customerId(self, customerId: int):
        self.__customerId = customerId

    @property
    def order26(self):
        return self.__order26
    @order26.setter
    def order26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__order26", None)
        self.__order26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer27"):
                    opp_val = getattr(item, "customer27", None)
                    
                    if opp_val == self:
                        setattr(item, "customer27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer27"):
                    opp_val = getattr(item, "customer27", None)
                    
                    setattr(item, "customer27", self)
                    



class Manager:

    def __init__(self, name: str, order22: set["Order"] = None, stock24: set["Stock"] = None):
        self.name = name
        self.order22 = order22 if order22 is not None else set()
        self.stock24 = stock24 if stock24 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def order22(self):
        return self.__order22
    @order22.setter
    def order22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__order22", None)
        self.__order22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager23"):
                    opp_val = getattr(item, "manager23", None)
                    
                    if opp_val == self:
                        setattr(item, "manager23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager23"):
                    opp_val = getattr(item, "manager23", None)
                    
                    setattr(item, "manager23", self)
                    

    @property
    def stock24(self):
        return self.__stock24
    @stock24.setter
    def stock24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__stock24", None)
        self.__stock24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager25"):
                    opp_val = getattr(item, "manager25", None)
                    
                    if opp_val == self:
                        setattr(item, "manager25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager25"):
                    opp_val = getattr(item, "manager25", None)
                    
                    setattr(item, "manager25", self)
                    



class Stock:

    def __init__(self, items__: Item, item21: set["Item"] = None, manager25: "Manager" = None):
        self.items__ = items__
        self.item21 = item21 if item21 is not None else set()
        self.manager25 = manager25
        
        pass
    @property
    def items__(self):
        return self.__items__
    @items__.setter
    def items__(self, items__: Item):
        self.__items__ = items__

    @property
    def item21(self):
        return self.__item21
    @item21.setter
    def item21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock__item21", None)
        self.__item21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stock20"):
                    opp_val = getattr(item, "stock20", None)
                    
                    if opp_val == self:
                        setattr(item, "stock20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stock20"):
                    opp_val = getattr(item, "stock20", None)
                    
                    setattr(item, "stock20", self)
                    

    @property
    def manager25(self):
        return self.__manager25
    @manager25.setter
    def manager25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock__manager25", None)
        self.__manager25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stock24"):
                opp_val = getattr(old_value, "stock24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stock24"):
                opp_val = getattr(value, "stock24", None)
                if opp_val is None:
                    setattr(value, "stock24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Item:

    def __init__(self, item_code: int, item_name: str, order31: set["Order"] = None, stock20: "Stock" = None):
        self.item_code = item_code
        self.item_name = item_name
        self.order31 = order31 if order31 is not None else set()
        self.stock20 = stock20
        
        pass
    @property
    def item_code(self):
        return self.__item_code
    @item_code.setter
    def item_code(self, item_code: int):
        self.__item_code = item_code

    @property
    def item_name(self):
        return self.__item_name
    @item_name.setter
    def item_name(self, item_name: str):
        self.__item_name = item_name

    @property
    def stock20(self):
        return self.__stock20
    @stock20.setter
    def stock20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__stock20", None)
        self.__stock20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item21"):
                opp_val = getattr(old_value, "item21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item21"):
                opp_val = getattr(value, "item21", None)
                if opp_val is None:
                    setattr(value, "item21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order31(self):
        return self.__order31
    @order31.setter
    def order31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Item__order31", None)
        self.__order31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "item30"):
                    opp_val = getattr(item, "item30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "item30"):
                    opp_val = getattr(item, "item30", None)
                    
                    if opp_val is None:
                        setattr(item, "item30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Order:

    def __init__(self, Order_id: int, Cust_id: int, Customer_Order_11: "Customer" = None, item30: set["Item"] = None, manager23: "Manager" = None):
        self.Order_id = Order_id
        self.Cust_id = Cust_id
        self.Customer_Order_11 = Customer_Order_11
        self.item30 = item30 if item30 is not None else set()
        self.manager23 = manager23
        
        pass
    @property
    def Cust_id(self):
        return self.__Cust_id
    @Cust_id.setter
    def Cust_id(self, Cust_id: int):
        self.__Cust_id = Cust_id

    @property
    def Order_id(self):
        return self.__Order_id
    @Order_id.setter
    def Order_id(self, Order_id: int):
        self.__Order_id = Order_id

    @property
    def manager23(self):
        return self.__manager23
    @manager23.setter
    def manager23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__manager23", None)
        self.__manager23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order22"):
                opp_val = getattr(old_value, "order22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order22"):
                opp_val = getattr(value, "order22", None)
                if opp_val is None:
                    setattr(value, "order22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer_Order_11(self):
        return self.__Customer_Order_11
    @Customer_Order_11.setter
    def Customer_Order_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__Customer_Order_11", None)
        self.__Customer_Order_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Order_00"):
                opp_val = getattr(old_value, "Customer_Order_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Order_00"):
                opp_val = getattr(value, "Customer_Order_00", None)
                if opp_val is None:
                    setattr(value, "Customer_Order_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def item30(self):
        return self.__item30
    @item30.setter
    def item30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__item30", None)
        self.__item30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order31"):
                    opp_val = getattr(item, "order31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order31"):
                    opp_val = getattr(item, "order31", None)
                    
                    if opp_val is None:
                        setattr(item, "order31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, name: str, Customer_id: int, Customer_Order_00: set["Order"] = None):
        self.name = name
        self.Customer_id = Customer_id
        self.Customer_Order_00 = Customer_Order_00 if Customer_Order_00 is not None else set()
        
        pass
    @property
    def Customer_id(self):
        return self.__Customer_id
    @Customer_id.setter
    def Customer_id(self, Customer_id: int):
        self.__Customer_id = Customer_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Customer_Order_00(self):
        return self.__Customer_Order_00
    @Customer_Order_00.setter
    def Customer_Order_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Order_00", None)
        self.__Customer_Order_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Order_11"):
                    opp_val = getattr(item, "Customer_Order_11", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Order_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Order_11"):
                    opp_val = getattr(item, "Customer_Order_11", None)
                    
                    setattr(item, "Customer_Order_11", self)
                    

