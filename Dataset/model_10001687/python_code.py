from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer_Data:

    def __init__(self, Name: str, Contact: str, store11: "Store" = None, customer13: set["Customer"] = None, order14: "Order" = None, terminal23: set["Terminal"] = None, online_Portal37: "Online_Portal" = None):
        self.Name = Name
        self.Contact = Contact
        self.store11 = store11
        self.customer13 = customer13 if customer13 is not None else set()
        self.order14 = order14
        self.terminal23 = terminal23 if terminal23 is not None else set()
        self.online_Portal37 = online_Portal37
        
        pass
    @property
    def Contact(self):
        return self.__Contact
    @Contact.setter
    def Contact(self, Contact: str):
        self.__Contact = Contact

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def terminal23(self):
        return self.__terminal23
    @terminal23.setter
    def terminal23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Data__terminal23", None)
        self.__terminal23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer_Data22"):
                    opp_val = getattr(item, "customer_Data22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer_Data22"):
                    opp_val = getattr(item, "customer_Data22", None)
                    
                    if opp_val is None:
                        setattr(item, "customer_Data22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Data__order14", None)
        self.__order14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Data15"):
                opp_val = getattr(old_value, "customer_Data15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Data15"):
                opp_val = getattr(value, "customer_Data15", None)
                if opp_val is None:
                    setattr(value, "customer_Data15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def online_Portal37(self):
        return self.__online_Portal37
    @online_Portal37.setter
    def online_Portal37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Data__online_Portal37", None)
        self.__online_Portal37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Data36"):
                opp_val = getattr(old_value, "customer_Data36", None)
                if opp_val == self:
                    setattr(old_value, "customer_Data36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Data36"):
                opp_val = getattr(value, "customer_Data36", None)
                setattr(value, "customer_Data36", self)

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Data__customer13", None)
        self.__customer13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer_Data12"):
                    opp_val = getattr(item, "customer_Data12", None)
                    
                    if opp_val == self:
                        setattr(item, "customer_Data12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer_Data12"):
                    opp_val = getattr(item, "customer_Data12", None)
                    
                    setattr(item, "customer_Data12", self)
                    

    @property
    def store11(self):
        return self.__store11
    @store11.setter
    def store11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Data__store11", None)
        self.__store11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Data10"):
                opp_val = getattr(old_value, "customer_Data10", None)
                if opp_val == self:
                    setattr(old_value, "customer_Data10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Data10"):
                opp_val = getattr(value, "customer_Data10", None)
                setattr(value, "customer_Data10", self)



class Inventory:

    def __init__(self, Products: str, Services: str, store7: "Store" = None, terminal19: set["Terminal"] = None, online_Portal33: "Online_Portal" = None):
        self.Products = Products
        self.Services = Services
        self.store7 = store7
        self.terminal19 = terminal19 if terminal19 is not None else set()
        self.online_Portal33 = online_Portal33
        
        pass
    @property
    def Services(self):
        return self.__Services
    @Services.setter
    def Services(self, Services: str):
        self.__Services = Services

    @property
    def Products(self):
        return self.__Products
    @Products.setter
    def Products(self, Products: str):
        self.__Products = Products

    @property
    def store7(self):
        return self.__store7
    @store7.setter
    def store7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__store7", None)
        self.__store7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inventory6"):
                opp_val = getattr(old_value, "inventory6", None)
                if opp_val == self:
                    setattr(old_value, "inventory6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inventory6"):
                opp_val = getattr(value, "inventory6", None)
                setattr(value, "inventory6", self)

    @property
    def online_Portal33(self):
        return self.__online_Portal33
    @online_Portal33.setter
    def online_Portal33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__online_Portal33", None)
        self.__online_Portal33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inventory32"):
                opp_val = getattr(old_value, "inventory32", None)
                if opp_val == self:
                    setattr(old_value, "inventory32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inventory32"):
                opp_val = getattr(value, "inventory32", None)
                setattr(value, "inventory32", self)

    @property
    def terminal19(self):
        return self.__terminal19
    @terminal19.setter
    def terminal19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Inventory__terminal19", None)
        self.__terminal19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "inventory18"):
                    opp_val = getattr(item, "inventory18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "inventory18"):
                    opp_val = getattr(item, "inventory18", None)
                    
                    if opp_val is None:
                        setattr(item, "inventory18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    pass


class Employee:

    pass


class Manager:

    pass


class Store:

    pass


class Service:

    def __init__(self, Terms: str, Info: str, store43: set["Store"] = None):
        self.Terms = Terms
        self.Info = Info
        self.store43 = store43 if store43 is not None else set()
        
        pass
    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: str):
        self.__Info = Info

    @property
    def Terms(self):
        return self.__Terms
    @Terms.setter
    def Terms(self, Terms: str):
        self.__Terms = Terms

    @property
    def store43(self):
        return self.__store43
    @store43.setter
    def store43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__store43", None)
        self.__store43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service42"):
                    opp_val = getattr(item, "service42", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service42"):
                    opp_val = getattr(item, "service42", None)
                    
                    if opp_val is None:
                        setattr(item, "service42", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Product:

    def __init__(self, Company: str, store41: set["Store"] = None):
        self.Company = Company
        self.store41 = store41 if store41 is not None else set()
        
        pass
    @property
    def Company(self):
        return self.__Company
    @Company.setter
    def Company(self, Company: str):
        self.__Company = Company

    @property
    def store41(self):
        return self.__store41
    @store41.setter
    def store41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__store41", None)
        self.__store41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product40"):
                    opp_val = getattr(item, "product40", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product40"):
                    opp_val = getattr(item, "product40", None)
                    
                    if opp_val is None:
                        setattr(item, "product40", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Online_Portal:

    def __init__(self, StoreLocation: str, inventory32: "Inventory" = None, transactions34: "Transactions" = None, customer_Data36: "Customer_Data" = None, customer39: set["Customer"] = None):
        self.StoreLocation = StoreLocation
        self.inventory32 = inventory32
        self.transactions34 = transactions34
        self.customer_Data36 = customer_Data36
        self.customer39 = customer39 if customer39 is not None else set()
        
        pass
    @property
    def StoreLocation(self):
        return self.__StoreLocation
    @StoreLocation.setter
    def StoreLocation(self, StoreLocation: str):
        self.__StoreLocation = StoreLocation

    @property
    def transactions34(self):
        return self.__transactions34
    @transactions34.setter
    def transactions34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Portal__transactions34", None)
        self.__transactions34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "online_Portal35"):
                opp_val = getattr(old_value, "online_Portal35", None)
                if opp_val == self:
                    setattr(old_value, "online_Portal35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "online_Portal35"):
                opp_val = getattr(value, "online_Portal35", None)
                setattr(value, "online_Portal35", self)

    @property
    def customer39(self):
        return self.__customer39
    @customer39.setter
    def customer39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Portal__customer39", None)
        self.__customer39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "online_Portal38"):
                    opp_val = getattr(item, "online_Portal38", None)
                    
                    if opp_val == self:
                        setattr(item, "online_Portal38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "online_Portal38"):
                    opp_val = getattr(item, "online_Portal38", None)
                    
                    setattr(item, "online_Portal38", self)
                    

    @property
    def inventory32(self):
        return self.__inventory32
    @inventory32.setter
    def inventory32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Portal__inventory32", None)
        self.__inventory32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "online_Portal33"):
                opp_val = getattr(old_value, "online_Portal33", None)
                if opp_val == self:
                    setattr(old_value, "online_Portal33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "online_Portal33"):
                opp_val = getattr(value, "online_Portal33", None)
                setattr(value, "online_Portal33", self)

    @property
    def customer_Data36(self):
        return self.__customer_Data36
    @customer_Data36.setter
    def customer_Data36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Portal__customer_Data36", None)
        self.__customer_Data36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "online_Portal37"):
                opp_val = getattr(old_value, "online_Portal37", None)
                if opp_val == self:
                    setattr(old_value, "online_Portal37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "online_Portal37"):
                opp_val = getattr(value, "online_Portal37", None)
                setattr(value, "online_Portal37", self)



class Terminal:

    def __init__(self, Current_Employee: str, inventory18: set["Inventory"] = None, transactions20: set["Transactions"] = None, customer_Data22: set["Customer_Data"] = None, employee25: set["Employee"] = None, manager27: "Manager" = None):
        self.Current_Employee = Current_Employee
        self.inventory18 = inventory18 if inventory18 is not None else set()
        self.transactions20 = transactions20 if transactions20 is not None else set()
        self.customer_Data22 = customer_Data22 if customer_Data22 is not None else set()
        self.employee25 = employee25 if employee25 is not None else set()
        self.manager27 = manager27
        
        pass
    @property
    def Current_Employee(self):
        return self.__Current_Employee
    @Current_Employee.setter
    def Current_Employee(self, Current_Employee: str):
        self.__Current_Employee = Current_Employee

    @property
    def inventory18(self):
        return self.__inventory18
    @inventory18.setter
    def inventory18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Terminal__inventory18", None)
        self.__inventory18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "terminal19"):
                    opp_val = getattr(item, "terminal19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "terminal19"):
                    opp_val = getattr(item, "terminal19", None)
                    
                    if opp_val is None:
                        setattr(item, "terminal19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def manager27(self):
        return self.__manager27
    @manager27.setter
    def manager27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Terminal__manager27", None)
        self.__manager27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "terminal26"):
                opp_val = getattr(old_value, "terminal26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "terminal26"):
                opp_val = getattr(value, "terminal26", None)
                if opp_val is None:
                    setattr(value, "terminal26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transactions20(self):
        return self.__transactions20
    @transactions20.setter
    def transactions20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Terminal__transactions20", None)
        self.__transactions20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "terminal21"):
                    opp_val = getattr(item, "terminal21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "terminal21"):
                    opp_val = getattr(item, "terminal21", None)
                    
                    if opp_val is None:
                        setattr(item, "terminal21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def customer_Data22(self):
        return self.__customer_Data22
    @customer_Data22.setter
    def customer_Data22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Terminal__customer_Data22", None)
        self.__customer_Data22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "terminal23"):
                    opp_val = getattr(item, "terminal23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "terminal23"):
                    opp_val = getattr(item, "terminal23", None)
                    
                    if opp_val is None:
                        setattr(item, "terminal23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def employee25(self):
        return self.__employee25
    @employee25.setter
    def employee25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Terminal__employee25", None)
        self.__employee25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "terminal24"):
                    opp_val = getattr(item, "terminal24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "terminal24"):
                    opp_val = getattr(item, "terminal24", None)
                    
                    if opp_val is None:
                        setattr(item, "terminal24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Order:

    def __init__(self, Product: str, Service: str, customer_Data15: set["Customer_Data"] = None, transactions17: "Transactions" = None):
        self.Product = Product
        self.Service = Service
        self.customer_Data15 = customer_Data15 if customer_Data15 is not None else set()
        self.transactions17 = transactions17
        
        pass
    @property
    def Service(self):
        return self.__Service
    @Service.setter
    def Service(self, Service: str):
        self.__Service = Service

    @property
    def Product(self):
        return self.__Product
    @Product.setter
    def Product(self, Product: str):
        self.__Product = Product

    @property
    def transactions17(self):
        return self.__transactions17
    @transactions17.setter
    def transactions17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__transactions17", None)
        self.__transactions17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                if opp_val is None:
                    setattr(value, "order16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer_Data15(self):
        return self.__customer_Data15
    @customer_Data15.setter
    def customer_Data15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer_Data15", None)
        self.__customer_Data15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order14"):
                    opp_val = getattr(item, "order14", None)
                    
                    if opp_val == self:
                        setattr(item, "order14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order14"):
                    opp_val = getattr(item, "order14", None)
                    
                    setattr(item, "order14", self)
                    



class Transactions:

    def __init__(self, Customer: str, Order: str, store9: "Store" = None, order16: set["Order"] = None, terminal21: set["Terminal"] = None, online_Portal35: "Online_Portal" = None):
        self.Customer = Customer
        self.Order = Order
        self.store9 = store9
        self.order16 = order16 if order16 is not None else set()
        self.terminal21 = terminal21 if terminal21 is not None else set()
        self.online_Portal35 = online_Portal35
        
        pass
    @property
    def Order(self):
        return self.__Order
    @Order.setter
    def Order(self, Order: str):
        self.__Order = Order

    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: str):
        self.__Customer = Customer

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transactions__order16", None)
        self.__order16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transactions17"):
                    opp_val = getattr(item, "transactions17", None)
                    
                    if opp_val == self:
                        setattr(item, "transactions17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transactions17"):
                    opp_val = getattr(item, "transactions17", None)
                    
                    setattr(item, "transactions17", self)
                    

    @property
    def store9(self):
        return self.__store9
    @store9.setter
    def store9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transactions__store9", None)
        self.__store9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions8"):
                opp_val = getattr(old_value, "transactions8", None)
                if opp_val == self:
                    setattr(old_value, "transactions8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions8"):
                opp_val = getattr(value, "transactions8", None)
                setattr(value, "transactions8", self)

    @property
    def terminal21(self):
        return self.__terminal21
    @terminal21.setter
    def terminal21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transactions__terminal21", None)
        self.__terminal21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transactions20"):
                    opp_val = getattr(item, "transactions20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transactions20"):
                    opp_val = getattr(item, "transactions20", None)
                    
                    if opp_val is None:
                        setattr(item, "transactions20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def online_Portal35(self):
        return self.__online_Portal35
    @online_Portal35.setter
    def online_Portal35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transactions__online_Portal35", None)
        self.__online_Portal35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions34"):
                opp_val = getattr(old_value, "transactions34", None)
                if opp_val == self:
                    setattr(old_value, "transactions34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions34"):
                opp_val = getattr(value, "transactions34", None)
                setattr(value, "transactions34", self)

