from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, CustNumber: int, order14: set["Order"] = None):
        self.CustNumber = CustNumber
        self.order14 = order14 if order14 is not None else set()
        
        pass
    @property
    def CustNumber(self):
        return self.__CustNumber
    @CustNumber.setter
    def CustNumber(self, CustNumber: int):
        self.__CustNumber = CustNumber

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order14", None)
        self.__order14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer15"):
                    opp_val = getattr(item, "customer15", None)
                    
                    if opp_val == self:
                        setattr(item, "customer15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer15"):
                    opp_val = getattr(item, "customer15", None)
                    
                    setattr(item, "customer15", self)
                    



class Vendor:

    def __init__(self, VendorID: int, ItemID: int, Address: str, purchaseOrder4: set["PurchaseOrder"] = None):
        self.VendorID = VendorID
        self.ItemID = ItemID
        self.Address = Address
        self.purchaseOrder4 = purchaseOrder4 if purchaseOrder4 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def ItemID(self):
        return self.__ItemID
    @ItemID.setter
    def ItemID(self, ItemID: int):
        self.__ItemID = ItemID

    @property
    def VendorID(self):
        return self.__VendorID
    @VendorID.setter
    def VendorID(self, VendorID: int):
        self.__VendorID = VendorID

    @property
    def purchaseOrder4(self):
        return self.__purchaseOrder4
    @purchaseOrder4.setter
    def purchaseOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vendor__purchaseOrder4", None)
        self.__purchaseOrder4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vendor5"):
                    opp_val = getattr(item, "vendor5", None)
                    
                    if opp_val == self:
                        setattr(item, "vendor5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vendor5"):
                    opp_val = getattr(item, "vendor5", None)
                    
                    setattr(item, "vendor5", self)
                    



