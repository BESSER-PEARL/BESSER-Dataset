from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class OrderCustomer:

    def __init__(self, id: int, Customer: Customer, Order: Order, order19: "Order" = None, customer21: "Customer1" = None):
        self.id = id
        self.Customer = Customer
        self.Order = Order
        self.order19 = order19
        self.customer21 = customer21
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: Customer):
        self.__Customer = Customer

    @property
    def Order(self):
        return self.__Order
    @Order.setter
    def Order(self, Order: Order):
        self.__Order = Order

    @property
    def customer21(self):
        return self.__customer21
    @customer21.setter
    def customer21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderCustomer__customer21", None)
        self.__customer21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderCustomer20"):
                opp_val = getattr(old_value, "orderCustomer20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderCustomer20"):
                opp_val = getattr(value, "orderCustomer20", None)
                if opp_val is None:
                    setattr(value, "orderCustomer20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order19(self):
        return self.__order19
    @order19.setter
    def order19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderCustomer__order19", None)
        self.__order19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderCustomer18"):
                opp_val = getattr(old_value, "orderCustomer18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderCustomer18"):
                opp_val = getattr(value, "orderCustomer18", None)
                if opp_val is None:
                    setattr(value, "orderCustomer18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Address:

    def __init__(self, House: str, Street: str, City: str, customer14: "Customer1" = None, order16: "Order" = None):
        self.House = House
        self.Street = Street
        self.City = City
        self.customer14 = customer14
        self.order16 = order16
        
        pass
    @property
    def Street(self):
        return self.__Street
    @Street.setter
    def Street(self, Street: str):
        self.__Street = Street

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def House(self):
        return self.__House
    @House.setter
    def House(self, House: str):
        self.__House = House

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__order16", None)
        self.__order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address17"):
                opp_val = getattr(old_value, "address17", None)
                if opp_val == self:
                    setattr(old_value, "address17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address17"):
                opp_val = getattr(value, "address17", None)
                setattr(value, "address17", self)

    @property
    def customer14(self):
        return self.__customer14
    @customer14.setter
    def customer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__customer14", None)
        self.__customer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address15"):
                opp_val = getattr(old_value, "address15", None)
                if opp_val == self:
                    setattr(old_value, "address15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address15"):
                opp_val = getattr(value, "address15", None)
                setattr(value, "address15", self)



class CustomerProduct:

    def __init__(self, ID: int, Customer: Customer, Product: Products, customer5: "Customer1" = None, products6: "Products" = None):
        self.ID = ID
        self.Customer = Customer
        self.Product = Product
        self.customer5 = customer5
        self.products6 = products6
        
        pass
    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: Customer):
        self.__Customer = Customer

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Product(self):
        return self.__Product
    @Product.setter
    def Product(self, Product: Products):
        self.__Product = Product

    @property
    def products6(self):
        return self.__products6
    @products6.setter
    def products6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerProduct__products6", None)
        self.__products6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerProduct7"):
                opp_val = getattr(old_value, "customerProduct7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerProduct7"):
                opp_val = getattr(value, "customerProduct7", None)
                if opp_val is None:
                    setattr(value, "customerProduct7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CustomerProduct__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customerProduct4"):
                opp_val = getattr(old_value, "customerProduct4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customerProduct4"):
                opp_val = getattr(value, "customerProduct4", None)
                if opp_val is None:
                    setattr(value, "customerProduct4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class OrderProduct:

    def __init__(self, ID: int, Oid: Order, Pid: Products, products9: "Products" = None, order11: set["Order"] = None):
        self.ID = ID
        self.Oid = Oid
        self.Pid = Pid
        self.products9 = products9
        self.order11 = order11 if order11 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Oid(self):
        return self.__Oid
    @Oid.setter
    def Oid(self, Oid: Order):
        self.__Oid = Oid

    @property
    def Pid(self):
        return self.__Pid
    @Pid.setter
    def Pid(self, Pid: Products):
        self.__Pid = Pid

    @property
    def products9(self):
        return self.__products9
    @products9.setter
    def products9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderProduct__products9", None)
        self.__products9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderProduct8"):
                opp_val = getattr(old_value, "orderProduct8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderProduct8"):
                opp_val = getattr(value, "orderProduct8", None)
                if opp_val is None:
                    setattr(value, "orderProduct8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderProduct__order11", None)
        self.__order11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orderProduct10"):
                    opp_val = getattr(item, "orderProduct10", None)
                    
                    if opp_val == self:
                        setattr(item, "orderProduct10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orderProduct10"):
                    opp_val = getattr(item, "orderProduct10", None)
                    
                    setattr(item, "orderProduct10", self)
                    



class Order:

    def __init__(self, id: int, Date: str, ProductID: Products, orderProduct10: "OrderProduct" = None, address17: "Address" = None, orderCustomer18: set["OrderCustomer"] = None):
        self.id = id
        self.Date = Date
        self.ProductID = ProductID
        self.orderProduct10 = orderProduct10
        self.address17 = address17
        self.orderCustomer18 = orderCustomer18 if orderCustomer18 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: Products):
        self.__ProductID = ProductID

    @property
    def orderProduct10(self):
        return self.__orderProduct10
    @orderProduct10.setter
    def orderProduct10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderProduct10", None)
        self.__orderProduct10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order11"):
                opp_val = getattr(old_value, "order11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order11"):
                opp_val = getattr(value, "order11", None)
                if opp_val is None:
                    setattr(value, "order11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderCustomer18(self):
        return self.__orderCustomer18
    @orderCustomer18.setter
    def orderCustomer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderCustomer18", None)
        self.__orderCustomer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order19"):
                    opp_val = getattr(item, "order19", None)
                    
                    if opp_val == self:
                        setattr(item, "order19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order19"):
                    opp_val = getattr(item, "order19", None)
                    
                    setattr(item, "order19", self)
                    

    @property
    def address17(self):
        return self.__address17
    @address17.setter
    def address17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__address17", None)
        self.__address17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if opp_val == self:
                    setattr(old_value, "order16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                setattr(value, "order16", self)



class Payment:

    def __init__(self, ID: int, Customer: Customer, Details: str, Amount: int, customer13: "Customer1" = None):
        self.ID = ID
        self.Customer = Customer
        self.Details = Details
        self.Amount = Amount
        self.customer13 = customer13
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details

    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: Customer):
        self.__Customer = Customer

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer13", None)
        self.__customer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment12"):
                opp_val = getattr(old_value, "payment12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment12"):
                opp_val = getattr(value, "payment12", None)
                if opp_val is None:
                    setattr(value, "payment12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Guest:

    pass


class Products:

    def __init__(self, ID: int, Name: str, Description: str, orderProduct8: set["OrderProduct"] = None, customerProduct7: set["CustomerProduct"] = None):
        self.ID = ID
        self.Name = Name
        self.Description = Description
        self.orderProduct8 = orderProduct8 if orderProduct8 is not None else set()
        self.customerProduct7 = customerProduct7 if customerProduct7 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def orderProduct8(self):
        return self.__orderProduct8
    @orderProduct8.setter
    def orderProduct8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__orderProduct8", None)
        self.__orderProduct8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products9"):
                    opp_val = getattr(item, "products9", None)
                    
                    if opp_val == self:
                        setattr(item, "products9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products9"):
                    opp_val = getattr(item, "products9", None)
                    
                    setattr(item, "products9", self)
                    

    @property
    def customerProduct7(self):
        return self.__customerProduct7
    @customerProduct7.setter
    def customerProduct7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Products__customerProduct7", None)
        self.__customerProduct7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "products6"):
                    opp_val = getattr(item, "products6", None)
                    
                    if opp_val == self:
                        setattr(item, "products6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "products6"):
                    opp_val = getattr(item, "products6", None)
                    
                    setattr(item, "products6", self)
                    



class Customer1:

    def __init__(self, ID: str, Name: str, Email: str, attribute: str, Password: str, payment12: set["Payment"] = None, address15: "Address" = None, customerProduct4: set["CustomerProduct"] = None, orderCustomer20: set["OrderCustomer"] = None):
        self.ID = ID
        self.Name = Name
        self.Email = Email
        self.attribute = attribute
        self.Password = Password
        self.payment12 = payment12 if payment12 is not None else set()
        self.address15 = address15
        self.customerProduct4 = customerProduct4 if customerProduct4 is not None else set()
        self.orderCustomer20 = orderCustomer20 if orderCustomer20 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def address15(self):
        return self.__address15
    @address15.setter
    def address15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__address15", None)
        self.__address15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer14"):
                opp_val = getattr(old_value, "customer14", None)
                if opp_val == self:
                    setattr(old_value, "customer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer14"):
                opp_val = getattr(value, "customer14", None)
                setattr(value, "customer14", self)

    @property
    def payment12(self):
        return self.__payment12
    @payment12.setter
    def payment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__payment12", None)
        self.__payment12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer13"):
                    opp_val = getattr(item, "customer13", None)
                    
                    if opp_val == self:
                        setattr(item, "customer13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer13"):
                    opp_val = getattr(item, "customer13", None)
                    
                    setattr(item, "customer13", self)
                    

    @property
    def customerProduct4(self):
        return self.__customerProduct4
    @customerProduct4.setter
    def customerProduct4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__customerProduct4", None)
        self.__customerProduct4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    if opp_val == self:
                        setattr(item, "customer5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    setattr(item, "customer5", self)
                    

    @property
    def orderCustomer20(self):
        return self.__orderCustomer20
    @orderCustomer20.setter
    def orderCustomer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__orderCustomer20", None)
        self.__orderCustomer20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer21"):
                    opp_val = getattr(item, "customer21", None)
                    
                    if opp_val == self:
                        setattr(item, "customer21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer21"):
                    opp_val = getattr(item, "customer21", None)
                    
                    setattr(item, "customer21", self)
                    



class Customer:

    def __init__(self, attribute: str, attribute2: str, attribute3: str, customer0: "Customer" = None, customer1: set["Customer"] = None, customer2: set["Customer"] = None, customer3: "Customer" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.customer0 = customer0
        self.customer1 = customer1 if customer1 is not None else set()
        self.customer2 = customer2 if customer2 is not None else set()
        self.customer3 = customer3
        
        pass
    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                if opp_val is None:
                    setattr(value, "customer2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer2", None)
        self.__customer2 = value if value is not None else set()
        
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
                    

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                if opp_val is None:
                    setattr(value, "customer1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customer1", None)
        self.__customer1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    if opp_val == self:
                        setattr(item, "customer0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    setattr(item, "customer0", self)
                    

