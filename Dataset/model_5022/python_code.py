from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Product:

    pass
class ordersystem_special_LimitedEditionProduct(Product):

    def __init__(self, availableUntil: str):
        self.availableUntil = availableUntil
        
    @property
    def availableUntil(self) -> str:
        return self.__availableUntil

    @availableUntil.setter
    def availableUntil(self, availableUntil: str):
        self.__availableUntil = availableUntil

class Customer:

    pass
class ordersystem_special_PreferredCustomer(Customer):

    def __init__(self, since: str):
        self.since = since
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

class ordersystem_Address:

    def __init__(self, number: str, street: str, apartment: str, city: str, province: str, postalCode: str, country: str, ordersystem_Address: "ordersystem_Warehouse" = None, ordersystem_Address32: "ordersystem_Account" = None, ordersystem_Address35: "ordersystem_Account" = None):
        self.number = number
        self.street = street
        self.apartment = apartment
        self.city = city
        self.province = province
        self.postalCode = postalCode
        self.country = country
        self.ordersystem_Address = ordersystem_Address
        self.ordersystem_Address32 = ordersystem_Address32
        self.ordersystem_Address35 = ordersystem_Address35
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def apartment(self) -> str:
        return self.__apartment

    @apartment.setter
    def apartment(self, apartment: str):
        self.__apartment = apartment

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def province(self) -> str:
        return self.__province

    @province.setter
    def province(self, province: str):
        self.__province = province

    @property
    def ordersystem_Address32(self):
        return self.__ordersystem_Address32

    @ordersystem_Address32.setter
    def ordersystem_Address32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Address__ordersystem_Address32", None)
        self.__ordersystem_Address32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Account"):
                opp_val = getattr(old_value, "ordersystem_Account", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Account", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Account"):
                opp_val = getattr(value, "ordersystem_Account", None)
                setattr(value, "ordersystem_Account", self)

    @property
    def ordersystem_Address35(self):
        return self.__ordersystem_Address35

    @ordersystem_Address35.setter
    def ordersystem_Address35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Address__ordersystem_Address35", None)
        self.__ordersystem_Address35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Account34"):
                opp_val = getattr(old_value, "ordersystem_Account34", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Account34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Account34"):
                opp_val = getattr(value, "ordersystem_Account34", None)
                setattr(value, "ordersystem_Account34", self)

    @property
    def ordersystem_Address(self):
        return self.__ordersystem_Address

    @ordersystem_Address.setter
    def ordersystem_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Address__ordersystem_Address", None)
        self.__ordersystem_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Warehouse"):
                opp_val = getattr(old_value, "ordersystem_Warehouse", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Warehouse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Warehouse"):
                opp_val = getattr(value, "ordersystem_Warehouse", None)
                setattr(value, "ordersystem_Warehouse", self)

class ordersystem_Account:

    def __init__(self, paymentMethod: str, accountNumber: str, Account: "ordersystem_Customer" = None, account: "ordersystem_Customer" = None, ordersystem_Account: "ordersystem_Address" = None, ordersystem_Account34: "ordersystem_Address" = None):
        self.paymentMethod = paymentMethod
        self.accountNumber = accountNumber
        self.Account = Account
        self.account = account
        self.ordersystem_Account = ordersystem_Account
        self.ordersystem_Account34 = ordersystem_Account34
        
    @property
    def accountNumber(self) -> str:
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self, accountNumber: str):
        self.__accountNumber = accountNumber

    @property
    def paymentMethod(self) -> str:
        return self.__paymentMethod

    @paymentMethod.setter
    def paymentMethod(self, paymentMethod: str):
        self.__paymentMethod = paymentMethod

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Account__account", None)
        self.__account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer30"):
                opp_val = getattr(old_value, "Customer30", None)
                if opp_val == self:
                    setattr(old_value, "Customer30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer30"):
                opp_val = getattr(value, "Customer30", None)
                setattr(value, "Customer30", self)

    @property
    def ordersystem_Account34(self):
        return self.__ordersystem_Account34

    @ordersystem_Account34.setter
    def ordersystem_Account34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Account__ordersystem_Account34", None)
        self.__ordersystem_Account34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Address35"):
                opp_val = getattr(old_value, "ordersystem_Address35", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Address35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Address35"):
                opp_val = getattr(value, "ordersystem_Address35", None)
                setattr(value, "ordersystem_Address35", self)

    @property
    def ordersystem_Account(self):
        return self.__ordersystem_Account

    @ordersystem_Account.setter
    def ordersystem_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Account__ordersystem_Account", None)
        self.__ordersystem_Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Address32"):
                opp_val = getattr(old_value, "ordersystem_Address32", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Address32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Address32"):
                opp_val = getattr(value, "ordersystem_Address32", None)
                setattr(value, "ordersystem_Address32", self)

    @property
    def Account(self):
        return self.__Account

    @Account.setter
    def Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Account__Account", None)
        self.__Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner25"):
                opp_val = getattr(old_value, "owner25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner25"):
                opp_val = getattr(value, "owner25", None)
                if opp_val is None:
                    setattr(value, "owner25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ordersystem_InventoryItem:

    def __init__(self, inStock: int, restockThreshold: int, nextStockDate: str, item18: "ordersystem_Warehouse" = None, ordersystem_InventoryItem: "ordersystem_Product" = None, InventoryItem: "ordersystem_Warehouse" = None):
        self.inStock = inStock
        self.restockThreshold = restockThreshold
        self.nextStockDate = nextStockDate
        self.item18 = item18
        self.ordersystem_InventoryItem = ordersystem_InventoryItem
        self.InventoryItem = InventoryItem
        
    @property
    def nextStockDate(self) -> str:
        return self.__nextStockDate

    @nextStockDate.setter
    def nextStockDate(self, nextStockDate: str):
        self.__nextStockDate = nextStockDate

    @property
    def inStock(self) -> int:
        return self.__inStock

    @inStock.setter
    def inStock(self, inStock: int):
        self.__inStock = inStock

    @property
    def restockThreshold(self) -> int:
        return self.__restockThreshold

    @restockThreshold.setter
    def restockThreshold(self, restockThreshold: int):
        self.__restockThreshold = restockThreshold

    @property
    def InventoryItem(self):
        return self.__InventoryItem

    @InventoryItem.setter
    def InventoryItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_InventoryItem__InventoryItem", None)
        self.__InventoryItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Warehouse"):
                opp_val = getattr(old_value, "Warehouse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Warehouse"):
                opp_val = getattr(value, "Warehouse", None)
                if opp_val is None:
                    setattr(value, "Warehouse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def item18(self):
        return self.__item18

    @item18.setter
    def item18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_InventoryItem__item18", None)
        self.__item18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Warehouse19"):
                opp_val = getattr(old_value, "Warehouse19", None)
                if opp_val == self:
                    setattr(old_value, "Warehouse19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Warehouse19"):
                opp_val = getattr(value, "Warehouse19", None)
                setattr(value, "Warehouse19", self)

    @property
    def ordersystem_InventoryItem(self):
        return self.__ordersystem_InventoryItem

    @ordersystem_InventoryItem.setter
    def ordersystem_InventoryItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_InventoryItem__ordersystem_InventoryItem", None)
        self.__ordersystem_InventoryItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Product21"):
                opp_val = getattr(old_value, "ordersystem_Product21", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Product21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Product21"):
                opp_val = getattr(value, "ordersystem_Product21", None)
                setattr(value, "ordersystem_Product21", self)

class ordersystem_Warehouse:

    def __init__(self, name: str, warehouse: "ordersystem_OrderSystem" = None, Warehouse19: "ordersystem_InventoryItem" = None, Warehouse: set["ordersystem_InventoryItem"] = None, ordersystem_Warehouse: "ordersystem_Address" = None, Warehouse14: "ordersystem_OrderSystem" = None):
        self.name = name
        self.warehouse = warehouse
        self.Warehouse19 = Warehouse19
        self.Warehouse = Warehouse if Warehouse is not None else set()
        self.ordersystem_Warehouse = ordersystem_Warehouse
        self.Warehouse14 = Warehouse14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Warehouse__warehouse", None)
        self.__warehouse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderSystem4"):
                opp_val = getattr(old_value, "OrderSystem4", None)
                if opp_val == self:
                    setattr(old_value, "OrderSystem4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderSystem4"):
                opp_val = getattr(value, "OrderSystem4", None)
                setattr(value, "OrderSystem4", self)

    @property
    def Warehouse(self):
        return self.__Warehouse

    @Warehouse.setter
    def Warehouse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Warehouse__Warehouse", None)
        self.__Warehouse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InventoryItem"):
                    opp_val = getattr(item, "InventoryItem", None)
                    
                    if opp_val == self:
                        setattr(item, "InventoryItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InventoryItem"):
                    opp_val = getattr(item, "InventoryItem", None)
                    
                    setattr(item, "InventoryItem", self)
                    

    @property
    def Warehouse14(self):
        return self.__Warehouse14

    @Warehouse14.setter
    def Warehouse14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Warehouse__Warehouse14", None)
        self.__Warehouse14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner13"):
                opp_val = getattr(old_value, "owner13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner13"):
                opp_val = getattr(value, "owner13", None)
                if opp_val is None:
                    setattr(value, "owner13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Warehouse19(self):
        return self.__Warehouse19

    @Warehouse19.setter
    def Warehouse19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Warehouse__Warehouse19", None)
        self.__Warehouse19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item18"):
                opp_val = getattr(old_value, "item18", None)
                if opp_val == self:
                    setattr(old_value, "item18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item18"):
                opp_val = getattr(value, "item18", None)
                setattr(value, "item18", self)

    @property
    def ordersystem_Warehouse(self):
        return self.__ordersystem_Warehouse

    @ordersystem_Warehouse.setter
    def ordersystem_Warehouse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Warehouse__ordersystem_Warehouse", None)
        self.__ordersystem_Warehouse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Address"):
                opp_val = getattr(old_value, "ordersystem_Address", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Address"):
                opp_val = getattr(value, "ordersystem_Address", None)
                setattr(value, "ordersystem_Address", self)

class ordersystem_OrderSystem:

    def __init__(self, version: int, OrderSystem: "ordersystem_Product" = None, OrderSystem4: "ordersystem_Warehouse" = None, OrderSystem23: "ordersystem_Customer" = None, owner8: set["ordersystem_Customer"] = None, owner11: set["ordersystem_Product"] = None, owner13: set["ordersystem_Warehouse"] = None):
        self.version = version
        self.OrderSystem = OrderSystem
        self.OrderSystem4 = OrderSystem4
        self.OrderSystem23 = OrderSystem23
        self.owner8 = owner8 if owner8 is not None else set()
        self.owner11 = owner11 if owner11 is not None else set()
        self.owner13 = owner13 if owner13 is not None else set()
        
    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def owner13(self):
        return self.__owner13

    @owner13.setter
    def owner13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__owner13", None)
        self.__owner13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Warehouse14"):
                    opp_val = getattr(item, "Warehouse14", None)
                    
                    if opp_val == self:
                        setattr(item, "Warehouse14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Warehouse14"):
                    opp_val = getattr(item, "Warehouse14", None)
                    
                    setattr(item, "Warehouse14", self)
                    

    @property
    def OrderSystem4(self):
        return self.__OrderSystem4

    @OrderSystem4.setter
    def OrderSystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__OrderSystem4", None)
        self.__OrderSystem4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warehouse"):
                opp_val = getattr(old_value, "warehouse", None)
                if opp_val == self:
                    setattr(old_value, "warehouse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warehouse"):
                opp_val = getattr(value, "warehouse", None)
                setattr(value, "warehouse", self)

    @property
    def OrderSystem23(self):
        return self.__OrderSystem23

    @OrderSystem23.setter
    def OrderSystem23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__OrderSystem23", None)
        self.__OrderSystem23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if opp_val == self:
                    setattr(old_value, "customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                setattr(value, "customer", self)

    @property
    def OrderSystem(self):
        return self.__OrderSystem

    @OrderSystem.setter
    def OrderSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__OrderSystem", None)
        self.__OrderSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product"):
                opp_val = getattr(old_value, "product", None)
                if opp_val == self:
                    setattr(old_value, "product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product"):
                opp_val = getattr(value, "product", None)
                setattr(value, "product", self)

    @property
    def owner11(self):
        return self.__owner11

    @owner11.setter
    def owner11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__owner11", None)
        self.__owner11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    if opp_val == self:
                        setattr(item, "Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    setattr(item, "Product", self)
                    

    @property
    def owner8(self):
        return self.__owner8

    @owner8.setter
    def owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_OrderSystem__owner8", None)
        self.__owner8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer9"):
                    opp_val = getattr(item, "Customer9", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer9"):
                    opp_val = getattr(item, "Customer9", None)
                    
                    setattr(item, "Customer9", self)
                    

class ordersystem_Product:

    def __init__(self, name: str, sku: str, price: float, product: "ordersystem_OrderSystem" = None, ordersystem_Product: "ordersystem_LineItem" = None, ordersystem_Product21: "ordersystem_InventoryItem" = None, Product: "ordersystem_OrderSystem" = None):
        self.name = name
        self.sku = sku
        self.price = price
        self.product = product
        self.ordersystem_Product = ordersystem_Product
        self.ordersystem_Product21 = ordersystem_Product21
        self.Product = Product
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def sku(self) -> str:
        return self.__sku

    @sku.setter
    def sku(self, sku: str):
        self.__sku = sku

    @property
    def ordersystem_Product21(self):
        return self.__ordersystem_Product21

    @ordersystem_Product21.setter
    def ordersystem_Product21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Product__ordersystem_Product21", None)
        self.__ordersystem_Product21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_InventoryItem"):
                opp_val = getattr(old_value, "ordersystem_InventoryItem", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_InventoryItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_InventoryItem"):
                opp_val = getattr(value, "ordersystem_InventoryItem", None)
                setattr(value, "ordersystem_InventoryItem", self)

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Product__product", None)
        self.__product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderSystem"):
                opp_val = getattr(old_value, "OrderSystem", None)
                if opp_val == self:
                    setattr(old_value, "OrderSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderSystem"):
                opp_val = getattr(value, "OrderSystem", None)
                setattr(value, "OrderSystem", self)

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Product__Product", None)
        self.__Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner11"):
                opp_val = getattr(old_value, "owner11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner11"):
                opp_val = getattr(value, "owner11", None)
                if opp_val is None:
                    setattr(value, "owner11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordersystem_Product(self):
        return self.__ordersystem_Product

    @ordersystem_Product.setter
    def ordersystem_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Product__ordersystem_Product", None)
        self.__ordersystem_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_LineItem"):
                opp_val = getattr(old_value, "ordersystem_LineItem", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_LineItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_LineItem"):
                opp_val = getattr(value, "ordersystem_LineItem", None)
                setattr(value, "ordersystem_LineItem", self)

class ordersystem_LineItem:

    def __init__(self, quantity: int, discount: float, LineItem: "ordersystem_Order" = None, item: "ordersystem_Order" = None, ordersystem_LineItem: "ordersystem_Product" = None):
        self.quantity = quantity
        self.discount = discount
        self.LineItem = LineItem
        self.item = item
        self.ordersystem_LineItem = ordersystem_LineItem
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def discount(self) -> float:
        return self.__discount

    @discount.setter
    def discount(self, discount: float):
        self.__discount = discount

    @property
    def LineItem(self):
        return self.__LineItem

    @LineItem.setter
    def LineItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_LineItem__LineItem", None)
        self.__LineItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordersystem_LineItem(self):
        return self.__ordersystem_LineItem

    @ordersystem_LineItem.setter
    def ordersystem_LineItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_LineItem__ordersystem_LineItem", None)
        self.__ordersystem_LineItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordersystem_Product"):
                opp_val = getattr(old_value, "ordersystem_Product", None)
                if opp_val == self:
                    setattr(old_value, "ordersystem_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordersystem_Product"):
                opp_val = getattr(value, "ordersystem_Product", None)
                setattr(value, "ordersystem_Product", self)

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_LineItem__item", None)
        self.__item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order"):
                opp_val = getattr(old_value, "Order", None)
                if opp_val == self:
                    setattr(old_value, "Order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order"):
                opp_val = getattr(value, "Order", None)
                setattr(value, "Order", self)

    def getCost(self) -> float:
        # TODO: Implement getCost method
        pass

class ordersystem_Customer:

    def __init__(self, lastName: str, firstName: str, Customer: "ordersystem_Order" = None, customer: "ordersystem_OrderSystem" = None, owner25: set["ordersystem_Account"] = None, owner27: set["ordersystem_Order"] = None, Customer9: "ordersystem_OrderSystem" = None, Customer30: "ordersystem_Account" = None):
        self.lastName = lastName
        self.firstName = firstName
        self.Customer = Customer
        self.customer = customer
        self.owner25 = owner25 if owner25 is not None else set()
        self.owner27 = owner27 if owner27 is not None else set()
        self.Customer9 = Customer9
        self.Customer30 = Customer30
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Customer30(self):
        return self.__Customer30

    @Customer30.setter
    def Customer30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__Customer30", None)
        self.__Customer30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account"):
                opp_val = getattr(old_value, "account", None)
                if opp_val == self:
                    setattr(old_value, "account", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account"):
                opp_val = getattr(value, "account", None)
                setattr(value, "account", self)

    @property
    def Customer9(self):
        return self.__Customer9

    @Customer9.setter
    def Customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__Customer9", None)
        self.__Customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner8"):
                opp_val = getattr(old_value, "owner8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner8"):
                opp_val = getattr(value, "owner8", None)
                if opp_val is None:
                    setattr(value, "owner8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__customer", None)
        self.__customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderSystem23"):
                opp_val = getattr(old_value, "OrderSystem23", None)
                if opp_val == self:
                    setattr(old_value, "OrderSystem23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderSystem23"):
                opp_val = getattr(value, "OrderSystem23", None)
                setattr(value, "OrderSystem23", self)

    @property
    def owner27(self):
        return self.__owner27

    @owner27.setter
    def owner27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__owner27", None)
        self.__owner27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order28"):
                    opp_val = getattr(item, "Order28", None)
                    
                    if opp_val == self:
                        setattr(item, "Order28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order28"):
                    opp_val = getattr(item, "Order28", None)
                    
                    setattr(item, "Order28", self)
                    

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order"):
                opp_val = getattr(old_value, "order", None)
                if opp_val == self:
                    setattr(old_value, "order", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order"):
                opp_val = getattr(value, "order", None)
                setattr(value, "order", self)

    @property
    def owner25(self):
        return self.__owner25

    @owner25.setter
    def owner25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Customer__owner25", None)
        self.__owner25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    if opp_val == self:
                        setattr(item, "Account", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    setattr(item, "Account", self)
                    

class ordersystem_Order:

    def __init__(self, placedOn: str, filledOn: str, completed: bool, id: str, order: "ordersystem_Customer" = None, owner: set["ordersystem_LineItem"] = None, Order: "ordersystem_LineItem" = None, Order28: "ordersystem_Customer" = None):
        self.placedOn = placedOn
        self.filledOn = filledOn
        self.completed = completed
        self.id = id
        self.order = order
        self.owner = owner if owner is not None else set()
        self.Order = Order
        self.Order28 = Order28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def filledOn(self) -> str:
        return self.__filledOn

    @filledOn.setter
    def filledOn(self, filledOn: str):
        self.__filledOn = filledOn

    @property
    def placedOn(self) -> str:
        return self.__placedOn

    @placedOn.setter
    def placedOn(self, placedOn: str):
        self.__placedOn = placedOn

    @property
    def completed(self) -> bool:
        return self.__completed

    @completed.setter
    def completed(self, completed: bool):
        self.__completed = completed

    @property
    def Order28(self):
        return self.__Order28

    @Order28.setter
    def Order28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Order__Order28", None)
        self.__Order28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner27"):
                opp_val = getattr(old_value, "owner27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner27"):
                opp_val = getattr(value, "owner27", None)
                if opp_val is None:
                    setattr(value, "owner27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Order__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LineItem"):
                    opp_val = getattr(item, "LineItem", None)
                    
                    if opp_val == self:
                        setattr(item, "LineItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LineItem"):
                    opp_val = getattr(item, "LineItem", None)
                    
                    setattr(item, "LineItem", self)
                    

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Order__Order", None)
        self.__Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item"):
                opp_val = getattr(old_value, "item", None)
                if opp_val == self:
                    setattr(old_value, "item", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item"):
                opp_val = getattr(value, "item", None)
                setattr(value, "item", self)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ordersystem_Order__order", None)
        self.__order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)
