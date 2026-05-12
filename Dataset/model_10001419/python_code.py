from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Items:

    def __init__(self, Description: str, shopping_Cart17: "Shopping_Cart" = None):
        self.Description = Description
        self.shopping_Cart17 = shopping_Cart17
        
        pass
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def shopping_Cart17(self):
        return self.__shopping_Cart17
    @shopping_Cart17.setter
    def shopping_Cart17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__shopping_Cart17", None)
        self.__shopping_Cart17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items16"):
                opp_val = getattr(old_value, "items16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items16"):
                opp_val = getattr(value, "items16", None)
                if opp_val is None:
                    setattr(value, "items16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Warehouse:

    def __init__(self, Warehouse_branch: str, products12: set["Products"] = None):
        self.Warehouse_branch = Warehouse_branch
        self.products12 = products12 if products12 is not None else set()
        
        pass
    @property
    def Warehouse_branch(self):
        return self.__Warehouse_branch
    @Warehouse_branch.setter
    def Warehouse_branch(self, Warehouse_branch: str):
        self.__Warehouse_branch = Warehouse_branch

    @property
    def products12(self):
        return self.__products12
    @products12.setter
    def products12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Warehouse__products12", None)
        self.__products12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse13"):
                    opp_val = getattr(item, "warehouse13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse13"):
                    opp_val = getattr(item, "warehouse13", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Account:

    def __init__(self, Address: str, customer8: "Customer" = None, customer11: "Customer" = None, order19: "Order" = None, order21: "Order" = None, order22: "Order" = None):
        self.Address = Address
        self.customer8 = customer8
        self.customer11 = customer11
        self.order19 = order19
        self.order21 = order21
        self.order22 = order22
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def order22(self):
        return self.__order22
    @order22.setter
    def order22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order22", None)
        self.__order22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account23"):
                opp_val = getattr(old_value, "account23", None)
                if opp_val == self:
                    setattr(old_value, "account23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account23"):
                opp_val = getattr(value, "account23", None)
                setattr(value, "account23", self)

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
    def order21(self):
        return self.__order21
    @order21.setter
    def order21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order21", None)
        self.__order21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account20"):
                opp_val = getattr(old_value, "account20", None)
                if opp_val == self:
                    setattr(old_value, "account20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account20"):
                opp_val = getattr(value, "account20", None)
                setattr(value, "account20", self)

    @property
    def customer11(self):
        return self.__customer11
    @customer11.setter
    def customer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer11", None)
        self.__customer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account10"):
                opp_val = getattr(old_value, "account10", None)
                if opp_val == self:
                    setattr(old_value, "account10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account10"):
                opp_val = getattr(value, "account10", None)
                setattr(value, "account10", self)



class Order:

    def __init__(self, Order_ID: int, payment15: "Payment" = None, account18: "Account" = None, account20: "Account" = None, account23: "Account" = None, customer3: "Customer" = None):
        self.Order_ID = Order_ID
        self.payment15 = payment15
        self.account18 = account18
        self.account20 = account20
        self.account23 = account23
        self.customer3 = customer3
        
        pass
    @property
    def Order_ID(self):
        return self.__Order_ID
    @Order_ID.setter
    def Order_ID(self, Order_ID: int):
        self.__Order_ID = Order_ID

    @property
    def account23(self):
        return self.__account23
    @account23.setter
    def account23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account23", None)
        self.__account23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order22"):
                opp_val = getattr(old_value, "order22", None)
                if opp_val == self:
                    setattr(old_value, "order22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order22"):
                opp_val = getattr(value, "order22", None)
                setattr(value, "order22", self)

    @property
    def payment15(self):
        return self.__payment15
    @payment15.setter
    def payment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment15", None)
        self.__payment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if opp_val == self:
                    setattr(old_value, "order14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                setattr(value, "order14", self)

    @property
    def account20(self):
        return self.__account20
    @account20.setter
    def account20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account20", None)
        self.__account20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order21"):
                opp_val = getattr(old_value, "order21", None)
                if opp_val == self:
                    setattr(old_value, "order21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order21"):
                opp_val = getattr(value, "order21", None)
                setattr(value, "order21", self)

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
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                if opp_val is None:
                    setattr(value, "order2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Payment:

    def __init__(self, Payment_ID: int, Date: int, order14: "Order" = None, customer7: "Customer" = None):
        self.Payment_ID = Payment_ID
        self.Date = Date
        self.order14 = order14
        self.customer7 = customer7
        
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
    def Payment_ID(self, Payment_ID: int):
        self.__Payment_ID = Payment_ID

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment6"):
                opp_val = getattr(old_value, "payment6", None)
                if opp_val == self:
                    setattr(old_value, "payment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment6"):
                opp_val = getattr(value, "payment6", None)
                setattr(value, "payment6", self)

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order14", None)
        self.__order14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment15"):
                opp_val = getattr(old_value, "payment15", None)
                if opp_val == self:
                    setattr(old_value, "payment15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment15"):
                opp_val = getattr(value, "payment15", None)
                setattr(value, "payment15", self)



class Shopping_Cart:

    def __init__(self, Date: int, items16: set["Items"] = None, customer5: set["Customer"] = None):
        self.Date = Date
        self.items16 = items16 if items16 is not None else set()
        self.customer5 = customer5 if customer5 is not None else set()
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: int):
        self.__Date = Date

    @property
    def items16(self):
        return self.__items16
    @items16.setter
    def items16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__items16", None)
        self.__items16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_Cart17"):
                    opp_val = getattr(item, "shopping_Cart17", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_Cart17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_Cart17"):
                    opp_val = getattr(item, "shopping_Cart17", None)
                    
                    setattr(item, "shopping_Cart17", self)
                    

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__customer5", None)
        self.__customer5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_Cart4"):
                    opp_val = getattr(item, "shopping_Cart4", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_Cart4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_Cart4"):
                    opp_val = getattr(item, "shopping_Cart4", None)
                    
                    setattr(item, "shopping_Cart4", self)
                    



class Products:

    def __init__(self, Product_ID: int, warehouse13: set["Warehouse"] = None, customer1: set["Customer"] = None):
        self.Product_ID = Product_ID
        self.warehouse13 = warehouse13 if warehouse13 is not None else set()
        self.customer1 = customer1 if customer1 is not None else set()
        
        pass
    @property
    def Product_ID(self):
        return self.__Product_ID
    @Product_ID.setter
    def Product_ID(self, Product_ID: int):
        self.__Product_ID = Product_ID

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__customer1", None)
        self.__customer1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products0"):
                    opp_val = getattr(item, "products0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products0"):
                    opp_val = getattr(item, "products0", None)
                    
                    if opp_val is None:
                        setattr(item, "products0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def warehouse13(self):
        return self.__warehouse13
    @warehouse13.setter
    def warehouse13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__warehouse13", None)
        self.__warehouse13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products12"):
                    opp_val = getattr(item, "products12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products12"):
                    opp_val = getattr(item, "products12", None)
                    
                    if opp_val is None:
                        setattr(item, "products12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, Name: str, Customer_ID: int, account9: "Account" = None, account10: "Account" = None, products0: set["Products"] = None, order2: set["Order"] = None, shopping_Cart4: "Shopping_Cart" = None, payment6: "Payment" = None):
        self.Name = Name
        self.Customer_ID = Customer_ID
        self.account9 = account9
        self.account10 = account10
        self.products0 = products0 if products0 is not None else set()
        self.order2 = order2 if order2 is not None else set()
        self.shopping_Cart4 = shopping_Cart4
        self.payment6 = payment6
        
        pass
    @property
    def Customer_ID(self):
        return self.__Customer_ID
    @Customer_ID.setter
    def Customer_ID(self, Customer_ID: int):
        self.__Customer_ID = Customer_ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def shopping_Cart4(self):
        return self.__shopping_Cart4
    @shopping_Cart4.setter
    def shopping_Cart4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__shopping_Cart4", None)
        self.__shopping_Cart4 = value
        
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
    def products0(self):
        return self.__products0
    @products0.setter
    def products0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__products0", None)
        self.__products0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    if opp_val is None:
                        setattr(item, "customer1", set([self]))
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
    def account10(self):
        return self.__account10
    @account10.setter
    def account10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account10", None)
        self.__account10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer11"):
                opp_val = getattr(old_value, "customer11", None)
                if opp_val == self:
                    setattr(old_value, "customer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer11"):
                opp_val = getattr(value, "customer11", None)
                setattr(value, "customer11", self)

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)

    @property
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order2", None)
        self.__order2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    if opp_val == self:
                        setattr(item, "customer3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    setattr(item, "customer3", self)
                    

