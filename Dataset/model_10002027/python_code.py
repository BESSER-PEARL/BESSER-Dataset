from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, phoneNumber: int, name: str, customerID: int, store4: "Store" = None, order6: set["Order"] = None):
        self.phoneNumber = phoneNumber
        self.name = name
        self.customerID = customerID
        self.store4 = store4
        self.order6 = order6 if order6 is not None else set()
        
        pass
    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def store4(self):
        return self.__store4
    @store4.setter
    def store4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__store4", None)
        self.__store4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                if opp_val is None:
                    setattr(value, "customer5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order6(self):
        return self.__order6
    @order6.setter
    def order6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order6", None)
        self.__order6 = value if value is not None else set()
        
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
                    



class Appliance:

    def __init__(self, Price: str, Brand: str, Model: str, Stock: int, store9: "Store" = None, order13: "Order" = None):
        self.Price = Price
        self.Brand = Brand
        self.Model = Model
        self.Stock = Stock
        self.store9 = store9
        self.order13 = order13
        
        pass
    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def Stock(self, Stock: int):
        self.__Stock = Stock

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Model(self):
        return self.__Model
    @Model.setter
    def Model(self, Model: str):
        self.__Model = Model

    @property
    def Brand(self):
        return self.__Brand
    @Brand.setter
    def Brand(self, Brand: str):
        self.__Brand = Brand

    @property
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appliance__order13", None)
        self.__order13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appliance212"):
                opp_val = getattr(old_value, "appliance212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appliance212"):
                opp_val = getattr(value, "appliance212", None)
                if opp_val is None:
                    setattr(value, "appliance212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def store9(self):
        return self.__store9
    @store9.setter
    def store9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appliance__store9", None)
        self.__store9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appliance8"):
                opp_val = getattr(old_value, "appliance8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appliance8"):
                opp_val = getattr(value, "appliance8", None)
                if opp_val is None:
                    setattr(value, "appliance8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class OrderList:

    def __init__(self, orderList: Order, store3: "Store" = None, order15: "Order" = None):
        self.orderList = orderList
        self.store3 = store3
        self.order15 = order15
        
        pass
    @property
    def orderList(self):
        return self.__orderList
    @orderList.setter
    def orderList(self, orderList: Order):
        self.__orderList = orderList

    @property
    def store3(self):
        return self.__store3
    @store3.setter
    def store3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderList__store3", None)
        self.__store3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderList2"):
                opp_val = getattr(old_value, "orderList2", None)
                if opp_val == self:
                    setattr(old_value, "orderList2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderList2"):
                opp_val = getattr(value, "orderList2", None)
                setattr(value, "orderList2", self)

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderList__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderList14"):
                opp_val = getattr(old_value, "orderList14", None)
                if opp_val == self:
                    setattr(old_value, "orderList14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderList14"):
                opp_val = getattr(value, "orderList14", None)
                setattr(value, "orderList14", self)



class BackOrder:

    def __init__(self, backOrderList: Order, store1: "Store" = None, order17: set["Order"] = None):
        self.backOrderList = backOrderList
        self.store1 = store1
        self.order17 = order17 if order17 is not None else set()
        
        pass
    @property
    def backOrderList(self):
        return self.__backOrderList
    @backOrderList.setter
    def backOrderList(self, backOrderList: Order):
        self.__backOrderList = backOrderList

    @property
    def order17(self):
        return self.__order17
    @order17.setter
    def order17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BackOrder__order17", None)
        self.__order17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backOrder16"):
                    opp_val = getattr(item, "backOrder16", None)
                    
                    if opp_val == self:
                        setattr(item, "backOrder16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backOrder16"):
                    opp_val = getattr(item, "backOrder16", None)
                    
                    setattr(item, "backOrder16", self)
                    

    @property
    def store1(self):
        return self.__store1
    @store1.setter
    def store1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BackOrder__store1", None)
        self.__store1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backOrder0"):
                opp_val = getattr(old_value, "backOrder0", None)
                if opp_val == self:
                    setattr(old_value, "backOrder0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backOrder0"):
                opp_val = getattr(value, "backOrder0", None)
                setattr(value, "backOrder0", self)



class ClothesWasher:

    def __init__(self, repairPlan: str):
        self.repairPlan = repairPlan
        
        pass
    @property
    def repairPlan(self):
        return self.__repairPlan
    @repairPlan.setter
    def repairPlan(self, repairPlan: str):
        self.__repairPlan = repairPlan



class Fridge:

    def __init__(self, capacity: str):
        self.capacity = capacity
        
        pass
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity



class ClothesDryer:

    def __init__(self, repairPlan: str):
        self.repairPlan = repairPlan
        
        pass
    @property
    def repairPlan(self):
        return self.__repairPlan
    @repairPlan.setter
    def repairPlan(self, repairPlan: str):
        self.__repairPlan = repairPlan



class KitchenRange:

    pass


class Dishwasher:

    pass


class Furnace:

    def __init__(self, maximumHeatOutput: str):
        self.maximumHeatOutput = maximumHeatOutput
        
        pass
    @property
    def maximumHeatOutput(self):
        return self.__maximumHeatOutput
    @maximumHeatOutput.setter
    def maximumHeatOutput(self, maximumHeatOutput: str):
        self.__maximumHeatOutput = maximumHeatOutput



class Store:

    def __init__(self, inventory: str, customers: str, orders: str, sales: str, backOrder0: "BackOrder" = None, orderList2: "OrderList" = None, customer5: set["Customer"] = None, appliance8: set["Appliance"] = None, order10: set["Order"] = None):
        self.inventory = inventory
        self.customers = customers
        self.orders = orders
        self.sales = sales
        self.backOrder0 = backOrder0
        self.orderList2 = orderList2
        self.customer5 = customer5 if customer5 is not None else set()
        self.appliance8 = appliance8 if appliance8 is not None else set()
        self.order10 = order10 if order10 is not None else set()
        
        pass
    @property
    def sales(self):
        return self.__sales
    @sales.setter
    def sales(self, sales: str):
        self.__sales = sales

    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

    @property
    def inventory(self):
        return self.__inventory
    @inventory.setter
    def inventory(self, inventory: str):
        self.__inventory = inventory

    @property
    def customers(self):
        return self.__customers
    @customers.setter
    def customers(self, customers: str):
        self.__customers = customers

    @property
    def backOrder0(self):
        return self.__backOrder0
    @backOrder0.setter
    def backOrder0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__backOrder0", None)
        self.__backOrder0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store1"):
                opp_val = getattr(old_value, "store1", None)
                if opp_val == self:
                    setattr(old_value, "store1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store1"):
                opp_val = getattr(value, "store1", None)
                setattr(value, "store1", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__customer5", None)
        self.__customer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "store4"):
                    opp_val = getattr(item, "store4", None)
                    
                    if opp_val == self:
                        setattr(item, "store4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "store4"):
                    opp_val = getattr(item, "store4", None)
                    
                    setattr(item, "store4", self)
                    

    @property
    def orderList2(self):
        return self.__orderList2
    @orderList2.setter
    def orderList2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__orderList2", None)
        self.__orderList2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store3"):
                opp_val = getattr(old_value, "store3", None)
                if opp_val == self:
                    setattr(old_value, "store3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store3"):
                opp_val = getattr(value, "store3", None)
                setattr(value, "store3", self)

    @property
    def appliance8(self):
        return self.__appliance8
    @appliance8.setter
    def appliance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__appliance8", None)
        self.__appliance8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "store9"):
                    opp_val = getattr(item, "store9", None)
                    
                    if opp_val == self:
                        setattr(item, "store9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "store9"):
                    opp_val = getattr(item, "store9", None)
                    
                    setattr(item, "store9", self)
                    

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__order10", None)
        self.__order10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "store11"):
                    opp_val = getattr(item, "store11", None)
                    
                    if opp_val == self:
                        setattr(item, "store11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "store11"):
                    opp_val = getattr(item, "store11", None)
                    
                    setattr(item, "store11", self)
                    



class Order:

    def __init__(self, appliance: Appliance, customer: Customer, customer27: "Customer" = None, store11: "Store" = None, appliance212: set["Appliance"] = None, orderList14: "OrderList" = None, backOrder16: "BackOrder" = None):
        self.appliance = appliance
        self.customer = customer
        self.customer27 = customer27
        self.store11 = store11
        self.appliance212 = appliance212 if appliance212 is not None else set()
        self.orderList14 = orderList14
        self.backOrder16 = backOrder16
        
        pass
    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer: Customer):
        self.__customer = customer

    @property
    def appliance(self):
        return self.__appliance
    @appliance.setter
    def appliance(self, appliance: Appliance):
        self.__appliance = appliance

    @property
    def orderList14(self):
        return self.__orderList14
    @orderList14.setter
    def orderList14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderList14", None)
        self.__orderList14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order15"):
                opp_val = getattr(old_value, "order15", None)
                if opp_val == self:
                    setattr(old_value, "order15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order15"):
                opp_val = getattr(value, "order15", None)
                setattr(value, "order15", self)

    @property
    def store11(self):
        return self.__store11
    @store11.setter
    def store11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__store11", None)
        self.__store11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                if opp_val is None:
                    setattr(value, "order10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backOrder16(self):
        return self.__backOrder16
    @backOrder16.setter
    def backOrder16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__backOrder16", None)
        self.__backOrder16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order17"):
                opp_val = getattr(old_value, "order17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order17"):
                opp_val = getattr(value, "order17", None)
                if opp_val is None:
                    setattr(value, "order17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer27(self):
        return self.__customer27
    @customer27.setter
    def customer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer27", None)
        self.__customer27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order6"):
                opp_val = getattr(old_value, "order6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order6"):
                opp_val = getattr(value, "order6", None)
                if opp_val is None:
                    setattr(value, "order6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appliance212(self):
        return self.__appliance212
    @appliance212.setter
    def appliance212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__appliance212", None)
        self.__appliance212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    if opp_val == self:
                        setattr(item, "order13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    setattr(item, "order13", self)
                    