class PurchaseOrder:

    def __init__(self, PurchaseOrderID: int, VendorID: int, ItemID: int, Quantity: float, Price: float, Date: date, vendor5: "Vendor" = None, items12: set["Items"] = None):
        self.PurchaseOrderID = PurchaseOrderID
        self.VendorID = VendorID
        self.ItemID = ItemID
        self.Quantity = Quantity
        self.Price = Price
        self.Date = Date
        self.vendor5 = vendor5
        self.items12 = items12 if items12 is not None else set()
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: float):
        self.__Price = Price

    @property
    def VendorID(self):
        return self.__VendorID
    @VendorID.setter
    def VendorID(self, VendorID: int):
        self.__VendorID = VendorID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: float):
        self.__Quantity = Quantity

    @property
    def PurchaseOrderID(self):
        return self.__PurchaseOrderID
    @PurchaseOrderID.setter
    def PurchaseOrderID(self, PurchaseOrderID: int):
        self.__PurchaseOrderID = PurchaseOrderID

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def ItemID(self):
        return self.__ItemID
    @ItemID.setter
    def ItemID(self, ItemID: int):
        self.__ItemID = ItemID

    @property
    def items12(self):
        return self.__items12
    @items12.setter
    def items12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PurchaseOrder__items12", None)
        self.__items12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "purchaseOrder13"):
                    opp_val = getattr(item, "purchaseOrder13", None)
                    
                    if opp_val == self:
                        setattr(item, "purchaseOrder13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "purchaseOrder13"):
                    opp_val = getattr(item, "purchaseOrder13", None)
                    
                    setattr(item, "purchaseOrder13", self)
                    

    @property
    def vendor5(self):
        return self.__vendor5
    @vendor5.setter
    def vendor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PurchaseOrder__vendor5", None)
        self.__vendor5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder4"):
                opp_val = getattr(old_value, "purchaseOrder4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder4"):
                opp_val = getattr(value, "purchaseOrder4", None)
                if opp_val is None:
                    setattr(value, "purchaseOrder4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Menu:

    def __init__(self, MenuItem: str, order0: "Order" = None, items6: set["Items"] = None):
        self.MenuItem = MenuItem
        self.order0 = order0
        self.items6 = items6 if items6 is not None else set()
        
        pass
    @property
    def MenuItem(self):
        return self.__MenuItem
    @MenuItem.setter
    def MenuItem(self, MenuItem: str):
        self.__MenuItem = MenuItem

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__order0", None)
        self.__order0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu1"):
                opp_val = getattr(old_value, "menu1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu1"):
                opp_val = getattr(value, "menu1", None)
                if opp_val is None:
                    setattr(value, "menu1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items6(self):
        return self.__items6
    @items6.setter
    def items6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__items6", None)
        self.__items6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu7"):
                    opp_val = getattr(item, "menu7", None)
                    
                    if opp_val == self:
                        setattr(item, "menu7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu7"):
                    opp_val = getattr(item, "menu7", None)
                    
                    setattr(item, "menu7", self)
                    



class Inventory:

    def __init__(self, ItemID: int, StoreID: int, Quantity: float, store2: set["Store"] = None, items8: set["Items"] = None):
        self.ItemID = ItemID
        self.StoreID = StoreID
        self.Quantity = Quantity
        self.store2 = store2 if store2 is not None else set()
        self.items8 = items8 if items8 is not None else set()
        
        pass
    @property
    def ItemID(self):
        return self.__ItemID
    @ItemID.setter
    def ItemID(self, ItemID: int):
        self.__ItemID = ItemID

    @property
    def StoreID(self):
        return self.__StoreID
    @StoreID.setter
    def StoreID(self, StoreID: int):
        self.__StoreID = StoreID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: float):
        self.__Quantity = Quantity

    @property
    def store2(self):
        return self.__store2
    @store2.setter
    def store2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__store2", None)
        self.__store2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory3"):
                    opp_val = getattr(item, "inventory3", None)
                    
                    if opp_val == self:
                        setattr(item, "inventory3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory3"):
                    opp_val = getattr(item, "inventory3", None)
                    
                    setattr(item, "inventory3", self)
                    

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__items8", None)
        self.__items8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory9"):
                    opp_val = getattr(item, "inventory9", None)
                    
                    if opp_val == self:
                        setattr(item, "inventory9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory9"):
                    opp_val = getattr(item, "inventory9", None)
                    
                    setattr(item, "inventory9", self)
                    



class Employee:

    def __init__(self, EmployeeID: int, Role: str, StoreID: int, Salary: float, store11: "Store" = None):
        self.EmployeeID = EmployeeID
        self.Role = Role
        self.StoreID = StoreID
        self.Salary = Salary
        self.store11 = store11
        
        pass
    @property
    def StoreID(self):
        return self.__StoreID
    @StoreID.setter
    def StoreID(self, StoreID: int):
        self.__StoreID = StoreID

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: float):
        self.__Salary = Salary

    @property
    def EmployeeID(self):
        return self.__EmployeeID
    @EmployeeID.setter
    def EmployeeID(self, EmployeeID: int):
        self.__EmployeeID = EmployeeID

    @property
    def Role(self):
        return self.__Role
    @Role.setter
    def Role(self, Role: str):
        self.__Role = Role

    @property
    def store11(self):
        return self.__store11
    @store11.setter
    def store11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__store11", None)
        self.__store11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee10"):
                opp_val = getattr(old_value, "employee10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee10"):
                opp_val = getattr(value, "employee10", None)
                if opp_val is None:
                    setattr(value, "employee10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, CustNumber: int, OrderID: int, MenuItem: int, ItemName: str, OrderDate: date, menu1: set["Menu"] = None, customer15: "Customer" = None):
        self.CustNumber = CustNumber
        self.OrderID = OrderID
        self.MenuItem = MenuItem
        self.ItemName = ItemName
        self.OrderDate = OrderDate
        self.menu1 = menu1 if menu1 is not None else set()
        self.customer15 = customer15
        
        pass
    @property
    def MenuItem(self):
        return self.__MenuItem
    @MenuItem.setter
    def MenuItem(self, MenuItem: int):
        self.__MenuItem = MenuItem

    @property
    def OrderDate(self):
        return self.__OrderDate
    @OrderDate.setter
    def OrderDate(self, OrderDate: date):
        self.__OrderDate = OrderDate

    @property
    def ItemName(self):
        return self.__ItemName
    @ItemName.setter
    def ItemName(self, ItemName: str):
        self.__ItemName = ItemName

    @property
    def CustNumber(self):
        return self.__CustNumber
    @CustNumber.setter
    def CustNumber(self, CustNumber: int):
        self.__CustNumber = CustNumber

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer15", None)
        self.__customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                if opp_val is None:
                    setattr(value, "order14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def menu1(self):
        return self.__menu1
    @menu1.setter
    def menu1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__menu1", None)
        self.__menu1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order0"):
                    opp_val = getattr(item, "order0", None)
                    
                    if opp_val == self:
                        setattr(item, "order0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order0"):
                    opp_val = getattr(item, "order0", None)
                    
                    setattr(item, "order0", self)
                    



class Store:

    def __init__(self, StoreID: int, Address: str, Name: str, inventory3: "Inventory" = None, employee10: set["Employee"] = None):
        self.StoreID = StoreID
        self.Address = Address
        self.Name = Name
        self.inventory3 = inventory3
        self.employee10 = employee10 if employee10 is not None else set()
        
        pass
    @property
    def StoreID(self):
        return self.__StoreID
    @StoreID.setter
    def StoreID(self, StoreID: int):
        self.__StoreID = StoreID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def employee10(self):
        return self.__employee10
    @employee10.setter
    def employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__employee10", None)
        self.__employee10 = value if value is not None else set()
        
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
                    

    @property
    def inventory3(self):
        return self.__inventory3
    @inventory3.setter
    def inventory3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__inventory3", None)
        self.__inventory3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store2"):
                opp_val = getattr(old_value, "store2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store2"):
                opp_val = getattr(value, "store2", None)
                if opp_val is None:
                    setattr(value, "store2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Items:

    def __init__(self, ItemID: int, Name: str, menu7: "Menu" = None, inventory9: "Inventory" = None, purchaseOrder13: "PurchaseOrder" = None):
        self.ItemID = ItemID
        self.Name = Name
        self.menu7 = menu7
        self.inventory9 = inventory9
        self.purchaseOrder13 = purchaseOrder13
        
        pass
    @property
    def ItemID(self):
        return self.__ItemID
    @ItemID.setter
    def ItemID(self, ItemID: int):
        self.__ItemID = ItemID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def purchaseOrder13(self):
        return self.__purchaseOrder13
    @purchaseOrder13.setter
    def purchaseOrder13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__purchaseOrder13", None)
        self.__purchaseOrder13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items12"):
                opp_val = getattr(old_value, "items12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items12"):
                opp_val = getattr(value, "items12", None)
                if opp_val is None:
                    setattr(value, "items12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def menu7(self):
        return self.__menu7
    @menu7.setter
    def menu7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__menu7", None)
        self.__menu7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items6"):
                opp_val = getattr(old_value, "items6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items6"):
                opp_val = getattr(value, "items6", None)
                if opp_val is None:
                    setattr(value, "items6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inventory9(self):
        return self.__inventory9
    @inventory9.setter
    def inventory9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__inventory9", None)
        self.__inventory9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items8"):
                opp_val = getattr(old_value, "items8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items8"):
                opp_val = getattr(value, "items8", None)
                if opp_val is None:
                    setattr(value, "items8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

